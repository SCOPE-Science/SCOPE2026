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
# Reproducibility and limits

Run `python3 verify.py` from the directory containing the standalone script. It requires only the Python standard library. The reported output was obtained from that program and is embedded as `verification_output.txt`.

For each \(m=2,3,4,5\) and every \(1\le k<m\) coprime to \(m\), all \(q^4\) ambiguity positions are computed by integer character sums, without floating-point approximations. For \(m=6\), every zero-translation Walsh coefficient and every derivative-fiber cardinality are computed directly; the remaining contributions are counted by the proven two-point-fiber formula. Expected singular-value multiplicities are computed independently from the theorem's closed forms. The script merges equal-valued spectral bands, including \(q=4\).

The tests do not supply an exhaustive check for infinite degree. The all-degree proof uses the radical equation, field multiplicative-group divisibility, and character orthogonality. The independent audit channel has not been used. Output equality is an exact integer check, not a publication or priority certificate.
