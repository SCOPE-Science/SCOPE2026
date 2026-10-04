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

The proof has three checkable layers.

1. **Prime-tail criterion.** The published greedy density proof applies after deleting the primes \(2\) and \(3\). At \(r=2\), the published monotonicity of \(F_m\) reduces all tail inequalities to the direct check at \(m=4\), where
\[
F_4=\frac{1807104}{2941225}>\frac{39}{64}>\frac{6}{\pi^2}.
\]

2. **Finite overlap chain.** The eight constants from exponents \(0,1,2\) at primes \(2\) and \(3\) are checked exactly. Their smallest consecutive ratio is \(117/128\). The classical bound \(\pi>3.14\) implies \(9/\pi^2<117/128\), so the associated intervals overlap from \(6/\pi^2\) through \(73/81\).

3. **Gap separation.** The classical bound \(\pi<22/7\) implies \(73/81<9/\pi^2\), proving the two components are disjoint.

`verify.py` checks the exact rational arithmetic and exhaustively evaluates the defining function for every integer through \(200000\). That finite sweep is not used as an infinite proof and does not establish novelty.
