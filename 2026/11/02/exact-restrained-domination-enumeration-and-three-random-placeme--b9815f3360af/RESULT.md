# Exact restrained-domination enumeration and three random-placement windows for rook graphs

## Finding

For every pair of integers \(m,n\ge 2\), let the rook graph \(R_{m,n}=K_m\square K_n\) have vertex set \([m]\times[n]\), with two distinct cells adjacent when they share a row or column. A restrained dominating set \(S\) is a set for which every cell outside \(S\) has a neighbor inside \(S\) and a neighbor outside \(S\). Write \(U=V(R_{m,n})\setminus S\), and form its incidence bipartite graph \(B_U\) on row vertices \([m]\) and column vertices \([n]\), having edge \(ij\) if and only if \((i,j)\in U\).

**Structure.** The set \(S\) is restrained dominating if and only if (i) \(B_U\) has no connected component consisting of a single edge, and (ii) \(B_U\) does not have simultaneously a row vertex of degree \(n\) and a column vertex of degree \(m\).

**Complete complement-size enumerator.** Define \(F_{m,n}(t)=\sum_{S\text{ restrained dominating}}t^{|V\setminus S|}\). Then
\[
\begin{aligned}
F_{m,n}(t)={}&\sum_{k=0}^{\min(m,n)}(-1)^k\binom mk\binom nk k!\,t^k(1+t)^{(m-k)(n-k)}\\
&-\sum_{a=1}^{m}\sum_{b=1}^{n}(-1)^{a+b}\binom ma\binom nb\,t^{an+bm-ab}(1+t)^{(m-a)(n-b)}.
\end{aligned}
\]
The usual restrained-domination polynomial, weighting selected vertices, is \(D_r(R_{m,n};z)=z^{mn}F_{m,n}(z^{-1})\). The displayed expression is a polynomial with nonnegative integer coefficients despite its inclusion--exclusion terms.

**Three square-board random-placement windows.** For \(N\ge 2\), select each of the \(N^2\) rook-graph vertices independently with probability \(p\), and let \(\mathcal R_N(p)\) be the probability that the selected set is restrained dominating. For every fixed real \(c\),
\[
\lim_{N\to\infty}\mathcal R_N\left(\frac{\log N+c}{N}\right)
=2e^{-e^{-c}}-e^{-2e^{-c}},
\]
\[
\lim_{N\to\infty}\mathcal R_N\left(1-\frac{\log N+\log\log N+c}{2N}\right)
=\exp(-e^{-c}/2),
\]
and for every fixed \(c\ge0\),
\[
\lim_{N\to\infty}\mathcal R_N\left(1-\frac{c}{N^2}\right)=e^{-c}.
\]
Expressions are understood only for sufficiently large \(N\) so all probabilities lie in \([0,1]\). The last two limits expose a nonmonotone near-complete-selection effect: a larger omitted-vertex probability may *increase* the chance of restrained domination by eliminating isolated omissions.

## Assumptions and scope

Graphs are finite, undirected, loopless, simple and labeled. We require \(m,n\ge2\) for the polynomial and incidence characterization. The three probability limits apply to the symmetric sequence \(R_{N,N}\), with the stated fixed \(c\) and independent vertex selection. A single isolated outside vertex is forbidden because it has no neighbor outside \(S\), whereas the empty outside set is permitted. No finite-size exact approximation is claimed for the limit laws.

## Proof

**1. Incidence characterization.** An outside cell \((i,j)\) has \(\deg_U(i)+\deg_U(j)-2\) outside neighbors in the rook graph, where degrees refer to \(B_U\). This number vanishes precisely when both degrees are one, meaning \(ij\) forms an isolated edge component of \(B_U\). The cell has no selected neighbor precisely when its whole row and whole column are outside \(S\), that is, row \(i\) has degree \(n\) and column \(j\) has degree \(m\). Conversely, whenever any full outside row and full outside column exist, their intersection is an outside cell with no selected neighbor. These are exactly the two forbidden patterns, proving both necessity and sufficiency.

**2. Exact polynomial.** Let \(A\) be the family of all edge sets \(U\subseteq E(K_{m,n})\) having no isolated edge component. Apply inclusion--exclusion over the \(mn\) candidate events that a particular edge is present as an isolated edge. A compatible set of \(k\) such events is a matching, since two isolated edges cannot share a row or column. There are \(\binom mk\binom nk k!\) such matchings. Every matching edge is forced present, every other edge touching one of its endpoints is forced absent, and the remaining \((m-k)(n-k)\) edges may be chosen freely. This proves
\[
\sum_{U\in A}t^{|U|}=\sum_{k=0}^{\min(m,n)}(-1)^k\binom mk\binom nk k!\,t^k(1+t)^{(m-k)(n-k)}.
\]

Let \(B\) denote the edge sets with both a full row and a full column. Crucially, \(B\subseteq A\): a full column supplies an outside edge incident with every row, and a full row supplies one incident with every column. Consequently, any present edge outside those two stars has at least one *additional* edge at each endpoint, and every edge in either star has a star endpoint of degree at least two. No edge can be an isolated component. Thus the admissible outside sets are exactly \(A\setminus B\), and the generating polynomial for \(B\) may be subtracted without double-counting a separate obstruction.

To count \(B\), apply inclusion--exclusion to the event that at least one row is full and independently to the event that at least one column is full. Fix \(a\ge1\) designated full rows and \(b\ge1\) designated full columns. They force precisely \(an+bm-ab\) distinct outside cells; the remaining \((m-a)(n-b)\) are optional. The resulting product of alternating sums is
\[
\sum_{U\in B}t^{|U|}=\sum_{a=1}^{m}\sum_{b=1}^{n}(-1)^{a+b}\binom ma\binom nb\,t^{an+bm-ab}(1+t)^{(m-a)(n-b)}.
\]
Subtracting yields the claimed formula. Replacing \(t\) by the inverse selected-vertex variable completes the ordinary restrained-domination polynomial identity.

