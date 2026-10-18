# Logarithmic spectral sampling and arithmetic noncompleteness for crescent Cesàro eigenvectors

## Finding

Fix a complex Lebesgue space \(L^p(0,1)\) with \(1<p<2\), and let \(q=p/(p-1)\), \(a=1/q\), \(b=1/p\), \(\sigma\in(a,b)\), and \(w=\min\{\sigma-a,b-\sigma\}>0\). For the bounded real-variable Cesàro operator

\[
(C_pf)(x)=\frac1x\int_0^x\frac{f(u)}{1-u}\,du,
\]

put \(e_t(x)=x^{\sigma+it-1}(1-x)^{-\sigma-it}\) and \(\lambda_t=(\sigma+it)^{-1}\) for real \(t\). Every \(e_t\) is a nonzero eigenvector of \(C_p\) with eigenvalue \(\lambda_t\). The following complementary assertions hold.

**Dense spectral sampling.** For any sequence of *pairwise distinct* real numbers \((t_n)_{n\ge1}\), if there exists \(\delta\in(0,w)\) such that

\[
\sum_{n\ge1}\exp\!\left(-\frac{\pi|t_n|}{2\delta}\right)=\infty,
\]

then \(\overline{\operatorname{span}}\{e_{t_n}:n\ge1\}=L^p(0,1)\).

**Arithmetic obstruction.** If \(\Gamma\subset\mathbb R\) is contained in any finite union \(\bigcup_{j=1}^m(\theta_j+h\mathbb Z)\), where \(m\ge1\), \(\theta_j\in\mathbb R\), and \(h>0\), then \(\overline{\operatorname{span}}\{e_t:t\in\Gamma\}\) has **infinite codimension** in \(L^p(0,1)\).

In particular, for every \(0<c<2w/\pi\), the sampling sequence \(t_n=c\log n\), \(n\ge2\), is complete, whereas \(t_n=hn\), \(n\ge1\), is infinitely codimensional. Although the conclusions differ, both corresponding eigenvalue sets are discrete away from zero and accumulate exactly at \(\{0\}\) on the spectral boundary.

## Assumptions and scope

All spaces, linear spans, and dual functionals are **complex**. Complex powers on \((0,1)\) use the real logarithm. The domain is precisely \(1<p<2\), since the eigenvector strip \(1/q<\operatorname{Re}(1/\lambda)<1/p\) is then nonempty. The parameter \(\sigma\) is fixed in this open strip, and sampling is along the line \(1/\lambda=\sigma+it\). There are no regularity or separation assumptions on the distinct \(t_n\) besides the displayed divergence condition. The arithmetic set may be finite, infinite, or have missing elements in its cosets.

## Proof

**1. Eigenvectors and normalization.** Set \(s=\sigma+it\). The derivative identity

\[
\frac{d}{du}\left(\frac{u}{1-u}\right)^s
=s\,u^{s-1}(1-u)^{-s-1}
\]

and \(\operatorname{Re}s>0\) give \(C_pe_t=s^{-1}e_t\). Moreover,

\[
\|e_t\|_p^p=\int_0^1x^{p(\sigma-1)}(1-x)^{-p\sigma}\,dx
=B\bigl(p(\sigma-a),p(b-\sigma)\bigr)<\infty,
\]

where \(B\) is the Euler beta integral. Thus these are genuine, uniformly norm-bounded-in-\(t\) eigenvectors.

**2. A bounded analytic annihilator.** Suppose \(g\in L^q(0,1)\) annihilates a prescribed eigenvector family under the bilinear dual pairing. Define

\[
F(s)=\int_0^1g(x)x^{s-1}(1-x)^{-s}\,dx,
\qquad a<\operatorname{Re}s<b.
\]

Hölder's inequality yields

\[
|F(s)|\le\|g\|_q
B\bigl(p(\operatorname{Re}s-a),p(b-\operatorname{Re}s)\bigr)^{1/p}.
\]

Dominated differentiation on compact substrips makes \(F\) analytic. Fix \(0<\delta<w\). Then \(G(z)=F(\sigma+iz)\) is bounded and analytic in the horizontal strip \(S_\delta=\{z:|\operatorname{Im}z|<\delta\}\).

**3. Non-Blaschke zeros force completeness.** The conformal map

\[
\Psi(z)=\tanh\!\left(\frac{\pi z}{4\delta}\right):S_\delta\longrightarrow\mathbb D
\]

sends real \(t\) to the real interval \((-1,1)\), with \(1-|\Psi(t)|\asymp\exp[-\pi|t|/(2\delta)]\) as \(|t|\to\infty\). The zero set of a nonzero bounded analytic function on the disk must satisfy the Blaschke summability condition. Therefore, if \(F(\sigma+it_n)=0\) for pairwise distinct \(t_n\) and the stated sum diverges, \(G\) vanishes identically. This also follows directly from the identity theorem when the frequencies have a finite accumulation point. Hence \(F(\sigma+it)=0\) for every real \(t\).

Now set \(y=\log(x/(1-x))\), \(x(y)=e^y/(1+e^y)\), and

\[
H(y)=g(x(y))\,(1-x(y))e^{\sigma y}.
\]

Since \(dx=x(1-x)\,dy\), direct substitution gives

\[
F(\sigma+it)=\int_{\mathbb R}H(y)e^{ity}\,dy.
\]

