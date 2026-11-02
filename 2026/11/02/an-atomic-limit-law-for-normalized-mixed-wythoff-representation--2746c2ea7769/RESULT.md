# An atomic limit law for normalized mixed Wythoff representation counts

## Finding
Put \(\varphi=(1+\sqrt5)/2\), \(\alpha=\varphi^{-1}\), and \(\beta=\varphi^{-2}=1-\alpha=(3-\sqrt5)/2\). For every integer \(n\ge1\), let
\[
r(n)=\#\{(h,k)\in\mathbb Z_{\ge1}^2:\lfloor h\varphi\rfloor+\lfloor k\varphi^2\rfloor=n\}.
\]
Define the continuous function \(g:[0,1]\to[0,\beta]\) by
\[
g(t)=\begin{cases}\beta-t,&0\le t\le\beta,\\t-\beta,&\beta\le t\le2\beta,\\\beta,&2\beta\le t\le1.\end{cases}
\]
Then **uniformly for all positive integers** \(n\),
\[
\boxed{r(n)=n\,g(\{n\alpha\})+O(\log(n+2))}.
\]
For uniformly sampled \(n\in\{1,\ldots,X\}\), the normalized representation count \(r(n)/n\) converges in distribution as \(X\to\infty\) to the probability measure
\[
\boxed{\mu=2\,\mathbf1_{(0,\beta)}(y)\,dy+(1-2\beta)\delta_\beta}.
\]
In particular, this law has a genuine atom of mass \(1-2\beta=\sqrt5-2\) at its right endpoint \(\beta\); its remaining mass \(2\beta\) has constant density \(2\) on \((0,\beta)\). For every fixed real \(s>0\),
\[
\lim_{X\to\infty}\frac1X\sum_{n=1}^X\bigl(r(n)/n\bigr)^s
=\frac{2\beta^{s+1}}{s+1}+(1-2\beta)\beta^s.
\]

## Assumptions and scope
The lower and upper Wythoff sequences are \(U=\{\lfloor h\varphi\rfloor:h\ge1\}\) and \(V=\{\lfloor k\varphi^2\rfloor:k\ge1\}\). Pairs \((h,k)\) are ordered by which sequence supplies each summand; each sequence is strictly increasing, so this equals the number of decompositions \(n=u+v\) with \(u\in U\) and \(v\in V\). Only positive summands are counted. The error constant is absolute and independent of \(n\). Here \(\{x\}=x-\lfloor x\rfloor\). The displayed convergence means weak convergence of empirical probability measures on the real line.

## Proof
**1. Rotation representation.** By the complementary Beatty theorem, \(U\) and \(V\) partition the positive integers. The indicator of membership in \(U\) is
\[
w(m)=\lfloor(m+1)\alpha\rfloor-\lfloor m\alpha\rfloor
=\mathbf1_{[\beta,1)}(\{m\alpha\}),\qquad m\ge1.
\]
This follows because \(\alpha=1/\varphi\), so \(\lfloor(m+1)\alpha\rfloor-\lfloor m\alpha\rfloor\) counts whether a lower-Beatty integer equals \(m\). Consequently
\[
r(n)=\sum_{m=1}^{n-1}w(m)(1-w(n-m)).
\]

**2. A moving interval.** Fix \(n\ge2\), put \(t=\{n\alpha\}\) and \(x=\{m\alpha\}\). Since \(\{(n-m)\alpha\}=\{t-x\}\), simultaneous conditions \(w(m)=1\), \(w(n-m)=0\) mean \(x\in[\beta,1)\) and \(\{t-x\}<\beta\). Solving these inequalities separately for \(t<\beta\), \(\beta<t<2\beta\), and \(t>2\beta\) yields, respectively,
\[
I_t=(\alpha+t,1),\quad I_t=(\beta,t),\quad I_t=(t-\beta,t),
\]
up to interval endpoints, whose contribution is at most an absolute constant. Their lengths are \(\beta-t\), \(t-\beta\), and \(\beta\), respectively, i.e. \(|I_t|=g(t)\). At the two transition points either adjacent description has the same length; in fact \(\{n\alpha\}\) never equals those points for any positive integer \(n\). Hence
\[
r(n)=\#\{1\le m<n:\{m\alpha\}\in I_{\{n\alpha\}}\}+O(1).
\]

