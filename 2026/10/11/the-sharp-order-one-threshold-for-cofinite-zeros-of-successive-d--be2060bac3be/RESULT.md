# The sharp order-one threshold for cofinite zeros of successive derivatives

## Finding

**Theorem (sharp order threshold).** There exists a transcendental entire function \(f\) of **order exactly \(1\) and infinite exponential type** such that, for every nonempty open \(U\subset\mathbb C\), some integer \(N(U)\) satisfies
\[
 n\ge N(U)\quad\Longrightarrow\quad
 \{z\in U:f^{(n)}(z)=0\}\ne\varnothing.
\]
Conversely, **no transcendental entire function of finite exponential type** has this property. In particular, no transcendental entire function of order strictly less than \(1\) has it. Hence order \(1\), necessarily of infinite type, is the minimal possible finite order.

The construction is probabilistic but gives existence without any computational or independence certification. Its proof does not establish a deterministic explicit coefficient realization or bounds on the first qualifying derivative order for a particular open set.

## Assumptions and scope

For an entire \(g(z)=\sum_{n\ge0}a_nz^n\), let its order be
\[
 \rho(g)=\limsup_{n\to\infty}\frac{n\log n}{\log(1/|a_n|)},
\]
when the usual coefficient formula applies, with vanishing coefficients omitted. Finite exponential type means that there are \(C,\tau>0\) for which \(|g(z)|\le C e^{\tau|z|}\) everywhere. A transcendental function is nonpolynomial; polynomials are explicitly excluded because sufficiently high derivatives vanish identically.

Define the increasing deterministic weights
\[
 L_j=\bigl(\log(j+e)\bigr)^2,\quad
 B_0=1,\quad B_n=\prod_{j=1}^{n}L_j\quad(n\ge1).
\]
Let \((\xi_n)_{n\ge0}\) be independent random variables, each uniformly distributed with normalized planar area on the closed complex unit disk. Set
\[
 f(z)=\sum_{n=0}^{\infty}\xi_n\frac{B_n}{n!}z^n,
 \qquad F_n(z)=f^{(n)}(z)
 =\sum_{m\ge0}\xi_{n+m}\frac{B_{n+m}}{m!}z^m.
\]
Since \(\log B_n=2n\log\log n+O(n)\), this series converges normally on compact sets for every realization with \(|\xi_n|\le1\).

## Proof

**1. Two deterministic saddle estimates.** Fix \(R>0\). For all sufficiently large \(n\), uniformly over \(|z|\le R\),
\[
 |F_n(z)|\le 2B_n\exp\bigl(|z|L_{2n}\bigr).
 \tag{1}
\]
Indeed, for \(0\le m\le n\), monotonicity of \(L_j\) gives \(B_{n+m}/B_n\le L_{2n}^{m}\); summing these terms gives \(e^{|z|L_{2n}}\). For \(m>n\), \(n+m<2m\), so Stirling's lower bound \(m!\ge(m/e)^m\) gives
\[
 \frac{B_{n+m}}{B_n}\frac{R^m}{m!}
 \le\left(\frac{eR(\log(2m+e))^2}{m}\right)^m
 \le 2^{-m}
\]
for all \(m>n\), once \(n\) is large depending on \(R\). The tail is at most \(2^{-n}\), proving (1).

Now fix \(0<\delta\le |z|\le R\), and put \(x=|z|L_n\), \(m=\lfloor x\rfloor\); for large \(n\), \(m\ge1\). Since \(B_{n+m}/B_n\ge L_n^m\), the coefficient of \(\xi_{n+m}\) in \(F_n(z)\) has modulus
\[
 A_{n,m}(z)=\frac{B_{n+m}|z|^m}{m!}
 \ge B_n\frac{x^m}{m!}
 \ge B_n\frac{e^{x-1}}{3\sqrt x}.
 \tag{2}
\]
For the last inequality use \(m!\le3\sqrt m(m/e)^m\), \(m\le x<m+1\), and \((x/m)^m\ge1\). With
\[
 H_{n,R}=3+\log(1+RL_n),\qquad
 p_n(z)=\log B_n+|z|L_n,
\]
equation (2) implies \(\log A_{n,m}(z)\ge p_n(z)-H_{n,R}\).

**2. Uniform pointwise logarithmic anti-concentration.** Conditional on all coefficients except \(\xi_{n+m}\), one has \(F_n(z)=a\xi_{n+m}+w\) with \(|a|=A_{n,m}(z)\). Planar uniform measure satisfies
\[
 \mathbb P\{|a\xi+w|<\epsilon\}\le(\epsilon/|a|)^2
 \qquad(a\ne0),
\]
because the preimage of a radius-\(\epsilon\) disk has area at most \(\pi(\epsilon/|a|)^2\). Therefore, for all \(s\ge0\) and sufficiently large \(n\),
\[
 \mathbb P\{p_n(z)-\log|F_n(z)|>H_{n,R}+s\}\le e^{-2s}
 \qquad(\delta\le|z|\le R).
 \tag{3}
\]
At an isolated zero, the logarithm is interpreted as \(-\infty\); this convention changes neither the pointwise probability (the conditional law is nonatomic) nor the circle integrals below. Almost surely no \(F_n\) is identically zero.

