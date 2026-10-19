# A sharp return-count profile across Chung–Feller occupations of a random-walk bridge

## Finding

For each integer \(n\ge 1\), choose uniformly one of the \(\binom{2n}{n}\) nearest-neighbor walks of length \(2n\) from \(0\) back to \(0\), with increments \(+1\) and \(-1\). Let \(A\) be **half** the number of steps whose open midpoint has positive height. Thus \(A\in\{0,\ldots,n\}\); each complete strictly positive excursion of duration \(2\ell\) contributes \(\ell\) to \(A\). Let \(K\) count all completed excursions, equivalently the number of visits to height zero at positive times, **including** the terminal visit.

Write \(C_r=\frac{1}{r+1}\binom{2r}{r}\) for the Catalan numbers and \(m_{n,j}=\mathbb E[K\mid A=j]\). Then **the exact conditional regression** is
\[
m_{n,j}=\frac{1}{C_n}\sum_{a=0}^{j}\sum_{b=0}^{n-j}
  C_{a+b}C_{n-a-b}-1,\qquad 0\le j\le n.
\]
It satisfies \(m_{n,j}=m_{n,n-j}\), \(m_{n,0}=m_{n,n}=3n/(n+2)\), and, for every \(0\le j<(n-1)/2\),
\[
m_{n,j+1}-m_{n,j}=
\frac{1}{C_n}\sum_{s=j+1}^{n-j-1}C_s C_{n-s}>0.
\]
For odd \(n\), the two central levels have identical maximum expectation; for even \(n\), the unique central level maximizes it. The regression strictly decreases beyond the central level(s). In particular, conditioning on balanced occupation maximizes the expected number of returns, while an extreme one-sided occupation minimizes it.

For each fixed \(t\in(0,1)\), this dependence persists on the macroscopic scale:
\[
\lim_{n\to\infty}\frac{m_{n,\lfloor tn\rfloor}}{\sqrt n}
=\frac{8}{\sqrt\pi}\sqrt{t(1-t)}.
\]
The endpoint expectations remain bounded, tending to \(3\), whereas central expectations grow as \(4\sqrt{n/\pi}\).

There is simultaneously a sharp distinction between linear and quadratic dependence. Although
\[\operatorname{Cov}(A,K)=0,\]
one has, for all \(n\ge1\),
\[
\boxed{\operatorname{Cov}\!\left(\left(A-\frac n2\right)^2,K\right)
=-\frac{n(n-1)4^n}{48\binom{2n}{n}}.}
\]
The covariance is strictly negative for \(n\ge2\), with equality at \(n=1\). Moreover,
\[
\lim_{n\to\infty}\operatorname{Cov}\!\left(
 \left(\frac An-\frac12\right)^2,\frac K{\sqrt n}\right)
=-\frac{\sqrt\pi}{48}.
\]
These statements constitute one joint dependence theorem for occupation and excursion count; the conditional regression is the principal structural assertion, and the quadratic covariance quantifies its centered consequence.

## Assumptions and scope

A walk is a sequence \(S_0=0,S_1,\ldots,S_{2n}=0\), with increments in \(\{-1,+1\}\), under the uniform law on such sequences. A step from height \(h\) to height \(h'\) is counted as positive exactly when \((h+h')/2>0\). This convention includes a final down-step from height \(1\) to \(0\) and excludes a final up-step from height \(-1\) to \(0\). Because excursions from zero have even durations, the total number of counted steps is even and \(A\) is an integer. Each return to zero after time zero terminates one excursion. All formulas concern this bridge model and this occupation convention, not an unconditioned walk.

## Proof

**1. Excursion generating functions and uniform occupation.** Every strictly positive excursion of \(2\ell\) steps has \(C_{\ell-1}\) possible shapes; reflection gives the same number for a negative excursion. Put
\[
P(z)=\sum_{\ell\ge1}C_{\ell-1}z^\ell
=\frac{1-\sqrt{1-4z}}2,
\qquad P(z)(1-P(z))=z.
\]
Concatenating signed excursions and marking positive half-duration by \(x\), negative half-duration by \(y\), and excursion count by \(u\), gives the *exact* ordinary generating function
\[
F(x,y,u)=\frac{1}{1-u(P(x)+P(y))}.
\]
Its coefficient of \(x^j y^{n-j}u^k\) counts bridges with occupation \(j\) and exactly \(k\) completed excursions. The identity \(x-y=(P(x)-P(y))(1-P(x)-P(y))\) implies
\[
F(x,y,1)=\frac{P(x)-P(y)}{x-y}
=\sum_{a,b\ge0}C_{a+b}x^a y^b.
\]
Consequently exactly \(C_n\) bridges have \(A=j\), for every \(0\le j\le n\). Thus \(A\) is uniform on \(\{0,\ldots,n\}\), recovering the classical bridge form of the Chung–Feller law. This is used as a known ingredient, not claimed as novel.

