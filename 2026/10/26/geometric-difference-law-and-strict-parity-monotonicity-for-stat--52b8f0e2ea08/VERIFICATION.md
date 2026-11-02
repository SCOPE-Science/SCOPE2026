---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The Gnedin–Olshanski Theorem 5.1 exact normalized double sum has terms (1-q)(q;q)_infty q^(rs+r+s)/((q;q)_r(q;q)_s). In the annulus q<|z|<q^-1, absolute convergence permits summing s first by Euler q-binomial and then r by the general q-binomial identity, obtaining (q;q)_infty^2/[(qz;q)_infty(q/z;q)_infty]. Each factor is the product of generating functions of independent geometric(q^k) variables, and their total expectations sum to a finite value, proving X-Xprime law. At z=-1 the parity difference is a convergent strictly positive product. Log differentiation on compact q-subintervals gives -4 Σ_{k>=1} k q^(k-1)/(1-q^(2k))<0, proving strict monotonicity and endpoints. Independent double-sum/product diagnostics at four q values agree to 1e-8. Those are corroborative; the q-binomial evaluation establishes the infinite law.

## originality

PASS

Gnedin–Olshanski 2011 proves the exact one-point double-sum distribution, and this is explicitly an exact transform of that known marginal. He–Müller–Verstraaten 2022/2023 Section 10 explicitly leaves c_o>1/2>c_e for Q>1 as an open problem; this product gives its strict global solution and additionally monotonicity. The paper does NOT explicitly pose monotonicity as a second separate open problem, despite that wording in the assigned result; that attribution overstates the source, while both mathematical monotonicity and the explicitly posed parity inequality remain established. Bufetov–Chen 2024 uses a different nonergodic mixture measure.

## value

PASS

The exact independent-geometric difference representation is a natural structural law for stationary single-site Mallows displacement and directly resolves a published open parity inequality. The strict monotonicity supplies additional global information, not just a computational reformulation of isolated values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