Define the nonnegative deficit
\[
 D_n(z)=\max\{p_n(z)-\log|F_n(z)|-H_{n,R},0\}.
\]
The tail bound (3) gives the **exact integrability estimate**
\[
 \mathbb E e^{D_n(z)}
 =1+\int_0^\infty e^s\mathbb P\{D_n(z)>s\}\,ds\le2.
 \tag{4}
\]

**3. A summable zero-free disk estimate.** Fix \(c\in\mathbb C\setminus\{0\}\) and \(r>0\) with \(2r<|c|\), and let \(R=|c|+2r\) and \(\delta=|c|-2r>0\). Consider the circle \(z_\theta=c+re^{i\theta}\), and write \(\overline{h}=(2\pi)^{-1}\int_0^{2\pi}h(z_\theta)\,d\theta\). Applying Jensen's inequality to the exponential and Fubini/Tonelli to (4),
\[
 \mathbb E\exp(\overline{D_n})\le
 \overline{\mathbb E e^{D_n(z_\theta)}}\le2,
 \qquad
 \mathbb P\{\overline{D_n}\ge t\}\le2e^{-t}.
 \tag{5}
\]
Set
\[
 \gamma(c,r)=\frac1{2\pi}\int_0^{2\pi}|c+re^{i\theta}|\,d\theta-|c|>0.
\]
Strict positivity follows from \(\Delta|z|=1/|z|>0\) off the origin, because the closed disk centered at \(c\) of radius \(r\) misses \(0\). In fact the Green-area formula gives \(\gamma(c,r)\ge r^2/(4(|c|+r))>0\).

On the event \(E_n(c,r)\) that \(F_n\) has **no zero anywhere in** \(B(c,2r)\), its logarithmic modulus is harmonic near the closed radius-\(r\) disk; therefore \(\overline{\log|F_n|}=\log|F_n(c)|\). Since the maximum defining \(D_n\) is at least its second argument, estimate (1) at \(c\) gives on this event
\[
 \overline{D_n}\ge
 \gamma(c,r)L_n-|c|(L_{2n}-L_n)-H_{n,R}-\log2.
 \tag{6}
\]
Here \(L_n=(\log(n+e))^2\sim(\log n)^2\), \(L_{2n}-L_n=O(\log n)\), and \(H_{n,R}=O(\log\log n)\). Consequently, for all sufficiently large \(n\) depending on the disk, the right-hand side of (6) is at least \(\gamma(c,r)L_n/2\). By (5),
\[
 \mathbb P(E_n(c,r))\le2\exp\bigl(-\gamma(c,r)L_n/2\bigr).
 \tag{7}
\]
The right-hand side is summable over positive integers \(n\): for every \(q>1\), \(\exp(-\gamma(\log n)^2/2)=o(n^{-q})\).

Choose the countable family of balls \(B(c,2r)\) with nonzero rational-complex centers \(c\), positive rational radii \(r\), and \(2r<|c|\). These balls form a subbasis sufficient for every nonempty open subset of \(\mathbb C\): each open set contains such a ball, since it contains a point other than the origin. First Borel--Cantelli applied to (7), followed by countable intersection, yields with probability one: for each of these balls, every sufficiently high derivative has a zero inside it. It follows that every nonempty open \(U\) contains a zero of \(F_n\) for all sufficiently large \(n\). No independence across derivative orders is required here.

**4. Order and exponential type.** Since the coefficient law is nonatomic, \(\xi_n\ne0\) for every \(n\) almost surely. Also \(|\xi_n|\ge1/2\) occurs infinitely often almost surely (independence and probability \(3/4\)). Since
\[
 \log B_n=2n\log\log n+O(n),\qquad
 \log(n!)=n\log n-n+O(\log n),
\]
the coefficient formula for order gives \(\rho(f)\le1\) for every sample and \(\rho(f)=1\) along the infinitely many indices with \(|\xi_n|\ge1/2\). On that same subsequence,
\[
 |f^{(n)}(0)|^{1/n}=(|\xi_n|B_n)^{1/n}
 \sim(\log n)^2\longrightarrow\infty.
\]
Every finite-exponential-type entire function has \(|f^{(n)}(0)|=O(\sqrt n\,\tau^n)\) for some finite \(\tau\), by Cauchy's estimate with radius proportional to \(n\). Thus our function has infinite exponential type.

