---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Checked analytically and independently exhaustively within the bounded needed lattice-vector norm range: in L0=2Z^3 union ((1,1,1)+2Z^3) there are precisely six nonzero vectors ±2ei of l1 length 2 and eight odd sign vectors of l1 length 3; no other vector has length <=3. For r<=1 interiors do not overlap. For 1<=r<=3/2 only differences ±2ei create positive-volume pair lenses; centered at coordinate x1=1+t each lens section is a planar l1 ball of radius r-1-|t| and volume integral ∫_{-(r-1)}^(r-1)2(r-1-|t|)^2dt=(4/3)(r-1)^3. Three unordered short pairs per volume-4 lattice fundamental cell yield exact double-covered fraction (r-1)^3. Distinct short neighbors differ by l1 distance 4>2r, forbidding any positive-volume triple intersection. Inclusion/exclusion gives covered=r^3/3-(r-1)^3, uncovered=1-r^3/3+(r-1)^3=r(3-r)(3-2r)/3 and singles=r^3/3-2(r-1)^3. At r=3/2 uncovered0, double1/8 and single7/8, with exact near-threshold polynomial 3epsilon/2-2epsilon^3/3. These are symbolic infinite periodic consequences of a proven bounded neighbor classification, not numerical sampling.

## originality

PASS

Best-knowledge PASS for the complete radial multiplicity profile of the specific BCC optimizer; Lian--Xue proves the sharp covering density 9/8 and is the source of the natural lattice normalization but that endpoint statement alone does not determine all subcritical occupied and double-overlapped fractions. The source abstract was inspected; primary full text was unavailable, so detailed absence from the actual primary appendices is NOT verified and is retained as material risk. The earlier Dougherty--Faber degree-diameter conjecture is about optimal covering, not on inspected abstract evidence an exact radial volume distribution.

## value

PASS

The just-established optimum singles out a canonical body-centered cubic lattice and natural first-overlap scaling window. The full uncovered/single/double multiplicity classification explains precisely where the density excess 1/8 sits, proves triple coverage is null at threshold and gives exact near-covering deficit; such data directly inform geometric understanding and local stability questions without pretending to prove lattice perturbation stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
