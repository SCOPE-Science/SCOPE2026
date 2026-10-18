# Full \(\mathfrak S_6\) homology character of the six-vertex domination complex

## Finding
Let \(D_{6,3}\) be the complex of graphs on six labeled vertices whose domination number is at least three, regarded as a simplicial complex with graph edges as vertices. Relabeling the underlying six vertices acts on its reduced rational homology. If \(S^{\lambda}\) denotes the rational irreducible Specht module indexed by the partition \(\lambda\vdash6\), then
\[
\begin{aligned}
\widetilde H_4(D_{6,3};\mathbb Q)\cong{}&S^{(5,1)}\oplus2S^{(4,2)}\oplus S^{(4,1,1)}\oplus S^{(3,3)}\\
&\oplus3S^{(3,2,1)}\oplus S^{(3,1,1,1)}\oplus S^{(2,2,2)}\\
&\oplus S^{(2,2,1,1)}\oplus S^{(2,1,1,1,1)},\\
\widetilde H_5(D_{6,3};\mathbb Q)\cong{}&S^{(5,1)}\oplus S^{(4,2)}\oplus S^{(4,1,1)}.
\end{aligned}
\]
All other reduced rational homology vanishes. Thus the degree-four homology contains **every non-one-dimensional irreducible rational \(\mathfrak S_6\)-representation**; neither graded group contains the trivial or sign representation. In particular, both \(|D_{6,3}|/\mathfrak S_6\) and \(|D_{6,3}|/\mathfrak A_6\) are rationally acyclic.

The complete graded character, on conjugacy classes indexed by the cycle type of the relabeling permutation, is:

| Cycle type | Trace on \(\widetilde H_4\) | Trace on \(\widetilde H_5\) |
| --- | ---: | ---: |
| \((1^6)\) | 115 | 24 |
| \((2,1^4)\) | 3 | 8 |
| \((2^2,1^2)\) | 3 | 0 |
| \((2^3)\) | 3 | 0 |
| \((3,1^3)\) | -2 | 3 |
| \((3^2)\) | -2 | 0 |
| \((3,2,1)\) | 0 | -1 |
| \((4,1^2)\) | -1 | 0 |
| \((4,2)\) | -1 | 0 |
| \((5,1)\) | 0 | -1 |
| \((6)\) | 0 | 0 |

## Assumptions and scope
A graph has fixed labeled vertex set \(\{0,1,2,3,4,5\}\), including isolated vertices; it is simple, undirected, and has no loops. A subset \(T\) dominates the graph if every vertex outside \(T\) is adjacent to at least one vertex of \(T\). The domination number \(\gamma(G)\) is the smallest cardinality of a dominating set. A \(d\)-simplex of \(D_{6,3}\) is an edge set \(E\subseteq E(K_6)\) of cardinality \(d+1\) satisfying \(\gamma(([6],E))\ge3\). All group actions use the signed orientation induced by increasing lexicographic edge order.

This is one specific finite graph complex and its **rational** graded representation. The already known nonequivariant homotopy type \(\bigvee^{115}S^4\vee\bigvee^{24}S^5\) is used as an input, not asserted as a new result. In particular, its integral reduced homology is free and is concentrated in degrees four and five.

## Proof
**1. Reconstruct the complex.** Every dominating singleton extends to a dominating pair. Thus \(\gamma(G)\ge3\) exactly when none of the \(\binom62=15\) vertex pairs dominates \(G\). There are \(2^{15}\) candidate edge sets. Testing this criterion exhaustively gives \(4503\) faces including the empty face, and counts by simplicial degree \(-1,0,1,2,3,4,5,6\) of
\[
(1,15,105,455,1185,1647,915,180).
\]
The full reduced chain complex independently has boundary ranks \((1,14,91,364,821,711,180)\) in degrees \(0\) through \(6\) over each of the two primes used below; hence its reduced Betti dimensions are \(115\) in degree four and \(24\) in degree five. Freeness over the integers follows from the cited prior sphere-wedge theorem, not from modular ranks alone.

**2. Invariant chain bases.** Fix a permutation \(g\in\mathfrak S_6\) of order \(m\). Since both computational primes are coprime to \(m\), averaging by
\[
 e_g=\frac1m\sum_{j=0}^{m-1}g^j
\]
projects simplicial chains to the \(\langle g\rangle\)-invariant subcomplex. Orient each nonempty simplex by the lexicographic order of its graph edges; the empty simplex has the usual reduced-chain orientation. Every cyclic orbit of faces either gives one invariant chain (when its stabilizer acts orientation-preservingly) or none (when some stabilizer reverses orientation). The invariant boundary of an averaged oriented orbit representative is obtained by deleting each edge with its simplicial incidence sign, then converting each resulting face into its oriented orbit representative. This produces a finite integer matrix for every boundary map. The included program implements this definition directly, checks \(\partial^2=0\), and reports all chain dimensions and ranks.

**3. Exact identification of rational invariant dimensions.** The prior integral sphere-wedge theorem makes \(H_*(D_{6,3};\mathbb Z)\) torsion-free. For any prime \(p\nmid m\), localization at \(p\) makes \(e_g\) an idempotent on a finite free module, splitting that module into its invariant image and complementary kernel. Reduction modulo \(p\) preserves the ranks of these direct summands. Consequently the invariant homology dimensions computed from averaged simplicial chains over \(\mathbb F_p\) equal those over \(\mathbb Q\), not merely lower bounds for them. The program computes independent modular ranks for \(p=2147483647\) and \(p=1000000007\); both give the same complete output.