Also \(H\in L^1(\mathbb R)\) by Hölder's inequality and the preceding finite beta integral. Fourier-transform uniqueness on \(L^1\) yields \(H=0\) almost everywhere, whence \(g=0\) almost everywhere. Thus the sampled eigenvectors have no nonzero continuous annihilator. Hahn–Banach proves their closed span is all of \(L^p(0,1)\).

**4. Finite arithmetic cosets leave infinitely many obstructions.** Let \(L=2\pi/h\) and \(\tau_L\phi(y)=\phi(y-L)\). For any nonzero compactly supported smooth \(\phi\) with support contained in an interval shorter than \(L\), define

\[
H_\phi=\prod_{j=1}^m\bigl(\tau_L-e^{i\theta_jL}I\bigr)\phi.
\]

For the Fourier transform convention above,

\[
\widehat H_\phi(t)
=\widehat\phi(t)\prod_{j=1}^m(e^{itL}-e^{i\theta_jL}),
\]

which vanishes on each coset \(\theta_j+h\mathbb Z\). The translated pieces of \(H_\phi\) have disjoint supports, and the leading coefficient of its translation polynomial is one, so \(H_\phi\ne0\). Define the compactly supported function \(g_\phi\in L^q(0,1)\) through

\[
g_\phi(x(y))=\frac{H_\phi(y)e^{-\sigma y}}{1-x(y)}.
\]

The same substitution shows \(\int_0^1g_\phi(x)e_t(x)\,dx=\widehat H_\phi(t)=0\) for every \(t\in\Gamma\). Translating the initial \(\phi\) to infinitely many pairwise distant intervals yields infinitely many disjointly supported \(H_\phi\) and linearly independent continuous annihilators \(g_\phi\). Therefore the closed span has infinite codimension.

**5. A shared spectral cusp with opposite behavior.** For \(t_n=c\log n\), \(n\ge2\), choose \(\delta\) with \(\pi c/2<\delta<w\). Then

\[
\sum_{n\ge2}e^{-\pi t_n/(2\delta)}
=\sum_{n\ge2}n^{-\pi c/(2\delta)}=\infty,
\]

proving density. For \(t_n=hn\) use the single coset \(h\mathbb Z\), proving infinite codimension. In both cases \(t_n\to+\infty\), so \(\lambda_{t_n}\to0\); the eigenvalues are distinct and have no other accumulation point.

## Verification

The proof directly verifies the eigenvalue equation, the exact beta-integrability window, the boundedness domain for the holomorphic annihilator, the strip-to-disk Blaschke exponent, the logistic Jacobian, and the finite-translation Fourier zeros. The separate standalone \(\texttt{check_sampling.py}\) recomputes the finite arithmetic-coset factor cancellations and the logarithmic-exponent inequality using only Python's standard library. Those finite checks are sanity checks; the infinite-dimensional conclusions follow from Blaschke uniqueness, Fourier uniqueness, and Hahn–Banach, not from numerical sampling.

## Relationship to prior work

Belli, Gül, Ross and Siskakis (2026), in their Example 6.5, identify the same eigenvectors and explicitly ask when an infinite collection spans \(L^p(0,1)\). Their Proposition 3.1 establishes the eigenvalue strip; they do not state the logarithmic non-Blaschke sufficient condition or the arithmetic infinite-codimension obstruction. The present result supplies contrasting explicit countable answers to that question. Classical Blaschke zero-set theory and Fourier uniqueness furnish the proof mechanism; the claim is the combined spectral sampling statement for this concrete operator, not a new general zero-set theorem. The earlier work on the \(L^2\) variant has empty point spectrum and does not cover this regime; discrete Cesàro matrices have different underlying spaces and eigenfamilies.

## Limitations

The logarithmic bound \(c<2w/\pi\) is **sufficient**, not claimed sharp or necessary. No exact completeness characterization for arbitrary frequency sets is obtained, and no quantitative approximation rate is proved. The conclusion is specific to the vertical spectral line and \(1<p<2\), not arbitrary points throughout the crescent or the spaces with \(p\ge2\). Known complex approximation results may suggest further extensions; exhaustive historical priority and independent verification are not claimed.

## References

1. A. Belli, U. Gül, W. T. Ross, and A. G. Siskakis, *Crescents and the Real Variable Cesàro Operator*, *Integral Equations and Operator Theory* **98** (2026), 42. DOI: 10.1007/s00020-026-02865-7; first public preprint arXiv:2606.08600 (7 June 2026), especially Proposition 3.1 and Example 6.5.
2. A. Belli, U. Gül, W. T. Ross, and A. G. Siskakis, *The Cesàro Operator on \(L^2(0,1)\)*, arXiv:2604.19691 (2026), for the distinct Hilbert-space spectral setting.
3. P. Borwein and T. Erdélyi, *The Full Müntz Theorem in \(C[0,1]\) and \(L^1[0,1]\)*, *Journal of the London Mathematical Society* **54** (1996), 102–110. DOI: 10.1112/jlms/54.1.102; comparison with real-power Müntz completeness, not a covering theorem for the present complex spectral family.
4. Classical Blaschke zero-set theorem for bounded analytic disk functions; uniqueness theorem for Fourier transforms of integrable functions; Hahn–Banach separation theorem (standard auxiliary results).
