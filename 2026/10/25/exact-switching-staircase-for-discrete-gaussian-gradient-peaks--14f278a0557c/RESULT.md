# Exact switching staircase for discrete-Gaussian gradient peaks

## Finding
For every integer \(n\ge0\), write \(I_n\) for the modified Bessel function of the first kind and define
\[
H_n(x)=I_n(x)-2I_{n+1}(x)+I_{n+2}(x),\qquad x>0.
\]
There is **exactly one simple positive zero** \(x_n\) of \(H_n\), and its location satisfies the strict, all-order bounds
\[
(n+1)^2<x_n<(n+1)(n+2).
\]
Moreover \(H_n(x)>0\) for \(0<x<x_n\) and \(H_n(x)<0\) for \(x>x_n\). The intervals for successive zeros are disjoint, so \(0<x_0<x_1<\cdots\).

For the discrete Laplacian \((\Delta f)(k)=f(k+1)-2f(k)+f(k-1)\) on \(\mathbb Z\), let \(D f(k)=f(k+1)-f(k)\), \(T_t=e^{t\Delta}\), and \(p_t(k)=e^{-2t}I_{|k|}(2t)\). Then
\[
\|DT_t\|_{\ell^1(\mathbb Z)\to\ell^\infty(\mathbb Z)}
=e^{-2t}\max_{n\ge0}\bigl(I_n(2t)-I_{n+1}(2t)\bigr).
\]
Writing \(x_{-1}=0\), if \(x_{N-1}<2t<x_N\), the nonnegative-index maximum occurs at the **unique** index \(N\); if \(2t=x_N\), the maximum is shared by the **adjacent** indices \(N,N+1\). The corresponding full-line gradient has the reflected points of equal absolute magnitude. Hence every individual peak relocation happens exactly once, with the strictly increasing switching times \(t_n=x_n/2\).

## Assumptions and scope
Here \(n,N\) are nonnegative integers, \(x,t\) are strictly positive real numbers, and the norm is the operator norm from complex or real \(\ell^1(\mathbb Z)\) to \(\ell^\infty(\mathbb Z)\). The Bessel normalization is
\[
I_n(x)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{x\cos\theta}e^{-in\theta}\,d\theta,
\]
so \(p_t\) is the Fourier-coefficient sequence of \(\theta\mapsto e^{-2t(1-\cos\theta)}\). No claim is made for other lattices, higher spatial derivatives, or continuous time-dependent optimizer interpolation.

## Proof
**1. Ratio reduction.** Fix \(n\ge0\), put \(a=n+1\), and set \(r(x)=I_{n+1}(x)/I_n(x)\) and \(q(x)=x/(x+a)\). Bessel's three-term recurrence gives
\[
I_{n+2}(x)=I_n(x)-\frac{2a}{x}I_{n+1}(x),\qquad
H_n(x)=2I_n(x)\left[1-\left(1+\frac ax\right)r(x)\right].
\]
The power series for \(I_n\) makes \(I_n(x)>0\) and \(r(x)>0\) for \(x>0\). Consequently \(\operatorname{sgn}H_n=-\operatorname{sgn}(r-q)\).