**5. Exclusion of finite exponential type.** Let \(g\) be transcendental and satisfy \(|g(z)|\le C e^{\tau|z|}\) with \(\tau>0\). Put \(b_n=g^{(n)}(0)\). Cauchy's estimate at radius \(n/\tau\), together with Stirling, gives \(|b_n|\le C'\sqrt n\,\tau^n\). Choose \(\lambda>\tau\), so \(|b_n|/\lambda^n\to0\), and choose \(r>0\) so small that \(e^{\lambda r}-1<1\). For any \(N\), since \(g\) is nonpolynomial, the positive maximum
\[
 M_N=\max_{k\ge N}\frac{|b_k|}{\lambda^k}
\]
is attained at some index \(n\ge N\). If \(g^{(n)}(z)=0\) for some \(|z|<r\), Taylor's theorem at the origin and the maximality of the normalized coefficient imply
\[
 |b_n|\le\sum_{m\ge1}\frac{|b_{n+m}|r^m}{m!}
 \le M_N\lambda^n\bigl(e^{\lambda r}-1\bigr)
 <M_N\lambda^n=|b_n|,
\]
a contradiction. Thus for every \(N\) some derivative of order \(n\ge N\) is zero-free in \(B(0,r)\), so the cofinite property is impossible. Every entire function of order less than \(1\) has finite exponential type (indeed type zero), completing the sharpness proof. \(\square\)

## Verification

The proof rests on elementary inequalities and probability identities rather than on finite numerical experiments: coefficient monotonicity, the two explicit Stirling bounds, the exact planar disk small-ball estimate, the logarithmic tail integration (4), Jensen's inequality on a circle, the harmonic mean-value identity conditional on zero-freeness, and first Borel--Cantelli. The summability check is asymptotic over all orders, not a truncated enumeration. The maximal-coefficient argument proves the converse for all finite-exponential-type transcendental entire functions. None of these steps requires any external formal proof system or a numerical search.

The key quantitative gain is \(\gamma(c,r)L_n\asymp(\log n)^2\), while the comparison errors grow only as \(O(\log n)\). This strict scale separation is why the hole probabilities are summable. The coefficient normalization \(B_n/n!\) also directly certifies order exactly \(1\).

## Relationship to prior work

Hou's July 2026 preprint proves the same cofinite zero-hitting property for a bounded-coefficient Fock series of order exactly \(2\) and finite type, with weights \(1/\sqrt{n!}\). The current theorem establishes the previously unevaluated sharp **order threshold** by replacing those weights with \(B_n/n!\), obtaining order \(1\) of necessarily infinite type and proving the converse via normalized Taylor coefficients. Hou discusses the earlier Almeida and Chojecki Gaussian constructions; they also use \(1/\sqrt{n!}\), not the order-one weight sequence above.

The 1972 Barth--Schneider theorem prescribes derivative zeros along a selected sequence of derivative orders, which does not imply the cofinite condition. Classical work of Boas--Reddy on successive derivative zeros contains a printed general finite-type claim invalidated by Hou's order-two construction; no such disputed assertion is used in this proof. The independent converse given above depends only on the elementary finite-exponential-type coefficient bound. Publicly indexed literature and related-result searches did not locate an equivalent order-one construction or optimal threshold, but the absence of a search result cannot certify uniqueness.

## Limitations

Existence is almost sure under the specified coefficient law, not an explicit deterministic series with identified coefficients. The theorem does not optimize the slowly varying weights, hole probabilities, or \(N(U)\), nor does it establish finite exponential type at order one (which the converse proves impossible). An independently checked publication-level novelty determination remains outstanding; in particular, an independently circulated April 2026 proposed-solution PDF and some older proceedings literature were not inspected in full. These are prior-art risks, not gaps filled by assuming the sources absent. The proof covers nonpolynomial entire functions only.

## References

1. Eric Hou, *Cofinite Zeros of High Derivatives*, arXiv:2607.20816v1, first posted 23 July 2026. See the open manuscript and author-posted source at `https://arxiv.org/abs/2607.20816` and `https://github.com/erichou1/cofinite-derivative-zeros/blob/main/paper.tex`.
2. K. F. Barth and W. J. Schneider, *On a Problem of Erdős Concerning the Zeros of the Derivatives of an Entire Function*, 1972; primary full text publicly indexed at `https://www.researchgate.net/publication/238868008_On_a_Problem_of_Erdos_Concerning_the_Zeros_of_the_Derivatives_of_an_Entire_Function`.
3. R. P. Boas and A. R. Reddy, *Zeros of successive derivatives of entire functions*, 1973; bibliographic indexing `https://portal.mardi4nfdi.de/wiki/Zeros_of_successive_derivatives_of_entire_functions`.
4. A. Almeida, proposed solution of Erdős problem 906 (April 2026), archive `https://github.com/Drill23/erdos-problem-906-proposed-solution` (repository README examined; full manuscript not adjudicated).
