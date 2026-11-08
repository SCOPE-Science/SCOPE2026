---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For prime p and sum-free multiplicative H<=F_p^*, S_H is GD. If a GD superset contains t not in S_H, p|t is excluded by 1+t collision. K=<H,t mod p> must be modular sum-free: any K modular triple can be represented r_i=t^{e_i}h_i and lifted to a positive exact integer triple through A s1+B s2=C s3 with A,B,C powers of t; g=gcd(A,B,C) divides the numerator and, since p∤g, also N=(C h3-A h1-B h2)/p. Bézout provides integer z_i solving A z1+B z2-C z3=N, and positive kernel increments (LC,LC,L(A+B)) make all s_i positive. This contradicts GD closure; hence global integer maximality iff finite subgroup maximality. Cyclic F_p^* means every first enlargement has prime index ell, and divide-by-w converts modular u+v=w to a+b=1, or a-b=1 with -1. Checked safe primes, p≡1 mod4 fourth roots, p=19 and 31 and independent exact subgroup enumerations.

## originality

PASS

The preceding 2026 GD paper defines the same arithmetic closure problem and shows residue-one progressions for p>=5 admit ±1 extensions, but its full openly available eight-page text addresses T_k,V_k,W_k (Theorems 4–5) and expressly leaves a formula for maximal extensions of V_p open in Problem 7. The fresh prime-index test handles whether the ±1 extension or arbitrary sum-free subgroup residue system is itself globally maximal, including nonperiodic extensions. This extends rather than reproduces the previous paper.

## value

PASS

A finite explicit prime-index decision test for maximality against *all* nonperiodic GD supersets closes a natural residue-extension problem left open in the recent originating paper; its positivity-preserving lifting lemma is a structural argument, not a trivial renaming or isolated congruence example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
