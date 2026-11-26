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

Every m-plane is the common kernel and image of exactly |GL_m| possible factors. Nontransverse kernels give a nonzero common annihilated vector; for complementary kernels the two restrictions are independent uniform isomorphisms A,B and C=diag(AB,-BA). Complements are graphs of q^(m^2) maps; AB is uniform and BA conjugate to it. The signed direct sum is cyclic exactly when T is cyclic and its opposite characteristic polynomial is coprime to its own. In characteristic two the doubled module is never cyclic. For odd q, the primary centralizer of a single phi^k block has q^(d(k-1))(q^d-1) units, giving the local orbit factors and formal coefficient law. An independent analytic simplification avoids the full cycle index: multiply H by the polynomial zeta product over phi!=t of [1-(z/q)^deg(phi)] = (1-z)/(1-z/q). This yields (1-z)H as (1-z/q) times the paired factors with [1-(z/q)^d]^2 and the self-opposite factors [1-(z/q)^d]. The paired factors have first-order residual coefficient 2/[q^d(q^d-1)] in z^d and quadratic remainder O((|z|/q)^(2d)); self-opposites are g(t^2) with count at most q^(d/2). Normal convergence on every closed disk of radius smaller than sqrt(q) gives the exponential coefficient tail. At z=1 the normalized paired factors are 1+q^(-2d). Writing A,B for the paired and self-opposite half-degree Euler products, even-polynomial factorization gives AB=Z=(1-v)/(1-qv); irreducible g(t^2) is equivalent to the norm of a root of g being nonsquare. The quadratic-character Euler product is 1 because each positive degree has equal signed constant-term counts; its nonsquare factors give B(v)^2/B(v^2)=Z(v). Thus A(v)/(A(v^2)B(v))=1/Z(v^2). At v=q^-2 this gives the stated kappa after the prefactor 1-q^-1; the Gaussian-binomial complement fraction tends to Phi_q. Independent bounded GF(9) enumeration (arithmetic in F_3[i]/(i^2+1)) gave 5104/5760=319/360 at m=2, using the equivalent invertible 2x2 test of nonscalar and nonzero trace. Inspected the frozen checker and recorded output, not executing it; its finite prime-field tests do not prove the asymptotic or the extension-field result.

## originality

PASS

The transverse normal form and counting theorem in Resultary already supply the invertible-commutator block law as a corollary; do not credit this reduction or the classical GL cycle index as novel in isolation. The supported distinct contribution is the signed cyclicity law, especially the explicit rational limiting constant for that event. The closest earlier generation statistic detects cyclic T without testing signed coprimality, and ordinary cyclic or regular semisimple GL results do not give this law.

## value

PASS

This computes a natural, finer random-matrix invariant of a structured bracket ensemble. The signed exclusion is essential, and the closed constant shows exactly how characteristic and opposite primary collisions modify ordinary GL cyclicity; exponentially fast convergence makes the fixed-field distinction quantitative. This value rests on the odd-field signed law, not on reproducing the already available transverse normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
