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

Reconstructed RESULT.md lines 23–70. Character orthogonality gives q^(-3) times the sum of squared triple-fiber sums. With w=a+b and v=a−b, the second constraint becomes u=s²+sw−v², so the fiber cardinalities are q at s≠0 and q, 2q or 0 as stated at s=0. The squared cardinalities sum to q⁴+q³−q². Unit modulus gives the upper bound, with equality exactly when triple phases align separately in each fiber. The diagonal (0,0) fiber forces cube roots after removing the common phase. Translating zero-sum triples makes each first phase difference additive after subtracting its value at zero, yielding a symmetric F_3-bilinear polarization B. Comparing (t,1−t,0) with (v,v,1+v), v=t²−t, gives B(t,t)=B(1,t²); polarizing gives B(a,b)=B(1,ab). Nondegeneracy of the field trace yields precisely linear-plus-quadratic field trace phases, and also makes the q² normalized classes distinct. Every such phase attains equality. This covers fixed nontrivial additive character and the claimed d≥2, not unrestricted L² extremizers. VERIFICATION.md, verify.py and verification_output.txt record finite corroboration at 3, 9 and 27; they were inspected, not run, and no conclusion for arbitrary d rests on them.

## originality

PASS

The same normalized sharp numerical value occurs in neighboring parabola literature. The supported distinction is global equality rigidity among unimodular full-field inputs for every nonprime field of characteristic three. The closest inspected statements do not establish that classification or a stronger theorem implying it.

## value

PASS

At the natural endpoint for parabola restriction, characteristic three changes the degenerate fibers and permits many abstract F_3-quadratic functions before the nonsingular constraints are imposed. Proving that only field-trace quadratic chirps survive globally is substantial and useful for identifying exact maximizers over every nonprime extension. The value is the complete classification, not another calculation at q=3 or an unrestricted sharp extension claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
