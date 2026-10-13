# Self-review

## Correctness
PASS. Kapranov identifies the generic maximal-torus orbit closure in \(\operatorname{Gr}(k,n)\) with the projective normal toric variety of the hypersimplex \(\Delta(k,n)\). Its Plücker degree is the normalized lattice volume
\[
A(n-1,k-1),
\]
and its toric orbit stratification gives
\[
\chi_{\mathrm{top}}=\binom nk.
\]

The Eulerian recurrence gives the sharp interior lower bound
\[
A(n-1,k-1)\ge2^{n-1}-n,
\]
while a parity-class decomposition of Pascal's row gives
\[
2^{n-1}-n>\binom n{\lfloor n/2\rfloor}
\]
for \(n\ge5\). Small \(n\) and the simplex endpoints are checked separately. This proves the complete strict comparison and excludes equality.

The bundled checker reconstructs Eulerian numbers independently through \(n=120\). Finite computation is regression evidence only.

## Originality
PASS. The inspected archival sources separately provide the generic hypersimplex toric model and the Eulerian normalized-volume formula. Targeted searches in hypersimplex-toric, Grassmannian-orbit, Eulerian-versus-binomial, and equality formulations did not locate the all-parameter crossover.

Residual risk remains because the final inequality is elementary and may appear in purely combinatorial literature without geometric terminology.

## Value
PASS. The theorem compares the two most immediate numerical complexities of a canonical toric family inside Grassmannians: generic linear-section count and torus-fixed-point topology. It gives a sharp dimension threshold, a complete parameter classification, and a no-equality result across the whole hypersimplex family.

Self-review: passed. Independent audit: not yet performed.
