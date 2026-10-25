# A dihedral-equivariant collapse from Schrijver independence to neighborhood topology

## Finding

Let \(G=SG_{3,2}\) be the Schrijver graph on the sixteen cyclically stable three-subsets of \(\mathbb Z/8\mathbb Z\), with two triples adjacent exactly when they are disjoint. Its ordinary open Lovász neighborhood complex is a simplicial subcomplex of its independence complex. **The inclusion**
\[
\mathcal N(G)\hookrightarrow \operatorname{Ind}(G)
\]
**is a dihedral-equivariant simplicial collapse**, implemented by fourteen successive complete dihedral orbits of elementary free-face pairs. There are exactly 176 pairs, removing precisely the 352 faces not in \(\mathcal N(G)\). In particular, this particular inclusion, rather than merely some unspecified homotopy equivalence, is a simple-homotopy equivalence and a strong equivariant deformation retraction.

The sphere homotopy type of \(\mathcal N(G)\simeq S^2\) was established in earlier work and is **not claimed as new**. Consequently the induced map is an isomorphism on integral second homology. With \(r(t)=t+1\), \(s(t)=-t\), the shared integral orientation character is
\[
\deg(r^as^b\mid\widetilde H_2)=(-1)^{a+b}
\quad(0\le a<8,\quad b\in\{0,1\}).
\]
This character is a consequence of the relative collapse and direct signed-chain checks, not a claim of a new nonequivariant sphere classification.

## Assumptions and scope

A three-element set \(T\subset\mathbb Z/8\mathbb Z\) is *stable* if it contains no cyclically adjacent pair, including \(\{0,7\}\). Order the sixteen stable triples lexicographically as \(T_0,\dots,T_{15}\). The graph vertices are these sixteen triples; two vertices are adjacent when the underlying triples are disjoint. A face of \(\operatorname{Ind}(G)\) is a set of graph vertices containing no edge of \(G\). A nonempty face of \(\mathcal N(G)\) is a set of graph vertices adjacent to one common graph vertex; include the empty face in both. Since \(G\) has no triangle, each open neighborhood is independent, giving the canonical simplicial inclusion.

The dihedral group \(D_8=\langle r,s\mid r^8=s^2=1,\;srs=r^{-1}\rangle\) has order sixteen and acts on the eight underlying cyclic positions. It preserves stable sets and disjointness, hence acts on both simplicial complexes. The term *equivariant orbit collapse* means that at each stage a full \(D_8\)-orbit of pairwise disjoint elementary collapse pairs is removed; the simultaneous operation commutes with every group element. This finite statement is only for \(SG_{3,2}\), not an all-parameter theorem.

## Proof

**Exhaustive complexes.** Represent a nonempty simplex \(\sigma\) by the 16-bit integer \(\sum_{i\in\sigma}2^i\) in lexicographic graph-vertex order. Enumerate all \(2^{16}-1\) nonempty masks and retain exactly those with no adjacent graph vertices; for the neighborhood complex, retain every nonempty subset of each of the sixteen open neighborhoods. Direct enumeration gives respectively
\[
 f(\operatorname{Ind}(G))=(16,84,184,186,88,16),\qquad
 f(\mathcal N(G))=(16,68,88,42,8).
\]
Thus the set difference contains 352 nonempty faces, distributed by dimension as \((0,16,96,144,80,16)\).

**Finite orbit certificate.** The fourteen pairs below are written as `(free_mask, coface_mask)` in the specified lexicographic indexing, in their required stage order. Every row denotes its **entire dihedral orbit**, not just that representative:

```
(58624,60672)  (52480,52544)  (58368,60416)  (57600,59648)
(43010,59394)  (52224,52288)  (50432,50496)  (40962,57346)
(57344,59392)  (50176,50240)  (16648,49416)  (16450,49218)
(41216,43264)  (40960,43008)
```

