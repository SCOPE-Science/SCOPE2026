---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Put t=beta/alpha>0. For any unit Birkhoff pair, ||t x-y||=t||x-y/t||>=t, and ||x+t y||<=1+t; hence objective <=1. If 0<t<=1, triangle/reverse-triangle give ||x+t y||<=1+t and ||t x-y||>=1-t, so objective <=2t. For 0<t<=1/2 the unit vectors x=(1,-1), y=(2t-1,-1) are Birkhoff orthogonal: when lambda>=0 the second coordinate has modulus 1+lambda; when lambda<0 the first coordinate 1+(2t-1)lambda>=1. Their objective is 2t because ||x+t y||=1+t and ||t x-y||=1-t. For t>=1/2, x=(1,-1), y=(1,0) are Birkhoff orthogonal for all lambda via the fixed second coordinate; ||x+t y||=1+t and ||t x-y||=max(|t-1|,t)=t, achieving 1. The endpoints t=1/2 and t=1 are included, and t is always strictly positive. Any square sphere segment lies in a common face, so shared saturated coordinate of x,y becomes (1-2/t) times its sign at z=x-(2/t)y, of modulus >1 for t<1; hence no two-segment witness then. The full publisher original Theorem 2 prints that condition as necessary, so the claimed counterexample interval is valid. Independent exact rational regression over 13,395 t values reconstructs witnesses and source Git tree but does not prove the universal quantifiers.

## originality

PASS

Best-of-knowledge: the original full-text 2024 source introduces the exact same constant and bounds it by 1, but does not state the square all-parameter profile and in fact prints a necessary upper-bound-attainment condition refuted on a nonempty interval. The published Radon/hexagonal result applies a symmetry hypothesis violated by the square. A 2026 skew-gauge preprint studies different unrestricted weights; its full primary text was inaccessible, so only the abstract-level distinction is asserted and that material remains a specific risk. Resultary included a listing of the assigned finding itself, excluded as independent prior publication, and noncovering related Birkhoff constants. No distinct published stronger statement implying both the exact square profile and the sharp-attainment counterexample was found in actual searches.

## value

PASS

The real square plane is a canonical nonsmooth extreme Banach plane and B_{alpha-beta} is a named geometric invariant. Determining its complete two-parameter (ratio) profile, rather than a selected example, identifies the sharp natural switch at t=1/2. More substantively, the exact extremizers expose an interval of explicit counterexamples to a printed iff characterization of maximal skew separation; the supporting-face contradiction identifies the structural reason. This is a motivated correction/benchmark for any subsequent equality-condition or Banach geometric-constant study, not an arbitrary tiny parameter slice. It does not claim a complete general corrected iff theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
