# Sharp edge general position and edge-geodesic cover in three Fibonacci cubes

## Finding

Let \(\Gamma_n\) be the \(n\)-dimensional Fibonacci cube, with vertices the binary strings of length \(n\) having no adjacent ones, and adjacent vertices differing in exactly one coordinate. For \(n\in\{6,7,8\}\), the edge-general-position and edge-geodesic-cover numbers are exactly
\[
\begin{array}{c|ccc}
n &6&7&8\\ \hline
\operatorname{gcover}_e(\Gamma_n)&8&13&21\\
\operatorname{gp}_e(\Gamma_n)&16&26&42
\end{array}.
\]
Equivalently, both identities \(\operatorname{gcover}_e(\Gamma_n)=F_n\) and \(\operatorname{gp}_e(\Gamma_n)=2F_n\) are established here for only the three asserted dimensions. Here \(F_0=0,F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). This verifies the next three cases beyond dimension five of Klavžar–Tan Conjecture 4.5; it is not a proof of that conjecture in all dimensions.

## Assumptions and scope

Graphs are finite, undirected and simple. A *geodesic* is a shortest vertex-to-vertex path. An *edge general position set* \(S\subseteq E(G)\) has \(|S\cap E(P)|\le2\) for every geodesic \(P\); \(\operatorname{gp}_e(G)\) is its maximum cardinality. An *edge-geodesic cover* is a family of geodesics whose union of edge sets equals \(E(G)\); \(\operatorname{gcover}_e(G)\) is its minimum cardinality. The result applies only to \(n=6,7,8\), not to arbitrary Fibonacci or Lucas cubes.

Each vertex is written as an ordinary left-to-right binary word. The certificate file `fibonacci_geodesic_certificate.json` gives, separately for each of the three dimensions, explicit ordered vertex sequences for \(F_n\) candidate geodesics. No unlisted auxiliary paths are assumed.

## Proof

**1. Geodesic characterization.** Every edge flips exactly one coordinate, so every path between binary strings \(u,v\) has length at least their Hamming distance \(d_H(u,v)\). Conversely, first clear all coordinates that are one in \(u\) and zero in \(v\), and then set all coordinates that are zero in \(u\) and one in \(v\). Clearing ones cannot create a forbidden adjacent-one pair; during the second phase the current one-set is always a subset of the one-set of \(v\), so that phase also remains within the Fibonacci cube. This gives a path of length exactly \(d_H(u,v)\), proving that Fibonacci-cube distance equals Hamming distance. Accordingly, if a sequence of Fibonacci strings changes one bit at every step and has exactly \(d_H(u,v)\) steps, it is a geodesic. In particular, any geodesic in a Fibonacci cube flips a given coordinate *at most once*: the number of steps equals the number of coordinates on which endpoints differ.

**2. Lower bound for the edge-geodesic cover.** There are exactly \(F_n\) edges flipping the first coordinate. Their endpoint with initial bit one must have second bit zero, while its remaining \(n-2\) bits form an arbitrary Fibonacci string. The number of such strings is \(F_n\). Since a geodesic flips the first coordinate at most once, any edge-geodesic cover must use at least \(F_n\) paths. Thus \(\operatorname{gcover}_e(\Gamma_n)\ge F_n\).

**3. Upper bound for the edge-geodesic cover: explicit finite witnesses.** For \(n=6,7,8\), use the respective lists of \(8,13,21\) vertex sequences in `fibonacci_geodesic_certificate.json`. Every listed vertex has length \(n\) and no adjacent ones. Each two consecutive words differs in exactly one coordinate, and each listed sequence has length exactly the Hamming distance between its endpoints. Consequently every listed sequence is a geodesic by Step 1. Regenerating the graph from all admissible binary strings gives respectively \(38,71,130\) edges; in each case the union of edges of the listed geodesics equals the entire graph edge set. These are finite, fully specified certificates; the standalone verifier reproduces each property. Therefore \(\operatorname{gcover}_e(\Gamma_n)\le F_n\) for the three stated dimensions, completing the first equality.

