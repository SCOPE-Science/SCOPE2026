# A projective-plane wedge in the Clebsch closed-neighborhood complex

## Finding
Let \(C\) be the standard \(5\)-regular Clebsch graph, represented on the \(16\) binary words of even length-five parity, with two distinct words adjacent if their Hamming distance is \(4\). Let \(\mathcal N[C]\) be the **closed-neighborhood complex**: a nonempty vertex set is a simplex if it is contained in the closed neighborhood of some vertex. There is an integral homotopy equivalence
\[
\boxed{\lvert\mathcal N[C]\rvert\simeq \mathbb{RP}^{2}\vee\bigvee^{55}S^{2}.}
\]
In particular,
\[
\pi_1(\mathcal N[C])\cong\mathbb Z/2\mathbb Z,\qquad
\widetilde H_j(\mathcal N[C];\mathbb Z)\cong
\begin{cases}\mathbb Z/2\mathbb Z,&j=1,\\ \mathbb Z^{55},&j=2,\\0,&\text{otherwise.}\end{cases}
\]
The original complex is pure of dimension \(5\), yet it collapses to dimension \(2\). Its integral torsion excludes any wedge-of-spheres homotopy type, and its lower-dimensional homology excludes shellability of this pure complex.

## Assumptions and scope
The vertex set is the even-parity subspace \(V=\{v\in\{0,1\}^{5}:\sum_i v_i\equiv0\pmod2\}\). Set \(N_C[v]=\{v\}\cup\{w\in V:d_H(v,w)=4\}\). Each \(N_C[v]\) has exactly six members. The resulting graph is the \(5\)-regular Clebsch graph (strongly regular parameters \((16,5,0,2)\)), also the folded five-cube. It is isomorphic to the Cayley model with generators \(1,2,4,8,15\) on four-bit words: projecting the even five-bit words to four bits gives generators \(7,11,13,14,15\); the first four form a linear basis with XOR sum \(15\), so an invertible linear change of basis gives the stated conventional model.

The complex is the downward closure of the sixteen six-vertex sets \(N_C[v]\), not the Lovász *open* neighborhood complex and not the graph's clique or independence complex. Throughout the homotopy and homology statements are integral, and the theorem is only about this particular finite graph.

## Proof
**1. Exhaustive face construction.** Index the even five-bit words by increasing binary integer, producing vertices \(0,\ldots,15\). Represent a nonempty simplex by the sixteen-bit incidence mask of its vertices. Enumerate every nonempty subset of each of the sixteen closed neighborhoods and remove duplicates. The complete face vector by dimensions \(0\) through \(5\) is
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,320,240,96,16),
\]
with \(808\) nonempty faces. Every six-element neighborhood is an inclusion-maximal facet. The exact construction is implemented independently of any stored face table in `verify.py`.

**2. Explicit elementary simplicial collapse.** While a free-face pair exists, consider all faces \(\sigma\) with exactly one immediate coface \(\tau\) in the *current* face set. Choose the lexicographically smallest triple \(( -\lvert\sigma\rvert,\operatorname{mask}(\sigma),\operatorname{mask}(\tau))\) and remove \(\sigma\) and \(\tau\). The verifier reconstructs and checks the current immediate-coface count at every deletion. Exactly \(256\) pairs are deleted and no free pair remains. The surviving simplicial complex \(L\) is two-dimensional, with
\[
(f_0(L),f_1(L),f_2(L))=(16,120,160).
\]
It has the complete graph on sixteen vertices as its one-skeleton. Each deletion is an elementary collapse, so \(\lvert\mathcal N[C]\rvert\simeq\lvert L\rvert\).

**3. Contract a spanning tree.** Contract the fifteen edges \(\{0,j\}\), for \(1\le j\le15\), in the complete one-skeleton. Contracting a tree is a homotopy equivalence for the CW complex. The quotient has one zero-cell, \(105\) oriented one-cells indexed by \(\{i,j\}\) for \(1\le i<j\le15\), and \(160\) two-cells, each with the explicit attaching word obtained from the oriented boundary \([a,b]+[b,c]-[a,c]\) of its indexed triangle \(a<b<c\), omitting the tree edges. All computations use free-group words: an oriented edge \((i,j)\) contributes its generator if \(i<j\), the inverse generator if \(i>j\), and the identity if either endpoint is \(0\).

