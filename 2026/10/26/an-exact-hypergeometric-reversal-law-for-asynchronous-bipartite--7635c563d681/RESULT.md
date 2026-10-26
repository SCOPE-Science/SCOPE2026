# An exact hypergeometric reversal law for asynchronous bipartite majority

## Finding

For every pair of odd integers \(m,n\ge3\), independent fair binary initial opinions on the complete bipartite network \(K_{m,n}\) followed by random sequential strict-neighborhood-majority updates reach unanimous consensus almost surely. The probability of **reversing the initial strict overall majority**, excluding initially tied profiles from the inversion event, has an explicit finite hypergeometric formula. If both part sizes grow and their ratio tends to a finite \(\rho\ge1\), the reversal probability has the explicit arcsine limit

\[
\lim R_{m,n}=\frac1\pi\arcsin\left(\frac{\rho-1}{\rho+1}\right).
\]

The limit is zero for equal-sized communities, \(1/6\) for a three-to-one size ratio, and increases toward \(1/2\) as the finite limiting ratio increases without bound. The last statement takes the limit in the ratio **after** the fixed-ratio large-network limit; it does not cover ratios diverging with network size.

## Assumptions and scope

Let \(m,n\ge3\) both be odd. The network consists of two sets \(L,R\) with \(|L|=m\), \(|R|=n\), all possible cross-edges, and no internal edges. Each vertex initially publicly expresses red or blue, independently with probability \(1/2\). At each discrete time step select one vertex uniformly at random, independently of earlier steps, and replace its opinion by the majority opinion among its neighbors. As each part size is odd, **ties never arise at individual updates**. Initial opinions remain visible from time zero. Global ties at time zero are not counted as reversals.

For nonnegative integers define \(\binom uv=0\) if \(v<0\) or \(v>u\). When initial red counts on \(L,R\) are \(x>m/2\) and \(y<n/2\), put

\[
r=x,\qquad s=n-y,\qquad a=x-\frac{m-1}{2},\qquad b=\frac{n+1}{2}-y,
\]

and let

\[
H_{m,n}(x,y)=\frac{1}{\binom{r+s}{a+b-1}}\sum_{k=a}^{a+b-1}\binom{r}{k}\binom{s}{a+b-1-k}.
\]

For this profile the final unanimous opinion is blue with probability \(H_{m,n}(x,y)\). If the two parts initially agree on their majorities, consensus has this common color with probability one. The mirrored case \(x<m/2,\ y>n/2\) follows by exchanging color names.

More explicitly, with \(N=m+n\), the unconditional probability of strict-initial-majority reversal is

\[
R_{m,n}=2^{1-N}\sum_{x=(m+1)/2}^{m}\sum_{y=0}^{(n-1)/2}
\binom mx\binom ny\,\Theta_{m,n}(x,y),
\]

where

\[
\Theta_{m,n}(x,y)=\begin{cases}
H_{m,n}(x,y),&2(x+y)>N,\\
1-H_{m,n}(x,y),&2(x+y)<N,\\
0,&2(x+y)=N.
\end{cases}
\]

The prefactor \(2\) accounts for simultaneous red-blue reversal, not for interchanging the unequal parts.

## Proof

**1. The first tipping event determines consensus.** Suppose the part \(L\) initially has a red majority and \(R\) a blue majority. While both majorities persist, updating a vertex in \(L\) sets it blue, and updating a vertex in \(R\) sets it red. Therefore each initially red vertex in \(L\) changes at its first selection, each initially blue vertex in \(R\) changes at its first selection, and the other vertices do not change before the first majority reversal. The majority in \(L\) changes after \(a\) distinct initially red \(L\)-vertices have been selected; the majority in \(R\) changes after \(b\) distinct initially blue \(R\)-vertices have been selected. No single update can flip both groups. When the first group flips, both group majorities agree. From that time every selected vertex changes, if necessary, to the common majority; this cannot change either group majority. Almost surely all vertices are eventually selected, so unanimity in that color follows. If initial part majorities agree, the same monotonicity immediately applies.

**2. Exact hypergeometric first-flip probability.** The subsequence of first selections of the \(r+s\) relevant vertices (initial red in \(L\), initial blue in \(R\)) has the law of a uniformly random permutation of these vertices. The first \(a+b-1\) distinct relevant selections contain at least \(a\) vertices from the \(L\) class if and only if the \(L\) majority tips first. Their red-\(L\) count is hypergeometric with population \(r+s\), marked population \(r\), sample size \(a+b-1\). Counting yields precisely \(H_{m,n}(x,y)\). If \(L\) tips first, both resulting part majorities are blue. When \(R\) tips first, they are red.

**3. Finite unconditional formula.** The independent red-count variables are binomial with parameters \((m,1/2)\) and \((n,1/2)\). Sum the conditional probability of a reversed final consensus over profiles with \(L\) red-majority and \(R\) blue-majority. If initially \(x+y>N/2\), final blue occurs with probability \(H\); if initially \(x+y<N/2\), final red occurs with probability \(1-H\). Initially tied profiles contribute zero by definition. Color exchange bijects the opposite sector with equal conditional reversal probability. This gives the displayed exact formula.

