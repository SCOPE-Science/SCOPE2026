# Four-voter trimodality thresholds and exact rare-shock profiles in a noisy voter chain

## Finding

A model in which occasional population-wide shocks return a noisy voter population to a designated opinion count can exhibit three simultaneous stationary modes: the two unanimity states and the shock destination. The phenomenon occurs with as few as four voters, and four is sharp. The smallest model has an exact, nonempty open two-parameter interval of trimodality. For every fixed larger population and every nonboundary shock target separated by at least one count from each boundary, trimodality reappears when spontaneous noise is sufficiently smaller than the rare shock probability. The first-order stationary distribution on intermediate counts is an explicit absorbing-walk Green kernel.

For four voters and a shock target of two supporters, define
\[
R_+(\eta)=\frac{3-15\eta}{19-15\eta},\qquad
R_-(\eta)=\frac{5\eta^2-12\eta-1+\sqrt{41\eta^2+38\eta+1}}{14-23\eta+5\eta^2}.
\]
The stationary distribution has precisely three **strict local maxima**, located at counts \(0,2,4\), if and only if
\[
0<\eta<\frac15\quad\text{and}\quad R_-(\eta)<r<R_+(\eta).
\]
For each \(0<\eta<1/5\), this interval is nonempty. The boundary cases have a tie between neighboring masses and do not satisfy the strict-modal definition.

More generally, fix an integer \(N\ge4\) and \(2\le k\le N-2\). As \(r\downarrow0\) with \(\eta>0\) and \(\eta/r\to0\), the stationary probabilities satisfy
\[
\pi_j=rG_{kj}+o(r),\qquad
G_{kj}=\begin{cases}
\dfrac{N(N-k)}{N-j},&1\le j\le k,\\
\dfrac{Nk}{j},&k\le j\le N-1,
\end{cases}
\]
and \(\pi_0\to1-k/N\), \(\pi_N\to k/N\). For sufficiently small \(r\) along this regime, the strict maxima occur exactly at \(0,k,N\). The \(o(r)\) statement is at fixed \(N,k\); it is not asserted uniformly as \(N\to\infty\).

## Assumptions and scope

The population has \(N\ge2\) agents, each holding one of two opinions, and its count of supporters is \(j\in\{0,\ldots,N\}\). Each ordinary discrete-time update follows the **with-replacement** mean-field noisy-voter transition probabilities
\[
u_j=\frac{N-j}{N}\left[\eta+(1-\eta)\frac jN\right],\qquad
d_j=\frac jN\left[\eta+(1-\eta)\frac{N-j}{N}\right].
\]
Thus a baseline step increases the count with probability \(u_j\), decreases it with probability \(d_j\), and otherwise leaves it fixed. This is the precise normalization for the noisy model in the cited motivating work; it is important not to substitute the distinct no-self-neighbor normalization often used for the classical voter model.

Independently on each step, with probability \(r\), the entire count is set to a fixed target \(k\); with complementary probability \(1-r\), the ordinary step occurs. Parameters obey \(0<\eta<1\), \(0<r<1\); \(k\) is an integer in \(\{0,\ldots,N\}\). With row-stochastic matrices, the transition matrix is \(Q=(1-r)P_\eta+rR_k\), where all rows of \(R_k\) place unit mass at \(k\). It has a unique strictly positive stationary probability row \(\pi\), because the baseline chain is irreducible for positive \(\eta\) and there is positive ordinary-step probability.

A boundary count is a strict local maximum when its mass exceeds the mass at its unique adjacent count; an interior count is a strict local maximum when its mass exceeds both neighboring masses. Trimodality here means exactly three strict local maxima, at the two boundaries and the shock target; it does not refer to smoothing of a discrete probability histogram. The exact four-voter classification additionally specializes to the central target \(k=2\).

## Proof

### Exact four-voter classification

Reflection about count two leaves \(Q\) invariant for \(N=4,k=2\). Uniqueness therefore forces \(\pi=(a,b,c,b,a)\). Let \(A=a/b\) and \(B=c/b\). The stationary balance equation at count zero, using \(d_1=(3+\eta)/16\), gives
\[
A=\frac{(1-r)(3+\eta)}{16[r+(1-r)\eta]}.
\]
The balance equation at count one, where the relevant baseline transition probability from count two is \((1+\eta)/4\), gives
\[
B=\frac4{1+\eta}\left[\frac r{1-r}+\frac{3+5\eta}{8}-\eta A\right].
\]
Normalization gives \(\pi=(A,1,B,1,A)/(2A+2+B)\). Substituting these expressions into the remaining count-two balance equation verifies that this is the exact stationary solution for every allowed pair \((\eta,r)\). In particular no approximation or enumeration is used for these formulas.

