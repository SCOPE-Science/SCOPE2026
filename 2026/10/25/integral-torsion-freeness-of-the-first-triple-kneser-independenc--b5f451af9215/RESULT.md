# Integral torsion-freeness of the first triple-Kneser independence complex

## Finding

Let \(\mathrm{KG}(3,1)\) have as vertices the \(35\) three-element subsets of \([7]=\{1,\ldots,7\}\), with an edge between disjoint subsets. Write \(X=\operatorname{Ind}(\mathrm{KG}(3,1))\), so a simplex is a pairwise-intersecting family of triples of \([7]\). Then \(X\) is \(5\)-connected and its **complete reduced integral homology** is
\[
\widetilde H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{29},&i=6,\\
\mathbb Z^{7},&i=9,\\
0,&i\notin\{6,9\}.
\end{cases}
\]
In particular, it has no integral homology torsion in any degree. This settles the first nontrivial parameter \(k=1\) of the integral torsion-freeness question posed for \(\operatorname{Ind}(\mathrm{KG}(3,k))\) in arXiv:2610.17394, Question 19. It does **not** assert a wedge-of-spheres homotopy type.

A useful structural refinement is \(X\simeq S^9\vee\Sigma L\), where \(L\) is the complex of pairwise-intersecting families of triples of \([6]\) for which some subset of \([6]\) of size at most two meets every triple. Here \(L\) is \(4\)-connected, with \(\widetilde H_5(L;\mathbb Z)\cong\mathbb Z^{29}\), \(\widetilde H_8(L;\mathbb Z)\cong\mathbb Z^{6}\), and no other reduced integral homology.

## Assumptions and scope

All complexes are finite abstract simplicial complexes with their geometric realizations understood in homotopy statements. A Kneser vertex is a three-subset, not an element of the seven-point ground set. Homology uses the standard oriented simplicial boundary over \(\mathbb Z\). The suspension \(\Sigma\) is unreduced; for connected \(L\) it gives the usual reduced-homology shift. No conclusion is asserted for \(k\ge2\), for \(\mathrm{KG}(n,k)\) with \(n\ne3\), or for integral symmetry representations.

## Proof

**1. Topological reduction.** For \(m=6,7\), let \(X_m\) be the complex of pairwise-intersecting families of triples of \([m]\). The twenty triples of \([6]\) form ten complementary pairs; within \([6]\), two triples are disjoint if and only if they are complementary. Thus \(X_6\) is a join of ten zero-spheres, hence \(X_6\cong S^9\).

In \(X_7\), let \(U\) be the union of the closed simplicial stars of the triples containing the point \(7\). Those triples form a simplex; their star cluster \(U\) is contractible by the star-cluster theorem (or by the corresponding lemma in Feng, arXiv:2610.17394, §3.2). The union \(X_7=X_6\cup U\) has intersection \(L=X_6\cap U\). A face \(F\subset X_6\) is in this intersection exactly when some pair \(\{a,b\}\subset[6]\) intersects every triple in \(F\), which proves the asserted definition of \(L\).

The concentration map \(X_7\longrightarrow X_6\) fixes triples not containing \(7\), and sends \(\{7,a,b\}\) to the triple obtained by replacing \(7\) by the least element of \([6]\setminus\{a,b\}\). It is simplicial: if two triples already meet outside \(7\), their images still meet; if they meet only at \(7\), then their two-element remainders are disjoint, and either one of the added least elements lies in the other remainder or both added least elements coincide. Hence this is a retraction. Since \(L\hookrightarrow X_7\) factors through the contractible \(U\), the composite \(L\hookrightarrow X_7\to X_6\), which equals \(L\hookrightarrow X_6\), is null-homotopic. The cofibration pushout gives \(X_7\simeq X_6\vee\Sigma L\), since \(L\) is connected by the next step.

**2. Complete finite enumeration of \(L\).** Order the twenty triples of \([6]\) lexicographically and label them \(0,\ldots,19\). Partition them into ten complementary pairs. A family is pairwise intersecting if and only if it chooses at most one member from each pair. Consequently exactly \(3^{10}\) choices, including empty, are available before enforcing the two-point transversal condition. For every nonempty choice check the fifteen pairs of points in \([6]\): it belongs to \(L\) exactly when at least one pair intersects every selected triple. This exhausts all faces and gives \(54,870\) nonempty faces, with the face vector by dimensions \(0,\ldots,9\):
\[
(20,180,960,3360,8064,13410,14640,9900,3740,596).
\]

**3. Acyclic integral Morse reduction.** Start with all nonempty faces unmatched. For each triple-vertex \(v=0,1,\ldots,19\), match every still-unmatched face \(F\) not containing \(v\) to \(F\cup\{v\}\), if both faces remain unmatched. Process potential lower faces first by increasing cardinality and then by binary face mask. A fully exhaustive directed-Hasse verification orients paired cover relations upward and all others downward. The directed graph has \(54,870\) vertices, \(358,760\) covering arrows and admits a topological sort through all vertices, so the matching is acyclic. It contains \(27,398\) pairs and has critical cells: one of dimension zero; \(42\) of dimension five; \(19\) of dimension six; six of dimension seven; and six of dimension eight. Therefore \(L\) has a CW model with a single zero-cell and no cells in dimensions one through four, proving \(4\)-connectivity.