**2. Single-crossing lemma and strict lower boundary.** The derivative recurrence yields the Riccati equation
\[
r'(x)=1-\frac{2a-1}{x}r(x)-r(x)^2.
\]
Let \(w=r-q\). At every zero of \(w\), direct substitution gives the *exact transversal derivative*
\[
w'(x)=\frac{x-a^2}{(x+a)^2}.
\]
The positive-argument series implies \(r(x)=x/(2a)+O(x^3)\) as \(x\downarrow0\), whereas \(q(x)=x/a+O(x^2)\); thus \(w<0\) near zero. There cannot be a first zero with \(x<a^2\), because its derivative would be negative. There also cannot be a first zero at \(x=a^2\), since differentiating the equation for \(w\) there gives \(w''(a^2)=1/(a^2+a)^2>0\): such a zero would be a strict local minimum and could not be approached from negative values. Every zero therefore lies to the right of \(a^2\), and at every zero \(w'>0\). Two upward zero crossings are impossible without a downward or nontransverse intervening crossing. Thus \(w\) has at most one zero, necessarily simple, and it lies in \((a^2,\infty)\).

**3. Explicit upper boundary.** Define, for \(x>0\),
\[
L(x)=\frac{x}{a-\tfrac12+\sqrt{x^2+(a+\tfrac12)^2}},
\qquad y=\sqrt{x^2+(a+\tfrac12)^2}.
\]
The Bessel series and Taylor expansion of \(L\) imply
\[
r(x)-L(x)=\frac{x^3}{8a^2(a+1)(2a+1)}+O(x^5)>0
\qquad(x\downarrow0).
\]
Writing \(F(x,u)=1-(2a-1)u/x-u^2\), a direct symbolic differentiation, with \(y^2=x^2+(a+1/2)^2\), yields the strict subsolution inequality
\[
F(x,L(x))-L'(x)=
\frac{(2a+1)(2y-2a-1)}{y(2a+2y-1)^2}>0.
\]
Since \(r'=F(x,r)\), at a hypothetical first downward contact \(r=L\) we would have \((r-L)'=F(x,L)-L'>0\), a contradiction. Hence \(r>L\) for every \(x>0\). At \(x=a(a+1)\), the radical equals \(x+1/2\), so \(L(x)=x/(x+a)=q(x)\). Therefore \(w(a(a+1))>0\). Continuity and step 2 give exactly one simple root of \(w\), with \(a^2<x_n<a(a+1)\), and the stated sign pattern for \(H_n\).

**4. Strict positivity and staircase.** The same Riccati equation shows \(r(x)<1\): initially \(r<1\), and at a hypothetical first contact with \(r=1\) its derivative would equal \(-(2a-1)/x<0\), contrary to upward contact. Thus \(b_n(x):=I_n(x)-I_{n+1}(x)>0\). By definition \(b_n-b_{n+1}=H_n\). For \(n\ge1\), the bounds give \(x_{n-1}<n(n+1)<(n+1)^2<x_n\), so the switching zeros are strictly increasing. For fixed \(x\) between consecutive switching zeros, the signs of \(H_n\) make \(b_0,b_1,\ldots\) increase strictly up to one index and decrease strictly afterwards; at a switching zero, exactly two neighboring terms tie. This determines all maximizers of \(b_n\).

Finally \(DT_t\) is convolution with \(D p_t\), and \(\|f\mapsto k*f\|_{\ell^1\to\ell^\infty}=\sup_{j\in\mathbb Z}|k(j)|\), with equality on a signed point mass. Since \(p_t(-k)=p_t(k)\), the absolute differences in both half-lines equal \(e^{-2t}b_n(2t)\) for \(n\ge0\). The norm formula and exact peak-index staircase follow.

## Verification
All assertions follow from identities and strict inequalities valid for every real \(x>0\) and integer \(n\ge0\), not from finite enumeration. The Riccati tangency and subsolution identities can be independently checked by differentiation. Numerical spot checks (not part of the proof) give \(x_0\approx1.54512725799\), \(x_1\approx4.56148743756\), \(x_2\approx9.52904074311\), all within their stated open intervals.

## Relationship to prior work
Ciaurri et al. establish the discrete heat kernel and explicitly derive integral identities for the **same first and second finite Bessel differences** (their formulas (37) and (38)), but do not supply the all-order unique positive-zero law, strict quadratic root brackets, or the resulting complete peak-index staircase for the sharp gradient operator norm. Hornik and Grün analyze classical Amos-type ratio inequalities; indeed the function \(L\) above is an already-known lower bound, so **the Bessel-ratio bound itself is not asserted as new**. Its sharp-contact use at \(x=a(a+1)\), combined with the all-zero transversal Riccati argument, gives the stated switching classification. Chinta et al. place the discrete Gaussian kernel into a wider mathematical context without deriving this gradient transition law. These comparisons establish a bounded literature-based originality assessment, not an exhaustive priority guarantee.

## Limitations
The switching times have unique implicit Bessel-characterizations and explicit open brackets; no closed forms or asymptotic correction formula are asserted. The proof is specific to the one-dimensional nearest-neighbor heat operator and its first forward gradient. Relevant unindexed sources could contain equivalent statements, and external independent audit remains outstanding.

## References
1. Ó. Ciaurri, T. A. Gillespie, L. Roncal, J. L. Torrea, J. L. Varona, *Harmonic Analysis associated with a discrete Laplacian*, arXiv:1401.2091v1 (first public submission 2014-01-09), https://arxiv.org/abs/1401.2091. See the kernel identity and the first/second Bessel-difference formulas (37)–(38) in the later v2 PDF.
2. K. Hornik and B. Grün, *Amos-type bounds for modified Bessel function ratios*, J. Math. Anal. Appl. 408 (2013), 91–101, DOI:10.1016/j.jmaa.2013.05.070, https://pmc.ncbi.nlm.nih.gov/articles/PMC4047631/. Section 3 and Theorem 3 identify the classical ratio lower bound used here.
3. G. Chinta, J. Jorgenson, A. Karlsson, L. Smajlović, *The discrete analogue of the Gaussian*, arXiv:2409.14344, https://arxiv.org/abs/2409.14344. Background on the discrete Gaussian and its Fourier–Bessel representation.
