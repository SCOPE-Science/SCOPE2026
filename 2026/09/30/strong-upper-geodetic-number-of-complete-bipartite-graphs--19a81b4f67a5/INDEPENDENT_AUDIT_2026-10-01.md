# Independent audit — 2026-10-01

## Final claim

For \(K_{a,b}\) with \(1\le a\le b\), the strong upper geodetic number and all maximum-cardinality minimal strong geodetic sets are exactly as classified and counted in RESULT.md.

## Correctness — PASS

In \(K_{a,b}\), an omitted vertex of one part can be covered internally only by a chosen length-two geodesic joining a selected pair in the opposite part. Thus the exact feasibility conditions are \(a-s\le\binom t2\) and \(b-t\le\binom s2\). Strong-geodetic feasibility is upward closed, so minimality is equivalent to failure after each one-vertex deletion. The proof uses these inequalities to obtain the \(b+1\) upper/lower bound for \(a\ge2\), treats stars and \(K_2\) separately, and exhausts the omitted-count cases for maximum sets. A fresh replay of the actual verifier independently used path-slot matchings on all \(108204\) subsets across 35 bipartite types and matched every stated value, pattern, and count.

Checked sources:
- Bino Infanta--Antony Xavier, Strong Upper Geodetic Number of Graphs, Commun. Math. Appl. 12 (2021), complete 12-page primary PDF inspected.
- Iršič, Strong Geodetic Number of Complete Bipartite Graphs and of Graphs with Specified Diameter, Graphs Combin. 34 (2018), ordinary minimum parameter.
- Published-record semantic search for the strong upper geodetic number of complete bipartite graphs.
- Fresh replay of the package verifier on all 35 types with \(a\le7\) and \(b\le8\).

Residual risks:
- The finite replay is corroborative; the arbitrary-parameter theorem rests on the capacity proof.

## Originality — PASS

Best-of-knowledge originality passes. The complete 2021 primary paper introducing the strong upper parameter was inspected. Its main results cover general bounds and other graph families; complete bipartite graphs appear only through citation to the ordinary strong geodetic number. Semantic searches found no prior formula or maximum-minimal-set classification for \(\operatorname{sg}^+(K_{a,b})\).

### Equivalent formulations

Searches:
- Resultary query: strong upper geodetic number complete bipartite graphs
- Full-text inspection of the 2021 defining paper

Evidence:
- The assigned record is the only exact semantic hit.
- The 2021 paper cites Iršič for the ordinary strong geodetic number of complete bipartite graphs but does not state the upper parameter formula.

Reasoning: Equivalent formulations are the two capacity inequalities plus maximal-cardinality minimal solutions; no prior equivalent statement was found.

### Broader coverage

Searches:
- Bino Infanta--Antony Xavier 2021
- Iršič 2018 ordinary strong geodetic number

Evidence:
- The 2021 source is broader in general parameter introduction; the 2018 source concerns the minimum strong geodetic number, not the maximum size of a minimal set.

Reasoning: Neither broader source implies the upper parameter or its set classification.

### Exact database or table

Searches:
- Semantic searches for \(\operatorname{sg}^+(K_{a,b})\), upper strong geodetic bicliques, and maximum minimal sets

Evidence:
- No independent formula/table was located.

Reasoning: The audited theorem is a closed all-parameter classification rather than a finite table.

### Claim versus prior implication

Searches:
- 2021 main-results section versus audited capacity theorem

Evidence:
- The primary paper establishes general inequalities and selected-family results; no complete-bipartite upper theorem is among them.

Reasoning: The capacity argument is an additional family-specific analysis and not a mechanical corollary of the ordinary minimum parameter.

### Source inspections

- **Strong Upper Geodetic Number of Graphs** — Does not cover the complete-bipartite upper formula or maximum-set classification. Material read: Complete 12-page primary PDF, including the main-results section and references. Method: Primary full-text and rendered-page inspection. Evidence: The main-results section treats general bounds and other families; complete bipartite graphs occur in the references for the ordinary strong geodetic number.

Checked sources:
- Bino Infanta--Antony Xavier, Strong Upper Geodetic Number of Graphs, Commun. Math. Appl. 12 (2021), complete 12-page primary PDF inspected.
- Iršič, Strong Geodetic Number of Complete Bipartite Graphs and of Graphs with Specified Diameter, Graphs Combin. 34 (2018), ordinary minimum parameter.
- Published-record semantic search for the strong upper geodetic number of complete bipartite graphs.
- Fresh replay of the package verifier on all 35 types with \(a\le7\) and \(b\le8\).

Residual risks:
- Differently phrased later work on bicliques remains a best-of-knowledge risk.

## Scientific value — PASS

Complete bipartite graphs are a canonical benchmark family for geodetic parameters. The theorem converts an NP-hard-in-general upper invariant into an exact closed form and additionally classifies and counts every maximum minimal solution. The path-slot capacity criterion is structural and reusable, so the result is more than a list of small values.

Checked sources:
- Bino Infanta--Antony Xavier, Strong Upper Geodetic Number of Graphs, Commun. Math. Appl. 12 (2021), complete 12-page primary PDF inspected.
- Iršič, Strong Geodetic Number of Complete Bipartite Graphs and of Graphs with Specified Diameter, Graphs Combin. 34 (2018), ordinary minimum parameter.
- Published-record semantic search for the strong upper geodetic number of complete bipartite graphs.
- Fresh replay of the package verifier on all 35 types with \(a\le7\) and \(b\le8\).

Residual risks:
- The theorem is restricted to complete bipartite graphs.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
