---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For W^n the residue spaces H_r=span{e_{r+jn}:j>=0} are reducing, and ||W^n|H_r||=1 as products of n weights converge to one. Norm attainment on H_r is equivalent to a length-n all-unit-modulus block starting at residue r mod n; positive nonzero weights ensure that the norm-one eigenspace E=ker(I-(W^n)*W^n) with one coordinate in each residue is *-cyclic for W^n, thus its projection into every nonzero reducing subspace is nonzero and yields a norming vector. For universal P_m=>P_d let g=gcd(m,d), L=m-d+1. If m>=2d-g then the cyclic interval F_s={s,s-1,...,s-(L-1)} mod d contains an entire class mod g, forcing a length-d unit subblock in desired residue s from one of the m residue types. If m<d, separated unit blocks of length m witness failure. Otherwise L<=d-g and complement F_s meets all g-classes, allowing CRT starts modulo m and d avoiding s in all m separate blocks; all off-block weights 1-eta/(j+2) give arbitrarily small compact perturbations. Diagonal |W^n| has all-norming reducing restrictions iff only finitely many weights are deficient: with infinitely many deficient blocks, the diagonal restriction to those positions has unattained norm 1; finite deficiencies give finite spectral support. Defects at 2^k have arbitrarily long unit runs proving P_n for all n but no modulus P. Independent exact gcd-coset enumeration checked 10000 m,d pairs <=100; infinite theorem is analytic.

## originality

PASS

Su and Zhang 2026 supply the beta and beta0 reducing-subspace attainment framework and a single weighted-shift/modulus separation. Gu 2018 treats common reducing subspaces of weighted shifts, and earlier Ramesh–Osaka defines the property. The proof derives a new exact ordered-pair gcd threshold and near-unweighted compact witnesses, not merely the definition or a known norm profile. No inspected theorem implies the universal arithmetic criterion. The Ramesh–Osaka complete article was inaccessible; abstract-level material is not falsely labeled a full comparison.

## value

PASS

The exact inequality m>=2d-gcd(m,d) completely classifies which powers transmit a natural operator-theoretic norm-attainment property, with nontrivial coprimality dependence. Every failing pair has a counterexample compactly near the canonical unilateral shift, and simultaneous power attainment is sharply separated from modulus attainment. This is a motivated structural classification, not a textbook instance or an arbitrary table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
