# Arithmetic rigidity and sharp stability of harmonic Hardy endpoint extremizers
## Finding
Let \(S\subset\mathbb N\) be any finite nonempty set of positive integers; fix \(n_0\in S\). Define the positive integer
\[
d=\gcd\bigl(\{2n_0\}\cup\{n-n_0:n\in S\}\bigr).
\]
For each nonzero harmonic function \(f=h+\overline g\in\mathbf h^1(\mathbb D)\), write
\[
h(z)=\sum_{j\ge0}a_jz^j,\qquad g(z)=\sum_{j\ge1}b_jz^j,
\qquad \|f\|_1=\sup_{0\le r<1}\int_\mathbb T|f(r\zeta)|\,dm(\zeta).
\]
Here \(dm=dt/(2\pi)\). Let \(\mu\) be its unique finite complex boundary measure, so that \(f=P[\mu]\). Assume \(\|f\|_1=\|\mu\|_{\rm TV}=1\). Then the following exact classification holds:
\[
|a_n|+|b_n|=2\quad\text{for every }n\in S
\]
if and only if, for some \(t_0\in\mathbb R\), \(c\in\mathbb T\), and nonnegative \(\lambda_0,\ldots,\lambda_{d-1}\) summing to one,
\[
\mu=c\sum_{j=0}^{d-1}\lambda_j
 e^{in_0(t_0+2\pi j/d)}\delta_{e^{i(t_0+2\pi j/d)}}.
\tag{1}
\]
In particular, the largest possible number of distinct boundary Poisson poles in a simultaneous extremizer is exactly \(d\), achieved by all positive weights. For \(S=\{1,2\}\), only unimodular single Poisson kernels extremize both orders, whereas for \(S=\{1,3\}\) there are genuine two-pole mixtures.

The equality classification has a *sharp square-root stability refinement*. Write \(d\mu=u\,d\rho\) with \(|u|=1\) \(\rho\)-almost everywhere, where \(\rho=|\mu|\) is a probability measure. Let
\[
\varepsilon=\max_{n\in S}\left(2-|a_n|-|b_n|\right),\qquad 0\le\varepsilon<\tfrac12.
\]
Define \(L=\{n,-n:n\in S\}\) and, for every \(\ell\in L\), the nonzero normalized Fourier coefficient
\[
c_\ell=\frac{\widehat\mu(\ell)}{|\widehat\mu(\ell)|},\qquad
\widehat\mu(\ell)=\int_\mathbb T e^{-i\ell t}\,d\mu(e^{it}).
\]
Choose integers \(k_\ell\), indexed by \(\ell\in L\setminus\{n_0\}\), satisfying the Bézout identity
\[
\sum_{\ell\ne n_0}k_\ell(\ell-n_0)=d,
\qquad B=\sum_{\ell\ne n_0}|k_\ell|.
\]
Choose \(t_0\) so that
\[
e^{-idt_0}=\prod_{\ell\ne n_0}
(c_\ell\overline{c_{n_0}})^{k_\ell},
\qquad E=\{t_0+2\pi j/d:0\le j<d\}\pmod{2\pi}.
\]
Then, denoting angular geodesic distance on \(\mathbb T\) by \(\operatorname{dist}_{\mathbb T}\),
\[
\left(\int\operatorname{dist}_{\mathbb T}(t,E)^2\,d\rho(t)\right)^{1/2}
\le\frac{\pi\sqrt2 B}{d}\sqrt\varepsilon,\tag{2}
\]
and
\[
\left(\int|u(t)-c_{n_0}e^{in_0t}|^2\,d\rho(t)\right)^{1/2}
\le\sqrt{2\varepsilon}.\tag{3}
\]
More concretely, there exists a measure \(\mu_*\) of the exact extremal form (1) such that
\[
\sup_{\substack{\|\varphi\|_\infty\le1\\\operatorname{Lip}(\varphi)\le1}}
\left|\int\varphi\,d\mu-\int\varphi\,d\mu_*\right|
\le\left(\sqrt2+\frac{\pi\sqrt2 B(n_0+1)}d\right)\sqrt\varepsilon.\tag{4}
\]
The \(\sqrt\varepsilon\) exponent in (2), and hence in the geometric stability assertion, cannot be improved for fixed \(S\).

## Assumptions and scope
The space \(\mathbf h^1(\mathbb D)\) consists of complex-valued harmonic functions with finite radial \(L^1\) norm. Its boundary representing object is a finite complex *measure*, not necessarily an \(L^1\) function; point-mass Poisson kernels belong to this space. All measures use the unscaled circle convention \(P[\delta_{e^{it}}](0)=1\), and \(\delta\) means unit point mass. The Fourier identity is \(a_n=\widehat\mu(n)\) and \(\overline{b_n}=\widehat\mu(-n)\), so absolute values agree. The classification is for *all* finite nonempty \(S\); weights in (1) may vanish, and \(d\) is independent of which \(n_0\in S\) is selected. For (2)–(4), choose any valid integer Bézout certificate; constants depend on that choice. No estimate is asserted uniformly in \(S\). The Lipschitz norm in (4) uses shortest angular distance in radians.

