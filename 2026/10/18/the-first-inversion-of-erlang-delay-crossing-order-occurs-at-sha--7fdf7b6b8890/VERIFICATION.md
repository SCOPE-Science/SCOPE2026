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

At s=iω>0 imaginary, reality of the Erlang transform forces m arctan(τω/m)=kπ with 1≤k<m/2; the real part then gives exactly the stated ω_k and τ_k. For the implicit derivative denominator 2iω+bτQ with Q=(1+iτω/m)^(-m−1), Re Q=(−1)^k cos^(m+2)(kπ/m) is nonzero. The real derivative has numerator −2bω² Re Q over the squared modulus, giving simplicity and the claimed signs. At zero delay the two finite roots have derivative −b/2. For the other roots, w=τs/m gives the limiting polynomial m²w²(1+w)^m with m roots approaching w=−1, thus safely in the left half-plane. No zero root occurs and the polynomial has fixed degree at all finite positive delays. Odd-to-even order is strict immediately; for even-to-odd order the sign changes exactly at the stated ratio obtained by cross-multiplication of positive squared delays. Independent rational interval enumeration certified all 66 earlier even-index comparisons strictly above one, verified the frozen decimal bounds on ρ_28,2, verified ρ_28,2<999/1000 and proved all other admissible even-index thresholds at 28 above one. To check that the adjacent inversion gives precisely the stated total order, the odd subsequence increases with k. The even subsequence also increases: set x=tan²(kπ/m) and p=m/2; the derivative numerator for x/[1−r(1+x)^(-p)] is 1−r[1+(p+1)x]/(1+x)^(p+1)≥1−r>0 by Bernoulli's inequality. Therefore the only swap is 2,3, and signed transverse crossings give counts 0,2,4,2,0. At equality ω₂²<a<ω₃², so the ties are distinct pairs, not repeated roots. The primary equations give a₂=4, b₂=2κ at z*=0 with I*=3/2, consistent with the example's coupling and input.

## originality

PASS

The scalar model, general phase criterion, related alternation and some lower-shape stability facts are not credited as new. The exact integer-shape cutoff for chronological inversion over the full open coupling range, and its first distinct-pair boundary, are not supplied by the inspected passages or closest catalogue record.

## value

PASS

An alternating phase crossing list can mislead a stability count if it is used as a chronological list. The result determines exactly until which Erlang shape that shortcut is valid for every admissible coupling and identifies its first failure and simultaneous two-frequency boundary. The four-unstable-root interval is a substantive difference in the linearized spectrum of an existing model, even if the first inversion occurs only near b/a=1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
