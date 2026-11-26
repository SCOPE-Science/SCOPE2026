---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At fixed valuation the odd part is balanced mod 4; f is also balanced separately on the even and odd cylinders. Parity splitting therefore gives C(h)=0 for odd h, and C(2q)=((−1)^q+C(q))/2. After translating to a close-pair endpoint, the triple has offsets divisible by 2^m. On shells of valuation below m the product is a fixed multiple of the same balanced odd-unit sign, hence integrates to zero. Rescale the remaining cylinder of mass 2^(−m) to offsets (0,d,h) with d odd and h even. The odd base point contributes zero, and the even base point leaves chi_4(d)/2 times the signed pair integral R(h/2). This is zero for an odd argument u and equals (C(u/2)−(−1)^(u/2))/2 for even u, giving all three valuation branches, including r=1 where the close-pair orientation is immaterial. Expanding the sign indicators recovers all eight probabilities. Haar inversion and f(−x)=−f(x) reverse the cubic and preserve the pair moments. Finite cylinder approximation identifies the Haar process with word frequencies. The stated frozen verifier checks 767 cases but its explanation of the error bound omits shifted residue 2^12: its sign is not determined mod 2^13 either. In the tested offset range every exceptional shifted argument is isolated, with the other factors fixed. Both exceptional types have conditional sign mean zero, so assigning zero to residue 0 contributes no error and the representative sign at 2^12 contributes at most 1/2^13 per offset. Thus the given error bounds still hold for these comparisons. The script's two cylinder assertions use the predictor; as an independent exact check I summed Haar cylinders for all 4005 triples (0,a,b) with −45<=a<b<=45 and a,b nonzero, and for lags 1 through 90. For each pattern I used depth 3 plus the maximum pairwise valuation, integrated high-valuation arguments by their zero conditional mean, and averaged the constant signs on the remaining residues. All matched the stated formulas and yielded +++ probabilities 3/16 and 1/8 for (0,1,4) and (0,3,4). The frozen verifier was inspected, not executed.

## originality

PASS

The distinct supported content is the evaluated cubic valuation law for all distinct integer triples of the regular-paperfolding sign process, together with its quantitative three-site orientation witness. The odd-part description and general correlation machinery are prior; the conversion from moments into cylinder probabilities is routine and is not counted as separate novelty. No equivalent of the exact evaluated law was found in the inspected sources.

## value

PASS

This is a complete evaluated three-site law of a natural stationary process, not a selected finite-lag coincidence. It identifies precisely which scale patterns produce zero or nonzero orientation information and gives a concrete cylinder statistic that distinguishes the reversed law even though all pair moments agree. The result is useful for comparing higher-order statistics of dyadic processes beyond their pair spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
