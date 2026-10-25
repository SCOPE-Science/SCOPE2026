---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The seven degree-one components are intrinsically preserved by every projective automorphism of C=V(LQ). Their 21 pairwise intersections give five triple points and six doubles; the unique two collinear triples through P0 force P0 fixed and preserve or swap x=0,y=0. Fixing them individually and the third line x-y=0 gives matrices [x:y:cx+dy+ez]; target-pair constraints give exactly (c,d,e)=(0,0,1) or (2,1,-1). Swapping x,y would require simultaneously e=±2 and e=±1/2, impossible. The second matrix tau squares to identity, permutes all seven lines and fixes Q=z(z-2x-y)+(1-i)xy. These exhaustive two candidate line symmetries each fix Q and Qbar separately; coefficients of xy 1±i show Q and Qbar are nonproportional, so C and conjugate Cbar are not projectively equivalent. Field-of-moduli conclusion is restricted to projective equivalence over Qbar and Q(i). Independent exact SymPy incidence and polynomial-substitution checks reproduced five triple points, six doubles, invariance L/Q, plus coordinate-case arithmetic; no finite sampling claims completeness of PGL3.

## originality

PASS

The source article constructs the seven-line-plus-conic near-free arrangement but does not calculate its full PGL3 stabilizer or rule out real projective descent in inspected Section 4. These are distinct exact projective invariants requiring the new line-frame exhaustive argument. An earlier real free arrangement with same weak combinatorics is expressly acknowledged and not counted as the new contribution. Searches for exact conic coefficient, stabilizer and conjugation descent yielded only neighboring non-identical arrangements; historical priority is best-of-knowledge.

## value

PASS

The automorphism and real-descent obstruction is a mathematically motivated exact rigidity invariant of a published near-free arrangement bearing on an explicit real-case existence question. It excludes an otherwise plausible coordinate-change approach, while distinguishing the fixed model from other real witnesses; not just observation that a coefficient is nonreal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