For the eleven cycle types in the order of the character table above, the computed pairs
\(\big(\dim\widetilde H_4^{\langle g\rangle},\dim\widetilde H_5^{\langle g\rangle}\big)\) are
\[
(115,24),(59,16),(59,12),(59,12),(37,10),(37,8),
(19,6),(29,6),(29,6),(23,4),(19,4).
\]
For each degree and each element of order \(m\), these invariants satisfy
\[
 m\,\dim\widetilde H_d^{\langle g\rangle}
 =\sum_{j=0}^{m-1}\operatorname{tr}\big(g^j\mid\widetilde H_d\big).
\]
Proceeding from lower-order power classes to the desired class recovers precisely the eleven character pairs displayed in the finding.

**4. Irreducible decomposition and independent check.** For a partition \(\lambda\vdash6\), write \(\ell=\ell(\lambda)\). The Frobenius alternant coefficient formula gives the irreducible character on cycle type \(\mu\vdash6\) as
\[
\chi^{\lambda}(\mu)=
\left[x_1^{\lambda_1+\ell-1}x_2^{\lambda_2+\ell-2}\cdots x_{\ell}^{\lambda_{\ell}}\right]
\prod_{i<j}(x_i-x_j)\prod_{r\in\mu}\left(\sum_{i=1}^{\ell}x_i^r\right).
\]
The program independently builds this integer character table from the coefficient formula and verifies orthogonality. Scalar products with the computed degree-four and degree-five characters give the two Specht decompositions in the finding. A separate signed Lefschetz check directly enumerates all fixed oriented simplices for every conjugacy class and verifies that their reduced alternating chain trace equals the degree-four trace minus the degree-five trace in all eleven cases.

**5. Quotient consequence.** Neither displayed decomposition contains \(S^{(6)}\) or \(S^{(1^6)}\). Thus there are no invariants under \(\mathfrak S_6\), nor under its index-two alternating subgroup (the latter invariants would come from precisely those two linear characters). For a finite group acting on a finite simplicial complex, rational homology of the topological quotient equals its invariant rational homology, after taking an admissible barycentric subdivision. Both asserted quotients therefore have zero reduced rational homology in every degree.

## Verification
Run `python3 artifacts/verify.py` with Python 3 and the standard library. It constructs all faces independently of stored arrays, forms eleven cyclic invariant chain complexes, checks their differential identities, computes boundary ranks over two large primes, recovers character values by power sums, evaluates the Frobenius alternant, checks the full Specht-character orthogonality relations, and independently performs signed Lefschetz tests. Its printed JSON output must agree with `artifacts/verification_output.json` and conclude with `D63_SYMMETRY_VERIFY_OK`. The observed counts, ranks, class table, and constituent multiplicities are fully recorded there.

## Relationship to prior work
González and Hoekstra-Mendoza (first public arXiv version 2019-01-22) introduced the complexes \(D_{n,k}\), proved the sphere-wedge theorem for \(k=n-2\), and singled out \(D_{6,3}\) by its Euler characteristic. A subsequent published finite classification already established \(D_{6,3}\simeq\bigvee^{115}S^4\vee\bigvee^{24}S^5\); that homotopy type and its integral freeness are explicitly used here as prior inputs. Neither source provides the present action of \(\mathfrak S_6\) on both rational homology groups.

A published stable Specht formula for \(\widetilde H_2(D_{n,n-2};\mathbb Q)\) concerns the different domination threshold \(n-2\) (equal to four at \(n=6\)), rather than \(D_{6,3}\), and does not imply these degree-four and degree-five characters. A separate published computation for \(D_{7,4}\) concerns a different vertex count and supplies its nonequivariant homotopy type only. Searches for equivariant, cyclic-orbit, quotient and Specht reformulations of the present six-vertex claim did not locate a stronger covering statement. In particular, the characters are not determined by nonequivariant Betti numbers or Euler characteristics alone.

## Limitations
This is a rational representation-theoretic classification for one finite complex; it is not a result about integral \(\mathbb Z[\mathfrak S_6]\)-lattices, modular composition factors, or a uniform decomposition for arbitrary \(D_{n,k}\). The modular computation becomes an exact rational statement because it uses the previously established integral sphere-wedge theorem and the elementary prime-to-order averaging argument. A finite search and a database query cannot guarantee absence of an unindexed equivalent theorem. No independent audit of the present character calculation has been performed.

## References
1. J. González and T. I. Hoekstra-Mendoza, *On the homotopy type of complexes of graphs with bounded domination number*, arXiv:1901.07130, first posted 2019-01-22, subsequently *Contributions to Discrete Mathematics* 16 (2021), DOI 10.55016/ojs/cdm.v16i3.72114.
2. *A mixed-dimensional sphere wedge for \(D_{6,3}\)*, published mathematical result, 2026-10-04, published-finding corpus record identifier `55d89ec4bab2` (complete homotopy classification; used as an input).
3. *Stable Specht decomposition of \(\widetilde H_2(D_{n,n-2};\mathbb Q)\)*, published mathematical result, 2026-10-11, published-finding corpus record identifier `ab4fa03abdf7` (different domination threshold).
4. *The domination complex \(D_{7,4}\) is \(\bigvee^{811}S^4\vee\bigvee^{84}S^5\)*, published mathematical result, 2026-10-11, published-finding corpus record identifier `e4e894a65756` (different labeled vertex set).
