# Same-model review

## Correctness
PASS. Invariance against arbitrary antiderivatives of functions of \(x\) and \(z\) gives
\[
\mathbb E[y\mid x]=x,
\qquad
\mathbb E[x^2\mid z]=\frac chz.
\]
The latter forces \(z\ge0\) on the support. The exact polynomial identity
\[
L\left(-hxy+\frac h2x^2+bz-\frac k2z^2\right)
=
kc\,z^2-bc\,z-ah(y-x)^2
\]
gives the quadratic defect. Its equality case is reconstructed using invariance of the support and yields exactly the three equilibrium atoms. Strict defect then forces positive stationary mass above \(z=b/k\). The packaged exact-arithmetic checker verifies the algebra and canonical constants.

Risk: the equality proof uses the standard fact that the support of an invariant probability measure for a continuous complete flow is invariant.

## Originality
PASS. The most relevant inspected full text fixes the same equations, classical parameters, equilibria, and the local frozen-\(z\) transition at \(z=b/k\), then studies CCEBC and Hopf bifurcation. Targeted searches in that text found no invariant-measure, average, or moment formulation. The 2008 same-object paper concerns Hopf bifurcation and bifurcating-cycle stability, and the 2024 paper concerns Jacobi stability. Published semantic searches over parameter aliases, stationary moments, conditional laws, the \(b/k\) threshold, and recurrence returned no statement implying the final theorem.

Risk: the original 2004 paper and the 2008 Hopf paper were not available for complete line-by-line inspection.

## Value
PASS. The established literature already makes \(b/k\) a meaningful dynamical height: it is the nonzero-equilibrium height and the first threshold in the frozen planar subsystem. The theorem shows that every non-equilibrium compact recurrent statistical state must actually reach above that height, and it supplies two exact conditional laws plus a quantitative defect measuring departure from equilibrium mixtures. For the classical chaotic parameters this becomes the concrete universal barrier \(z>40\).

Same-model review: passed. Independent audit: not yet performed.
