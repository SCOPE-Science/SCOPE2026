# A torsion-free mixed-dimensional sphere wedge for the seven-cycle categorical product with four colors

## Finding

Let \(G=C_7\times K_4\) be the categorical (tensor) product. Its independence complex has the exact homotopy type
\[
\operatorname{Ind}(G)\simeq\bigvee^{3}S^3\ \vee\ \bigvee^{6}S^4.
\]
Consequently, \(\widetilde H_3(\operatorname{Ind}(G);\mathbb Z)\cong\mathbb Z^3\), \(\widetilde H_4(\operatorname{Ind}(G);\mathbb Z)\cong\mathbb Z^6\), and all other reduced integral homology groups vanish. In particular the integral homology is torsion-free. This is an exact finite case of the torsion-freeness question posed by Antolín Camarena and Carnero Bravo (Question 24 in their 2023 preprint).

## Assumptions and scope

Work with the finite, simple, undirected graph whose vertex set is \(\{(i,j):i\in\mathbb Z/7\mathbb Z,\ 0\le j<4\}\). Two *distinct* vertices \((i,j)\) and \((i',j')\) are adjacent exactly when \(i'-i\equiv 1\) or \(-1\pmod 7\) and \(j'\ne j\). This defines the categorical product \(C_7\times K_4\), not the Cartesian or strong product. Its independence complex has a simplex for each nonempty vertex subset with no adjacent pair. The result concerns only this 28-vertex graph; no assertion is made for all products \(C_k\times K_n\).

## Proof

Index vertices by \(v=4i+j\), increasing from zero to 27. Encode each nonempty independent set as a 28-bit integer mask. The exact enumeration algorithm in `c7k4_verifier.py` recursively splits on the least remaining available vertex, deleting the vertex's neighbors after including it. It enumerates **36,068 distinct nonempty faces**, including all dimensions through 11, without truncation or sampling. Its recursion includes each independent set exactly once because a vertex's inclusion is decided before continuing with the remaining eligible higher-index vertices.

Construct a discrete-Morse matching by considering the vertices in the order 0, 1, ... , 27. At each stage, among the presently unmatched faces, pair every face \(\sigma\) not containing that vertex with \(\sigma\cup\{v\}\) whenever both remain unmatched. Each face appears in at most one pair because the two members are removed immediately, and all paired faces differ in dimension by one. The exact verifier tests all such pairs and checks that the **complete 218,008-incidence directed Hasse graph**, with matched incidences reversed, admits a topological ordering. Thus the matching is acyclic (not merely locally gradient-like).

The exhaustive matching produces **18,023 pairs** and exactly **22 critical cells**: one dimension-zero cell, nine dimension-three cells and twelve dimension-four cells; there are no critical cells in any other dimension. Forman's discrete-Morse theorem provides a homotopy-equivalent CW complex \(X\) with precisely those cells. In particular its three-skeleton is \(\bigvee^{9}S^3\), with a single zero-cell and no cells in dimensions one or two.

Orient each simplex using the increasing indexed vertices. The cellular differential \(d_4:C_4(X;\mathbb Z)\to C_3(X;\mathbb Z)\) is computed exactly by signed gradient-path elimination. In detail, for a critical three-simplex \(\tau\), its projection is the corresponding basis vector; for a three-simplex paired above a two-simplex its projection is zero. If a three-simplex \(\tau\) is paired as a lower face with a four-simplex \(\eta\), write \(\epsilon(\tau,\eta)=\pm1\) for its oriented incidence and define its critical projection recursively by
\[
P(\tau)=-\epsilon(\tau,\eta)\sum_{\substack{\tau'\subset\eta\\\dim\tau'=3,\ \tau'\ne\tau}}\epsilon(\tau',\eta)P(\tau').
\]
The directed-Hasse acyclicity check guarantees these recurrences terminate; all values are integers. Applying \(P\) to the oriented boundary of each of the twelve critical four-simplices yields the full \(9\times12\) integral Morse differential. Its rows are listed in `VERIFICATION.md` and recreated from scratch in the verifier. Integer-only row and column operations using **six pivots equal to \(\pm1\)** reduce it to a diagonal matrix with six ones and zeros elsewhere. No division by nonunits, floating-point computation, or inference from mod-two ranks is involved.

Finally, the attaching maps of the twelve four-cells lie in \(\pi_3(\bigvee^{9}S^3)\cong\mathbb Z^9\), and their homotopy classes are exactly the corresponding columns of \(d_4\) by the Hurewicz isomorphism. Integral invertible changes of bases on the domain and codomain wedges are realized by homotopy equivalences and preserve the homotopy type of the mapping cone. The six unit diagonal maps yield contractible cone summands; the remaining three target sphere summands and six null-attached four-cells give \(X\simeq\bigvee^{3}S^3\vee\bigvee^{6}S^4\). This proves the claimed integral homotopy classification, not only homology dimensions.

## Verification

Run `python3 c7k4_verifier.py` with a standard Python 3 interpreter. The program builds the graph and all independent sets anew, checks all pairings, tests the full directed Hasse graph for acyclicity, computes every signed gradient-path contribution to the integer Morse boundary, verifies all six unit Smith pivots, and **independently** reduces the original simplicial boundary matrices in every dimension over \(\mathbb F_2\). It prints `VERIFY_OK` only after all assertions succeed. The independent finite-field check gives mod-two Betti numbers \(b_3=3\), \(b_4=6\), \(b_0=1\), and zero in all other degrees. It does not replace the integral Smith computation or the topological argument.

## Relationship to prior work

Antolín Camarena and Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs* (2023 preprint; 2024 publication), prove in their Theorem 23 that \(\operatorname{Ind}(C_7\times K_n)\) is simply connected, has reduced homology in at most dimensions three and four, and has a sphere-wedge-plus-possible-Moore-space homotopy form. Their Question 24 asks whether these homology groups are always torsion-free and explicitly names \(C_7\times K_4\) among their finite computational examples. That theorem **does not itself eliminate Moore-space torsion summands** or determine the integer differential. The present finite calculation eliminates them in this one named case and determines the two exact multiplicities. Goyal–Shukla–Singh (2019) analyze other categorical products, including products of two complete graphs. Later work on products involving paths (2025) and generalized Mycielskian graphs (2026) treats different graph constructions. Kozlov's 2005 work provides earlier simple-homotopy methodology but no calculation of this graph.

## Limitations

The proof is an exhaustive **finite** calculation for \(C_7\times K_4\), not a theorem for arbitrary cycle lengths, numbers of colors, or other products. The verifier proves acyclicity by complete incidence enumeration rather than providing a symbolic all-parameter matching theorem. A source-equivalent proof elsewhere, particularly in unindexed literature, cannot be ruled out; no claim of independent external validation is made. The comparison with prior computations is a comparison of published statements, not evidence that their private computational records lack this answer.

## References

- D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613 (first public 2005-03-28; primary MSC 57Q10). https://arxiv.org/abs/math/0503613
- S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (2019). https://arxiv.org/pdf/1905.06926
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v2 (2023), Theorem 23 and Question 24, pp. 25–27; published in *Homology, Homotopy and Applications* **26** (2024). https://arxiv.org/pdf/2307.12401
- A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457 (2025). https://arxiv.org/abs/2505.06457
- A. Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432 (2026). https://arxiv.org/pdf/2601.13432
