# Pointwise sectional positivity does not imply 3-positivity for Einstein algebraic curvature in dimension four; Wu's K > 1/12 threshold is pointwise sharp

## Context

Let (M^4,g) be a closed Einstein four-manifold with Ric_g = g (scalar curvature s = 4). A central rigidity conjecture asserts such manifolds with everywhere positive sectional curvature are S^4 or CP^2. Wu (NYJM 2017, arXiv:1903.11817) derived relations among k-positivity of the curvature operator, sectional curvature, and isotropic curvature, proving K > 1/12 implies 3-positivity and 3-positivity implies K > 1/30, and left open Question (2): does positive sectional curvature imply 3-positive curvature operator? Cao-Wu (2013 preprint, Math. Z. 2019) classified 3-nonnegative Einstein four-manifolds. The admitted target asked the closed-manifold version. The natural first route is the pointwise algebraic reduction, which this result settles sharply.

## Definitions

Work with an algebraic curvature operator R on Lambda^2 R^4 satisfying the Einstein condition Ric = g. By the duality decomposition R = diag(A^+, A^-) with A^pm = W^pm + (s/12) I_3 = W^pm + (1/3) I_3, where W^pm are trace-free symmetric 3x3 blocks. Write eigenvalues a_1 <= a_2 <= a_3 of A^+ and b_1 <= b_2 <= b_3 of A^-, with trace compatibility sum a_i = sum b_j = 1. Let c_1 <= ... <= c_6 be the combined spectrum. R is k-positive if c_1 + ... + c_k > 0. Lemma: min sectional curvature equals (a_1 + b_1)/2, since every 2-plane corresponds to a decomposable unit bivector (u^+ + u^-)/sqrt(2) with K = (<A^+u^+,u^+> + <A^-u^-,u^->)/2.

## Result

(a) Pointwise no-go: strictly positive sectional curvature does not imply 3-positivity for Einstein algebraic curvature tensors in dimension four. The trace-compatible pair a = (-0.2,-0.1,1.3), b = (0.25,0.3,0.45) has min K = 0.025 > 0 while combined spectrum (-0.2,-0.1,0.25,0.3,0.45,1.3) has c_1+c_2+c_3 = -0.05 < 0, violating even 3-nonnegativity. (b) Sharp threshold family: F(t) with A^+ = (1/3,1/3,1/3), A^-(t) = (-t,-t,1+2t) satisfies all trace/Weyl/Berger constraints, with min K(t) = (1/3-t)/2 and 3-sum = 1/3-2t. At t = 1/5: min K = 1/15 > 0 with 3-sum -1/15 < 0 (exact rational certificate); at t = 1/6: min K = 1/12 with 3-sum 0. Hence no pointwise constant below 1/12 can force 3-positivity: Wu's K > 1/12 sufficient condition is pointwise best possible. (c) Robustness: the failure is open; among 200000 random Einstein Weyl pairs, 46554 have min K > 0 and 1081 of those (~2.3%) have 3-sum <= 0.

## Proof / evidence

Spectra and traces: sums equal 1; shifted Weyl eigenvalues sum to 0, so the pair is a valid Einstein duality-blocks spectrum. Sectional minimum follows from the Lemma: (-0.2+0.25)/2 = 0.025 > 0, confirmed by 200000 random-plane samples (minimum ~0.0252) in verify_algebraic_counterexample.py. The 3-sum is -0.2-0.1+0.25 = -0.05 < 0. The family formulas follow by direct substitution; exact Fraction verification including the Berger-frame pairing and Bianchi/Berger inequalities is in sharp_threshold_certificate.py. Optimality: for any m < 1/12, F(t) with m < (1/3-t)/2 < 1/12 has negative 3-sum near the boundary, refuting K > m => 3-positive. Round S^4 (all 1/3, 3-sum 1) and Fubini-Study CP^2 (1,0,0,1/3,1/3,1/3, 3-sum 1/3) are both 3-positive, consistent with known closed examples.

## Limitations

This does not exhibit a closed Einstein 4-manifold with everywhere sec > 0 and a point where c_1+c_2+c_3 <= 0; no such metric is known (all known closed sec>0 Einstein metrics, S^4/Gamma and CP^2, are 3-positive). Realizing the algebraic tensor by a genuine Einstein metric would require solving the Einstein equations, not done here. It does not resolve the admitted closed-manifold target in either direction. Optimality is pointwise over algebraic tensors, not global.

## Reproducibility

Run output/artifacts/verify_algebraic_counterexample.py (trace/Weyl checks, analytic min K, sorted 3-sum, 200000-plane floor), output/artifacts/sharp_threshold_certificate.py (exact Fraction certificate for F(1/5) and F(1/6) including Berger constraints), and output/artifacts/recovery_search.py (200000-sample robustness survey and CP^2-to-counterexample interpolation). All pass.

## References

P. Wu, Curvature decompositions on Einstein four-manifolds, NYJM 23 (2017), 1739-1749; arXiv:1903.11817. X. Cao and P. Wu, Einstein four-manifolds of three-nonnegative curvature operator, preprint 2013 (Cornell), published Math. Z.; Proposition 2.4. Q. Cui and L. Sun, rigidity note; X. Cao and H. Tran, pinched sectional curvature; C. Bohm and B. Wilking, 2-positive space forms; R. Hamilton, four-manifolds with positive curvature operator.
