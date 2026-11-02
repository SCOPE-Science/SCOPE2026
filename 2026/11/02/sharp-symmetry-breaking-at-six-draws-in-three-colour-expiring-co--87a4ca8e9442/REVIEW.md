# Self-review

## Correctness — PASS

The new-entry characterization yields exact identity (1) by conditioning on the unique absent colour in the overlapping windows. Symmetric reductions for lengths three through six were derived and cross-checked against independent complete word enumeration. Strict Schur concavity for three, four and five symbols' window lengths follows from explicit strictly positive transfer factors. The general Hessian formula has a positive coefficient for every length at least six, proved using a positive-base induction. At length six, Lagrange stationary-point arguments reduce interior optima to a two-equal-coordinate branch; a strictly convex quartic isolates the two asymmetric candidates, and a transverse perturbation eliminates the wrong branch. Boundary flux is zero, and the remaining branch is the unique global optimum up to permutation. The machine checker independently passed 43 exact-symbolic assertions; it is not used as an infinite proof.

## Originality — PASS (subject to historical priority)

The closest full-text source is Long, arXiv:2604.26298v1, Theorem 3.1, deriving the uniform entry flux but not optimizing stationary entry rates over sampling weights. A prior fixed-alphabet nonuniform asymptotic result concerns \(M\to\infty\) and does not imply the exact change at \(M=6\), the unique low-window uniform regime, or the length-six global optimum. Nonuniform coupon coverage works investigate other, principally monotone statistics. Search of indexed research records, title/abstract literature and the source paper's accessible main text found no direct coverage of the sharp three-type finite-window boundary. Residual historical-priority risk remains because no search establishes exhaustive uniqueness.

## Mathematical value — PASS

For three symbols, unlike two, the expired-window completion problem is nondegenerate. The exact boundary \(M=5\) versus \(M=6\) identifies the first duration at which balanced sampling ceases to maximize the natural stationary *entry rate*, a quantity central to rare-entry approximations. The result gives all finite-horizon global maximizers at that first transition and a general all-longer-window local obstruction. The assertion is stronger than a numerical counterexample or the existing eventual large-window asymptotic.

## Limits and nearest literature

No statement is made about globally optimal nonuniform weights for arbitrary window lengths above six, nor about finite-size first-hit time optimization. Published source comparisons include Long's uniform-window theorem, the clumsy/careless related-model paper, and classical monotone nonuniform/structured coupon-covering work. Some tangential papers were accessible only through abstracts and could not be assessed as full-text noncoverage; these remain stated priority risks.

Self-review: passed. Independent audit: not yet performed.
