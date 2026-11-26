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

In the phase quotient the Fourier real parts are 2a s_k²[delta-(1+delta)s_k²], s_k=sin(pi k/N). At delta_H only modes ±1 are critical, Re lambda_1 crosses with positive slope, and Im lambda_1=a tan(pi/N). I recomputed the cubic from the sine Taylor tensors in RESULT.md:49–58. Write zeta=exp(2pi i/N), d=zeta-1, P=zeta+1, c=a², h=1-2c, kappa=2c/h. Then rho_H b/a=-zeta/P², 2i omega_H-lambda_2=a d³, and C_(1,1,-1)=-a d³. The quotient removes the constant Fourier output of B_(1,-1); inserting the two remaining B terms gives G21/a=-d³-((1-c)/c)(d/zeta)(1+kappa zeta)[P+kappa(zeta²+1)]. Its real part reduces to 2(1-u)(1+2u)(h+u)/h²; all factors have the asserted signs. At N=6, q=1 this same expression gives 4-3 sqrt(3)i for G21. The Hopf radial balance with coefficient Re G21/2 gives the stated amplitude and its unstable-cycle/stable-equilibrium directions, and reconstruction by the common rotation gives a relative-periodic lift. All these statements are local or at onset as claimed. The supporting verification is finite corroboration, not the proof for all N and q; the uploaded script was not run in this review.

## originality

PASS

Credit existing circulant linear stability, including the threshold obtainable by substitution, and the standard Hopf coefficient formula. The compared primary statements do not give the weighted directed finite-ring nonlinear coefficient, its strict sector-wide sign, or the consequent local branch. The closest catalogue hit shares six twisted sites but concerns the sink threshold of a different discrete one-link system. The judgment is bounded by the compared sources, especially the inaccessible 2026 item.

## value

PASS

The linear loss of stability is not enough to distinguish a stable post-onset modulation from an unstable pre-onset relative-periodic branch. The exact cubic and its uniform sign settle that question for a natural minimal competing directed topology across all admissible windings and sizes; the amplitude law quantifies the nearby unstable branch in a fixed coordinate. This is a local bifurcation classification, not a global attractor or basin result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
