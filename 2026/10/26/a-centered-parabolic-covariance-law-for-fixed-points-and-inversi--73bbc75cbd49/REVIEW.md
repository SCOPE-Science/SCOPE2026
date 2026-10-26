# Self-review

## Correctness — PASS
For any fixed position, deleting its one-cycle leaves Ewens(theta) on n-1 labels. Every non-fixed image has marginal probability 1/(theta+n-2). This yields conditional inversion mean M_{n-1}+2(i-1)(n-i)/(theta+n-2); combine with exact known M_n and Pr(fixed)=theta/(theta+n-1), then factor. All denominators positive at n>=3, theta>0. The nonstandard marked-point reduction and rational factorization were checked independently by exact Ewens-weight permutation enumeration through n=8, 5 rational parameters, and algebraic tests through n=150; the general proof is the deletion/marginal argument, not the finite tests.

## Originality — PASS (bounded literature review)
A specific-index conditional covariance is not the same as conditioning on the TOTAL fixed-point count. The closest full primary text (Pinsky-Schickentanz 2025) proves the unconditioned mean and total-count-conditional inversion probabilities, and Pinsky 2025 proves total-count-conditional means for uniform permutations. The known mean is acknowledged as a premise. Actual semantic searches of public mathematics results and a dedup comparison against accessible prior exact findings revealed only distinct cycle-count/inversion and fixed-point/descent work; no inspected stronger result entails the exact indexed sign law without the new marked-cycle deletion calculation. Earlier undiscovered statements remain a priority risk.

## Value — PASS
The sign of covariance with the same global statistic changes across positions within one permutation exactly when theta<1, with an explicit centered parabolic law and a sqrt(n)-scale crossing window; at theta=1 the unique central zero is explicit, and for theta>1 every position has negative covariance. This complete natural dependence classification quantifies why marking a central fixed point is different from forcing an endpoint fixed point, a motivated refinement of previously studied aggregate inversion/fixed-point dependence.

## Closest literature and risks
Pinsky–Schickentanz (arXiv:2510.20654v2) gives the unconditional inversion mean and full-count conditioning; Pinsky (arXiv:2505.02058v1) gives the uniform fixed-count counterpart; Özdemir (arXiv:1811.02039v1) concerns Ewens random-walk mixing. No claim is made that historical priority is independently established. The theorem does not extend to joint distribution or independence.

Self-review: passed. Independent audit: not yet performed.
