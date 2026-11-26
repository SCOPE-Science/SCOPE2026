# Independent mathematical audit

## correctness

PASS

The tropical max has dominant index 0 below e, 1 between e and U, and 3 above U; index 2 only ties at U. The midpoint is 1. Pérez §4 and §5.1 give direct-chart recovery blocks d−j and 1 and include 1≤|t|≤U_j, so the actual direct chart at j=1,d=3 gives the displayed S_U and blocks 2 and 1, including t=1 (shared with the reversed half). The displayed diagonal row and column scalings give exactly S_U from the Frobenius companion; a constant unit minor on its last two rows and the first two columns gives the two unit Smith factors, and in the reversal the last two rows and last two columns give a unit minor. Thus linearization is strong, and det S_U=−eQ_U. For t>0 the weighted sum of coefficient magnitudes is Q_U(t); the backward error is at least 1 by the triangle inequality and equals 1 by perturbing each coefficient by its negative. At e=0, the two nonzero singular values are φ and φ⁻¹, so their product is 1. Singular-value perturbation gives product 1+O(e), while |det S_U|=et+O(e²) and W_U=φ+O(e), uniformly for t in compact positive sets. Hence the least normalized residual is t/(φU)+O(U⁻²). The isolated null eigenvectors of the limiting right and left Gramians can be expanded with positive third component; the first-order singular equations give z'=−e₂ and w'=e₁−e₂ at t=1. The normalized recovered error ratio therefore tends to φU in the sense of asymptotic equivalence, with both recovery coordinates nonzero for large enough U. Zero recovery is a stronger constraint: the indicated column/row restrictions have exactly the specified traces and determinants, and their least Gram eigenvalues give attained thresholds. Using λ_min=D/λ_max with λ_max→T at e=0 gives Uδ_R→√(3/2)/φ and Uδ_L→√2/φ. Both limits exceed the unconstrained constant 1/φ at t=1, so for sufficiently large U the two singular modes indeed lie below the respective thresholds. Determinant, first-order singular equations, and Gram invariants were independently checked with `python /workspace/independent_reproduction.py`; the frozen check.py was inspected, not executed.

## originality

PASS

Unstructured pencil backward stability versus coefficientwise polynomial backward stability and the recovery-factor mechanism are established prior work. The supported distinct result is a concrete source-prescribed tropical companion with two distinct tropical roots, its sharp least residual asymptotic, simultaneous left/right recovery loss, and its exact constrained thresholds. The closest inspected source provides the chart but explicitly leaves control of computed recovery ratios unresolved; the evidence does not certify historical priority.

## value

PASS

This is a motivated residual-acceptance obstruction for a prescribed scaling chart, not a generic ill-conditioned matrix example. Even passing a strict threshold that rules out zero recovery cannot bound the recovered polynomial error: the left and right scalar recoveries are nonzero but both errors are 1 while the least unstructured pencil residual tends to zero. Exact constants and attained thresholds separate these requirements quantitatively. That is useful for distinguishing guarantees one could reasonably seek from an eigensolver from those a normwise residual test can provide on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
