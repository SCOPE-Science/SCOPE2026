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

Appending symbol i replaces the whole set of i-ending strings by the injective image of all old strings, including the empty one, since any old i-ending string can use the new i as its last symbol. The other ending class stays unchanged. The resulting shifted two-coordinate state gives s+t−2, counting strings rather than embeddings. With the stated reverse product convention, complementation is conjugation by P and doubling gives A_next=(PA)^2. Since det A=1 and det P=−1, the squared trace is t²+2. Also P A_next=A P A, whose trace is tr(P A²) by cyclicity; Cayley–Hamilton and tr P=0 give st. Nonempty seeds, including monochromatic ones, have s>=2 and t>=1. The scalar logarithmic recurrence implies z_next=2z+epsilon for z_m=log(t_m)+log(t_(m+1)), and the normalized log t recurrence is a contraction with coefficient −1/2. The parity ratios for s_m/t_m have summable log increments since t doubles at least, so log N_m−log t_m=O(1). The tail bound follows by epsilon<=2/t² and geometric ratio 1/8, with the coefficient 8/21. Independent matrix/string replay covered four stages for 126 seeds; direct sets through m=5 of the seed 0 and a separate last-occurrence count at m=6 reproduce all seven stated values. A 100-digit series replay through j=6 gives h(0)=0.4502248047496114629262541073… and exp(h(0))=1.56866478915034433761643869…, with series truncation error below 2.712e−53.

## originality

PASS

The ordinary distinct-subsequence update is established background, as is the complement-morphism setting. The supported distinctive part is exact two-scalar closure for an arbitrary seed and the resulting convergent rate formula with a quantitative error, not the ordinary recurrence or a new notion of Thue–Morse complexity. The strongest inspected indexed matrix recurrence counts absent strings, and the strongest rate analogue uses different host words; neither supplies the claimed result.

## value

PASS

Thue–Morse and its arbitrary-seed complement-doubling analogues are natural nonperiodic hosts. The exact count no longer requires storing or traversing the exponentially long doubled host once the two seed integers are computed. The same reduced state yields a per-symbol growth constant with a rigorously bounded series error; these structural and asymptotic uses, not the numerical illustration alone, make the result worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
