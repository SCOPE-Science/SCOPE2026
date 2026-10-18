---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Gauge phase alignment reduces the weighted-shift numerical radius on full complex ℓ∞ (as a real Banach norm) to the top of a bipartite Jacobi matrix with offdiagonal |a_n|/2. Binary zeros decompose it into path blocks; a run of m ones has top eigenvalue cos(π/(m+2)) and normalized sine eigenvector. If one finite run uniquely attains the maximum, other blocks lie below by a uniform spectral gap δ_m>0; Rayleigh decomposition gives O(||E||²/δ_m) uniformly for arbitrary bounded complex perturbations. Although modulus at zero is nonsmooth, the winning eigenvector sees only base-one edges, where |1+h|=1+Re h+O(|h|²), giving the exact real Fréchet derivative. In a tied maximum, scaling one run changes the right slope while another holds the left flat. For arbitrarily long/infinite runs, choose disjoint alternating long all-one blocks with ± signs, producing N(a+th)=1+|t| for small t. At a=0 every norm is nonsmooth. All binary cases exhausted; no finite-section inference.

## originality

PASS

The exact path radius and standard simple-eigenvalue perturbation tools are classical inputs. However the complete binary ℓ∞ dichotomy including arbitrarily many infinite-support runs and unrestricted complex perturbations is not entailed by the closest published spectral-gap result, which explicitly assumes every weight nonzero with moduli tending to b>0. Finite graph smooth-locus results cover each finite truncation but do not establish uniform infinite-sequence failure directions or global uniform spectral gap.

## value

PASS

Binary {0,1} sequences are a natural combinatorial skeleton of the numerical-radius norm, encoding disjoint paths. A complete classification and explicit full-ℓ∞ derivative separate isolated unique spectral winners from ties and infinite edge accumulation. It is a motivated exact smooth-locus boundary rather than a small arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
