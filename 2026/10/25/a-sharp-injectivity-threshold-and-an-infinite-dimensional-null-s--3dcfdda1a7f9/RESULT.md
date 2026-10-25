# A sharp injectivity threshold and an infinite-dimensional null space for generalized Fock Berezin transforms

## Finding
For every finite complex dimension \(d\ge1\), every \(\alpha>0\), and every \(m>0\), the bounded-symbol Berezin transform on the generalized power-weight Fock space, as well as bounded-symbol Toeplitz quantization, is **injective exactly when \(m\ge1\)**. The two symbol maps have exactly the same kernel.

When \(0<m<1\), write \(\beta=\alpha\tan(\pi m/2)\). Every essentially bounded measurable function \(a\) on the unit sphere gives an invisible symbol:
\[
 f_a(r\omega)=a_+(\omega)\sin(\beta r^m)+a_-(\omega)\cos(\beta r^m),\quad r>0,\ \omega\in S^{2d-1},
\]
where \(a_\pm(\omega)=\big(a(\omega)\pm a(-\omega)\big)/2\). Thus \(Bf_a=0\) identically and \(T_{f_a}=0\). The map \(a\mapsto f_a\) embeds the entire \(L^\infty(S^{2d-1})\) as a closed subspace of the symbol kernel. Taking \(a\equiv1\) produces the explicit nonzero **bounded real radial** null symbol \(f(r)=\sin(\beta r^m)\), so \(1\pm\varepsilon f\) are distinct positive symbols with equal Toeplitz operator \(I\) and Berezin transform \(1\) whenever \(0<\varepsilon<1\).

## Assumptions and scope
Let \(d\in\{1,2,\ldots\}\) and \(\alpha,m>0\). Let \(\mu=\mu_{\alpha,m}^{(d)}\) be the probability measure on \(\mathbb C^d\) with density \(c_{\alpha,m,d}e^{-\alpha|w|^m}\), where
\[
 c_{\alpha,m,d}=\frac{\Gamma(d)}{\pi^d}\frac{\alpha^{2d/m}}{(2/m)\Gamma(2d/m)}.
\]
Let \(\mathcal F^2=L^2(\mu)\cap\operatorname{Hol}(\mathbb C^d)\), with orthogonal projection \(P\) and reproducing kernel \(K\). For each \(f\in L^\infty(\mu)\), define \(T_f=P M_f|_{\mathcal F^2}\) and
\[
 (Bf)(z)=\frac{1}{K(z,z)}\int_{\mathbb C^d} f(w)|K(w,z)|^2d\mu(w).
\]
Here \(L^\infty\)-equality means equality almost everywhere, and \(Bf=0\) means equality at every \(z\in\mathbb C^d\). The unit sphere has its normalized spherical measure; every angular statement is interpreted modulo null sets. This result concerns bounded symbols, not unbounded or distribution-valued Toeplitz symbols, and only finite complex dimensions.

## Proof
**1. Exact correspondence with mixed moments.** The monomials \(e_\gamma(w)=w^\gamma/\|w^\gamma\|_{\mathcal F^2}\) for multi-indices \(\gamma\in\mathbb N_0^d\) form an orthonormal basis. For bounded \(f\), the Toeplitz matrix coefficients are nonzero normalizing multiples of
\[
 M_{\gamma,\delta}(f)=\int_{\mathbb C^d} f(w)w^\gamma\overline{w^\delta}\,d\mu(w).
\]
Hence \(T_f=0\) if and only if **all** mixed moments vanish. Conversely, the reproducing kernel is a Hilbert-convergent sum of monomials. The scalar function
\[
 Q_f(z)=K(z,z)(Bf)(z)=\langle T_f K_z,K_z\rangle
\]
is real analytic, with uniquely determined coefficients equal (up to strictly positive normalizations) to \(M_{\gamma,\delta}(f)\) in its \(z\)-and-\(\bar z\) power series. Compact convergence follows from the boundedness of \(T_f\) and local boundedness of the kernel vectors, or directly by Cauchy–Schwarz. Thus \(Q_f\equiv0\) if and only if every mixed moment vanishes. Since \(K(z,z)>0\),
\[
 \ker B=\ker(f\mapsto T_f)=\{f:\ M_{\gamma,\delta}(f)=0\ \text{for all }\gamma,\delta\}.
\]

