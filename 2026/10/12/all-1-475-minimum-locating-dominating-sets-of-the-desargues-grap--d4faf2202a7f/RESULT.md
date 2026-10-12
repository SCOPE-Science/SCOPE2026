# All 1,475 minimum locating-dominating sets of the Desargues graph

## Finding

**Theorem.** Let \(D\) be the twenty-vertex Desargues graph, equivalently the incidence graph of the Desargues \(10_3\) configuration or the bipartite Kneser graph \(H(5,2)\). The location-domination number is \(\lambda(D)=8\). Exactly \(1{,}475\) sets of eight vertices are locating-dominating; under the full automorphism group, these sets form thirteen orbits with respective sizes
\[
5,\ 30,\ 60,\ 60,\ 120,\ 120,\ 120,\ 120,\ 120,\ 120,\ 120,\ 240,\ 240.
\]
The split between the two bipartition sides is \(3+5\) for \(300\) optimal sets, \(4+4\) for \(875\), and \(5+3\) for \(300\). All thirteen orbits are explicitly represented below.

## Assumptions and scope

Let \(U=\{1,2,3,4,5\}\), and let \(E=\binom{U}{2}\) be its ten unordered pairs. The vertices of \(D\) are \(L_e,R_e\), for \(e\in E\), with \(L_eR_f\) an edge exactly when \(e\cap f=\varnothing\). The vertex \(R_e\) can equivalently be identified with the three-subset \(U\setminus e\), giving the usual point-line inclusion realization. In this paper an *ordinary locating-dominating set* \(C\subseteq V(D)\) means that the sets \(N_D(v)\cap C\) are **nonempty and pairwise different for all distinct \(v\notin C\)**. No condition is imposed on distinguishing vertices already inside \(C\). This differs from identifying codes, which distinguish all vertices using closed neighborhoods, and from total locating domination.

Order the elements of \(E\) as \(12,13,14,15,23,24,25,34,35,45\). For a ten-bit integer \(s\), write \(L(s)\) for the left vertices whose edge positions have a set bit, and similarly \(R(t)\) for a ten-bit integer \(t\). A pair \((s,t)\) represents the set \(L(s)\cup R(t)\). A hexadecimal numeral is interpreted as its exact ten-bit integer; leading zeros are irrelevant.

## Proof

**The lower bound.** Locating-domination is monotone under addition of code vertices: adding a vertex to a locating-dominating set leaves fewer unselected vertices and cannot turn two different nonempty signatures into equal ones. Thus to rule out every size below eight it suffices to rule out seven-vertex codes. Suppose \(C\) has seven vertices, with \(a\) in the \(L\)-side and \(b=7-a\) in the \(R\)-side. The \(10-b=3+a\) unselected right vertices must have different nonempty subsets of the \(a\) selected left vertices as signatures. Hence \(3+a\le 2^a-1\), impossible for \(a\le2\). The symmetric argument gives \(b\ge3\). Up to exchanging sides, \((a,b)=(3,4)\).

For \(a=3\), the six unselected right vertices occupy six distinct nonempty signatures among the seven subsets of a three-set. The sum of the signature sizes is therefore at least \(3\cdot1+3\cdot2=9\). The three selected left vertices have exactly nine incident edges in total, so equality must hold. The signatures are precisely the three singletons and the three doubletons, and none has size three; additionally all neighbors of the selected left vertices are unselected right vertices. Interpret the three selected left vertices as three distinct edges of \(K_5\). Every pair has a common right neighbor, so each pair of these edges intersects. A pairwise-intersecting triple of distinct edges is either a three-edge star or the edges of a triangle. In the triangle case the two remaining labels form a right edge disjoint from all three chosen left edges, yielding the forbidden size-three signature. The chosen left edges therefore form a three-edge star centered at a label \(x\). Their neighbors comprise all six right vertices indexed by edges not incident with \(x\). Since these are exactly the six unselected right vertices, the four selected right vertices must be the four edges incident with \(x\). The fourth star edge \(L_{xy}\) that was not selected on the left has no selected right neighbor, violating domination. Hence no seven-vertex locating-dominating set exists.

**Sharpness.** For any \(x\in U\), select the four edges incident with \(x\) on each side, forming an eight-vertex set \(C_x\). Each unselected left or right vertex is indexed by an edge \(e\) of \(K_5\) not containing \(x\), and its signature is the pair of chosen opposite-side star edges with endpoints in \(U\setminus(e\cup\{x\})\). These signatures are nonempty and uniquely recover \(e\); signatures on opposite sides are supported on disjoint selected bipartition classes and are therefore different. Thus all five \(C_x\) are locating-dominating and \(\lambda(D)=8\).

**Exact census and orbit classification.** For each \(e\in E\) define the ten-bit mask \(P_e\) of those \(f\in E\) disjoint from \(e\). Let \(s,t\) be ten-bit masks of selected left and right vertices, respectively. By the definition above, \(C=L(s)\cup R(t)\) is locating-dominating **if and only if** each of the lists
\[
\{P_e\mathbin{\&}t:e\in E,\ s_e=0\},\qquad
\{P_e\mathbin{\&}s:e\in E,\ t_e=0\}
\]
contains only nonzero, pairwise distinct integers. Here \(s_e\) and \(t_e\) are the indicator bits at edge \(e\), and \(\mathbin{\&}\) denotes bitwise intersection of the fixed edge-index masks. Indeed these are exactly the open-neighborhood signatures of unselected left and right vertices, and nonempty signatures on different sides automatically differ because they lie on disjoint selected sides.

