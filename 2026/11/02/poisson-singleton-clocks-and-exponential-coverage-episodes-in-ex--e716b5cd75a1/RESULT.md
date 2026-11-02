# Poisson singleton clocks and exponential coverage episodes in expiring coupon collection

## Finding

Fix \(0<\alpha<1\). For each integer \(n\ge2\), let \((X_j)_{j\in\mathbb Z}\) be independent uniform labels in \(\{1,\ldots,n\}\), and, for all sufficiently large \(n\), put \(M_n=\lfloor\alpha n\log n\rfloor\ge n\). A window \(W_t=(X_{t-M_n+1},\ldots,X_t)\) is **complete** when it contains all \(n\) labels. Condition on the stationary entrance event \(E_0=\{W_{-1}\text{ incomplete},\ W_0\text{ complete}\}\), and let

\[
L_n=\min\{\ell\ge1:W_\ell\text{ is incomplete}\}.
\]

Thus \(L_n\) is the number of consecutive complete windows in the episode beginning at that entrance, including \(W_0\). The episode has the following **exponential lifetime law**:

\[
\boxed{\Pr(L_n>\lfloor xn^\alpha\rfloor\mid E_0)\longrightarrow e^{-x}\quad(x\ge0),\qquad
\mathbb E[L_n\mid E_0]\sim n^\alpha.}
\]

More precisely, put \(m=M_n-1\) and \(U=(X_{-M_n+1},\ldots,X_{-1})\). Given \(E_0\), a label is a singleton of \(U\) if it appears exactly once there. Form the point measure

\[
\Xi_n=\sum_{j=1}^{m}\mathbf1\{U_j\text{ occurs exactly once in }U\}\,\delta_{j/n^\alpha}.
\]

Then \(\Xi_n\) converges in distribution, in the vague topology of locally finite counting measures on \([0,\infty)\), to a homogeneous Poisson point process with **unit rate**. On every fixed rescaled time interval, the episode's first exit and the first singleton clock agree with probability tending to one. This process assertion explains the exponential law, not just its mean.

For every finite \(n\ge2\) and \(M\ge n\), the mean episode length has the exact identity

\[
\boxed{\mathbb E[L\mid E_0]=\frac{n\,S(M,n)}{(n-1)\,S(M-1,n-1)},}
\]

where \(S(m,k)\) is the Stirling number of the second kind. The finite identity itself follows from previously known stationary mass and entrance-flux formulas; the new assertion is the microscopic Poisson/episode-length limit.

## Assumptions and scope

The probability law is conditional on an entrance at time zero of the **stationary two-sided** sliding-window chain. It is not the distribution of the first completion time when a collection starts empty. All draws are independent and uniform. Expiration is deterministic after exactly \(M_n\) draws. The parameter \(\alpha\) is fixed strictly between zero and one, and \(n\to\infty\) through integers. No endpoint assertion at \(\alpha=0\) or \(\alpha=1\) is included. The Poisson point process is locally finite on bounded subsets of \([0,\infty)\), not on the entire rescaled interval as a finite total-mass process.

## Proof

**1. Exact entrance conditioning.** Write \(a=X_0\). The common middle word \(U\) has length \(m=M_n-1\). The event \(E_0\) holds exactly when \(U\) contains each of the \(N=n-1\) labels other than \(a\), contains no \(a\), and \(X_{-M_n}\ne a\). Hence, conditionally on \(E_0\) and \(a\), the word \(U\) is uniform among surjections from its \(m\) positions onto those \(N\) labels. The future draws \(X_1,X_2,\ldots\) remain independent uniforms. Relabeling lets us set \(a=0\) and the labels of \(U\) equal to \(1,\ldots,N\).

**2. Tilted occupancy law.** Choose the unique \(\tau>0\) solving

\[
\frac mN=\frac\tau{1-e^{-\tau}}.
\]

Let \(Z_1,\ldots,Z_N\) be independent zero-truncated Poisson random variables with

\[
\Pr(Z_i=r)=\frac{\tau^r}{r!(e^\tau-1)},\qquad r=1,2,\ldots.
\]

The color-count vector of the uniform onto word \(U\) has the same law as \((Z_i)_{i=1}^N\) conditioned on \(S_N=\sum_i Z_i=m\): on that hyperplane both have weights proportional to \(\prod_i (Z_i!)^{-1}\). Because \(m/N=\alpha\log n+O(\log n/n)\), the defining equation gives

\[
\tau=\alpha\log n+o(1),\qquad n^\alpha e^{-\tau}\longrightarrow1.
\]

**3. Uniform lattice-local estimate, with the needed justification.** The characteristic function of one zero-truncated Poisson variable is

\[
\phi_\tau(t)=\frac{e^{\tau e^{it}}-1}{e^\tau-1},
\]

and its variance is

