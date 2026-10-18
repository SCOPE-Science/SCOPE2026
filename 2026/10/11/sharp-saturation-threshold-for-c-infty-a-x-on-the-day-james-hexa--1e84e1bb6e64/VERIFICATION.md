---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For real hexagonal plane N(s,t)=max(|s|,|t|,|s-t|), the defining three-vector quotient is min(N(x+y)^2,N(x-z)^2)/(2N(x)^2+N(y)^2+N(z)^2), with N(y-z)<=a N(x). Universal bound 1 follows by the two triangle inequalities plus (r-s)^2+(r-t)^2>=0. For a>=1 take x=(1,1), y=(0,1), z=(-1,0), yielding both shifted norms 2, denominator 4 and separation 1; strict-constraint endpoint a=1 follows by taking y=(0,1-e), z=(-(1-e),0) and e down to 0. If subcritical a<1 saturated as supremum, normalize a maximizing triple to the compact unit-ball domain; the nonzero limit has r=s=t=1 and N(x+y)=N(x-z)=2. Supporting-face equality forces x and y on one exposed edge and x and -z on one exposed edge. If x is edge-interior, both companion vectors share the same face and N(y-z)>=2; if a vertex, incident same-edge or cross-edge faces force N(y-z)>=1. This contradicts separation <=a<1. Independent exact rational endpoint fractions and finite vertex/edge geometry confirm; the proof, not sampled parameters, handles every a>0.

## originality

PASS

Best-of-knowledge comparison against the same primary mathematical object, stronger theorems, equivalent reductions, exact tables and indexed related results finds no previously established result implying the full final statement. Searches alone are not novelty proof. Most relevant full primary texts were read where accessible; restricted sources and mathematical priority uncertainties are named below.

## value

PASS

The defining separation parameter a controls saturation of the universal upper bound for a natural hexagonal Banach plane. The source examples establish saturation from a threshold but not sharpness; identifying precisely the subcritical nonsaturation range closes a natural equality-geometry question and provides a reusable exposed-face obstruction. This is an exact natural invariant boundary, not an arbitrary numerical slice, though it does not give the full subcritical profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
