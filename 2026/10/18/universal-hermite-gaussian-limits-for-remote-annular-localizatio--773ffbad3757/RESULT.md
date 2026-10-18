# Universal Hermite–Gaussian limits for remote annular localization

## Finding

Let \(h_q\) be the unit-norm Hermite function of order \(q\ge0\) for the Fourier convention \(e^{-2\pi i\xi t}\). For fixed \(q\in\mathbb N_0\) and fixed annular area \(w>0\), let \(T^{(q)}_{a,w}\) be the positive short-time-Fourier localization operator with window \(h_q\) and indicator symbol of
\[
\Omega_{a,w}=\{(x,\xi)\in\mathbb R^2:a\le\pi(x^2+\xi^2)\le a+w\},\qquad a\ge0.
\]
Write \(c=a+w/2\), and let \(\operatorname{He}_q\) denote the probabilists' Hermite polynomial, \(\exp(uz-z^2/2)=\sum_{q\ge0}\operatorname{He}_q(u)z^q/q!\). Define
\[
F_q(u)=q!^{-1}e^{-u^2/2}\operatorname{He}_q(u)^2,\quad M_q=\max_{u\in\mathbb R}F_q(u),\quad U_q=\operatorname*{argmax}_{u\in\mathbb R}F_q(u).
\]
**Theorem.** For each fixed \(q\ge0\) and \(w>0\),
\[
\lim_{a\to\infty}\frac{\sqrt{2\pi c}}{w}\,\|T^{(q)}_{a,w}\|=M_q.
\]
If \(k_a\) is *any* maximizing Hermite-signal degree, then
\[
\operatorname{dist}\left(\frac{k_a-c}{\sqrt c},U_q\right)\to0.
\]
Conversely, for every \(u_*\in U_q\), any nonnegative integer sequence satisfying \((k_a-c)/\sqrt c\to u_*\) is asymptotically optimal in the sense that its eigenvalue divided by the operator norm tends to one. In particular \(M_0=1\), \(M_1=2/e\), \(M_2=8e^{-5/2}\), with \(U_0=\{0\}\), \(U_1=\{-\sqrt2,\sqrt2\}\), \(U_2=\{-\sqrt5,\sqrt5\}\).

**Skew-selection theorem at order one.** For each fixed \(w>0\), all maximizing indices for \(q=1\) eventually belong to the lower asymptotic band, and satisfy
\[
k_a=c-\sqrt{2c}+O_w(1),\qquad
\|T^{(1)}_{a,w}\|=\frac{2w}{e\sqrt{2\pi c}}\left[1+\frac{\sqrt2}{6\sqrt c}+O_w(c^{-1})\right].
\]
The opposite band contributes the same leading coefficient but the *negative* first correction, so it cannot maximize for large \(a\).

## Assumptions and scope

The localization operator is defined on \(L^2(\mathbb R)\) by
\[
\langle T^{(q)}_{a,w}f,f\rangle=\int_{\Omega_{a,w}}|V_{h_q}f(x,\xi)|^2\,dx\,d\xi,\quad V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt.
\]
The parameters \(q,w\) are held fixed while \(a\to\infty\); the annular area remains exactly \(w\). All Hermite functions are normalized to unit \(L^2\) norm, and area is measured in the \((x,\xi)\)-plane. The operator is bounded, compact, positive and diagonal in the Hermite basis. Nothing is asserted uniformly for growing window order, nor for arbitrary nonradial regions.

## Proof

**1. Exact diagonalization and a Poisson–Charlier expression.** Rotational invariance of the symbol gives diagonalization in the signal Hermite basis \(\{h_k:k\ge0\}\). By the Fourier–Wigner/Laguerre identity, for \(t=\pi(x^2+\xi^2)>0\), the angularly independent squared overlap is
\[
|V_{h_q}h_k(x,\xi)|^2=e^{-t}\frac{\min(k,q)!}{\max(k,q)!}\,t^{|k-q|}\left[L_{\min(k,q)}^{(|k-q|)}(t)\right]^2.
\]
Define monic Charlier polynomials through
\[
\sum_{q=0}^\infty C_q(k;t)\frac{z^q}{q!}=e^{-tz}(1+z)^k.
\]
Their recurrence is \(C_0=1\), \(C_1=k-t\), and \(C_{q+1}=(k-t-q)C_q-qtC_{q-1}\). Expansion of the generating function or the Laguerre series gives, for every integer \(k,q\ge0\),
\[
e^{-t}\frac{\min(k,q)!}{\max(k,q)!}t^{|k-q|}[L_{\min(k,q)}^{(|k-q|)}(t)]^2
=\frac{e^{-t}t^k}{k!}\frac{C_q(k;t)^2}{q!t^q}.
\]
Polar integration uses \(dx\,d\xi=dt\,d\theta/(2\pi)\). Thus the exact nonnegative eigenvalues are
\[
\lambda_{k,q}(a,w)=\int_a^{a+w}\frac{e^{-t}t^k}{k!}\frac{C_q(k;t)^2}{q!t^q}\,dt,
\quad \|T^{(q)}_{a,w}\|=\max_{k\ge0}\lambda_{k,q}(a,w).
\]
At \(t=0\), the integrand is interpreted by its nonnegative Laguerre limit. These identities also show the sum over \(k\) of the integrand equals one for each \(t\), consistent with Moyal's identity and \(\operatorname{tr}T^{(q)}_{a,w}=w\).

