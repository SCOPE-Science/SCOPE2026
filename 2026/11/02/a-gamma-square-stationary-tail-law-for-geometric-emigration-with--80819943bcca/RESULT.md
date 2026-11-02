# A Gamma-square stationary tail law for geometric emigration without post-reproduction immigration

## Finding

For a natural critical branching process with one potential immigrant *before* emigration but no immigrant *after* offspring reproduction, the stationary law has a sharp Gamma-square polynomial tail in the regime where its mean is infinite. A second threshold separates this regime from the finite-mean phase, and the threshold itself has a logarithmic generating-function singularity.

For \(0<p<1\), define \(a=p/(1-p)\). The process is positive recurrent precisely when \(a>1\). If \(1<a<2\) and \(\pi\) is the unique stationary law, then

\[
\Pr_\pi\{Y>n\}\sim \Gamma(a)^2 n^{1-a}\quad(n\to\infty).
\]

Writing \(H(s)=\mathbb E_\pi[s^Y]\), the exact anchor is \(H(p)=1-a^{-2}\). At \(a=2\) we have \(1-H(s)\sim(1-s)\log(1/(1-s))\), hence \(\sum_{k=0}^{n}\Pr_\pi(Y>k)\sim\log n\). For \(a>2\) the stationary mean is exactly \((a-2)^{-1}\), while it is infinite for \(1<a\le2\).

## Assumptions and scope

All integer indices are nonnegative. Fix \(p\in(0,1)\), take independent geometric emigration variables \(K_n\) with \(\Pr(K_n=k)=(1-p)p^k\), and independent critical geometric offspring variables \(X_{n,j}\) with \(\Pr(X_{n,j}=k)=2^{-k-1}\). Every emigration variable is independent of every offspring variable. The integer-valued Markov chain is

\[
Y_{n+1}=\sum_{j=1}^{(Y_n+1-K_n)_+}X_{n,j},\qquad (z)_+=\max(z,0).
\]

The extra single potential progenitor is placed **before** emigration. There is **no post-reproduction immigrant**. Offspring have mean one and variance two. The chain may start from any deterministic finite state. A stationary measure, when present, is understood as a probability on \(\mathbb N_0\). The probabilistic limit in the theorem is for the unique stationary chain, not for arbitrary finite-time initial conditions.

## Proof

**1. Irreducibility and conditional generating function.** For each state \(y\), a sufficiently large emigration variable makes the next state zero with positive probability, while from state zero the event \(K=0\) permits the offspring variable to take every nonnegative value with positive probability. The chain is irreducible and aperiodic.

The offspring generating function is \(F(s)=1/(2-s)\). Conditioning on \(K\), for every \(0\le s\le1\) with \(F(s)\ne p\),

\[
\mathbb E[s^{Y_{n+1}}\mid Y_n=y]
=\sum_{k=0}^{y}(1-p)p^kF(s)^{y+1-k}+p^{y+1}
=\frac{(1-p)F(s)^2}{F(s)-p}F(s)^y
 +\frac{p^2(F(s)-1)}{F(s)-p}p^y.
\]

For a hypothetical invariant probability, its generating function \(H\) therefore satisfies

\[
H(s)=\frac{(1-p)F(s)^2}{F(s)-p}H(F(s))
+\frac{p^2(F(s)-1)}{F(s)-p}H(p).
\tag{1}
\]

**2. The stationary anchor and nonexistence threshold.** Put \(u=1/(1-s)\) and \(h(u)=H(1-u^{-1})\). Since \(F(1-u^{-1})=1-(u+1)^{-1}\), equation (1), for \(u>\max\{1,a\}\), becomes

\[
h(u)=\frac{u^2}{(u+1)(u-a)}h(u+1)-\frac{pa}{u-a}H(p),\qquad a=\frac p{1-p}.
\tag{2}
\]

Because \(h(u)\) increases to one, (2) implies