## Proof
**Boundary-measure isometry.** If \(f\in\mathbf h^1\), the measures \(f(r e^{it})\,dm(t)\) have uniformly bounded variation. Their weak-* cluster points are finite complex measures. Harmonic Fourier coefficient identities show that each cluster point has the same Fourier coefficients; trigonometric polynomials are uniformly dense in continuous functions, so this determines one measure \(\mu\), and \(f=P[\mu]\). Conversely, \(\int|P_r*\mu|\,dm\le\|\mu\|_{\rm TV}\) for every \(r\); weak-* lower semicontinuity of total variation on \(r\uparrow1\) gives \(\|\mu\|_{\rm TV}\le\sup_r\int|P_r*\mu|dm\). Hence equality of the two norms.

**Exact equality set.** Put \(d\mu=u\,d\rho\). For each integer \(\ell\),
\[
|\widehat\mu(\ell)|\le\int|u e^{-i\ell t}|\,d\rho=1.
\]
Thus \(|a_n|+|b_n|=2\) holds if and only if \(|\widehat\mu(n)|=|\widehat\mu(-n)|=1\). Equality in the integral triangle inequality is equivalent to \(u(t)e^{-i\ell t}=c_\ell\) for \(\rho\)-almost all \(t\). Divide the equalities for \(\ell\in L\) by that for \(n_0\), obtaining
\[
e^{-i(\ell-n_0)t}=c_\ell\overline{c_{n_0}}\qquad(\ell\in L).
\]
The differences generate the integer ideal \(d\mathbb Z\), since \(L=\{\pm n:n\in S\}\) and \(d\) equals the gcd of \(2n_0\) and \(n-n_0\): indeed \((-n)-n_0=-(n-n_0)-2n_0\). A Bézout combination yields \(e^{-idt}=e^{-idt_0}\) on the support. Therefore \(\rho\) is supported on the \(d\) points \(E\), and \(u=c_{n_0}e^{in_0t}\). This is (1). Conversely, for every \(\ell\in L\), \(d\) divides \(\ell-n_0\), so \(u e^{-i\ell t}\) is constant on \(E\), yielding \(|\widehat\mu(\ell)|=1\). Taking all \(\lambda_j>0\) realizes exactly \(d\) poles.

**Quantitative phase stability.** For \(\ell\in L\), each individual deficit \(1-|\widehat\mu(\ell)|\) is nonnegative and no greater than \(\varepsilon\). For \(w_\ell(t)=u(t)e^{-i\ell t}\), the identity
\[
\int|w_\ell-c_\ell|^2\,d\rho=2(1-|\widehat\mu(\ell)|)\le2\varepsilon
\]
is exact. At \(\ell=n_0\) it proves (3). For any other \(\ell\), using \(|w_\ell|=|c_\ell|=1\) and the \(L^2\) triangle inequality gives
\[
\left\|e^{-i(\ell-n_0)t}-c_\ell\overline{c_{n_0}}\right\|_{L^2(\rho)}\le2\sqrt{2\varepsilon}.
\]
For unit-modulus variables \(z,w\) and any integer \(k\), \(|z^k-w^k|\le|k|\,|z-w|\). Multiplying the Bézout identities and telescoping proves
\[
\left\|e^{-idt}-e^{-idt_0}\right\|_{L^2(\rho)}\le2B\sqrt{2\varepsilon}.
\]
At the nearest point of \(E\), let \(\delta=\operatorname{dist}_{\mathbb T}(t,E)\le\pi/d\). Then
\[
|e^{-idt}-e^{-idt_0}|=2\sin(d\delta/2)\ge(2d/\pi)\delta,
\]
because \(\sin x\ge2x/\pi\) for \(0\le x\le\pi/2\). Integration proves (2).

**Nearby exact extremizer.** Choose a measurable nearest-point map \(\pi_E:\mathbb T\to E\) (settle ties by index), and define
\[
\mu_*=(\pi_E)_*\bigl(c_{n_0}e^{in_0\pi_E(t)}\,\rho(dt)\bigr).
\]
Its total variation equals one, it has the form (1), and it extremizes every coefficient order in \(S\). For every test function as in (4), decompose its integrand difference into the phase defect \(|u-c_{n_0}e^{in_0t}|\), the test displacement \(|\varphi(t)-\varphi(\pi_E(t))|\), and the phase displacement \(|e^{in_0t}-e^{in_0\pi_E(t)}|\). These are bounded, respectively, in mean by \(\sqrt{2\varepsilon}\), \(\int\delta\,d\rho\), and \(n_0\int\delta\,d\rho\). Cauchy–Schwarz and (2) yield (4).

