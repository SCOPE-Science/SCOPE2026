---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

With the stated Fourier convention the quadratic form is the negative of the 2 log|s| form. The cutoff reciprocal kernel plus diagonal 2 log epsilon+2 gamma yields this multiplier; for the unit constant on (0,1) the renormalized value is 2 gamma-2, and rescaling a unit cell subtracts 2 log N. Direct cross-cell integration gives c_k even at k=1, whose corner is integrable. Strict Jensen gives c_k>1/k; the symmetric triangular second moment is 1/6, giving the cubic leading term, and the second differences telescope against H_m to 1-gamma. Polarization with zero extension gives the exact stated identity for every unit complex vector, including all shift terms k>=N. The constant-vector lower bound and bounded remainder give a lower bound on the continuum form along the Perron sequence. Compact support controls low frequencies and the lower form bound gives a high-frequency Fourier tail O(1/log R), hence strong L2 precompactness. The phrase 'boundedness of the logarithmic kernel near zero' in line 69 is inaccurate; the kernel there is integrable and the Fourier transforms are uniformly bounded, so dominated convergence gives precisely the needed low-frequency convergence. Fatou gives the high-frequency inequality. The fixed shifts k/N vanish on every strongly convergent subsequence and summability removes the entire discrete remainder. Compression and mollification give density in the logarithmic form norm. The cell-average error for a smooth test function has sup norm O(1/N) and uniformly bounded total variation, giving squared translation differences bounded by min(O(N^(-2)),O(|h|/N)); integration proves H^t convergence for 0<t<1/2 and thus the Rayleigh recovery bound. The resulting continuum maximizer is unique in the nonnegative unit class by Chen–Weth, so all Perron histograms converge. The finite checker was inspected, not executed; it checks finite algebra and gives sample eigenvalues, not a proof of this limit.

## originality

PASS

The same matrix, bounded-error growth, finite positive optimizer, and continuum ground-state theorem are established prior work. In the inspected sources none gives the additive limit, strong profile convergence, or exact cell-form identity of this matrix. The pass is limited to those distinct claims.

## value

PASS

It sharpens a natural critical finite HLS problem from a bounded error to an exact spectral constant and identifies the optimizer's continuum shape. The exact cell comparison also explains why the continuum operator gives the unshifted additive constant and why the discrete correction disappears. A numerical enclosure or convergence rate would be separate work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
