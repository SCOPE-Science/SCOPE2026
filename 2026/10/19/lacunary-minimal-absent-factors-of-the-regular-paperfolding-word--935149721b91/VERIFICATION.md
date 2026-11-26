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

The recurrence agrees with the odd-part definition and ensures late recurrence by shifts divisible by 4 times the largest power of two occurring in the positive indices of a given occurrence. For a word aub, minimal absence is equivalent to occurrence of both au and ub but not aub. Late recurrence ensures that a singleton one-sided extension cannot give a missing product pair, leaving only bispecial inner words. Neither alternating length-four pattern occurs because its local track of consecutive even-indexed symbols would be constant. Hence an occurrence of a factor of length at least eight at both parities would give the same track strictly alternating and a factor of length at least four with no alternating four-window. For a long odd-start factor the preceding even-indexed bit is forced; for a long even-start factor of even length the following even-indexed bit is forced. Thus long bispecials have odd length and even starting index. The lift from length m≥8 to 2m+1 is injective by recovery from odd coordinates; unique occurrence parity of the shorter factor fixes the alternation of the even coordinates. The flanking letters are exactly those of the shorter factor, so the entire extension relation is preserved; every longer bispecial arises this way when the reduced length is at least eight. Independent enumeration confirms the base profiles at inner lengths 7–16, the four specified length-nine words, and selected larger counts. Allouche's p(r)=4r theorem certifies the base sets. Independently, using positive indices and K=32, in any base window of length at most 18 the symbols at nonmultiples of K are determined modulo 2K and there is at most one multiple of K. If the window contains a multiple qK, move it to q'K where q' is 1 or 3 for odd q, or 2 or 6 for even q, choosing the same odd-part residue modulo 4. This reproduces the exceptional bit and all other bits in the first 223 positions. If no multiple occurs, move the start to 1 through 2K. Thus the 256-symbol prefix also suffices without invoking the complexity theorem. The base and odd-length lift give exactly inner lengths 2^j−1, with two strong and two weak bispecials, each weak one missing two pairs. Adding the two flanking letters gives the stated spectrum and inclusive cumulative count for N≥9.

## originality

PASS

Ordinary complexity and unique starting parity of long paperfolding factors are known. The supported distinct result is the stronger two-sided extension profile that gives the exact long minimal-forbidden spectrum for the specified regular fold. The closest inspected cyclic-complexity paper concerns a different equivalence of factors, and the closest catalogue result concerns the longest absent factors of finite dyadic prefixes. Neither establishes the reviewed exact infinite language count. The inaccessible canonical-positions paper is a concrete remaining risk, not evidence against the claim.

## value

PASS

The minimal forbidden spectrum measures a natural structure of a standard automatic word that its linear factor complexity cannot detect. Locating all lengths with new forbidden factors and establishing the exact logarithmic accumulation gives a useful language invariant. The preservation of complete extension relations makes the gap result reusable in studying this word, rather than a finite-prefix observation or an arbitrary cut through a larger enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
