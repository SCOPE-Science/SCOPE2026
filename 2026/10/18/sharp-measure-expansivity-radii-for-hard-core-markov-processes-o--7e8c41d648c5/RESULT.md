# Sharp measure-expansivity radii for hard-core Markov processes on the Hilbert-cube shift

## Finding
Consider the bilateral shift \(\sigma\) on the Hilbert cube \(Q=[0,1]^{\mathbb Z}\), equipped with the compatible metric
\[
 d(x,y)=\sum_{j\in\mathbb Z}2^{-|j|}|x_j-y_j|.
\]
For every integer \(m\ge1\), let \(Y_m\subset\{0,1\}^{\mathbb Z}\) be the spacing shift in which any two occurrences of \(1\) have at least \(m\) intervening zeros. For any \(0<p<1\), let \(\mu_{m,p}\) be the stationary finite-state renewal Markov law on \(Y_m\) that places the mandatory \(m\) zeros after every \(1\), and, when no zeros are mandatory, independently chooses the next \(1\) with probability \(p\), or \(0\) with probability \(1-p\). This law is mixing, nonatomic and has full support on \(Y_m\).

For a probability measure \(\mu\) on \(Q\), define its closed two-sided Bowen ball and maximal measure-expansivity radius by
\[
 \Gamma_r(x)=\{y\in Q:d(\sigma^k x,\sigma^k y)\le r\text{ for every }k\in\mathbb Z\},\qquad
 R(\mu)=\sup\{r>0:\mu(\Gamma_r(x))=0\text{ for every }x\in Q\}.
\]
Then the exact radius, independent of \(p\), is
\[
 \boxed{R(\mu_{m,p})=\min\!\left\{\frac32,\;1+\frac{2}{2^{m+1}-1}\right\}=\begin{cases}\frac32,&m=1,\\[2pt]1+\frac{2}{2^{m+1}-1},&m\ge2.\end{cases}}
\]
More strongly, every \(0<r<R(\mu_{m,p})\) is measure-expansive, whereas the critical radius itself is not: a constant center has a Bowen ball of full measure. Thus \(R(\mu_{1,p})=3/2\), \(R(\mu_{2,p})=9/7\), and \(R(\mu_{m,p})\downarrow1\) as \(m\to\infty\). All Bowen-ball centers range over the **ambient Hilbert cube**, not merely the binary support.

## Assumptions and scope
The shift is \((\sigma x)_j=x_{j+1}\). Define \(d_m=m+1\) as the minimum permitted separation between two ones. For \(0<p<1\), the Markov process can be constructed using the state \(h\in\{0,1,\ldots,m\}\) of compulsory zeros remaining before generating a symbol: for \(h>0\), output \(0\) and decrease \(h\) by one; for \(h=0\), output \(1\) with probability \(p\) and set the next state to \(m\), otherwise output \(0\) and keep state \(0\). Use the unique stationary distribution of this irreducible, aperiodic finite-state chain. Its observed binary process is supported on \(Y_m\), gives positive probability to every admissible finite word, and has a uniform positive probability of producing a prescribed admissible word after a bounded all-zero reset.

The metric normalization has total weight \(\sum_{j\in\mathbb Z}2^{-|j|}=3\). The stated supremum concerns closed Bowen balls. The theorem concerns this exact normalization, two-sided orbits and finite spacing \(m\), not universal radii for all compatible metrics or all stationary measures.

## Proof
**Step 1: an exact weighted packing radius.** Put \(t=2^{-(m+1)}\), and define
\[
 W_m=\max_{z\in Y_m}\sum_{j\in\mathbb Z}2^{-|j|}z_j.
\]
The weighted series converges uniformly on the compact subshift, so its maximum is attained. For \(z_0=1\), both tails may have ones at \(\pm(m+1),\pm2(m+1),\ldots\), but no more densely than this, and therefore their total weight is bounded by \(2t/(1-t)\). Equality is attained by the periodic configuration with ones at all multiples of \(m+1\). Thus the maximum among configurations with \(z_0=1\) is \((1+t)/(1-t)\).