\[
u\,[h(u+1)-h(u)]\longrightarrow1-a+paH(p).
\]

If the limit were positive, summing increments would force \(h\) to diverge; if negative, it would contradict monotonicity. Thus it is zero and

\[
H(p)=\frac{a-1}{pa}=1-\frac1{a^2}.
\tag{3}
\]

For \(a\le1\) the right side is nonpositive, whereas \(H(p)=\mathbb E[p^Y]>0\). No invariant probability exists in that regime.

**3. Existence for \(a>1\).** With \(\Delta=Y_{n+1}-y\), conditioning on the geometric emigration and the independent geometric offspring gives, uniformly as \(y\to\infty\),

\[
\mathbb E(\Delta\mid y)=1-a+\frac{p^{y+2}}{1-p},\qquad
\mathbb E(\Delta^2\mid y)=2y+O_p(1),\qquad
\mathbb E(|\Delta|^6\mid y)=O_p(y^3).
\]

The second expression follows from \(\operatorname{Var}(X)=2\) and the fact that the truncated geometric emigration has bounded moments. For the sixth bound use the finite sixth offspring moment and standard moment expansion for sums of centered independent variables conditional on the number of progenitors; the geometric emigration tail is exponentially small. Fix \(1<\eta<\min\{a,2\}\) and let \(V(y)=(1+y)^\eta\). Taylor expansion on \(|\Delta|\le y/2\), the sixth-moment bound for its complement, and the three displayed estimates yield

\[
\mathbb E[V(Y_{n+1})-V(y)\mid Y_n=y]
=\eta(\eta-a)y^{\eta-1}+o_p(y^{\eta-1}).
\tag{4}
\]

The leading coefficient is strictly negative, and \(\eta-1>0\). Consequently the drift is bounded above by a negative constant outside a finite set. The countable-state Foster criterion establishes positive recurrence; irreducibility gives uniqueness of \(\pi\).

**4. Exact stationary recurrence.** Define \(g(u)=1-h(u)\). Equations (2)–(3) yield the affine recurrence

\[
g(u+1)=\frac1{u^2}+\frac{(u+1)(u-a)}{u^2}g(u)
\qquad (u>a).
\tag{5}
\]

At \(u_0=a+1\) one has \(1-u_0^{-1}=p\), so \(g(u_0)=a^{-2}\). Set

\[
R(u)=u\frac{\Gamma(u-a)}{\Gamma(u)}.
\]

Then \(R(u+1)/R(u)=(u+1)(u-a)/u^2\) and \(R(u)\sim u^{1-a}\). Iterating (5) on the grid \(u_j=a+1+j\) gives the **exact identity**

\[
\frac{g(u_n)}{R(u_n)}=
\frac{\Gamma(a)}{a(a+1)}+
\sum_{j=0}^{n-1}
\frac{\Gamma(a+1+j)}{(a+1+j)(a+2+j)\Gamma(j+2)}.
\tag{6}
\]

If \(1<a<2\), the summands behave as \(j^{a-3}\), so the series converges. To evaluate it, insert

\[
\frac1{(a+1+j)(a+2+j)}=
\int_0^1 t^{a+j}(1-t)\,dt
\]

and expand \(\sum_{j\ge0}(a+1)_j t^j/(j+1)!=((1-t)^{-a}-1)/(at)\). Monotone interchange is valid. The sum becomes \(\Gamma(a)\{B(a,2-a)-B(a,2)\}\), with \(B(a,2)=1/[a(a+1)]\). The initial term cancels the latter contribution, so

\[
\frac{g(u_n)}{R(u_n)}\longrightarrow
\Gamma(a)^2\Gamma(2-a).
\tag{7}
\]

As \(u_{n+1}/u_n\to1\), monotonicity of \(g\) extends (7) from the grid to all real \(u\to\infty\). Thus

\[
1-H(s)\sim\Gamma(a)^2\Gamma(2-a)(1-s)^{a-1}\quad(s\uparrow1).
\]

