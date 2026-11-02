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

The n-state GF(2) XNFA is a linear representation λM_wγ, and its square-root series has Hankel kernel K_m(X,Y)=e0ᵀ(XY)²e_m after splitting endpoints by λγ∈{0,1}. Expanding gives Σ_{q,p,r}X_{0p}X_{qr}Y_{pq}Y_{rm}. Square-free monomials in matrix coordinates are independent Boolean functions. For m=0, q=0 has n surviving diagonal monomials because pairs cancel in characteristic two, while q≠0 each contributes rank n². For m=1, the q=0 and q=1 blocks each contribute n(n+1)/2 and the remaining n−2 blocks contribute n². Off-block variable supports separate, hence both cases have full matrix-monoid rank n³−n²+n. Restricting to word transformations proves the upper bound via residual Hankel span. The cyclic permutation, elementary transvection and rank-(n−1) projection generate all binary n×n matrices: adjacent row transvections and commutators yield GL_n(F2), whose left/right products with diagonal corank-one projections yield every rank. The ternary source is reachable/observable with ordinary rank n, giving a sharp lower bound with n essential states. In n=1 the bound is 1 even if endpoints vanish. An explicit independent binary-alphabet 6×6 minor realizes rank6 at n=2. Independent fresh checker built on a distinct tuple representation reproduces exact square-free monomial ranks for n=1..8, full 2^(n²) matrix-kernel ranks at n=2,3 (both endpoint cases), ternary monoid closures of 16 and 512 elements, and 6×6 minor rank. These are finite checks only; the all-n result rests on the source symbolic proof.

## originality

PASS

Best-of-knowledge exact characteristic-two state-complexity formula for word-duplication inverse in XNFA. Prior sharp ordinary NFA n^3 concerns existential paths, and prior deterministic complexity concerns a different model. General GF(2)-weighted automata minimization and parity decision algorithms do not mathematically imply the submitted square-free monomial rank. Three actual Resultary queries and targeted literature searches did not return equivalent theorems. The XNFA paper is only partially inspected; unindexed rational-series literature might contain an equivalent calculation, and failed indexing is not proof of novelty.

## value

PASS

Determining exact worst-case state complexity for the natural operation L↦{w:ww∈L} for an entire arithmetic automaton model is a motivated structural result rather than a finite slice. Characteristic-two monomial cancellations explain the nontrivial saving n(n−1) from the ordinary NFA n³ bound. A uniform three-letter sharp construction and a distinct binary two-state witness make the result robust under small fixed alphabets. The full matrix-monoid Hankel calculation is independently useful for GF(2) weighted language transforms, and the input source is shown to have exactly n essential states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
