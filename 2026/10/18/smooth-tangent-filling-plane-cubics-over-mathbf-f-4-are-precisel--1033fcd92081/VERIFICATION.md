---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently enumerated every nonzero coefficient vector modulo scalar by normalizing the last nonzero coefficient, with 21 normalized projective points and exact F4 arithmetic in a multiplicative exponent encoding. The complete tangent-filling census by (rational zeros, nonsingular rational zeros) is (9,8):5040, (9,9):280, (10,10):6048. Hasse excludes the 10-point class for geometrically smooth plane cubics and the 8-of-9 class is rationally singular. The remaining 280 are scalar Hermitian; their coefficient matrices have no nonzero F4 kernel by the independent gradient check on all projective points, hence are invertible over the closure. This proves geometric smoothness, not just nonsingularity over finite test extensions. Conversely all nonsingular Hermitian forms are congruent to the diagonal form. Its rational isotropic vectors have exactly two nonzero coordinates, giving nine points. The unitary group has order 2^3(2+1)(2^2−1)(2^3+1)=648, and its projective image has order 216. There is no extra F4 projective similitude factor: a nonzero scalar carrying a Hermitian form to another must be fixed under conjugation, and F2 has only one nonzero element. The independent census checks the indicated non-Hermitian cubic gives (9,9,18); its gradient forces all three coordinates to vanish if it vanishes, proving geometric smoothness. The frozen verifier's shortcut for fewer than five rational zeros is legitimate: four lines cover at most 1+4·4=17 points.

## originality

PASS

Credit the converse for geometrically smooth embedded cubics and the nine-point non-filling distinction, not the Hermitian construction, standard orbit/stabilizer or Hermitian point count. Checked later catalogue records substantially overlap, including one which explicitly gives the same smooth classification, but do not establish earlier priority. An unsourced attribution of earlier computation remains unresolved.

## value

PASS

The property is motivated by the Hermitian tangent-filling construction and smallest nontrivial Hermitian plane cubic. This is a complete intrinsic incidence criterion in the specified plane embedding, not a count for an arbitrarily selected coefficient slice. The maximal non-filling example is useful because it rules out just testing the abstract elliptic point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
