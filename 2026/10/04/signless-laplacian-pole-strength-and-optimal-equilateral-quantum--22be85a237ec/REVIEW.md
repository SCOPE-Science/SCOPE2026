# Same-model review

## Correctness

**PASS.** The edge boundary-value problem gives the exact matrix
\[
\Lambda_G(k^2)=\frac{k}{\sin(k\ell)}\left(A-\cos(k\ell)D\right).
\]
At an odd resonance \(k_0\ell=n\pi\), the matrix factor tends to \(Q=D+A\), while
\[
|k^2-k_0^2|\left|\frac{k}{\sin(k\ell)}\right|
\longrightarrow \frac{2k_0^2}{\ell}.
\]
Continuity of singular values therefore proves the stated coefficient. The even-resonance claim follows because the limiting numerator is \(-L\), which is singular. The fixed-order optimum follows from
\[
Q(G)+Q(\overline G)=(d-2)I+J
\]
and the positive-semidefinite signless-Laplacian quadratic form. The strict equality case is established by an explicit vector supported on a missing edge. Supplementary enumeration and near-resonance numerical checks replay these formulas.

## Originality

**PASS, with a narrow scope.** Do--Kuchment--Ong prove the uniform pole estimate abstractly, give an odd-cycle construction, and explicitly identify dependence of the gap size on their constant \(C\) as a design question. Their inspected full text does not evaluate that constant for general all-boundary equilateral simple decorations or optimize it over a fixed boundary size.

The signless-Laplacian reduction is specific to the all-boundary equilateral subclass. Targeted searches for combinations of “signless Laplacian,” “Dirichlet-to-Neumann,” “resonant spectral gap,” and “quantum graph decoration” did not locate an equivalent result. General signless-Laplacian spectral theory and unrelated signless-Laplacian quantum walks do not imply the quantum-graph residue formula without the edge Dirichlet-to-Neumann calculation.

Residual risk remains because the identity is compact and may appear in work phrased using \(M\)-functions or boundary triples. The claim therefore does not assert priority for the general resonant mechanism or for signless-Laplacian graph theory.

## Value

**PASS.** The finding answers the source paper's stated design question on a broad, natural finite class rather than for a single example. It turns the analytic pole-strength problem into a graph spectral invariant, gives a structural feasibility test through bipartiteness, proves a unique optimizer for every boundary size, and quantifies a more than fourfold improvement over the source's four-boundary example.

Same-model review: passed. Independent audit: not yet performed.
