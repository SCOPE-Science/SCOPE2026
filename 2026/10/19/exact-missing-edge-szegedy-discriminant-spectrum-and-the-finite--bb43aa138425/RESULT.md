# Exact missing-edge Szegedy discriminant spectrum and the finite-marked Rayleigh gap

## Finding
For every integer \(n\ge4\) and \(0\le m\le n-3\), consider the Szegedy discriminant of the uniformly normalized complete graph on \(n\) vertices, with \(m\) marked absorbing vertices, after removing exactly one edge between two unmarked vertices and redistributing each deleted directed edge's probability uniformly among its \(n-2\) remaining targets. Write \(k=n-m\), \(b=k-2\), \(p=1/(n-1)\), and \(a=1/\sqrt{(n-1)(n-2)}\). Its complete spectrum is
\[
\{1^{[m]},\lambda_+,\lambda_-,0,(-p)^{[b-1]}\},\qquad
\lambda_\pm=\frac{(b-1)p\pm\sqrt{(b-1)^2p^2+8ba^2}}2.
\]
The superscripts in square brackets denote multiplicities; zero multiplicities are omitted. The old largest unmarked eigenvalue is \(L=(k-1)/(n-1)\). The **actual** shifted eigenvalue satisfies
\[
L-\lambda_+=\frac{2m}{(n-1)^2(n-2)(L-\lambda_-)}.
\]
Therefore \(L=\lambda_+=1\) when \(m=0\), while \(0<\lambda_+<L\) for every \(m\ge1\). In the fixed-marked regime \(m\ge1\),
\[
\lim_{n\to\infty}n^3(L-\lambda_+)=2m.
\]
In contrast, the **exact Rayleigh-quotient deficit** \(D_R:=L-\langle v,\widetilde C v\rangle\) for the *old* unmarked uniform eigenvector \(v\) has \(n^3D_R\to2m+1/2\) (including \(m=0\)), and obeys \(0\le L-\lambda_+<D_R\) for every \(k\ge3\). The source's quotient formula must not be identified with the actual eigenvalue shift in this regime. If \(m/n\to\alpha\in(0,1)\), then \(n^2(L-\lambda_+)\to2\alpha/(1-\alpha)\).

## Assumptions and scope
Label the marked vertices \(1,\ldots,m\) and the remaining \(k\) vertices as unmarked. Two distinct unmarked vertices \(u,v\) lose their connecting edge. For each unmarked column \(j\), before deletion every transition to a different vertex has probability \(1/(n-1)\). The marked columns become absorbing unit columns. After deletion the columns \(u,v\) have probability \(1/(n-2)\) at each of the remaining \(n-2\) non-self, nonpartner destinations, including marked vertices. All other columns remain unchanged. The *symmetric Szegedy discriminant* has entries \(\widetilde C_{ij}=\sqrt{\widetilde P_{ij}\widetilde P_{ji}}\). The theorem concerns this discriminant and its spectral phase inputs; it does not assert an exact quantum search success probability. Integers \(n\ge4\), \(0\le m\le n-3\) are arbitrary. The case \(k=2\) is excluded from the uniform strict-Rayleigh comparison: its unmarked discriminant is exactly zero with multiplicity two.

## Proof
Marking makes a diagonal identity block \(I_m\), and removes all discriminant couplings from marked to unmarked vertices. Within the unmarked block, the pair \(u,v\) is uncoupled and has zero diagonal. Each defect-to-ordinary entry is \(a\), and each distinct ordinary-to-ordinary entry is \(p\). These entries follow by taking geometric means of opposite stochastic transitions. There are \(b=k-2\ge1\) ordinary unmarked vertices.

The defect antisymmetric vector \((e_u-e_v)/\sqrt2\) is a zero eigenvector. The ordinary sum-zero subspace is a \((-p)\)-eigenspace of dimension \(b-1\). The remaining orthonormal basis vectors \((e_u+e_v)/\sqrt2\) and \(b^{-1/2}\sum_{j\notin\{u,v\},\,j\,\mathrm{unmarked}}e_j\) reduce the discriminant to
\[
H=\begin{pmatrix}0&\sqrt{2b}\,a\\ \sqrt{2b}\,a&(b-1)p\end{pmatrix}.
\]
Its quadratic characteristic polynomial gives \(\lambda_\pm\), exhausting all \(n\) eigenvalues and multiplicities. Since \(\det H=-2ba^2<0\), \(\lambda_+>0>\lambda_-\); Perron positivity identifies \(\lambda_+\) as the top unmarked eigenvalue.