**2. Uniqueness for \(m\ge1\).** Suppose every mixed moment of bounded \(f\) vanishes and put \(d\nu=f\,d\mu\), a finite complex Borel measure on the real Euclidean space \(\mathbb R^{2d}\). All ordinary real multivariate polynomial moments of \(\nu\) vanish because each real coordinate is a linear combination of a complex coordinate and its conjugate. For \(m\ge1\), choose \(c>0\) sufficiently small (any \(0<c<\alpha\) if \(m=1\)); then
\[
 \int_{\mathbb R^{2d}}e^{c|x|}\,d|\nu|(x)<\infty.
\]
For each \(v\in\mathbb R^{2d}\), the function \(t\mapsto\int e^{it\langle v,x\rangle}\,d\nu(x)\) extends holomorphically to a strip around the real axis. Every derivative at zero vanishes by the moment assumption, so analytic continuation makes this function zero for all real \(t\). Consequently the Fourier transform of \(\nu\) is identically zero, and Fourier uniqueness gives \(\nu=0\), hence \(f=0\) almost everywhere. The endpoint \(m=1\) is included.

**3. Nonzero symbols when \(0<m<1\).** Put \(\theta=\pi m/2\in(0,\pi/2)\) and \(\beta=\alpha\tan\theta\). For every integer \(n\ge0\), the radial factors appearing in degree-\(n\) mixed moments are
\[
 I_n^s=\int_0^\infty r^{2d+n-1}e^{-\alpha r^m}\sin(\beta r^m)\,dr,
\qquad I_n^c=\int_0^\infty r^{2d+n-1}e^{-\alpha r^m}\cos(\beta r^m)\,dr.
\]
Substitute \(t=r^m\) and use the convergent complex Gamma integral (the real part of \(\alpha-i\beta\) is positive):
\[
 I_n^c+iI_n^s=\frac{\Gamma((2d+n)/m)}{m}(\alpha-i\beta)^{-(2d+n)/m}.
\]
The principal argument of \(\alpha-i\beta\) is \(-\theta\). Therefore the phase of this expression is \((2d+n)\pi/2\); **\(I_n^s=0\) for every even \(n\)**, whereas **\(I_n^c=0\) for every odd \(n\)**.

Write \(w=r\omega\) and let \(p_{\gamma\delta}(\omega)=\omega^\gamma\overline{\omega^\delta}\), of degree \(n=|\gamma|+|\delta|\) under \(\omega\mapsto-\omega\). Then \(p_{\gamma\delta}\) is even for even \(n\) and odd for odd \(n\). Because \(a_+\) is even and \(a_-\) is odd, the angular integral of \(a_-p_{\gamma\delta}\) vanishes for even \(n\), and that of \(a_+p_{\gamma\delta}\) vanishes for odd \(n\). The remaining radial factor vanishes by the preceding Gamma calculation. Every mixed moment of \(f_a\) is zero. Step 1 establishes both \(Bf_a=0\) and \(T_{f_a}=0\).

**4. A closed infinite-dimensional kernel.** The map \(J:a\mapsto f_a\) is linear, and
\[
 \tfrac12\|a\|_\infty\le\|Ja\|_\infty\le2\|a\|_\infty.
\]
For the lower bound, fix almost every \(\omega\). As \(r\) varies, \(\beta r^m\) takes all positive values. Evaluating the essential radial supremum arbitrarily near phases \(0\) and \(\pi/2\) gives \(\|Ja\|_\infty\ge\max\{|a_+(\omega)|,|a_-(\omega)|\}\ge|a(\omega)|/2\). The upper bound follows from \(|a_\pm|\le\|a\|_\infty\). Thus \(J\) has closed range and is an isomorphic embedding of the infinite-dimensional space \(L^\infty(S^{2d-1})\) into the common kernel.

