---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For F_h(u)=u-h(I+11^T)sin u and h<1, subtracting coordinates of an inverse of a diagonal target reduces to q_h(ui)=q_h(uj) modulo 2pi; q_h(v)=v-h sin v is a degree-one circle diffeomorphism, forcing all coordinates equal. Thus all backward ancestors reduce to f_c(u)=u-c sin u, c=(d+1)h. For 1<c<2, its critical points ±acos(1/c) give a three-branch window |t|<a_c=sqrt(c²-1)-acos(1/c), and each outer branch is one-to-one forever. Target zero generates ± one new outer ancestor per level, N_n(0)=2n+1. Nonzero central inverse grows in magnitude at least by (c-1)^(-1), so eventually exits; Taylor expansion of f_c near zero plus summable O(u_j²) distortion yields 2 log(1/|t|)/log(1/(c-1))+O_c(1) eventual count. Independent numerical bracketing gave N_n(0)=1,3,5,7,9,11 for c=1.2,1.5,1.9 at n=0..5 and finite stabilization for off-zero examples; numerical tolerance cannot certify the asymptotic.

## originality

PASS

The known Huygens paper gives a sharp invertibility/Morse–Smale threshold, while the submitted supercritical diagonal-target inverse-fiber classification addresses a different problem. Only its abstract and bibliographic links were accessible this run; an authorized full-text attempt was blocked by VPN. Thus priority is a qualified best-of-knowledge PASS, with explicit primary-text gap, not a claim that the whole paper lacks the result.

## value

PASS

Counts of all global torus preimages just past a known invertibility transition quantify precisely how inverse fibers proliferate and why a sink has linear rather than exponential ancestor growth. The exact logarithmic boundary layer is a natural dynamical invariant tied to the derivative magnitude c-1, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
