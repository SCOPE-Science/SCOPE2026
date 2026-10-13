import math

def log_target_nu(nu, gamma, eta, xi, xs, ys):
    if nu <= 0 or gamma <= 0 or eta <= 0 or xi <= 0:
        return float("-inf")
    N = len(xs) + len(ys)
    out = (N-1)*math.log(nu)
    out -= nu*(sum(math.log(x) for x in xs) + sum(math.log(y) for y in ys))
    out -= (gamma+1)*sum(math.log1p((x**(-nu))/xi) for x in xs)
    out -= (eta+1)*sum(math.log1p((y**(-nu))/xi) for y in ys)
    return out

gamma, eta, xi = 1.2, 1.8, 0.9
xs = [0.7, 1.3, 2.0]
ys = [0.8, 1.7]
old, new = 0.7, 1.0
var = 0.04

lo = log_target_nu(old, gamma, eta, xi, xs, ys)
ln = log_target_nu(new, gamma, eta, xi, xs, ys)
target_ratio = math.exp(ln-lo)
correct_accept = min(1.0, target_ratio)

# Natural proposal-density reading of the printed ratio:
# normal density at the proposed displacement divided by its modal density.
proposal_only = math.exp(-((new-old)**2)/(2*var))

assert abs(target_ratio - 3.8446793062664217) < 1e-12
assert correct_accept == 1.0
assert abs(proposal_only - 0.32465246735834974) < 1e-15
assert abs(correct_accept - proposal_only) > 0.6

# Detailed-balance obstruction. For a symmetric proposal q and symmetric
# displacement-only acceptance a, q and a cancel from forward/reverse flux.
q = math.exp(-((new-old)**2)/(2*var))/math.sqrt(2*math.pi*var)
a = proposal_only
pi_old = math.exp(lo)
pi_new = math.exp(ln)
forward = pi_old*q*a
reverse = pi_new*q*a
assert abs(reverse/forward - target_ratio) < 1e-13
assert abs(forward-reverse) > 1e-8

# The target ratio changes when conditioning parameters change, while a
# displacement-only proposal ratio does not.
lo2 = log_target_nu(old, 2.2, 0.9, 1.4, xs, ys)
ln2 = log_target_nu(new, 2.2, 0.9, 1.4, xs, ys)
target_ratio2 = math.exp(ln2-lo2)
assert abs(target_ratio2-target_ratio) > 1e-2
assert proposal_only == math.exp(-((new-old)**2)/(2*var))

print("VERIFY_OK")
print("target_ratio", format(target_ratio, ".15f"))
print("correct_accept", format(correct_accept, ".15f"))
print("proposal_only", format(proposal_only, ".15f"))
print("flux_ratio_reverse_over_forward", format(reverse/forward, ".15f"))
print("second_target_ratio", format(target_ratio2, ".15f"))
