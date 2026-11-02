---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Pick's theorem gives h*_P=1+a z+b z^2 with a-b=B_P-3>=0, and similarly Q. The standard join series has h*=h*_P h*_Q over (1-z)^6. Direct binomial-basis expansion shows n=U/60 and n^2=V/24, with U=137+12(a+c)-3ac+2ad+2bc-3bd-3b-3d and V=45+10(a+c)-ac+bd-b-d. Cubic=((a-b)(c-d)+7(a+c)+b+d+17)/24>0, quartic=(ac-bd+2(a+c)+b+d+3)/24>0, leading NM/120>0, constant 1. The exhaustive relaxed integer Pick-data domain includes every realizable polygon pair: N<=M, NM<=168, 0<=b<=(N-1)/2, 0<=d<=(M-1)/2, a=N-1-b,c=M-1-d. Independent exact enumeration found all 14,438 states below 168 with min U=5,min V=45, and among 14,838 states up to 168 only (N,M,b,d)=(12,14,0,0) with U=-4,V=142. Explicit empty triangles of normalized areas 12 and 14 realize n=-1/15; a primitive-boundary triangle of normalized area 157 realizes the independent n^2=-1/24 pattern. The all-volume criterion is algebraic, not extrapolated from the cutoff search.

## originality

PASS

The general join formula and failure of Ehrhart positivity are established by Liu–Tao–Xin (2026); the novelty under assessment is the sharp two-polygon parameter classification, volume threshold and two independent sign mechanisms. The inspected join theorem and generic operation survey do not state the exact bound or uniqueness; search absence is not absolute priority proof.

## value

PASS

A sharp first-size obstruction for the smallest equal-dimensional polygon factors addresses the natural follow-up to general failure of Ehrhart positivity under joins. The all-parameter sign criterion, uniquely first failing Ehrhart data, sharp realizable threshold 168, and separated linear/quadratic failures are structurally useful and not merely table recomputation. The result makes no unjustified claim about all 5-polytopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
