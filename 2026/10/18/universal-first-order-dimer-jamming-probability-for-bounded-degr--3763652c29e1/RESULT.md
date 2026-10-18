# Universal first-order dimer jamming with bounded-degree bipartite defects

## Finding

Fix a positive integer \(\Delta\). For a bipartite forbidden graph \(H_n\subseteq K_{n,n}\) with maximum degree at most \(\Delta\), write \(m_n\) for its number of edges. Process the allowed edges of \(K_{n,n}\setminus H_n\) in uniformly random order, accepting each whenever both incident vertices remain unoccupied. Let \(P_n(H_n)\) be the probability that the terminal matching is not perfect. For every nonempty \(H_n\), uniformly as \(n\to\infty\),

\[
P_n(H_n)=\frac{2m_n}{n(n+1)}\bigl(1+O_{\Delta}(n^{-1/3})\bigr).
\]

If \(m_n=0\), then \(P_n(H_n)=0\) exactly. In particular, whenever \(m_n/n\to c\), the limiting rare-jamming constant exists and equals \(\lim_{n\to\infty}nP_n(H_n)=2c\). This is a uniform structural universality statement: the first-order failure probability depends on the count, not the arrangement, of forbidden placements.

## Assumptions and scope

The vertex sets \(L_n,R_n\) are disjoint and have exactly \(n\) labeled sites each. The forbidden graph \(H_n\) is simple, is supported only between the two sides, and has maximum degree bounded by a constant \(\Delta\) independent of \(n\). Priorities on allowed edges are independent continuous random variables with a common distribution. Equivalently, at each successful step the next accepted edge is uniformly chosen from those joining currently unoccupied sites. Both sides always have the same number \(k\) of vacant vertices; this is called stage \(k\). The event of failure is a non-perfect terminal matching, not an inability of the substrate to admit a perfect matching: for \(n>2\Delta\), Hall's condition ensures the allowed graph has a perfect matching.

The \(O_{\Delta}\) error may depend on the fixed degree bound but not on \(n\), the number \(m_n>0\), or the arrangement of forbidden edges. The theorem is asymptotic, rather than an exact probability identity for every finite graph.

## Proof

**1. Residual dynamics.** At stage \(k\), let \(F\) be the forbidden edges with both endpoints still vacant, let \(e=|F|\), and let \(d_u,d_v\) be the degrees in \(F\) of any currently vacant vertices \(u\in L_n\), \(v\in R_n\). Necessarily \(e\le\Delta k\). If \(k>\Delta\), every vacant left vertex has at least one allowed vacant right neighbor. Hence the process cannot terminate before stage \(\Delta\). Uniform residual priorities imply that the next accepted edge is uniformly chosen from the \(k^2-e\) allowed vacant pairs.

**2. Survival of marked sites.** Fix any set of \(a\) left and \(b\) right vertices, with \(a+b\) fixed independently of \(n\). Conditional on all its vertices still vacant at stage \(k\), its probability of surviving the next adsorption is

\[
\frac{(k-a)(k-b)-e_{\mathrm{out}}}{k^2-e},
\]

where \(e_{\mathrm{out}}\) counts forbidden edges entirely outside the marked set. Since only at most \(\Delta(a+b)\) forbidden edges touch marked vertices, the ratio of this probability to \((1-a/k)(1-b/k)\) is \(1+O_{\Delta,a,b}(k^{-2})\) for all sufficiently large \(k\). Multiplication over stages from \(n\) down to any \(K\ge K_0(\Delta,a,b)\) gives

\[
\Pr(\text{all marked vertices vacant at stage }K)
=\frac{(K)_a(K)_b}{(n)_a(n)_b}
\left(1+O_{\Delta,a,b}(K^{-1})\right),
\]

where \((k)_a=k(k-1)\cdots(k-a+1)\). In particular the probability is \(O_{\Delta,a,b}((K/n)^{a+b})\), and the same bound holds for a fixed sufficiently large endpoint stage \(K_0\).

**3. One forbidden pair.** Mark a forbidden edge \(f=(u,v)\). If its endpoints survive at stage \(k\), the exact probability that both survive the next step is

\[
 s_k=\frac{(k-1)^2-(e-d_u-d_v+1)}{k^2-e}.
\]

For the graph with just this one forbidden edge, this reduces to \(s_k^{(1)}=(k-1)/(k+1)\). Using \(e\le\Delta k\) and \(d_u,d_v\le\Delta\), direct subtraction gives \(s_k/s_k^{(1)}=1+O_\Delta(k^{-2})\) uniformly when \(k\) exceeds a constant depending on \(\Delta\). Thus, with \(S_f(K)\) denoting the survival of both endpoints to stage \(K\),

\[
 \Pr(S_f(K))=\frac{K(K+1)}{n(n+1)}
 \left(1+O_\Delta(K^{-1})\right).
\]

When no other forbidden edge remains at stage \(K\), the conditional chance that \(f\) is the final unoccupied pair is exactly \(2/[K(K+1)]\), by telescoping the factors \((k-1)/(k+1)\). Even if other forbidden edges remain at \(K\), the chance that the marked pair stays vacant to termination is at most \(C_\Delta/K^2\): the process must reach a fixed stage \(K_0>\Delta\) before stopping, and the same uniform survival-product bound applies down to \(K_0\).

