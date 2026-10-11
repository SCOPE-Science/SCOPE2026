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

# Reproduction and proof checks

Run `python verify_golden_dyadic.py` with Python 3 and `mpmath` available. The interval calculation uses 45-digit outward enclosures and terminal depth 36. It proves the two conservative rational ranges for the imaginary parts of the Fourier transform at \(1\) and \(2\). The error bound follows directly from \(\operatorname{supp}\mu\subset[0,2/3]\) and \(|e^{i\theta}-1|\le|\theta|\), and it is propagated without amplification because \(p+q=1\).

The infinite part is independently established symbolically in the proof: for integer \(n\ge2\), \(e^{\pi i2^n}=1\), so the Fourier imaginary part obeys \(u_n=p u_{n-1}+q u_{n-2}\). Hence the two rigorous initial inequalities imply \(u_n>1/5\) for *all* integers \(n\ge0\). No finite enumeration is mistaken for a complete proof.

To reconstruct the total-variation certificate, check the affine pushforward equalities \(T\circ S_0=\mathrm{id}\), \(T\circ S_1=S_0\) and, for integer \(n\ge2\), \(T^n\circ S_1=T^{n-2}\) modulo one. Then solve the measure recurrence and use the disjoint support intervals \([0,1/3]\) and \([1/2,2/3]\). This establishes the *exact* total-variation value for every integer \(n\ge0\), without experimental assumptions.

Scope: no Fourier-zero assertion outside the dyadic-frequency family; no claim about spectrality; no external independent audit performed. The 2026 motivating manuscript was not available in full for literary comparison.
