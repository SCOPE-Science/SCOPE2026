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

For every k>=1, the normalized quadratic Gauss sum at a nonzero frequency difference is zero precisely when after removing their common 2-power either m=1 and U+V odd or m>=2 and U odd. At m>=2 an odd U cancels by half-period translation; if U even and V odd the two surviving terms in the squared modulus give 2^(m+1)>0. The lowest-differing-bit orthogonality rule forces two occupied child prefixes per occupied node; a full N=2^k family uniquely yields a 1-Lipschitz f on residues mod 2^(k−1) and one of four terminal H/V edges per residue. The count of f is 2^(2^k−2), times 4^(2^(k−1)) terminal choices, hence 2^(2^(k+1)−2). End k=1 is four edges. Exact checks of all Gauss sums for k=1..5 and constructed spectra k<=3 corroborate, not prove, the all-k statement.

## originality

PASS

Best-of-knowledge: odd-prime parabola spectra are characterized by strictly contracting graphs, but characteristic-two Gauss zeros have distinct last-bit Hamming edge behavior. The 1D cyclic p-adic spectral/tiling theorems and finite-field extension theorems do not classify ambient two-coordinate quadratic-graph spectral partners; no implication to this exact dyadic count identified.

## value

PASS

Characteristic-two boundary is structurally different from the known odd-prime result: a complete, unique dyadic-binary classification and closed enumeration of every orthonormal ambient spectral partner for the natural quadratic graph, including vertical top-bit frequency edges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
