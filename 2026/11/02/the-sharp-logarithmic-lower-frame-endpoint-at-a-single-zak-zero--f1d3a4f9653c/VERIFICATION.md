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

# Reproducibility and verification

The theorem is entirely analytic. Reproduce its central checks in this order:

1. Use Zak unitarity to write the synthesis inequality as equation (1) of RESULT.md. The Fourier multiplier is \((1+|k|^2)^{1/2}[\log(e+|k|)]^\beta\), and the deleted character is the constant mode after a lattice shift.
2. Check the Riesz-representation duality: modulo the deleted constant Fourier mode, any representing function must be \((\psi-d)/\phi\). A nonzero \(\psi(p)-d\) leaves an uncancelled two-dimensional \(r^{-2}\) singularity, forcing \(d=\psi(p)\). This proves equivalence to the point-remainder estimate (2).
3. On a dyadic Fourier square shell with \(O(2^{2j})\) modes, Cauchy–Schwarz gives \(\|\psi_j\|_\infty\lesssim2^j\|\psi_j\|_2\), and differentiation adds a factor \(2^j\). Sum over spatial annuli. Apply the adjoint Hardy inequality \(\sum_i(\sum_{j>i}a_j)^2\le4\sum_jj^2a_j^2\), proving the \(\beta=1\) endpoint.
4. For each \(N\), the explicitly displayed \(\psi_N\) uses \(N\) disjoint positive-quadrant Dirichlet blocks. Check that each has point value \(1\), Fourier weighted squared norm \(\asymp(1+j)^{2\beta}\), and uniformly small modulus whenever its frequency greatly exceeds inverse distance to \(p\). On order \(N\) disjoint spatial annuli this gives a cumulative \(N^3\) lower bound, contradicting the Hardy bound when \(\beta<1\).
5. Independently verify the sourced Gaussian theta expansion and unique simple zero (Hart et al., 2025, Section 4.3). All estimates are uniform in the deleted atom by unitary lattice displacement.

No numerical enumeration or external software is required. The proof is an infinite-dimensional argument; its exactness cannot be established by a finite checker. The material Lyubarskii–Seip (1999) full-text overlap risk remains, and independent assessment is not performed.
