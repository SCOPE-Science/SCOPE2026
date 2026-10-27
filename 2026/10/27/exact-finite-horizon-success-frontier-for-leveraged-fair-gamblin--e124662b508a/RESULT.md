# Exact finite-horizon success frontier for leveraged fair gambling

## Finding

For every integer \(N\ge1\), leverage \(L\ge1\), initial fortune \(0<x<M\), and target \(M\), the largest probability of reaching \(M\) before insolvency in **at most** \(N\) fair bets is
\[
\boxed{P_N(x;L,M)=\left(\frac{L}{L+(M/x)^{1/N}-1}\right)^N.}
\]
This optimum permits arbitrary, history-dependent one-step distributions subject to the constraints below, not only two-outcome or fixed-multiplier bets.

For \(L>1\), every optimal policy, conditional on any positive fortune \(z<M\) reached with \(k\ge1\) bets remaining, uses the unique two-point next-fortune distribution
\[
Y=\begin{cases}
 z(M/z)^{1/k},&\text{with probability }\displaystyle\frac{L}{L+(M/z)^{1/k}-1},\\[2pt]
 -(L-1)z,&\text{otherwise.}
\end{cases}
\]
Thus an optimal surviving trajectory makes equal proportional increases, and its first loss is immediately terminal. Uniqueness concerns conditional distributions at positive fortunes that occur with positive probability; it is not a claim about unreachable histories. At \(L=1\), the optimal value is \(x/M\) for every \(N\), but the optimal policy need not be unique.

For fixed \(L>1\) and \(R=M/x>1\), \(P_N\) increases strictly with \(N\) and approaches the infinite-horizon upper bound. Its *sharp first-order budget deficit* is
\[
R^{-1/L}-P_N(x;L,M)
=R^{-1/L}\frac{(L-1)(\log R)^2}{2L^2N}
+O_{L,R}(N^{-2}).
\]

## Assumptions and scope

At each nonterminal time with current fortune \(z\in(0,M)\), the gambler selects any probability distribution of the next fortune \(Y\), possibly depending on the entire history, with
\[
\mathbb E[Y\mid\text{history}]=z,\qquad -(L-1)z\le Y\le M\quad\text{almost surely}.
\]
The game terminates upon \(Y\le0\) (insolvency) or \(Y=M\) (success); for the horizon-constrained problem, failure also occurs if the target has not been attained after \(N\) bets. The maximizing policy itself always terminates within \(N\) steps; hence adding the standard requirement of eventual termination does not alter the optimum. All real \(L\ge1\) and \(0<x<M\) are covered, as well as every integer \(N\ge1\).

## Proof

**Bellman values and base case.** Write \(V_k(z)\) for the best success probability at positive fortune \(z<M\) with at most \(k\) bets left, and put \(V_k(y)=0\) for \(y\le0\), \(V_k(y)=1\) for \(y\ge M\), and \(V_0(y)=\mathbf1_{\{y\ge M\}}\). For \(k=1\), set \(a=(L-1)z\). Since \(Y+a\ge0\),
\[
M\,\mathbb P(Y=M)+a\,\mathbb P(Y=M)
\le\mathbb E(Y+a)=Lz.
\]
Therefore \(V_1(z)=Lz/(M+a)=L/(L+M/z-1)\), attained by the outcomes \(M\) and \(-a\). For \(L=1\), the same upper bound follows, and every horizon has value \(z/M\): nonnegative fair wealth gives \(M\mathbb P(\text{success by }k)\le\mathbb E[Y_{k\wedge\tau}]=z\), while the one-step \(0\)-or-\(M\) lottery attains equality.

**Induction for \(L>1\).** Suppose, for some \(k\ge2\), the formula is valid for \(k-1\) bets:
\[
V_{k-1}(u)=\left(\frac{L}{L+(M/u)^{1/(k-1)}-1}\right)^{k-1},\qquad0<u<M.
\]
For a current \(z\in(0,M)\) define \(a=(L-1)z\) and
\[
c=\max_{0<u\le M}\frac{V_{k-1}(u)}{u+a}.
\]
We have \(V_{k-1}(y)\le c(y+a)\) pointwise for every \(y\in[-a,M]\), including \(y\le0\). Therefore every admissible next-fortune distribution satisfies the **affine dual bound**
\[
\mathbb E[V_{k-1}(Y)]\le c\mathbb E[Y+a]=Lz c.
\]
Writing \(q=(M/u)^{1/(k-1)}\), direct differentiation gives
\[
\frac{d}{du}\log\frac{V_{k-1}(u)}{u+a}
=\frac{(L-1)(zq-u)}{u(L+q-1)(u+a)}.
\]
For \(L>1\), the derivative changes from positive to negative exactly at \(u_*=z(M/z)^{1/k}\). Thus \(c=V_{k-1}(u_*)/(u_*+a)\) and
\[
Lz c=\left(\frac{L}{L+(M/z)^{1/k}-1}\right)^k.
\]
The distribution supported on \(u_*\) and \(-a\), with upper-branch probability \(Lz/(u_*+a)\), meets the mean constraint and attains the affine bound. On the upper branch its next \(k-1\) steps follow the induction optimizer. Hence this is the exact Bellman value. The pointwise affine inequality is strict except at \(-a\) and \(u_*\) (when \(L>1\)), so equality forces exactly the indicated two-point distribution. Induction proves both value and conditional-law uniqueness at visited states.

