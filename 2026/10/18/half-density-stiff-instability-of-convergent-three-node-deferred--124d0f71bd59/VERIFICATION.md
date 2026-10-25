---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For the stated Q and implicit Euler D, direct SymPy reconstruction gives tr B(z)=z(11z-24)/(12(z-2)^2), det B=z^2/(4(z-2)^2), negative discriminant for z<0 and spectral radius |z|/(2(2+|z|))<1/2. At z->-infinity the affine stage block is [[1/3,1/12],[-2/3,7/12]] with fixed point (-1/2,1). The endpoint error recurrence e_(K+2)=(11/12)e_(K+1)-(1/4)e_K, e0=0,e1=-1 gives eK=-2^(1-K) sin(K theta)/sin(theta). Since 2 cos(theta)=11/6 is nonintegral rational, theta/pi is irrational, implying density exactly 1/2 by equidistribution. Independent exact recurrence gives R8=35934757/35831808, and direct 8 rational sweeps yield R8(-5000)-1=756246564724929917066932564741749988412224800808855000/1708230988498214163982099587351742945781521223046779160729>0. This distinguishes fixed-negative-z convergence from separate stiff-limit K.

## originality

PASS

The generic SDC iteration/preconditioning and stiff matrix formalism are established, but the exact nonadaptive 3-Lobatto IE endpoint recurrence and sweep-count equidistribution appear unreported in the primary articles compared; broader diagonal sweeper work uses different node and preconditioner families. Priority remains best-of-knowledge.

## value

PASS

An unstable finite-sweep update on a negative real scalar decay mode despite converging correction iteration is a direct, nontrivial numerical-analysis stability gap; locating its first K=8 witness and proving half-density gives a precise and potentially actionable pathology, not a trivial reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
