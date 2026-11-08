---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed the birational Artin–Schreier-over-elliptic model y²+xy=x³+1, z²+z=y/x+(x⁴+x³+1)/(x(x³+1)); its eight distinct simple ramification poles yield genus 9 by Riemann–Hurwitz, with rational exceptional contribution B_n=2+2 gcd(3,2^n-1). Reproduced independent exhaustive plane-model counts for n=1..9 in fields F_{2^n}, obtaining 4,8,4,24,44,8,116,312,508. Newton identities and the genus-nine Weil symmetry uniquely fix the degree-18 numerator from those nine counts; direct factor multiplication verifies (1-T+2T²)(1+T+2T²)^2(1-T²+4T^4)(1-2T²+T^4-8T^6+16T^8), value L(1)=1024. Independent exact rational factorization confirms degree-four and degree-eight factors irreducible, supporting simple isogeny dimensions 2 and 4 (alongside three elliptic factors). This finite computation genuinely suffices for all extension counts only because genus and Weil functional equation are proved.

## originality

PASS

The 2026 Tafazolian model and its genus/automorphism results are acknowledged original prior work. The purported contribution is the explicit F2 numerator, extension counts and simple isogeny-factor decomposition; a different genus-nine large-automorphism example in Giulietti–Korchmáros does not directly supply these invariants. Original Tafazolian full text could not be retrieved this run (abstract/metadata only) and may hide a zeta calculation; this is a serious specifically named priority risk but not proof of coverage.

## value

PASS

The exact zeta numerator for a canonical explicit genus-nine ordinary curve determines all extension-field point counts, its finite Jacobian group order and the simple factors of its rational isogeny class. These are motivated natural arithmetic invariants complementing the prior geometric automorphism construction; distinct simple dimensions are not a recomputed generic table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
