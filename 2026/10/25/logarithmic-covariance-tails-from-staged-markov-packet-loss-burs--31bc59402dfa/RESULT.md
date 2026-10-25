# Logarithmic covariance tails from staged Markov packet-loss bursts

## Finding
For every integer \(m\ge2\), progressive loss-channel stages produce a precise hierarchy of logarithmic corrections to the heavy tail of scalar Kalman **peak prediction covariance**. With the definitions below, write \(\alpha=-\log p/(2\log |a|)\). Then
\[
 \Pr(M>x)=\Theta\!\bigl(x^{-\alpha}(\log x)^{m-1}\bigr),\qquad x\to\infty.
\]
The moment criterion is exact for every \(r>0\):
\[
 \mathbb E[M^r]<\infty\quad\Longleftrightarrow\quad p|a|^{2r}<1.
\]
At equality the moment diverges. If \(q_\varepsilon=\inf\{x:\Pr(M>x)\le\varepsilon\}\), its extreme-quantile order is
\[
 q_\varepsilon=\Theta\!\left(\varepsilon^{-1/\alpha}(\log(1/\varepsilon))^{(m-1)/\alpha}\right),\quad \varepsilon\downarrow0.
\]
Thus the purely geometric, two-state channel and the staged channel may have the same logarithmic decay exponent but different tail envelopes and high-risk quantiles.

## Assumptions and scope
Let \(x_{t+1}=a x_t+w_t\) and, on successful reception, \(y_t=h x_t+v_t\), where \(|a|>1\), \(h\ne0\), and the independent centered Gaussian process and measurement noises have variances \(Q>0\) and \(R>0\). Packet reception indicators and noises are independent. A receiver knows whether each observation was lost.

The channel has one successful-reception state \(S\) and \(m\ge2\) loss states \(L_1,\ldots,L_m\). From \(S\), it enters \(L_1\) with probability \(\eta\in(0,1)\) and otherwise remains in \(S\). From \(L_i\) it remains at \(L_i\) with probability \(p\), advances to \(L_{i+1}\) with probability \(c\) when \(i<m\), and otherwise returns to \(S\). Here \(0<p<1\), \(0<c<1-p\); from \(L_m\), return-to-\(S\) probability is \(1-p\). Therefore the substochastic transition matrix within loss states is \(T=pI_m+cJ_m\), with \(J_m\) the nilpotent first-superdiagonal shift. Every loss run starts at \(L_1\) and ends almost surely.

Let \(N\ge1\) count the number of lost measurements in a generic nonempty run, and let \(M\) be the Kalman one-step prediction error variance just before processing the first successfully recovered measurement. All probability assertions are conditional on such a loss run; the probability \(\eta\) of initiating one does not alter their conditional law. No stationarity assumption on the covariance immediately before the preceding received measurement is needed.

## Proof
Put \(B=a^2>1\). The scalar covariance update after a received observation is
\[
 g(P)=Q+\frac{BRP}{h^2P+R},\qquad Q\le g(P)\le Q+\frac{BR}{h^2},\quad P\ge0.
\]
During a lost observation the update is \(f(P)=BP+Q\). Hence, if \(N\) consecutive packets are lost after a reception, the predictor at the next reception is \(M=f^{N}(g(P))\), where \(P\ge0\) is the predictor at the previous reception. The exact iteration gives
\[
 M=B^{N}g(P)+Q\frac{B^{N}-1}{B-1}.
\]
Consequently, for every possible preceding predictor and every integer \(N\ge1\),
\[
 QB^N\le M\le \left(Q+\frac{BR}{h^2}+\frac{Q}{B-1}\right)B^N.
\tag{1}
\]
Write the fixed upper coefficient as \(C_+\); both constants in (1) are positive, deterministic, and independent of the preceding history.

Starting at \(L_1\), survival in loss states for \(n-1\) transitions means \(N\ge n\). For every integer \(n\ge1\), the binomial theorem and \(J_m^m=0\) yield the **exact finite sum**
\[
 \Pr(N\ge n)=e_1^{\mathsf T}T^{n-1}{\bf1}
 =\sum_{j=0}^{\min(m-1,n-1)}\binom{n-1}{j}p^{n-1-j}c^j.
\tag{2}
\]
For fixed \(m\ge2\) and \(p,c>0\), the top term \(j=m-1\) dominates all lower-degree terms, whence
\[
 \Pr(N\ge n)\sim\frac{c^{m-1}}{(m-1)!p^m}\,n^{m-1}p^n
 \quad(n\to\infty).
\tag{3}
\]
In particular, there are positive finite constants bounding this probability above and below by \(n^{m-1}p^n\) for every sufficiently large integer \(n\).

