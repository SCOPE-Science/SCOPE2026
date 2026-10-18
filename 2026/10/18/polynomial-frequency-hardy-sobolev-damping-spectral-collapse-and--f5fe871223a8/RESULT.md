# Polynomial-frequency Hardy–Sobolev damping: spectral collapse and a sharp power threshold

## Finding
Let \(n\ge 1\) be an integer, \(a>1\), and \(b\ge0\). On the upper half-plane \(\mathbb C_+=\{z:\operatorname{Im}z>0\}\), equip the Hilbert Hardy–Sobolev space
\[
\mathcal H_n=\{F\text{ holomorphic on }\mathbb C_+:F^{(j)}\in H^2(\mathbb C_+),\ 0\le j\le n\}
\]
with \(\|F\|_{\mathcal H_n}^2=\sum_{j=0}^n\|F^{(j)}\|_{H^2}^2\), using boundary-Lebesgue normalization of \(H^2\). Write
\[
p_n(s)=\sum_{j=0}^n s^{2j},\qquad (T_b F)(z)=F(az+ib).
\]
All the \(T_b\) are bounded. Their spectra equal their Fredholm essential spectra, with the following sharp dichotomy:
\[
\sigma(T_0)=\sigma_{\mathrm{ess}}(T_0)
=\{\lambda\in\mathbb C:a^{-1/2}\le |\lambda|\le a^{n-1/2}\},
\]
\[
\sigma(T_b)=\sigma_{\mathrm{ess}}(T_b)
=\{\lambda\in\mathbb C:|\lambda|\le a^{-1/2}\}\quad(b>0).
\]
For each positive integer \(m\),
\[
\|T_0^m\|=a^{m(n-1/2)}.
\]
For \(b>0\), set
\[
K_{n,a}(b)=\max_{s\ge0} e^{-2bs/(a-1)}p_n(s),\qquad
b_*(n,a)=\frac{a-1}{2}\max_{s>0}\frac{\log p_n(s)}s.
\]
The maximum defining \(b_*\) is finite, positive, and attained. The **normalized power limit** and its sharp damping threshold are
\[
\lim_{m\to\infty}a^{m/2}\|T_b^m\|=\sqrt{K_{n,a}(b)},\qquad
K_{n,a}(b)=1\ \Longleftrightarrow\ b\ge b_*(n,a).
\]
As \(b\downarrow0\),
\[
\sqrt{K_{n,a}(b)}\sim\left(\frac{n(a-1)}{e b}\right)^n.
\]
Although \(T_b\to T_0\) strongly as \(b\downarrow0\), the exact distance remains
\[
\|T_b-T_0\|=a^{n-1/2}\quad\text{for every }b>0.
\]
Thus positive vertical displacement collapses a Sobolev-order-dependent annulus to a universal disk, while a finite critical displacement removes all excess normalized power amplification. Spectral radii are discontinuous at zero displacement.

## Assumptions and scope
All statements hold for each **fixed** integer \(n\ge1\), real \(a>1\), and real \(b\ge0\), without limiting the dimension of \(\mathcal H_n\). The spectral notions are the complex operator spectrum and the Fredholm essential spectrum, defined by failure of \(T_b-\lambda I\) to be Fredholm. The perturbation has positive imaginary translation \(ib\); negative \(b\) would not map the upper half-plane to itself. Neither complex dilation nor arbitrary nonaffine symbols are covered.

## Proof
**Fourier model and exact powers.** The Paley–Wiener theorem for these derivative Hardy–Sobolev spaces [1] identifies \(\mathcal H_n\) unitarily with \(L^2((0,\infty),p_n(s)\,ds)\), via
\[
F(z)=\frac1{\sqrt{2\pi}}\int_0^\infty e^{isz}f(s)\,ds.
\]
Then \(T_b\) corresponds to the weighted dilation
\[
(A_bf)(s)=\frac1a e^{-bs/a}f(s/a).
\]
Its \(m\)-th iterate corresponds to composition with \(a^m z+ib(a^m-1)/(a-1)\), hence a change of variables gives the **operator-norm identity**
\[
\|T_b^m\|^2=a^{-m}\mathop{\operatorname{ess\,sup}}_{s>0}
 e^{-\frac{2b(1-a^{-m})}{a-1}s}\frac{p_n(s)}{p_n(a^{-m}s)}.\tag{1}
\]
The continuous expression has the same supremum. For \(b=0\), the ratio is no greater than \(a^{2nm}\) term by term, and it tends to this value at infinity. Consequently \(\|T_0^m\|=a^{m(n-1/2)}\). Its inverse is dilation by \(a^{-1}\), and the same change of variables yields \(\|T_0^{-m}\|=a^{m/2}\). Spectral-radius and inverse-spectral-radius bounds imply
\[
\sigma(T_0)\subseteq \{a^{-1/2}\le|\lambda|\le a^{n-1/2}\}.
\]