\[
\sigma_\tau^2=\frac\tau{1-e^{-\tau}}-\frac{\tau^2e^{-\tau}}{(1-e^{-\tau})^2}\sim\tau.
\]

For \(\tau=\alpha\log n+o(1)\), the third absolute centered moment is \(O(\tau^{3/2})\), so the centered Fourier expansion on the \((N\tau)^{-1/2}\) scale has vanishing cumulative error. The span is one. On a small arc outside that scale, the characteristic function has Gaussian damping of order \(\exp(-c\tau t^2)\); on arcs bounded away from zero, the displayed characteristic function has exponential damping in \(\tau\). Splitting Fourier inversion into these arcs gives the triangular-array local central limit estimate and point-mass bound

\[
\Pr(S_N=m)\sim (2\pi N\sigma_\tau^2)^{-1/2},\qquad
\sup_j\Pr(S_{N-1}=j)\le \frac C{\sqrt{N\tau}}.
\]

The full Fourier argument is also developed for this precise truncated-Poisson family in Appendix A of Long (2026), and the stated range satisfies its hypotheses. In particular, uniformly for every integer \(r\ge1\), including values whose conditional probability vanishes,

\[
\Pr(Z_1=r\mid S_N=m)
=\Pr(Z_1=r)\frac{\Pr(S_{N-1}=m-r)}{\Pr(S_N=m)}
\le C'\Pr(Z_1=r).
\]

**4. Singleton counts concentrate even under the surjection condition.** Let \(K\) be the number of singleton colors of \(U\). Before conditioning on \(S_N=m\), the corresponding count is binomial with mean

\[
Np_1=N\frac{\tau}{e^\tau-1}\asymp n^{1-\alpha}\log n\longrightarrow\infty.
\]

The binomial Chernoff tail \(\exp(-c_\varepsilon Np_1)\) remains negligible after division by \(\Pr(S_N=m)\asymp(N\tau)^{-1/2}\). Thus the conditional ratio \(K/(Np_1)\to1\) in probability. The same bound, together with \(0\le K\le N\), gives convergence of the corresponding expectations. Since \(Np_1/m=e^{-\tau}\) exactly,

\[
\frac{n^\alpha K}{m}\ \longrightarrow\ 1
\quad\text{in probability},\qquad
\mathbb E\frac{n^\alpha K}{m}\ \longrightarrow\ 1.
\]

**5. Singleton-position point process.** Conditional on \(K\), the singleton positions form a uniformly chosen \(K\)-element subset of the \(m\) positions, by exchangeability of the letters. For pairwise disjoint bounded intervals \(I_1,\ldots,I_d\subset[0,\infty)\), let \(h_j\) be the number of integers \(1\le k\le m\) with \(k/n^\alpha\in I_j\). For fixed nonnegative integers \(r_1,\ldots,r_d\), put \(r=\sum_jr_j\). Their conditional joint falling-factorial moment is

\[
\mathbb E\!\left[\prod_{j=1}^d (\Xi_n(I_j))_{r_j}\mid K\right]
=\frac{(K)_r}{(m)_r}\prod_{j=1}^d(h_j)_{r_j}.
\]

Here \((z)_r=z(z-1)\cdots(z-r+1)\). Because \(h_j/n^\alpha\to|I_j|\), \(K\to\infty\), and \(n^\alpha K/m\to1\), these moments tend to \(\prod_j|I_j|^{r_j}\). The strong concentration from step 4 controls exceptional values of \(K\), so unconditional moments have the same limit. These are the joint factorial moments of independent Poisson variables of means \(|I_j|\). Tightness on bounded intervals follows from their first moments. This proves \(\Xi_n\Rightarrow\operatorname{PPP}(1)\).

**6. From singleton clocks to the first loss.** Fix \(x\ge0\), put \(t=\lfloor xn^\alpha\rfloor\), and define \(R_t\) as the number of labels of \(U\) whose *every* occurrence lies in its first \(t\) positions. Let \(J_t\) count those labels among \(R_t\) that occur at least twice. For one color of multiplicity \(r\), the chance that all its positions belong to the first \(t\), conditional on the multiplicities, is \((t)_r/(m)_r\le(t/m)^r\). The point-mass ratio from step 3 yields

\[
\begin{aligned}
\mathbb E J_t
&\le C N\sum_{r\ge2}\frac{\tau^r}{r!(e^\tau-1)}\left(\frac tm\right)^r\\
&=\frac{CN}{e^\tau-1}\left(e^{\tau t/m}-1-\frac{\tau t}{m}\right)
=O(n^{\alpha-1})=o(1).
\end{aligned}
\]

The expected number of singleton positions in the first \(t\) is \(t\mathbb E[K]/m=O(1)\), so \(\mathbb E R_t=O(1)\). If \(R_t=0\), no old label can disappear from any of the first \(t\) subsequent windows; the newly appended label \(a\) is still present because \(t=o(M_n)\). Conversely, if \(R_t>0\) and the window remains complete through step \(t\), some color counted by \(R_t\) must have been redrawn in the first \(t\) future steps. Conditional on \(U\), that probability is at most \(tR_t/n\). Therefore

