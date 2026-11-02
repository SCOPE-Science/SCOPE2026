---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For a,b>0, p=b/(a+b), q=1-p, u∈(0,1), s=h(a+b)>0, the supplied stage reduces error to (u−p)R(s,p,u). Independently expanded N′D−ND′=−H with each H coefficient positive since E=u(1−u)/(pq)>0 and B−E=(u−p)^2/(pq)≥0. Thus R strictly decreases from 1 to −1/(1+B); comparing the flipped weighted-density maximum for positive or negative initial error gives a violation precisely when max(p,q)>(√5−1)/2. The exact strictly interior witness (p,u,s)=(3/4,9/10,10) yields output (15134/21985,6851/21985), violating 6/5. Independently verified symbolic derivative and rational state update; finite checks do not prove the universal theorem. The endpoints u=0,1 and s=∞ are excluded and used only in suprema.

## originality

PASS

At the stated best-of-knowledge level, the specific step-uniform inverse-golden-ratio frontier for the equilibrium-weighted maximum is not a theorem or immediate corollary in the inspected closest Patankar sources; exact rational endpoints and qualitative oscillation analysis remain prior art.

## value

PASS

The equilibrium-relative maximum is an intrinsic Markov comparison invariant beyond positivity and mass conservation; an exact sharp equilibrium-asymmetry threshold in the smallest nontrivial Chang–Cooper/MPRK diffusion identifies a real numerical invariant-region loss. It is not an arbitrary method parameter slice or a generic restatement of Patankar positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
