# Self-review

## Correctness — PASS

The exact result is proved for every finite number of types, arbitrary positive individual fractions, and every nonnegative matrix with the stated row sums and detailed balance. The proof reconstructs the weighted self-adjoint Rayleigh principle, obtains an exact two-dimensional compression at the aggregate cross-flux, proves strict rank-one monotonicity when the two rates differ, and constructs an irreducible optimizer. Equality in the Rayleigh principle forces the classwise cross-row-sum conditions and gives the full class of minimizers. At equal rates the constant row-sum identity handles the boundary. The four-type witness has exact rational row sums and reciprocity and spectral root \((1+\sqrt{13})/5\). `checks/verify.py` was run successfully on actual package content; its finite spectral spot checks are not treated as the proof. No requirement of a zero diagonal is assumed or silently added.

## Originality — PASS, with priority risk

The closest primary source is Bizzotto–Ball–Britton (arXiv:2602.23885v2). Its Theorem 3.2 gives general nonsharp explicit bounds, its Theorem 3.6 solves the **two-type** sharp bound, and Section 8.1 provides an exact **general numerical semidefinite program**. These are acknowledged as genuine stronger computational coverage of the underlying optimization: novelty is **not** claimed for the existence of a general minimization algorithm or for the two-type quadratic formula. The present analytical statement concerns arbitrarily many fine types in precisely two row-total classes, including unequal individual fractions and arbitrary non-lumpable feasible contacts; it provides explicit sharp attainment and a necessary-and-sufficient **all-optimizer** lumpability classification. No equivalent theorem was found among inspected relevant sections or targeted mathematical-record and literature searches. The result is an explicit evaluation and optimizer rigidity consequence of a known broader optimization framework, so a classical matrix result or a short unreported implication of the source remains a material priority risk.

## Value — PASS

The motivating study treats partially known contact matrices, and its real-data illustration subdivides broad age classes by activity. When only two distinct activity totals are known but the types have been further divided, the theorem replaces a many-variable semidefinite optimization with a closed two-by-two formula **without assuming lumpable contacts**, while also completely characterizing equality. The explicit four-type construction shows that a contact class with rate above one need not prevent a subcritical reciprocal overall network. This is a natural complete multitype classification and a sharp public-health threshold statement, not merely a recomputation of a preselected example. Its role is limited to the spectral threshold and does not predict finite epidemic outcomes.

## Closest literature and limitations

Bizzotto, Ball and Britton, arXiv:2602.23885v1/v2 (full relevant results and computational appendix materially inspected); Britton and Ball, arXiv:2408.07298 (social-contact heterogeneity motivation and abstract); O'Clery et al., *Physical Review E* 88 (2013), 042805 (equitable-partition background, abstract only). Further historical priority checking is warranted because the SDP may have a previously documented closed-form two-rate reduction. The theorem allows nonnegative diagonal entries and no prescribed network topology; zero-diagonal and more-than-two-rate problems remain unresolved here.

Self-review: passed. Independent audit: not yet performed.
