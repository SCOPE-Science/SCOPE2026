# A self-centered, nonregular zero-forcing exchange graph on 1,704 configurations

## Finding
Let \(M=GP(8,3)\) be the Möbius–Kantor graph. Let \(\mathcal Z(M)\) be the graph whose vertices are minimum ordinary zero-forcing subsets of \(V(M)\), adjacent if and only if one selected vertex is replaced by one unselected vertex. Then \(Z(M)=6\), \(\mathcal Z(M)\) has exactly \(1,704\) vertices and \(16,560\) edges, and **every vertex of \(\mathcal Z(M)\) has eccentricity six**. Thus this connected, nonregular graph has radius and diameter both equal to six.

For each integer \(j\), write \(d_j\) for the number of *unordered pairs of distinct configurations* at exchange distance \(j\). The complete distance enumerator is
\[
\sum_{j=1}^{6}d_jq^j
=16,560q+127,008q^2+417,720q^3+565,488q^4
+276,792q^5+47,388q^6.
\]
The Wiener index (sum of distances over unordered pairs) is \(5,453,976\). The complete degree distribution, with \(a_d\) configurations of degree \(d\), is
\[
(a_{16},a_{17},a_{18},a_{19},a_{20},a_{21},a_{22},a_{24})
=(240,96,336,192,288,192,240,120).
\]
There are no configurations of degree \(23\).

The exchange graph sits as an induced subgraph of the Johnson graph \(J(16,6)\). For configurations \(S,T\), their ambient Johnson distance is \(\delta(S,T)=6-|S\cap T|\). Of the \(1,450,956\) unordered pairs, exactly \(1,441,284\) have exchange distance \(\delta\), exactly \(9,648\) have distance \(\delta+1\), and exactly \(24\) have distance \(\delta+2\). No larger excess occurs. All \(24\) doubly stretched pairs have ambient distance two and exchange distance four, and comprise \(48\) distinct degree-sixteen endpoints, each in exactly one such pair.

## Assumptions and scope
All graphs are finite, undirected, and simple. The base graph has labeled vertices \(a_0,\ldots,a_7,b_0,\ldots,b_7\), with subscripts reduced modulo eight, and exactly the edges
\[
\{a_i a_{i+1},a_i b_i,b_i b_{i+3}:0\le i<8\}.
\]
A blue vertex with exactly one white neighbor may turn that neighbor blue. An initial subset is *zero forcing* when iterating this rule colors all sixteen vertices blue. A minimum zero-forcing set is a zero-forcing set of smallest cardinality. Each exchange move must preserve cardinality six and feasibility. The numerical conclusions refer to these *labeled* vertex subsets, without quotienting by graph automorphisms.

## Proof
This is an exact, finite exhaustive theorem, with two complete and executable enumeration proofs in `verify_primary.py` and `verify_alt.cpp`.

**Step 1: enumerate all feasible configurations.** Each six-subset of a fixed sixteen-element set appears once in a lexicographic combination enumeration, and each five-subset appears once in its corresponding enumeration. The two implementations construct the graph from the stated edge rule and use two different implementations of forcing closure. The first simultaneously applies all available unique-neighbor forces; the second applies one available force at a time. Because a force never changes a blue vertex back to white, every legal forcing order has the same terminal closure: if one terminal closure omits a white vertex, that stable set cannot be extended by any legal force, and a different legal ordering could not bypass it. Both computations find zero forcing five-subsets and exactly \(1,704\) forcing six-subsets. The existence of six-subsets proves \(Z(M)\le6\). Monotonicity of zero forcing under enlarging an initial subset ensures that the absence of forcing five-subsets also rules out sizes below five, hence \(Z(M)=6\).

**Step 2: construct all exchange edges.** Two distinct six-subsets are adjacent precisely when their intersection has five elements. The first program groups every six-set by its six contained five-faces and joins all configurations sharing a face; the second program directly toggles one selected and one unselected bit and tests membership. Each method accounts for all possible swaps and no non-swaps. Both return \(16,560\) undirected edges and the same full degree distribution.

