# Same-model review

## Correctness

**PASS.** The source scattering formula reduces the local transmission probability to \(P_\alpha(E)=[1+\alpha^4F(E)^2]^{-1}\), with \(F(E)=\Lambda(E)/(2k(E))\). Green's identity for the boundary-normalized compact-graph solution gives the exact slope
\[
\Lambda'(E_0)=\frac{1}{c|\psi_0(v_0)|^2}
\]
at a positive simple visible eigenvalue. The inverse-function theorem then gives the unique local half-maximum points. The \(O(\alpha^{-6})\) FWHM remainder follows because even powers cancel in \(G(\varepsilon)-G(-\varepsilon)\). A change of variables proves the peak-area limit. An exactly solvable interval independently reproduces the same coefficient and line shape.

## Originality

**PASS, narrowly scoped.** The primary source gives the exact transmission amplitude, proves the strong-coupling indicator limit, and describes “narrow peak passbands,” but the inspected full text contains no occurrence of “width” and does not relate peak width or area to the local eigenfunction value. Related Turek--Cheon star-filter work does contain a bandwidth calculation, but for a different threshold/potential-controlled device; Turek's flat-passband work is likewise a different filter architecture.

Semantic-database and web searches combining the source title with “linewidth,” “FWHM,” “peak width,” “Dirichlet-to-Neumann derivative,” “local spectral weight,” and “eigenfunction value” did not locate the exact statement. The accepted originality claim is therefore only the local spectral-weight line-shape theorem for the attached-compact-graph filter, not the filtering mechanism itself.

Residual risk remains because the Dirichlet-to-Neumann derivative identity is standard in Weyl-function theory and an equivalent linewidth statement may be phrased differently in unindexed literature.

## Value

**PASS.** The result supplies a quantitative resolution law for the source's spectral analyzer: peak location measures the eigenvalue while peak width or area measures \(|\psi_0(v_0)|^2\). It also gives a universal Lorentzian scaling and the universal area-to-FWHM ratio \(\pi/2\). This distinguishes eigenmodes with the same or nearby energies by their local coupling strength and provides a concrete design rule for selecting attachment points.

Same-model review: passed. Independent audit: not yet performed.
