# Independent audit — 2026-10-01

## Final claim

For bounded derivations on any complex C*-algebra, compactness, finite strict singularity, and strict singularity are equivalent; every noncompact derivation fixes either a copy of \(c_0\) or, in the weakly compact case, a one-complemented copy of \(\ell_2\) on which it is bounded below.

## Correctness — PASS

The proof closes all implications. Strict singularity prevents fixing \(c_0\), hence gives an unconditionally converging operator; Pełczyński property (V) for C*-algebras then makes the derivation weakly compact. Akemann--Wright Theorem 3.3 represents every weakly compact derivation by a \(c_0\)-sum of compact-operator ideals. If such a derivation is noncompact, some nonzero compact component acts on an infinite-dimensional \(K(H)\). Choosing a vector \(y\) with \(k^*y
e0\) and an infinite-dimensional subspace on which \(k\) is small makes the rank-one fiber \(\theta_{x,y}\) a Hilbert subspace on which the commutator is bounded below. Right multiplication by the rank-one projection and orthogonal projection onto that subspace give a norm-one complement. Thus a strictly singular derivation must be compact, and compact implies FSS implies SS.

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- C. A. Akemann, S. Wright, Compact and weakly compact derivations of C*-algebras, Pacific J. Math. 85 (1979), complete primary paper inspected; Theorem 3.3 inspected on the rendered page.
- H. Pfitzner, Weak compactness in the dual of a C*-algebra is determined commutatively, Math. Ann. 298 (1994), property-(V) source; theorem known through standard later statements.
- M. Mathieu, Properties of the Product of Two Derivations of a C*-Algebra (1989), abstract/full searchable text inspected for neighboring compactness literature.
- Published-record and web searches for strictly singular C*-derivations and compactness.

Residual risks:
- None.

## Originality — PASS

Best-of-knowledge originality passes. Akemann--Wright completely classify compact and weakly compact derivations but do not state the strict-singularity collapse or the complemented Hilbert witness. Property (V) supplies only the first reduction to weak compactness. Targeted searches of derivation and elementary-operator literature did not locate the final compact/FSS/SS equivalence.

### Equivalent formulations

Searches:
- Published-record semantic query: strictly singular derivations C star algebra compact finitely strictly singular
- Web query: strictly singular derivation C*-algebra compact
- Akemann--Wright 1979 full-text inspection

Evidence:
- Only the assigned finding appeared as an exact published-record match.
- Akemann--Wright give structural characterizations for compact and weakly compact derivations, not strict singularity.

Reasoning: Equivalent formulations include absence of noncompact strictly singular derivations, a compact/FSS/SS collapse inside \(\mathrm{Der}(A)\), and a \(c_0\)-versus-complemented-\(\ell_2\) witness dichotomy.

### Broader coverage

Searches:
- Akemann--Wright 1979 Theorem 3.3
- Pfitzner property (V)
- Mathieu 1989 neighboring derivation compactness work

Evidence:
- The structure theorem identifies the elementary ideals supporting a weakly compact derivation.
- Property (V) makes unconditionally converging maps weakly compact.
- No inspected source supplies the rank-one lower-bound lemma that excludes strict singularity in the noncompact weakly compact case.

Reasoning: The published ingredients reduce the problem but do not by themselves state or mechanically encode the crucial complemented-rank-one obstruction without an additional operator-geometric argument.

### Exact database or table

Searches:
- Exact strict-singularity/derivation searches

Evidence:
- No prior exact theorem or table was located.

Reasoning: No finite database is relevant; the check concerns theorem implication across the older derivation literature.

### Claim versus prior implication

Searches:
- Akemann--Wright structure theorem plus the assigned rank-one lemma

Evidence:
- A weakly compact noncompact derivation has a nonzero compact implementer on an infinite-dimensional elementary ideal.
- The assigned proof shows such a compact commutator is bounded below on a complemented rank-one Hilbert fiber.

Reasoning: The second statement is the nonstandard step needed to reach the strict-singularity collapse and was not found in the primary structure theorem.

### Source inspections

- **Compact and weakly compact derivations of C*-algebras** — Essential prior ingredient but not covering the strict-singularity conclusion. Material read: Complete primary paper, with Theorem 3.3 and surrounding proof inspected on rendered pages. Method: Primary full-text and rendered-page inspection. Evidence: Theorem 3.3 represents weakly compact derivations by a restricted direct sum of elementary ideals and a compact implementer.
- **Properties of the Product of Two Derivations of a C*-Algebra** — Treats products of derivations and compact/weakly compact behavior, not the strict-singularity collapse. Material read: Abstract and searchable full-text material. Method: Primary-text search/inspection. Evidence: Its stated theorems concern when a product of two derivations is a derivation, compact, or weakly compact.

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- C. A. Akemann, S. Wright, Compact and weakly compact derivations of C*-algebras, Pacific J. Math. 85 (1979), complete primary paper inspected; Theorem 3.3 inspected on the rendered page.
- H. Pfitzner, Weak compactness in the dual of a C*-algebra is determined commutatively, Math. Ann. 298 (1994), property-(V) source; theorem known through standard later statements.
- M. Mathieu, Properties of the Product of Two Derivations of a C*-Algebra (1989), abstract/full searchable text inspected for neighboring compactness literature.
- Published-record and web searches for strictly singular C*-derivations and compactness.

Residual risks:
- An unadvertised corollary in older derivation/elementary-operator literature remains a best-of-knowledge risk, but no such statement was located in the targeted searches.

## Scientific value — PASS

The theorem identifies a clean geometric boundary between weak compactness and strict singularity for derivations on arbitrary C*-algebras and gives explicit witnesses for every noncompact case. The complemented Hilbert fiber is a reusable structural lemma, so the result is more than a formal combination of the structure theorem and property (V).

Checked sources:
- Assigned package RESULT.md at the assigned Git snapshot.
- C. A. Akemann, S. Wright, Compact and weakly compact derivations of C*-algebras, Pacific J. Math. 85 (1979), complete primary paper inspected; Theorem 3.3 inspected on the rendered page.
- H. Pfitzner, Weak compactness in the dual of a C*-algebra is determined commutatively, Math. Ann. 298 (1994), property-(V) source; theorem known through standard later statements.
- M. Mathieu, Properties of the Product of Two Derivations of a C*-Algebra (1989), abstract/full searchable text inspected for neighboring compactness literature.
- Published-record and web searches for strictly singular C*-derivations and compactness.

Residual risks:
- An unadvertised corollary in older derivation/elementary-operator literature remains a best-of-knowledge risk, but no such statement was located in the targeted searches.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
