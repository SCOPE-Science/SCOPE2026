# Universal first-order dimer jamming under degree-two forbidden-edge deletion

## Finding

Let \(N\ge6\) be even, and let \(H_N\) be an arbitrary simple graph on \(N\) labelled vertices with maximum degree at most two. Put \(m_N=|E(H_N)|\), and let \(G_N=K_N\setminus E(H_N)\). Run random sequential dimer adsorption on the edges of \(G_N\): order all allowed edges uniformly at random, accepting an edge exactly when neither endpoint has previously been occupied. Let \(P_N\) be the probability of imperfect final coverage and \(U_N\) the number of vacant vertices. Uniformly over all such \(H_N\), as even \(N\to\infty\),

\[
P_N=\frac{3m_N}{N^2-1}\bigl(1+O(N^{-1/3})\bigr)\quad (m_N>0),
\]

where the implicit constant is absolute. If \(m_N=0\), then \(P_N=0\). For every instance, \(U_N\in\{0,2\}\). Thus, if \(m_N/N\to c\in[0,1]\), then \(NP_N\to3c\), and \(\mathbb E[U_N]/N=2P_N/N\). In particular, deleting a Hamiltonian cycle or a spanning path produces \(NP_N\to3\), while deleting a perfect matching produces \(NP_N\to3/2\). The leading term depends only on the number, not the placement, of forbidden edges; this is a uniform assertion over paths, cycles, their disjoint unions, and all other graphs of maximum degree two.

## Assumptions and scope

All graphs are finite, simple, undirected and labelled. \(N\) is even and at least six; \(H_N\) may vary arbitrarily with \(N\), but has maximum degree at most two. The weights or priority times on all **allowed** edges are independent and identically distributed with an atomless law; only their relative order matters. An edge whose endpoint was already occupied cannot be accepted. The graph \(G_N\) always has a perfect matching: every vertex has at least \(N-3\ge N/2\) neighbors, so the Dirac Hamiltonicity criterion applies, and alternating edges of a Hamiltonian cycle form a perfect matching. Moreover, every induced subgraph on an even number \(k\ge4\) of vertices has a permitted edge. Thus the adsorption outcome is a maximal matching with zero or two vacancies. There is no assumption that forbidden-edge components have a limiting size distribution.

The \(O(N^{-1/3})\) estimate is an **asymptotic uniform relative error** for \(m_N>0\), not a claimed numerical inequality for small \(N\). It is equivalently an absolute error \(O(m_NN^{-7/3})\), which is \(O(N^{-4/3})\) because \(m_N\le N\).

## Proof

**1. The random-priority process is an exact uniform-edge Markov chain.** Assign independent unit-rate exponential clocks to the allowed edges. Processing clocks in increasing order gives the same random edge permutation as any atomless independent priorities. Memorylessness shows that, conditional on the current unoccupied vertex set \(S\), the next accepted edge is uniform among all allowed edges inside \(S\). Delete its endpoints, and repeat. Since a graph of maximum degree two cannot induce a complete graph on four or more vertices, \(G_N[S]\) has an edge whenever \(|S|\ge4\); therefore the only possible jammed residual sets have zero or two vertices. A residual pair is jammed precisely when it is an edge of \(H_N\).

**2. A tagged forbidden pair and the one-deletion baseline.** Fix an edge \(e=\{u,v\}\) of \(H_N\). At a stage with \(k\) unoccupied vertices containing both endpoints of \(e\), write \(r\) for the number of other forbidden edges entirely among the remaining \(k-2\) vertices and \(a\) for the number of forbidden edges joining \(\{u,v\}\) to those vertices. The degree bound gives \(0\le a\le2\), \(r\le k\). The conditional probability of choosing the next dimer away from the tagged endpoints is exactly

\[
p_k(e)=\frac{\binom{k-2}{2}-r}{\binom{k}{2}-1-a-r}.
\]

If the only forbidden edge were \(e\), this would be

