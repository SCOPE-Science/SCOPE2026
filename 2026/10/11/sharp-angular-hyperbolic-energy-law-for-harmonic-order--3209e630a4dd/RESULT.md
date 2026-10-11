# Sharp angular hyperbolic-energy law for harmonic order

## Finding

**Theorem (exact first angular moment and sharp radial order bound).** Let \(f=h+\overline{g}\) be any sense-preserving, locally univalent harmonic mapping on the unit disk \(\mathbb D\), with analytic dilatation \(\omega=g'/h':\mathbb D\to\mathbb D\). Define its harmonic order operator by
\[
A_f(z)=\frac{1-|z|^2}{2}\left(\frac{h''(z)}{h'(z)}-\frac{\overline{\omega(z)}\omega'(z)}{1-|\omega(z)|^2}\right)-\overline z.
\]
For every \(0<r<1\), the following **exact** identity holds, with planar Lebesgue area \(dA\):
\[
\frac{1}{2\pi}\int_0^{2\pi}e^{i\theta}A_f(re^{i\theta})\,d\theta
=-r-\frac{1-r^2}{2\pi r}\int_{|z|<r}\frac{|\omega'(z)|^2}{(1-|\omega(z)|^2)^2}\,dA(z).
\tag{1}
\]
Consequently,
\[
\max_{|z|=r}|A_f(z)|\ge r+\frac{1-r^2}{2\pi r}\int_{|z|<r}\frac{|\omega'(z)|^2}{(1-|\omega(z)|^2)^2}\,dA(z)\ge r.
\tag{2}
\]
For every \(r\) and every \(a\in\mathbb D\), **equality holds in the first inequality of (2)** for the nontrivial harmonic shear \(f_a(z)=z+\overline{a z^2/2}\). Thus the energy correction, not merely the radius term, has sharp coefficient and is strictly positive whenever \(\omega\) is nonconstant.

**Rigidity application.** The inequality in Theorem 2 of Efraimidis--Hernández (2026),
\[
(1-|z|^2)^2|S_f(z)|+2|\omega^*(z)A_f(z)|\le\frac12|\omega^*(z)|^2\quad(z\in\mathbb D),
\tag{3}
\]
where \(\omega^*(z)=(1-|z|^2)\omega'(z)/(1-|\omega(z)|^2)\) and \(S_f=(P_f)_z-P_f^2/2\), is satisfied **if and only if** \(f\) is an affine harmonic image of a Möbius map: \(f(z)=M(z)+\overline{cM(z)}+C\), with \(|c|<1\), \(C\in\mathbb C\), and \(M\) nonconstant Möbius and holomorphic on \(\mathbb D\). The new quantitative content is (1)--(2); the classification also follows directly by combining the earlier universal order bound with the 2026 criterion.

## Assumptions and scope

The hypothesis \(J_f=|h'|^2-|g'|^2>0\) implies \(h'(z)\ne0\) throughout \(\mathbb D\) and \(|\omega(z)|<1\). No boundary smoothness, quasiconformal extension, global univalence, normalization at zero, or finite energy on the whole disk is assumed. For each fixed \(r<1\), the integrals in (1)--(2) are finite by holomorphicity and compact containment. The circlewise maximum exists by continuity. The Schwarzian \(S_f\) in (3) is the harmonic Schwarzian from the indicated Jacobian pre-Schwarzian, not the minimal-surface Schwarzian.

## Proof

**1. Subharmonic logarithm of the dilatation defect.** Put
\[
u(z)=-\log(1-|\omega(z)|^2),\qquad H(z)=\frac{h''(z)}{h'(z)}.
\]
The function \(H\) is holomorphic on \(\mathbb D\), whereas \(u\) is real-valued and smooth. Ordinary Wirtinger differentiation, using \(\partial_z\overline{\omega(z)}=0\), yields
\[
u_z=\frac{\overline\omega\omega'}{1-|\omega|^2},\qquad
u_{z\bar z}=\frac{|\omega'|^2}{(1-|\omega|^2)^2},\qquad
\Delta u=\frac{4|\omega'|^2}{(1-|\omega|^2)^2}.
\tag{4}
\]
In particular, \(A_f(z)=\frac{1-|z|^2}{2}(H(z)-u_z(z))-\overline z\).

**2. Extract the angular Fourier mode.** Define the circular mean
\[
U(r)=\frac{1}{2\pi}\int_0^{2\pi}u(re^{i\theta})\,d\theta.
\]
Since \(H\) is holomorphic, its Taylor series shows
\[
\frac1{2\pi}\int_0^{2\pi}e^{i\theta}H(re^{i\theta})\,d\theta=0.
\]
Wirtinger polar differentiation gives \(e^{i\theta}u_z=(u_r-i u_\theta/r)/2\). The circular angular derivative integrates to zero, hence
\[
\frac1{2\pi}\int_0^{2\pi}e^{i\theta}u_z(re^{i\theta})\,d\theta=\frac12 U'(r).
\]
Moreover \(e^{i\theta}\overline{re^{i\theta}}=r\). Combining these identities,
\[
\frac{1}{2\pi}\int_0^{2\pi}e^{i\theta}A_f(re^{i\theta})\,d\theta
=-r-\frac{1-r^2}{4}U'(r).
\tag{5}
\]

**3. Convert the radial derivative to hyperbolic energy.** The divergence theorem on the disk \(|z|<r\), followed by (4), gives
\[
2\pi r U'(r)=\int_{|z|<r}\Delta u(z)\,dA(z)
=4\int_{|z|<r}\frac{|\omega'(z)|^2}{(1-|\omega(z)|^2)^2}\,dA(z).
\tag{6}
\]
Substituting (6) into (5) proves (1). The right side of (1) is real and nonpositive, so its modulus is the full positive expression in (2). The modulus of a first angular average cannot exceed the largest modulus of its integrand, proving (2). If \(\omega\) is nonconstant, its derivative is nonzero on some open subset of every centered disk, so the extra integral is positive.

**4. Sharpness on every circle.** Fix \(|a|<1\). For \(h(z)=z\) and \(g(z)=a z^2/2\), the dilatation is \(\omega(z)=az\) and
\[
A_{f_a}(re^{i\theta})=-re^{-i\theta}\left(1+\frac{|a|^2(1-r^2)}{2(1-|a|^2r^2)}\right).
\tag{7}
\]
The integrand in the angular moment therefore has constant phase and the triangle estimate in (2) is exact. These witnesses are even globally injective: for any distinct points in the disk, the modulus of the coanalytic increment is at most \(|a|\) times the modulus of the analytic increment, so their sum cannot vanish. Direct integration shows
\[
\int_{|z|<r}\frac{|\omega'(z)|^2}{(1-|\omega(z)|^2)^2}\,dA(z)
=\frac{\pi |a|^2r^2}{1-|a|^2r^2},
\]
which matches (7). The coefficient of the energy term is attained for every fixed nonzero \(a\) and \(r\); it cannot be increased in an inequality of that precise form.

**5. Application to the 2026 criterion.** If \(\omega\) is nonconstant, the zeros of \(\omega'\) are isolated. Dropping the nonnegative Schwarzian term in (3) and dividing where \(\omega^*\ne0\) gives
\[
|A_f(z)|\le\frac14|\omega^*(z)|\le\frac14
\]
by Schwarz--Pick. Continuity extends this bound over the isolated zeros. However (2) with, for example, \(r=1/2\) gives \(\max_{|z|=1/2}|A_f(z)|\ge1/2\), a contradiction. Thus \(\omega\equiv c\in\mathbb D\). Then \(P_f=h''/h'\) and \(S_f=S_h\); (3) reduces to \(S_h\equiv0\), so \(h=M\) is nonconstant Möbius, and \(g=cM+\mathrm{constant}\). Conversely every such affine harmonic Möbius image has \(\omega^*\equiv0\) and \(S_f\equiv0\) and hence satisfies (3). This completes the characterization.

## Verification

Each equality (4)--(6) follows from direct differentiation and the disk divergence theorem; no computation or finite experiment is used as a substitute for their all-radius proof. The sharpness identity (7) can be checked independently in exact rational arithmetic for arbitrary rational test parameters; `checks/model_examples.py` replays such test instances using the two symbolic expressions, while the general equality follows algebraically from (7). The normalization of the area measure and the factor \(2\pi r\) in (6) are explicit. The constant-dilatation boundary case and nonconstant shears have both been covered.

## Relationship to prior work

Efraimidis and Hernández, *Harmonic mappings, univalence criteria and a theorem of Lehtinen* (arXiv:2604.00269v1, first public 2026-03-31), introduce precisely the harmonic operator and inequality (3) in Theorem 2 and ask whether non-Möbius examples exist. Their article proves injectivity under (3), not the radial energy identity (1). Sobczak-Kneć, Starkov, and Szynal (2011, Corollary 3.5) and Arbeláez, Hernández, and Sierra (arXiv:2107.01756v1, Proposition 3) already establish the universal global bound \(\sup_{\mathbb D}|A_f|\ge1\). **Combining that known bound with (3) already establishes the classification in step 5**; novelty is not claimed for that logical consequence alone. The additional sharp identity (1), with its explicitly positive dilatation-energy remainder for each radius, is a stronger, circlewise quantitative statement not contained in those previously inspected results. Hernández and Martín (arXiv:1210.2330) provide the harmonic pre-Schwarzian/Schwarzian definitions underlying the calculation.

## Limitations

The theorem does not calculate the harmonic inner radius of univalence, resolve the separate conjectures about it, or quantify a stability distance to Möbius maps for near-satisfaction of (3). The radial energy integral is not asserted finite as \(r\uparrow1\). Global sharpness is proved only for the specifically stated circular estimate (2); there is no claim of unique extremizers among all maps. No independently performed assessment is represented here. As with other literature-led results, undiscovered equivalent radial-energy formulas remain possible.

## References

1. I. Efraimidis and R. Hernández, *Harmonic mappings, univalence criteria and a theorem of Lehtinen*, arXiv:2604.00269v1 (2026-03-31), DOI: 10.1007/s41478-026-01157-y; specifically Section 4, Theorem 2 and the following open question.
2. M. Sobczak-Kneć, V. V. Starkov, and J. Szynal, *Old and new order of linear invariant family of harmonic mappings and the bound for Jacobian*, Annales UMCS Mathematica **65** (2011), 191--202, DOI: 10.2478/v10062-011-0024-3; specifically Corollary 3.5.
3. H. Arbeláez, R. Hernández, and W. Sierra, *Lower and upper order of harmonic mappings*, arXiv:2107.01756v1 (2021), subsequently J. Math. Anal. Appl. **507** (2022), 125837; specifically Section 5, Proposition 3.
4. R. Hernández and M. J. Martín, *Pre-Schwarzian and Schwarzian derivatives of harmonic mappings*, arXiv:1210.2330v1, subsequently J. Geom. Anal. **25** (2015), 64--91.
