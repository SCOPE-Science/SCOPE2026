---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Tabachnikov’s Lemma 7.1 for convex bicycle polygons, read in the original 2004 full preprint and page image, gives an isosceles trapezoid for each index i with bases ViVi+m and Vi+1Vi+m−1. Pair the trapezoids indexed i and i+m along their common long diagonal. Reflection of leg directions forces θ_i+θ_{i+m−1}≡θ_{i+m}+θ_{i−1} mod 2π, so strict exterior turning angles α_i and α_{i+m} agree (both in (0,π)). Total turn 2π gives a half-turn π per m edges and e_{i+m}=−e_i, hence Vi+m+Vi is constant. Center at zero; then Xi+m−1=−Xi−1, so equal side s and (m−1)-diagonal d yield s²+d²=2(||Xi||²+||Xi−1||²). Subtraction forces squared-radius period two. For odd m, the antipodal index shift swaps parity and equalizes all radii. Strict convexity gives consecutive central angle in (0,π), where equal chord length forces equal angle, hence regularity. For even m, original Theorem 10 gives nonregular one-parameter convex examples n even and k odd, with strict convex parameter choices. No finite experiment is invoked as an infinite proof.

## originality

PASS

Tabachnikov’s foundational 2004 Theorem 9 rigid families do not cover the line (n,k)=(2m,m−1) for odd m≥7; his Theorem 10 already supplies the even-m flexible side and is explicitly credited. Connelly–Csikós examines local first-order flexibility, not global convex rigidity; Tabachnikov–Tsukerman 2012 Theorem 9 concerns the different line (4k,k). The previously published Resultary (10,4) theorem settles only m=5. The uniform new central-symmetry, alternating squared-radius structure, and parity-dependent global rigidity are not logical consequences of that isolated case or the listed neighboring parameter families.

## value

PASS

The original bicycle classification asks exactly which arithmetic (n,k) parameter families permit nonregular convex polygons. The nearest-to-half diagonal k=n/2−1 is a natural infinitely varying line, and the theorem supplies a global central-symmetry/two-radius mechanism and complete parity threshold: infinitely many new odd-m rigid cases with an already-known flexible complementary half. It is not arbitrary low-order enumeration or mere title/parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
