---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The proof is complete. Nonzero translation rows are indexed by the difference set \(A-B\). If the two unoriented support differences differ, all four differences are distinct, every row is a point mass, and the support is \(4p\). If they align, there are exactly three rows: two singleton rows contribute \(p\) each, and the middle row is a two-point Fourier transform. Because multiplication by the nonzero support difference permutes all \(p\)-th roots, that row has exactly one zero iff the stated cross-ratio is a \(p\)-th root of unity, and otherwise none, giving \(3p-1\) or \(3p\). The explicit examples attain all three values. Finite verifier cases are consistency checks only.

## originality

PASS

Originality passes. Krahmer--Pfander--Rashkov Proposition 4.4 already gives the sharp lower bound \(3p-1\) after specializing to two-sparse \(f,g\), and its proof already decomposes by translation rows and uses Cauchy--Davenport. What it does not state is the exact two-sparse spectrum \(\{3p-1,3p,4p\}\) for all primes or the equality criterion in terms of aligned support differences and one coefficient cross-ratio. Nicola classifies the much lower universal support-\(p\) extremizers, not this sparse stratum.

## value

PASS

Equality in a sharp uncertainty bound is a natural structural question, and the two-sparse stratum is the first nontrivial fixed-sparsity case. The theorem converts a known lower bound into a complete support spectrum and a transparent geometric/phase equality criterion valid for every prime, which is a motivated sharp classification despite the short proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