For \(z_0=0\), if ones occur on both sides, let \(-a<0<b\) be the positions of the closest ones, with \(a,b\ge1\) and \(a+b\ge m+1\). The two tails contribute at most
\[
 \frac{2^{-a}+2^{-b}}{1-t}\le\frac{1/2+2^{-m}}{1-t}<\frac{1+t}{1-t}.
\]
The middle bound follows because, at fixed smallest possible sum \(a+b=m+1\), the convex function \(a\mapsto2^{-a}+2^{-(m+1-a)}\) reaches its maximum at an endpoint \(a=1\) or \(a=m\); larger sums only decrease one contribution. If one side has no ones, its weight is zero and the other side contributes at most \((1/2)/(1-t)\). The strict inequality also holds for \(m=1\). Consequently
\[
 \boxed{W_m=\frac{1+t}{1-t}=1+\frac{2}{2^{m+1}-1}.}
\]

**Step 2: the optimal ambient constant center.** Define the continuous convex function
\[
 F(x)=\max_{z\in Y_m}d(x,z),\qquad x\in Q.
\]
It is \(1\)-Lipschitz in \(d\), as a supremum of \(1\)-Lipschitz functions. For the constant configuration \(\mathbf c=(\ldots,c,c,\ldots)\), \(0\le c\le1\), each binary \(z\) satisfies
\[
 d(\mathbf c,z)=3c+(1-2c)\sum_j2^{-|j|}z_j.
\]
The all-zero configuration and the exact maximum from Step 1 give
\[
 F(\mathbf c)=\begin{cases}
 3c+(1-2c)W_m,&0\le c\le1/2,\\
 3c,&1/2\le c\le1.
 \end{cases}
\]
This piecewise affine function has minimum
\[
 R_m:=\min_{0\le c\le1}F(\mathbf c)=\min\{W_m,3/2\}.
\]
For \(m=1\), the minimizing center \(\mathbf{1/2}\) has distance exactly \(3/2\) from **every** binary configuration. For \(m\ge2\), \(W_m<3/2\), and the minimizing center \(\mathbf0\) has distance at most \(W_m\) from every configuration in \(Y_m\). In each case \(\mu_{m,p}(\Gamma_{R_m}(\mathbf c))=1\). Therefore \(R(\mu_{m,p})\le R_m\), and the endpoint is not expansive.

**Step 3: an all-centers averaging obstruction.** Fix an arbitrary \(x\in Q\) and define
\[
 A_N=\frac1N\sum_{k=0}^{N-1}\sigma^k x,\qquad
 c_N=\frac1N\sum_{k=0}^{N-1}x_k.
\]
Arithmetic means of sequences are taken coordinatewise. For each fixed \(j\), cancellation of the overlapping averaging windows yields
\[
 |(A_N)_j-c_N|\le\min\{1,2|j|/N\}.
\]
Dominated convergence with the summable weights implies
\[
 d(A_N,\mathbf{c_N})\le\sum_{j\in\mathbb Z}2^{-|j|}\min\{1,2|j|/N\}\longrightarrow0,
\]
uniformly in the original center \(x\). Since \(F\) is convex and \(1\)-Lipschitz, Jensen's inequality gives
\[
 \frac1N\sum_{k=0}^{N-1}F(\sigma^k x)\ge F(A_N)
 \ge F(\mathbf{c_N})-d(A_N,\mathbf{c_N})\ge R_m-o(1).
\]
Hence for every \(0<r<R_m\), there exist \(\eta>0\) and infinitely many positive times \(k\), with arbitrarily large separations, such that \(F(\sigma^k x)>r+2\eta\). This conclusion holds for **every** ambient real-valued center \(x\), irrespective of stationarity or admissibility of \(x\).

