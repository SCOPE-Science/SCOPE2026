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

The companion `artifacts/verify.py` uses only the Python standard library.

It first computes Stirling numbers of the second kind by recurrence. Independently, it enumerates set partitions as restricted-growth strings. For each \(2\le r\le5\) and each tested small arity, the two equality-pattern counts agree and the direct sum over equality patterns and arbitrary \(r\)-hyperedges agrees with
\[
T_r(n)=\sum_{k=0}^{n}S(n,k)2^{\binom kr}.
\]

For \(r=2\), the script checks the published A335390 initial values
\[
1,1,3,15,127,1895,53071,2953575,337064047.
\]

It then rewrites the exact ratio \(T_r(n)/I_r(n)\) as the collision-layer sum
\[
\sum_{j=0}^{n}S(n,n-j)2^{-\left(\binom nr-\binom{n-j}{r}\right)}
\]
and checks this identity exactly using rational arithmetic. The first and second collision layers are checked separately.

Finally, it normalizes the noninjective excess by the predicted leading term
\[
\binom n2 2^{-\binom{n-1}{r-1}}
\]
for \(2\le r\le5\). For \(r=2\), the normalized ratio decreases from about \(1.0258901\) at \(n=12\) to \(1.0000000013\) at \(n=40\); for larger \(r\) the correction beyond the first layer is already below ordinary floating-point display precision at much smaller \(n\).

The replay terminates with `VERIFY_OK`. The script verifies the finite identities and numerical convergence; the asymptotic tail bound itself is the mathematical argument in `RESULT.md`.
