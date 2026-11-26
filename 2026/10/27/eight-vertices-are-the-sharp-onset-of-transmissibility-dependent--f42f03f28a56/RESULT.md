# The two eight-vertex trees with transmissibility-dependent optimal vaccination

## Finding

Among the 23 unlabelled trees on eight vertices, exactly two have no single vertex that minimizes the expected final outbreak size at every transmissibility after perfect vaccination of one vertex. In the following labelled representatives the sets of minimizing vertices are exact:

- **Broom**, with edges \((1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(6,7)\). Let \(\rho\in(0,1)\) be the unique solution of \(\rho^3+\rho^2=1\). The optimum is \(\{2\}\) for \(p<\rho\), \(\{1\}\) for \(p>\rho\), and \(\{1,2\}\) at \(p=\rho\).
- **Double-broom**, with edges \((1,0),(1,2),(2,3),(2,4),(0,5),(5,6),(5,7)\). The optimum is \(\{2,5\}\) for \(p<1/\sqrt{2}\), \(\{0,1\}\) for \(p>1/\sqrt{2}\), and \(\{0,1,2,5\}\) at equality.

The broom is the previously documented witness that a switch can occur at order eight. The result here is the complete classification at that order, including the second switching tree and its distinct threshold.

## Assumptions and scope

The tree is finite, simple, undirected and unweighted. Vaccination deletes one chosen vertex \(v\) and its incident edges before a seed is chosen uniformly from the remaining vertices. The outbreak is the seed's open component after independent Bernoulli edge opening with the same probability \(p\in(0,1)\) on every remaining edge. Final outbreak size includes the seed. A universal optimum is a vertex minimizing the mean outbreak size for every \(p\) in this open interval. Isomorphism types are unlabelled; the vertex numbers above are only for specifying the optimizer sets in the two representatives.

## Proof

**Objective polynomial.** For a chosen vertex \(v\), let \(a_{v,j}\) be the number of ordered pairs of distinct vertices at distance \(j\) in a common component of \(T-v\). Let \(W_v(p)=\sum_{j=1}^6 a_{v,j}p^j\). Each pair in the same component is connected in the open graph precisely when all edges on its unique path are open; all other pairs have connection probability zero. Summing over targets and averaging over the seven possible seeds gives the exact expected final size \(1+W_v(p)/7\). Thus the optimizers are precisely the minimizers of \(W_v(p)\).

**Complete census.** Every labelled tree of order eight occurs once among the Prüfer sequences of length six with entries in \(\{0,\ldots,7\}\). To gather the unlabelled types, repeatedly remove leaves to find the one or two centers. Encode a rooted tree by enclosing the sorted list of child encodings in parentheses. For a tree with two centers, remove their common edge and take the sorted pair of rooted encodings of the halves. The rooted encoding is complete by induction on the number of vertices, while the center set is preserved by isomorphisms; separate one-center and two-center encodings therefore identify exactly the unlabelled types.

For each canonical type and each deletion, compute the coefficients by breadth-first enumeration of the distances in \(T-v\). Given \(F(p)=W_w(p)-W_v(p)=\sum_{j=1}^6 c_jp^j\), substitute \(p=t/(1+t)\) and multiply by \((1+t)^6\). The coefficient of \(t^i\) is \(\sum_{j=1}^i c_j\binom{6-j}{i-j}\). If all these coefficients are nonnegative, then \(W_v\le W_w\) on the full open interval. This is a sufficient test, not a necessary one. Applied against every competing \(w\), the exact integer test certifies one or more universal optima on 21 of the 23 types. The two remaining encodings are those of the displayed broom and double-broom. This finite census is reproducible with `verify.py`, which includes the Prüfer enumeration, canonical encoding, distance counts and coefficient tests. No conclusion about nonexistence of a universal optimum is drawn merely from failure of the sufficient test.

**Broom.** The distance polynomials at the two candidates are
\[
W_2=8p+6p^2+4p^3+2p^4,\qquad W_1=10p+6p^2+2p^3.
\]
The other differences from \(W_1\) are

| Vertex \(w\) | \(W_w-W_1\) |
|---|---|
| \(0\) | \(2p^2(1-p)\) |
| \(3,4\) | \(2p+4p^2+6p^3+6p^4+4p^5+2p^6\) |
| \(5\) | \(2p^2+2p^3\) |
| \(6\) | \(4p^2+4p^3+4p^4\) |
| \(7\) | \(2p+6p^2+6p^3+6p^4+4p^5\) |

All are positive on \((0,1)\). The remaining difference \(W_1-W_2=2p(1-p^2-p^3)\) has precisely one interior zero, since \(p^2+p^3\) increases strictly from zero to two over \([0,1]\). Its sign gives the optimizer sets as stated.

**Double-broom.** The two degree-three vertices and the two intermediate vertices are paired by the reversal symmetry. Their polynomials are
\[
W_2=W_5=8p+8p^2+4p^3,\qquad W_1=W_0=10p+8p^2.
\]
For each leaf \(w\), the difference \(W_w-W_1=2p+4p^2+8p^3+6p^4+4p^5\) is strictly positive. Finally, \(W_1-W_2=2p(1-2p^2)\). It is positive below \(1/\sqrt2\), zero there, and negative above, proving the optimizing sets and the four-way tie. For each of the two trees the sets on opposite sides of the switch are disjoint, so neither has a universal optimum. This completes the census.

## Verification

The accompanying standard-library Python 3 checker `verify.py` implements exact integer coefficient tests and rational-parameter comparisons. Run `python3 verify.py` with assertions enabled. The unlabelled type counts at orders two through eight are \(1,1,2,3,6,11,23\). At order eight it certifies 21 types, identifies the two remaining types with the edge lists in the Finding, and checks that their optimizing sets at \(p=1/2\) and \(p=9/10\) are disjoint. The tables and factorizations above give the exact interior optimizer sets, not just the two rational comparisons.

## Relationship to prior work

*Sharp eight-vertex onset of transmissibility-dependent optimal vaccination on contact trees* proves universal optimality through order seven, the switch on the eight-vertex spider with arms \((1,1,5)\) (the broom above), and analogous switches on spiders of larger orders. The threshold theorem and that witness are not new claims of this result. *Eight vertices are sharp for a transmissibility-dependent vaccination target on trees* gives the same eight-vertex witness under the same vaccination and seed convention. A general broom-family analysis also includes that witness. None of those stated witness results gives the exhaustive order-eight census or the double-broom transition.

Holme computes exact vaccination means for connected graphs through order seven under continuous-time Markov SIR. On a tree, the matched marginal probability of transmission along a specified edge is \(p=\beta/(\beta+\gamma)\) for infection and recovery rates \(\beta,\gamma\). Along a path, different vertices are the transmitters, yielding path probability \(p^j\) and the same mean objective; the joint outbreak laws need not coincide. This low-order/model connection does not classify the eight-vertex cases.

## Limitations

The classification is for order eight, one perfectly removed vertex, a uniform remaining seed and homogeneous edge probabilities, and does not describe all larger trees, multiple interventions or other outbreak objectives. The cited comparisons do not exclude equivalent unindexed work.

## References

1. *Sharp eight-vertex onset of transmissibility-dependent optimal vaccination on contact trees*, https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-sharp-eight-vertex-onset-of-transmissibility-dependent-optimal-v--639f57a81324.
2. *Eight vertices are sharp for a transmissibility-dependent vaccination target on trees*, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-eight-vertices-are-sharp-for-a-transmissibility-dependent-vaccin--9ba80a93d3d8.
3. *A single irreversible vaccination-site transition on broom trees*, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-single-irreversible-vaccination-site-transition-on-broom-trees--11637719c3c8.
4. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, Phys. Rev. E **96** (2017), 062305, https://arxiv.org/abs/1708.06456.
