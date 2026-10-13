import math

def t_value(x, tau, sigma):
    return math.sqrt(1.0 + (x-tau)/sigma) - 1.0

def lambda_hat(xs, sigma):
    tau=min(xs)
    S=sum(t_value(x,tau,sigma) for x in xs)
    return len(xs)/S

def profile_loglik(xs, sigma):
    tau=min(xs)
    n=len(xs)
    S=sum(t_value(x,tau,sigma) for x in xs)
    lam=n/S
    return (
        n*math.log(n/S)-n-n*math.log(2*sigma)
        -0.5*sum(math.log(1+(x-tau)/sigma) for x in xs)
    )

def direct_loglik(xs, sigma):
    tau=min(xs)
    lam=lambda_hat(xs,sigma)
    total=0.0
    for x in xs:
        total += (
            math.log(lam)-math.log(2*sigma)
            -0.5*math.log(1+(x-tau)/sigma)
            -lam*t_value(x,tau,sigma)
        )
    return total

def check_sample(xs, k, expected_step):
    vals=[]
    for j in range(2,10):
        sigma=10.0**(-j)
        p=profile_loglik(xs,sigma)
        d=direct_loglik(xs,sigma)
        assert abs(p-d) < 1e-10
        vals.append((sigma,p,lambda_hat(xs,sigma)))
    for a,b in zip(vals[-4:-1],vals[-3:]):
        increment=b[1]-a[1]
        assert abs(increment-expected_step) < 0.02
    tau=min(xs)
    C=sum(math.sqrt(x-tau) for x in xs if x>tau)
    target=len(xs)/C
    sigma,p,lam=vals[-1]
    assert abs(lam/math.sqrt(sigma)-target) < 0.01
    return vals, target

unique, target1=check_sample([1.0,2.0,5.0],1,0.5*math.log(10))
tied, target2=check_sample([1.0,1.0,2.0,5.0],2,math.log(10))

assert unique[-1][1] > unique[0][1]
assert tied[-1][1] > tied[0][1]

print("VERIFY_OK")
print("unique_min_target_lambda_over_sqrt_sigma", format(target1, ".15f"))
for row in unique:
    print("unique", "sigma", f"{row[0]:.1e}", "ell", f"{row[1]:.12f}", "lambda", f"{row[2]:.12g}")
print("two_min_target_lambda_over_sqrt_sigma", format(target2, ".15f"))
for row in tied:
    print("tied", "sigma", f"{row[0]:.1e}", "ell", f"{row[1]:.12f}", "lambda", f"{row[2]:.12g}")
