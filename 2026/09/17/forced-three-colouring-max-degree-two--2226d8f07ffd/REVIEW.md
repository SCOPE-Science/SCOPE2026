# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The central characterization is local and exact. For three colours on a graph of
maximum degree two, an uncoloured vertex can be forced only after its two
neighbours are coloured with distinct colours. On a path or cycle, any adjacent
pair of initially uncoloured vertices therefore creates a nonempty uncoloured
run in which no vertex can be first forced. Hence the initially uncoloured set
must be independent; path endpoints must additionally be initially coloured.

For an admissible uncoloured set, suppressing each uncoloured vertex converts
the forcing constraints into ordinary different-colour constraints on the
surviving path or cyclic sequence. This gives exactly
\(3\cdot2^{n-j-1}\) assignments for each size-\(j\) admissible set on a path and
\(2^{n-j}+2(-1)^{n-j}\) assignments for each size-\(j\) independent set on a
cycle. The standard counts
\(\binom{n-1-j}{j}\) and
\(\frac{n}{n-j}\binom{n-j}{j}\) then yield the formulas.

The formulas were also checked by exhaustive enumeration for paths through
order 7 and cycles through order 7. This is supporting evidence rather than a
substitute for the proof.

A further consistency check detects a small error in the source paper:
arXiv:2609.17108v1, Proposition 6, equation (10), prints
\(FC_3(K_{1,2};p)=6p^2(1-2p)\). Direct counting and the path formula give
\(6p^2(1-p)\). At \(p=1/3\), the printed value is \(2/9\), contradicting the
paper's own Proposition 4(c), which requires
\(3^{-3}P(P_3;3)=4/9\). The corrected formula satisfies that identity.

## Originality

**PASS, to the best of our knowledge.**

The most directly relevant source is Farr, arXiv:2609.17108v1. Its full text
states formulas for empty and complete graphs, all connected graphs on at most
four vertices, and a general formula for bipartite graphs when \(\lambda=2\).
It does not give path or cycle family formulas for \(\lambda=3\); text searches
for path-family terminology in the full paper found no such result. The earlier
Farr--Morgan paper arXiv:2406.15746v1 introduces the forced-colouring function
and basic examples but likewise does not provide the formulas proved here.

Searches using the exact and synonymous phrases "forced 3-colouring polynomial",
"forced 3-coloring polynomial", "forced colouring polynomial" together with
"path", "cycle", and symbolic forms such as \(FC_3(P_n)\) did not locate an
earlier path/cycle formula. Searches for a correction or erratum to
arXiv:2609.17108 also did not locate one.

No inaccessible source was identified as especially likely to contain the same
result. The principal residual risk is parallel work that has not yet been
indexed or made public, because the 2026 source paper is only days old.

The originality claim is limited to the exact \(\lambda=3\) formulas for paths,
cycles, and maximum-degree-two graphs, together with the correction of the
displayed \(K_{1,2}\) value. The \(\lambda=2\) bipartite formula,
multiplicativity, and the \(\lambda>\Delta+1\) reduction to the chromatic
polynomial are prior results of Farr.

## Value

**PASS.**

The result closes the only nontrivial colour-count case left by the general
structural statements for the entire maximum-degree-two class. It supplies
closed coefficient formulas, a second-order path recurrence, and an immediate
linear-time arithmetic evaluation procedure on that class, while the unrestricted
fixed-\(\lambda\ge3\) evaluation problem is #P-hard. It also identifies and
repairs a concrete small-case formula in the current source paper.

## Sources inspected

- G. E. Farr, *The forced colouring function of a graph*,
  arXiv:2609.17108v1, including the definitions, Propositions 2, 4--6,
  Theorem 7, the small-graph table, complexity statement, and future-work
  section.
- G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*,
  arXiv:2406.15746v1, including its introduction of the forced-colouring
  function and displayed basic examples.

## Limitations

The theorem is confined to maximum degree at most two. Degree three permits a
forced vertex to have several different neighbour pairs witnessing forcing and
requires new structure. Very recent parallel work remains possible.

**Same-model review: passed. Cross-model review: not yet performed.**
