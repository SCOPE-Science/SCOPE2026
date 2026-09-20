# Review — sharpness of the DPO one-half threshold

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For every \(0<\varepsilon<1/2\), the displayed inverse matrix has both absolute column sums equal to \(1/2+\varepsilon\), while its entrywise absolute value is upper triangular with Perron root \(1/2+\varepsilon\). Because this quantity is below one, standard AVE theory guarantees unique solvability.

All four sign candidates can be inverted in closed form. The candidate at \(z=(1,-1)\) has both coordinates positive, so it has a genuine sign mismatch. The candidate at \(z=(1,1)\) is positive and is the unique AVE solution. Exact subtraction of the four potential values gives three strictly positive gaps from \(F(1,-1)\) to every competitor. The nontrivial cubic numerator in one gap is positive by a sum-of-positive-terms decomposition. Thus the wrong sign vector is the unique global DPO maximizer.

The mismatch flip from \((1,-1)\) to \((1,1)\) has the negative of the first positive gap, proving that the source paper's monotone-ascent mechanism cannot hold universally once the threshold is exceeded.

The spectral-scaling statement is also exact: positive diagonal similarity preserves the spectral radius of the entrywise absolute matrix, and every induced norm dominates spectral radius. Hence no positive diagonal similarity can reduce this family below the one-half weighted-norm threshold.

The scalar minimal-dimension claim follows from the exact identity
\[
F(+)-F(-)=2ab/(a^2-1)
\]
for \(|a|>1\): the winning potential sign is exactly the sign of the unique scalar AVE solution. The higher-dimensional extension is block diagonal and preserves the controlling norm and spectral radius.

The included artifact independently checks a rational instance with \(\varepsilon=1/20\) using exact `Fraction` arithmetic only.

## Originality

**PASS, to the best of our knowledge, with the novelty claim restricted to the DPO landscape.** The current September 2026 Chen–Xia manuscript introduces the discrete potential and states the global-maximizer characterization under the strict one-half \(1\)-norm condition, together with a spectral-radius extension obtained through diagonal scaling. Searches by paper title, arXiv identifier, DPO terminology, the exact potential form, sharpness/counterexample terminology, and equivalent AVE formulations did not locate an erratum, comment, or prior result giving the present family or proving sharpness of the DPO global-equivalence threshold.

A closely related but distinct prior result was identified and checked. Radons (2016) proves sharpness of a one-half infinity-norm restriction for signed Gaussian elimination, where the property at issue is correct sign identification from a largest-magnitude right-hand-side coordinate. That result means the numerical threshold \(1/2\) itself is not claimed as new. It does not state or imply the present global-optimality failure for \(F(z)=z^\top(A-Z)^{-1}b\), the simultaneous \(1\)-norm and spectral-radius sharpness, or the strict DPO descent under the unique mismatch correction.

The 2026 Hladík–Moosaei–Hashemi–Ketabchi–Pardalos overview was inspected for unique-solvability conditions and sign-based methods. It records \(\rho(|A^{-1}|)<1\) as a standard sufficient condition for unique AVE solvability and surveys the earlier one-half signed-elimination regime, but it predates the Chen–Xia DPO potential and therefore does not cover the present landscape statement.

No inaccessible source was identified as especially likely to contain this exact DPO counterexample. Older AVE and LCP literature remains a general residual originality risk, so the claim is explicitly only to the best of our knowledge.

## Value

**PASS.** The result answers a natural boundary question for a new optimization formulation: the sufficient constant \(1/2\) cannot be increased by any positive amount if the desired conclusion is universal correctness of the unweighted DPO global maximizer under only the stated norm or spectral control. The obstruction appears in the smallest possible dimension, persists on an open set of right-hand sides, occurs for rational inputs arbitrarily close to the threshold, and embeds in all higher dimensions.

It also separates three notions that could otherwise be conflated. The AVE remains uniquely solvable throughout the construction because the spectral radius is below one; the DPO global maximizer is nevertheless wrong; and the full mismatch flip can still reach the solution even though it decreases the potential. Any extension beyond one half must therefore change the certification geometry, exploit additional structure, or use a different potential rather than simply weakening the scalar threshold in the existing argument.

## Limitations

The result does not prove divergence, cycling, or super-polynomial behavior of GNM or any other sign-flip solver above \(1/2\). On the explicit bad state, flipping the sole mismatch reaches the AVE solution in one step. The result is instead a sharp obstruction to the unweighted DPO global-maximizer equivalence and its monotone-ascent proof mechanism.

The spectral statement rules out entering the sub-one-half weighted-\(1\)-norm regime by positive diagonal scaling for this family; it does not rule out other weighted potentials, non-diagonal transformations, or stronger matrix-structural assumptions. No claim is made about the exact behavior at equality \(\|A^{-1}\|_1=1/2\).
