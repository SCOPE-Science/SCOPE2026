---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Path-basis J has vector spaces U⊕F_q⊕W⊕U⊕W⊕(U⊗W), dimension 2a+2c+ac+1. Commutator equations are tu−sv=0, sx−tw=0 and u⊗y−v⊗z+p⊗x−r⊗w=0. Top paths are central, giving factor q^(2ac). When (s,t)=0, rank-r a×4 matrix M and 4×c matrix N give MN=0, contributing Z=sum R_(a,4)(r;q)q^((4−r)c). When (s,t)≠0, u=su0,v=tu0,w=sw0,x=tw0, and remaining tensor map P0⊗w0+u0⊗Q0 has rank 0,a,c,a+c−1 in the four zero/nonzero configurations. Its kernel counts yield T and the q²−1 scalar multiplier, exact in all characteristics. Burnside commuting pairs / |J| yields class number of 1+J. Independent modular commutator-matrix rank enumerations for (a,c,q)=(1,1,2),(1,1,3),(2,1,2),(1,2,2) reproduced 1024,41553,30208,30208. They corroborate but do not prove the all-prime-power formula.

## originality

PASS

Qualified best-of-knowledge PASS solely for the uniform explicit closed C_(a,c)(q), not polynomiality: Hennecart–Perry solve path-length≤2; here every a,c positive give length 3. Goodwin–Röhrle cover polynomial class counts for ≤5-step parabolics and Pak–Soffer provide general pattern-group recurrences. Neither accessible statement prints this symbolic outer-block expression, though complete technical texts and potential small-parabolic coefficient tables were not read, a material priority risk.

## value

PASS

A compact exact class-count for the natural four-block (a,1,1,c) unipotent radical uniformly in a,c and all finite fields, reducing arbitrary outer sizes to ranks of a×4 matrices. Answers an explicit first longer-path case of a motivating quiver counting problem, a useful reference formula even though polynomiality and algorithmic countability are known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
