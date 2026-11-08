---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Using character dual grid z_i^N=1, the Fourier polynomial for a symmetrized optimizer is F_t(z)=1+t(|sum_i z_i|²-4). Exact minimal root-sum radius is r=0 for even N, 2(1-cos(π/N)) for odd N, yielding masses 4 or 1+3/(c(2-c)). The odd equality contacts are twelve permutations of (1,1,-c+is,-c-is); independent symbolic six-by-six real/imaginary contact determinants reproduced -64 c³(c-2)(c-1)³(c+1)^5 and -64(c-1)³(c+1)³, nonzero for odd N>=5. At even N zero-sum character contacts enforce three complementary real-edge-sum equations and imaginary gradient potentials modulo constants; nonzero Fourier slack gives full six-real-dimensional relative face. Independent direct four-root enumeration N5..12 reproduced the sharp minimum; the package checker was inspected for separate Fourier-contact tests. The quartic expansion is 3π^4/(4N^4)+O(N^-6) along odd N. Enumeration does not prove all N; the 4-root geometry and contact-rank argument do.

## originality

PASS

Finite A3 entire complex optimal-equality class, even six-dimensional face and odd unique optimizer are distinguished from the known four-root minimum and generic finite-group Turán framework. No identified source covers those equality classes; priority assessed best-of-knowledge.

## value

PASS

Determines not merely a scalar Turán bound but the geometry of its entire optimal face: even-order six-dimensional complex optimizer degeneracy, odd-order strict uniqueness, and quartic parity defect. These are natural sharp extremal questions for the A3 root neighborhood under finite Fourier positivity, and potentially useful for extremal positive-definite design and equality rigidity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
