# The strong chromatic index of the Tutte–Coxeter graph is seven

## Finding

The Tutte–Coxeter graph has strong chromatic index exactly \(7\). The new direction addressed here is the upper bound, witnessed by an explicit coloring of its forty-five edges. The lower bound is the published nonexistence of a strong six-edge-coloring.

## Assumptions and scope

A strong edge coloring is a partition of the edge set into induced matchings. Two edges may receive the same color only if they have disjoint endpoints and there is no edge between their endpoints. This is the ordinary strong chromatic index of a single graph, not a list-coloring bound or an assertion for all cubic graphs of a given girth.

Write the graph as the bipartite incidence graph of the fifteen unordered pairs (duads) of \(\{0,1,2,3,4,5\}\) and the fifteen partitions of this set into three pairs (synthemes). A duad and a syntheme are adjacent when the duad belongs to the syntheme. Sort the duads lexicographically; represent each syntheme as a sorted tuple of its three duads and sort these tuples lexicographically. Order the graph edges first by their duad and then by their syntheme.

## Proof

The colors in this edge order are

```text
0,6,1,3,6,4,0,1,4,6,2,0,5,2,0,
2,3,4,0,5,4,2,5,3,1,6,5,2,4,6,
5,3,1,4,6,3,2,0,6,4,0,1,5,1,6
```

For distinct incidences \((D,S),(D',S')\), a conflict is exactly \(D\in S'\) or \(D'\in S\). This detects shared endpoints as well: if \(D=D'\) or \(S=S'\), both membership tests hold. Otherwise the graph is bipartite, and these are the only possible cross-edges. The assignment can therefore be verified by the following exhaustive pair check, which reconstructs the ordered incidence list from the definition.

```python
from itertools import combinations

duads = list(combinations(range(6), 2))
synthemes = [s for s in combinations(duads, 3)
             if len({v for d in s for v in d}) == 6]
edges = [(d, s) for d in duads for s in synthemes if d in s]
colors = (0,6,1,3,6,4,0,1,4,6,2,0,5,2,0,
          2,3,4,0,5,4,2,5,3,1,6,5,2,4,6,
          5,3,1,4,6,3,2,0,6,4,0,1,5,1,6)
assert len(edges) == len(colors) == 45 and set(colors) == set(range(7))
for i, j in combinations(range(45), 2):
    if colors[i] == colors[j]:
        d, s = edges[i]
        e, t = edges[j]
        assert d not in t and e not in s
```

Thus \(\chi'_s\le7\). For the reverse inequality, Lužar, Mačajová, Škoviera and Soták, Section 5, explicitly report that the Tutte eight-cage does not admit any strong six-edge-coloring. This gives \(\chi'_s\ge7\), since a coloring with fewer colors would also be a coloring with at most six. Together the bounds give equality.

## Verification and scope of the contribution

The edge ordering and membership tests above are self-contained for the upper bound. The included files `CERTIFICATE.json`, `verify_exact.py` and `verify_independent.py` also contain the coloring and finite checks, including an alternative exhaustive exclusion of six colors. The matching enumeration used by those checks is supporting evidence, not a claimed new census. The description of the ten maximum matchings by balanced \(3+3\) partitions and the size-eight extension count are already given in [Induced matchings of the Tutte–Coxeter graph: ten balanced partitions](https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-induced-matchings-of-the-tutte-coxeter-graph-ten-balanced-partit--c4c0fb33bc3e/RESULT.md).

The seven-color certificate settles one natural edge-coloring invariant of the cubic eight-cage, a specific graph known to require more than six colors. It does not settle the conjectured seven-color bound for all subcubic graphs of girth at least five.

## Primary reference

B. Lužar, E. Mačajová, M. Škoviera and R. Soták, *Strong edge colorings of graphs and the covers of Kneser graphs*, [arXiv:2101.04768](https://arxiv.org/abs/2101.04768), §5; DOI: 10.1002/jgt.22802.