**Optimality of square-root rate.** For fixed \(S\), let \(\mu_s=\tfrac12(\delta_1+\delta_{e^{is}})\), with \(s>0\) small enough that \(ns<\pi\) for all \(n\in S\). Then \(|\widehat\mu_s(\pm n)|=\cos(ns/2)\), and
\[
\varepsilon_s=\frac{(\max S)^2s^2}{4}+O_S(s^4).
\]
For all sufficiently small \(s\), the infimum over *all* translated \(d\)-point cosets of the \(L^2(\rho_s)\) distance is \(s/2\), attained by placing a coset point halfway between the two atoms. (If they project to distinct coset points, the separating circle distance is bounded below independently of \(s\), so such a projection is worse for small \(s\).) Thus the order in (2) cannot be smaller than \(\sqrt\varepsilon\).

## Verification
All steps establishing the infinite theorem are analytic: boundary measure representation, rigidity of equality in a complex integral, integer Bézout identities, elementary circle geometry, and Cauchy–Schwarz. The accompanying standard-library script `verify_endpoint_rigidity.py` checks discrete-support exact extremizers in 135 cases, quantitative phase and coset bounds in 180 randomized finite cases, and sharpness asymptotics in 15 finite cases. It printed `PASS: 135 exact-support checks, 180 quantitative checks, 15 sharpness checks`. These checks do not replace the analytic proof or certify every infinite-dimensional case.

## Relationship to prior work
Chen, Huang, Jin, and Li (arXiv:2609.33159v1; first public September 27, 2026; primary MSC 31A05) prove the sharp bound \(|a_n|+|b_n|\le2\|f\|_1\) in Theorem 1.3. Their page 12 shows that a *single* Poisson kernel attains equality for every \(n\); they do not classify all simultaneous equality measures, determine the gcd-dependent maximal number of poles, or give a uniform quantitative near-equality theorem for any finite index set. The formerly published result “Extremizer spectrum and index rigidity for sharp harmonic Hardy coefficients” (published-finding corpus record 2026/10/4/SCOPE-extremizer-spectrum-and-index-rigidity-for-sharp-harmonic-hardy--16ebd1a33be1) proves a converse equality classification only for \(1<p<\infty\) and proves *incompatibility* of two indices in that range; its explicit endpoint exclusion is essential, as the classification here exhibits extensive simultaneous equality at \(p=1\). Earlier Chen–Ponnusamy–Wang (2012) give previous coefficient estimates and a \(p=\infty\) extremal description, not the sharp \(\mathbf h^1\) simultaneous equality-and-stability theorem. A 2026 paper by Shi, Li, and Lian on prescribed \(L^p\) boundary data is a plausible related source, but only abstract-level material was accessible; its stated \(L^p\) boundary-data hypothesis does not subsume the atomic \(\mathbf h^1\) extremizers here. The elementary triangle-equality and Bézout ingredients are classical and not individually claimed new. The claim is the full finite-index arithmetic phase diagram *together with* its sharp quantitative rigidity statement.

## Limitations
The theorem does not assert a total-variation distance bound between \(\mu\) and \(\mu_*\): displaced atoms have large total-variation distance. The bounded-Lipschitz metric is used deliberately. Stability constants can be large and depend on the selected Bézout identity; no best constant is claimed. The bound \(\varepsilon<1/2\) guarantees the phase ratios exist, rather than being an optimal threshold. No claim for infinite index sets or for \(\mathbf h^p\) at \(p\ne1\) is made. An unindexed or inaccessible equivalent stability formulation in the measure-theoretic Fourier literature remains an originality risk. For a nonzero ordinary \(L^1\) boundary density, simultaneous exact equality is impossible, since the equality measure must be supported on finitely many points; the ambient harmonic Hardy space includes these singular Poisson extensions.

## References
1. S. Chen, M. Huang, L. Jin, Q. Li, “Sharp constant problems for harmonic mappings,” arXiv:2609.33159v1, September 27, 2026, Theorem 1.3 and proof, pp. 4–5, 10–13.
2. “Extremizer spectrum and index rigidity for sharp harmonic Hardy coefficients,” published-finding corpus, public record `2026/10/4/SCOPE-extremizer-spectrum-and-index-rigidity-for-sharp-harmonic-hardy--16ebd1a33be1` (2026), especially Finding, Scope, Proof and Limitations.
3. S. Chen, S. Ponnusamy, X. Wang, “Integral means and coefficient estimates on planar harmonic mappings,” Annales Academiae Scientiarum Fennicae Mathematica 37 (2012), 69–79, doi:10.5186/aasfm.2012.3707.
4. Q. Shi, X. Li, X. Lian, “Estimates on the Schwarz Lemma and Landau Theorem for a Harmonic Mapping with a Given Boundary Function in Lebesgue Space,” Computational Methods and Function Theory (2026), doi:10.1007/s40315-025-00600-8 (abstract and publisher preview only).
