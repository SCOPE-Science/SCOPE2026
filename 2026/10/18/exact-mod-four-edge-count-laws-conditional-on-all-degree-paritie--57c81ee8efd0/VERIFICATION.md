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

Fix n>=3, fair independent edges of labeled K_n and feasible even-weight binary degree syndrome d. Its binary incidence matrix has rank n-1, so every parity fiber has 2^(M-n+1) graphs, M=C(n,2). Apply character expansion of 1_{Bx=d} and independent edge products to obtain Z=(1+i)^M/2^(M+1)*sum_{k=0}^n K_k(w;n)(-i)^{k(n-k)}, where K_k are coefficients of (1-t)^w(1+t)^(n-w). For even n, the k-phase takes only its even/odd constants; F(1)=F(-1)=0 for 0<w<n, while w=0 or n gives explicit nonzero endpoints. For odd n the trigonometric roots of unity and even w evaluate to the stated nonzero phase and magnitude. Symmetric difference with any fixed triangle on >=3 vertices preserves every degree parity but reverses parity of E, so conditional E[(-1)^E]=0; four-root inversion gives P(E≡a mod4|D=d)=[1+2 Re(i^(-a) Z)]/4 and uniformity iff Z=0. Independently enumerated all graphs on n=3,4,5,6 and verified all 4 residue counts and characteristic-function closed forms for every feasible syndrome, total 8+64+1024+32768=33864 graphs. The all-order argument uses exact algebra and the triangle involution, not exhaustive finite extrapolation.

## originality

PASS

The exact all-fiber conditional edge-count residue law was compared with degrees-congruence and partition results, plus generic graph-cycle-code weight enumerators. Fourier/MacWilliams methods as such are classical and not newly claimed; the exact K_n all-syndrome sign, vanishing criterion and uniformity exceptions require evaluation. No inspected primary theorem was found whose statement already classifies the same conditional all-degree-pattern mod-four law. Residual coverage risk of an older evaluated Ising/cycle-coset enumerator is genuine, so originality is best-of-knowledge.

## value

PASS

Degree parities are the natural F2 syndrome of a labeled graph, and the global edge count is an intrinsically interesting second statistic. The theorem proves a sharp exact conditional independence regime for every even graph size with nonconstant feasible parity syndrome, classifies all exceptional and odd-order cases, and evaluates finite-sample complex biases. Such a qualitative complete zero/nonzero boundary is not implied by marginal parity uniformity and is relevant to parity-constrained graph sampling and code-coset probabilities. The named object/invariant are motivated before calculation; the result is not a one-instance table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
