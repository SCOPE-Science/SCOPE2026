# Sharp ten-vertex limit of mean-outbreak source identifiability on trees

## Finding

**Theorem (exact finite-tree source identifiability).** Let \(T\) be a known, finite, simple, connected, unweighted tree with \(1\le n\le10\) vertices. Independently retain each edge with the same probability \(p\in[0,1]\), and write \(X_v(p)\) for the size of the retained-edge component containing the initially infected/source vertex \(v\), including \(v\). Write \(M_v(p)=\mathbb E[X_v(p)]\) and \(V_v(p)=\operatorname{Var}(X_v(p))\).

1. For \(n\le9\), \(M_u(p)=M_v(p)\) for every \(p\in[0,1]\) **if and only if** a tree automorphism sends \(u\) to \(v\).
2. For \(n=10\), precisely **two unordered pairs of distinct source automorphism orbits**, each in a different tree isomorphism class, have identical entire mean curves. Thus ten is the least tree order at which the complete expected-outbreak curve fails to identify a source up to inherent symmetry.
3. For **every** tree on at most ten vertices, the pair consisting of the full mean-outbreak curve \(M_v(\cdot)\) and the single variance \(V_v(1/2)\) distinguishes the source up to tree automorphism. The two ten-vertex exceptional pairs have nonzero, exactly calculated variance gaps of magnitude \(21/128\) and \(1/16\), respectively.

A concrete first witness is the ten-vertex tree with edges

```text
(0,1) (0,5) (0,8) (1,2) (2,3) (3,4) (5,6) (6,7) (8,9)
```

The nonautomorphic source vertices \(2\) and \(8\) have exactly the same expected outbreak for every transmissibility,

\[M_2(p)=M_8(p)=1+2p+2p^2+2p^3+2p^4+p^5.\]

But their half-transmissibility outbreak-size laws, for sizes \(1,2,\ldots,10\), have integer numerators over \(512\), respectively

```text
source 2: 128 128 112 56 32 26 17 9 3 1
source 8: 128 160  64 56 44 32 17 7 3 1
```

Consequently \(M_2(1/2)=M_8(1/2)=93/32\), while \(V_2(1/2)-V_8(1/2)=-21/128\). In a second ten-vertex tree with edges

```text
(0,1) (0,6) (0,9) (1,2) (1,4) (2,3) (4,5) (6,7) (6,8)
```

sources \(0\) and \(1\) have identical curves \(1+3p+4p^2+2p^3\), but \(V_0(1/2)-V_1(1/2)=1/16\).

## Assumptions and scope

The graph is a **known** unweighted tree. Source location is unknown, and vertices identified by automorphisms of the known graph are legitimately indistinguishable by any graph-invariant statistic. Retained contacts are **independent Bernoulli variables on undirected edges** with common probability \(p\). The observation is only terminal outbreak size, not infection time, path, or affected identities. “Complete mean curve” means exact values for every real \(p\in[0,1]\), equivalently its polynomial coefficients; it is not inferred from a finite noisy sample. The variance is observed exactly at \(p=1/2\). All quantifiers in the theorem are restricted to trees with \(n\le10\). The finding is a mathematical fact about the independent-edge epidemic representation; it is not claimed for general stochastic SIR models with correlated transmissibilities.

## Proof

**Step 1: exact connection to a classical distance invariant.** In a tree, exactly one simple path joins source \(v\) and target \(w\). The event that the latter lies in the same retained-edge component is exactly the event that every edge on that path is retained, of probability \(p^{d(v,w)}\). Thus, with \(a_k(v)=|\{w:d(v,w)=k\}|\),

\[M_v(p)=\sum_{w\in V(T)}p^{d(v,w)}=1+\sum_{k=1}^{n-1}a_k(v)p^k.\]

Polynomial identity makes equality for all \(p\) **equivalent** to equality of the complete distance-degree sequences. This identity is previously known as decay centrality (plus one); the new claim does not assert otherwise.

**Step 2: finite exhaustive classification with no missing trees or root orbits.** Encode a rooted tree recursively as a balanced-parenthesis word: the root's word is an opening parenthesis, then the recursively encoded rooted child subtrees sorted lexicographically, then a closing parenthesis. This encoding is complete and unique up to rooted graph isomorphism: induction on order proves that rooted trees correspond bijectively to multisets of already-coded smaller rooted trees whose sizes sum to one less than the total order. The standalone code constructs exactly these multisets for every order through ten. Its rooted-tree type counts are

\[(1,1,2,4,9,20,48,115,286,719).\]

To forget the root, decode one representative and compute the rooted canonical code at **every** vertex. The lexicographically least such code is a complete invariant of the underlying unrooted tree. Grouping by this code produces unrooted-tree counts

\[(1,1,1,2,3,6,11,23,47,106).\]

