# Sharp small-network failures of forward-acquaintance vaccination in directed epidemics

## Finding
Let \(G=(V,E)\) be a finite strongly connected loopless directed graph of order \(n\ge2\). Vaccinate exactly one vertex before a directed, independent-arc Reed–Frost epidemic. With probability \(p\in[0,1]\), each remaining arc independently transmits infection if reached. The initial infected vertex is uniform among the \(n-1\) unvaccinated vertices. Compare uniform vaccination \(U\) with **forward-acquaintance vaccination** \(A\): first choose a uniformly random vertex \(u\), then vaccinate a uniformly random out-neighbor of \(u\). Define \(\Delta_G(p)=\mathbb E_A[X_G(p)]-\mathbb E_U[X_G(p)]\), with larger values indicating a worse expected outbreak under acquaintance vaccination.

**Theorem (two sharp network-scale boundaries).**

1. Every strongly connected directed graph on at most three vertices satisfies \(\Delta_G(p)\le0\) for all \(p\in[0,1]\). On four vertices, exactly one isomorphism class can have \(\Delta_G(p)>0\) for some \(p\). It has seven arcs and is represented by
   \[
   E_4=\{0\to1,\ 0\to2,\ 1\to0,\ 1\to2,\ 1\to3,\ 2\to3,\ 3\to0\}.
   \]
   Its exact gap is
   \[
   \Delta_{G_4}(p)=\frac{p(1-6p-5p^2)}{72},
   \]
   strictly positive **if and only if** \(0<p<(\sqrt{14}-3)/5\). For all other strongly connected four-vertex graphs the gap is nonpositive for every \(p\in[0,1]\). Hence four vertices and seven arcs are sharp for a negative performance comparison at some transmissibility.

2. At full transmissibility \(p=1\), every strongly connected directed graph on at most four vertices satisfies \(\Delta_G(1)\le0\). Five vertices are necessary and sufficient for \(\Delta_G(1)>0\), and among five-vertex examples at least eight arcs are required. Exactly one eight-arc isomorphism class works, represented by
   \[
   E_5=\{0\to1,\ 0\to3,\ 1\to2,\ 1\to3,\ 2\to3,\ 2\to4,\ 3\to1,\ 4\to0\}.
   \]
   For this graph,
   \[
   \Delta_{G_5}(p)=\frac{-18p-24p^2+36p^3+24p^4-6p^5}{240},
   \qquad \Delta_{G_5}(1)=\frac1{20}.
   \]
   In particular the full-transmission expected outbreak size is \(16/5\) under forward-acquaintance vaccination versus \(63/20\) under uniform vaccination. The strict disadvantage also persists for \(p<1\) sufficiently close to one; explicitly \(\Delta_{G_5}(9/10)=46791/4000000>0\).

Both graphs are strongly connected and simple. The classifications and minima are up to directed-graph isomorphism; unlike an undirected contact, an arc and its reverse are distinct.

## Assumptions and scope
The protocol samples a vertex uniformly and then an **outgoing** neighbor uniformly. This is not the same sampling distribution as selecting a uniformly random directed arc, nor as sampling an incoming neighbor. Strong connectivity makes every out-degree positive. A vaccine perfectly removes one vertex and its incident arcs, after which a seed is selected uniformly from those remaining. All directed arcs are independently open with common probability \(p\); the final outbreak is the forward reachable set of the seed in the retained directed graph. All expectations include the vaccination, seed, and percolation randomness. This theorem compares the **mean final outbreak size** and does not compare reproduction-number thresholds or strategic behavior.

## Proof
For a graph \(G\) and vaccinated vertex \(v\), let
\[
 R_v(F)=\sum_{s\in V\setminus\{v\}}\left|\operatorname{Reach}_{(V\setminus\{v\},F)}(s)\right|
\]
for a retained-arc subset \(F\subseteq E\); the reachability set includes \(s\) itself. The expected outbreak size conditioned on \(v,F\) is \(R_v(F)/(n-1)\). By choosing the queried vertex first, the probability that acquaintance vaccination selects \(v\) is
\[
 a_v=\frac1n\sum_{u:\,u\to v}\frac1{d^+(u)},
\qquad\sum_{v\in V}a_v=1.
\]
Uniform vaccination selects every vertex with probability \(1/n\). Consequently
\[
 \Delta_G(p)=\frac1{n-1}\sum_{v\in V}\left(a_v-\frac1n\right)
 \sum_{F\subseteq E}p^{|F|}(1-p)^{|E|-|F|}R_v(F).
\]
Choose a common multiple \(L\) of the positive out-degrees. Put
\[
 b_v=\sum_{u:\,u\to v}\frac L{d^+(u)}-L,
 \quad
 B_k=\sum_{\substack{F\subseteq E\\ |F|=k}}\sum_{v\in V}b_vR_v(F),\quad m=|E|.
\]
Thus the *integer* Bernstein representation is
\[
 \Delta_G(p)=\frac1{nL(n-1)}\sum_{k=0}^m B_kp^k(1-p)^{m-k}.
 \tag{1}
\]
This is an identity over all labeled graphs and all real \(0\le p\le1\), not an approximation.

