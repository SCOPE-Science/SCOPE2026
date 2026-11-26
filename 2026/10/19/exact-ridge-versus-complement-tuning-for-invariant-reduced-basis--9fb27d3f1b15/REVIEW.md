# Independent mathematical audit

## correctness

PASS

Invariance and self-adjointness reduce A and S into the same orthogonal blocks. After dividing by alpha, the Type-I extreme quotient is max(b+s,d)/min(a+s,c), s=1/alpha>0. If c<=a, the denominator stays c and a plateau at the limiting value exists exactly for 0<s<=d-b when d>b. If c>a, the quotient strictly decreases up to c-a: d/(a+s) decreases, and (b+s)/(a+s) also decreases unless b=a, in which case it is 1 and the former dominates to the breakpoint. To the right, the denominator is fixed, with the optimum attained exactly through max(c-a,d-b). Type II leaves one normalized block value 1 and the range [alpha c,alpha d] on the other block; equality with d/c is exactly inclusion of 1. These arguments include singleton spectra and all endpoint equalities. For A=diag(K,1), the condition numbers are K+1/alpha and, at alpha=1 for Type II, 1. Independent exact rational checks: 784 endpoint quadruples and 28,224 reciprocal parameter comparisons of both methods; replay: python3 /workspace/branches/independent_checks.py 2. The finite check does not replace the proof.

## originality

PASS

Credit the preconditioners and invariant-block spectral reduction as known methods. The defensible distinct claim is the joint exact scalar classification for this objective, in particular the sharp Type-I improvement and attainment conditions versus Type II; no equivalent or stronger coverage was established in the material inspected. The Type-II spectral band inclusion by itself is an elementary observation, not a standalone novelty claim.

## value

PASS

These are two existing algorithmic choices on a naturally spectral benchmark. The full classification answers when ridge tuning actually helps, identifies when its best value is only a limit, and supplies an unbounded quantitative separation from complement-only tuning even for a two-eigenvalue SPD system. The decision boundary and failure witness, not the routine spectral decomposition, give this narrow comparison its use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
