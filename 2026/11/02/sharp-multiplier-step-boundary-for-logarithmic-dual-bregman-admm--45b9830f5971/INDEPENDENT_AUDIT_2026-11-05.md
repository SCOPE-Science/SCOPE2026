# Independent mathematical audit

## correctness

PASS

PASS: For any positive marginals a,b on m,n>=2, rho>0, nonconstant column-only C_ij=c_j, feasible X^0=ab^T and Z^0=0, column normalization of rank-one X^k and column-constant multiplier makes Y^{k+1}=ab^T exactly. Dual contrasts evolve by subtracting s(c_j-c_l)(1-s)^{k-1}. Geometric summation gives Z^k_j-Z^k_l=-(c_j-c_l)(1-(1-s)^{k-1}); row normalization gives exact softmax X^k_ij=a_i b_j exp[-c_j(1-s)^{k-1}/rho]/sum b exp. If 0<s<2, summable increments show full multiplier convergence and first-order nonconstant softmax derivative gives exact asymptotic factor |1-s| for s≠1; s=1 reaches balanced coupling at X². At s=2, sign alternation gives distinct positive two-cycle; s>2 softmax polarizes to disjoint argmin/argmax-cost supports along alternating parity, dual contrasts diverge. Positivity and gauge normalizations hold at every finite k. Independent numerical replay of 25 checks corroborated; proof is exact algebra.

## originality

PASS

PASS, qualified best-of-knowledge: exact final mathematical statement checked against the identified primary literature and published-finding records; no decisive covering theorem identified in material actually read; historical uncertainties are explicit below.

## value

PASS

PASS: A genuine sharpness counterexample for a published sufficient step-size interval matters for guaranteed convergence of a natural transport splitting method. The cost is additive so objective degenerate, but this explicitly isolates an instability of dual-relaxation mechanism under exact positive feasible starts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
