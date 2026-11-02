---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For every integer n>=3 and threshold-one synchronous 3-state Greenberg–Hastings dynamics on C_n square K2, apply Gravner–Lyu–Sivakoff finite-graph Theorem 3: extinction iff the integer edge 1-form g(a,b)=1_(a,b)=(0,1)-1_(a,b)=(1,0) has zero cycle circulation. n square faces plus one rim generate the integer cycle lattice (rank n+1). Build the 9-state rung Laurent matrix from zero square curl, impose one independent upper-rim winding by [z^0]tr M(z)^n. Direct symbolic 9x9 computation independently confirms det(xI-M(1))=(x-2)^3(x+1)^4(x²-7x+4) and second log-weight derivative -2(x-2)(x+1)^2(3x³+21x-16), giving lambda=(7+sqrt33)/2 and sigma²>0. A zero-weight self loop and weight-one allowed 3-cycle show unique Fourier maximal phase, eliminating other saddle contributions and proving Gaussian local limit n^-1/2 with one winding constraint. Independent Laurent dynamic programming yields E_3=261,E_4=1485,E_5=8409,E_6=49215. Finite checks do not prove all-n asymptotics; primitive PF perturbation and Fourier steepest descent do.

## originality

PASS

Best-of-knowledge mathematical comparison of the same object, definitions, parameter quantifiers, and implication strength. Foundation and partial coverage are credited explicitly; neither failed searches nor inaccessible full literature alone are represented as novelty proof. The general iff criterion is fully credited. Extinction-count enumeration for the prism is not synonymous with the ability to decide extinction of one state. Prior irrotational theorem proves the conceptual premise, not the exact count and Gaussian prefactor. Claim does not purport to rediscover that premise.

## value

PASS

The general irrotational extinction criterion is known, but extracting exact extinction counts for all prism circumferences and the nontrivial Gaussian winding penalty addresses a natural sparse periodic graph family. The algebraic Perron growth constant and n^-1/2 subexponential correction distinguish local face constraints from the one global homology cycle, useful for finite excitable-media census and statistical mechanics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
