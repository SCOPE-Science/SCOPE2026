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

For code C the signature of (i,j) is R_i∪B_j. In a row i, two column signatures agree exactly when both column contributions outside R_i are empty. An empty column thus forces at least 2(m−1) selected cells; with no empties, at most three singletons are possible and at size 2m−3 there must be exactly one per row and exactly two entries in every other column. Such words dominate and separate within rows. Equality of two signatures from different rows i,h forces each cell to lie in the other row's singleton column, by membership of the two singleton codewords; it then forces both rows to lack any other codeword. A double column must meet at least one of i,h, which rules this out for m≥4. There are m(m−1)(m−2) singleton placements and three choices per double. Preserving column counts allows only double recoloring (2 choices per double); changing them relocates an S_i into a double containing i, with 2 receiving-row labels and 2 recolorings of the vacated singleton per double. This gives all 6(m−3) distinct moves and the stated edge total. Recoloring lets any singleton move to any double column; an unfixed singleton occupying a desired target can be moved into a double buffer without dislodging a fixed marker. This connects every singleton placement and then independent double recolorings finish the path. Row and column equivalence is exactly equality of the three missing-row multiplicities up to permutation. Independent signature and token-jump enumeration at m=4,5,6 checked 1586,16384,155382 subsets through the respective optimum, found 72,540,3240 optimum words and 216,3240,29160 edges, and reached every optimum word in each exchange graph. Frozen verify.py is the supplied replay (inspected, not run): its m=8 check is on predicted configurations, not an exhaustive subset search. All-m claims use the proof, not extrapolation.

## originality

PASS

The scalar optimum is prior and explicitly attributed. The necessary singleton-column pattern also follows from Goddard–Wash's lower-bound argument by equality. The supported distinct content is the sufficiency of the complete equality description and the exact token-jumping structure, including exhaustive moves, degree, connectivity and natural orbits, which are not established by the earlier sources inspected. A later catalogue theorem implies the static classification; its date does not certify publication priority.

## value

PASS

Recovering every minimizer and how one-token modifications connect them goes beyond the known optimum. The minimal rectangle with three distinct singleton markers has a complete uniform move rule and reconfiguration invariants, not merely a list of small cases. The structural description directly gives all states and local transitions and supports exact reachability; the proof does not claim a diameter or results for all rectangular sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
