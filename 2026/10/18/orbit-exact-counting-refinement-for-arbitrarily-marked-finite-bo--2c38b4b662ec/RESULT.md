# Orbit-exact counting refinement for arbitrarily marked finite Boolean lattices

## Finding
Let \(n\ge2\), and let \(A_1,\ldots,A_m\) be any ordered list of pairwise distinct subsets of \([n]\), including the empty list. On \(B_n=2^{[n]}\), retain only the binary directed Hasse predicate \(R(X,Y)\), meaning \(Y=X\cup\{i\}\) for some \(i\notin X\). Give each named vertex \(A_j\) its own colour and all unnamed vertices a common colour. At each refinement round, replace each colour by the old colour together with separate multisets of colours of incoming and outgoing neighbours.

**Theorem.** After at most \(2n-2\) rounds, equal colours are equivalent to belonging to the same automorphism orbit of this marked directed lattice. Define \(I_\sigma=\{i\in[n]:(\mathbf1_{i\in A_j})_{j=1}^m=\sigma\}\) and \(N_\sigma=|I_\sigma|\) for \(\sigma\in\{0,1\}^m\). The stable colour of a vertex \(X\) is determined exactly by \(c_\sigma(X)=|X\cap I_\sigma|\). Thus the number of stable colours and the size of each colour class are respectively
\[
\prod_{\sigma\in\{0,1\}^m}(N_\sigma+1),\qquad
\prod_{\sigma\in\{0,1\}^m}\binom{N_\sigma}{c_\sigma}.
\]
Zero-sized membership classes contribute factors one. For \(n=1\), the orbit assertion holds directly; no general iteration bound is needed. The theorem concerns refinement **inside the marked Boolean lattice**, not identification against arbitrary finite digraphs.

## Assumptions and scope
All sets are finite. Marker names and their individual colours are part of the relational vocabulary; two markers of the same vertex are excluded for definiteness. An automorphism must preserve each marker, not merely their unordered set. Covers are upward directed and downward and upward neighbour counts are distinguished. The initial unmarked vertices carry one common colour. All assertions are uniform in the ground-set size and in the finite number of markers.

## Proof
**1. Determine the orbit invariant.** Any automorphism of the finite Boolean lattice permutes its atoms (its singleton subsets), and conversely any permutation of atoms induces a unique lattice automorphism. Fixing all marked subsets is therefore equivalent to permuting the coordinates separately inside the mutually disjoint regions \(I_\sigma\). Two vertices \(X,Y\) are in the same orbit if and only if \(c_\sigma(X)=c_\sigma(Y)\) for all \(\sigma\). Transitivity in each region gives the stated class sizes and class count.

**2. Refinement distinguishes ranks.** The number of incoming covers at \(X\) equals \(|X|\), and the number of outgoing covers equals \(n-|X|\). Thus after one round two vertices of distinct ranks have different colours. Colours only split in subsequent rounds.

**3. Refinement recovers all marker-membership patterns of atoms.** Fix a marker \(A_j\) of size \(a\ge1\). For an atom \(\{i\}\), the number of upward directed paths of length \(a-1\) from \(\{i\}\) to the uniquely coloured vertex \(A_j\) is \((a-1)!\) if \(i\in A_j\), and zero otherwise. When \(a=1\), the same distinction follows from the initial named-vertex colour. For an empty marked set no atom belongs to it, so its membership coordinate is constant. At every stable equitable colouring, all vertices of one colour have identical numbers of directed paths of any prescribed length to each uniquely coloured marker cell: induction on path length follows from equality of outgoing-neighbour colour multiplicities. More quantitatively, the path count of length \(\ell\) is encoded by at most \(\ell\) further rounds after the marker is initially distinguished. Therefore every atom's complete vector of memberships in all markers is distinguished within \(n-1\) rounds (as \(a-1\le n-1\)); its rank is also distinguished by the first round. Atoms with the same membership vector are interchangeable by the coordinate permutations of Step 1 and hence remain equally coloured.

**4. Induct on vertex rank.** Suppose all vertices of rank \(k\ge1\) have been distinguished exactly by their vectors \(c(X)=(c_\sigma(X))_\sigma\). A vertex \(Y\) of rank \(k+1\) has precisely the \(k+1\) immediate predecessors \(Y\setminus\{i\}\), \(i\in Y\). Each predecessor colour, by induction, determines its pattern-count vector. Summing these \(k+1\) vectors gives \(k\,c(Y)\), since each element of \(Y\) is present in precisely \(k\) of the predecessors. Hence their multiset of colours determines \(c(Y)\) uniquely. One more refinement round therefore separates all distinct vectors at rank \(k+1\). Since rank is already preserved and coordinate permutations preserve colours, the vector is both necessary and sufficient for colour equality. Starting at rank one and advancing through rank \(n\) uses at most \((n-1)+(n-1)=2n-2\) rounds. Rank zero contains a single vertex. The proof is complete.

## Verification
The provided standalone standard-library program explicitly constructs all \(2^n\) vertices and both directed-cover adjacency lists, executes ordinary vertex-level counting refinement, and compares its colour partition with the independently defined atom-pattern orbit vectors. It passed 2,047 marker configurations across ground-set sizes one through seven, including all distinct marker tuples of lengths zero through three for sizes at most three, and deterministic additional marker samples for sizes four through seven. The largest observed stabilization-to-orbits count was five rounds, which is below the theoretical bound. This finite testing corroborates, but is not a substitute for, the all-size proof.

To replay, from the package root run `python3 scripts/check_marked_boolean.py`. The expected output ends in `MARKED_BOOLEAN_ORBIT_REFINEMENT_PASS`.

## Relationship to prior work
The usual counting colour-refinement procedure and its relationship to two-variable counting logic provide general methodological background; the result concerns a particular explicitly marked family of directed lattice cover structures. Arvind, Köbler, Rattan and Verbitsky give foundational colour-refinement methods. Kiefer and McKay analyze general iteration bounds. Maynard and Siemons study reconstruction of integer partitions from deletion minors, which is a different reconstruction operation and does not supply the present orbit theorem. The proof here uses directed path propagation from individually coloured vertices and a rank-by-rank predecessor-sum identity; no claim about a first-ever discovery is asserted.

## Limitations
Directed cover orientation, unique marker colours, and separate predecessor/successor multiplicities are hypotheses. We do not claim the same bound for undirected covers, uncoloured or collectively coloured marker sets, infinite Boolean lattices, or comparison against arbitrary structures. The complexity bound counts rounds of colour refinement, not total implementation time. Exact publication priority has not been independently established, and the proof and computations have not received an independent mathematical audit.

## References
1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, 2015, https://arxiv.org/abs/1502.01255 .
2. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, ICALP 2020, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2020.73 .
3. P. Maynard and J. Siemons, *Efficient reconstruction of partitions*, Discrete Mathematics 293 (2005), 205–211, available online 31 March 2005, https://esdocs.com/doc/484394/efficient-reconstruction-of-partitions .
