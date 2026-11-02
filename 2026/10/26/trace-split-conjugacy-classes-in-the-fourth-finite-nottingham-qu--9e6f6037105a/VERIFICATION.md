---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For q=2^e and f=t+at²+bt³+ct⁴+dt⁵ mod t⁶, direct formal composition shows that conjugation preserves a,b and changes c,d by Δc=aA²+(b+a²)A+aB and Δd=bA²+a²B. Central a=b=0 has q² singleton classes. For a=0,b≠0, the invariant d+c²/b yields q(q-1) size-q classes. For a≠0,h=b+a²=0, d+ac yields q(q-1) size-q classes. When ah≠0, B adjusts c arbitrarily while Δ(d+ac)=h(A²+aA); normalized A/a maps via u²+u onto trace-zero elements, so precisely two trace fibers per leading pair, each size q²/2. Hence K_q(X)=q²+2q(q-1)X^q+2(q-1)²X^{q²/2}, k=5q²-6q+2 and cp=k/q⁴ (combine exponents at q=2). Independently constructed GF4 arithmetic, enumerated all 256 elements into actual conjugacy orbits, obtaining {1:16,4:24,8:18}; independently checked all corresponding direct composition commutators. General q assertion follows from elementary Artin–Schreier image argument, not the GF4 enumeration.

## originality

PASS

Claim-specific Resultary and relevant primary literature were compared by statements and implications. The assessed specialized mathematical statement was not identified as covered in the material actually inspected. This is a best-of-knowledge judgment, not absolute novelty proof; stronger plausible inaccessible works are explicitly retained as priority risks.

## value

PASS

An exact full conjugacy-class size distribution and commuting probability for a natural low Nottingham quotient over all characteristic-two extension fields is meaningful finite-group structural information. The q=2 prime-field specialization is explicitly prior; extension-field Artin–Schreier trace split is the substantive new classification, with no claims for higher quotients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
