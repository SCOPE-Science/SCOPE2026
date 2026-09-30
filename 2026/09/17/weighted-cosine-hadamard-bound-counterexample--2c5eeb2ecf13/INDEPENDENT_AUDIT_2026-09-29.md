# Independent audit — 2026-09-29

**Record:** `2026/09/17/weighted-cosine-hadamard-bound-counterexample--2c5eeb2ecf13`  
**Audited source tree:** `761c05992e441311ce266e0e258077d8df9ad866`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** **PASSED**

## Correctness — PASS

PASS. I independently recomputed the exact algebra. The displayed U is orthogonal and U diag(3,1,1/3) U^T equals [[5/3,-2/3,2/3],[-2/3,4/3,-1],[2/3,-1,4/3]]. Hence the squared off-diagonal correlations are 1/5,1/5,9/16, giving ||C||_F^2=197/40. The effective dimension is gamma=13/7, so 9/gamma=63/13 and the exact violation is 41/520. Symbolic simplification for Sigma_t=diag(t,1,t^-1) reproduces the filed factorization 18(t-1)^2(2t^3-t^2-4)/((t+2)(t^2+t+1)(2t^2+t+3)^2); the cubic is 1/2 at t=3/2 and increasing thereafter. The order-four embedding gives gamma=20/7 and gap 13/40. I also rederived the n=2 proof: each normalized weighted frame has a 2x2 Gram matrix G_W with trace two and determinant at least 4ab/(a+b)^2, so writing G_W=I+A_W and applying Frobenius Cauchy--Schwarz yields ||C(U,V)||_F^2<=4(a^2+b^2)/(a+b)^2=4/gamma, with equality at a common 45-degree frame. Thus n=3 is indeed the first real dimension in which the proposed bound can fail.

## Originality — PASS

PASS, to the best of current evidence. Loe--Huang--Needell's September 2026 manuscript presents the n^2/gamma inequality as a numerically suggested Appendix-A conjecture and does not prove a global Hadamard maximizer. A current open-problem index still lists exactly that conjecture, and searches found no erratum, comment, or independent counterexample preceding the record. Classical Benedetto--Fickus frame-potential theory concerns minimization/tight frames and does not imply this spectrum-dependent upper bound. The record's exact dimension-three witness, open spectral family, minimal-dimension theorem, and order-four embedding therefore appear original.

## Scientific value — PASS

PASS. The result directly falsifies a concrete structural conjecture in a current numerical-linear-algebra paper, proves the failure is robust rather than numerical noise, and pins down the exact first possible dimension. Showing failure also at order four rules out the tempting explanation that dimension three is exceptional only because no real Hadamard matrix exists. These facts materially constrain any corrected weighted-coherence bound.

## Sources checked

- https://arxiv.org/abs/2609.17947 — Loe, Huang and Needell, A Geometric View of Adaptive Cross Approximation via Exterior Algebra; source of the weighted-cosine/Hadamard conjecture.
- https://arxiv.org/abs/2112.02916 — Mixon, Needham, Shonkwiler and Villar, modern account of the Benedetto--Fickus frame-potential theorem; relevant background but not coverage of the upper-bound conjecture.
- https://www.emergentmind.com/open-problems/weighted-cosine-frobenius-norm-hadamard-conjecture — Current open-problem index reproducing the conjecture and noting that the source manuscript provides numerical evidence rather than a proof.

## Limitations

- The result disproves only the proposed global upper bound; it does not produce a sharp replacement for n>=3 or classify global maximizers.
- The analysis is for the real orthogonal setting of the source manuscript.

No GitHub content was modified during this audit. This file records an independent evidence review; it is not a peer-review or priority guarantee.
