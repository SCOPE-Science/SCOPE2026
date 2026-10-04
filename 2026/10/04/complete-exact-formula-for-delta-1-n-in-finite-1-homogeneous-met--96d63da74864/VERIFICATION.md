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

The proof was replayed as a chain of four explicit statements.

1. A finite \(1\)-homogeneous metric space gives a vertex-transitive edge-coloring of the complete graph by positive distance values.
2. Every positive singleton distance is a color of valency \(1\), hence one of the odd entries controlled by Edmonds' Theorem 1.4. For even \(n\), Edmonds' Theorem 1.2 gives at most \(n/2+n_2/2-1\) such positive singleton colors. Including the zero distance gives \(|S_X|\le n/2+n_2/2\).
3. Observation 6.2 of Bargetz et al. then gives \(\delta(X)\le(n+|S_X|)/2\le(3n+n_2)/4\).
4. If \(n=2^a(2k+1)\) with \(a\ge1\), Example 6.10 has exactly \(2^{a-1}(3k+2)=(3n+n_2)/4\) distances, proving sharpness. The odd case is already exact in Proposition 6.7.

The bundled `verify.py` checks the arithmetic identity and integrality of the closed form for \(1\le n\le4096\), and checks that it reduces to the previously established odd, power-of-two, and \(2\)-adic-valuation-one formulas. This finite computation is only an arithmetic replay; the proof of the all-\(n\) theorem is the argument above.