\[
p_k^{(0)}=\frac{\binom{k-2}{2}}{\binom{k}{2}-1}=\frac{k-3}{k+1}.
\]

For \(k\ge10\), elementary subtraction of the displayed fractions, with \(r\le k\) and \(a\le2\), gives \(p_k(e)/p_k^{(0)}=1+O(k^{-2})\), **uniformly in the unoccupied set**. For any even \(K\ge10\), iterating these conditional upper and lower bounds over the stages \(N,N-2,\dots,K+2\) yields

\[
\Pr(e\subseteq S_K)=\prod_{k=K+2,K+4,\dots,N}p_k^{(0)}\bigl(1+O(K^{-1})\bigr)
=\frac{K^2-1}{N^2-1}\bigl(1+O(K^{-1})\bigr).
\]

Here \(S_K\) is the set of the \(K\) vertices left after \((N-K)/2\) accepted dimers; \(N\ge K\). The second identity is the exact telescoping product. In the model with only the single missing edge \(e\), its survival probability from \(K\) vertices all the way to the last pair is exactly

\[
F_K=\prod_{k=4,6,\dots,K}\frac{k-3}{k+1}=\frac3{K^2-1}.
\]

**3. Other forbidden edges are unlikely to accompany the tagged edge late in the process.** For any specified set \(T\) of \(t\in\{2,3,4\}\) vertices, given that it is still present at stage \(k\), write \(r_T\le k\) for forbidden edges wholly outside \(T\) and \(s_T\le2t\) for those incident to \(T\). The probability that the next selected edge avoids \(T\) is

\[
\frac{\binom{k-t}{2}-r_T}{\binom{k}{2}-r_T-s_T}.
\]

Comparing to the complete-graph probability \(\binom{k-t}{2}/\binom{k}{2}\) gives a ratio \(1+O_t(k^{-2})\), uniformly for sufficiently large \(k\): the numerator of the difference of these ratios is \(\binom{k-t}{2}s_T-r_T[\binom{k}{2}-\binom{k-t}{2}]\), of order at most \(O_t(k^2)\), and its denominator is of order \(k^4\). Consequently,

\[
\Pr(T\subseteq S_K)\le(1+O_t(K^{-1}))\frac{(K)_t}{(N)_t},
\]

where \((x)_t=x(x-1)\cdots(x-t+1)\). Let \(B_e\) be the event that \(e\subseteq S_K\) **and** \(H_N[S_K]\) contains another forbidden edge. There are at most two forbidden edges sharing a vertex with \(e\), and at most \(m_N\le N\) disjoint forbidden edges. Applying the preceding estimate with \(t=3\) or \(4\), followed by the tagged survival estimate of step 2, gives

\[
\Pr(B_e\mid e\subseteq S_K)
\le C\left(\frac KN+\frac{K^2}{N}\right),
\]

for \(N\ge2K\) and a universal constant \(C\).

**4. Uniform control even on the exceptional event.** From any unoccupied \(K\)-set containing \(e\), survival of \(e\) through the stages down to eight vertices has conditional probability at most \(C/K^2\). Indeed, apply the \(t=2\) comparison from step 3 down to eight vertices and use the complete-graph survival product \((8)_2/(K)_2\). The probability of finally leaving \(e\) vacant is no larger. In contrast, if \(H_N[S_K]\) contains **only** the missing edge \(e\), the exact conditional final-survival probability is \(F_K=3/(K^2-1)\). Thus, uniformly over the history before stage \(K\),

\[
\Pr(e=S_2)=\Pr(e\subseteq S_K)F_K
\left(1+O\left(\frac KN+\frac{K^2}{N}\right)\right)
=\frac3{N^2-1}\left(1+O\left(K^{-1}+K^2/N\right)\right).
\]

Here \(S_2\) is the intermediate set of two vertices just before the potential last deposition; every trajectory with \(e\subseteq S_K\) reaches this stage, and the event \(S_2=e\) is terminal because \(e\) is forbidden. Select an even \(K\) comparable to \(N^{1/3}\) and at least ten, to obtain

