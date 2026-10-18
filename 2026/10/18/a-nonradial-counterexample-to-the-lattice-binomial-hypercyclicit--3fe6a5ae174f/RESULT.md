# A nonradial counterexample to the lattice binomial hypercyclicity test

## Finding
Let \(V=\mathbb N_0^2\), \(s=i+j\), and define the angular departure from a central cone by
\[
h(i,j)=\max\{0,\,|i-j|-s/2\},\qquad
\mu_{i,j}=\frac{2^s}{s+1}\exp\bigl(-h(i,j)/100\bigr).
\]
Let \(B\) denote the unweighted backward lattice shift \((Bf)(i,j)=f(i+1,j)+f(i,j+1)\), acting on the weighted sequence spaces \(\ell^p(V,\mu)\), \(1\le p<\infty\), or \(c_0(V,\mu)\). Here \(\|f\|_p^p=\sum_{i,j}|\mu_{i,j}f(i,j)|^p\) and \(\|f\|_{c_0}=\sup_{i,j}|\mu_{i,j}f(i,j)|\), with the weighted coordinates tending to zero at infinity.

**Theorem.** The operator \(B\) is bounded on every stated space but is not hypercyclic on any of them. Nevertheless, for every fixed \((i,j)\in V\) and every \(1<p<\infty\), with \(q=p/(p-1)\), its original single-vertex binomial necessary condition holds **along the full sequence**:
\[
\lim_{n\to\infty}\sum_{\ell=0}^n
\left(\frac{\binom n\ell}{\mu_{i+\ell,j+n-\ell}}\right)^q=+\infty.
\]
Indeed the \(q\)-th root grows at least as \(2^{-i-j}\sqrt{2n/\pi}\,(1+o(1))\). The weight is genuinely nonradial: on the diagonal of even total degree \(s\),
\[
\frac{\mu_{s,0}}{\mu_{s/2,s/2}}=\exp(-s/200)\longrightarrow0.
\]
Thus the coordinatewise binomial test of Baranov–Lishanskii–Papathanasiou is not sufficient for hypercyclicity on the infinite quadrant, even for positive nonradial weights with uniformly bounded adjacent ratios.

## Assumptions and scope
All vertices have nonnegative integer coordinates. Weights are positive real numbers, the shift has two outgoing edges at every vertex, and the finite-difference functional below is well-defined and continuous on every listed space. No radiality, normality, or Hilbert-only assumption is imposed. The assertion concerns the failure of sufficiency of a particular necessary condition; it does **not** purport to characterize all hypercyclic nonradial lattice shifts or to negate the radial Hilbert-space classification available in the later literature.

## Proof
**Boundedness.** The function \(h\) is \(3/2\)-Lipschitz along coordinate edges because \(|i-j|\) changes by at most one and \((i+j)/2\) changes by \(1/2\). Consequently, for each \((i,j)\) and either coordinate successor \((i',j')\),
\[
\frac{\mu_{i,j}}{\mu_{i',j'}}
=\frac12\frac{s+2}{s+1}
\exp\left(\frac{h(i',j')-h(i,j)}{100}\right)
\le e^{3/200}.
\]
Each coordinate shift therefore has norm at most \(e^{3/200}\) on the weighted \(\ell^p\) and weighted \(c_0\) spaces; hence \(\|B\|\le2e^{3/200}\).

**Divergence of every single-vertex binomial test.** Fix \(i,j\) and write \(s_0=i+j\). Set \(\ell_n=\lfloor n/2\rfloor\). Then
\[
\big|\,(i+\ell_n)-(j+n-\ell_n)\,\big|
\le|i-j|+1,
\]
so \(h(i+\ell_n,j+n-\ell_n)=0\) for sufficiently large \(n\). Selecting the central summand in the \(\ell^q\) norm gives
\[
\left[\sum_{\ell=0}^n
\left(\frac{\binom n\ell}{\mu_{i+\ell,j+n-\ell}}\right)^q\right]^{1/q}
\ge\frac{n+s_0+1}{2^{n+s_0}}\binom n{\lfloor n/2\rfloor}
=2^{-s_0}\sqrt{\frac{2n}{\pi}}\,(1+o(1)),
\]
by the standard central-binomial asymptotic. This holds for each fixed \(q\in(1,\infty)\), along every \(n\to\infty\).

**A higher-order cancellation witness.** Define a nonzero continuous linear functional
\[
\Lambda(f)=f(0,3)-3f(1,2)+3f(2,1)-f(3,0).
\]
The binomial formula for \(B^n\) gives, for every \(n\ge0\),
\[
\Lambda(B^nf)=\sum_{r=0}^{n+3}c_{n,r}f(r,n+3-r),\qquad
\sum_{r=0}^{n+3}c_{n,r}z^r=(1-z)^3(1+z)^n.
\]
Parseval's identity and the beta integral give the *exact* coefficient-square sum
\[
\begin{aligned}
\sum_{r=0}^{n+3}|c_{n,r}|^2
&=\frac1{2\pi}\int_0^{2\pi}|1-e^{it}|^6|1+e^{it}|^{2n}\,dt\\
&=\frac{64\,4^n}{\pi}\,\mathrm B\!\left(\frac72,n+\frac12\right)\\
&=\frac{120}{(n+1)(n+2)(n+3)}\binom{2n}{n}.
\end{aligned}
\]
The last equality follows by writing \(\mathrm B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)\) and using the half-integer gamma identities. Hence Cauchy–Schwarz and the central-binomial bound give an absolute constant \(C>0\) such that
\[
\sum_r|c_{n,r}|\le\sqrt{n+4}\left(\sum_r|c_{n,r}|^2\right)^{1/2}
\le C\,2^n(n+1)^{-5/4}.
\]

