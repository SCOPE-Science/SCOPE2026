# Independent mathematical audit

## correctness

PASS

The original source incorrectly claimed uniqueness of an eligible sorted index. Independent counterexample a=(1,1), G=(1,3), g=2 yields tau_1=B1/A1=3 and tau_2=B2/A2=3, so both k=1 and k=2 meet rho_k<=tau_k<=rho_(k+1). This refutes the stated index uniqueness, but not the optimization. Fully corrected RESULT.md, REVIEW.md and VERIFICATION.md replace that assertion with the first eligible k convention and explicit tie handling. In logarithmic variables y=log r the objective is strictly convex (the g>0 term gives the second log-sum-exp a zero exponent vector) and coercive; KKT yields r_i=max(1,sqrt(rho_i/tau)), sorted clamping, and tau=B_k/A_k. The weighted-average recurrence proves existence of the first admissible k. All admissible indices describe the same unique r, and minimum (sqrt(Ak Bk)+sum_{i>k}sqrt(a_i G_i))^2; ceiling increases only first factor by <=2. At the tie example F(1,1)=12, exactly both formulas. Full final scientific files were created with exact original blob guards and UTF-8 SHA-256, and the corrected final claim was reassessed.

## originality

PASS

Low arXiv:2610.01125v1 announces a general resource model and gives Eq. (7.51) as the leading objective (from the source package and arXiv abstract); the exact lower-bounded threshold and ceiling bound are not in the accessible abstract. A full independent read of Low's same paper was blocked at both arXiv PDF/HTML and institutional retrieval, so its exact Eq. (7.51) discussion is a material priority risk, not a fabricated full-text comparison. Prior generic water-filling/KKT theory may imply the same closed form under optimization aliases; the practical exact expression for the particular leading proxy still passes a bounded best-of-knowledge novelty judgment with the risk stated. Jing et al. arXiv:2610.03393 treats distinct query-complexity objectives.

## value

PASS

The structural continuous solution changes the source's constant-factor leading proxy into an exact computable allocation, pinpoints which oracle components must be queried every step, and bounds ceiling-rounding loss. The mathematical motivation is the concrete gate-cost resource tradeoff, not a claim that KKT alone is novel or a solution of the full precision-aware circuit program.

The dated certificate retains the supplied scientific assessment, sources and limitations.
