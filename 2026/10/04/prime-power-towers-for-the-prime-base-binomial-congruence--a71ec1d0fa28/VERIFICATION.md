---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Jacobsthal--Ljunggren gives \(B_j\equiv B_{j-1}\pmod{p^{3j}}\), so \(B_r\) converges and already equals its limit modulo \(p^r\). LTE gives the analogous Teichmüller convergence for \(q^{p^r}\). Their difference therefore controls the congruence exactly. The first binomial lift is \(q\) modulo \(p^3\), which yields the two stated low-level Wieferich equivalences. The verifier independently checks 60 cases through \(r=4\) and selected lift valuations.

## originality

PASS

The full Guedes--Machado paper, obtained through authorized institutional access after open retrieval failed, proves only the square \(p^2\) layer as a base-\(q\) Wieferich criterion and otherwise studies the different family \(n=q^t p\). No all-\(p^r\) tower or p-adic limit criterion appears there, and targeted searches found no predecessor.

## value

PASS

The theorem organizes every higher prime-power layer of a natural congruence into one p-adic invariant, proves an initial-segment law, and identifies the cubic layer as a higher-Wieferich condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