**Exponential control outside the central cone.** Write \(N=n+3\) and \(C_N=\{r:0\le r\le N,\ |2r-N|\le N/2\}\). For \(r\in C_N\), \(h(r,N-r)=0\). If \(r\notin C_N\) and \(n\ge15\), then for each \(a\in\{0,1,2,3\}\),
\[
\left|r-a-\frac n2\right|\ge\frac{n-3}{4}\ge\frac n5.
\]
Since \(c_{n,r}=\sum_{a=0}^3(-1)^a\binom3a\binom n{r-a}\), with out-of-range binomial coefficients zero, Hoeffding's inequality for a symmetric binomial variable yields
\[
\sum_{r\notin C_N}|c_{n,r}|
\le 8\cdot2^n\mathbb P\!\left(\left|\operatorname{Bin}(n,1/2)-\frac n2\right|\ge\frac n5\right)
\le16\cdot2^n e^{-2n/25}.
\]
On every degree-\(N\) vertex, \(0\le h\le N/2\). Therefore
\[
\begin{aligned}
\sum_{r=0}^{N}\frac{|c_{n,r}|}{\mu_{r,N-r}}
&=\frac{N+1}{2^N}\sum_r|c_{n,r}|\exp\big(h(r,N-r)/100\big)\\
&\le\frac{n+4}{2^{n+3}}
\left[C2^n(n+1)^{-5/4}
+16\cdot 2^ne^{-2n/25}\,e^{(n+3)/200}\right]\\
&=O(n^{-1/4})+O\!\left(n\,e^{-3n/40}\right)\longrightarrow0.
\end{aligned}
\]
The exponent is \(-2/25+1/200=-3/40\), so the exponential term indeed vanishes.

**Failure of hypercyclicity on all stated spaces.** On every weighted \(\ell^p\), including \(p=1\), and weighted \(c_0\), the elementary inequality \(|f(r,N-r)|\le\|f\|_X/\mu_{r,N-r}\) applies. The preceding bound gives
\[
|\Lambda(B^nf)|\le\|f\|_X\sum_{r=0}^N\frac{|c_{n,r}|}{\mu_{r,N-r}}\longrightarrow0
\quad\text{for each }f\in X.
\]
For any candidate hypercyclic vector, its image under a nonzero continuous functional would have to be dense in \(\mathbb C\), but the scalar orbit \(\Lambda(B^nf)\) converges to zero and cannot be dense. This contradiction concludes the proof.

## Verification
The accompanying `verify.py` independently checks the finite exact binomial-convolution and beta-integral coefficient identities using integer arithmetic across a range of orders, checks representative central-column formulas, and reports normalized coefficient bounds. The infinite claims rely on the displayed analytic argument, the classical central-binomial estimate and Hoeffding's inequality, not on finite sampling.

## Relationship to prior work
Baranov, Lishanskii and Papathanasiou, *Hypercyclic shifts on lattice graphs* (first publicly posted 2023-12-21), Proposition 5.1, proved the single-vertex binomial condition necessary for hypercyclicity and explicitly asked if it is sufficient on the infinite quadrant. Their Theorem 2.3 handles exponential regimes \(\limsup\mu^{1/s}<2\) and \(\mu\gtrsim2^s\); neither applies to the present angularly varying critical weight. Chen, Wang and Zhou, *\(\mathcal F\)-Transitivity of Backward Shifts on Lattice Graphs* (first posted 2026-09-28), report a characterization for **radial weighted \(\ell^2\) spaces** on the infinite quadrant. The present nonradial weight is exponentially incomparable along each large antidiagonal and hence does not fall under a radial hypothesis. The substantive difference is failure of a collective cancellation condition despite every individual binomial row growing without bound.

## Limitations
The theorem disproves sufficiency of the single-vertex necessary condition, not any joint matrix/singular-value criterion. No general characterization of hypercyclicity for nonradial weights is claimed. The complete September 2026 manuscript was not available for full-text comparison; although its public abstract explicitly restricts its infinite-quadrant characterization to radial Hilbert-space weights, a specialized nonradial observation elsewhere in it cannot be conclusively excluded without independent inspection. The coefficient verifier is finite and is not a substitute for the proof.

## References
1. A. Baranov, A. Lishanskii and D. Papathanasiou, *Hypercyclic shifts on lattice graphs*, arXiv:2312.13934 (first public version 2023-12-21), Proposition 5.1 and Theorem 2.3. https://arxiv.org/abs/2312.13934 ; https://doi.org/10.1007/s13398-026-01868-8.
2. X. Chen, C. Wang and Z.-H. Zhou, *\(\mathcal F\)-Transitivity of Backward Shifts on Lattice Graphs*, arXiv:2609.34308 (first public version 2026-09-28). https://arxiv.org/abs/2609.34308.
3. Standard identities: Parseval for trigonometric polynomials, Euler's beta integral, and Hoeffding's concentration inequality for binomial random variables.