\[
\Pr(S_2=e)=\frac3{N^2-1}\bigl(1+O(N^{-1/3})\bigr)
\]

uniformly in the specified forbidden edge \(e\). Finally, the events \(\{S_2=e\}\) over distinct forbidden edges are disjoint, and their union is precisely imperfect coverage. Summing over the \(m_N\) forbidden edges proves the claimed formula, with the \(m_N=0\) case immediate. The stated vacancy and limit consequences follow by algebra. \(\square\)

## Verification

The included standalone `verify.py` uses exact rational dynamic programming on **unoccupied vertex sets** for random-edge greedy adsorption; no approximation or simulation is used for those values. It checks forbidden matchings, paths, and cycles for \(N=6,8,10,12\), including \(P_6=1/3\) for a deleted six-cycle and \(P_6=1/5\) for a deleted perfect matching. It checks a small boundary example with two disjoint deleted triangles. Independently, it enumerates all \(9!=362880\) edge-priority orders for \(K_6\setminus C_6\), finding exactly \(120960\) imperfect outcomes. Command: `python3 verify.py` using Python 3 standard library. This finite evidence checks the stochastic recursion; the uniform infinite-family statement is proved in steps 2–4, not by extrapolating finite tests.

## Relationship to prior work

The random-priority dimer process is the random-edge greedy maximal-matching process. Dyer and Frieze (1991) established foundational results about its performance on general and sparse graph classes; their accessible abstract does not settle the specific dense-host leading constant, but the complete primary text was not available for review. Gamarnik and Goldberg (2008), *Randomized greedy algorithms for independent sets and matchings in regular graphs*, analyze fixed-degree, large-girth graph classes and bounded-host-degree concentration; neither hypothesis captures \(K_N\) with a maximum-degree-two **deleted** graph, whose host degree grows with \(N\). Dietzfelbinger, Peilke and Rink (2012) investigate different greedy heuristics on sparse random graphs. Tang, Wu and Zhang (2019/2020) analyze randomized decision-order and oblivious matching guarantees rather than rare failure on almost-complete fixed graphs.

A narrower previously recorded result establishes the coefficient for the particular case in which the deleted graph is a perfect matching (the cocktail-party graph). That **special case is not presented as new** here. The point of the current theorem is its uniform graph-independent extension to arbitrary unions of paths and cycles, with a shared leading coefficient, including deleted Hamiltonian cycles and arbitrary non-regular forbidden graphs. Searches and comparisons did not identify an equivalent universal statement; this does not prove bibliographic uniqueness.

## Limitations

The theorem requires uniformly sampled allowed-edge priorities and degree at most two in the **forbidden** graph. It does not establish a second-order expansion, nor does it cover unrestricted bounded-degree deletions, independently biased priorities, or other adsorption protocols. The asymptotic error is not numerically optimized. The complete text of Dyer and Frieze (1991) and Pippenger (1989) was inaccessible during the literature comparison; a stronger earlier theorem expressed in different language remains a residual originality risk. The zero-vacancy versus two-vacancy law is specific to this bounded-degree-two complement geometry. No independent scientific audit has been performed.

## References

1. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277, first publicly posted 2008-07-08, https://arxiv.org/html/0807.1277v1.
2. M. E. Dyer and A. M. Frieze, *Randomized greedy matching*, Random Structures & Algorithms **2** (1991), 29–46, doi:10.1002/rsa.3240020104.
3. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. **2** (1989), 393–401, doi:10.1137/0402034.
4. M. Dietzfelbinger, H. Peilke, and M. Rink, *A More Reliable Greedy Heuristic for Maximum Matchings in Sparse Random Graphs*, arXiv:1203.4117, first posted 2012-03-19, https://arxiv.org/pdf/1203.4117.
5. Z. G. Tang, X. Wu, and Y. Zhang, *Towards a Better Understanding of Randomized Greedy Matching*, arXiv:1907.05135, first posted 2019-07-11, https://arxiv.org/pdf/1907.05135.
