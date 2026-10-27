# Parity bifurcation and an essential singularity in Bernstein absolute moments

## Finding
For each integer \(n\ge2\), each real \(r>1\), and \(p\in[0,1]\), let
\[
M_{n,r}(p)=\sum_{k=0}^n\binom nk p^k(1-p)^{n-k}\left|\frac{k}{n}-p\right|^r.
\]
This is the absolute central moment of order \(r\) of the classical degree-\(n\) Bernstein kernel. At \(r=2\), its unique maximizing position is \(p=1/2\), since \(M_{n,2}(p)=p(1-p)/n\).

**Theorem.** For each fixed integer \(n\ge2\), there exists \(\eta_n>0\) with the following conclusions for \(2-\eta_n<r<2+\eta_n\).

* If \(n\) is odd, \(p=1/2\) is the unique global maximizer of \(M_{n,r}\).
* If \(n\) is even and \(r\ge2\), \(p=1/2\) is the unique global maximizer.
* If \(n\) is even and \(r<2\), there are exactly two global maximizers \(p=1/2\pm d_{n,r}\), with \(0<d_{n,r}<1/2\). Writing \(b_n=2^{-n}\binom{n}{n/2}\), their displacement obeys the sharp essential-singularity law
\[
\boxed{\lim_{r\uparrow2}(2-r)\log\frac1{d_{n,r}}=\log\left(1+\frac1{n b_n}\right).}
\]
Moreover, with \(\mathcal M_{n,r}=\max_{0\le p\le1}M_{n,r}(p)\), the gain over the symmetric position satisfies
\[
\boxed{\mathcal M_{n,r}-M_{n,r}(1/2)\sim\frac{(b_n+1/n)(2-r)}2\,d_{n,r}^2}\qquad(r\uparrow2,\ n\ \text{even}).
\]
Consequently, the gain itself has exponential rate
\[
\lim_{r\uparrow2}(2-r)\log\frac1{\mathcal M_{n,r}-M_{n,r}(1/2)}=2\log\left(1+\frac1{n b_n}\right).
\]
All limits keep \(n\) fixed; there is no claim of a degree-uniform interval \(\eta_n\), or of a complete phase diagram for exponents far from two.

## Assumptions and scope
Use the standard normalized Bernstein basis on the closed interval \([0,1]\), with integer degree \(n\ge2\). The absolute-moment exponent is real and varies in a sufficiently small, degree-dependent neighborhood of two, always remaining above one. Maximizers are taken over all \(p\in[0,1]\). The even-degree constant \(b_n\) is the exact binomial probability of its central lattice atom at \(p=1/2\), and is strictly positive.

## Proof
**1. Symmetry, variance, and derivative control.** Replacing \(k\) by \(n-k\) yields \(M_{n,r}(1-p)=M_{n,r}(p)\). The binomial variance identity gives \(M_{n,2}(p)=p(1-p)/n\). For \(r\) in a compact neighborhood of two contained in \((1,\infty)\), the summands \(p^k(1-p)^{n-k}|k/n-p|^r\) and their first \(p\)-derivatives depend jointly continuously on \((p,r)\), including points where a distance vanishes (the derivative of \(|z|^r\) is zero at \(z=0\)). Hence \(\partial_pM_{n,r}\to(1-2p)/n\) uniformly on \([0,1]\). In particular, for any fixed small \(h>0\), and all sufficiently near-two \(r\), the derivative is strictly negative on \([1/2+h,1]\); symmetry gives the opposite sign on \([0,1/2-h]\). Every global maximizer therefore lies within distance \(h\) of the center.

**2. Odd degree.** When \(n\) is odd, no lattice point \(k/n\) equals \(1/2\). Fix \(h>0\) smaller than the distance from \(1/2\) to the closest lattice point. All summands then have jointly continuous second derivatives in \((p,r)\) on \(|p-1/2|\le h\) for \(r\) near two. Since \(\partial_p^2M_{n,2}=-2/n\), these second derivatives sum to a strictly negative quantity there. Symmetry forces the first derivative to vanish at the center. The first-derivative signs inside and outside this neighborhood prove unique global maximality of \(1/2\).

**3. Even degree and its isolated central atom.** Let \(n=2m\), set \(\delta=p-1/2\), and isolate the term \(k=m\):
\[
M_{n,r}(1/2+\delta)=H_r(\delta)+W(\delta)|\delta|^r,\qquad W(\delta)=b_n(1-4\delta^2)^m.
\]
Here \(H_r\) is the sum over \(k\ne m\). For fixed \(0<h<1/n\), \(H_r\) is smooth in \(\delta\) on \([-h,h]\), uniformly for \(r\) near two, and is even. Consequently, with \(A_r=-H_r''(0)/2\),
\[
H_r'(\delta)=-2A_r\delta+O(\delta^3),\qquad H_r(\delta)-H_r(0)=-A_r\delta^2+O(\delta^4),
\]
where the errors are uniform for nearby \(r\). At order two, the entire expression equals \(1/(4n)-\delta^2/n\), while the isolated central term is \(b_n\delta^2+O(\delta^4)\). It follows that
\[
A_r\longrightarrow A=b_n+\frac1n>b_n\qquad(r\to2).
\]
For \(\delta>0\), put \(Q_r(\delta)=\partial_pM_{n,r}(1/2+\delta)/\delta\). Expanding the central term and the preceding Taylor series gives, uniformly for small positive \(\delta\),
\[
Q_r(\delta)=r b_n\delta^{r-2}\bigl(1+O(\delta^2)\bigr)-2A_r+O(\delta^2).
\]
For \(r\ge2\) sufficiently near two, \(\delta^{r-2}\le1\) when \(0<\delta<h<1\). Because \(2A>2b_n\), shrinking \(h\) and the exponent neighborhood makes \(Q_r(\delta)<0\) throughout \((0,h]\); first-derivative control outside \(h\) gives a unique maximizer at \(1/2\).