\[
\Pr(R_t=0)\le\Pr(L_n>t\mid E_0)
\le\Pr(R_t=0)+\frac tn\mathbb E R_t,
\]

and the difference between \(\Pr(R_t=0)\) and the probability of no singleton position in the first \(t\) is at most \(\mathbb E J_t=o(1)\). By step 5, the latter probability tends to \(e^{-x}\). The same estimates with a fixed upper rescaled horizon show that the first exit and first singleton clock agree with probability \(1-o(1)\) up to that horizon. This proves the lifetime limit.

**7. Exact mean and its limit.** Let \(\pi_{n,M}\) be the stationary mass of complete windows and \(\mu_{n,M}\) the stationary probability of an incomplete-to-complete transition. Their known exact counts are

\[
\pi_{n,M}=\frac{n!S(M,n)}{n^M},\qquad
\mu_{n,M}=\frac{(n-1)(n-1)!S(M-1,n-1)}{n^M}.
\]

Every consecutive complete episode begins with exactly one entrance, and the finite window chain is stationary and ergodic. Counting its complete windows per entrance gives \(\mathbb E[L\mid E_0]=\pi_{n,M}/\mu_{n,M}\), which is the displayed finite identity. Equivalently, the stationary exit flux divided by \(\pi_{n,M}\) is

\[
\frac{\mu_{n,M}}{\pi_{n,M}}
=\left(1-\frac1n\right)\mathbb E\!\left[\frac{K_{n,M}}M\,\Bigm|\, W_0\text{ complete}\right],
\]

where \(K_{n,M}\) counts singleton colors in the stationary complete word. The same tilted-occupancy argument as steps 2–4, now with \(N=n\), \(m=M\), shows that the expectation on the right is asymptotic to \(n^{-\alpha}\). Thus \(\mathbb E[L_n\mid E_0]\sim n^\alpha\), without inferring mean convergence from weak convergence alone. \(\square\)

## Verification

The independent standard-library script `verify.py` enumerates all relevant short surjections and forward strings for \(2\le n\le4\), \(n\le M\le n+2\), checking the exact entrance Palm law, singleton-count formula, uniform singleton positions, stationary entrance-to-occupancy ratio, and finite-time survival sandwiches. Its saved output records **403 exact assertions passed**. These computations inspect the exact finite combinatorics; the limiting statements use steps 2–7, not experimental extrapolation. To reproduce, run `python3 verify.py` in a directory containing that file; the script requires no external packages or datasets.

## Relationship to prior work

Long (2026, arXiv:2604.26298v1) proves the stationary entrance flux, rare-entry waiting-time law, and truncated-Poisson conditioning bounds. Those results concern the **waiting time until a complete window appears**; no distribution for the consecutive complete-window episode following an entrance is stated in the inspected manuscript. The exact finite mean above is algebraically implied by Long's stationary mass and flux and is explicitly credited as such. The genuinely additional step is the conditional singleton-position point-process limit and its transfer to the whole forward episode length.

Joriki's 2012 Math StackExchange answer anticipates the relevant \(n^\alpha\) scale with a heuristic model for the loss of unique coupons. This is significant prior intuition, not a proved Poisson process or episode-length limit. Barbour, Braunsteins and Ross (2019) study occupancy local limits; their inspected results and applications do not furnish the conditioned sliding-window episode theorem. The argument therefore claims a rigorous local process law, not priority for the heuristic timescale or any general local central limit principle.

## Limitations

The conclusion is for the stationary entrance Palm law and fixed \(0<\alpha<1\) only. Nonuniform coupon frequencies, random expiration, windows at critical or supercritical length, and joint limits of separated complete episodes are not treated. The Poisson limit is a weak local limit; a finite \(n\) episode is not exactly geometric. The finite enumeration does not establish convergence as \(n\to\infty\). A broader earlier theorem for clumps of conditioned occupancy words might subsume the result even if it uses different language; independent historical-priority and mathematical assessment remain to be conducted.

## References

1. Christopher D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1, first posted April 29, 2026. https://arxiv.org/abs/2604.26298
2. Joriki, answer to *Expiring coupon collector's problem*, Mathematics Stack Exchange, October 11, 2012. https://math.stackexchange.com/questions/188889/expiring-coupon-collectors-problem
3. A. D. Barbour, Peter Braunsteins and Nathan Ross, *Local limit theorems for occupancy models*, arXiv:1908.00251v1, first posted August 1, 2019. https://arxiv.org/abs/1908.00251
4. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, Electronic Journal of Probability 14 (2009), 365–384. https://doi.org/10.1214/EJP.v14-608
