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

The bundled `verify_fork_preorder.py` checks the finite combinatorial consequences independently of the proof text.

It exhaustively enumerates every state vector in \(V^{\binom{k}{2}}\) for \(1\le k\le4\), where \(V\) is the fork \(0<+,0<-\). It verifies:

- mutual reachability in the product order is equality;
- the rank distribution is the coefficient sequence of \((1+2q)^{\binom{k}{2}}\);
- the number of ordered comparable pairs is \(5^{\binom{k}{2}}\);
- the number of directed covers is \(2\binom{k}{2}3^{\binom{k}{2}-1}\) for \(k\ge2\);
- every comparable interval has Möbius value \((-1)^{r(y)-r(x)}\).

It also computes Stirling numbers by recurrence and checks the displayed all-tuple formulas and first seven values for the strong-orbit, comparable-pair, and cover sequences.

The finite checker does not certify the infinite extension step. That step uses the published theorem that the generic digraph without 2-cycles is MB-homogeneous, meaning that every finite monomorphism extends to a bimorphism.
