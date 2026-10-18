# Strict entropy collapse with a zeta correction for Lebesgue-preserving intermittent maps

## Finding
For the symmetrized intermittent interval family of Shinkai and Aizawa, equipped with its **exact** invariant normalized Lebesgue probability, the Kolmogorov–Sinai entropy is a strictly decreasing function of the intermittency exponent \(B\ge1\), even though the invariant probability never changes. Writing \(q=B-1\), \(a=B/(B+1)\), and
\[
F(z)=(1+z)\log(1+z)-z\log z,\qquad F(0)=0,
\]
the exact entropy (natural-logarithm units) is
\[
h(B)=\frac{B}{B+1}\int_0^1F(t^{B-1})\,dt,
\qquad h(1)=\log2,
\qquad 0<h(B)<\log2\ \ (B>1).
\]
It decreases strictly throughout \([1,\infty)\) and has sharp endpoint expansions
\[
h(B)=\log2-\frac{(B-1)^2}{4}+O((B-1)^3)\quad(B\downarrow1),
\]
\[
h(B)=\frac{C}{B}-\frac{C+\frac34\zeta(3)}{B^2}+O(B^{-3})\quad(B\to\infty),
\qquad C=2\log2+\frac{\pi^2}{12}.
\]
In particular \(\lim_{B\to\infty}B h(B)=2\log2+\pi^2/12\). These statements concern measure-theoretic, rather than equipartition-histogram, entropy.

## Assumptions and scope
For every real \(B\ge1\), let \(a=B/(B+1)\) and define \(T_B:[-1,1]\to[-1,1]\) by
\[
T_B(x)=\begin{cases}
x+(1-a)((x+1)/a)^B,&-1\le x<-1+a,\\
x+1-a((-x)/(1-a))^{1/B},&-1+a\le x<0,\\
x-1+a(x/(1-a))^{1/B},&0\le x<1-a,\\
x-(1-a)((1-x)/a)^B,&1-a\le x\le1.
\end{cases}
\]
At the finitely many partition boundaries, the displayed half-open convention is adopted; their values do not affect any measure-theoretic assertion. Let \(\lambda\) be normalized Lebesgue probability on \([-1,1]\), so \(d\lambda=dx/2\). Let \(h(B)=h_\lambda(T_B)\) denote Kolmogorov–Sinai entropy. The power-law family and its invariant-measure motivation originate in the 2014 source; the strict full-parameter entropy law and endpoint constants are the claims assessed here.

## Proof
**1. Exact invariance and the inverse-branch probabilities.** Define
\[
\Phi_B(t)=a t+(1-a)t^B=\frac{Bt+t^B}{B+1},\quad 0\le t\le1.
\]
It is a strictly increasing bijection of \([0,1]\). For any target \(y\in(0,1)\), put \(t=\Phi_B^{-1}(1-y)\) and \(z=t^{B-1}\). The two preimages of \(y\) are
\[
x_{\rm inner}=-(1-a)t^B,\qquad x_{\rm outer}=1-a t.
\]
Their positive derivatives are \(1+1/z\) and \(1+z\), respectively (with the evident limiting convention at \(t=0\)). Their inverse derivatives are
\[
p_{\rm inner}=\frac{z}{1+z},\qquad p_{\rm outer}=\frac1{1+z};\qquad p_{\rm inner}+p_{\rm outer}=1.
\]
The two inverse branches of negative targets are obtained by reflection and have the same weights. Hence the Perron–Frobenius operator sends the constant density to itself exactly, proving \(T_{B*}\lambda=\lambda\).

