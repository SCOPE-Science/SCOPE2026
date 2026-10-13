# All optimal finite decompositions of the canonical GHZ–W concurrence-fill mixture

## Finding
For the canonical rank-two family
\[
\rho_\lambda=\lambda|\mathrm{GHZ}\rangle\!\langle\mathrm{GHZ}|+(1-\lambda)|W\rangle\!\langle W|,
\qquad 0<\lambda<1,
\]
every finite pure-state decomposition attaining the concurrence-fill convex roof has a simple and complete form. After discarding zero-probability labels and ignoring irrelevant global phases, it is optimal if and only if
\[
|\phi_j\rangle=\sqrt{\lambda}\,|\mathrm{GHZ}\rangle+e^{i\theta_j}\sqrt{1-\lambda}\,|W\rangle,
\qquad p_j>0,
\]
with
\[
\sum_j p_j=1,
\qquad
\sum_j p_j e^{i\theta_j}=0.
\]
Hence the optimal finite ensembles are exactly the weighted phase polygons whose complex barycenter is the origin.

The support minimum is exactly two. Every support-two optimum has equal probabilities and antipodal phases, so, up to a common phase and relabeling,
\[
p_+=p_-=\frac12,
\qquad
|\phi_\pm\rangle=\sqrt{\lambda}\,|\mathrm{GHZ}\rangle\pm\sqrt{1-\lambda}\,|W\rangle.
\]
The four-column co-isometry exhibited in the source therefore represents two duplicate copies of each of these two pure states. The source convex-roof value is unchanged:
\[
F(\rho_\lambda)=\frac{5\lambda^2-4\lambda+8}9.
\]

## Assumptions and scope
The statement concerns the canonical GHZ–W family and the concurrence-fill convex roof studied in arXiv:2608.07145v1. It classifies finite pure-state ensembles with strictly positive weights for \(0<\lambda<1\). The endpoints \(\lambda=0\) and \(\lambda=1\) are excluded because \(\rho_\lambda\) then has rank one and the equality structure degenerates.

Write
\[
|\mathrm{GHZ}\rangle=\frac{|000\rangle+|111\rangle}{\sqrt2},
\qquad
|W\rangle=\frac{|001\rangle+|010\rangle+|100\rangle}{\sqrt3}.
\]
No claim is made for arbitrary rank-two pairs, for other multipartite entanglement measures, or for operational monotonicity of concurrence fill.

## Proof
The Hughston–Jozsa–Wootters parametrization writes any finite decomposition supported on the two-dimensional range of \(\rho_\lambda\) as
\[
|\phi_j\rangle=
\frac{v_{1j}\sqrt{\lambda}\,|\mathrm{GHZ}\rangle+v_{2j}\sqrt{1-\lambda}\,|W\rangle}{\sqrt{p_j}},
\]
where the two rows of \(V=(v_{aj})\) are orthonormal and
\[
p_j=\lambda|v_{1j}|^2+(1-\lambda)|v_{2j}|^2.
\]
Define
\[
r_j=\frac{|v_{1j}|^2}{p_j}.
\]
The source reduces the ensemble-averaged concurrence fill to
\[
\sum_j p_j g(r_j),
\qquad
g(r)=\frac{5\lambda^2r^2-4\lambda r+8}9,
\]
and row normalization gives
\[
\sum_j p_jr_j=1.
\]
For \(0<\lambda<1\),
\[
g''(r)=\frac{10\lambda^2}9>0,
\]
so equality in Jensen's inequality is possible exactly when \(r_j=1\) for every positive-weight term. Thus optimality is equivalent to
\[
|v_{1j}|^2=p_j.
\]
Substituting this into the formula for \(p_j\), and using \(0<\lambda<1\), gives
\[
|v_{2j}|^2=p_j
\]
for every \(j\). Hence there are phases \(\alpha_j,\beta_j\) with
\[
v_{1j}=\sqrt{p_j}e^{i\alpha_j},
\qquad
v_{2j}=\sqrt{p_j}e^{i\beta_j}.
\]
The row-orthogonality condition is
\[
0=\sum_jv_{1j}v_{2j}^*
 =\sum_jp_j e^{i(\alpha_j-\beta_j)}.
\]
After removing the global phase \(e^{i\alpha_j}\) from each state and setting \(\theta_j=\beta_j-\alpha_j\), this is exactly
\[
\sum_j p_j e^{i\theta_j}=0,
\]
and the state has the form stated above.

