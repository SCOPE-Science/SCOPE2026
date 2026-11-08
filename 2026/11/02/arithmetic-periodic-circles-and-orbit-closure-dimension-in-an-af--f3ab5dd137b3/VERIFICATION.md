---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The integer unimodular transformation (u,v)=(x−2y,y) conjugates F to (u+delta,4v+u+f), with exact nth iterate (u+n delta,4^n v+H_n(u+f)+W_n delta), H_n=(4^n−1)/3, W_n=(4^n−1−3n)/9 an integer. The rational-base return condition is precisely q|n; fixed-point character H_n u+(4^n−1)v+constant=0 has gcd(H_n,4^n−1)=H_n parallel connected kernel circles. Their common direction makes any smaller-period fixed component either entire or disjoint, so Möbius inversion yields exact primitive-period component counts. Fourier frequencies map (a,b) to (a+b,4b) under Koopman, forcing all L2 eigenfunctions to have b=0 and giving the claimed ergodicity/eigenvalue conclusions; irrational base ergodicity plus full-support Haar yields generic density, rational base gives q expanding-fiber circles. Independent exact-fraction iteration checks and Möbius arithmetic tested q=1,2,3,5 and several translation examples; not a substitute for all-parameter proof.

## originality

PASS

Wang--Ding 2018 introduced this exact integer-matrix model and e,f forcing, discussing fixed points, Lyapunov exponents and hidden attractors, but did not derive all-translation periodic-circle topology, arithmetic primitive-period component counts, Haar point spectrum or orbit-closure phase transition. General finite rational-grid toral orbit counting and linear unshifted period sets concern different objects; standard rotation/expanding-map facts are credited as ingredients. A general affine neutral-expanding torus theorem could imply the combined classification, and this is retained as residual risk.

## value

PASS

Provides an exact mathematical dynamical classification of a published matrix map, rigorously separating an irrational all-torus Haar-ergodic regime from rational families with finitely many typical closure circles and exponentially many primitive-period connected components. The precise 349525-versus-ten numerical contrast corrects what Lyapunov/phase plots alone cannot establish. The all-translation result is more than a routine single-parameter computation, while broad rotation and expanding map ingredients are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
