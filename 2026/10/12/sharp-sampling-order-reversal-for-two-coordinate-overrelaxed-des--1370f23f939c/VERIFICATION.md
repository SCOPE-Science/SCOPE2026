---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Diagonal Hessian normalization yields C=[[1,c],[c,1]], 0<=c<1, and exact overrelaxed coordinate maps U,V. Direct matrix pullbacks for the two permutations versus four replacement pairs give generalized modal difference ω²(1-c²)(2-ω)/4 times [2-ω(1+c)] on symmetric C-energy and [2-ω(1-c)] on antisymmetric C-energy. The latter coefficient is always positive on 0<ω<2. Thus uniform strict P-over-R preference holds iff ω<2/(1+c), becomes nonstrict on one mode at equality, and preferences reverse by mode above it for c>0. Independent symbolic expansion recovers the factors and exact worst-case example at c=1/2,ω=19/10: P worst-case 137143/160000 > R worst-case 53949/64000. The one-coordinate decrement -ω(2-ω)[(Cy)_i]^2/2 is nonpositive. Results are one epoch only.

## originality

PASS

Recht-Re two-factor PSD norm inequalities and Oswald-Zhou randomized SOR convergence bounds do not yield this exact two-dimensional statewise relaxation threshold where coordinate maps are overrelaxed. Work on exact coordinate minimization corresponds to ω=1 and misses the reverse mode. Closest independently identified Resultary Kaczmarz results concern other update protocols.

## value

PASS

Determines the maximal relaxation range for universal random-permutation advantage and constructs a sharp opposing-mode/worst-case failure regime even while every elementary update decreases the quadratic objective. This is a motivated question in randomized coordinate methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