**4. Exactly two maxima below order two.** Let \(r=2-\varepsilon\), \(0<\varepsilon\ll1\), and define \(L=\log(A/b_n)>0\). Then \(Q_r(\delta)\to+\infty\) as \(\delta\downarrow0\). Put \(t_\varepsilon=\exp[-L/(2\varepsilon)]\). At this scale, \(\delta^{-\varepsilon}=e^{L/2}\), so
\[
Q_r(t_\varepsilon)\longrightarrow2b_n e^{L/2}-2A=2\sqrt{A b_n}-2A<0.
\]
For sufficiently small fixed \(h\), the uniform remainder estimates show that \(Q_r<0\) on \([t_\varepsilon,h]\): the leading positive factor \(\delta^{-\varepsilon}\) decreases as \(\delta\) increases, and its maximum there is \(e^{L/2}\). On \((0,t_\varepsilon]\), differentiation of the same smooth expansions gives
\[
Q_r'(\delta)=-\varepsilon r b_n\delta^{-\varepsilon-1}\bigl(1+O(\delta^2)\bigr)+O(\delta^{1-\varepsilon}+\delta)<0,
\]
because \(t_\varepsilon^2/\varepsilon\to0\). Thus \(Q_r\) decreases strictly from \(+\infty\) to a negative value on that interval and has exactly one zero \(d_{n,r}\). As \(\partial_pM_{n,r}=\delta Q_r(\delta)\), the moment increases up to that point and decreases afterward on \((1/2,1]\). Reflection supplies exactly the second global maximizer.

**5. Sharp displacement and gain.** The zero equation and the expansions imply
\[
r b_n d_{n,r}^{-\varepsilon}=2A_r+O(d_{n,r}^2),
\]
where the error is uniform. Taking logarithms gives
\[
\varepsilon\log(1/d_{n,r})=\log\bigl(2A_r/(r b_n)\bigr)+o(1)\longrightarrow\log(A/b_n).
\]
At the same critical point, \(b_n d_{n,r}^{r}=(2A_r/r)d_{n,r}^2+O(d_{n,r}^4)\). Therefore
\[
M_{n,r}(1/2+d_{n,r})-M_{n,r}(1/2)=\frac{A_r(2-r)}r d_{n,r}^2+O(d_{n,r}^4).
\]
The displacement is exponentially small in \(1/(2-r)\); hence \(d_{n,r}^2=o(2-r)\), and the error is negligible compared with \((2-r)d_{n,r}^2\). This proves the sharp gain and its logarithmic rate. \(\square\)

## Verification
The proof is analytic and applies to every fixed integer degree without relying on finite sampling. The accompanying `check_moments.py` independently evaluates exact finite binomial sums at high numerical precision, solves the positive-side first-derivative equation for sample even degrees, and compares \((2-r)\log(1/d_{n,r})\) with \(\log(1+1/(n b_n))\). Such computations test arithmetic and normalization but do not constitute a proof of uniqueness or of the limiting statements.

## Relationship to prior work
Adell, Bustamante, and Quesada (2015) define these Bernstein absolute moments and derive general degree-, parameter-, and exponent-dependent estimates with approximation-theoretic applications. Their accessible theorems give bounds, rather than the near-quadratic location and essential-singularity law asserted here. Berend and Kontorovich (2013) give an exact first absolute binomial moment and uniform bounds in that order; a result at order one does not imply the bifurcation or exponential displacement as the exponent approaches two. Relevant comparisons and remaining full-text-access uncertainty are recorded in the accompanying review.

## Limitations
The existence threshold \(\eta_n\) is not quantified or uniform in degree. Only exponents sufficiently close to two are classified. The result concerns moments of the standard binomial/Bernstein kernel, not all positive approximation kernels. The gain is extraordinarily small near the transition, so ordinary floating-point grids can fail to detect it. The 2015 primary paper could not be examined in full in the available accessible copy; unindexed or uninspected previous formulations remain a residual originality risk.

## References
1. J. A. Adell, J. Bustamante, and J. M. Quesada, *Estimates for the moments of Bernstein polynomials*, Journal of Mathematical Analysis and Applications 432 (2015), 114–128, doi:10.1016/j.jmaa.2015.05.020.
2. D. Berend and A. Kontorovich, *A sharp estimate of the binomial mean absolute deviation with applications*, Statistics & Probability Letters 83 (2013), 1254–1259, doi:10.1016/j.spl.2013.01.023 (publicly available 23 January 2013).
