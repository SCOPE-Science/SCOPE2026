# Independent mathematical audit

## correctness

PASS

Verified source Definition 2.2 and Remark 2.1 exactly: Parseval K-frame means Σ_j|<x,f_j>|²=||K*x||² so S=KK*. In C², K=diag(1,0), F={e1} has equality for all x; S has spectrum {1,0}, energies Σ||f_j||²=1, while 2||K*e1||²=2 and 2||K*e2||²=0, contradicting both printed claims. Spectral trace gives Σ_j||f_j||²=tr(KK*)=Σ_k||K*e_k||² for every ON eigenbasis; simultaneous equality to n times each eigenvalue iff all eigenvalues coincide (KK*=cI). Strict positivity iff K* injective. Exact finite operator computation, no probabilistic or formal-checker assumptions.

## originality

PASS

Bounded corrective novelty: the target published paper explicitly states general S=KK* and warns a K-frame operator need not be invertible, yet Proposition 2.2 separately asserts universally positive eigenvalues and an unsupported eigenvectorwise formula. The audited contribution is the *specific published-proposition correction*, minimal witnessing projection and sharp equality criterion, not novelty of the standard trace identity or spectral theorem. Related Resultary correction to the same paper concerns distinct Theorem 3.3 and its noncanonical subspace map, not Proposition 2.2; no indexed prior formal correction of the latter located.

## value

PASS

A pinpointed refutation of a citable published proposition and its immediate published equal-norm consequence prevents reuse of a false eigenvaluewise equality; the replacement trace formula and exact flat-spectrum criterion delimit valid downstream applications. Its mathematical content is elementary and should not be inflated into a broad new K-frame theorem; the concrete literature error and affected consequence supply the substantive motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
