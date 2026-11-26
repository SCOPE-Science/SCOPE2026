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

The two indicated branch maps have the given signed monomial derivatives. Independently of the cited coding theorem, both closed inverse branches map the box to itself. In normalized coordinates y1=(x1+1)/2 and yi=xi otherwise, the left inverse halves slot 1; the right inverse shifts backward, with slot 2 to slot 1 taking t to (1+t)/2 and slot 1 to slot M taking t to 1-t. If a word has k>0 right symbols, repeating its inverse ℓ=M/gcd(M,k) times makes each coordinate traverse the entire cyclic list of slots q=k/gcd(M,k) times, hence contracts every direction. The inverse product has a unique fixed point. In its periodically repeated inverse itinerary a boundary value cannot stay on the boundary: to enter slot 1 from slot 2 while remaining on the boundary it must enter at value 1; the next left inverse in slot 1 makes it interior, or the next right inverse sends it to slot M at 0 and the following entry into slot 1 makes it interior. Once interior it remains interior. Thus the closed-branch construction does not yield spurious itineraries at a switch, and different positioned words give different points. Forward each cycle of the return coordinate permutation wraps exactly q times, giving (-2)^q. A left step in gap j doubles a coordinate in cycle class j mod g, up to relabeling, so the only additional exponent is b_r, the gap sum. Any composition is attainable by putting each part in the first corresponding gap. Cycle factors with distinct b have distinct root moduli, so only permutations of a tuple can identify spectra. There are q+1 gaps of residue 0, and q for every other residue, giving the stated multiplicities by stars and bars, including q=1 and N=0. The contrast is 2^((max b-min b)/ℓ); concentrated and balanced compositions respectively give the attained extrema, while g=1 forces contrast 1.

## originality

PASS

The coordinate-cycle factorization and much of the real/nonreal type classification are already known. Credit is confined to the fixed-twist attainable exponent profiles, exact multiplicities of the spectra, and resulting sharp contrasts. The available strongest pre-dated result does not classify how the left-step weights are distributed among cycles.

## value

PASS

The map is a natural example of periodic instability. Conditioning on twist count controls the coordinate permutation but not the expansion accumulated by each cycle. The classification resolves exactly which expansion profiles are possible at those fixed permutation data and how often they occur, information lost in the known real/nonreal dichotomy even for spectra of identical type. This is a complete spectral census with realizable extrema, not just a rephrasing of the monomial factorization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
