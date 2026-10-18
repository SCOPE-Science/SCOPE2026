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

Characteristic not 2 separates twist eigenspaces for alpha=diag(1,-1,-1). Twist-commutation forces block N=[[a,0,0],[0,b,d],[0,c,e]]. Recomputed Nijenhuis torsion: D(e1,e2)= -d(a-e)e2+(ab-ae-be+cd+e^2)e3 and D(e1,e3)=-d^2e2+d(a-e)e3. Since d^2=0 over a field, d=0; torsion vanishes iff (a-e)(b-e)=0, precisely union of two affine A3 components meeting in A2. Count 2q^3-q^2 for q odd, rank tuple 1,(q-1)(q+2),(q-1)(3q-1),q(q-1)(2q-3) by component inclusion-exclusion, zero deformed bracket 2q^2-q. Hom-Lie automorphisms have (s,p,r) block shape and conjugation c maps to sc+(r/p)(b-e), giving q(q-1)+q^2+q^2=3q^2-q normal forms; zeta follows point counts over F_{q^m}. Independently recomputed defects and enumerated every twist-compatible matrix over F3,F5,F7, yielding 45,225,637, correct rank profiles and zero-deformation counts; finite checks corroborative only.

## originality

PASS

Best-of-knowledge PASS for this concrete reducible Nijenhuis variety, finite-field ranks, bracket fiber and conjugacy census. General Hom-Lie Nijenhuis identities are established prior art. The highly relevant 2021 Das–Sen article could not be read in full: arXiv and lawful open-access full-text attempts failed, and authorized Oxford route returned vpn_disconnected; explicitly residual priority risk, not automatic scientific failure. Full 2024 same-framework preprint was inspected and did not cover this involutive Heisenberg twist.

## value

PASS

This small canonical nontrivial Hom-Heisenberg example exhibits a reducible operator variety with exact rank, deformation, isomorphism, automorphism-orbit and zeta distributions. The conjunction gives natural algebraic-geometric classification and distinguishes it from automatically Nijenhuis twist cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