**4. Elementary CW cell cancellations.** Whenever a generator occurs exactly once, with exponent \(+1\) or \(-1\), in an attaching word, cyclically rotate that word to isolate the generator, solve that relation for it, and substitute the resulting word in all other attaching maps. Discard the isolated generator and its two-cell. This is a homotopy-preserving elementary one/two-cell cancellation: after rotating the attaching circle and changing its orientation if needed, that two-cell crosses the chosen one-cell exactly once, permitting the elementary CW collapse after the standard change of attaching maps. Free and cyclic word reduction are attaching-map homotopies. Select the available cancellation using the explicit deterministic cost/key in `verify.py`; no guessed group presentations are trusted.

There are exactly \(104\) such cancellations. They leave one generator, \(56\) two-cells and one zero-cell. The verifier checks the **entire** final list of attaching words: \(42\) are empty, and the remaining \(14\) are either \(gg\) or \(g^{-1}g^{-1}\), for the single surviving generator \(g\). This is a full two-dimensional CW presentation, not merely its abelianization or its group presentation.

**5. Identify the homotopy type.** Choose one degree-two two-cell. Together with the one-cell and zero-cell it forms the standard CW model of \(\mathbb{RP}^{2}\). Every one of the other \(13\) degree-two attaching circles becomes nullhomotopic in that projective plane because its class is an even power of the generator of \(\pi_1(\mathbb{RP}^{2})\cong\mathbb Z/2\mathbb Z\). The remaining \(42\) constant attachments are nullhomotopic as well. Attaching a two-cell along a nullhomotopic map wedges on one \(S^2\). Thus the complex is \(\mathbb{RP}^{2}\vee\bigvee^{13+42}S^2\), as claimed. The integral homology and fundamental group follow from this CW description. The Euler characteristic consistency check is \(16-120+160=1-1+56=56\).

## Verification
Run `python3 verify.py` with a standard Python 3 installation; no third-party library or external data is needed. It independently builds the Clebsch graph and all \(808\) nonempty faces; checks every one of the \(256\) current-complex elementary free-face removals; enumerates the exact \(160\) residual triangles and their attaching words; performs all \(104\) group-word/CW cancellations; and verifies the exact \(42\) null plus \(14\) degree-two final attaching words. Direct simplicial chain calculations on the **uncontracted** two-dimensional spine independently check the boundary ranks \(104\) over \(\mathbb F_2\) and \(105\) over each of \(\mathbb F_3\) and \(\mathbb F_5\), giving mod-two reduced Betti ranks \((1,56)\) in degrees \((1,2)\) and odd-characteristic ranks \((0,55)\). The executable terminates with `ALL_VERIFY_OK` only after all these checks pass. This is a finite exact proof certificate for one graph, not an extrapolation to other folded cubes.

## Relationship to prior work
Matsushita [1] establishes the general closed-neighborhood construction and its relations to double-cover independence complexes, neighborhood-hypergraph Alexander duality, and graph fundamental groups. The inspected full version of [1] gives a worked classification for rook graphs but not this Clebsch case; its general equivalences alone do not determine this integral homotopy type. The graph is not a rook graph, and no applicable exact double-cover independence calculation was identified.

An existing calculation [2] establishes \(\mathcal N(C)\simeq\bigvee^{31}S^2\) for the *open* Lovász neighborhood complex of the **same** Clebsch graph; it does not imply the closed-neighborhood result. The change to closed neighborhoods introduces a nontrivial fundamental group and two-torsion. Adams–Shukla–Singh [3] analyze Čech complexes of hypercube graphs; the folded five-cube is not an ordinary binary hypercube. An integral-torsion calculation for the Grötzsch graph [4] concerns a different graph and supplies only homology, not this homotopy classification. Related reflexive/Dowker, double-cover, and metric Čech formulations were compared; no covering Clebsch result was found. An equivalent unindexed computation cannot be excluded.

## Limitations
The result is specific to the Clebsch graph. It is not a classification of all folded cubes, all strongly regular graphs, higher Čech scales, or equivariant homotopy actions. Its attaching-word certificate is exact for this finite complex; it supplies no independent external scientific validation. Literature comparisons cannot rule out all unindexed or inaccessible equivalent computations.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first public 2025-11-16, especially Definitions 1.1 and Theorems 1.2 and 1.5, https://arxiv.org/html/2511.12608v2.
2. *The 5-regular Clebsch neighborhood complex is a wedge of 31 two-spheres*, publicly available mathematical record (2026-10-11), open-neighborhood formulation.
3. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first public 2022-12-12, https://arxiv.org/abs/2212.05871.
4. *Integral two-torsion in the scale-two graph Čech nerve of the Grötzsch graph*, publicly available mathematical record (2026-10-11), different graph and homological conclusion.
