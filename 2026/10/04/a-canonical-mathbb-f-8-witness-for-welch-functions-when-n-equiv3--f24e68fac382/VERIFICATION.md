---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

If odd \(n\) is divisible by \(3\), write \(n=6r+3\) and \(m=(n-1)/2=3r+1\). Finite-field subfield theory gives \(\mathbb F_8\subset\mathbb F_{2^n}\), a three-dimensional \(\mathbb F_2\)-linear subspace and hence an allowed affine three-flat. On \(\mathbb F_8^\times\), whose order is seven, \(2^m+3\equiv2+3\equiv5\pmod7\). Therefore \(\sum_{x\in\mathbb F_8}x^{2^m+3}=\sum_{x\in\mathbb F_8^\times}x^5=0\), since fifth power permutes the nonzero cyclic group and the sum of all its elements is zero. Thus the Welch function fails third-order sum-freedom. Independently, on \(\mathbb F_8\) the Frobenius \(z\mapsto z^{2^m}\) is squaring, and substitution into the Hou–Zhao obstruction polynomial cancels its first two terms in characteristic two and annihilates the third.

## originality

PASS

The current indexed abstract of Hou–Zhao's Welch paper, last updated on 2026-09-28, still describes the third-order Welch statement as a conjecture supported by numerical evidence. Exact searches for an \(\mathbb F_8\) Welch witness or a theorem for \(3\mid n\) found no prior theorem, and Resultary returned only the assigned record as the exact hit. The superficially similar earlier divisible-by-three theorem is explicitly for the multiplicative inverse function, not the Welch exponent. The current Hou–Zhao revision's full PDF could not be obtained through the lawful arXiv/OA route or authorized institutional retrieval, so possible revision-only overlap is recorded as a residual risk rather than treated as noncoverage evidence.

## value

PASS

The theorem proves an infinite arithmetic progression of a newly stated Welch sum-freedom conjecture and replaces determinant/search evidence with a canonical subfield mechanism. That is a motivated structural advance even though the final proof is elementary once the witness is recognized.

The dated certificate retains the supplied scientific assessment, sources and limitations.