The endpoints are strict maxima precisely when \(A>1\), and the midpoint is a strict maximum precisely when \(B>1\). Direct simplification yields
\[
A-1=\frac{(3-15\eta)(1-r)-16r}{16[\eta(1-r)+r]},
\]
so \(A>1\) is equivalent to \(\eta<1/5\) and \(r<R_+(\eta)\). Likewise
\[
B-1=\frac{H_\eta(r)}{4(1+\eta)(1-r)[\eta(1-r)+r]},
\]
where
\[
H_\eta(r)=(14-23\eta+5\eta^2)r^2+(2+24\eta-10\eta^2)r+\eta(5\eta-1).
\]
For \(0<\eta<1/5\), the quadratic coefficient and linear coefficient of \(H_\eta\) are positive, while its constant coefficient is negative. Thus \(H_\eta(r)\) has exactly one positive root, and \(B>1\) holds exactly when \(r>R_-(\eta)\). The quadratic formula gives the displayed expression for \(R_-\); its discriminant simplifies to \(4(41\eta^2+38\eta+1)\). Finally, at \(r=R_+(\eta)\),
\[
B-1=\frac{5(1-5\eta)}{4(1+\eta)}>0.
\]
Hence \(R_-(\eta)<R_+(\eta)\) throughout the interval \(0<\eta<1/5\). Outside these inequalities one of the two necessary strict comparisons fails. This proves necessity, sufficiency, and nonemptiness of the exact phase window.

For the rational parameter choice \(\eta=1/10\), \(r=1/25\), the stationary distribution is
\[
\pi=\frac1{1220}(279,204,254,204,279).
\]
The three strict modes are visible by the exact comparisons \(279>204\) and \(254>204\).

### Rare-shock profile at arbitrary fixed population size

Write \(T=\{1,\ldots,N-1\}\), \(B=\{0,N\}\). With \(\eta=0\), the ordinary chain is a symmetric absorbing birth-death walk whose probability to move each way from count \(j\in T\) is \(p_j=j(N-j)/N^2\). The embedded walk observed only at movement times is simple symmetric random walk killed on \(B\). The expected number of its visits to count \(j\) starting from count \(k\) is
\[
V_{kj}=\frac{2\min(k,j)[N-\max(k,j)]}{N}.
\]
One elementary derivation solves the discrete second-difference equation for the expected number of visits to \(j\), with zero boundary values and a unit source at \(j\); the solution is piecewise affine in the starting count, continuous at \(j\) with the required jump of its first difference. Each embedded visit has mean holding time \(1/(2p_j)\) in the full discrete-time chain. Therefore the ordinary-chain Green kernel on \(T\) is
\[
G_{kj}=\frac{V_{kj}}{2p_j}
=\frac{N\min(k,j)[N-\max(k,j)]}{j(N-j)},
\]
which reduces to the displayed two-branch formula. Equivalently, \(G\) is \((I-P_{0,TT})^{-1}\); this inverse exists because the ordinary \(\eta=0\) chain eventually hits one of the absorbing boundaries with probability one.

Decompose the positive-noise stationary row into \(\pi_T,\pi_B\). Its interior balance equation is exactly
\[
\pi_T=\left[re_k+(1-r)\pi_B P_{\eta,BT}\right]
\left[I-(1-r)P_{\eta,TT}\right]^{-1}.
\]
The boundary-to-interior block is of order \(O_N(\eta)\). The inverse is uniformly bounded and converges to \((I-P_{0,TT})^{-1}\) as \((r,\eta)\to(0,0)\), by finite-dimensional invertibility and continuity. Consequently
\[
\pi_j=rG_{kj}+O_N(r^2+\eta),\qquad 1\le j\le N-1.
\]
In particular, if \(\eta=o(r)\), this is \(rG_{kj}+o(r)\) and the total interior mass tends to zero.

