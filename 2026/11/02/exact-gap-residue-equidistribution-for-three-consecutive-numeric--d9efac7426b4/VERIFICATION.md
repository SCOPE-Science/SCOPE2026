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
# Verification

The proof uses exact Apéry minima, finite geometric-sum identities, and the ordinary roots-of-unity criterion. The singular denominator \(q^{a+2}=1\) is excluded from the rational identity and evaluated separately at order three. The quadratic nonvanishing argument has no numerical approximation.

To reproduce the bounded computational cross-check, run `python verify.py` using Python 3 and its standard library. The script computes Apéry sets using Dijkstra shortest paths rather than the proof's ceiling formula, enumerates all gaps in each residue class, then checks the theorem for \(3\le n\le170\) and \(2\le m<\min(3n,220)\). It reports exactly 29,098 checked parameter-modulus pairs. All finite checks passed in the current package; no external dependency or downloaded data is required.

These finite calculations do not exhaust the infinite parameter ranges. Originality is established only to the extent of the recorded targeted literature comparisons. Independent mathematical validation has not been performed.
