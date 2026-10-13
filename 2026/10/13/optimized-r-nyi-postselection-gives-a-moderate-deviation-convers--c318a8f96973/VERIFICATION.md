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
# Verification

The analytic argument has two imported premises from arXiv:2610.02176v1: the exact postselection inequality with \(g_{n,d}=\binom{n+d^2-1}{d^2-1}\), and a channel-uniform second-order bound on \(Q^\downarrow_{1+t}\) for \(0<t\le1/2\). The source proves both premises.

The new steps are algebraic. The verifier checks that substituting \(t=\sqrt{L/n}\) into the finite-\(n\) coherent-information bound gives the displayed \((a+1)\sqrt{L/n}+(c+1)L/n\) expression, and that for \(K=a+c+1\), \(0<\Delta\le K\), and \(t=\Delta/(2K)\), one has
\[
a t+c t^2\le\Delta/2,
\qquad
\frac{t}{1+t}\ge\frac{\Delta}{3K},
\]
so the fidelity exponent is at least \(n\Delta^2/(6K)\).

Run `python3 artifacts/verify.py` from the package root. Expected output: `VERIFY_OK`.

The script uses only the Python standard library and a deterministic parameter grid. It does not numerically verify the quantum postselection lemma, the Rényi-divergence expansion, or fidelity monotonicity; those are analytical source premises. No finite numerical test is used to infer an infinite-dimensional or asymptotic statement.
