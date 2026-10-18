# Eight optimal harmonious colour classes of the Heawood graph form one orbit

## Finding
Let \(H\) be the Heawood graph, the incidence graph of the seven-point Fano plane. A *harmonious colouring* is a proper vertex colouring for which any unordered pair of distinct colours occurs along at most one edge. Then \(H\) has precisely **eight** harmonious seven-colourings modulo permutation of colour names, or **40,320** with a fixed palette of seven named colours. The eight colour partitions form a single orbit under the \(168\)-element point-collineation group of the Fano plane; the stabiliser of each partition within that group has order \(21\).

More precisely, every such partition consists of seven pairs, one point and one nonincident line per pair. Equivalently there are exactly eight bijections \(f:\mathcal L\to\mathcal P\) from the seven lines to seven points satisfying (i) \(f(L)\notin L\) for each line \(L\), and (ii) the \(21\) unordered pairs \(\{p,f(L)\}\), for incidences \(p\in L\), are pairwise distinct. In fact those pairs exhaust \(\binom{\mathcal P}{2}\).

## Assumptions and scope
The Fano plane is represented by nonzero binary three-vectors \(p,l\in\{1,\dots,7\}\). The line with normal vector \(l\) contains point \(p\) exactly when the parity of \(p\mathbin{\&}l\) is even, i.e. their binary scalar product equals zero. There are seven lines of size three and exactly \(21\) incidences. Graph vertices are its points and lines. Colour names are regarded as distinct for the \(40,320\) count and interchangeable for the eight-class count. Collineations act jointly on points and lines, not on colour names.

## Proof
**Step 1: lower bound and two-vertex classes.** A harmonious colouring with \(k\) colours assigns a distinct unordered pair of different colours to each of the \(21\) edges, so \(\binom{k}{2}\ge21\), hence \(k\ge7\). For \(k=7\), each possible unordered colour pair must appear exactly once. Consequently the three edges at each vertex require three distinct other colours. For every colour \(c\), the six unordered pairs involving \(c\) each appear on exactly one edge, giving precisely six edge ends of colour \(c\); as \(H\) is cubic, that colour has precisely two vertices. Two points cannot have the same colour: the unique common line would make two distinct incident edges carry the same unordered pair. The same argument applies to any two lines. Therefore every colour class is precisely a pair consisting of one point and one line, and that pair must be nonincident by propriety.

**Step 2: finite exhaustive bijection test.** Relabel each colour by its unique point; a seven-colouring is then determined, up to a permutation of the colour names, by a bijection \(f:\mathcal L\to\mathcal P\). There are \(7!=5040\) such bijections. In the specified binary-vector presentation a candidate is proper exactly when \(f(l)\notin L_l\) for all seven normals \(l\). The checker `verify_bijections.py` runs an ordinary lexicographic traversal through all 5040 choices, without omissions. Exactly \(144\) are proper. For each, it constructs all \(21\) unordered pairs \(\{p,f(l)\}\) for incidences \(p\in L_l\), and requires all 21 pairs to be distinct. The numbers of proper bijections with 14, 15, 18, or 21 different edge-colour pairs are respectively \(24,56,56,8\), exhausting \(144\). Hence exactly eight harmonious partitions exist. An example, with line normals ordered \(1,\dots,7\), is \(f=(1,3,6,7,4,5,2)\). The eight partitions yield \(8\cdot7!=40,320\) named colourings. The equivalence with complete proper colourings and with Fano-plane perfect nestings follows because all \(\binom72=21\) pairs are used.

**Step 3: one symmetry orbit.** Independently of the preceding enumeration, all permutations of seven point labels are filtered for the property of sending the seven Fano blocks onto themselves. Exactly \(168\) survive. Each surviving point permutation induces a unique corresponding line permutation; the image of the displayed example under each is computed. Those \(168\) images comprise exactly the eight solutions from Step 2. Thus the action is transitive, and orbit-stabiliser gives \(168/8=21\) collineations fixing any solution. This proves the stated orbit and stabiliser results.

## Verification
Run the included standalone Python 3 programs with no third-party dependencies:

```shell
python3 verify_bijections.py
python3 verify_pairings.py
```

The first exhausts \(5040\) line-to-point bijections and independently identifies \(168\) Fano collineations. The second independently constructs the incidence edges and exhausts all \((14-1)!!=135,135\) partitions of 14 vertices into seven unordered pairs; \(23,412\) are proper and exactly eight are harmonious. Its final count has no assumption that the classes are point-line pairs, checking the key structural reduction separately. Stored stdout records are included; each program terminates with `VERIFY_OK` and was rerun after embedding.

## Relationship to prior work
The harmonious-colouring notion predates this calculation; the older graph-colouring literature and the 2012 work of Akbari, Kim and Kostochka treat general and forest problems, not this census. Buratti, Merola, Nakić and Rubio-Montiel (2023, *Banff designs*) establish that any Desarguesian projective plane admits a harmonious colouring of its Levi graph using exactly the number of points. In particular, the equality \(h(H)=7\) and **existence** of at least one optimum are already known and are not claimed new. Their correspondence between harmonious colourings and nestings of Steiner triple systems identifies the relevant design-theoretic interpretation, but their existence theorem does not enumerate every nesting of the fixed seven-point Fano plane or determine the collineation stabiliser. Stinson's 2024 treatment of weak and strong nestings gives an explicit nesting for order seven and develops the correspondence; the inspected example and discussion do not state this complete orbit/count classification.

## Limitations
This is an exact finite classification of a particular labelled incidence graph. It does not classify nestings or harmonious colourings of larger projective planes, and it supplies no new bound for the harmonious chromatic number, which was already known here. Exhaustive enumeration certifies precisely the specified finite domain, not an infinite family. The equivalence with a Banff design is established in earlier literature. Unindexed older enumeration of the Fano-plane nestings remains a possible novelty risk. No independent external scientific audit has been performed.

## References
1. S. Akbari, J. Kim and A. Kostochka, *Harmonious Coloring of Trees with Large Maximum Degree*, arXiv:1202.1046, first public version 2012-02-06. https://arxiv.org/abs/1202.1046.
2. M. Buratti, F. Merola, A. Nakić and C. Rubio-Montiel, *Banff designs: difference methods for coloring incidence graphs*, arXiv:2312.05861 (2023), especially Sections 3 and 5, Theorem 3. https://arxiv.org/abs/2312.05861.
3. D. R. Stinson, *Weak and Strong Nestings of BIBDs*, arXiv:2405.12820 (2024), Example 3.1 and Section 5. https://arxiv.org/abs/2405.12820.
