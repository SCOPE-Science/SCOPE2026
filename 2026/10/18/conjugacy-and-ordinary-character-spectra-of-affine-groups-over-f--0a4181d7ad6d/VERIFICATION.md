---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For a finite commutative chain ring R with maximal ideal m=(π), |m^j|=q^{n−j}, multiplier group U abelian and G=R^+⋊U, direct conjugation gives (b,w)(a,u)(b,w)^{-1}=(wa+(1−u)b,u). If k=v(1−u), the additive orbit is one class mod m^k when v(a)≥k, size q^{n−k}, and one complete shell for each h<k, size (q−1)q^{n−1−h}; hence k+1 classes per multiplier. Summing |1+m^j| gives N+(q^n−1)/(q−1) classes and stated commuting probability. A generating additive character exists because every nonzero ideal contains the socle; the additive dual is R with unit orbits by valuation. Clifford induction from H_h=1+m^{n−h} of size q^h yields exactly q^h degree (q−1)q^{n−h−1} irreducibles plus |U| linear characters. Differences of ideal-character sums give the stated three-case formula S_(n−h)(a) and complete values, and the sum of squared degrees is |G|. For Z/8 vs F2[t]/(t³), U differs C2² vs C4 so G_ab differs C2³ vs C4×C2 even though q=2,n=3. Independently enumerated affine Z/8 conjugacy classes 1^2,2^3,4^6 (order32), Z/9 classes 1^1,2^1,3^2,6^3,9^3 (order54), and Z/4 classes 1^2,2^3, consistent with the formulas. These finite counts corroborate, not prove, the universal representation classification.

## originality

PASS

PASS qualified best-of-knowledge: the finite-field GA_n(q) literature, cyclic ring Z/p^n character calculations, and general Clifford induction are acknowledged. The specific full valuation-shell conjugacy spectrum, all ordinary character-value formulas for arbitrary mixed/equal-characteristic commutative chain rings, and equal-spectrum nonisomorphic example were not shown as consequences of the inspected sources alone. Unread thesis and specialist classification remain risks, not novelty proofs.

## value

PASS

A family-wide closed classification of conjugacy classes, ordinary complex character degrees and values for affine groups over every finite commutative chain ring is useful representation-theoretic structure. Uniform spectral invariants across different ring types and an exact obstruction to recovering group isomorphism from those spectra are natural questions, not an arbitrary small numeric gain; cyclic-ring cases and general induction are explicitly credited as prior mathematics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
