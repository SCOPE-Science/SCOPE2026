---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The source files `verify_pg_rank4.cpp`, `check_extension_table.py`, and their outputs `VERIFY_OUTPUT.txt`, `EXTENSION_OUTPUT.txt` are supplied as reproducible computational support. Compile and run with `g++ -O3 -std=c++17 verify_pg_rank4.cpp -o verify_pg_rank4 && ./verify_pg_rank4`. The program constructs normalized finite-field vectors for points and hyperplanes and computes exact rank-four recursive types from ordered atomic diagrams, including equality and unary sorts. It confirms the binary projective-dimensional comparison \(\operatorname{PG}(3,2)\equiv_4\operatorname{PG}(4,2)\) and a rank-four distinction from \(\operatorname{PG}(3,3)\). It does not computationally exhaust every dimension or field size; the general theorem is proved by the extension-count argument in `RESULT.md`.

Mathematical verification conditions: \(d\ge3\), finite prime-power \(q\ge2\), and an otherwise unexpanded point-hyperplane incidence signature. Nonstandard critical step: all new incidence patterns for a fourth object are enumerated from one- and two-object counts or the collinear/noncollinear triple table. Every pattern required in the four-round game has a witness. The argument does not assert anything about full first-order elementary equivalence, rank-five equivalence, or arbitrary finite projective planes and designs. Independent validation has not been performed.

The second script can be run with `python3 check_extension_table.py`. It enumerates projective points and hyperplane covectors in dimension three over finite fields of sizes 2, 3, 4 and 5, confirming the precise incidence-pattern supports for dependent and independent point triples, including the nonprime field of size four. It is a finite check of a lemma whose general proof is given symbolically.