**3. Sparse selected vertices.** Set \(p_N=(\log N+c)/N\). Let \(X_N\) and \(Y_N\) be the numbers of rows and columns, respectively, containing no selected vertex. For any fixed nonnegative integers \(a,b\),
\[
\begin{aligned}
\mathbb E[(X_N)_a(Y_N)_b]
&=(N)_a(N)_b(1-p_N)^{N(a+b)-ab}\\
&\longrightarrow e^{-c(a+b)}.
\end{aligned}
\]
Here \((v)_k=v(v-1)\cdots(v-k+1)\) is the falling factorial, with \((v)_0=1\). This is the joint factorial-moment sequence of two independent Poisson random variables of common mean \(\lambda=e^{-c}\). Tightness follows from bounded first moments, and joint convergence follows from the factorial-moment method (equivalently, convergence of the joint probability-generating functions near the origin). The condition that no full outside row and full outside column coexist is the event \(X_N=0\) or \(Y_N=0\); its limiting probability is \(2e^{-\lambda}-e^{-2\lambda}\).

An outside cell is isolated within the outside rook graph only if that cell is unselected and all its \(2N-2\) rook neighbors are selected. Therefore
\[
\mathbb P(\text{some isolated outside cell})
\le N^2(1-p_N)p_N^{2N-2}\longrightarrow0.
\]
The structural equivalence proves the first probability limit.

**4. Critical sparse omissions.** Set \(q_N=1-p_N=(\log N+\log\log N+c)/(2N)\), and let \(Z_N\) count isolated edges of the bipartite incidence graph of omitted cells, equivalently isolated vertices in the outside rook graph. A simultaneous collection of \(k\) distinct isolated omitted cells necessarily uses \(k\) different rows and \(k\) different columns. There are \((N)_k^2\) ordered possible collections. Exactly \(k\) omission events must occur, while the other \(2kN-k^2-k\) cells incident to those rows or columns must be selected. Hence for each fixed \(k\ge0\),
\[
\mathbb E[(Z_N)_k]=(N)_k^2q_N^k(1-q_N)^{2kN-k^2-k}
\longrightarrow (e^{-c}/2)^k.
\]
The resulting Poisson law has mean \(\mu=e^{-c}/2\). Its zero probability tends to \(e^{-\mu}\). The other possible obstruction, a fully omitted row and column, occurs with probability at most \(Nq_N^N\), the probability bound for the occurrence of any fully omitted row, which tends to zero. This proves the second limit.

**5. Extremely sparse omissions.** Set \(q_N=c/N^2\), with fixed \(c\ge0\). The probability of omitting no cell equals \((1-q_N)^{N^2}\to e^{-c}\); this configuration is always restrained dominating. The rook graph has exactly \(N^2(N-1)\) edges, so the probability that any two omitted vertices are adjacent is at most
\[
N^2(N-1)q_N^2\le c^2/N\longrightarrow0.
\]
When omissions are nonempty and contain no adjacent pair, each omitted vertex lacks an omitted neighbor, contradicting restraint. Thus the difference between the success probability and the no-omissions probability vanishes, proving the third limit.

## Verification

Run the standalone Python 3 file `verify_rook_restrained.py`, which uses only the standard library. It checks the original two-neighbor definition without relying on the incidence characterization and separately checks the polynomial coefficients. All \(70{,}480\) labeled selected subsets for boards \((m,n)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\) were tested successfully. A numerical factorial-moment diagnostic is provided but does not replace the proofs in Sections 3--5.

## Relationship to prior work

Canoy's 2014 theorem gives a general structural condition for restrained domination in Cartesian products of connected graphs. That general condition logically covers the *definitional feasibility test* after specialization; the present contribution is not the existence of such a test in isolation. The two independent incidence obstructions, their exact overlap-free inclusion--exclusion enumeration for every rectangular board, and the three asymptotic placement laws do not appear in the inspected product theorem. Paul, Chauhan and Swain (publicly posted 2021) developed restrained-domination polynomials for cycles, not for rook graphs; the present polynomial is a different closed incidence enumeration. Standard Poisson moment methods supply a probability technique, not a pre-existing conclusion for this event. The constrained claim is the combined enumerator and three distinct probability limits, not foundational invention of restrained domination, inclusion--exclusion, or Poisson approximation.

## Limitations

The finite verification covers the six listed labeled board sizes; it cannot establish the universal formulas or distributional limits, which require the separate proofs. The three distribution limits hold for independent Bernoulli selection on square boards, not for arbitrary correlated placements, rectangular aspect ratios, or uniform fixed-size subsets. Although no mathematically equivalent enumerator and placement-window law was found in the inspected sources and targeted indexed searches, literature coverage is not exhaustive; priority against unindexed formulations remains uncertain.

## References

1. S. Paul, R. P. Chauhan and S. Swain, *Novel ways of enumerating restrained dominating sets of cycles*, arXiv:2111.11140, first posted 2021-11-22. https://arxiv.org/abs/2111.11140
2. S. R. Canoy Jr., *Restrained Domination in Graphs Under Some Binary Operations*, Applied Mathematical Sciences 8 (2014), 6025--6031, especially Theorem 3.1. https://www.m-hikari.com/ams/ams-2014/ams-121-124-2014/canoyAMS121-124-2014-1.pdf