The corresponding ordered orbit sizes are
\[
(8,8,16,16,8,16,8,16,16,16,8,16,8,16),
\]
whose sum is 176. Each orbit pair has a lower simplex one vertex smaller than its upper simplex. For each current lower simplex, the complete list of its codimension-one cofaces in the *current* complex consists of the designated upper simplex alone. Within each orbit every simplex occurs in exactly one pair, and no pair contains a retained neighborhood face. The fourteen successive orbit removals therefore are well-defined elementary simplicial collapses, and are equivariant under the full group. The terminal face collection is checked to equal the original \(\mathcal N(G)\) **mask-for-mask**. This gives the asserted equivariant relative strong deformation retraction; it does not infer a collapse solely from equal homology ranks.

**Homology consequence and character.** Previously established work shows \(\mathcal N(SG_{3,2})\simeq S^2\). The collapse gives the same integral homotopy type for the larger independence complex and identifies their homology by the actual inclusion. For every \(r^as^b\), count each setwise fixed simplex with the parity of its induced ordered-vertex permutation and alternate by simplicial dimension. The ordinary Lefschetz trace equals one plus the action trace on second homology, because the only ordinary rational homology is in dimensions zero and two. Complete fixed-face calculations on both complexes agree and give the displayed \((-1)^{a+b}\) character. Since integral second homology is a rank-one free group, its integral action is uniquely determined by these signs.

## Verification

Run `python3 verify_relative_collapse.py` from the package directory with Python 3.10 or newer. It requires only the Python standard library; all fourteen orbit representatives appear literally in the program. It independently constructs graph vertices and edges from stable triples, independently enumerates both entire face sets, checks triangle-freeness, rebuilds the sixteen dihedral permutations and checks they preserve adjacency, then checks all orbit-pair incidences against the **current** face collection at every stage. In addition, it checks disjointness of all pairs, the size of every orbit, invariance of every remaining face collection and exact equality with the neighborhood complex at the end. Finally it computes signed simplicial Lefschetz traces on both complexes for all sixteen group elements. The expected concluding line is `VERIFY_OK_SCHRIJVER_SG32_RELATIVE_EQUIVARIANT_COLLAPSE`; `relative_verification_output.txt` records the actual successful execution. This finite enumeration is exhaustive, not an extrapolation from sampled instances.

## Relationship to prior work

Braun (first public arXiv version 2009-12-03) investigates Schrijver independence complexes and determines the homotopy type of a related graph \(E_{2n+2}\), with the case \(n=3\) giving the same sphere homotopy type. That nonequivariant result is not relabeled new here. Braun and Zeckner (first public version 2011-02-09) prove that \(\mathcal N(SG_{n,2})\) collapses to a polyhedral sphere, and study a dihedral-invariant *subdivided* neighborhood sphere. Their collapse operates **inside the neighborhood complex**, whereas the present orbit matching removes the complementary faces of the strictly larger independence complex and proves a statement about a specific inclusion. The two pre-existing sphere homotopy types cannot alone establish that their inclusion is an equivariant homotopy equivalence, much less exhibit 176 elementary face pairs. Another published finite graph example (the Chvátal graph) admits a comparable type of inclusion collapse, but has different vertices, orbits and free faces and does not imply this result.

## Limitations

The theorem is for one canonical sixteen-vertex graph. It does not assert that the natural inclusion is a homotopy equivalence for arbitrary triangle-free graphs or for other Schrijver parameters; a triangle-free path on four vertices already demonstrates that equality of the two constructions is not automatic. The character classifies the induced homology action, not the equivariant homeomorphism type of the sphere. The proof is an explicit finite calculation and the accompanying replayable certificate, not a broad classification. Equivalent statements in unindexed literature could remain unidentified.

## References

- B. Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1 (first posted 2009-12-03), especially Theorems 1.4–1.5 and Section 4. https://arxiv.org/abs/0912.0720
- B. Braun and M. Zeckner, *Deformation Retracts of Neighborhood Complexes of Stable Kneser Graphs*, arXiv:1102.1984v1 (first posted 2011-02-09), especially Theorems 1.2–1.3 and Sections 3–5. https://arxiv.org/abs/1102.1984
- A. Björner and M. de Longueville, *Neighborhood complexes of stable Kneser graphs*, Combinatorica 23 (2003), 23–34; homotopy sphere theorem as cited and used by Braun–Zeckner.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