Writing \(q_j=\Pr_\pi(Y>j)\), the identity \((1-H(s))/(1-s)=\sum_{j\ge0}q_j s^j\) and the Hardy–Littlewood–Karamata power-series Tauberian theorem, followed by the monotone density theorem for the decreasing sequence \(q_j\), imply

\[
q_n\sim\frac{\Gamma(a)^2\Gamma(2-a)}{\Gamma(2-a)}n^{1-a}=\Gamma(a)^2n^{1-a}.
\tag{8}
\]

**5. Remaining regimes.** If \(a=2\), the series summands in (6) are asymptotic to \(1/j\), hence \(g(u)\sim u^{-1}\log u\), equivalently the stated logarithmic generating-function singularity. The corresponding Tauberian theorem yields \(\sum_{j\le n}q_j\sim\log n\), and \(\sum_jq_j=\infty\). If \(a>2\), the sum in (6) is asymptotic to \(u^{a-2}/(a-2)\); multiplying by \(R(u)\sim u^{1-a}\) gives \(g(u)\sim[(a-2)u]^{-1}\). Since \(\lim_{s\uparrow1}(1-H(s))/(1-s)=\mathbb E_\pi Y\), the mean is \((a-2)^{-1}\). For \(1<a<2\), the tail (8) has divergent mean. This completes the assertions.

## Verification

Run `python checker.py` with Python 3 and optional `mpmath`. Its finite exact-fraction tests check conditional generating functions, conditional means, stationary functional recurrences, and the critical harmonic identity; optional high-precision checks inspect beta-integral constants and numerical scaling. The recorded execution passed **990 checks** with `mpmath` available. These are algebraic and numerical checks only; the proof of recurrence and all infinite limits is the argument above.

## Relationship to prior work

Patrick Carper's *A Branching Process with Geometric Emigration and the “Have Your Cookie and Eat It” Random Walk* (arXiv:2609.06311v1, publicly posted September 5, 2026) studies a closely related process with post-reproduction immigration and gives recurrence and mean results. The present chain has no such immigrant; that mechanism changes the recurrence threshold and makes its stationary tail exactly tractable. Kosygina–Peterson (arXiv:1504.06280) develops related branching-process tools in excited walks, but its results do not state the present no-post-immigration gamma-square asymptotic. Classical emigration–immigration theory, including Yanev–Yanev (2004), may contain a broader implication and warrants specialist historical review. The result does not claim a new Tauberian theorem or a new general Foster criterion.

## Limitations

The sharp pointwise tail equivalent is established for \(1<a<2\) only. At \(a=2\), the established assertion is a logarithmic generating-function law and a truncated-tail-sum law; no pointwise constant is asserted. The proof does not give a convergence rate to stationarity, a law for the return time, or a joint near-critical parameter limit. The scope is the stated geometric offspring/emigration law and exact order of immigration and emigration. Broader generalizations and absolute historical priority are not established; independent expert mathematical audit has not been performed.

## References

1. Patrick Carper, *A Branching Process with Geometric Emigration and the “Have Your Cookie and Eat It” Random Walk*, arXiv:2609.06311v1 (September 5, 2026). https://arxiv.org/abs/2609.06311
2. Elena Kosygina and Jonathon Peterson, *Excited random walks with Markovian cookie stacks*, arXiv:1504.06280 (April 23, 2015). https://arxiv.org/abs/1504.06280
3. George P. Yanev and Nickolay M. Yanev, *A Critical Branching Process with Stationary-Limiting Distribution*, Stochastic Analysis and Applications 22 (2004), 721–738, doi:10.1081/SAP-120030453. https://doi.org/10.1081/SAP-120030453
4. Classical countable-state Foster–Lyapunov recurrence theorem and Hardy–Littlewood–Karamata Tauberian theorem (standard tools; no new general theorem claimed).
