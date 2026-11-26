---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a shortest gap of length a and any strictly longer gap, the first differing symbol is at one-based position a+2. The ordinary minimum starts at the unique shortest gap, and the alternating comparison selects it against every other zero-start rotation exactly when a is odd. The unique marked gap also precludes a proper power and roots the cyclic list without overcounting. With k further gaps the length is a+1+k(a+2)+sum(t_i), t_i>=0, giving the stated summand for k>=1. The positive root rho_a is simple and is the only pole of its modulus by equality in the triangle inequality. For a parity tail with smallest index b, on any circle of radius r<rho_b the denominators are bounded below by 1-r-r^(b+2)>0 and the numerators are summable. This justifies the residue constants and exponentially smaller tails. The global bound follows from the conflict between prefixes 00 and 01 for mixed words, the trace of the two-state cyclic no-00 transfer matrix, and n distinct rotations for each primitive necklace. A fresh direct rotation census confirmed both series for n=1 through 18, including (u_18,v_18)=(96,23), and checked the 00 obstruction in that range. The run is finite corroboration, not a proof or a formal certificate.

## originality

PASS

The supported distinct content is the paired exact enumerators for agreement and disagreement in the uniquely rooted gap family and their conditional asymptotics, contrasted with the global bound. Alternating canonical rotation and structural membership theory are prior work. A distinct later indexed result has exact overlap on the agreement subcount at fixed zero count; it neither establishes earlier priority nor supplies the disagreement count or the stated conditional ratio.

## value

PASS

The unique shortest gap is an intrinsic root, not an arbitrary sample restriction. Counting both outcomes yields exact coefficients and distinguishes a natural conditional concentration from global rarity, with a quantitative exponential correction. This is more useful than the local parity observation or an isolated count; it does not purport to solve the global enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
