# Three natural-isometry classes of optimal two-use \(C_7\) zero-error codes
## Finding
Let \(C_7\) have vertex set \(\mathbb Z/7\mathbb Z\), with two symbols confusable exactly when they are equal or adjacent on the cycle. A block-length-two zero-error code is therefore an independent set of \(C_7^{\boxtimes 2}\). Let
\[
G=(D_{14}\times D_{14})\rtimes S_2
\]
act by independent rotations/reflections in the two coordinates and by interchanging the coordinates.

Every optimal two-use code has ten words. The 980 labeled optimal codes form exactly three \(G\)-orbits, of sizes \(392\), \(196\), and \(392\). Their stabilizer orders are \(1\), \(2\), and \(1\), respectively. Canonical representatives are
\[
\begin{aligned}
A=&\,\{(0,0),(0,2),(1,4),(2,0),(2,2),(3,4),(4,1),(4,6),(5,3),(6,5)\},\\
B=&\,\{(0,0),(0,2),(1,4),(2,0),(3,2),(3,4),(4,6),(5,1),(5,3),(6,5)\},\\
C=&\,\{(0,0),(0,2),(1,4),(2,1),(2,6),(3,3),(4,0),(4,5),(5,2),(6,4)\}.
\end{aligned}
\]

For a pair of codewords, sort the two cyclic coordinate distances and count the resulting types. The signatures of \(A,B,C\) are
\[
\begin{aligned}
A:&\ \{02{:}6,12{:}14,13{:}12,22{:}2,23{:}6,33{:}5\},\\
B:&\ \{02{:}5,03{:}1,12{:}15,13{:}11,22{:}2,23{:}6,33{:}5\},\\
C:&\ \{02{:}5,03{:}1,12{:}16,13{:}10,22{:}1,23{:}7,33{:}5\}.
\end{aligned}
\]
These histograms are invariant under \(G\) and distinguish the three classes.

## Assumptions and scope
The claim concerns the finite graph \(C_7^{\boxtimes 2}\) and the explicitly defined 392-element natural channel-isometry group \(G\). It does not assert that this group has been independently identified here with the full abstract automorphism group of the strong square. The classification is of maximum independent sets, equivalently optimal two-use zero-error codes, under this stated natural equivalence.

The structured source date is 1994-08-07, the earliest fully day-resolved inspected public source carrying primary MSC \(94A15\) for graph Shannon-capacity work. Hales' direct odd-cycle product theorem is older and was inspected in full, but the inspected publication metadata resolves it only to October 1973; no day has been invented for that article.

## Proof
Construct the compatibility graph on the 49 ordered pairs in \((\mathbb Z/7\mathbb Z)^2\): two distinct pairs are compatible when at least one coordinate has cyclic distance at least two. Cliques in this compatibility graph are exactly zero-error codes.

The included verifier performs a complete recursive clique enumeration. It finds no clique of size eleven and exactly 980 cliques of size ten. Thus the finite search independently establishes the maximum ten and exhausts every equality case. The size-ten count also matches the leading coefficient \(980\) in the exact independence polynomial published by Hildebrant.

The verifier then constructs all 392 maps in \((D_{14}\times D_{14})\rtimes S_2\), applies every map to every maximum code, and canonicalizes each orbit. Exactly three canonical classes remain. Their computed orbit sizes are \(392,196,392\); direct stabilizer counts are \(1,2,1\), and in every case orbit size times stabilizer order equals 392. The three distance-pair histograms above are recomputed directly from the representatives and are pairwise distinct.

## Verification
Run `python3 verify.py` with the standard Python library. The packaged replay returns:

`VERIFY_OK vertices=49 target11=0 maximum=10 labeled_maxima=980 group=392 orbits=3 orbit_sizes=392,196,392 stabilizers=1,2,1 nodes11=266991 nodes10=432900 census_sha256=7bedb501045012255db706cd7e32facf1e07891edeac480c48a721885fb0e3ab`

The verifier rebuilds the graph, enumeration, group action, orbit partition, stabilizers, representatives, signatures, and census digest from definitions; it does not consume a precomputed list of maximum codes.

## Relationship to prior work
Hales proved the exact independence number for the strong product of two odd cycles; specializing his theorem gives \(\alpha(C_7^{\boxtimes 2})=10\). Korže and Vesel restate that formula in a later full-text treatment motivated by zero-error information theory. Jurkiewicz studies greedy construction of maximum independent sets for this exact strong square, again using the known value ten.

Hildebrant computes the exact independence polynomial of \(C_7^{\boxtimes 2}\); its leading coefficient is \(980\), so the number of labeled maximum codes is already known. The orbit decomposition in that paper's appendix concerns the 29 independent sets of the base graph \(C_7\) under \(D_{14}\), not the 980 maximum independent sets of the strong square under \((D_{14}\times D_{14})\rtimes S_2\). Thus the present result is a symmetry classification of the already-counted extremizers, not a claim to rediscover either the optimum ten or the count 980.

## Limitations
This is a finite equality classification for two channel uses only; it gives no new value for the Shannon capacity \(\Theta(C_7)\). The natural isometry group is defined explicitly rather than identified here with every possible abstract automorphism. The 1974 Sonnemann--Krafft paper is a plausible historical source on the odd-cycle product formula whose full text was not inspected; the accessible later primary literature attributes to it the independence-number formula, not an equality-case orbit classification. An obscure unindexed historical classification remains the principal originality risk.

## References
1. R. S. Hales, “Numerical invariants and the strong product of graphs,” *Journal of Combinatorial Theory, Series B* 15 (1973), 146–155. DOI 10.1016/0095-8956(73)90014-2.
2. K. Marton, “On the Shannon capacity of probabilistic graphs,” *Journal of Combinatorial Theory, Series B*. DOI 10.1006/JCTB.1993.1015. Public metadata gives 1994-08-07 and primary MSC 94A15.
3. D. Korže and A. Vesel, “A Note on the Independence Number of Strong Products of Odd Cycles,” *Ars Combinatoria* 106 (2012), 473–481, published 2012-07-31.
4. M. Jurkiewicz, “On zero-error codes produced by greedy algorithms,” *Journal of Combinatorial Optimization* 44 (2022), 2963–2980, published online 2021-11-02. DOI 10.1007/s10878-021-00825-y.
5. T. Hildebrant, “Transfer Operators and Independence Polynomials for Strong Powers of Circulant Graphs,” arXiv:2604.14416v1, 2026-04-15.
