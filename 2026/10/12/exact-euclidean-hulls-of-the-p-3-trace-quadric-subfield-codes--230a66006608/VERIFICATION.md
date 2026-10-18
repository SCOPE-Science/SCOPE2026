---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For p>3, F_p^× scaling of S annihilates both degree-one and degree-two moments; since |S|=p^5-p^3+p^2 is 0 in F_p, the seven-generator Gram matrix is zero. For p=3 the source complete enumerator has weights 144,153,162,225, all multiples of three; self-dot=weight mod 3 and polarization give all inner products zero. In the unpunctured code Gram(u,v)=Tr(b)Tr(b' ), and trace surjectivity gives one-dimensional Gram rank, hence hull dimension 6. The argument assumes source dimension 7; a finite check alone is not a universal proof. Independent check: The scalar-invariance Gram proof was algebraically reconstructed, and the source p=3 weight enumerator independently checked for divisibility; the source code length p=3 is 225. Frozen tree SHA rederived from actual blobs.

## originality

PASS

The Liu–Liu–Yu Section 4 source enumerates weights and distances but does not state Euclidean hulls. A universal Gram-rank formula for linearized-polynomial image codes does not apply directly to this trace-quadric evaluation construction without a new Gram calculation. Exact 7/6 hull distinction remains best-of-knowledge distinct; it is an elementary but previously unrecorded structural invariant.

## value

PASS

The complete Euclidean hull identifies self-orthogonality and the effect of one punctured trace coordinate in a natural published code family. Hull dimension matters for duality and quantum-code constructions; no optimal quantum parameters are asserted. The p>3 proof is short, but determining exact hulls in an infinite family is a motivated invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
