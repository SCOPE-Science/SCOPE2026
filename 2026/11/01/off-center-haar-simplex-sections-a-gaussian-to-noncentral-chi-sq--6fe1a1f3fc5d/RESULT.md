# Off-center Haar simplex sections: a Gaussian-to-noncentral-chi-square face-vector transition

## Finding
Let \(m\ge4\). Embed the unit-circumradius regular \((m-1)\)-simplex in the zero-sum subspace of \(\mathbb R^m\), with vertices
\[
v_i=\sqrt{\frac m{m-1}}\left(e_i-\frac1m\mathbf1\right),\qquad 1\le i\le m.
\]
Let \(u_m\) be a Haar-uniform unit vector in this subspace and intersect the simplex with
\[
H_m(\alpha_m)=\left\{x:\langle u_m,x\rangle=\frac{\alpha_m}{\sqrt{m-1}}\right\}.
\]
Write \(f_{m,j}\) for the number of \(j\)-faces of the section, setting it to zero when the section is empty. Fix a finite integer \(J\ge0\), and take \(m\ge J+3\). Define
\[
p_\alpha=1-\Phi(\alpha),\quad \varphi_\alpha=\frac{e^{-\alpha^2/2}}{\sqrt{2\pi}},\quad
\sigma_\alpha^2=p_\alpha(1-p_\alpha)-\varphi_\alpha^2\left(1+\frac{\alpha^2}{2}\right)>0,
\]
\[
A_j(p)=\frac{1-p^{j+2}-(1-p)^{j+2}}{(j+2)!},\qquad
D_j(p)=\frac{(1-p)^{j+1}-p^{j+1}}{(j+1)!}.
\]

**Fixed nonzero offset.** If \(\alpha_m=\alpha\ne0\), then, jointly for \(0\le j\le J\),
\[
\boxed{\left(\frac{f_{m,j}-m^{j+2}A_j(p_\alpha)}{m^{j+3/2}}\right)_{j=0}^{J}
\Longrightarrow\left(D_j(p_\alpha)G_\alpha\right)_{j=0}^{J},\qquad
G_\alpha\sim N(0,\sigma_\alpha^2).}
\tag{1}
\]
The Gaussian fluctuation is rank one across face dimensions, with a variance reduction involving **both** centering and standardization of the random normal.

**Microscopic displacement from the centroid.** Suppose \(\alpha_m=\lambda/\sqrt m\), for fixed real \(\lambda\), and put
\[
B_{m,j}=\binom m{j+2}-\binom{\lfloor m/2\rfloor}{j+2}-\binom{\lceil m/2\rceil}{j+2},\qquad
\sigma_0^2=\frac14-\frac1{2\pi}.
\]
Then, jointly for \(0\le j\le J\),
\[
\boxed{\left(\frac{B_{m,j}-f_{m,j}}{m^{j+1}}\right)_{j=0}^{J}
\Longrightarrow\left(\frac{(G_0-\lambda/\sqrt{2\pi})^2}{2^j j!}\right)_{j=0}^{J},\qquad G_0\sim N(0,\sigma_0^2).}
\tag{2}
\]
For \(\lambda\ne0\), this is a **noncentral** one-degree chi-square law, multiplied by the displayed deterministic rank coefficients; its noncentrality parameter is \(\lambda^2/(2\pi\sigma_0^2)\). The \(\lambda=0\) central case is a previously recorded result and is included only to describe the transition continuously. The new assertion is the full off-center pair of laws (1)–(2), including the studentization correction in (1).

## Assumptions and scope
The offsets are signed relative to a randomly oriented **unit** normal. Thus the physical centroid-to-hyperplane distance is \(|\alpha_m|/\sqrt{m-1}\). In (1) it is of order \(m^{-1/2}\), whereas in (2) it is of order \(m^{-1}\). No fixed-dimensional, noncentral face-count probability mass formula is claimed. The ranks \(j\) are fixed while \(m\to\infty\). The hyperplane may miss the simplex for some orientations; those sections are assigned the zero face vector. All exceptional vertex-on-hyperplane events have probability zero.

## Proof
**1. An exact all-dimensional combinatorial reduction.** For a deterministic generic hyperplane, let \(k\) of the \(m\) simplex vertices lie strictly above it. Every \(j\)-face of a nonempty section arises uniquely by intersecting the hyperplane with a \((j+1)\)-face of the simplex containing vertices on both sides. Consequently, with \(r=j+2\),
\[
f_{m,j}=\binom mr-\binom kr-\binom{m-k}r.
\tag{3}
\]
When \(k=0\) or \(m\), both sides of (3) are zero under the empty-section convention. Convexity of \(k\mapsto\binom kr+\binom{m-k}r\), seen from its nonnegative discrete second differences, shows that \(B_{m,j}\) is the maximum. In particular, all ranks depend on just the single sign count \(k\).

