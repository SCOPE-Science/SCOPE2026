# Independent mathematical audit

## correctness

PASS

Examined normalization carefully: S consists only of hub o and leaves v_i, with d(o,vi)=rho and d(vi,vj)=2rho, and sum-normalized BL norm = sup|f|+Lip(f). Because μ(total)=0, put y_i=f(vi)-f(o) and translate f to center its entire range; the least sup norm is (U+V)/2 with U=max(0,-inf_i y_i), V=max(0,sup_i y_i). The exact Lip constant is sup_i |y_i|/rho because leaf-leaf differences <=2sup|y_i|. Homogeneity fixes max(U,V)=1, and pairing coefficients bounds |∫f dμ| by PV+QU, valid for countable absolutely summable series. Along edges U=1 and V=1 the fractional functions have derivatives of constant sign, so only three corners matter and give rho(P+Q)/(1+rho), 2rho P/(2+rho), 2rho Q/(2+rho). Explicit centered sign potential and two one-sided potentials attain each candidate even with infinitely many leaves; check the zero family separately. Comparing values gives exact transition at ratio (1+2/rho), with ties at equalities. Independently solved sixteen finite signed examples and four arm radii by a separate linear program (all agreement within 1e-8), including balanced, unbalanced and mixed-sign coefficients; analytic proof, not LP sampling, handles arbitrary countable I.

## originality

PASS

General finite-molecule dual BL computation via LP and abstract extremal functions are known, but neither checked source provides a closed all-size/all-radius sign-mass formula with switch boundaries or countably infinite case. Best-of-knowledge O retains a risk of an unindexed elementary star specialization.

## value

PASS

Dudley/Fortet–Mourier is a canonical dual norm controlling convergence of signed finite or countable measures. An exact all-radius phase diagram on a natural star metric identifies when balanced sign potentials versus one-sided potentials are extremal, with nontrivial mass-imbalance transition 1+2/rho and explicit infinite-star attainment. This is a motivated sharp norm computation beyond a generic finite LP recipe or a single trivial molecule, even though it is special to equal arm lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
