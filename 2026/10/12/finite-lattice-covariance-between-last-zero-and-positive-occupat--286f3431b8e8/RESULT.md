# Finite-lattice covariance between last zero and positive occupation
## Finding
Let \(X_1,X_2,\ldots\) be independent with \(\Pr(X_i=1)=\Pr(X_i=-1)=1/2\), and let
\[
S_0=0,\qquad S_j=\sum_{i=1}^j X_i.
\]
For an integer \(n\ge1\), define the last zero before the fixed horizon and the strict-positive occupation count by
\[
L_{2n}=\max\{0\le j\le2n:S_j=0\},\qquad
A_{2n}=\sum_{j=1}^{2n}\mathbf 1\{S_j>0\}.
\]
Write
\[
u_{2k}=\Pr(S_{2k}=0)=\frac{\binom{2k}{k}}{4^k}.
\]
Then, for every \(0\le k\le n\),
\[
\mathbb E[A_{2n}\mid L_{2n}=2k]
=n+\frac12-\frac{1}{2u_{2k}}.
\]
In particular,
\[
\operatorname{Cov}(L_{2n},A_{2n})
=-\frac{n(2n+1)}6\frac{\binom{2n}{n}}{4^n}<0.
\]
Equivalently,
\[
\operatorname{Cov}\!\left(\frac{L_{2n}}{2n},\frac{A_{2n}}{2n}\right)
=-\frac{2n+1}{24n}\frac{\binom{2n}{n}}{4^n}
\sim-\frac{1}{12\sqrt{\pi n}}.
\]

## Assumptions and scope
The walk is the ordinary one-dimensional simple symmetric random walk and the horizon is even. The occupation statistic is strict: visits with \(S_j=0\) do not count as positive. The result is exact for every integer \(n\ge1\). It does not assert a formula for biased walks, non-nearest-neighbor increments, or other conventions for counting zero visits.

The primary subject is finite-horizon random-walk fluctuation theory, classified here as MSC \(60G50\).

## Proof
The classical discrete arcsine decomposition gives
\[
\Pr(L_{2n}=2k)=u_{2k}u_{2n-2k},\qquad 0\le k\le n.
\]
Condition on \(L_{2n}=2k\). Independence of increments shows that the path through time \(2k\), conditioned on returning to zero there, is a simple random-walk bridge. The condition that there is no later zero concerns only subsequent increments and does not alter that bridge law.

For the bridge, sign symmetry gives one half of the expected nonzero observation times as positive. At an even bridge time \(2r\),
\[
\Pr(S_{2r}=0\mid S_{2k}=0)
=\frac{u_{2r}u_{2k-2r}}{u_{2k}}.
\]
The return-probability generating function
\[
U(z)=\sum_{r\ge0}u_{2r}z^r=(1-z)^{-1/2}
\]
implies
\[
\sum_{r=0}^k u_{2r}u_{2k-2r}=1.
\]
Hence the expected number of zero observations among times \(1,\ldots,2k\), including the terminal return, is
\[
\frac{1-u_{2k}}{u_{2k}}
=\frac1{u_{2k}}-1.
\]
Therefore the expected strict-positive occupation before and including time \(2k\) is
\[
k-\frac12\left(\frac1{u_{2k}}-1\right)
=k+\frac12-\frac1{2u_{2k}}.
\]

After the last zero, the zero-free terminal segment has one sign throughout. Reflection symmetry makes that sign positive or negative with equal probability. Its length is \(2(n-k)\), so its mean strict-positive contribution is \(n-k\). Adding the bridge contribution proves
\[
\mathbb E[A_{2n}\mid L_{2n}=2k]
=n+\frac12-\frac1{2u_{2k}}.
\]

