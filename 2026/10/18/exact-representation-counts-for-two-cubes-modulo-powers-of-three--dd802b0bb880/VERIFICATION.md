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

PASS. For n>=2 the cube homomorphism on the cyclic unit group (Z/3^n)^* has kernel size three and image exactly ±1 mod9. Nonunit cubes vanish mod27. The residue classes ±1, ±2, 3/4/5/6 and 0 mod9 therefore partition all targets with the stated counts. For r=0 mod9, fix unit x and set y=-x+3t; x^3+y^3=9 t(x^2-3xt+3t^2), whose derivative is x^2 mod3 and whose reduction is x^2 t, proving Hensel bijection for each n and exactly 2*3^n opposite-unit pairs. For both coordinates multiples of three, each lower modulus 3^(n-3) pair has 3^4=81 lifts. n=0,1,2 treated separately. Independent exact cyclic cube-frequency convolution checked every target for n=1..7 (3+9+27+81+243+729+2187=3279 residues), reproducing N_n(1)=2*3^n. This finite corroboration is not the universal proof.

## originality

PASS

Best-of-knowledge originality PASS on the exact final claim after new Git-tree proof and computation reconstruction, Resultary semantic searches, checked primary theorem scopes and explicit source risks. Not a claim of comprehensive historical priority, external certification or entire-paper noncoverage where material was inaccessible. All known special-case antecedents are credited.

## value

PASS

PASS. Prime 3 is the exceptional ramified prime for cubic power congruences. Resolving the explicit A087412 three-power conjecture and obtaining the full exact additive two-cube local representation distribution with a nonunit singular recursion is a natural, independently useful arithmetic counting fact. The solvability criterion r mod9∈{0,1,2,7,8} and exact number of pairs for every n are mathematically motivated. Already-known r=0 OEIS formula is credited, and value does not rely on that special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