Writing \(L=(b+1)p\), substitution into that characteristic polynomial gives
\[
(L-\lambda_+)(L-\lambda_-)=L^2-(b-1)pL-2ba^2
=2(b+1)p^2-2ba^2=\frac{2m}{(n-1)^2(n-2)}.
\]
The final equality follows from \(b=n-m-2\). The denominator \(L-\lambda_-\) is strictly positive, proving the exact formula, equality for \(m=0\), and strict negativity of the actual eigenvalue change for \(m\ge1\). When \(m=0\), the positive root is exactly one; this also follows from reversibility of a finite stochastic chain.

For \(m\) fixed, \(L-\lambda_-\to1\), hence \(n^3(L-\lambda_+)\to2m\). For \(m/n\to\alpha\in(0,1)\), \(L-\lambda_-\to1-\alpha\) and the numerator after multiplication by \(n^2\) approaches \(2\alpha\), yielding the displayed limit.

For the old unmarked uniform unit vector \(v\), direct summation of the two defect rows gives
\[
D_R=\frac{2p}{k(n-2)}\left[m+(k-2)(\sqrt{n-1}-\sqrt{n-2})^2\right].
\]
The variational characterization of the top eigenvalue gives \(\lambda_+\ge\langle v,\widetilde C v\rangle\). Equality would require \(v\) to be an eigenvector. Yet the unmarked row sums at a defect and ordinary vertex are respectively \(ba\) and \(2a+(b-1)p\). Their difference is positive, since \((b-2)a<(b-1)p\): for \(b=1\) it is immediate, while for \(b\ge2\), use \(a/p=\sqrt{1+1/(n-2)}<1+1/[2(n-2)]\) and \(b\le n-2\). Thus the variational inequality is strict. Furthermore \(D_R>0\). Finally \((\sqrt{n-1}-\sqrt{n-2})^2\sim1/(4n)\), giving \(n^3D_R\to2m+1/2\) for fixed \(m\ge0\).

## Verification
The standalone file `verify.py` independently builds the full finite discriminant for each \(4\le n\le55\) and every \(0\le m\le n-2\), compares its numerical eigenvalues to the proposed closed formulas, checks the exact rationalized shift identity, strict Rayleigh comparison in \(k\ge3\), and tests fixed-marked/proportional-marked limits. It successfully completes 5,787 assertions. These checks are corroborative, not a proof for all dimensions; the preceding two-invariant-subspace argument proves the infinite family.

## Relationship to prior work
Giordano and Martin-Delgado, arXiv:2607.19129v1, introduce precisely this marked complete-graph missing-link Szegedy model and derive the Rayleigh quotient \(\langle v,(\widetilde C-C)v\rangle\), including its negative sign. Their Proposition 4, equation (42), supplies the expression here denoted \(-D_R\); their appendices calculate that old-vector quotient. That calculation is valid **as a Rayleigh quotient**, but the exact new eigenvalue is instead \(\lambda_+\) obtained by diagonalizing the invariant two-dimensional quotient block. The distinction is visible already for \(m=0\), where the leading discriminant eigenvalue remains one. General perturbation bounds and generic Szegedy spectral correspondence are background, not claims of novelty. Searches found no identified primary result covering this exact full shifted spectrum and the fixed-marked constant gap; all novelty conclusions remain subject to further literature checking.

## Limitations
The proof is restricted to *uniform* redistribution and one deleted unmarked--unmarked edge in the marked-complete-graph transition model. It does not establish uniqueness among all graph spectral descriptions, an experimental identification method, or exact full quantum-walk success probabilities. A generic equitable-partition result explains the basic reduction; the concrete comparison with the published claimed shift and its fixed-marked leading error is the substantive model-specific conclusion. No independent scientific audit has been performed.

## References
1. S. Giordano and M. A. Martin-Delgado, *Single Link Removal Perturbation in Szegedy Quantum Walk: from Graph Completeness Testing to Integrity Monitoring*, arXiv:2607.19129v1, first posted 2026-07-21. In particular Sections 3–5, Proposition 4, equation (42), and Appendix C.
2. M. Szegedy, *Quantum speed-up of Markov chain based algorithms*, 2004 (spectral discriminant correspondence, cited in reference 1).
3. Rayleigh–Ritz variational principle for finite real symmetric matrices (standard theorem; applied directly above).
