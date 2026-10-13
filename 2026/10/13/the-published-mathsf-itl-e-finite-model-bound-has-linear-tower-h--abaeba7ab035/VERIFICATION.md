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

The verifier checks the recurrence transcription and the numerical boundary inequalities used by the symbolic proof.

For manageable \((n,k)\), it computes \(E_k^n\) and \(Q_k^n\) exactly and verifies
\[
T_{k-1}(n)\le E_k^n\le\frac12T_{k-1}(3n),
\qquad
Q_k^n\le T_{k-1}(3n).
\]
It then checks, on broad exact integer ranges, the two scalar inequalities that make those inductions uniform:
\[
\log_2(n+1)\le\frac{3n}{2}-1\quad(n\ge2),
\]
encoded without floating point as \((n+1)^2\le2^{3n-2}\), and
\[
1+\frac{D^2}{2}\le2^D\quad(D\ge6).
\]
It also verifies \(\log_2^*T_h(x)=h+\log_2^*x\) on every tower small enough to construct directly.

Replay:

```text
python3 verify_tower_height.py
```

The finite replay is not the proof of the all-\(s\) statement. The proof is the uniform induction and final envelope in RESULT.md. Independent audit has not been performed.
