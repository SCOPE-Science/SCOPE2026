---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Translation reduces every four-set to an anchored triple. Explicit group characters give the three candidate values; 4|N subgroup case is already known. The inspected CHECK.py computes exact rational Machin arctangent and Taylor enclosures for each sine/cosine (Q=10^8), rounds to integers with coordinate error <1/Q, and uses corrected integer square roots satisfying w^2<=X^2+Y^2<(w+1)^2. All squared sums <2^63 and a score margin >13(N-1) Q-units separates each noncandidate in true D_N. Four actual CERT files cover 8-96,97-112,113-120,121-128 and sum to 10,667,965 anchored configurations. A separately implemented batch enumerator, using different floating trig estimates and independently corrected integer roots for corroboration (not exact-error proof), checked 8-110 and 111-128 covering all anchored sets; minimum observed rigorous-budget margin corresponds to 0.10997296 at N=123. No extension beyond N=128 is asserted.

## originality

PASS

PASS at best knowledge with known branch explicitly credited: Ferguson et al., arxiv:2610.36276v1 Theorem 2.3 gives subgroup-coset equality for 4|N; Question 9.1 explicitly asks four-element minimizers for 4<=m<=N/2 with m not dividing N, including twice-odd lifts; Proposition 9.2 certifies only a local-search obstruction at N=17. This new finite exhaustive 121-modulus global theorem resolves a meaningful finite slice of that open cardinality. Published Resultary four-character projection norms and fourth moments optimize different quantities. Unindexed earlier exhaustive tables remain plausible.

## value

PASS

PASS: The first unsettled cardinality in a natural Fourier-compressibility/graph-labeling minimization is classified exhaustively over a substantial exact range, with all equality orbits and noncandidate separation, not arbitrary isolated tests. The cutoff 128 is explicitly finite; it provides finite data and proof technique for a source-stated open minimizer problem without claiming the unbounded result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
