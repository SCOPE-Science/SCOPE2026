"""Exact finite multinomial checks and numerical asymptotic checks for Shannon/richness covariance."""
import json, math
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def compositions(n, s):
    if s == 1:
        yield (n,)
        return
    for x in range(n + 1):
        for v in compositions(n - x, s - 1):
            yield (x,) + v


def binexp_frequency(p, n, k):
    return sum(F(math.comb(n, k)) * a**k * (1-a)**(n-k) for a in p)


def exact_checks(p, n):
    s = len(p)
    ek = F(0)
    ef = {k: F(0) for k in range(2, n+1)}
    ekf = {k: F(0) for k in range(2, n+1)}
    for x in compositions(n, s):
        prob = F(math.factorial(n), math.prod(math.factorial(z) for z in x))
        for a,z in zip(p,x):
            prob *= a**z
        nr = sum(z > 0 for z in x)
        ek += prob * nr
        for k in range(2,n+1):
            freq = x.count(k)
            ef[k] += prob * freq
            ekf[k] += prob * nr * freq
    assert ek == sum(1-(1-a)**n for a in p)
    assert all(ef[k] == binexp_frequency(p,n,k) for k in ef)
    for k in range(2,n+1):
        lhs = ekf[k] - ek*ef[k]
        rhs = F(0)
        for i,a in enumerate(p):
            q = tuple(b/(1-a) for j,b in enumerate(p) if j != i)
            rhs += (1-a)**n * (binexp_frequency(p,n,k)-binexp_frequency(q,n,k))
        assert lhs == rhs, (p,n,k,lhs,rhs)
    return n-1


def mean_entropy(p,n):
    sm = 0.0
    for a in p:
        sm += sum(math.comb(n,k)*a**k*(1-a)**(n-k)*k*math.log(k)
                  for k in range(2,n+1))
    return math.log(n)-sm/n


def entropy(p):
    return -sum(float(a)*math.log(float(a)) for a in p)


def asymptotic_record(p,n):
    t=min(p); m=sum(a==t for a in p)
    ip=p.index(t)
    q=[a/(1-t) for i,a in enumerate(p) if i != ip]
    delta=entropy(p)-entropy(q)
    cov=sum((1-a)**n*(mean_entropy(p,n)-mean_entropy([b/(1-a) for j,b in enumerate(p) if j!=i],n)) for i,a in enumerate(p))
    normalized=cov / (m*(1-t)**n)
    return {'n':n, 'covariance':cov, 'normalized':normalized, 'limit_delta':delta,
            'first_correction_estimate': (normalized-delta)*n,
            'expected_first_correction':-0.5}


def run():
    profiles=[(F(1,2),F(1,3),F(1,6)),
              (F(1,3),F(1,3),F(1,3)),
              (F(1,2),F(1,4),F(1,4)),
              (F(1,10),F(3,10),F(6,10)),
              (F(1,8),F(1,8),F(1,4),F(1,2))]
    identities=0
    for p in profiles:
        for n in range(2,10):
            identities += exact_checks(p,n)
    examples=[{'probabilities':list(map(str,p)),
               'asymptotics':[asymptotic_record(tuple(map(float,p)),n) for n in (80,160)]}
              for p in (profiles[0],profiles[1],profiles[3])]
    payload={'status':'verified','method':'exact rational multinomial partition enumeration and independent binomial conditional-frequency identity; float asymptotics are diagnostic only',
             'profiles_tested':len(profiles),'sample_sizes':list(range(2,10)),
             'exact_log_coefficients_checked':identities,'asymptotic_diagnostics':examples,
             'limits':'Exact finite tests are not an infinite proof. Asymptotics follow from the analytic argument in RESULT.md.'}
    return payload

if __name__=='__main__':
    cert=run()
    path=Path(__file__).with_name('certificate.json')
    if path.exists():
        assert json.loads(path.read_text(encoding='utf-8'))==cert
        print('certificate_reproduced')
    else:
        path.write_text(json.dumps(cert,indent=2,sort_keys=True,allow_nan=False)+'\n',encoding='utf-8')
        print('certificate_created')
    print('exact_log_coefficients_checked',cert['exact_log_coefficients_checked'])