For a directed simple graph on \(n\) labeled vertices, there are exactly \(2^{n(n-1)}\) arc subsets. Enumerate them all, retain only strongly connected graphs, enumerate every \(F\subseteq E\), compute each \(R_v(F)\) by finite reachability closure, and accumulate the integer \(B_k\) of (1). The complete executable enumerator is supplied as `verify_directed.cpp`; the loops are explicit and do not use graph-isomorphism libraries or randomized tests. It finds \(1,18,1606\) strongly connected labeled graphs respectively at orders \(2,3,4\). At orders two and three every coefficient \(B_k\) is nonpositive. At order four, exactly \(24\) graphs have any positive coefficient; these are exactly the relabelings of \(G_4\), whose automorphism group is trivial. All remaining four-vertex graphs have \(B_k\le0\) for every \(k\), implying \(\Delta_G(p)\le0\) on the full interval. For \(G_4\), taking \(L=6\) gives
\[
 (B_0,\ldots,B_7)=(0,1,0,-20,-60,-75,-44,-10).
\]
Substituting in (1) and expanding yields \(p(1-6p-5p^2)/72\). Its sole positive zero is \((\sqrt{14}-3)/5\); its sign establishes part 1, including all endpoint cases. Because its only exception graph has seven arcs, seven arcs are sharp.

At \(p=1\), only \(F=E\) contributes to (1), so it suffices to calculate
\[
 \Delta_G(1)=\frac{\sum_v b_vR_v(E)}{nL(n-1)}.
\]
The first part rules out positive gaps at orders at most four. Complete enumeration of the \(2^{20}\) directed graphs of order five finds \(565080\) strongly connected labeled graphs, of which \(15180\) have \(\Delta_G(1)>0\). Among those, the minimum arc count is eight; the \(120\) qualifying labeled eight-arc graphs are precisely all relabelings of \(G_5\), again an asymmetric graph. For \(G_5\), the vaccination weights and full-transmission conditional expected sizes, in vertex order \(0,\ldots,4\), are
\[
 (a_v)=\left(\frac15,\frac3{10},\frac1{10},\frac3{10},\frac1{10}\right),\qquad
 (\mathbb E[X\mid v,p=1])=\left(\frac{13}4,\frac52,\frac{11}4,4,\frac{13}4\right).
\]
Taking their scalar product gives \(16/5\), versus their uniform mean \(63/20\), so the gap is \(1/20\). To establish the polynomial formula, take \(L=12\); exhaustive arc-subset enumeration yields
\[
 (B_0,\ldots,B_8)=(0,-18,-150,-486,-786,-660,-252,-12,12),
\]
whose expansion using (1) is the displayed degree-five polynomial. The rational evaluation at \(p=9/10\) proves a strict interior counterexample. This establishes part 2.

The enumeration certifies only the finite vertex-order and arc-count assertions just made. Neither a general optimality theorem nor a statement about arbitrary large directed networks is inferred.

## Verification
Compile and run the self-contained certificate using `g++ -O3 -std=c++17 verify_directed.cpp -o verify_directed && ./verify_directed`. It checks the exact Bernstein and power-basis coefficients of the two witnesses, the two full-transmission gaps, every strongly connected labeled directed graph through order four, all exceptional isomorphism orbits, and all strongly connected labeled directed graphs of order five for the full-transmission minimum. The program prints `PASS` only after all assertions succeed. Its exact integer reachability closure and binomial expansion are specified in the source. No floating-point numerical experiment is used in the proof.

## Relationship to prior work
Cohen, Havlin, and ben-Avraham (first public preprint July 2002) introduced acquaintance immunization as a local alternative to uniform or degree-targeted immunization, focusing on degree-heterogeneous and mostly undirected network models, including SIR epidemic thresholds. Their analysis does **not** provide the sharp finite directed-network comparisons of one-vaccine final outbreak expectations above. Allard and colleagues (2023) explain that in directed epidemic graphs, out-neighbor and predecessor sampling favor different combinations of infection risk and onward spread; their analyses of directed network structure and outbreak risk do not establish these smallest-order exact classifications. A directed friendship-paradox analysis by the authors of arXiv:1905.05286 studies degree and opinion-prevalence sampling biases rather than this particular vaccination/outbreak performance criterion. The broader conceptual warning about directionality is prior knowledge; the present mathematical statement is the exact order-four and saturated order-five boundary with explicit polynomials and exhaustive proofs.

## Limitations
This is a one-vaccine, one-initial-infection Reed–Frost/percolation calculation for finite, strongly connected directed graphs, assuming exchangeable arc transmissibility, no partial immunity, and no later interventions. One out-neighbor of a uniformly chosen vertex is the specified acquaintance rule. A uniform seed is drawn **after** vaccination. The statement does not apply without modification to undirected sampling, selection proportional to degree, alternate seed distributions, multiple simultaneous vaccines, correlated transmissions, repeated contacts, or any large-network asymptotic criterion. The finite classification is dependent on the included exact enumerator; independent audit and wider bibliographic verification have not occurred.

## References
- R. Cohen, S. Havlin, D. ben-Avraham, *Efficient Immunization Strategies for Computer Networks and Populations*, arXiv:cond-mat/0207387 (first submitted 2002-07-16), published in *Physical Review Letters* 91, 247901 (2003), https://arxiv.org/abs/cond-mat/0207387.
- A. Allard, C. Moore, S. V. Scarpino, B. M. Althouse, L. Hébert-Dufresne, *The Role of Directionality, Heterogeneity, and Correlations in Epidemic Risk and Spread*, *SIAM Review* 65 (2023), 471–492, https://doi.org/10.1137/20M1383811.
- *Friendship Paradox Biases Perceptions in Directed Networks*, arXiv:1905.05286 (2019), https://arxiv.org/abs/1905.05286.