**2. Uniform central Charlier and Poisson limits.** Set \(t=c+v\) with \(|v|\le w/2\), \(k=c+u\sqrt c+O(1)\), and keep \(u\) in a fixed compact interval. In the generating function substitute \(z=s/\sqrt t\). Uniformly for bounded complex \(s\),
\[
e^{-s\sqrt t}(1+s/\sqrt t)^k\longrightarrow e^{us-s^2/2}.
\]
Coefficient extraction on a fixed complex circle therefore gives
\[
t^{-q/2}C_q(k;t)=\operatorname{He}_q(u)+O_{q,w}(c^{-1/2})
\]
uniformly on compact \(u\)-ranges. Stirling's formula in the same region gives
\[
\sqrt{2\pi t}\,e^{-t}t^k/k!=e^{-u^2/2}[1+O_w(c^{-1/2})].
\]
Together and after integrating \(t\) over an interval of length \(w\),
\[
\frac{\sqrt{2\pi c}}{w}\lambda_{k,q}(a,w)=F_q(u)+O_{q,w}(c^{-1/2})
\]
uniformly for bounded \(u=(k-c)/\sqrt c\), with a harmless nearest-integer convention. This is convergence of the *individual* eigenvalues at central degrees.

**3. No escape of maximizing degrees.** For fixed \(q\), the recurrence yields the elementary bound
\[
|C_q(k;t)|\le A_q\bigl(\sqrt t+|k-t|+q\bigr)^q\quad(t\ge1,\ k\ge0),
\]
by induction (increase \(A_q\) for the finitely many initial orders). Let \(r=|k-t|/\sqrt t\). Elementary Stirling/Chernoff inequalities for the Poisson mass imply that for \(t\ge1\), its \(\sqrt t\)-rescaled value outside the central region is at most a fixed constant times \(e^{-b\min(r^2,r\sqrt t)}\), with appropriate universal \(b>0\), up to harmless polynomial factors when \(k\) is small. Combining with the preceding fixed-order polynomial growth shows
\[
\lim_{R\to\infty}\limsup_{c\to\infty}
\sup_{\substack{k\ge0\\|k-c|\ge R\sqrt c}}
\frac{\sqrt{2\pi c}}{w}\lambda_{k,q}(a,w)=0.
\]
Here \(|t-c|\le w/2\), so \(r\) and \(|k-c|/\sqrt c\) differ by \(o(1)\), uniformly where needed. Since \(F_q\) is continuous, positive somewhere, and tends to zero at infinity, Steps 2–3 imply the norm limit, localization of every maximizing degree to \(U_q\), and asymptotic optimality of every integer sequence approaching any member of \(U_q\).

**4. Explicit orders zero, one, two.** For \(q=0\), \(F_0=e^{-u^2/2}\). For \(q=1\), \(F_1=u^2e^{-u^2/2}\), whose unique maxima are at \(u=\pm\sqrt2\) with height \(2/e\). For \(q=2\), \(F_2=\tfrac12(u^2-1)^2e^{-u^2/2}\); its critical points are \(0,\pm\sqrt5,\pm1\), and \(F_2(\pm\sqrt5)=8e^{-5/2}>F_2(0)=1/2\), yielding the stated maxima.

