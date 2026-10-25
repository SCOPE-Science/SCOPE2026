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

For p≥5 and unit c in Z/p², (a+b=d+e) becomes one-to-one (s,t,w), 2 invertible, and quartic+quadratic equality reduces to (t−w)(t+w)(t²+w²+6s²+4c)≡0 mod p². Every base-p triple in exactly one smooth factor yields p² lifts; any in at least two zero factors yields p³ lifts, no others lift. Q=0 is nonsingular since c is a unit; binary conic H=p−χ(−3), triple intersection J=1+χ(−6c), total quadratic locus p²+p χ(6c). Union U=3p²+p(η−3)+2δ+J, multiple intersection I=3p−2δ−2J, hence E=p²U+p²(p−1)I, giving both formulas. Character substitution χ(−6c)=χ(−1)η yields class difference −2p²(p−3) for p≡1 mod4 and +6p²(p−1) for p≡3 mod4; Fourier orthogonality with probability output p^(−4) yields L4^4=E exactly, not full extension norm. Independent direct pair-sum map (not 3-factor enumeration) verified p=5,7,11, coefficients 1,2,1+p,2+p plus p=7,c=3; e.g. E_5,1=2925, E_5,2=3025, E_7,1=10437, E_7,3=12201. Finite cases do not prove all primes.

## originality

PASS

Finite-field quartic energy and prime-power quadratic parabola results do not imply the unit-deformed quartic graph collision number over the nonfield Z/p². Crucial smooth-factor versus intersecting-factor lift multiplicities have no analogue in the pure-field formula. Hickman–Wright supplies general ring-restriction setup, not this explicit Legendre residue-class split. Source formulas are compared by objects, parameters, and normalization, not merely titles.

## value

PASS

Constant-input Fourier fourth moment/additive energy is a natural exact invariant of polynomial graphs over local rings, influencing Fourier extension lower bounds and collision structure. The sharp p mod4 reversal of which unit perturbation has greater energy is an unexpected arithmetic classification and cannot be inferred by formally substituting the pure quartic or parabolic cases. Its complete uniform p≥5 count is meaningful even without proving the unrestricted operator norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
