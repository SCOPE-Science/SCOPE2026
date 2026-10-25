---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

For a cactus the cycle rank of an occupied edge set is exactly the number of fully included host cycles, yielding independent blocks with Bernoulli parameters r_e=v_e/(q+v_e) and a single all-ones penalty delta=1-q on each cycle. A direct expansion of E(F), E(H), E(FH) under this rank-one tilt gives Cov(F,H)= -delta rho (F(1)-E0F)(H(1)-E0H)/(1-delta rho)^2 for arbitrary increasing disjoint-support functions; both factors nonnegative. Positive fields preserve r_e form, positive-probability pins either remove a penalty or retain an all-ones penalty, and product-of-NA blocks remains NA. Forest restriction is the delta=1 non-full-cycle product. For cycles length >=3, diagonal polynomial P(z)=prod(1+z_i)-delta prod z_i vanishes with all z_i in upper half-plane by choosing (1+z)/z=delta^(1/m) exp(-2pi i/m), so strong Rayleigh fails for q<1 and forest; q=1 independent Bernoulli is stable. Independently checked an exact rational triangle at q=2/5 for nontrivial increasing functions on 2 vs 1 edges: covariance=-400/48387 matches rank-one prediction. Claims include positive-weight and degenerate bridge/disconnected cases; finite check is not universal proof.

## originality

PASS

Best-of-knowledge the full quantified final claim is not shown covered by the inspected primary statements, including aliases/stronger-theorem comparisons. The rank-one exact all-increasing-function covariance and closure under all fields/pins differs from pairwise negative correlation and wired branch connectivity. Broader graph classes support weaker assertions and therefore do not imply full cactus edge CNA+. An exact finite table is inapplicable to a theorem universally quantified over positive activities and arbitrary cactus size; database search alone is not novelty proof. Neither hypothesis-conclusion pair entails CNA+ for arbitrary disjoint edge subsets of cyclic finite cacti; our symbolic block proof supplies the missing strengthening. Inaccessible relevant full text is explicitly a residual risk; absence from a database alone is not novelty proof.

## value

PASS

Full edge CNA+ (all disjoint increasing observables under every positive tilt and positive-probability pinning) is much stronger than known pairwise covariance on arbitrary graphs; its exact heterogeneous cactus proof resolves a natural infinite graph class and exhibits a rigorous boundary between CNA+ and strongly Rayleigh. The non-real-stable witness and rank-one formula are reusable structural tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