Conversely, suppose positive probabilities and phases satisfy that zero-barycenter equation. Choosing
\[
v_{1j}=\sqrt{p_j},
\qquad
v_{2j}=\sqrt{p_j}e^{i\theta_j}
\]
gives two unit rows with zero inner product. Therefore it is an admissible HJW co-isometry, every \(r_j=1\), and Jensen is saturated. This proves the iff classification.

For two states, the barycenter equation is
\[
p_1e^{i\theta_1}+p_2e^{i\theta_2}=0,
\qquad p_1+p_2=1.
\]
Taking absolute values forces \(p_1=p_2=1/2\), and then the two phases differ by \(\pi\). Since \(\rho_\lambda\) has rank two for \(0<\lambda<1\), no one-state decomposition exists. Hence two is the exact minimum support.

The phase-independence used by the source can also be checked directly. For
\[
|\psi\rangle=\sqrt q\,|\mathrm{GHZ}\rangle+e^{i\theta}\sqrt{1-q}\,|W\rangle,
\]
permutation symmetry makes the concurrence triangle equilateral, and a one-qubit reduction has
\[
4\det\rho_A=\frac{5q^2-4q+8}9,
\]
independent of \(\theta\). Thus no hidden phase term is being discarded in the equality argument.

## Verification
The proof uses only the source's exact HJW reduction, strict Jensen equality, and elementary row-orthogonality. A standalone checker in `artifacts/verify.py` independently confirms the phase-independent one-qubit determinant formula, the two-state optimizer, the source four-column co-isometry, and strict Jensen gaps for nonconstant \(r_j\) samples. These finite checks corroborate but do not replace the all-parameter proof.

The source's displayed co-isometry has first row \((1/2,1/2,1/2,1/2)\) and second row \((1/2,1/2,-1/2,-1/2)\). Its four probabilities are all \(1/4\), so its first two normalized states coincide with \(|\phi_+\rangle\) and its last two coincide with \(|\phi_-\rangle\). Merging duplicate ensemble letters gives the support-two optimum without changing the density operator or average concurrence fill.

## Relationship to prior work
Verma and Kulkarni derive the exact convex-roof value for the canonical GHZ–W mixture by Jensen's inequality and exhibit one four-state co-isometry attaining it. Their text notes that many co-isometries can attain the bound, but it does not give the equality-case classification, the zero-barycenter phase-polygon parametrization, or the exact minimum support. The present result is the equality theory of that same optimization.

Aggarwal studies concurrence fill for generalized GHZ/W-class rank-two mixtures and obtains eigenstate formulas and an upper bound in a zero-three-tangle regime. That work does not supply the exact all-optimal-ensemble classification for the canonical convex roof considered here. The HJW theorem supplies the general ensemble parametrization but does not select the concurrence-fill equality cases.

## Limitations
The result is confined to finite optimal ensembles of the canonical GHZ–W family with \(0<\lambda<1\). It does not assert that every optimal decomposition for an arbitrary rank-two three-qubit state has a phase-polygon form, and it does not address infinite probability measures beyond the finite HJW formulation used here. It also makes no new claim about whether concurrence fill is monotone under local operations and classical communication.

Because the anchor paper is recent, an equivalent equality-case observation could appear in a follow-up not yet well indexed. Focused searches by the source identifier, equality/Jensen language, optimal-decomposition language, phase-barycenter language, and rank-two GHZ–W terminology found no such statement.

## References
1. D. K. Verma and G. Kulkarni, *From triangles to prisms: towards a geometric extension of concurrence fill for three-qubit mixed states*, arXiv:2608.07145v1 (2026).
2. S. Aggarwal, *Classification of Three-Qubit Genuine Entangled States Using Concurrence Fill*, arXiv:2506.16935; International Journal of Theoretical Physics 64, 292 (2025), DOI 10.1007/s10773-025-06152-w.
3. L. P. Hughston, R. Jozsa, and W. K. Wootters, *A complete classification of quantum ensembles having a given density matrix*, Physics Letters A 183, 14–18 (1993).