**2. Conditional regression and strict shape.** Differentiating the marked generating function and setting \(u=1\) gives
\[
\left.\partial_u F(x,y,u)\right|_{u=1}
=F(x,y,1)^2-F(x,y,1).
\]
Coefficient extraction and division by \(C_n\) give the announced expression for \(m_{n,j}\). At \(j=0\), the Catalan convolution \(\sum_{s=0}^n C_sC_{n-s}=C_{n+1}\) gives \(m_{n,0}=C_{n+1}/C_n-1=3n/(n+2)\). Symmetry follows on swapping \(x,y\). For adjacent occupation levels \(j\) and \(j+1\), the sums differ only by one added column and one deleted row:
\[
C_n(m_{n,j+1}-m_{n,j})
=\sum_{s=j+1}^{n}C_sC_{n-s}-\sum_{s=n-j}^{n}C_sC_{n-s}.
\]
For \(j<(n-1)/2\) this equals the strictly positive middle sum displayed above. At the central transition for odd \(n\) it is zero, and the remaining inequalities follow by symmetry. All strictness and boundary cases are therefore exact.

**3. Conditional-scale limit.** Stirling's formula gives, uniformly on compact subintervals of \((0,1)\),
\[
\frac{C_{\lfloor un\rfloor} C_{n-\lfloor un\rfloor}}{C_n}
\sim\frac{1}{\sqrt\pi\,n^{3/2}[u(1-u)]^{3/2}}.
\]
For \(0<t<1/2\), the exact increment formula therefore yields
\[
\sqrt n\,(m_{n,\lfloor tn\rfloor+1}-m_{n,\lfloor tn\rfloor})
\longrightarrow\frac{4(1-2t)}{\sqrt\pi\sqrt{t(1-t)}}.
\]
To justify summing these limits down to the endpoint, standard two-sided Catalan bounds imply the uniform estimate \(0\le m_{n,j+1}-m_{n,j}\le M/\sqrt{j+1}\) for \(0\le j<n/2\), with a numerical constant \(M\) independent of \(n\). The normalized initial segment of length \(\delta n\) is consequently bounded by \(O(\sqrt\delta)\). Away from that segment ordinary Riemann-sum convergence applies. Since \(m_{n,0}/\sqrt n\to0\), integration of the preceding limit gives
\[
\frac4{\sqrt\pi}\int_0^t \frac{1-2v}{\sqrt{v(1-v)}}\,dv
=\frac8{\sqrt\pi}\sqrt{t(1-t)}.
\]
Symmetry covers \(t\ge1/2\), including the central level.

