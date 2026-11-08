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

PASS: For prescribed output (s,Q) on (0,1)xR and 0<k<1, invert the affine belief update q=(Q-kp0-kp1 x)/(1-k); substituting into the logistic coordinate gives the equivalent scalar equation H(x)=L(s,Q), H=logit(x)-a beta x, beta=[1-k(1+cp1)]/(1-k). H tends to -infinity/+infinity at endpoints, giving surjectivity. H'(x)=1/[x(1-x)]-a beta, and det DF=(1-k)s(1-s)H'(x): beta<=0 or a beta<4 gives a smooth positive-orientation global inverse. At a beta=4, H increases strictly but derivative vanishes at x=1/2 and local Taylor coefficient 16/3 yields cubic inverse singularity. Above 4, two fold abscissae (1±sqrt(1-4/Lambda))/2 divide three monotonic intervals and yield exactly one, two or three inverse points depending on target level. The width W=Lambda*d-4atanh(d)~(Lambda-4)^(3/2)/3; at k=1 the inverse is separately smooth onto Q in (p0,p0+p1). The explicit a=6log3, c=500, k=2/5, p1=1/1000 three physical input witness has identical exact output and Jacobian signs +,-,+; independently recalculated q outputs, logits and signs. No claim that every supercritical parameter has a three-point physical fiber.

## originality

PASS

PASS, qualified: The actual motivating June 2026 model was read in author-posted full text, Sections 2–3 and bifurcation/equilibrium discussion. That paper introduces the same map and analyzes cycles, attractors, chaos and Cesaro convergence but the inspected material does not state a global inverse-fiber count or precise fold boundary. Earlier MWU game-chaos papers treat different systems, and known general fold/cusp theory is explicitly not claimed new. An unindexed conjugate classification remains possible.

## value

PASS

PASS: The model-specific exact global diffeomorphism boundary, cubic critical homeomorphism, sharp three-preimage opening law and in-rectangle exact witness distinguish one-step folding from complicated forward attractor dynamics. It supplies a precise structural theorem for a published nonlinear map rather than a routine Jacobian sign check, with essential global fiber and physical admissibility features.

The dated certificate retains the supplied scientific assessment, sources and limitations.
