#!/usr/bin/env python3
import mpmath as mp
mp.mp.dps = 80

def eh(t):
    return mp.digamma(t+1)-mp.digamma(1)

def vh(t):
    return t/(t+1)**2 + mp.polygamma(1,2)/(t+1) - mp.polygamma(1,t+2)

def beta_inc(t,n):
    same = t/((t+n)*(t+n+1))*(mp.digamma(t+n+2)-mp.digamma(2))
    diff = t/(t+n+1)**2 + t/(t+n+1)*eh(t)
    return same + diff - t/(t+n)*eh(t)

def closed_inc(t,n):
    return t/((t+n)*(t+n+1))*(mp.digamma(t+n+1)-mp.digamma(t+1))

def cov_sum(t,n):
    if n <= 1:
        return mp.mpf("0")
    a = mp.fsum(1/(t+k)**2 for k in range(1,n))
    b = mp.fsum(1/(t+k) for k in range(1,n))
    return t*(a-b/(t+n))

def cov_special(t,n):
    if n <= 1:
        return mp.mpf("0")
    return t*(mp.polygamma(1,t+1)-mp.polygamma(1,t+n)
              -(mp.digamma(t+n)-mp.digamma(t+1))/(t+n))

def var_k(t,n):
    return (t*(mp.digamma(t+n)-mp.digamma(t))
            -t*t*(mp.polygamma(1,t)-mp.polygamma(1,t+n)))

def cov_limit(t):
    return t*mp.polygamma(1,t+1)

def scaled_corr_limit(t):
    return mp.sqrt(t)*mp.polygamma(1,t+1)/mp.sqrt(vh(t))

def close(a,b,tol=mp.mpf("1e-55")):
    assert abs(a-b) <= tol*max(1,abs(a),abs(b)), (a,b)

def run():
    thetas=[mp.mpf(x) for x in ("0.05","0.2","0.5","1","2","5","20")]
    beta_checks=closed_checks=monotone_checks=0
    for t in thetas:
        cumulative=mp.mpf("0")
        previous=mp.mpf("0")
        for n in range(1,121):
            a=beta_inc(t,n); b=closed_inc(t,n)
            close(a,b)
            assert b>0
            beta_checks+=1
            cumulative += b
            c=cov_sum(t,n+1)
            close(cumulative,c)
            close(c,cov_special(t,n+1))
            assert c>previous
            previous=c
            closed_checks+=2
            monotone_checks+=1
        assert vh(t)>0

    saturation_checks=0
    huge=mp.mpf(10)**50
    for t in thetas:
        c=cov_special(t,huge)
        target=cov_limit(t)
        assert 0 < target-c
        assert (target-c)/target < mp.mpf("0.01")
        saturation_checks+=1

    scaled_checks=0
    for t in [mp.mpf(x) for x in ("0.1","0.5","1","3","10")]:
        n=huge
        rho=cov_special(t,n)/mp.sqrt(var_k(t,n)*vh(t))
        scaled=mp.sqrt(mp.log(n))*rho
        target=scaled_corr_limit(t)
        assert abs(scaled-target)/target < mp.mpf("0.02")
        scaled_checks+=1

    print(
        "VERIFY_OK "
        f"beta_increment_checks={beta_checks} "
        f"closed_form_checks={closed_checks} "
        f"monotonicity_checks={monotone_checks} "
        f"saturation_checks={saturation_checks} "
        f"scaled_correlation_checks={scaled_checks}"
    )

if __name__ == "__main__":
    run()
