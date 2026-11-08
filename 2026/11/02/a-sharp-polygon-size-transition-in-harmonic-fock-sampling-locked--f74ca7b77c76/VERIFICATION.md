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

From harmonic basis derive kernel R(z,w)=exp(z*conj(w))+exp(conj(z)*w)-1. DFT of circulant Gram gives lambda_j=P_{k,j}+P_{k,-j}-exp(-t)1_{j=0}, with P Poisson congruence class probabilities. k=2 difference exp(-t)(2exp(-t)-1). k=3 difference exp(-t)(2exp(-t/2)cos(sqrt(3)t/2)-1), monotone until unique crossing and bounded below thereafter. k=4 explicit cos(t) splits minima along alternating pi sequences. For each fixed k>=5, primitive roots of unity dominate correction at rate exp(-(1-cos(2pi/k))t)cos(t sin(2pi/k))cos(2pi j/k), with a uniform faster remainder; choose alternating cosine signs. Independent Poisson/spectral checks for k=2..9 validate example modes. Finite checks do not establish infinite switching.

## originality

PASS

The harmonic Fock kernel and radial Toeplitz spectral theory are standard and reported by Sun, Du and Qi (2024); Poisson-residue and circulant formulas are routine. The new mathematical classification orders finite nonradial point-sampling singular eigenvalues across all k and arbitrarily large radii; radial-symbol Toeplitz results do not dominate it. Resultary searches returned cyclic Fourier and sampling rigidity on other spaces/objects, not this harmonic Fock polygon eigenvalue-order phase diagram.

## value

PASS

A natural point-evaluation Gram matrix controls condition and observability of Fourier sample modes; the sharp k=3 versus k=4 transition and exact small-k tight radii provide a structural sampling distinction that cannot be inferred from knowing the kernel alone. There is no ambient infinite-dimensional frame lower bound claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