**5. First-order skewness and selection for \(q=1\).** Here \(C_1(k;t)=k-t\), so the exact density is the Poisson mass \(e^{-t}t^k/k!\) multiplied by \((k-t)^2/t\). Write \(u=(k-c)/\sqrt c\). Uniformly for \(u\) in fixed neighborhoods of \(\pm\sqrt2\), Stirling's formula one order further yields
\[
\sqrt{2\pi c}\frac{e^{-c}c^k}{k!}=e^{-u^2/2}\left[1+\frac{u^3-3u}{6\sqrt c}+O(c^{-1})\right].
\]
Taylor expansion in \(t\) around \(c\) and symmetry of \([c-w/2,c+w/2]\) show that replacing the annular integral by \(w\) times its center integrand incurs relative error \(O_w(c^{-1})\), uniformly for these \(u\). Hence
\[
\frac{\sqrt{2\pi c}}{w}\lambda_{k,1}(a,w)
=u^2e^{-u^2/2}\left[1+\frac{u^3-3u}{6\sqrt c}+O_w(c^{-1})\right].
\]
At \(u=-\sqrt2\), the bracket's first correction is \(+\sqrt2/(6\sqrt c)\); at \(+\sqrt2\), it is \(-\sqrt2/(6\sqrt c)\). By the localization theorem and these strictly separated corrections, every global maximizer is in the negative band for sufficiently large \(c\). Finally, the real interpolation \(k\mapsto e^{-c}c^k/\Gamma(k+1)\cdot(k-c)^2/c\) has logarithmic derivative \(\log c-\psi(k+1)+2/(k-c)\), and strictly negative logarithmic second derivative of order \(c^{-1}\) near \(u=-\sqrt2\). Its critical index is \(c-\sqrt{2c}+O(1)\). For the annular integral, differentiating the symmetric midpoint Taylor remainder shows that the first logarithmic derivative differs by \(O_w(c^{-3/2})\) and the second by \(O_w(c^{-2})\), uniformly in fixed neighborhoods of those peaks. Because the unperturbed logarithmic curvature is \(-2/c+O(c^{-3/2})\), the corresponding critical index also differs by \(O_w(1)\). Integer maximizers are within a bounded distance of this real critical index. Substitution gives the claimed norm expansion and \(O_w(1)\) mode localization.

## Verification

Run `python3 check_annular_hermite.py` (requires `sympy` and `mpmath`). The standalone program checks the Charlier recursion against the generating polynomial, exact Laguerre–Charlier equivalence over 120 test cases, 15 Moyal-normalization identities, numerical spectral maxima at three remote annuli for each \(q=0,1,2,3\), and the sharper first-window correction and lower-branch selection. The executed test suite passed 160 assertions. These are finite checks of formulas and asymptotic trends; Steps 1–5 above constitute the proof for unbounded \(a\).

## Relationship to prior work

Abreu and Gröchenig develop the Hermite-window/polyanalytic Bargmann transform framework. Agorram and collaborators derive the complex Hermite/Fourier–Wigner identities underpinning the exact density. Abreu, Gröchenig and Romero study accumulation of spectrograms for expanding regions. Maximenko and Tellería-Romero give a stronger general exact radial Toeplitz eigenvalue *formula* (not claimed new here), including the Laguerre integral. The additional result proved here is the fixed-area *remote* annulus norm limit for every fixed window order, the localization of maximizing signal indices on the Hermite–Gaussian argmax set, and the definite skewness-based selection of one of two asymptotically tied branches when \(q=1\). None of the specific inspected full-text portions of these sources states these asymptotic max-over-all-modes conclusions. An earlier implication from general radial-symbol or Poisson–Charlier asymptotic theory has not been ruled out absolutely.

## Limitations

The theorem is pointwise in the fixed window order \(q\) and area \(w\); there is no uniformity as either grows. Exact global maximizing Hermite indices for bounded \(a\) are not classified. All statements concern the specified rotationally invariant symbols and normalization. The relationship-to-prior-work assessment is not a certification of publication priority. An independent audit has not been carried out.

## References

1. L. D. Abreu and K. Gröchenig, *Banach Gabor frames with Hermite functions: polyanalytic spaces from the Heisenberg group*, arXiv:1012.4283, first public version 2010-12-20, https://arxiv.org/abs/1012.4283.
2. H. Agorram et al., *Complex Hermite functions as Fourier–Wigner transforms*, arXiv:1506.07084 (2015), https://arxiv.org/abs/1506.07084.
3. L. D. Abreu, K. Gröchenig and J. L. Romero, *On accumulated spectrograms*, arXiv:1404.7713 (2014), https://arxiv.org/abs/1404.7713.
4. E. A. Maximenko and A. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978 (2019), https://arxiv.org/abs/1905.00978, particularly the general radial Laguerre multiplier formula in Section 6.
5. I. Daubechies, *Time-Frequency Localization Operators: A Geometric Phase Space Approach* (1988), background radial localization; full text not inspected in this assessment.
