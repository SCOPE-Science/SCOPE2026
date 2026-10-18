---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Using p=2m+1 and h=2m, source B_i triangle indeed has signed edges (2,h,h), A_i has (1,1,−2); all edges are ±1, ±2, ±h modulo N=2h+2. For m≥4, a bounded symbolic 3- or 4-step case division leaves four oriented triangle step multisets (all actual faces) and four nonbacktracking quadrilateral patterns that give exactly U,V,W,R,S after cyclic ordering; U,V,W bound pairs of A/B triangles. The Z-valued edge cocycle α(+1)=1, α(+2)=2, α(+h)=−1 is closed on every face, nontrivial on the +1 Hamiltonian cycle, but zero on R,S. The F2 cocycle β supported on h-edges by vertex parity is closed and has β(R)=β(S)=1, proving each surviving cycle is nonzero pure order-two in H1(Klein;Z)=Z⊕Z/2. R has N and S has p distinct unoriented translates, yielding exactly 6m+3 carriers of minimum length four; no essential triangle. Independent enumerations at m=4,5,8,12,20 confirmed step patterns and counts; uniform symbolic argument supplies universal m≥4 scope.

## originality

PASS

Datta–Upadhyay arXiv:math/0403433 original and revised versions identify Q_{2m+1,n} Klein-bottle triangulations and give the cyclic n=2 construction, but their text examines automorphisms, weak regularity and other short induced cycles rather than complete nonzero integral 1-systole representatives. Resultary nearby Q_{7,2} (m=3) short-cycle spectrum is specifically excluded by the present theorem, has free classes absent for m≥4, and does not imply stabilization; the own Resultary exact match is not independent prior coverage. Searches using torsion/nonbounding quadrilateral and Q-notation found no stronger formula for all m≥4.

## value

PASS

This is an infinite natural triangulated Klein-bottle family where shortest nonzero integral cycles unexpectedly represent only orientation torsion, with a complete orbit-count formula and a genuine low-parameter boundary. The torsion/free distinction, sharp length and full carrier classification are useful and mathematically motivated beyond code enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