**4. Multiple marked forbidden pairs are negligible.** Choose \(K=\lfloor n^{1/3}\rfloor\). Given \(S_f(K)\), the conditional probability that another forbidden edge also has both endpoints vacant is

\[
 O_\Delta\!\left(\frac Kn+\frac{m_nK^2}{n^2}\right)
 =O_\Delta(n^{-1/3}).
\]

Indeed, at most \(2(\Delta-1)\) other edges share an endpoint with \(f\), and each costs a third marked survivor, giving conditional probability \(O_\Delta(K/n)\); at most \(m_n\le\Delta n\) disjoint edges remain to consider, and each costs two additional marked survivors, giving \(O_\Delta((K/n)^2)\). The joint-survival bound from step 2 justifies these estimates without independence assumptions. Splitting according to whether another forbidden edge survives at stage \(K\), and applying the tail estimates in step 3, yields uniformly for each forbidden edge \(f\),

\[
\Pr(f\text{ has both endpoints vacant at termination})
=\frac{2}{n(n+1)}\bigl(1+O_\Delta(n^{-1/3})\bigr).
\]

**5. Convert the first moment to jamming probability.** At termination, if \(k\) vertices remain vacant on either side, then all \(k^2\) pairs between the two vacancy sets must be forbidden. In particular \(k\le\Delta\). Let \(J\) be the number of forbidden edges whose endpoints are both vacant at termination; then \(J=0\) for a perfect matching and \(J=k^2\) otherwise. The desired failure probability is \(\Pr(J\ge1)\). For any fixed \(k\ge2\), the maximum-degree condition permits only \(O_\Delta(n)\) labeled forbidden copies of \(K_{k,k}\): choose one left vertex, all \(k\) right neighbors, and the other \(k-1\) left common neighbors. Each copy's \(2k\) vertices survive to fixed stage \(K_0>\Delta\) with probability \(O_\Delta(n^{-2k})\) by step 2. Hence

\[
\Pr(\text{terminal }k\ge2)=O_\Delta(n^{-3}),
\qquad
|\mathbb E J-P_n(H_n)|=O_\Delta(n^{-3}).
\]

Summing step 4 over the \(m_n\) forbidden edges gives \(\mathbb E J=2m_n/[n(n+1)]\,(1+O_\Delta(n^{-1/3}))\). Since \(m_n\ge1\), the remaining additive \(O_\Delta(n^{-3})\) error is absorbed into the claimed relative bound. This proves the theorem.

For completeness, Hall's theorem applies whenever \(n>2\Delta\). If a nonempty left subset \(X\) has size at most \(n-\Delta\), any of its vertices has at least \(n-\Delta\) allowed neighbors. If \(|X|>n-\Delta\), any right vertex absent from \(N(X)\) would have \(|X|>\Delta\) forbidden left neighbors, contradicting the degree bound. Therefore \(|N(X)|\ge|X|\) always.

## Verification

The included Python 3 program `verify.py` computes exact rational failure probabilities using the vacancy-mask Markov chain. It verifies for each \(2\le n\le8\) the one-defect identity \(P_n=2/[n(n+1)]\), and evaluates matching-, path-, and cycle-shaped forbidden families on the same range. For three examples on \(K_{3,3}\), a second implementation explicitly enumerates all orders of allowed edges and agrees with the Markov-chain value. All 31 exact checks passed. These checks corroborate the local counting model; the uniform infinite-family error bound is proved analytically above, not by finite enumeration.

## Relationship to prior work

Random sequential adsorption and random greedy graph matchings are classical; see Pippenger (1989), Dyer and Frieze (1991), and the later general analysis by Bennett and Bohman, first circulated on 12 October 2012. The Bennett–Bohman theorem controls an unsaturated fraction for regular high-degree hypergraphs; it does not give the rare failure probability or the coefficient \(2m_n/[n(n+1)]\) for arbitrary bounded-degree defects. Dyer–Frieze analyze the random-edge greedy algorithm and derive worst-case and sparse-family approximation guarantees; their accessible abstract does not address this dense rare-jamming asymptotic. The entire Dyer–Frieze text was not available for a decisive whole-paper noncoverage check. Pippenger's abstract discusses general edge adsorption but emphasizes graphs with few short cycles; its full text was also not available, leaving residual bibliographic uncertainty. Earlier finite-model calculations establish the matching-deletion special case and a different unipartite deletion theorem; neither implies arrangement universality for arbitrary bipartite degree-bounded defects.

## Limitations

The fixed degree bound is essential to the present proof; allowing \(\Delta\) to grow with \(n\) is not covered. The error exponent \(1/3\) is a proved uniform rate, not claimed optimal. The result does not describe the conditional distribution of the rare terminal defects, the entire deposition history, or forbidden graphs with macroscopic complete rectangles. No independent external audit has been performed. Possible unindexed earlier work on rare failures of dense random greedy matchings remains a bibliographic risk.

## References

1. N. Pippenger, “Random Sequential Adsorption on Graphs,” SIAM Journal on Discrete Mathematics 2 (1989), 393–401, DOI 10.1137/0402034.
2. M. Dyer and A. Frieze, “Randomized Greedy Matching,” Random Structures & Algorithms 2 (1991), 29–45, DOI 10.1002/rsa.3240020104.
3. P. Bennett and T. Bohman, “A natural barrier in random greedy hypergraph matching,” arXiv:1210.3581, initially submitted 12 October 2012; later published in Combinatorics, Probability and Computing 28 (2019), 816–825.