**4. Integral Morse differential.** Fix ascending-vertex orientations. For any matched pair \(F\subset G=F\cup\{v\}\), the coefficient of \(F\) in \(\partial G\) is \(\pm1\). In the algebraic Morse reduction solve this boundary relation for \(F\), recursively substituting the other codimension-one faces of \(G\); the verified acyclic directed graph guarantees termination. This is precisely the integral chain contraction induced by the matching. The resulting critical-cell differential has matrices \(\partial_6: \mathbb Z^{19}\to\mathbb Z^{42}\), \(\partial_7:\mathbb Z^6\to\mathbb Z^{19}\), and \(\partial_8:\mathbb Z^6\to\mathbb Z^6\). Their exact nonzero Smith invariants are
\[
\partial_6:\underbrace{1,\ldots,1}_{13},\qquad
\partial_7:\underbrace{1,\ldots,1}_{6},\qquad
\partial_8:0.
\]
The first two matrices have respectively \(186\) and \(40\) nonzero entries, all \(\pm1\); the third is zero. For each matrix, the verifier applies only unimodular integer row and column operations with unit pivots, and checks that the final residual block vanishes. It also checks \(\partial_6\partial_7=\partial_7\partial_8=0\) entrywise. Thus both nonzero images are saturated, and the Morse complex has precisely \(\widetilde H_5(L;\mathbb Z)=\mathbb Z^{42-13}=\mathbb Z^{29}\) and \(\widetilde H_8(L;\mathbb Z)=\mathbb Z^6\), with no other reduced homology and no torsion.

**5. Reassemble \(X_7\).** From \(X_7\simeq S^9\vee\Sigma L\), the nonzero reduced groups are in degrees six and nine; degree six has rank \(29\), and degree nine has rank \(1+6=7\). The decomposition and the \(4\)-connectivity of \(L\) give \(5\)-connectivity of \(X_7\). This proves the claim.

## Verification

Run `python3 verify_morse.py` and `python3 independent_mod2.py` with Python 3 (standard library only). The first re-enumerates all faces, constructs every matched pair, checks every directed Hasse arrow for acyclicity, computes the full integer Morse boundary through signed gradient-path elimination, and performs unimodular unit-pivot reductions. The second independently constructs the same complex by recursive clique enumeration and directly computes its mod-two boundary ranks without using the Morse matching. Files `verify_morse_output.txt` and `independent_mod2_output.txt` contain actual outputs. Both scripts terminate with their stated checks. Finite verification is exhaustive for exactly the six-point auxiliary complex; it is not extrapolated to larger parameters.

## Relationship to prior work

Feng and Wang, arXiv:2404.10566v1 (first public April 16, 2024), Table 1, computed mod-two Betti numbers \((29,7)\) for \(\operatorname{Ind}(\mathrm{KG}(3,1))\), and their §7 asked for the homotopy type. Feng, arXiv:2610.17394v1 (October 12, 2026), Theorem 18, proves the **rational** Betti numbers \((29,7)\) and their all-parameter formulas; its Question 19 explicitly asks whether all corresponding **integral** homology groups are torsion-free. Agreement of mod-two and rational Betti numbers rules out two-primary torsion in this case, but does not rule out odd-primary torsion. The new claim is the exact integral assertion at \(k=1\), obtained from a finite integer Morse certificate and the published decomposition framework. Barmak's star-cluster result supplies the contractibility mechanism, not these integral invariants.

## Limitations

The calculation covers the first nontrivial triple-Kneser parameter only; it does not settle the all-parameter integral torsion question. A free integral homology calculation does not prove that \(X_7\) is a wedge of spheres, so that stronger claim is withheld. The model's six-dimensional summands may have nontrivial higher attaching phenomena. The proof uses a reproducible finite computer-assisted integer computation, not a hand-derived symbolic Smith normal form. Bibliographic search cannot exclude unindexed or unpublished equivalent calculations. Independent scientific audit has not been performed.

## References

1. Ziqin Feng, *The rational homology of independence complexes of Kneser graphs on triples*, arXiv:2610.17394v1, October 12, 2026, §§1,3,5–7 and Appendix A. https://arxiv.org/html/2610.17394v1
2. Ziqin Feng and Guanghui Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1, April 16, 2024, Table 1 and §§4–7. https://arxiv.org/html/2404.10566v1
3. Jonathan Ariel Barmak, *Star clusters in independence complexes of graphs*, Advances in Mathematics 241 (2013), 33–57; arXiv:1007.0418 (first public July 2, 2010).
