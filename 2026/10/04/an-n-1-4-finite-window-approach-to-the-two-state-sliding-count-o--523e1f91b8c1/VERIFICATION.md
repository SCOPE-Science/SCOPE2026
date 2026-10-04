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

`verify.py` performs three independent finite checks using only the Python standard library.

First, it enumerates binary paths for small window lengths with exact rational arithmetic and recovers the first-order coefficients
\[
\frac{\Pr(K_0=k)}u\to s^{k-1}\bigl(2+(n-k-1)r\bigr),
\qquad
\frac{\Pr(K_0=n)}u\to \frac{s^{n-1}}r,
\]
and the projected upward-edge coefficients
\[
\frac{\Pr(K_0=k,K_1=k+1)}u\to s^k.
\]

Second, it compares the energy and second-moment coefficients produced by those enumerated path weights with the closed forms used in the proof.

Third, it evaluates the exact finite geometric-sum rare-limit quotient for increasing \(n\) at the theorem's tuning and checks convergence of
\[
n^{1/4}\left(R_n^0-\frac14\right)
\]
toward \(1/\sqrt2\), with the next normalized residual approaching the analytically predicted coefficient \(7/8\).

The script's finite calculations do not prove the infinite asymptotic statement. That statement is established in `RESULT.md` by exact path classification, geometric-sum identities, Taylor expansion, and a superexponential bound on the finite-\(u_n\) remainder.
