---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The published paperfolding theorem gives a global maximum factor length 45 for words admitting repetition factorizations. In the four-letter 2-uniform fixed point, factor sets of μ^9(0) and μ^10(0) agree through length 45. Any factor of μ(z) of length ℓ≤45 depends on a source factor of length at most ceil((ℓ+1)/2)≤23 and one parity offset, proving by induction no later factors appear at length ≤45. Coding yields a complete regular binary bounded factor language. Exact dynamic programming over every admissible prefix with period ≤ half its length finds 232 distinct factorizable factors, counts {1:112,2:94,3:12,4:2,5:10,6:2}, shortest ambiguous length 9 (four factors), longest unique length 30 (two), maximal multiplicity 6 (two). Distinct factors, not occurrences, are counted; the global cutoff is essential.

## originality

PASS

The primary theorem of Rampersad–Shallit–Xu supplies the length 45 cutoff and short-width work, but not a complete multiplicity-by-factor census of regular paperfolding. Exact 232-word classification and full per-factor catalogue are additional finite invariants of a natural automatic sequence, not the previously proved finiteness itself.

## value

PASS

The ambiguity distribution is a natural exact classification of repetition factorizations of an extensively studied automatic word. It determines exactly when unique factorization fails, by how many decompositions and at what lengths, potentially serving future work on automatic-string factorization and decidable regularity cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
