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

For the stated Fourier convention the multiplier uses a minus sign in the exponent, which does not change the vanishing criterion (replace the odd primitive exponent by its negative). At order 2^r division of the rational residue polynomial by z^{2^{r−1}}+1 gives the opposite-mass differences, all of which must vanish. The positive constant-frequency multiplier is nonzero. Independently consider the highest vanishing level r. Each occupied opposite pair consumes at least two sites. With just one pair, reduction at every lower level collapses all mass to one site, which cannot cancel. With two pairs, each consists of two sites of the same weight; lower cancellation then requires equal magnitudes for the two resulting phasors, so the weights on both pairs coincide. If equal, opposition of the two projected pair classes can occur only at the level determined by the 2-adic valuation of their difference. This proves all shell-count bounds. Attaining N/2 with unequal weights forces the order-N shell, and the distinct sites must be two antipodal, separately matched pairs. The equal maximum requires both order N and order N/2, exactly an order-four coset. For a specified r, two same-weight pairs spaced by 2^{r−1} with distinct pair weights give the desired shell; use starts 0 and 2^r for r<k and 0 and 1 for r=k, so all four sites remain distinct. Powers 1,2,4,8 admit no equal disjoint nonempty subset sums and give nullity zero. In the real example the cubic factors as (z+1)(z²+√2 z+1); on eighth roots the zeros are −1 and exp(±3πi/4), exactly the listed classes with orders N/4 and N.

## originality

PASS

The shell criterion is classical and the equal-weight classification is covered. The distinct contribution supported by comparison is the cross-conductor rigidity for four positive rational taps with unequal weights, its weighted sharp classification, and the explicit irrational boundary example. No covering statement for this contribution was identified in the inspected sources.

## value

PASS

The support-four constraint gives an exact rank-defect classification for sparse positive rational circulants beyond a local zero test: one can tell that no other dyadic scale contributes, characterize the sharp weighted configurations, and realize the entire defect spectrum. The positive irrational example isolates failure of this conductor phenomenon without introducing negative weights; it is a meaningful coefficient-field boundary. Value does not rest on the known equal-weight case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
