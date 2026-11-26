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

The degree-two anticanonical map is the double cover of the plane branched over the smooth quartic. Its rational sections are indexed by 31 rational lines; a section is smooth genus one precisely when the homogeneous quartic restriction has four simple geometric roots. The 3 coordinate lines always qualify; the 4 lines at each pair of nonzero equation coordinates qualify exactly when the corresponding branch coefficients do not sum to zero. For 16 full-support lines, coordinate rescaling reduces to x+y+z=0. One can independently check the asserted discriminant test as follows: a tangent there has ax³=by³=cz³≠0. Write A=1/a, B=1/b, C=1/c, and scale to x³=A, y³=B, z³=C. Then x+y+z=0 implies (A+B+C)³=27ABC. Conversely if the last equality holds, take cube roots x,y and set z=(A+B+C)/(3xy); now z³=C. Factor x³+y³+z³−3xyz into the three cube-root-of-unity linear forms and rotate the cube roots as needed to make x+y+z=0. Thus the homogeneous tangent test is D=(ab+ac+bc)³−27a²b²c², which expands into the frozen polynomial modulo 5. This test includes geometric contacts, with no degree-drop problem. The normalized coefficient table yields the stated frequencies. For (1,1,2), coordinate-line counts are 2,2,4, mixed-support counts are 8,10,10 in groups of four, and the remaining 16 counts are all 6. Every base value is nonzero, so nonsquare scaling complements each line count to 12 and the total count to 62. The distinct totals 36 and 26 distinguish the twists; permutations and common square scaling exhaust the isomorphism presentations in scope. An independent exact homogeneous-resultant scan reproduced the complete enumeration and spectra.

## originality

PASS

The same-day pointless-quartic bitangent census already covers the underlying tangent-free branch example and, via a small diagonal support argument, the all-transverse diagonal branch locus. It also covers the Fermat example's 15 transverse lines. The distinct supported content is the full 64-triple distribution, including the nonpointless diagonal cases outside that census, and the two complete anticanonical member point spectra on the double covers. Do not claim priority or separate novelty for the covered examples or branch locus.

## value

PASS

The side-by-side spectrum of the two twists describes how the 31 smooth rational genus-one members are distributed, not just whether a smooth section exists or how many rational points lie on the surface. The support-type formula explains how the full spread of 15 to 31 arises in the natural exact diagonal F5 family, including branch curves with rational points omitted from the pointless census. The exact spectra offer concrete tests for arithmetic Bertini and twist comparisons. No additional value is predicated on rediscovering the covered branch example or its all-transverse property.

The dated certificate retains the supplied scientific assessment, sources and limitations.
