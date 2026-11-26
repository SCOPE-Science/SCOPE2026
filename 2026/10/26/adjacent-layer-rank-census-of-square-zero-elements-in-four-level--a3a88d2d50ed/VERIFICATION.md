---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Block multiplication leaves exactly AB=0, BC=0 and AE+DC=0, so the outer block F is free. For each rank-t B, A factors through the (b-t)-dimensional quotient by im B, and C has range in the (c-t)-dimensional ker B. Choosing the image of each rank-j map and then a surjection onto it gives the stated Gaussian-binomial rank count. To check the less immediate completion factor, send a map H from the fourth to the first layer to its restriction to ker C followed by projection modulo im A. This restriction/projection map is onto by choosing complements. Its kernel is exactly the possible AE+DC: first extend the im A-valued restriction on ker C to a map with range in im A and lift that through A; the remainder vanishes on ker C and factors through C, then extends from im C. The coupling image thus has dimension ad-(a-r)(d-s)=rd+as-rs. Its kernel in the (D,E) variables, together with free F, has dimension ad+bd+ac-rd-as+rs and gives the exact power of q. This argument includes zero ranks and characteristic two. In the scalar case B nonzero forces A=C=0, while B=0 gives one independent completion constraint exactly when A or C is nonzero, confirming the displayed small polynomial. The submitted checker and its verification notes were inspected, not executed; the general count is established by the linear argument.

## originality

PASS

The distinct claim is the explicit factored coefficient, in particular the uniform completion factor for any compatible triple with prescribed adjacent ranks. It is not the first way to obtain the census: Melnikov's weighted involution orbits already give an exact, generally much larger orbit sum for the same polynomial. The inspected sources do not give the evaluation of each such coefficient as three ordinary rank counts times one power of q. The new factorization uses the overlap in the two completion terms, not just a relabeling of orbit or Jordan data.

## value

PASS

The adjacent ranks distinguish natural consecutive-layer quotient maps that ambient Jordan and prefix-tableau counts merge. Four levels introduce the first completion constraint coupling two nonadjacent blocks. The exact fiber dimension identifies its overlap term and gives each profile coefficient with a fixed number of rank factors rather than a sum over individual involutions. This structural simplification is useful across all sizes and finite fields, without needing to claim a first census or an orbit classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