**The entire undamped annulus is essential.** The adjoint on the Fourier side satisfies
\[
(A_0^*g)(t)=\frac{p_n(at)}{p_n(t)}g(at).
\]
For arbitrary \(\gamma\in\mathbb C\) with \(-1/2<\operatorname{Re}\gamma<n-1/2\),
\[
g_\gamma(t)=\frac{t^\gamma}{p_n(t)}
\]
belongs to the weighted \(L^2\)-space: at zero the integrand in \(\|g_\gamma\|^2\) behaves as \(t^{2\operatorname{Re}\gamma}\), while at infinity it behaves as \(t^{2\operatorname{Re}\gamma-2n}\). Direct substitution proves \(A_0^*g_\gamma=a^\gamma g_\gamma\). Multiply \(g_\gamma\) by arbitrarily many linearly independent bounded measurable functions \(h\) with \(h(at)=h(t)\); these remain adjoint eigenfunctions. Such \(h\) arise from disjoint subsets of a multiplicative fundamental interval \([1,a)\), extended under powers of \(a\). Thus every point in the open annulus is an eigenvalue of the adjoint of infinite geometric multiplicity; its complex conjugate belongs to the Fredholm essential spectrum of \(T_0\). As the annulus is invariant under conjugation, the full open annulus is contained in the essential spectrum. Since the essential spectrum is closed, the boundary circles are included too. This proves the first spectral equality.

**The positive-displacement disk and normalized powers.** Fix \(b>0\). For \(m\ge1\) the supremand after removing \(a^{-m}\) in (1) converges pointwise to
\[
e^{-2bs/(a-1)}p_n(s).
\]
For all sufficiently large \(m\), its tail is uniformly bounded by \(e^{-bs/(a-1)}p_n(s)\), which tends to zero at infinity; convergence is uniform on compact \(s\)-intervals (including zero). Therefore the suprema converge to \(K_{n,a}(b)\) and the stated normalized-power limit follows. In particular \(r(T_b)=a^{-1/2}\).

For any \(\gamma\in\mathbb C\) satisfying \(\operatorname{Re}\gamma>-1/2\), the Fourier function
\[
f_\gamma(t)=t^\gamma e^{-bt/(a-1)}
\]
belongs to the weighted \(L^2\)-space; the exponential controls infinity. A direct calculation yields
\[
A_bf_\gamma=a^{-(\gamma+1)}f_\gamma.
\]
Multiplying by independent bounded functions invariant under \(t\mapsto at\) yields infinite-dimensional eigenspaces. As \(\gamma\) varies, the eigenvalues fill the punctured disk \(0<|\lambda|<a^{-1/2}\). The spectral-radius bound excludes the exterior; closure of the Fredholm essential spectrum includes the boundary and zero. This proves the positive-displacement formula.

**Critical damping and singular power prefactor.** Since \(p_n(0)=1\), necessarily \(K_{n,a}(b)\ge1\). It equals one precisely when \(2bs/(a-1)\ge \log p_n(s)\) for every \(s>0\), equivalently \(b\ge b_*(n,a)\). The quotient defining \(b_*\) is continuous, positive, and tends to zero at both ends of \((0,\infty)\): near zero use \(\log p_n(s)=s^2+O(s^4)\); at infinity use \(\log p_n(s)=2n\log s+o(1)\). This proves attainment and sharp positivity.

Write \(c=2b/(a-1)\) and \(u=cs\). Then
\[
c^{2n}K_{n,a}(b)=\sup_{u\ge0} e^{-u}\sum_{j=0}^{n} c^{2(n-j)}u^{2j}.
\]
For \(c\downarrow0\) the right-hand side tends uniformly in \(u\ge0\) to \(\sup_{u\ge0}e^{-u}u^{2n}=(2n/e)^{2n}\): each discarded summand has uniformly bounded \(e^{-u}u^{2j}\). Taking square roots proves the displayed equivalent.