**2. Haar normals and Gaussian sample standardization.** Let \(Z_1,\ldots,Z_m\) be independent standard normals and define \(\bar Z=m^{-1}\sum_iZ_i\) and \(s_m^2=m^{-1}\sum_i(Z_i-\bar Z)^2\). The random unit vector
\[
u_m=\frac{(Z_i-\bar Z)_{i=1}^m}{\sqrt m\,s_m}
\]
is Haar-uniform in the zero-sum space. Direct substitution into the vertex formula gives the **exact** signed height relation
\[
\langle v_i,u_m\rangle=\frac{Z_i-\bar Z}{s_m\sqrt{m-1}}.
\]
Therefore the random count in (3) equals, in distribution,
\[
K_m(\alpha_m)=\#\left\{i:\frac{Z_i-\bar Z}{s_m}>\alpha_m\right\}.
\tag{4}
\]
This is a count **above a studentized sample threshold**, not an independent-binomial count.

**3. The exact influence variance.** For fixed real \(\alpha\) and \(\alpha_m=\alpha+\lambda/\sqrt m+o(m^{-1/2})\), the law of large numbers and Taylor expansion give
\[
\bar Z=\frac1m\sum_iZ_i,\qquad
s_m=1+\frac1{2m}\sum_i(Z_i^2-1)+o_{\mathbb P}(m^{-1/2}).
\]
For the empirical cdf \(F_m\), stochastic equicontinuity at the moving point \(t_m=\bar Z+\alpha_m s_m=\alpha+O_{\mathbb P}(m^{-1/2})\) yields
\[
F_m(t_m)=F_m(\alpha)+\Phi(t_m)-\Phi(\alpha)+o_{\mathbb P}(m^{-1/2}).
\tag{5}
\]
For completeness, (5) needs no unproved functional central limit theorem. On the high-probability event \(|t_m-\alpha|\le C/\sqrt m\), partition that interval by a deterministic mesh of length at most \(m^{-3/4}\). There are \(O_C(m^{1/4})\) grid points. Each centered count between \(\alpha\) and a grid point has variance \(O_C(\sqrt m)\), so Chebyshev's inequality plus the union bound makes their maximal fluctuation \(o_{\mathbb P}(\sqrt m)\). Monotonicity between grid points adds at most the expected count \(O(m^{1/4})\). Letting \(C\) increase establishes (5).

Because \(K_m/m=1-F_m(t_m)\) almost surely, (5) gives
\[
\frac{K_m(\alpha_m)-mp_\alpha}{\sqrt m}
=\frac1{\sqrt m}\sum_{i=1}^m\psi_\alpha(Z_i)-\lambda\varphi_\alpha+o_{\mathbb P}(1),
\tag{6}
\]
where
\[
\psi_\alpha(z)=\mathbf1_{\{z>\alpha\}}-p_\alpha-\varphi_\alpha z-\frac{\alpha\varphi_\alpha}{2}(z^2-1).
\]
The independent summands have mean zero. Gaussian integration gives
\(\mathbb E[Z\mathbf1_{\{Z>\alpha\}}]=\varphi_\alpha\),
\(\mathbb E[(Z^2-1)\mathbf1_{\{Z>\alpha\}}]=\alpha\varphi_\alpha\),
\(\mathbb EZ^2=1\) and \(\mathbb E(Z^2-1)^2=2\). Orthogonality of the first two Gaussian Hermite components then yields
\(\operatorname{Var}(\psi_\alpha(Z))=\sigma_\alpha^2\). This is strictly positive for every finite \(\alpha\), since an indicator step function cannot agree almost surely with a quadratic polynomial. The iid central limit theorem applied to (6) proves
\[
\frac{K_m(\alpha_m)-mp_\alpha}{\sqrt m}
\Longrightarrow N(-\lambda\varphi_\alpha,\sigma_\alpha^2).
\tag{7}
\]

**4. The Gaussian regime.** If \(\alpha_m=\alpha\ne0\), equation (7) has \(\lambda=0\). Expand the exact polynomial (3) uniformly for \(k/m=p_\alpha+O_{\mathbb P}(m^{-1/2})\):
\[
f_{m,j}=m^{j+2}A_j(k/m)+O_j(m^{j+1}).
\]
A first-order Taylor expansion of \(A_j\) at \(p_\alpha\) has derivative \(D_j(p_\alpha)\), proving (1) simultaneously over the finite range of ranks. For \(\alpha\ne0\), \(p_\alpha\ne1/2\), and the derivative coefficients are nonzero.

