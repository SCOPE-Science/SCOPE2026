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

# Direct proof and computation checks

The proof was reconstructed from the stated normalized-Laplacian spectrum: \(\lambda_k=1-\cos(2\pi k/N)\). It checks the Fourier basis normalization, both two-by-two Gram eigenvalues, the constant block, the integer circular-spacing pigeonhole bound, the explicit maximizing residue, equality rigidity when \(K+1\mid M\), and invertibility of the temporal Vandermonde matrix. These arguments apply to all allowed integers, not just to tested sizes.

The standalone file `verify.py` uses only the Python standard library and checks every integer \(5\le N\le120\) and every strict low-pass cutoff \(1\le K<N/2\). For every nonzero sensor separation it evaluates the modular angular gap and compares the trigonometric formula; in addition it checks the sharp maximum, counts all optimal separations when \(K+1\mid M\), and directly diagonalizes representative complex Fourier Gram blocks. The emitted PASS line records the executed finite checks.

Limitations: numerical checks alone prove no infinite-domain statement; that statement rests on the displayed analytic argument. The optimal bounds concern the demixed spectral samples, **not** the raw time-trajectory Euclidean norm. Complete text of the motivating 2026 preprint was unavailable for a decisive literature comparison; no external or independent audit is represented here.
