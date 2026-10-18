---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The polynomial follows by whether neither, u, or v is chosen: (1+z)^(a+b)+z((1+z)^a+(1+z)^b). With Re z=x>=0, s=|1+z|>r=|z|, s>=1, and s²-2r=(r-1)²+2x>=0. For a=min(a,b)=0, |(1+z)^(b+1)|>r. For a=1, factor (1+z)[(1+2z)(1+z)^(b-1)+z]; the first factor nonzero and |1+2z|²-r²=1+4x+3r²>0. For a>=2, root would imply s^a<=r(1+s^(a-b))<=2r<=s²<=s^a. At s>1 this is impossible for a<b or a=b>2; when a=b=2, all equalities imply x=0,r=1, z=±i, at which (1+z)²+2z=±4i ≠0. The edge K2, star, singleton boundaries hold. Independently constructed independence polynomials for all 0<=a,b<=8 and numerically evaluated all roots, with max tested real part approx -0.144056 at (8,8); only analytic moduli proof is unrestricted.

## originality

PASS

Brown–Cameron establish stars, low independence number, and nonstable trees; Zhang–Tu extend to spiders with one branching center; neither result covers proper double-stars with two branching vertices and arbitrarily many leaves. Hibi–Kara–Vien Proposition 3.1 already implies the displayed polynomial enumeration identity, which is not claimed new, while Bencs yields a special real-rooted D2,2 subfamily, not arbitrary unequal a,b. The new assertion is strict left-half-plane zero exclusion for the entire double-star family. Full text Zhang–Tu was inaccessible and Oxford VPN disconnected; its precise theorem from metadata describes spiders; overlap remains residual.

## value

PASS

Strict Hurwitz stability of all diameter-at-most-three trees is a clear motivated boundary within the known fact that some trees have unstable independence polynomials. Two branching vertices are genuinely outside spider results, providing a natural structural nontrivial step, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