For real \(x>0\), the sandwich (1) implies
\[
 \Pr\!\left(B^N>\frac{x}{Q}\right)
 \le \Pr(M>x)
 \le \Pr\!\left(B^N>\frac{x}{C_+}\right).
\]
Both flanking integer thresholds equal \(\log_B x+O(1)\). Since replacing \(n\) by \(n+O(1)\) changes \(n^{m-1}p^n\) by at most constant factors, (3) proves the stated two-sided tail order with \(\alpha=-\log p/\log B\). The integer nature of \(N\) prevents an unqualified asymptotic-constant assertion.

For \(r>0\), (1) also yields \(\mathbb E[M^r]<\infty\) exactly when \(\mathbb E[B^{rN}]<\infty\). The tail-sum identity for \(s=B^r>1\) is
\[
 \mathbb E[s^N]=1+(s-1)\sum_{n\ge0}s^n\Pr(N>n).
\]
Equation (3), together with the ratio test and the nonvanishing polynomial factor at the boundary, makes this series finite exactly when \(sp<1\). The moment criterion follows, including divergence for \(sp=1\). Finally, monotonic inversion of the two-sided tail bounds gives the displayed high-quantile envelope. This is one result and its equivalent consequences, not independent unrelated assertions.

## Verification
Identity (2) may be checked without probabilistic simulation: multiply the row vector \(e_1^{\mathsf T}\) successively by \(T\) and sum all \(m\) components. For the rational example \(m=3\), \(p=1/2\), \(c=1/4\), the exact values of \(\Pr(N\ge n)\) for \(n=1,2,3,5,8,12\) are respectively \(1\), \(3/4\), \(9/16\), \(9/32\), \(39/512\), and \(81/8192\). Direct rational recurrence agrees with the binomial sum at each index. This finite check corroborates equation (2), while the proof for all \(m,n\) is algebraic and does not rely on enumeration. For this example with \(|a|=2\), the tail envelope is \(\Theta(x^{-1/2}(\log x)^2)\), and positive moments exist precisely below order \(1/2\).

## Relationship to prior work
Huang and Dey's 2006 conference paper derives upper and lower power-tail bounds for peak covariance under a **two-state** Gilbert–Elliott channel (Section IV.C). Their 2007 article develops the two-state stability theory. Mo and Sinopoli's 2012 paper derives the logarithmic decay exponent for Gilbert–Elliott channels; its Remark 5 observes that its methods can be adapted to other packet-loss processes, but its stated channel-specific results do not provide the staged-loss \((\log x)^{m-1}\) envelope. The finite-state Markov process in Wu, Shi, Xie and Johansson (2015) instead governs **bounded** run lengths, so its stability theorem does not imply any unbounded-tail asymptotic. The present model addresses progressive loss stages with a nonprimitive within-loss transition matrix. Its repeated Perron eigenvalue leaves the power exponent unchanged while introducing a genuine polynomial factor in burst survival and hence a logarithmic factor in covariance risk.

## Limitations
The result concerns a scalar, one-step-observable Kalman predictor at the ends of nonempty loss episodes, not a vector state, the distribution of the physical estimation error, or arbitrary observation times. The positive parameters \(p,c\) and strict inequality \(p+c<1\) are essential to the specified finite-state construction. The statement is a two-sided envelope, not a regularly varying limit with an asymptotic constant; lattice oscillations may persist. The quantile relation is likewise an order statement. No independent external validation has been performed. A generic phase-type distribution theorem combined with scalar Riccati comparison may supply an alternate route; the claim does not assert that either ingredient is new.

## References
1. M. Huang and S. Dey, *Kalman Filtering with Markovian Packet Losses and Stability Criteria*, Proceedings of the 45th IEEE Conference on Decision and Control, 2006, pp. 5621–5626. DOI: 10.1109/CDC.2006.376710. Full text: https://mural.maynoothuniversity.ie/id/eprint/14463/1/kalman%20filtering.pdf.
2. M. Huang and S. Dey, *Stability of Kalman Filtering with Markovian Packet Losses*, Automatica 43 (2007), 598–607. DOI: 10.1016/j.automatica.2006.10.023. Full text: https://mural.maynoothuniversity.ie/id/eprint/14418/1/stability.pdf.
3. Y. Mo and B. Sinopoli, *Kalman Filtering with Intermittent Observations: Tail Distribution and Critical Value*, IEEE Transactions on Automatic Control 57 (2012), 677–689. DOI: 10.1109/TAC.2011.2166309. Full text: https://yilinmo.github.io/public/papers/journal2009kalman.pdf.
4. J. Wu, L. Shi, L. Xie and K. H. Johansson, *An Improved Stability Condition for Kalman Filtering with Bounded Markovian Packet Losses*, arXiv:1501.05469v1, January 22, 2015. https://arxiv.org/pdf/1501.05469.
