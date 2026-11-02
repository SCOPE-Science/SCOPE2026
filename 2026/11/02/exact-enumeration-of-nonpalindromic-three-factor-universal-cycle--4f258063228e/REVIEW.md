# Review of the nonpalindromic three-factor universal-cycle enumeration

## Correctness

**PASS.** Each allowed length-three factor \(abc\) with \(a\ne c\) is a distinct directed edge \((a,b)\to(b,c)\). The graph is balanced of degree \(q-1\). The proved decomposition of its adjacency action into the doubly centered symmetric and skew sectors, the all-ones line, and \(q-1\) explicit two-dimensional blocks gives the complete characteristic polynomial. A simple degree eigenvalue and the matrix-tree cofactor product give positive in-arborescence counts and strong connectivity. The fixed-first-edge version of BEST yields exactly the stated rotation-class count. A separate direct search gives all 108 classes when \(q=3\), and exact integer minors agree through \(q=6\). The finite tests are not used as proof for larger alphabets.

## Originality

**PASS, with residual bibliographic risk.** Gardner--Godbole (arXiv:1711.07029v1) study several other restricted universal-cycle families, chiefly their existence. Chen--Kitaev--Sun (doi:10.3390/math8050778) evaluate probabilities of existence under removals, specifically up to two forbidden words or tiny binary examples, and do not enumerate every Euler tour of this \(q^2\)-forbidden family. Burris--Motta--Shipman (arXiv:1608.08480v1) quotient by reversal and cover each reflection class, a mathematically different edge set. Bernardini et al. (doi:10.4230/LIPIcs.CPM.2022.12) optimize making a de Bruijn graph Eulerian; the present graph already is Eulerian and is being counted. Arrigo et al. (doi:10.1016/j.laa.2018.07.010) count non-backtracking walks rather than Euler tours using each permissible factor once. No matching published result or indexed equivalent was identified in the specific searches recorded with the finding. An unindexed special case or non-backtracking spectral specialization remains possible; originality has not been independently audited.

## Value

**PASS.** Removing the \(q^2\) ordinary three-letter palindromes is a canonical minimal nontrivial palindrome-exclusion rule, and exact universal cycles give optimal once-only test strings for its entire allowed length-three language. The all-alphabet product count is not a single small-case census or a renaming of standard full de Bruijn enumeration: the graph has a different degree, mixed complex spectral blocks, and a separately evaluated arborescence factor. The proof offers the full spectral decomposition and exact counts for arbitrarily large alphabets. It does not purport to solve other forbidden factors or reverse-complement constraints.

## Closest literature and limitations

The closest methodological relationships are restricted universal cycles (Gardner--Godbole 2017), small forbidden-set enumerations (Chen--Kitaev--Sun 2020), reversal-quotient de Bruijn constructions (Burris--Motta--Shipman 2016), and general non-backtracking graph methods (Arrigo et al. 2018). Published methods alone do not constitute a previously published evaluation of this precise product formula. A prior specialized result not discoverable by the performed queries remains a risk.

Self-review: passed. Independent audit: not yet performed.