**5. The noncentral chi-square crossover.** In (7) take \(\alpha=0\) and \(\alpha_m=\lambda/\sqrt m\). Then
\[
T_m=\frac{K_m(\alpha_m)-m/2}{\sqrt m}\Longrightarrow
G_0-\frac{\lambda}{\sqrt{2\pi}}.
\]
Writing \(k=m/2+\sqrt m\,t\), the even binomial polynomial in (3) has the uniform fixed-rank expansion
\[
\frac{B_{m,j}-f_{m,j}}{m^{j+1}}=\frac{t^2}{2^j j!}+o(1)
\]
for bounded \(t\); the integer-versus-half-integer midpoint changes the expression by \(O_j(m^{-1})\). Since \(T_m=O_{\mathbb P}(1)\), the continuous mapping theorem gives (2) jointly. In particular, the complete finite vector of normalized deficits remains rank one, but its common factor changes from a centered squared Gaussian to a shifted squared Gaussian when the physical section displacement is of order \(m^{-1}\). This completes the proof.

## Verification
Run the self-contained `verify.py` using Python, NumPy and SciPy. The program checks exact finite-rank binomial identities and balanced extrema for every sign split with \(4\le m\le15\); directly forms cross-edge intersections, projects them into each random affine section, and verifies their convex hulls for dimensions three through six; checks the Hermite-corrected variance by independent Gaussian sampling; and compares both fluctuation regimes with finite-sample predictions at \(m=2400\). It prints `VERIFY_OK` followed by the diagnostic count. All these are finite diagnostics only; the uniform mathematical statements rest on the preceding analytic argument.

## Relationship to prior work
The September 11, 2026 manuscript of Ambrus and Gárgyán [1], inspected through its available full HTML text, proves an extremal **central-section volume** theorem; it does not study randomly oriented noncentral section face-count fluctuations. König [2] and Dirksen [3] investigate extremal **noncentral or near-central volumes**, again not the Haar face-vector distribution. Two publicly available notes [4,5], examined at their full scientific statements, establish the **central** Haar face-count chi-square law and its joint-rank extension. Those statements correspond to \(\lambda=0\) in (2), which is explicitly acknowledged as known; they do not imply the nonzero-offset studentization variance in (1) or the noncentral limit in (2). A related but different affine sampling rule fixes a point moving along a distinguished simplex vertex axis and chooses a Haar hyperplane **through that point**. Under that rule the signed centroid offset depends on the random normal, whereas here it is deterministic; even at the same physical displacement scale, a randomly coupled offset gives a centered scaled-square law rather than the noncentrally shifted square in (2). These statements do not imply one another by relabeling parameters. The empirical-process and Gaussian influence-function tools used here are classical, and no novelty is claimed for them individually.

The novelty assessed is the combined **noncentral affine-section geometric limit**, whose fixed-offset Gaussian fluctuations have the exact three-term variance \(\sigma_\alpha^2\), and whose displacement at scale \(m^{-1}\) induces an explicit shifted chi-square face-vector transition. An equivalent older calculation under the language of studentized Gaussian residual exceedances or random polytope sections remains a historical-priority risk; keyword searches alone do not establish uniqueness.

## Limitations
The orientation law is Haar and the vertices must form a Euclidean regular simplex. Only fixed face dimensions are treated as the ambient dimension grows; no uniform-in-rank limit, total-variation rate, or law for arbitrary nonregular simplices is claimed. The \(\alpha=0\) special case was previously published. Full texts of the most relevant cited central and noncentral geometric studies were inspected where lawfully accessible, but the completeness of historical priority is not independently certified. There is no independent mathematical audit of this finding.

## References
[1] G. Ambrus and B. Gárgyán, *Minimal central slices of the regular simplex*, arXiv:2609.12714, first submitted 11 September 2026. https://arxiv.org/html/2609.12714v2

[2] H. König, *Non-central sections of the regular n-simplex*, arXiv:2312.01325, first submitted 3 December 2023. https://arxiv.org/html/2312.01325v2

[3] H. Dirksen, *Sections of the regular simplex—Volume formulas and estimates*, Mathematische Nachrichten 290 (2017), 2567–2584. https://doi.org/10.1002/mana.201600109

[4] *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts* (2026), publicly available research note. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-mean-and-chi-square-fluctuations-of-haar-central-simplex-s--d3f9b0447a8e

[5] *Joint chi-square face-vector fluctuations of random central regular-simplex sections* (2026), publicly available research note. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-joint-chi-square-face-vector-fluctuations-of-random-central-regu--aa90c887fe90
