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

On probability S³ a Gaussian's radial moments are 24 and 322560 at orders 4 and 12. For a trace-free symmetric matrix the quadratic Gaussian cumulants are 2^(j−1)(j−1)!p_j; the sixth moment uses partitions 6, 4+2, 3+3, 2+2+2. Newton gives p₆=(3/4)p₂p₄+p₃²/3−p₂³/8. Thus ∥Y∥₂²=p₂/12 and the ratio is −27/14+(162/7)p₄/p₂²+(72/7)p₃²/p₂³. As an independent check of the endpoints, write the four eigenvalues as r+s+t, r−s−t, −r+s−t, −r−s+t and put D=r²+s²+t². Then p₂=4D, p₃=24rst, and p₄/p₂²=3/4−(r⁴+s⁴+t⁴)/(2D²). The last term gives bounds 1/4 and 7/12; AM–GM gives p₃²/p₂³≤1/3. Lower equality is one nonzero coordinate (two plus and two minus eigenvalues), and the upper bounds are jointly saturated exactly when |r|=|s|=|t| (one-versus-three). The unit sphere of trace-free real matrices is connected, so the full real interval is attained. For Y=U+iV the angular mean of |Re(e^(−iθ)Y)|⁶ is (5/16)|Y|⁶. If the real component Gram matrix has trace L=a+b and determinant d=ab−c², the angular mean of ∥Re(e^(−iθ)Y)∥₂⁶ is (5/16)L³−(3/4)Ld by diagonalizing the Gram matrix. The real inequality then yields deficit at least 36Ld. Zero determinant forces constant phase; real upper equality then forces the zonal profile. Conversely each stated extremizer gives equality. There is no claimed lower bound for general complex harmonics.

## originality

PASS

The exact real interval, equality cases, invariant formula and both real defects have equivalent coverage in distinct record ae7779ab9a93. The checklist does not credit those as an uncovered result in the current corpus, or infer priority or derivation from dates. The distinction supported for the frozen finding is the quantitative complex phase estimate on S³, with sharp complex upper classification. Qualitative complexification follows from the real upper bound by a standard triangle inequality, but the explicit Gram determinant control is not furnished by that argument or any inspected stronger theorem. The real inputs, already known trace bounds, and later equivalent real statement should be distinguished from this quantitative conclusion.

## value

PASS

S³ degree two is a natural fixed harmonic eigenspace, and the quantitative phase conclusion adds information to a qualitative equality classification. In fact the determinant is the product of the squared L² lengths of the phase-rotated perpendicular components; the phase loss forces the smaller one to vanish at equality and controls it for near extremizers, not just on the zonal orbit. The exact real norm range is useful context for the complex estimate but is not counted again as a new result relative to the equivalent real record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
