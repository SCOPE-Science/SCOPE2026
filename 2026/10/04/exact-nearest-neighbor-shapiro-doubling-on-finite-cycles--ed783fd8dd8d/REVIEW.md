# Review

## Correctness
PASS. For \(C_n=4c_n-1\), the signed comparison kernel \(h=C_n1_U-1_{2U}\) is decomposed explicitly as \(h=\sigma+\tau\), where \(\sigma=(6c_n-4)(\delta_1+\delta_{-1})\ge0\) and
\[
\widehat\tau(k)=4(1-x_k)(x_k+c_n)\ge0.
\]
This proves the upper bound for every nonnegative positive-definite \(f\). The displayed witness \(f_*\) has nonnegative Fourier coefficients, is pointwise nonnegative, vanishes at \(\pm1\), and attains \(C_n\). Boundary cases \(n\ge5\) are included without a limiting argument.

## Originality
PASS relative to the checked literature and database. The primary Gaál--Révész source defines the general Shapiro quantity and proves duality but contains no finite-cyclic nearest-neighbor formula. Gorbachev--Tikhonov treat Euclidean convex-body doubling. The classical Lovász theta formula for cycles has different constraints and a global objective; it does not by itself yield the local five-point/three-point inequality. Exact-form and alias searches did not locate a covering statement.

## Value
PASS. The three-point neighborhood is the smallest nontrivial symmetric local neighborhood on a cycle, and its two-fold sumset is the first local doubling test. The exact answer exhibits a structural parity transition: even cycles saturate the elementary ceiling \(3\), while odd cycles have the sharp defect
\[
4(1-\cos(\pi/n)).
\]
The explicit dual certificate also supplies a reusable template for finite-group Shapiro comparisons.

## Closest literature and limitations
The closest harmonic-analysis source is Gaál--Révész, arXiv:1803.06409. Gorbachev--Tikhonov, arXiv:1612.08637, is the closest doubling paper. Lovász's cycle theta formula is a related finite cyclic extremum but does not have the same feasible set or objective. The theorem does not classify every maximizer and does not treat larger neighborhoods or higher dilations.

Same-model review: passed. Independent audit: not yet performed.
