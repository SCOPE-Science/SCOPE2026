# Three symmetry types of minimum identifying codes in the four-dimensional binary cube
## Finding
Write \(Q_4\) for the graph with vertex set \(\mathbb F_2^4\), where two distinct words are adjacent exactly when they have Hamming distance one. A radius-one identifying code is a subset \(C\) for which all sixteen closed-neighborhood signatures \(B_1(v)\cap C\) are nonempty and pairwise distinct. It is known that the minimum cardinality is \(7\) and that exactly \(960\) labeled seven-word codes attain it. The new assertion is a complete equivalence classification of that known equality layer.

**Classification theorem.** Under the full Hamming-isometry group
\[
G=\mathbb F_2^4\rtimes S_4,\qquad |G|=384,
\]
the \(960\) minimum identifying codes split into precisely three orbits. Representatives and their orbit and stabilizer orders are:

| Representative, written as four-bit words | Orbit size | Stabilizer order | Distance counts at \(1,2,3,4\) |
| --- | ---: | ---: | --- |
| \(\{0000,0001,0010,0101,1010,1100,1111\}\) | 192 | 2 | \((4,9,6,2)\) |
| \(\{0000,0001,0010,0101,0110,1011,1101\}\) | 384 | 1 | \((5,8,7,1)\) |
| \(\{0000,0001,0010,0101,0110,1101,1111\}\) | 384 | 1 | \((6,7,6,2)\) |

The Hamming-distance profiles prove pairwise inequivalence. The middle class, whose representative has exactly one antipodal codeword pair, is not represented by either of the two explicit example codes in the earlier quaternary-Lee-cube enumeration.

## Assumptions and scope
A code is an *unordered subset* of the sixteen labeled binary words. Its identifying signature at a vertex \(v\) is \(B_1(v)\cap C\), including \(v\) itself if it is in the code. Every one of the sixteen signatures must be nonempty and different from every other signature. No linearity or uniformity condition is imposed.

A Hamming isometry has the form \(x\mapsto P x+a\) with \(P\) a permutation of the four coordinate positions and \(a\in\mathbb F_2^4\). Thus the full graph automorphism group has order \(16\cdot 24=384\). The theorem uses this full group, rather than only the dihedral symmetries of a chosen quaternary Lee-grid presentation.

The graph \(Q_4\) is also the Lee graph on \(\mathbb Z_4^2\). The Gray map \(0\mapsto00\), \(1\mapsto01\), \(2\mapsto11\), \(3\mapsto10\) in each quaternary coordinate sends Lee distance to Hamming distance. Hence the seven-word optimum and the labeled count \(960\) in the 2010 Kim--Kim census apply **exactly** to the present vertex set.

## Proof
First, the three displayed seven-subsets are identifying codes: evaluating the sixteen nonempty radius-one signatures gives sixteen distinct subsets for each. This fact is verified directly and independently from the neighborhood definition by `verify.py`.

For a seven-set \(C\), let its unordered pair-distance distribution be the number of its \(\binom{7}{2}=21\) distinct pairs at each Hamming distance \(1,2,3,4\). For the three displayed code sets, the distributions are \((4,9,6,2)\), \((5,8,7,1)\), and \((6,7,6,2)\). Every element of \(G\) preserves Hamming distances, so the three examples occupy different orbits.

Enumerating the \(24\) coordinate permutations and \(16\) bit translations, each explicitly applied to the seven-word representatives, gives stabilizer orders \(2,1,1\). The first stabilizer consists of the identity and the permutation swapping coordinate positions \(0\leftrightarrow1\) and \(2\leftrightarrow3\), with zero translation; the other stabilizers contain only the identity. The orbit--stabilizer theorem now gives respective orbit sizes
\[
384/2=192,\qquad 384/1=384,\qquad 384/1=384.
\]
Their sum is \(960\), **exactly the total number of labeled minimum codes established in the earlier Kim--Kim census**. Because the three orbits are disjoint, the known census and these orbit sizes prove they exhaust all minimum codes. This argument does not claim that the earlier total \(960\) is new.

For a standalone finite check not depending on the previous census, `verify.py` exhaustively enumerates all \(\binom{16}{6}=8008\) six-word candidates and \(\binom{16}{7}=11440\) seven-word candidates, using two independently constructed closed-neighborhood predicates. It finds no valid six-word code and exactly \(960\) valid seven-word codes, independently partitions these into the same three orbits, and verifies Burnside's lemma: the sum over all \(384\) group elements of their numbers of fixed minimum codes is \(1152=3\cdot384\). No admissible smaller code exists because extending an identifying code by new codewords preserves identification.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. It independently builds adjacency by Hamming distance and by single-bit flips, checks all codeword signatures with two different representations for every six- and seven-element subset, enumerates the complete isometry group, certifies each orbit and stabilizer, checks the distance distributions, and cross-checks the number of orbits by Burnside's lemma. It also checks the Gray-map isomorphism on all sixteen-by-sixteen pairs of vertices.

Expected final line:

`VERIFY_OK minima=960 orbits=3 orbit_sizes=192,384,384 stabilizers=2,1,1 burnside=1152`

## Relationship to prior work
Karpovsky, Chakrabarty, and Levitin introduced graph identifying codes for fault diagnosis in 1998. Janson and Laihonen study identifying codes in binary Hamming spaces and state the codeword-neighborhood formulation in their 2008 open preprint.

**Most importantly, Kim and Kim's full 2010 treatment of identifying codes in quaternary Lee hypercubes already proves both the minimum size \(7\) and the exact labeled count \(960\) in \(\mathbb Z_4^2\), which is graph-isomorphic to \(Q_4\).** Its Theorem 3.6 displays two example optimal codes but does not give a complete classification under graph automorphisms. Under the Gray isomorphism, those two examples have distance profiles \((4,9,6,2)\) and \((6,7,6,2)\). They do not display the third profile \((5,8,7,1)\). The new result is therefore the exact three-orbit classification and stabilizer/distance-structure data, not the optimum or raw census.

A 2015 identifying-code study of degree-four Abelian Cayley graphs gives primary MSC \(94B25\) for this area; its published focus is general Cayley-graph constructions rather than this small equality-orbit census.

## Limitations
This is a finite classification of minimum, *radius-one*, *single-vertex* identifying codes in the four-cube. It does not classify larger identifying codes, codes in other hypercube dimensions, general multiple-fault identifying sets, or nonstandard open-neighborhood/local-identifying variants. The full symmetry group is the graph automorphism group, not a restricted group of quaternary coordinate transformations. A targeted literature search cannot exclude an obscure unindexed orbit census.

## References
1. M. G. Karpovsky, K. Chakrabarty, and L. B. Levitin, “On a New Class of Codes for Identifying Vertices in Graphs,” *IEEE Transactions on Information Theory* 44(2) (1998), 599--611, DOI:10.1109/18.661507.
2. S. Janson and T. Laihonen, “On the Size of Identifying Codes in Binary Hypercubes,” arXiv:0804.3029v1, first public 2008-04-18.
3. J.-L. Kim and S.-J. Kim, “Identifying Codes in q-ary Hypercubes,” *Bulletin of the Institute of Combinatorics and Its Applications* 59 (2010), 93--102; Theorem 3.6.
4. “Identifying Codes of Degree 4 Cayley Graphs over Abelian Groups,” *Advances in Mathematics of Communications* 9(2) (2015), 129--148, DOI:10.3934/amc.2015.9.129 (classification context).