**5. Positive-symbol degeneracy.** With \(a\equiv1\), \(f_a\) is real, nonzero, and has \(\|f_a\|_\infty=1\). For \(0<\varepsilon<1\), both \(1+\varepsilon f_a\) and \(1-\varepsilon f_a\) are strictly positive essentially bounded symbols. Their Toeplitz operators both equal \(I\), and their Berezin transforms both equal \(1\), despite the distinct symbols. This completes the sharp dichotomy.

## Verification
The Gamma-integral phase is exact, not asymptotic. The self-contained `verify_moments.py` exercises parity identities for several dimensions, decay exponents, scales and moment degrees using standard-library complex arithmetic, and tests elementary norm bounds for representative angular profiles. These finite checks provide diagnostics but are **not** the proof of any infinite-dimensional assertion. Every norm estimate, moment quantifier, and uniqueness step used in the theorem is analytical and appears above.

## Relationship to prior work
Tian (2026) introduces precisely these normalized power-weight Fock Berezin transforms and classifies parameter rigidity and multiplication/commutation of their products. His main conclusions distinguish the Gaussian exponent \(m=2\), whereas the **bounded-symbol faithfulness threshold** here is \(m=1\). The two properties are different and neither implies the other.

The Gaussian Fock literature of Grudsky and Vasilevski (2002) contains nonzero, generally **unbounded** radial symbols yielding zero Toeplitz operators, along with a uniqueness theorem for symbols with sufficient exponential integrability. Those results do not produce bounded null symbols for the present subexponential power weight. Bommier-Hato (2010) obtains Lipschitz estimates for operator Berezin symbols on the same power-weight scale, not this symbol-map dichotomy. Bdarneh (2026) describes radial/quasi-radial Toeplitz spectral decompositions for general radial weights, but does not derive the sharp bounded-symbol injectivity threshold or the angular closed kernel. Looi (2026) gives oscillatory bounded Gaussian examples separating asymptotic Berezin positivity from essential positivity; those operators are not identically zero.

Classical moment indeterminacy and Stieltjes-type trigonometric perturbations explain the basic radial oscillatory mechanism; that mechanism itself is **not** asserted to be new. The claim here is the operator-level all-dimensional sharp equivalence and the explicit closed nonradial \(L^\infty\) family of null symbols.

## Limitations
The theorem is for bounded measurable symbols, not arbitrary growth classes, signed distributional symbols or singular weights. It does not characterize the entire common null space when \(0<m<1\), nor assert any stability or inverse bound in the injective regime. The construction permits discontinuous angular profiles and gives no Sobolev/smoothness classification. Historical priority for more abstract determinacy-to-Toeplitz equivalences requires independent examination; none is claimed to have been ruled out exhaustively.

## References
1. H. Tian, *Products of Berezin Transforms on Generalized Fock Spaces*, arXiv:2610.14599v1 (first public 10 October 2026), https://arxiv.org/html/2610.14599v1 .
2. H. Bommier-Hato, *Lipschitz estimates for the Berezin transform*, Journal of Function Spaces and Applications 8 (2010), 103–128, https://doi.org/10.1155/2010/461315 .
3. S. M. Grudsky and N. L. Vasilevski, *Toeplitz operators on the Fock space: radial component effects*, Integral Equations and Operator Theory 44 (2002), 10–37, https://doi.org/10.1007/BF01197858 .
4. K. Bdarneh, *Toeplitz C*-algebras on radially weighted Fock spaces: commutativity and spectral representation*, arXiv:2609.20652v2, https://arxiv.org/abs/2609.20652 .
5. S. Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879v1, https://arxiv.org/html/2603.10879v1 .
6. Z. Lin, Y. Lu, C. Zu, *A Fourier Criterion for Recognizing Toeplitz Operators on Fock Spaces*, arXiv:2607.04102, https://arxiv.org/abs/2607.04102 (Gaussian case, public abstract consulted).
