---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Under zero second-layer conditioning the first-layer retained configurations are independent sets with activity λ=p/(1−p), so each branch cavity ratio follows f(r)=λ/(1+r)^d for d forward descendants. There is a unique fixed point r*, but at dr*/(1+r*)=1 the antitone map acquires distinct two-cycle limits for λ>λc=d^d/(d−1)^(d+1); at/below λc they coincide by the standard hard-core tree uniqueness theorem. With the occupied exterior of the two-layer source, an outer forced-vacant shell gives cavity start r0=0. For root-empty/all-q-neighbor-occupied cylinder, the conditional probability Pq(r)=r^q/((1+r)^q+λ), q=d+1, is strictly increasing for r>0. The parity limits differ above λc, and the exact second-layer conditional ratio transfer is provided by the source Lemma1 with uniformly positive denominator from its Remark2, establishing non-quasilocality there. An independent rational threshold identity check for d=2..8 and numerical two-cycle check confirmed the transition example (d2,p_c=4/5), but the infinite-volume conclusion follows from the analytic recursion+source lemma rather than numerical iterations. The boundary/lower statement is only absence of THIS parity witness, not Gibbsian uniqueness for all observations.

## originality

PASS

Henning–Külske–Schubert arXiv:2304.03102v2 studies exactly this transformation and proves non-Gibbsianness for sufficiently large p with unspecified degree-dependent threshold via an inhomogeneous-tree cutset argument. The exact hard-core uniqueness activity on regular rooted trees is standard, but its theorem alone says nothing about the two-layer image measure. The new statement specializes the conditional ratio transfer to homogeneous cavity recursions and obtains an explicit sharp onset for a specified all-zero witness. The claims are not the full Gibbs boundary and do not assert known hard-core critical activity itself is original. Resultary and alias/formula searches found no equivalent combined theorem; risk of an implicit corollary in weakly indexed notes retained.

## value

PASS

The exact onset of a physically motivated hidden-phase witness improves an unspecified sufficiently-large-density non-Gibbs region to a sharp computable threshold in the canonical regular-tree case. The sharpness includes both parity phases and equality onset, and distinguishes that witness from the unknown global Gibbs/non-Gibbs phase boundary. This is a meaningful boundary refinement, not merely restating the hard-core critical activity without its conditional-probability consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
