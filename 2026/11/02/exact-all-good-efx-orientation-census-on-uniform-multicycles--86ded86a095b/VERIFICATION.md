---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each edge i let x_i count its goods allocated to i+1; self-value L_i=x_(i−1)+q−x_i. All-good EFX, crucially including deleting a good of zero value to the envier, is exactly equivalent to the two local inequalities x_i≤2x_(i−1)+1_(x_(i−2)=0) and 2x_(i−1)≤x_(i−2)+q+1_(x_i=q). They depend only on consecutive triples, so closed walks on state pairs (a,b) with binomial(q,c) weight count every labeled orientation exactly once, yielding trace(T_q^n). Integer Newton identities verify q2/q3 characteristic polynomials and their cubic recurrences; positive dominant roots with other eigenvalue moduli≤1 yield exponential survival bases. Independent direct all-good EFX orientation enumeration checks small n,q including zero-value goods and independent exact charpolys q2,3. Infinite n,q follows from the bijection, not finite tests.

## originality

PASS

Qualified PASS: existence and computational complexity of EFX multicycle allocations/orientations are prior art; the evaluated all-good uniform-q census, small-q characteristic factors, and rarity comparison are not supplied by inspected existence papers. Particular q=1 simple-cycle enumeration is not novel.

## value

PASS

Counting all fair orientations, not merely proving existence, is a natural enumerative refinement for agents with identical incident-unit values. Exact transfer law and first genuinely parallel q2/q3 spectra expose a non-obvious survival-rate comparison relevant to random allocations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