**4. Lower bound for edge general position.** The first-coordinate and last-coordinate edge sets are disjoint, and each has \(F_n\) members (by the same endpoint count and reversal). Let \(S\) be their union, hence \(|S|=2F_n\). Every geodesic changes each coordinate at most once, so it contains at most two edges of \(S\). Thus \(S\) is an edge general position set and \(\operatorname{gp}_e(\Gamma_n)\ge2F_n\).

**5. Upper bound for edge general position.** Fix any edge general position set \(X\). For any edge-geodesic cover \(\mathcal P\), every \(P\in\mathcal P\) contains at most two edges of \(X\), and every edge of \(X\) occurs on at least one member of the cover. Therefore
\[
|X|\le\sum_{P\in\mathcal P}|X\cap E(P)|\le2|\mathcal P|.
\]
Apply this inequality to the explicit \(F_n\)-path covers in Step 3. The result is \(\operatorname{gp}_e(\Gamma_n)\le2F_n\), matching Step 4. This proves both equalities with all quantifiers restricted to \(n\in\{6,7,8\}\).

## Verification

Run from a directory containing the accompanying files:

```sh
python verify_fibonacci_geodesics.py fibonacci_geodesic_certificate.json
```

The verifier independently generates all binary strings of each length, tests adjacency by one-bit changes, reconstructs all edges, checks every certificate vertex and path, checks endpoint Hamming distance against path length, and asserts complete edge coverage. It independently counts first- and last-coordinate edge sets. It checks every path explicitly rather than trusting a solver status or a summary log. Expected graph orders are \(21,34,55\); edge counts are \(38,71,130\); geodesic-cover cardinalities are \(8,13,21\). An additional independent breadth-first-search comparison of certificate endpoint distances was performed for all \(42\) listed geodesics. All checks agreed.

The proof is not an extrapolation from empirical data: finitely many explicit paths supply the necessary mathematical upper-bound witnesses, and the lower bounds hold for every choice of geodesic cover or edge general position set in each finite graph.

## Relationship to prior work

Klavžar and Tan (2023), Theorem 4.3, established the universal \(2F_n\) lower bound and maximality of the union of two extremal coordinate classes. Their Proposition 4.4 established the value ten in dimension five; their Conjecture 4.5 posits equality in all dimensions. The present claim adds only dimensions six through eight and a matching exact edge-geodesic-cover result.

Manuel, Prabha and Klavžar (2022), Lemma 2.4, give the general cover/general-position inequality used in Step 5. That inequality is **not** asserted to be new. Their treated network families include hypercubes, torus networks and Beneš networks; the Fibonacci-cube cover witnesses supplied here are not part of those stated results. Tian, Klavžar and Tan (2024) study different graph classes, including block graphs and extremal edge-general-position cases, and do not state this three-dimension result. Source and equivalence searches found no covering assertion in the inspected material, but absence of a search hit is not proof of novelty.

## Limitations

No statement for dimension nine or higher is proved; the general Klavžar–Tan conjecture remains unproved by this finding. The construction is a finite explicit witness, not a structural formula for covers in arbitrary dimension. Proof correctness can be checked from the supplied standard-library verifier and path certificate, but no independent scientific validation or comprehensive historical priority determination has been conducted. Relevant unindexed work or a stronger theorem may still exist.

## References

1. S. Klavžar and E. Tan, *Edge General Position Sets in Fibonacci and Lucas Cubes*, Bulletin of the Malaysian Mathematical Sciences Society 46, Article 120 (2023), Theorem 4.3, Proposition 4.4, Conjecture 4.5. First preprint: arXiv:2304.10114v1 (20 April 2023); https://doi.org/10.1007/s40840-023-01517-y.
2. P. Manuel, R. Prabha and S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357v1 (15 July 2022), especially Lemma 2.4; https://arxiv.org/abs/2207.07357.
3. J. Tian, S. Klavžar and E. Tan, *Extremal Edge General Position Sets in Some Graphs*, Graphs and Combinatorics 40, Article 40 (2024); https://doi.org/10.1007/s00373-024-02770-z.
