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

Reconstructed the continuous-time generator with transient states (1,+),(2,+),(1,-),(2,-), absorbing 0 and 3. Its backward matrix is A=[[1+x+e,-1,-e,0],[-y,1+y+M,0,-M],[-M,0,1+y+M,-1],[0,-e,-x,1+x+e]], with right-hand side (0,1,0,1). Since every row is strictly diagonally dominant with positive diagonal and nonpositive off-diagonal entries, A is a nonsingular M-matrix; det(A)>0 for x,y,e,M>0. Independent symbolic adjugate computation verified as an identically zero rational function the difference u-1/(1+x+xy) -(y-x)[xM^2+(xy-e)M-e(e+1)(y+1)]/[(1+x+xy)det(A)]. The better fixed + environment has probability 1/(1+x+xy), the - environment 1/(1+y+xy). Because 0<x<y and det(A)>0, the sign equivalence follows; the threshold polynomial has positive leading coefficient and strictly negative constant, hence exactly one positive root, equal to the displayed M_*. For N=2 with arbitrary nonnegative switching rates alpha (+->-) and beta (- -> +), the differences from 1/(1+x) are alpha(x-y)/[(1+x)D2] and (x-y)(alpha+x+1)/[(1+x)D2], where D2=alpha*y+alpha+beta*x+beta+xy+x+y+1>0; so neither initial environment improves on the better frozen state. Independent exact rational elimination confirms u=181/1373, fixed values 1/9 and 1/10, and F=6464/25 for x=2,y=3,e=1/10,M=10; 60 independent rational-grid generator solves confirmed the sign criterion. The M->infinity limit u->1/(1+x+x^2) additionally explains the feedback advantage for x<y. These computations corroborate the algebraic proof and do not establish generality by finite testing. Boundaries x=y, zero/negative rates, arbitrary starting environments, N>3 and different rate families are not covered.

## originality

PASS

Best-of-knowledge PASS, qualified. The closest published exact fixation models assume environmental switching independent of mutant count; this claim treats a generator in which the switch rate depends on the count i and derives a sharp all-parameter inequality and minimum population-size cutoff in a specifically normalized family. Ashcroft–Altrock–Galla 2014 already establish generic fluctuating-environment advantages and backward recurrences, so those phenomena or methods are not claimed new. Baron–Galla 2018 explicitly name composition-dependent switching rates as a possible extension. Wienand–Frey–Mobilia 2017 use an externally switching carrying capacity and a different variable-size population model. No same threshold or universal implication was established in the inspected primary text or targeted Resultary results. The exact generator calculation and cutoff appear new at this bounded level, but generic CTMC linear algebra, uncatalogued feedback models and unindexed literature are residual priority risks.

## value

PASS

The finding addresses a motivated mathematical question in finite-population stochastic evolution: what is the smallest number of individuals at which an environment that reacts to mutant composition can strictly outperform either constituent frozen environment, and at what switching-rate threshold? For N=2 there is only one transient mutant count and no separate stage for feedback to exploit; N=3 is the first nontrivial state-space with two distinct count-conditioned decisions. The theorem proves this sharp cutoff and a necessary-and-sufficient four-parameter threshold, not just an example, and exhibits selection-disfavored mutants in both environments still benefiting from feedback. Baron & Galla 2018 explicitly suggest composition-dependent environment rates as a future modeling extension. Although the proof is finite-state algebra and the model is stylized, the exact benchmark is a natural structural boundary a later researcher comparing feedback rules could use; it is not merely a known table entry, restated theorem, or arbitrary normalization test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