**3. Uniform discrepancy.** For \(\alpha=(\sqrt5-1)/2\), continued-fraction convergent denominators are successive Fibonacci numbers \(q_j\) and \(|\alpha-p_j/q_j|<q_j^{-2}\). For any starting phase \(\theta\), the \(q_j\) points \(\{\theta+\ell\alpha\}\), \(0\le\ell<q_j\), are within circular distance \(1/q_j\) of a translated complete rational grid \(\{\theta+\ell p_j/q_j\}\). Because \(p_j\) is coprime to \(q_j\), that grid hits any interval in \(q_j|I|+O(1)\) points, and moving its nodes by at most \(1/q_j\) changes the count by at most an absolute constant. Thus every consecutive block of \(q_j\) orbit points has discrepancy \(O(1)\), uniformly in starting index and interval. Greedy expansion of an integer \(N\) in the Fibonacci denominators uses \(O(\log(N+2))\) blocks. Therefore, uniformly for every interval \(I\subset[0,1)\),
\[
\#\{1\le m\le N:\{m\alpha\}\in I\}=N|I|+O(\log(N+2)).
\]
Use \(N=n-1\), \(I=I_{\{n\alpha\}}\) and \(0\le g\le\beta\) to obtain the claimed \(r(n)=ng(\{n\alpha\})+O(\log(n+2))\). For \(n=1\), enlarge the absolute error constant.

**4. Limit law and moments.** The irrational rotation \(\{n\alpha\}\) is equidistributed in \([0,1)\). Since \(g\) is continuous and the approximation error divided by \(n\) tends uniformly to zero as \(n\to\infty\), the empirical law of \(r(n)/n\) is the pushforward of Lebesgue measure by \(g\). Each of the first two linear branches covers \((0,\beta)\) once with slope magnitude one, contributing density one apiece. The third branch, of length \(1-2\beta\), is constant \(\beta\), giving the endpoint atom. Integration of \(y^s\), which is continuous on the common bounded range, gives the moment formula for every fixed \(s>0\). This proves all statements.

## Verification
The accompanying `verify.py` checks both (i) the definition by independent generated Beatty sets and (ii) the convolution of exact floor-difference membership indicators for all \(1\le n\le750\). It constructs floor values using rational lower/upper bounds for \(\sqrt5\), checking that both bounds give the same integer before use. It compares the exact counts with the predicted rotation profile and finds maximum absolute residual below \(1.469\) over this finite range. These computations are independent of the infinite proof; finite checking cannot prove the discrepancy estimate or distributional convergence.

## Relationship to prior work
Ashburn's arXiv:2610.04842v1 proves exact classifications for \(r(n)=0,1,2\); it does not determine the normalized global representation-count distribution. Shallit's arXiv:2006.04177 (Section 11.2) explains how to obtain a rank-19 Fibonacci-automatic linear representation for the *exact* mixed-Beatty count. That is a substantially stronger computational evaluation framework than merely knowing the count at isolated inputs, but its displayed theorem and discussion do not state the uniform moving-interval asymptotic or the limiting measure with its endpoint atom. An earlier analysis of the linear representation might still imply this law, so priority beyond the inspected documents is not certified. OEIS A259598 records the representation sequence and low-count conjectures. A separate study of Fibonacci-interval maxima of the same \(r(n)\) concerns extrema, not the global weak limit, and does not imply the asserted atom or density.

## Limitations
The error bound is \(O(\log n)\), not a sharp absolute error bound or an exact finite-\(n\) count. The theorem does not describe local fluctuations inside the endpoint atom, shrinking windows, or effective convergence rates for arbitrary test functions. The result is subject to possible earlier equivalent formulations and has not undergone independent mathematical audit.

## References
1. A. Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words*, arXiv:2610.04842v1 (first public 2026-10-04), Sections 1 and 3, https://arxiv.org/abs/2610.04842.
2. J. Shallit, *Sumsets of Wythoff sequences, Fibonacci representation, and beyond*, arXiv:2006.04177, Section 11.2, https://arxiv.org/abs/2006.04177.
3. OEIS A259598, mixed lower-plus-upper Wythoff representation counts, https://oeis.org/A259598.
4. Classical complementary Beatty theorem, continued-fraction discrepancy for bounded-type irrational rotations, and Weyl equidistribution theorem (used explicitly in the proof).
