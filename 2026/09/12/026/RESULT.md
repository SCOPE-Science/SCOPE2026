# Maximality of the 37 known Ramsey(4,6;35) witnesses under single-vertex extension

## Context

The classical Ramsey number R(4,6) is the least n such that every graph on n
vertices contains a K4 or an independent set of size 6. Equivalently, a
Ramsey(4,6;n) witness is a graph G on n vertices with no K4 (omega(G) <= 3)
and independence number alpha(G) <= 5; its complement is K6-free with clique
number at most 5. It is known that 36 <= R(4,6) <= 41. The lower bound
R(4,6) >= 36 was established by Exoo (2012), who found 37 new edge-colorings
of K35 with no K4 in the first color and no K6 in the second color, i.e. 37
Ramsey(4,6;35) witnesses. The admitted target asked whether R(4,6) >= 37 via
an explicit Ramsey(4,6;36) witness. That target is blocked; this record states
the strongest rigorously established increment found while pursuing it.

## Definitions

- Graph G is simple, undirected, on vertex set V with |V| = 35 or 36.
- Ramsey(4,6;n) witness: K4-free graph on n vertices with alpha(G) <= 5.
- Ledger: `artifacts/r46data.g6` holds 37 graphs on 35 vertices in graph6
  format (the working copy of the known corpus).
- For G on 35 vertices and a new vertex v with neighbourhood S subset of V(G),
  write G+S for the 36-vertex graph formed by joining v to exactly S.

## Result (headline claim)

Each of the 37 graphs in `r46data.g6` is a valid Ramsey(4,6;35) witness and
is maximal under single-vertex extension: none of the 37 graphs admits a
triangle-free vertex set S meeting all of its independent 5-sets (742-818
per graph). By the one-vertex extension theorem below, no graph in the corpus
is an induced 35-vertex subgraph of any Ramsey(4,6;36) witness. Consequently,
any 36-vertex witness for R(4,6) >= 37, if one exists, must be de novo and
contain none of these 37 graphs as a 35-vertex induced subgraph.

Per-graph certificates: independent-5-set counts range 742-818 and exhaustive
proof search-node counts range 2491-5800; see
`artifacts/noext_proof_summary.json` and the verifier output.

## Proof and evidence

One-vertex extension theorem. Let G have 35 vertices, K4-free with
alpha(G) <= 5, and let v be a new vertex with neighbourhood S. Then G+S is a
Ramsey(4,6;36) witness if and only if (i) S is triangle-free in G and
(ii) S meets every independent 5-set of G. Proof: a K4 using v exists iff two
neighbours of v are adjacent and share a third neighbour in S, i.e. iff S
contains a triangle of G (K4s avoiding v already lie in G, which is K4-free);
an independent set using v is {v} union an independent set of G[V \ S], so
alpha(G+S) <= 5 iff no independent 5-set of G survives in the
non-neighbourhood of v, i.e. iff S is a hitting set (transversal) for the
family of independent 5-sets. Hence extension is exactly the problem: does G
contain a triangle-free set meeting all independent 5-sets?

Machine-checked proof. (1) Exact K4 counting (bitmask) and branch-and-bound
independent-6-set search show all 37 graphs have K4 count 0 and no independent
6-set; cross-checked by itertools.combinations brute force (graph 0 has 784
independent 5-sets by brute force and by both DFS counters). (2) Exhaustive
fail-first branch-and-bound over triangle-free hitting sets (branch on an
uncovered independent 5-set; prune vertices that would close a triangle with
the partial set), implemented twice independently with identical per-graph
results: PROVED-NO-EXTENSION on all 37 graphs. (3) Frozen self-contained
verifier `artifacts/verify_maximality.py` plus ledger copy
`artifacts/r46data.g6`; rerun reproduces all 37 proofs in about 12 seconds
(stdlib only). Independent audit reran the frozen verifier end-to-end (12 s,
all counts matching) and spot-checked graphs 0, 14, 26 by full
itertools.combinations enumeration (K4 = 0, independent-6 count 0,
independent-5 counts 784/742/797). (4) Obstruction diagnostics: on graph 0
the best triangle-free set covers only 733/784 independent 5-sets (uncovered
families concentrate on specific vertices), while the best pair of
triangle-free sets covers 784/784, so the obstruction is specific to single
neighbourhoods and a de novo 36-graph is not ruled out.

## Limitations

- Proves maximality only against single-vertex extension of these 37 graphs;
  it does not prove R(4,6) = 36 and does not rule out a de novo 36-vertex
  witness.
- The corpus may not exhaust all Ramsey(4,6;35) graphs; the quantifier is over
  the provided ledger, not over all 35-vertex extremal graphs.
- De novo search evidence (five stochastic batteries: seeded simulated
  annealing, K4-aware annealing, K4-free repair, circulant search with 237,595
  iterations, tabu search) is bounded non-convergence evidence, not a
  nonexistence proof, and is context only, not part of the headline theorem.
- Verification is machine-checked exhaustive search with two independent
  implementations plus a frozen rerunnable verifier, not a hand-checked proof.

## Reproducibility

Run `python3 artifacts/verify_maximality.py` with `r46data.g6` beside it
(a copy is included as `artifacts/r46data.g6`). Total runtime about 12-20 s,
stdlib only. Expected output: ledger line reporting 37 graphs, validity line,
per-graph `indep5=... proved_no_ext=True nodes=...` lines, and
`MAXIMALITY VERIFIED`.

## References

- G. Exoo, On the Ramsey Number R(4,6), Electron. J. Combin. 19(1) (2012), P66.
  DOI 10.37236/2102. Proves R(4,6) >= 36 via 37 new K35 colorings.
- S. P. Radziszowski, Small Ramsey Numbers, Electron. J. Combin., Dynamic
  Survey DS1. Records current R(4,6) bounds 36..41.
- E. W. Weisstein, Ramsey Number, MathWorld. Tabulates known Ramsey bounds.
- House of Graphs, Ramsey numbers meta-directory. Graph lists and bounds.