The mean count \(m=\sum_jj\pi_j\) can be computed without approximations. The ordinary-step conditional mean change is \(u_j-d_j=\eta(1-2j/N)\). At stationarity, therefore,
\[
m=\frac{(1-r)\eta+rk}{r+2(1-r)\eta/N}\longrightarrow k
\]
when \(\eta=o(r)\). Since the interior mass vanishes, \(m=N\pi_N+o(1)\), giving \(\pi_N\to k/N\) and \(\pi_0\to1-k/N\).

For \(2\le k\le N-2\), the Green kernel is strictly increasing in \(j\) for \(1\le j\le k\) and strictly decreasing for \(k\le j\le N-1\). These finitely many strict inequalities persist under the \(o(r)\) perturbation for sufficiently small \(r\), while the two strictly positive limiting boundary masses dominate their neighboring interior masses. It follows that the sole strict local maxima are \(0,k,N\). Finally, any probability sequence with three strict local maxima requires at least five successive entries (there must be a lower intervening entry between each pair); because a population with \(N\) voters has \(N+1\) entries, \(N\ge4\) is necessary. The four-voter example above proves sharpness.

## Verification

The embedded standalone program `verify.py` reconstructs every row of the finite transition matrix over exact rational numbers, solves the stationary linear system directly, and verifies stationarity. It checks the four-voter ratio identities and modal inequalities on 32,580 rational parameter pairs; checks the displayed five-point example exactly; verifies each Green-matrix inverse equation for \(4\le N\le11\); and tests the small-noise/rare-shock three-mode pattern at finite rational parameters in those population sizes. The program was executed successfully from the embedded package. The all-parameter phase boundaries and the all-size asymptotics follow from the analytic proof, not from the finite computations.

## Relationship to prior work

Argany Herrera, Alvarez-Zuzek and Artime introduce system-wide exogenous shocks, specify the noisy-voter transition rates and present numerical stationary-distribution phase diagrams, including trimodal states at a large population size (arXiv:2609.39858, section on noisy-voter shocks). Their general transition-matrix framework allows finite stationary distributions to be computed. The present result goes further in a narrower natural regime: it identifies the **smallest feasible population**, gives necessary-and-sufficient **closed-form strict-mode inequalities** in both parameters, and proves a **fixed-size all-population rare-shock Green-kernel asymptotic**.

Caligiuri and Galla (arXiv:2305.19096) study multiple stationary peaks under switching noise or moving influencer populations, which are not the one-step collective projection shocks considered here. Llabrés, San Miguel and Toral (arXiv:2301.09563) study preference-driven partisan noisy voters, rather than a global reset of the entire count. Grange (arXiv:2207.08590) studies stochastic resetting of individual voters, not the same global reset mechanism. General finite absorbing-chain Green kernels and quadratic inequalities are classical tools; neither is presented as a new technique. The claim is the exact classification and its associated modal interpretation for the specified model, not generic novelty of stochastic resetting or noisy voter processes.

## Limitations

Strict peaks are peaks of the count probability mass function, not peaks of a smoothed density. The precise update normalization matters. The phase window applies to the symmetric target \(k=2\) at \(N=4\); the larger-\(N\) theorem establishes a limiting existence regime, not an exact arbitrary-size two-parameter phase diagram. The small-parameter estimates are for fixed \(N,k\), not a joint thermodynamic limit. No conclusion is drawn for noncomplete social networks, correlated shocks, shock destinations drawn from a distribution, or time-dependent noise parameters. The priority comparison is limited to inspected literature and can be refined by independent specialist review.

## References

1. G. Argany Herrera, L. G. Alvarez-Zuzek and O. Artime, *Opinion dynamics under large-scale exogenous events* (2026), arXiv:2609.39858, https://arxiv.org/abs/2609.39858. First public source: 2026-09-30. Relevant material: noisy-voter transition rules (27)–(29), section on stationary phases, and discussion.
2. A. Caligiuri and T. Galla, *Noisy voter models in switching environments*, Physical Review E **108**, 044301 (2023), arXiv:2305.19096, https://arxiv.org/abs/2305.19096. Relevant material: sections II, IV and V.
3. J. Llabrés, M. San Miguel and R. Toral, *Partisan Voter Model: Stochastic description and noise-induced transitions* (2023), arXiv:2301.09563, https://arxiv.org/abs/2301.09563. Relevant material: noisy-partisan model and phase-transition discussion.
4. P. Grange, *Voter model under stochastic resetting* (2022), arXiv:2207.08590, https://arxiv.org/abs/2207.08590. Used for the distinction between local and global resetting; complete paper not materially inspected.