Set
\[
T_n=\sum_{r=0}^n u_{2r}.
\]
Since \(U(z)/(1-z)=(1-z)^{-3/2}\),
\[
T_n=(2n+1)u_{2n}.
\]
Also
\[
\sum_{r=0}^n r u_{2r}
=[z^n]\frac{zU'(z)}{1-z}
=\frac n3 T_n.
\]
Symmetry of the last-zero mass function gives \(\mathbb E[L_{2n}]=n\). Averaging the conditional mean gives
\[
\mathbb E[A_{2n}]=n+\frac12-\frac12T_n.
\]
For the mixed moment,
\[
\begin{aligned}
\mathbb E[L_{2n}A_{2n}]
&=\sum_{k=0}^n 2k\,u_{2k}u_{2n-2k}
\left(n+\frac12-\frac1{2u_{2k}}\right)\\
&=n\left(n+\frac12\right)-\sum_{k=0}^n k u_{2n-2k}\\
&=n\left(n+\frac12\right)-\frac{2n}3T_n.
\end{aligned}
\]
Subtracting \(\mathbb E[L_{2n}]\mathbb E[A_{2n}]\) yields
\[
\operatorname{Cov}(L_{2n},A_{2n})
=-\frac n6T_n
=-\frac{n(2n+1)}6\frac{\binom{2n}{n}}{4^n}.
\]
Finally, the central-binomial asymptotic
\[
\frac{\binom{2n}{n}}{4^n}
=\frac1{\sqrt{\pi n}}\left(1+O(n^{-1})\right)
\]
gives the stated normalized covariance asymptotic.

## Verification
The accompanying `checker.py` independently enumerates every \(2n\)-step sign sequence for \(1\le n\le9\) using exact integer counts and rational arithmetic. It verifies the last-zero distribution, every conditional mean \(\mathbb E[A_{2n}\mid L_{2n}=2k]\), both generating-function coefficient identities used in the proof, the two marginal means, and the final covariance. The run reported in `CHECKER_OUTPUT.txt` completed 153 exact assertions.

## Relationship to prior work
Pitman and Yor's arcsine-law treatment places positive occupation and last-zero functionals in the same classical Brownian excursion framework. Their result is continuous-time and does not state this finite-lattice conditional mean or covariance.

A particularly close discrete comparison is Chao and Slivka's 1987 paper on the number of one-sided deviations and the time of the last such deviation. Its full text treats infinite-horizon crossings of a nonzero linear boundary and gives separate exact distributions for the number of exits and the last exit time. Its variables are not the fixed-horizon pair \((L_{2n},A_{2n})\), and its hypotheses require a positive boundary offset; its theorems do not imply the covariance above.

Csáki's 1994 paper gives exact and asymptotic joint distributions for selected variables defined on Bernoulli excursions. The accessible abstract and references establish its relevance, but the full article was not available through the public source inspected here. This leaves a residual literature risk, recorded in the review, though the paper's stated scope concerns variables on individual excursions rather than the whole-path pair studied here.

The finite formula is also not implied by a previously checked result for covariance between positive occupation and the terminal random-walk position: replacing the endpoint by the non-stopping last-zero functional changes both the decomposition and the dependence mechanism.

## Limitations
The proof is specific to symmetry and nearest-neighbor increments. The exact expression concerns strict-positive occupation and an even deterministic horizon. The literature comparison cannot exclude every unindexed historical identity; in particular, only abstract-level material was available for the most relevant 1994 Bernoulli-excursion paper. The checker verifies finite instances and algebraic identities but is supplementary to, not a substitute for, the all-\(n\) proof.

## References
1. J. Pitman and M. Yor, “Arcsine Laws and Interval Partitions Derived from a Stable Subordinator,” *Proceedings of the London Mathematical Society* 65 (1992), 326–356. DOI: 10.1112/plms/s3-65.2.326.
2. C.-C. Chao and J. Slivka, “Some exact distributions of the number of one-sided deviations and the time of the last such deviation in the simple random walk,” *Stochastic Processes and their Applications* 24 (1987), 279–286. DOI: 10.1016/0304-4149(87)90018-4.
3. E. Csáki, “Some joint distributions in Bernoulli excursions,” *Journal of Applied Probability* 31A (1994), 239–250. DOI: 10.2307/3214959.
