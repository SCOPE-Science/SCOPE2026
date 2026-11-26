---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With k represented in 0,…,N−1, split the cyclic sum at j=k: the wrapped terms acquire w=γ^N, and z=|γ|²ω^b has z^N=|w|². The resulting numerator is w−|w|²+(1−w)z^k, and the z=1 limit is the stated linear sum. Off the unit circle a zero requires |z^k|=|w|, using |w̄−1|=|1−w|, hence k=N/2. The remaining equation (−1)^b=(|w|−w/|w|)/(1−w) gives exactly odd b for positive w and even b for negative w, and rules out other phases. On the unit circle the nonzero-frequency numerator vanishes exactly when w=1 or N divides kb; the zero-frequency equation requires k=N/2 and w=−1. The gcd count includes k=0 correctly. In the Weyl basis the coefficients of the base projector are proportional to conjugate ambiguities. Orbit conjugation multiplies each by a distinct character, so character orthogonality isolates exactly the nonzero coefficients and their directions, proving the complex rank. In the missing half-shift Weyl modes the entries at (j,j+m) and (j+m,j) differ by (−1)^b, and either parity supplies a full m-point Fourier basis on j=0,…,m−1. Hermiticity then makes the independent entries imaginary antisymmetric or real symmetric, as stated. A nonzero block has eigenvalues ±1 on its two coordinates and yields a rank-one positive pair with identical data. Flat unit-circle atom magnitudes give the coordinate-vector witness. For nonunit ratios shifts 0 and 1 are measured in every N≥3, including N=3 and N=4, so the rank-one diagonal and first cyclic off-diagonal determine the phases for full support. The inspected verification script's floating-point data checks illustrate these cases but do not replace this exact analysis; I did not execute the frozen upload.

## originality

PASS

A previous positive-real geometric record covers precisely the positive-w nonunit branch up to simple equivalences, including its kernel. A fixed complex seed and the general rank/recovery criteria are also previous inputs. The supported distinction is the complete parameter diagram beyond those already covered cases: all complex nonunit zero loci and the negative-w kernel, all unit-circle strata and counts, and the resulting exact arbitrary-signal versus full-support boundary. A later catalog record states the same complete zero/rank diagram; the demonstrated overlap is reported separately from priority.

## value

PASS

This is a natural low-parameter window family for complete-orbit tomography, and a single zero-free example or the usual sufficient theorem cannot distinguish degeneracy of the measurement operator from ambiguity of rank-one signals. The exact resonance/parity and unit-modulus arithmetic strata quantify every rank defect; the explicit low-rank kernel and full-support comparison show how the same measurements can lose injectivity on sparse signals without losing it on full-support signals. That provides useful exact information beyond the already known positive-real branch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