**2. Entropy identity.** The four open monotonicity intervals form a finite partition \(\mathcal P\). On every interval the derivative is at least one, and it is strictly greater than one at every interior point, except that derivatives at finitely many boundaries are immaterial. The partition is generating modulo \(\lambda\): otherwise, an infinite itinerary would contain a nondegenerate interval \(J\) on which every iterate remains inside single monotonicity branches. All image lengths are at least \(|J|>0\), whereas the minimum expansion ratio over subintervals of a branch with length at least \(|J|\) is uniformly greater than one. Repeated expansion would make their lengths exceed the total interval length two, a contradiction. Thus \(h_\lambda(T_B)=h_\lambda(T_B,\mathcal P)\). The conditional-entropy identity for a generating partition gives
\[
h_\lambda(T_B)=H_\lambda(\mathcal P\mid T_B^{-1}\mathcal B)
=\int_0^1 H_2\!\left(\frac{z(y)}{1+z(y)}\right)dy,
\]
where \(H_2(p)=-p\log p-(1-p)\log(1-p)\), \(z(y)=\Phi_B^{-1}(1-y)^{B-1}\), and \(\mathcal B\) is the Borel sigma field. (The positive and negative output halves have identical inverse statistics, cancelling the normalized-length factor \(1/2\).) Since \(dy=a(1+t^{B-1})dt\) after reversing the parameter \(t\), and \((1+z)H_2(z/(1+z))=F(z)\), this gives the asserted integral formula. Equivalently, it equals \(\int\log|T'_B|\,d\lambda\). Integrability near the inverse-branch singularities follows from integrability of powers of \(|\log t|\) on \((0,1)\).

**3. Strict monotonicity.** For \(B>1\), set \(q=B-1\). At a fixed \(z\in(0,1)\), the target coordinate \(u=\Phi_B(t)\) with \(z=t^q\) is
\[
u=z^{1/q}\frac{q+1+z}{q+2}.
\]
Its logarithmic derivative with respect to \(q\), at fixed \(z\), is
\[
\frac{\partial}{\partial q}\log u
=\frac{-\log z}{q^2}
+\frac{1-z}{(q+1+z)(q+2)}>0.
\]
Consequently, at each fixed target \(u\in(0,1)\), the corresponding \(z\) strictly **decreases** as \(q\) increases. Because \(H_2(z/(1+z))\) is strictly increasing for \(0<z<1\), its output-coordinate integral decreases strictly. At \(B=1\), all inverse weights are equal, and \(h(1)=\log2\); strictness for every larger \(B\) follows from comparison to the limiting \(z=1\).

**4. The small-\(q\) expansion.** The derivatives in \(q\) of \(F(t^q)\) up to third order are dominated near \(q=0\) by integrable polynomials in \(|\log t|\), permitting Taylor expansion under the integral. Using
\(F(1)=2\log2\), \(F'(1)=\log2\), \(F''(1)=-1/2\), and \(\int_0^1(\log t)^jdt=(-1)^j j!\), one gets
\[
\int_0^1F(t^q)dt=2\log2-q\log2+q^2(\log2-1/2)+O(q^3).
\]
Multiplication by \((1+q)/(2+q)=1/2+q/4-q^2/8+O(q^3)\) cancels the linear term and leaves the coefficient \(-1/4\).

**5. The large-\(B\) zeta correction.** Substituting \(z=t^{B-1}\), write
\[
h(B)=\frac{B}{B^2-1}\int_0^1 z^{1/(B-1)-1}F(z)dz.
\]
All logarithmic moments \(\int_0^1F(z)|\log z|^j dz/z\) for \(j=0,1,2\) are finite, allowing the second-order expansion. Put \(C=\int_0^1F(z)dz/z\) and \(J=\int_0^1F(z)\log z\,dz/z\). Integration and the alternating zeta sums yield
\[
C=2\log2+\pi^2/12,
\qquad J=-2\log2-\pi^2/12-3\zeta(3)/4.
\]
Indeed, \(\int_0^1\log(1+z)dz/z=\pi^2/12\), \(\int_0^1\log(1+z)\log z\,dz/z=-3\zeta(3)/4\), and \(\int_0^1\log(1+z)\log z\,dz=2-2\log2-\pi^2/12\). Thus \(h(B)=C/B+J/B^2+O(B^{-3})\), with controlled remainder from the second log-moment.

## Verification
Run `python verify.py` with Python 3 and `mpmath`. The verifier uses exact rational arithmetic to check the two inverse-Jacobian weights for multiple integer parameters and tests two independent numerical integral representations of entropy. It also checks monotonic samples, the local quadratic coefficient, and the first two inverse-parameter coefficients at high precision. A successful execution prints `VERIFY_OK`; the actual local execution yielded `VERIFY_OK 8 entropy(2)= 0.590862907413260413 C= 2.20876139454400384 J= -3.11030407191369955`. These are finite consistency checks; all universal and limiting assertions are justified analytically above.

## Relationship to prior work
The map and parameter choice \(a=B/(B+1)\), \(g(t)=t^B\), are those in Shinkai and Aizawa (2014), Sections II.3 and IV.1. The article studies residence-time and correlation exponents and tests invariance via numerical equipartition histograms. That histogram quantity is **not** Kolmogorov–Sinai entropy. The same authors' related 2014 work on log-Weibull intermittency uses a different function \(g\). The general conditional-entropy identity for generating piecewise monotone maps is standard; the specific strict parameter ordering and the two sharp endpoint expansions for this family are the assessed extension. Searches for equivalent results did not identify a covering publication; unindexed priority remains possible.

## Limitations
The theorem is confined to the exact four-piece power-law family above and invariant normalized Lebesgue initialization. It says nothing about topological entropy, entropy-production large-deviation rate functions, exponential correlation decay, or a central/stable limit theorem. The entropy-zero limit concerns \(B\to\infty\), not any finite parameter. Search coverage is not a proof of historical novelty; see the accompanying structured comparison for residual risks.

## References
1. S. Shinkai and Y. Aizawa, *On stable laws in a one-dimensional intermittent map equipped with a uniform invariant measure*, arXiv:1401.6746v1 (first posted 2014-01-27), especially Sections II.3 and IV.1. https://arxiv.org/html/1401.6746
2. S. Shinkai and Y. Aizawa, *1/f Spectrum and 1-Stable Law in One-Dimensional Intermittent Map with Uniform Invariant Measure and Nekhoroshev Stability*, arXiv:1401.6377 (first posted 2014-01-24). https://arxiv.org/abs/1401.6377
3. T. Miyaguchi and Y. Aizawa, *Spectral analysis and an area-preserving extension of a piecewise linear intermittent map*, Physical Review E **75**, 066201 (2007), https://doi.org/10.1103/PhysRevE.75.066201. (Related precursor; only the public abstract was inspected.)