**Step 4: uniform Markov block forcing.** Choose \(L\) so large that the two-sided weight tail satisfies
\[
 \sum_{|j|>L}2^{-|j|}=2^{1-L}<\eta.
\]
For each selected time \(k_i\), choose \(z^{(i)}\in Y_m\) attaining \(F(\sigma^{k_i}x)\). The admissible word \(w^{(i)}=z^{(i)}|_{[-L,L]}\), of common length \(\ell=2L+1\), therefore satisfies
\[
 \sum_{|j|\le L}2^{-|j|}|x_{k_i+j}-w^{(i)}_j|>r+\eta>r.
\]
Thin the times further so the observation blocks \([k_i-L,k_i+L]\) and their immediately preceding \(m\)-site reset blocks are pairwise disjoint and ordered. Conditional on any past before a reset block, the Markov process outputs \(m\) zeros with probability at least \((1-p)^m\): forced zeros have probability one, and optional zeros have probability \(1-p\). After this reset it can output any allowed word of length \(\ell\), with probability at least \(q^\ell\), where \(q=\min\{p,1-p\}>0\). Thus each prescribed word event, including its reset prefix, has conditional probability at least
\[
 \delta=(1-p)^m q^{\ell}>0
\]
independently of the past and of the particular admissible target word. For the separated selected blocks, repeated conditioning yields that the probability of avoiding the first \(N\) prescribed word events is at most \((1-\delta)^N\), which tends to zero.

If even one prescribed word event occurs, the corresponding shifted metric distance exceeds \(r\), so the random trajectory is outside \(\Gamma_r(x)\). Therefore \(\mu_{m,p}(\Gamma_r(x))=0\). Since \(x\in Q\) was arbitrary, every \(r<R_m\) is expansive. Together with Step 2, this proves the exact radius and its endpoint behavior.

## Verification
A self-contained Python 3 verifier (`verify.py`) carries out 504 exact rational assertions. Dynamic programming computes maximal weighted finite-window admissible binary words for \(1\le m\le8\) and lengths \(7,15,23,35\), compares them with the limiting packing bound and its explicit tail error, and checks the constant-center minimax formula at 17 rational values in each spacing family. Run `python3 verify.py`. These finite tests are consistency checks, **not** a proof for all \(m\), arbitrary centers, or infinitely many Markov blocks; those conclusions follow from Steps 1–4.

## Relationship to prior work
Lacerda [1] establishes the existence of expansive product Lebesgue measure for the bilateral Hilbert-cube shift, together with genericity statements. That construction does not give the exact maximal closed-Bowen-ball expansivity radius of a singular, dependent, stationary hard-core Markov measure. Morales [2] supplies general terminology and structural foundations of measure expansivity rather than this metric-dependent exact packing problem. The published concentration-criterion result [3] characterizes **independent** (possibly nonstationary) coordinate-product measures and a Baire dichotomy in their marginal-law parameter space. Its proof explicitly uses factorization of cylinder-box masses into independent marginal probabilities, which cannot cover the Markov measures here; the present proof instead uses an orbitwise convex minimax argument and uniform conditional block forcing. General symbolic coding and finite-state Markov foundations do not by themselves evaluate the displayed weighted packing radii. No claim of a new definition of expansivity, Markov mixing, or weighted-interval convexity is made.

## Limitations
The exact numerical thresholds depend on the chosen exponentially weighted \(\ell_1\) product metric and on the condition that Bowen-ball centers range over all of \(Q\). The probability law is a full-support stationary hard-core Markov law with \(0<p<1\); the endpoints \(p=0\) and \(p=1\), arbitrary dependent processes without uniform conditional block forcing, nonbinary alphabets, other weight sequences, and one-sided Bowen balls are not included. The result is a theorem about finite-spacing symbolic supports in an infinite-dimensional ambient shift, not about invariant distributions on the entire Hilbert cube. It supplies no universal invariant of topological conjugacy under changing the compatible metric. Equivalent results may be implicit in wider quantitative measure-expansivity or constrained symbolic-packing literature; the prior-art search cannot prove universal novelty.

## References
[1] G. Lacerda, *Typical expansive measures for infinite-dimensional maps*, arXiv:2610.09482v1, first public 2026-10-07, https://arxiv.org/abs/2610.09482.

[2] C. A. Morales, *Measure-expansive systems*, arXiv:2503.16757, public electronic posting 2025-03-21, https://arxiv.org/abs/2503.16757.

[3] *A concentration criterion and Baire dichotomy for product measures on the Hilbert-cube shift*, publicly available research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-concentration-criterion-and-baire-dichotomy-for-product-measur--a21666c938a0 (RESULT.md inspected in full).