**4. Asymptotic race.** Let \(X=2x-m\) and \(Y=2y-n\) be initial signed majority margins. Their variances are \(m\) and \(n\) and they are independent. Work on the event of opposite group-majority signs. Independent unit-rate exponential clocks for vertices give the same sequence of selected vertices as the discrete uniform-choice process. The tipping times are the \((|X|+1)/2\)-th first activation among \((m+|X|)/2\) relevant vertices in the left part, and analogously in the right part. Conditionally on margins of order at most a constant times the respective square roots, the \(a\)-th order statistic of \(r\) independent unit exponentials has mean \(\sum_{j=0}^{a-1}(r-j)^{-1}=|X|/m+O(m^{-1})\) and variance \(\sum_{j=0}^{a-1}(r-j)^{-2}=O(m^{-3/2})\). The same estimate holds with \(Y,n\). Central-limit tightness allows the constant cutoff to increase after taking limits. Hence the race outcome converges in probability, outside a limiting zero-probability equality boundary, to the comparison of \(|X|/m\) with \(|Y|/n\).

The global initial majority is determined by the larger **unnormalized** absolute margin when signs differ. The final consensus is determined by the larger **normalized** absolute margin because that group's majority tips later. Assume \(m/n\to\rho\ge1\); interchange the parts if necessary. Consequently the limiting inversion event is the wedge

\[
XY<0,\qquad |Y|<|X|<\rho|Y|.
\]

By the bivariate central limit theorem, \(X/\sqrt m\) and \(Y/\sqrt n\) converge jointly to independent standard normals \(Z_1,Z_2\), and the wedge boundaries have zero Gaussian probability. Thus the limit is

\[
\frac12\Pr\!\left(\rho^{-1/2}<\left|\frac{Z_1}{Z_2}\right|<\rho^{1/2}\right)
=\frac2\pi\arctan\sqrt\rho-\frac12
=\frac1\pi\arcsin\frac{\rho-1}{\rho+1},
\]

using that a ratio of independent standard normals has the Cauchy distribution. The formula also holds for \(\rho=1\), where the limiting wedge has zero measure. This completes the proof.

## Verification

The accompanying standalone `verify.py` computes the hypergeometric first-tip law with exact rational arithmetic and independently solves the absorbing-state recurrence for the asynchronous Markov process. It compares every initial count pair for all \(16\) ordered part-size pairs with both sides in \(\{3,5,7,9\}\), totaling \(784\) conditional cases. It also directly enumerates each labeled binary initial profile for three small networks and checks the resulting unconditional rational inversion probabilities. Representative results are

\[
R_{3,3}=\frac9{160},\qquad R_{3,5}=\frac{131}{1792},\qquad R_{3,9}=\frac{233}{2048}.
\]

These finite computations check the formula at specified sizes and do not constitute a proof of the infinite statement; the analytical argument above does.

## Relationship to prior work

Schoenebeck and Yu (2018) investigate random sequential node dynamics, including majority-like updates, on complete and dense Erdős–Rényi random graphs; their publicly available paper was inspected for its model and principal theorems. Their results do not directly provide this exact complete-bipartite majority-reversal formula. Mohan and Prałat (first posted 2023-09-09) study asynchronous majority dynamics on binomial random graphs, but their public announcements are initially *unset* and derive from private signals, unlike the fully public initial opinions here. The 2015 spectral voter-model analysis of Pickering and Lim treats neighbor-copying rather than deterministic neighborhood-majority updates. No claim is made that the hypergeometric distribution, the Cauchy-ratio identity, or first-activation racing techniques are new.

## Limitations

The formula requires odd part sizes (hence no update ties), independent fair initial colors, complete cross-community adjacency, and uniform independent vertex updates. It excludes initial global ties from its event. The arcsine law assumes both side sizes diverge with a **finite** limiting ratio, and does not assert an interchange of this limit with the large-ratio limit. No theorem is established for sparse bipartite networks, even part sizes, correlated or biased initial opinions, or simultaneous updates. Although targeted literature and overlap searches found no stronger covering result, equivalent unindexed results cannot be ruled out; independent validation has not been performed.

## References

1. Grant Schoenebeck and Fang-Yi Yu, *Consensus of Interacting Particle Systems on Erdős–Rényi Graphs*, SODA 2018, DOI: 10.1137/1.9781611975031.127, public version at `https://schoeneb.people.si.umich.edu/papers/Voter-Model.pdf`.
2. Divyarthi Mohan and Paweł Prałat, *Asynchronous Majority Dynamics on Binomial Random Graphs*, arXiv:2309.04691, first posted 2023-09-09, `https://arxiv.org/abs/2309.04691`.
3. William Pickering and Chjan Lim, *Solution of the Voter Model by Spectral Analysis*, Physical Review E 91 (2015), 012812, DOI: 10.1103/PhysRevE.91.012812.
