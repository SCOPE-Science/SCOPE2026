---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The actual RESULT.md specifies open neighborhoods N(i)=i+{-3,-2,-1,1,2,3} and an n>=13 short-arc normalization. We reconstructed the ten ordered free-face orbit removals and periodic R=Q[t,t^-1] boundary template, and independently computed D1D2=D2D3=0 as Laurent-polynomial matrices, a unit 5x5 minor of D2, a unit 4x4 minor of D3, and a 5x5 minor of D3 equal to -(t+1). These certify Smith factors (t-1), five units, and four units plus t+1; tensoring with R/(t^n-1) and PID UCT yields the parity-sensitive homology and rotation eigenvalues. Independent fixed-face trace sums in dimensions 0..5 were [1,-6,-2,4,0,-1] for odd n, [2,-6,-4,6,0,-2] for even n/even j and [0,-6,0,2,0,0] for even n/odd j, giving higher reflection signs; the degree-one circle map reverses under s. Rational averaging after barycentric subdivision proves ordinary quotient invariant-homology identities. The finite n=13..25 collapse replays alone would not prove all n, so uniform locality of 13 distinct residues and the explicit free-face incidence test were checked as the needed universal argument.

## originality

PASS

Distinct equivariant refinement: the complete D_n representation and ordinary quotient rational homology are not supplied by the previously published complete nonequivariant C_n^3 bundle classification; targeted primary and indexed searches revealed no dominating character theorem.

## value

PASS

Classifies all positive-degree rational D_n representations for a natural infinite graph family, distinguishing the two even-order reflection classes and computing the rational topology of two different symmetry quotients. These are structural refinements of a known sphere-bundle topology and are not mechanical Betti-number restatements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