**Strict budget monotonicity and sharp gap.** Let \(h=\log(M/x)>0\) and
\[
g(t)=\log\left(1+\frac{e^t-1}{L}\right),\qquad
P_N=\exp[-N g(h/N)].
\]
For \(L>1\), \(g(0)=0\) and \(g''(t)=(L-1)e^t/(L+e^t-1)^2>0\). Thus \(N g(h/N)\) strictly decreases as \(N\) increases. Taylor's formula at zero yields
\[
-Ng(h/N)=-h/L-\frac{(L-1)h^2}{2L^2N}+O_{L,h}(N^{-2}),
\]
which proves both the infinite-horizon limit and the stated sharp deficit.

## Verification

The accompanying `check_finite_leverage.py` uses exact rational special cases, symbolic differentiation and Taylor coefficients, and 15,375 sampled Bellman-affine inequalities across prescribed leverage levels, target ratios, horizons and possible next fortunes. Run it with Python 3 and SymPy via `python check_finite_leverage.py`. Its finite checks independently corroborate algebraic identities and inequalities; the preceding induction and convexity arguments establish the statements for **all** parameters and horizons.

As an exact example, \(L=2\), \(x=1\), \(M=16\), \(N=4\) gives \(P_4=(2/3)^4=16/81\), whereas the unlimited-budget supremum is \(1/4\). The first bet wins by moving from fortune \(1\) to \(2\) with probability \(2/3\), or loses by moving to fortune \(-1\).

## Relationship to prior work

Kuszmaul, *With Leverage, the Gambler is Not the One Who Gets Ruined* (arXiv:2610.19239v1, first posted 13 October 2026) establishes the leveraged fair-lottery model, derives the success probability of a fixed-multiplier strategy (Lemma 2.1), and proves an **unbounded-horizon** upper bound \(R^{-1/L}\) (Proposition 2.2). Substituting the multiplier \(R^{1/N}\) into Lemma 2.1 already gives the *achievability* expression above. The new contribution here is the **matching finite-horizon upper bound over arbitrary adaptive lotteries**, its strict optimal-law characterization for \(L>1\), and the sharp \(1/N\) budget penalty. These are not asserted as results of Kuszmaul's paper.

The finite-horizon bold-play theorems of Yao (2007) and Yao–Chen (2008) concern primitive casinos with fixed win probabilities and stakes **limited to current nonnegative fortune**. Their Bellman feasible sets differ from the present fair lotteries, which may end with negative fortune. They establish neither the leverage-dependent formula nor its equality cases in this model. Broad gambling and martingale literature could nevertheless contain an equivalent envelope theorem; see limitations.

## Limitations

The result is exact within the stated toy fair-betting model, not a claim about real credit markets, transaction costs, margin calls, dependence in market returns or realistic leverage regulation. The horizon counts placed bets, not elapsed calendar time. The uniqueness claim excludes \(L=1\), unreachable histories, and arbitrary changes after the game has already ended. Originality is assessed against the explicitly inspected primary results and searchable research records; independent priority assessment has not been performed. The 2007 Yao full paper was not accessed beyond its abstract and accessible introductory material; it uses a mathematically different primitive-casino model.

## References

- William Kuszmaul, *With Leverage, the Gambler is Not the One Who Gets Ruined*, arXiv:2610.19239v1 (13 October 2026). https://arxiv.org/html/2610.19239v1
- Yi-Ching Yao, *On Optimality of Bold Play for Discounted Dubins–Savage Gambling Problems with Limited Playing Times*, Journal of Applied Probability **44** (2007), 212–225. https://doi.org/10.1239/jap/1175267173
- Yi-Ching Yao and May-Ru Chen, *Strong Optimality of Bold Play for Discounted Dubins–Savage Gambling Problems with Time-Dependent Parameters*, Journal of Applied Probability **45** (2008), 403–416. https://doi.org/10.1239/jap/1214950356
