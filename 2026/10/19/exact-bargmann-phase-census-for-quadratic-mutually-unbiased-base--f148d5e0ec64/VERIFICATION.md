---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With the first slot conjugate-linear, completing the square in the finite-basis inner product gives the factor γ_q χ_q(c−a)ψ(−(j−i)²/[4(c−a)]). In the product for three finite slopes, the third difference is −(A+B); the character product is χ_q(−K), so the prefactor reduces to γ_q χ_q(K) and the exponent to −[B(j−i)−A(k−j)]²/(4K). In the computational case one cyclically moves that basis first, giving the stated square −A[h+(k−j)/(2A)]² and prefactor γ_q χ_q(A). Both square parameters are surjective linear functions of three labels, with q² preimages each. Nonzero square parameters give γ_q³ χ_q(z)ψ(z), and multiplying slopes by a nonsquare flips the square class for both types of triples. Thus the two zero-parameter signs each have B_q q²/2 preimages and each fixed nonzero z has B_q q² preimages globally. Fourier expansion of the trace condition gives S(t)=(γ_q√q/p) Σ_{u≠0 in F_p} χ_q(u)ζ_p^(−ut). Restriction to F_p is trivial at even r and χ_p at odd r; the latter Gauss sum supplies χ_p(−t)γ_p√p at nonzero t. This gives the stated signs and multiplicities and their total. The signs label distinct phases because −1 is not a p-th root for odd p. The prime trace is the identity; in extension degree at least two the nonzero-t character imbalance is smaller than fiber size, and the zero-parameter contribution ensures both t=0 signs. Gram minors give the cubic; at q=3 the phases ±i alone are singular, yielding 216 ordered cases and roots 0,1,2. At q≥5 the Gershgorin lower bound 1−2/√q is positive.

## originality

PASS

The supported distinction is the global sign/trace multiplicity law for odd extension fields, including full phase support in degree at least two. The prime-field census is exactly reproduced by a separate, later-dated indexed record, and the q=3 numerical counts have a published small-dimensional counterpart. Those special cases, the phase invariant itself and the general Gram expansion do not independently carry the originality assessment.

## value

PASS

Pairwise unbiasedness fixes magnitudes only. The exact distribution of the natural third-order, phase-gauge-invariant statistic supplies a dimension-wide comparison for these canonical bases. The distinction between a prime field and its extensions is substantive: traces combine different field elements with different quadratic signs, changing both multiplicities and support, and the distribution also determines the corresponding three-vector Gram spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