**Strong, but not uniform, displacement limit.** On the Fourier side, \(A_b\to A_0\) strongly by dominated convergence after the substitution \(s=at\), because the multipliers \(e^{-bt}\) tend to one and have modulus at most one. The difference has exact norm
\[
\|T_b-T_0\|^2=\frac1a\sup_{t>0}(1-e^{-bt})^2\frac{p_n(at)}{p_n(t)}.
\]
The quotient is at most \(a^{2n}\); both factors approach their respective maxima as \(t\to\infty\). Thus the norm is \(a^{n-1/2}\) for every \(b>0\).

## Verification
All operator identities above are obtained in the exact Fourier model; the infinite-dimensional spectral assertions follow from explicit eigenvector families and analytic norm bounds. The independent finite diagnostics in `check.py` confirm the pointwise eigenfunction equation for several nonreal parameters and sample the normalized power limit at three orders and dilation factors. They do not prove essential spectrum or quantify an infinite-dimensional limit. The verified source normalization is the standard \(H^2\) boundary-Lebesgue normalization, with the \(1/\sqrt{2\pi}\) Fourier factor in the displayed transform.

## Relationship to prior work
Liang, Li and Qian [1, Theorem 4.1] give the exact Paley–Wiener model for this derivative-based \(\mathcal H_n\) and, in their operator section, boundedness conditions for weighted composition operators and spectral results for **multiplication** operators. The present theorem concerns spectra, Fredholm essential spectra, exact powers and sharp displacement thresholds for a different operator class.

Chalendar and Partington [2, Section 3] previously developed dilation spectral-radius formulas and eigenvector mechanisms for the **Zen-space** Laplace-transform setting, including an annulus-to-disk example on Hardy–Bergman intersections. Their class is generated by nonnegative measures and has Laplace weights that are nonincreasing; the derivative Hardy–Sobolev weight \(p_n\) here is strictly increasing and does not satisfy that hypothesis. Their norm mechanism inspired the method, and the qualitative annulus/disk phenomenon is not claimed as new in general. The new specialized quantitative assertion is the exact high-frequency Sobolev annulus and its collapse to a universal disk, together with a nontrivial sharp damping threshold and the \(b^{-n}\) normalized-power amplification law.

Galé, Matache, Miana and Sánchez-Lajusticia [3], and Liu, Li, Kou and Qu [4], study a distinct scale requiring weighted derivatives \(z^jF^{(j)}\in H^2\), rather than unweighted derivatives \(F^{(j)}\in H^2\); their composition-operator results concern boundedness rather than this spectral/power classification. The inspected results do not state the polynomial-weight spectral and power threshold classification; historical priority beyond these sources is unresolved.

## Limitations
The result is for the Hilbert exponent two, finite integer derivative order, real dilation greater than one, and nonnegative vertical displacement. The exact critical threshold \(b_*\) is characterized variationally, not by elementary radicals. The normalized-power limit is at fixed positive \(b\); its small-\(b\) limit is taken afterwards, and no uniform two-parameter interchange is claimed. The numerical checker has finite scope. Related unindexed weighted-composition literature may affect historical priority.

## References
[1] H. Liang, H. Li, T. Qian, *Banach Hardy–Sobolev Spaces on the Upper Half-plane and Operator Theory*, arXiv:2603.13983v1 (first public 2026-03-14), Theorem 4.1 and Section 5. https://arxiv.org/pdf/2603.13983

[2] I. Chalendar, J. R. Partington, *Composition Operators on Function Spaces on the Halfplane: Spectra and Semigroups*, arXiv:2204.05894v2 (2023), Section 3, particularly equations (6)–(7), Propositions 3.5–3.6 and Theorem 3.7. https://arxiv.org/pdf/2204.05894

[3] J. E. Galé, V. Matache, P. J. Miana, L. Sánchez-Lajusticia, *Hilbertian Hardy-Sobolev spaces on a half-plane*, arXiv:2401.16091v1, 2024. https://arxiv.org/pdf/2401.16091

[4] D. Liu, H. Li, K. I. Kou, W. Qu, *The Theory of Hardy-Sobolev Spaces over the Upper Half-Plane*, J. Nonlinear Var. Anal. 9 (2025), 247–262. https://jnva.biemdas.com/issues/JNVA2025-2-5.pdf