**4. Exact quadratic dependence.** Conditional on the sequence of unsigned excursion half-lengths \(L_1,\ldots,L_K\), the excursion signs are independent fair signs \(\epsilon_i\in\{-1,+1\}\), and \(\sum_iL_i=n\). Hence
\[
A-\frac n2=\frac12\sum_{i=1}^{K}\epsilon_iL_i,
\quad
\mathbb E[A\mid L_1,\ldots,L_K]=\frac n2,
\quad
\mathbb E\!\left[\left(A-\frac n2\right)^2\mid L_1,\ldots,L_K\right]
=\frac14\sum_iL_i^2.
\]
In particular, \(\operatorname{Cov}(A,K)=0\). Write \(H=\sum_iL_i^2\) and \(D=z\frac{d}{dz}\). Marking one excursion by its squared half-duration and then marking the number of excursions yields the two exact power series
\[
\sum_{n\ge0}\sum_{\text{bridges of size }2n} H z^n
=\frac{2D^2P(z)}{(1-2P(z))^2}
=z\big[(1-4z)^{-5/2}+(1-4z)^{-3/2}\big]
\]
and
\[
\sum_{n\ge0}\sum_{\text{bridges of size }2n} KH z^n
=\frac{2D^2P(z)(1+2P(z))}{(1-2P(z))^3}
=z\big[2(1-4z)^{-3}-(1-4z)^{-5/2}
  +2(1-4z)^{-2}-(1-4z)^{-3/2}\big].
\]
Using \([z^n](1-4z)^{-1/2}=\binom{2n}{n}\) and the ordinary binomial-series identities, these imply
\[
\mathbb E[H]=\frac{n(n+2)}3,\quad
\mathbb E[KH]=\frac{4^{n-1}n(n+3)}{\binom{2n}{n}}-\frac{n(n+2)}3,
\quad
\mathbb E[K]=\frac{4^n}{\binom{2n}{n}}-1.
\]
Their covariance is \(\operatorname{Cov}(H,K)=-n(n-1)4^n/[12\binom{2n}{n}]\). The preceding conditional second-moment identity divides this by four and proves the boxed formula. Finally, \(\binom{2n}{n}\sim4^n/\sqrt{\pi n}\) proves the normalized limit. No finite enumeration is used to infer an infinite statement.

## Verification

Run `python verify.py` with Python's standard library. The self-contained verifier independently enumerates all bridges through \(16\) steps and compares them with a Catalan-excursion dynamic program; it checks occupation marginals, exact conditional means, sign/equality cases, the squared-occupation covariance, and rational telescoping identities through size \(120\). It also compares several large-size values with the asymptotic profile. The implementation executed successfully with **25,711 assertions**. Its finite checks corroborate the analytic proof and do not constitute a proof for all sizes or all real scaling fractions.

## Relationship to prior work

Chung and Feller established the special occupation convention and its uniformity for a bridge. Lachal's 2010 preprint gives a detailed bivariate generating function for sojourn time and bridge endpoint, including Theorem 6.1 and Theorem 6.2: at the bridge endpoint it specializes to the unmarked function \(F(x,y,1)\) above. Those results do not directly present excursion-return marking, the evaluated conditional return regression, strict central unimodality, or the quadratic dependence identity.

Banderier and Flajolet develop general algebraic generating functions for lattice paths, bridges and excursions. Their framework contains tools sufficient to enumerate the same walks, but the investigated sections do not evaluate the present conditional return-count profile. Pitman's work derives distributions of Brownian-bridge local time, a related *continuous* observable, not the asserted finite discrete regression. The present claim does not assert novelty of Catalan numbers, Chung–Feller uniformity, primitive-excursion decomposition, or generic generating-function differentiation.

## Limitations

The theorem is restricted to symmetric nearest-neighbor bridges with equal counts of positive and negative steps; a drifted walk conditioned to return has the same bridge law, but nonnearest-neighbor or nonbridge analogues are not established here. \(A\) uses the precise midpoint-positive step convention; counting strict-positive vertices instead gives another statistic. The regression describes only a conditional mean, not stochastic ordering of the entire conditional return-count distribution. Asymptotic assertions hold for fixed interior occupation fraction; no uniform approximation at boundaries is claimed. General lattice-path enumeration could conceivably contain an implicit prior derivation of the new formulas, so historical priority requires independent literature validation.

## References

1. A. Lachal, *Sojourn time in \(\mathbb Z^+\) for the Bernoulli random walk on \(\mathbb Z\)*, first arXiv posting 2010-03-25, arXiv:1003.5009, especially Theorems 6.1–6.2. https://arxiv.org/abs/1003.5009
2. K. L. Chung and W. Feller, *On fluctuations in coin-tossing*, Proceedings of the National Academy of Sciences **35** (1949), 605–608. Cited as historical background in Lachal (2010).
3. C. Banderier and P. Flajolet, *Basic analytic combinatorics of directed lattice paths*, Theoretical Computer Science **281** (2002), 37–80. https://www-lipn.univ-paris13.fr/~banderier/Papers/tcs_banderier_flajolet_2002.pdf
4. J. Pitman, *The distribution of local times of a Brownian bridge*, Séminaire de Probabilités XXXIII (1999), 388–394. https://www.numdam.org/item/SPS_1999__33__388_0.pdf
