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

The general proof is symbolic and classifies every character. The accompanying finite replay is a consistency check of the character arithmetic and divisor-cohomology case split.

For each \(n\) from \(2\) through \(8\), `verify.py` enumerates all six-tuples of edge weights in \(\{0,\ldots,n-1\}\) whose total is divisible by \(n\). For each character it computes
\[
d=\frac1n\sum_e a_e,
\qquad
b_v=\left\lfloor\frac1n\sum_{e\ni v}a_e\right\rfloor,
\qquad
k=\#\{v:b_v=2\}.
\]
It then evaluates Riemann--Roch and the explicit Serre-duality dimension for plane curves of degree at most two through up to four general points.

The replay checks that the only characters contributing nonzero \(H^1\) have \((d,k)=(2,1)\) or \((4,4)\), each with one-dimensional contribution. It verifies the totals
\[
0,5,15,30,50,75,105
\]
for \(n=2,3,4,5,6,7,8\), exactly matching \(5\binom{n-1}{2}\). It also checks the closed polynomial for \(p_g\) and the value \(p_g(Y'_6)=1975\).

The replay output stored in `verification_output.txt` must end in `VERIFY_OK`.

Unproved limits: finite enumeration does not prove the all-\(n\) statement, literature novelty, the Albanese geometry, or the full graded local-cohomology module. Those limits are handled by the mathematical proof and literature comparison rather than by the script.
