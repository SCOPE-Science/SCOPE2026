---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For Im z>0, θ(t)=arg(z+t) is continuous and strictly decreasing, and (z+t)^(-2) has argument spread 2[θ(a)-θ(b)]. The signed inner product Re[(z+a) conjugate(z+b)] = (x+a)(x+b)+y² = |z+(a+b)/2|²-(b-a)²/4. Outside the diameter disk this is positive, so θ(a)-θ(b)<π/2 and the squared inverse kernels all lie in a common open half-plane after rotation: positive μ cannot cancel. Real z off [-b,-a] gives positive kernels and lower Im follows by conjugation. For any nonreal z in disk, θ(a)-θ(b)>=π/2; by IVT there exists t*∈[a,b] with θ(a)-θ(t*)=π/2. Setting masses |z+a|² at a and |z+t*|² at t* produces two unit kernel phases differing by π and exact cancellation. Verified both boundary z=(-1+i)/2 for δ0+δ1 and interior z=-1/2+i/4 for 4δ0+δ_(5/8) using fresh exact algebra. No finite sample is a substitute for the angular proof.

## originality

PASS

Karp–Prilepkina 2012 develop generalized Stieltjes functions and broad sectorial mapping estimates; their inspected complex-variable analysis does not state the sharp support-interval disk or converse two-atom realization. Love–Byrne 1980 concerns inversion, with only bibliographic-level material accessible, so whole-document noncoverage is not claimed. Searched aliases involving derivatives of Cauchy/Stieltjes transforms and zeros of rational resolvent mixtures; no decisive dominating localization theorem identified. Best-of-knowledge with classical-literature risk.

## value

PASS

The support diameter is the most natural intrinsic scale for a positive Stieltjes mixture, and the exact disk gives an optimal parameter-free zero region for the derivative of a Stieltjes/Cauchy transform. The converse realization at every nonreal point with only two atoms distinguishes it from a routine sufficient half-plane criterion and makes it a reusable sharp extremal localization fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
