# All seventy minimum feedback-vertex sets of the Heawood graph

## Finding

Let \(H\) be the Heawood graph: the incidence graph of the seven points and seven lines of the Fano plane. A **feedback vertex set** (also called a decycling set) is a vertex set \(S\subseteq V(H)\) such that the vertex-induced complement \(H-S\) is a forest. For every minimum feedback vertex set \(S\) of \(H\), precisely one of the following mutually exclusive descriptions holds:

1. **Type A:** \(S\) consists of the four point-vertices outside a Fano line, or dually of the four line-vertices not passing through a Fano point. There are exactly \(14\) such sets.
2. **Type B:** \(S\) consists of one line-vertex together with three of the four point-vertices off that line, or dually of one point-vertex together with three of the four line-vertices not incident with that point. There are exactly \(56\) such sets.

Conversely, every set in these descriptions is a minimum feedback vertex set. In particular,
\[
\nabla(H)=4,\qquad \#\{S\subseteq V(H): |S|=4,\ H-S\text{ acyclic}\}=70.
\]
Every optimal complement is a connected induced **tree on ten vertices**. Type A leaves a tree with four degree-three vertices and six leaves. Type B leaves a tree whose one degree-three vertex is joined to each of three leaves by a path of length three; its degree counts are \(n_1=3\), \(n_2=6\), and \(n_3=1\). The two types are exactly two orbits, of respective sizes \(14\) and \(56\), under the full graph automorphism group of order \(336\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Label the Fano points by the nonzero vectors of \(\mathbf F_2^3\); each line has the form \(\{a,b,a+b\}\) for distinct nonzero vectors \(a,b\). The Heawood graph has one vertex per point and line and one edge for each point-line incidence. Thus it is cubic, with \(14\) vertices and \(21\) edges. A set is minimum if its cardinality is least among all feedback vertex sets, not merely inclusion-minimal.

The classification is exact for this one graph, with every subset counted as an unlabelled set of the specified fourteen *distinguishable* point/line vertices. The graph is not being varied with any parameter.

## Proof

**1. Sharp lower bound and a tightness criterion.** Suppose that \(S\) has \(k\) vertices and induces \(e(S)\) edges. Deleting \(S\) removes exactly \(3k-e(S)\) edges. Thus \(H-S\) has \(14-k\) vertices and \(21-3k+e(S)\) edges. If it is a forest with \(c\) connected components, the forest edge identity yields
\[
21-3k+e(S)=(14-k)-c,
\qquad c=2k-7-e(S).
\]
Since a nonempty forest has \(c\ge1\), no set of at most three vertices can decycle \(H\). If \(k=4\), the identity forces \(c=1\) and \(e(S)=0\). Hence every optimal four-vertex feedback set is an **independent** set and leaves one induced tree. Conversely, any independent four-vertex set whose complement is connected is a feedback vertex set, because the complement then has ten vertices and nine edges.

**2. Four point-vertices, and its dual.** Let \(S\) contain four points and no lines. The three retained points either lie on one line or are noncollinear. If noncollinear, the three pair-joining lines and the three points form a six-cycle, so the complement is not acyclic. If collinear on a line \(\ell\), that line remains adjacent to all three points and each of the six other Fano lines meets exactly one retained point. The complement is therefore a ten-vertex tree: \(\ell\) is joined to three degree-three points, each with two pendant line-vertices. Each of the seven choices of \(\ell\) gives one admissible \(S\). Point-line duality gives seven four-line sets. These are the \(14\) type-A sets, with six degree-one and four degree-three vertices in the complement.

**3. Three point-vertices and one line-vertex, and its dual.** Let \(S\) delete three points and a line \(\ell\). Independence requires all three deleted points to be among the four points **outside** \(\ell\). Let \(q\) be the remaining off-line point. The surviving vertices are \(q\), the three points of \(\ell\), and the six line-vertices other than \(\ell\). Each of the three lines through \(q\) meets \(\ell\) at a different point (the Fano projective-plane axiom). These are three length-two paths from \(q\) to the three surviving points on \(\ell\). Each of those on-line points lies on exactly one further surviving line not through \(q\), which is a leaf because its other two points were deleted. Thus the complement is the tree formed by three vertex-disjoint length-three arms emanating from \(q\). There are \(7\cdot4=28\) choices of \(\ell\) and omitted fourth off-line point \(q\). Exchanging points with lines contributes another \(28\), giving \(56\) type-B sets.

**4. Two points and two lines are impossible.** Suppose \(S\) contains distinct point-vertices \(a,b\) and distinct line-vertices, and \(S\) is independent. Exactly two Fano lines avoid both \(a\) and \(b\): call them \(\ell_1,\ell_2\). They are therefore precisely the deleted lines. Let \(r\) be the third point on the unique line \(m\) through \(a,b\). The two other lines through \(r\) are \(\ell_1,\ell_2\), so \(r\) and \(m\) form an isolated two-vertex connected component in \(H-S\). This contradicts the necessary connectedness from step 1. No independent two-and-two split can be optimal.

These five split possibilities (four and zero, three and one, two and two, and their duals) exhaust every independent four-vertex set, proving the entire classification and count.

**5. Full symmetry and the two orbits.** Every automorphism preserves or interchanges the two sides of the connected bipartite graph. On the point side, an incidence-preserving automorphism is a collineation of the Fano plane; all such collineations form \(\operatorname{GL}(3,2)\), with order \(168\). A point-line polarity exists and swaps the sides, so the full automorphism group has order \(336\). It is transitive on lines and on anti-flags, i.e. nonincident point-line pairs. Type A is determined by a line or its dual point, and is one orbit of size \(14\). Type B is determined by a line together with the unique retained point off it (an anti-flag), or its dual, and is one orbit of size \(56\). Their complements have different degree distributions, so the two orbits cannot merge.

## Verification

The accompanying standalone Python 3 verifier, `verify.py`, constructs the Fano incidence table directly from nonzero binary triples, enumerates **all** \(2^{14}=16{,}384\) vertex subsets, and checks acyclicity, all seventy optimal sets against the two described types, the two complementary tree degree distributions, and both automorphism orbits. It enumerates the \(168\) invertible linear maps and a point-line polarity to obtain \(336\) verified automorphisms. Run `python3 verify.py` in the same directory. Its expected summary is:

```
VERIFY_OK vertices=14 edges=21 masks=16384 optimum=4 minimum_sets=70
VERIFY_OK orbit_types=A:14,B:56 group_order=336 tree_degrees=A:(1^6,3^4),B:(1^3,2^6,3^1)
```

The mathematical proof above establishes the classification without relying on exhaustion. Exhaustive enumeration is a separate finite consistency check and applies only to the stated fourteen-vertex graph.

## Relationship to prior work

A feedback vertex set is the complement of an induced forest, and the lower bound for cubic decycling sets is standard. Bau's *The Decycling Number of Graphs* (2007) provides general decycling-number inequalities; specializing the known cubic bound gives the lower bound four, but not the seventy-set classification or automorphism-orbit enumeration. Alon, Mubayi and Thomas (2001) address large induced forests of sparse graphs, again at the level of general estimates. Ren, Yang and Zhao (2017), subsequently also Yang and Ren (2019), give a regular-graph identity relating the decycling-set size to its internal edges and complement components; the elementary edge bookkeeping in step 1 is an instance of this known principle, **not claimed as original**. Nedela and Škoviera's (1995) cyclic-connectivity paper concerns edge-connectivity structures rather than this vertex-deletion census.

The later Nedela–Škoviera (2022) work on cyclic connectivity and edge elimination contains a general existence theorem for suitably small decycling sets with connected tree complements in highly cyclically connected cubic graphs. That existence principle is **not sufficient** to derive the exact seventy-set classification or the two symmetry orbits. The full text of that closely related paper was not available for a conclusive page-by-page priority check, so a residual priority risk remains. The present result concerns an exhaustive classification for the particular Heawood graph, not general decycling-number bounds.

## Limitations

This is a statement about one fourteen-vertex incidence graph, not a classification for all projective planes, all cubic graphs or all girth-six cages. The named exact enumeration and automorphism-orbit description are verified by a complete combinatorial proof and independent finite checking, but earlier unpublished or differently titled enumerations cannot be excluded. A full-text priority comparison with the 2022 cyclic-connectivity paper remains open. No independent external mathematical audit or certification is claimed.

## References

- S. Bau, *The Decycling Number of Graphs*, arXiv:math/0703544v1, first posted 19 March 2007, https://arxiv.org/abs/math/0703544.
- N. Alon, D. Mubayi and R. Thomas, *Large induced forests in sparse graphs*, Journal of Graph Theory **38** (2001), 113–123, DOI:10.1002/jgt.1028.
- H. Ren, C. Yang, and T.-X. Zhao, *A new formula for the decycling number of regular graphs*, Discrete Mathematics **340** (2017), 3020–3031, DOI:10.1016/j.disc.2017.07.011.
- C. Yang and H. Ren, *New Formulae for the Decycling Number of Graphs*, Discussiones Mathematicae Graph Theory **39** (2019), 125–141, DOI:10.7151/dmgt.2064.
- R. Nedela and M. Škoviera, *Atoms of cyclic connectivity in cubic graphs*, Mathematica Slovaca **45** (1995), 481–499.
- R. Nedela and M. Škoviera, *Cyclic connectivity, edge-elimination, and the twisted Isaacs graphs*, Journal of Combinatorial Theory, Series B (2022), DOI:10.1016/j.jctb.2022.01.007 (abstract assessed; full text not inspected).