**Step 3: certify every shortest-path distance.** For each of the \(1,704\) configurations, both programs perform ordinary breadth-first search in the complete exchange graph, assigning distance zero to the source and distance \(k+1\) when a new vertex is first discovered from a vertex at distance \(k\). The standard breadth-first-search induction shows that the first discovered distance is the exact graph distance. Every search reaches all \(1,704\) configurations and has maximum distance six, proving connectivity, radius six, and diameter six. Collecting distances only for indices \(i<j\) gives the displayed exact distance polynomial and its weighted sum \(5,453,976\).

**Step 4: compare against Johnson geometry.** Each exchange changes exactly one of the six selected elements, so any path from \(S\) to \(T\) has length at least \(6-|S\cap T|\). For each unordered pair, the programs compare the certified breadth-first-search distance with this lower bound. The excess histogram is exactly \((1,441,284,9,648,24)\) for excess zero, one, or two, respectively. The \(24\) excess-two pairs have ambient distance two. The alternate checker also counts their degree types and their incidences, showing that all \(48\) endpoints have degree sixteen and appear only once.

Completeness rests on enumerating all \(\binom{16}{5}=4,368\) five-subsets and all \(\binom{16}{6}=8,008\) six-subsets, followed by complete adjacency construction and all-root breadth-first searches. There is no sampling, floating-point arithmetic, or unproved infinite extrapolation.

## Verification
Run `python3 verify_primary.py` with Python's standard library. Separately compile and run `c++ -O3 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt`. Both were executed successfully from the submitted source contents. Both check the configuration count, edge count, connectivity, six-eccentricity assertion, exact degree/distance histograms, Wiener index, and Johnson-distance excess distribution; the second checker additionally verifies the \(24\) exceptional-pair endpoint incidences. The two forcing-closure strategies and edge-generation strategies are distinct.

## Relationship to prior work
The 2007 online publication of *Zero forcing sets and the minimum rank of graphs* introduced ordinary zero forcing. Alameda and collaborators (2018) and Rashidi–Poursalavati–Tavakkoli (2020) study zero forcing numbers for generalized Petersen graphs. Geneson–Haas–Hogben (2020, later journal publication) define the single-vertex-exchange zero forcing graph and determine structural properties for various families, particularly forests and specially constructed graphs. The 2026 paper by Krishnan revisits zero forcing numbers for the \(GP(n,3)\) family. None of the inspected material establishes this exact Möbius–Kantor minimum-set exchange graph's all-pairs distance/degree classification. The minimum-zero-forcing framework and the general definition of its exchange graph are **not** claimed as new.

## Limitations
The theorem is about one canonical sixteen-vertex graph and its finite exchange graph. It does not establish a general theorem for all generalized Petersen graphs or imply that every minimum-zero-forcing exchange graph is connected or self-centered. The exact finite proof is algorithmic and depends on replaying the supplied enumeration; the formulas are not derived from a closed symbolic classification of all six-subsets. Novelty remains subject to possible equivalent results in unindexed literature or an inaccessible full text of relevant contemporary work. No independent scholarly audit has been performed.

## References
1. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra Appl. 428 (2008), 1628–1648; available online 2007-11-26. DOI: 10.1016/j.laa.2007.10.009.
2. J. S. Alameda et al., *Families of graphs with maximum nullity equal to zero forcing number*, Special Matrices 6 (2018), 56–67. DOI: 10.1515/spma-2018-0006.
3. S. Rashidi, N. Shajareh Poursalavati and M. Tavakkoli, *Computing the zero forcing number for generalized Petersen graphs*, J. Algebra Combin. Discrete Struct. Appl. 7 (2020), 183–193. DOI: 10.13069/jacodesmath.729465.
4. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020); Discrete Appl. Math. (2023). DOI: 10.1016/j.dam.2023.01.027.
5. A. Krishnan, *A correction to the Zero Forcing Number of the Generalized Petersen Graphs P(n,3)*, arXiv:2607.19412 (2026); relevant full-text access remains uncertain.