This gives a complete finite decision criterion on exactly \(2^{20}\) candidates. The attached self-contained verifier implements this criterion and a second direct twenty-vertex neighborhood predicate, compares both on every candidate, and enumerates all \(\binom{20}{8}\) eight-vertex possibilities without pruning. It finds precisely \(1{,}475\) valid eight-vertex masks, with left-size multiplicities \(300,875,300\) for sizes three, four and five. This is an exhaustive, finite exact enumeration, **not an inference from sample data**.

The full automorphism group has order \(240\) and is \(S_5\times C_2\): permutations of the five labels act simultaneously on left and right, and the involution interchanges \(L_e\) with \(R_e\). To see completeness, a side-preserving automorphism must induce an automorphism of the distance-two graph on a side; that graph is the line graph of \(K_5\), whose five maximum cliques of size four are the stars centered at individual labels. Thus every side-preserving automorphism induces a permutation of those five labels, and the unique neighborhoods force the same permutation on both sides. The bipartition-exchanging involution supplies the other coset.

For each of the \(1{,}475\) valid masks the verifier constructs its orbit under these \(240\) transformations, then partitions the full set into exactly the thirteen orbits in the following table. The \(s,t\) columns are in the fixed ten-bit convention above, and are complete reproducible representatives.

| Representative \(s\) | Representative \(t\) | Orbit size |
|:--|:--|--:|
| `0x00f` | `0x00f` | 5 |
| `0x095` | `0x036` | 30 |
| `0x017` | `0x017` | 60 |
| `0x01b` | `0x017` | 60 |
| `0x01f` | `0x007` | 120 |
| `0x037` | `0x015` | 120 |
| `0x06b` | `0x015` | 120 |
| `0x027` | `0x017` | 120 |
| `0x02b` | `0x01d` | 120 |
| `0x207` | `0x01d` | 120 |
| `0x0c3` | `0x03a` | 120 |
| `0x03b` | `0x015` | 240 |
| `0x02b` | `0x017` | 240 |

The orbit sizes sum to \(1{,}475\). Since every possible optimum mask is tested and the orbits partition exactly those masks, this proves both the cardinality and the complete orbit classification. The first orbit consists of the five symmetric star codes \(C_x\).

## Verification

Run `python3 verify.py` with Python 3.8 or later; only the standard library is used. It constructs the graph from the stated five-symbol pair model, independently tests all \(2^{20}\) masks using the raw twenty-vertex adjacency relation and the two side-projection criterion, confirms the minimum and every cardinality-eight mask, computes the split counts, enumerates \(120\) label permutations together with the bipartition swap, and checks all thirteen canonical representative masks and their orbit sizes. The exact expected success output is included in `VERIFICATION.md`. Proof of the lower bound is independent of computation; the finite census is an exact computer-assisted proof with the entire search space exhausted.

## Relationship to prior work

Hernando, Mora and Pelayo (2015) define ordinary location-domination in bipartite graphs and study general relations to the complement graph and global location-domination. Their work fixes the terminology and provides general tools, but its inspected full text does not enumerate minimum codes in the Desargues graph. Stroppel and Stroppel (2012) describe the Desargues point-line configuration as incidence between two- and three-subsets of a five-set and establish its geometric symmetries; the incidence representation is standard and is not claimed as new. Existing databases record the Desargues graph and its group of order \(240\), without providing the thirteen classes of minimum locating-dominating sets. Bousquet and collaborators' general identifying-code study concerns a distinct, stronger condition requiring all graph vertices to be identified; the locating-dominating census here does not follow from a count of identifying codes. Related published work on generalized Petersen graphs or other domination parameters should not be conflated with ordinary location-domination.

## Limitations

This is a finite classification for the single twenty-vertex Desargues graph, not a formula for every bipartite Kneser graph or every generalized Petersen graph. The exact count and orbit table use a short exhaustive verifier rather than a closed, non-computational enumeration of the thirteen types. A literature search cannot rule out a previous equivalent table under incidence-geometric, test-cover, or related vocabulary. Broader historical surveys of identification, including some inaccessible materials, remain priority risks; the present proof is independent of them. The theorem does not claim originality of the graph model, its automorphism group, or the location-domination definition.

## References

1. C. Hernando, M. Mora and I. M. Pelayo, *On global location-domination in bipartite graphs*, arXiv:1506.03442v1 (first posted June 10, 2015). https://arxiv.org/abs/1506.03442
2. B. Stroppel and M. Stroppel, *Desargues, Doily, Dualities, and Exceptional Isomorphisms*, Mathematische Berichte 2012/017, Universität Stuttgart (2012). https://www.f08.uni-stuttgart.de/.content/media/downloads/Mathematik/mathematische_berichte/2012/2012-017.pdf
3. C. Hernando et al., *Locating domination in bipartite graphs and their complements*, arXiv:1711.01951v1 (2017). https://arxiv.org/abs/1711.01951
4. N. Bousquet et al., *Identifying codes in hereditary classes of graphs and VC-dimension*, arXiv:1407.5833v1 (2014). https://arxiv.org/abs/1407.5833
5. E. W. Weisstein, *Desargues Graph*, MathWorld (graph identification and classical structural parameters). https://mathworld.wolfram.com/DesarguesGraph.html