For each fixed free-tree class, distinct rooted canonical codes are precisely the vertex automorphism orbits. For each orbit compute its exact breadth-first-search distance histogram \((a_0,\ldots,a_{n-1})\). Grouping these histograms within each free-tree class yields **no** equal-histogram pairs through order nine and exactly **two** pairs at order ten. Their distinct rooted codes and distance histograms are reproduced in `certificate.json`; the executable proof-by-exhaustive-classification is `check_source.py`. These computations are finite and complete **because** the recursive generator covers all rooted trees; they do not purport to classify larger trees.

**Step 3: the second moment separates every exceptional pair.** For each of the two size-ten pairs, independently enumerate all \(2^9=512\) edge-retention masks and count the size of the component of the encoded source root. At probability one-half, each mask has probability \(1/512\). The first exceptional pair has raw first-moment numerators \(1488,1488\) and raw second-moment numerators \(6032,6116\); the second has first-moment numerators \(1920,1920\) and second-moment numerators \(9088,9120\). Since the first moments agree inside each pair, subtracting squared means gives variance differences \(-84/512=-21/128\) and \(-32/512=-1/16\) in the canonical certificate ordering. Every nonexceptional pair of nonautomorphic source orbits has different mean polynomials; the two exceptional pairs are separated by variance. This completes all three statements.

## Verification

Run `python3 check_source.py` using Python 3 standard library. Compare its exact UTF-8 output including the final line feed with `certificate.json` (`python3 check_source.py > replay.json && cmp replay.json certificate.json`). No third-party package or external data is needed. The program constructs all rooted trees to order ten, forms unrooted equivalence classes, computes every rooted distance histogram, finds all collisions, and for the exceptional pairs enumerates every retained-edge mask. The package's exact outputs independently match a separate unrooted-tree enumeration and direct enumeration on the explicit labeled witness. The program is an exhaustive **finite proof certificate** alongside the induction argument establishing coverage of its enumeration; its tests alone say nothing about order eleven or above.

## Relationship to prior work

Newman (2002) presents epidemic/bond-percolation connections and mean outbreak statistics: this supplies the epidemiological model, not a classification of indistinguishable sources within finite known trees. The coefficients in the displayed mean polynomial are the established *distance-degree sequence* / *decay centrality* (Hurajová, Gago, and Madaras, 2018; Huilgol, 2014). Their mathematical identity is prior work, not an originality claim. In particular, Huilgol discusses nonisomorphic trees with matching aggregate distance-degree information, a **different** question from two nonautomorphic source vertices of a single known tree; see also Slater's graph-invariant literature cited there. Work on network source localization such as Shah–Zaman (2011) observes infected subgraphs or diffusion histories, not only an exact curve of expected total outbreak sizes. The new contribution here is restricted to the sharp small-tree within-network source-orbit cutoff and the exact half-transmissibility variance that eliminates its two exceptions. Poklukar–Žerovnik (2025, 2026) investigate decay-centrality ranking stability; the former accessible text does not give this source-orbit cutoff. The latter's abstract was accessible, but its complete technical proof was not, and equivalent prior coverage cannot be ruled out without further bibliography review.

## Limitations

The result concerns exact source identifiability on **known** trees of order ten or less under independently open undirected contacts. It does not establish novelty or source identification for arbitrary graphs, larger trees, incomplete mean measurements, finite-data estimation, heterogeneous transmissibility, or all SIR mechanisms. The distance-polynomial equality is known mathematics; originality is only the finite sharp classification and variance separation. A human/independent literature examination of historical distance-degree and decay-centrality enumerations is not yet performed.

## References

1. M. E. J. Newman, “Exact solutions of epidemic models on networks,” first public arXiv posting 2002-01-24, https://arxiv.org/abs/cond-mat/0201433 .
2. J. Coroničová Hurajová, S. Gago, T. Madaras, “On decay centrality in graphs,” *Mathematica Scandinavica* 123 (2018), 39–50, https://doi.org/10.7146/math.scand.a-106210 .
3. M. I. Huilgol, “Distance Degree Regular Graphs and Distance Degree Injective Graphs: An Overview,” *International Journal of Mathematics and Mathematical Sciences* (2014), article 358792, https://doi.org/10.1155/2014/358792 .
4. D. Shah, T. Zaman, “Finding Rumor Sources on Random Trees,” arXiv posting 2011-10-28, https://arxiv.org/abs/1110.6230 .
5. D. Rupnik Poklukar, J. Žerovnik, “Generalized Closeness and Decay Stability of Some Graphs,” *Mathematics* 13 (2025), 939, https://doi.org/10.3390/math13060939 .
6. D. Rupnik Poklukar, J. Žerovnik, “Almost all trees are decay-unstable,” *Mathematica Scandinavica* 132 (2026), 1–16, https://doi.org/10.2140/mscand.2026.132.1 (abstract inspected, complete text not accessed).
