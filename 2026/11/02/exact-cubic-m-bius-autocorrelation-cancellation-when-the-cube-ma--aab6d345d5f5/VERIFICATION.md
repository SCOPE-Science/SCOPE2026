---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For odd q with gcd(3,q-1)=1 and h!=0 constant, Pellet identity makes mu(f)mu(f+h)=chi(Disc(f)Disc(f+h)). If char!=3, depress T^3+aT²+bT+c and substitute U=-4A³ using cube bijection. For each B, sum_U chi((U-27B²)(U-27(B+h)²)) is q-1 exactly at B=-h/2 and -1 otherwise, yielding 0 on summing all q B and a. In char 3, Disc=a²b²-b³-a³c, so a!=0 contributes -q(q-1), while a=0 contributes +q(q-1); cancellation is exact. The proof covers odd prime powers including extensions of char 3. Independent root/squarefreeness computation gives zero for all nonzero constant h in F_3 and F_5 (and h=1 in F_11); excluded F_7 gives -91 at h=1 and 77 at h=2. Actual finite-field source checker was read, not trusted as proof.

## originality

PASS

Best-of-knowledge PASS for an exact all-field cubic shift identity distinguished from Carmon–Rudnick asymptotic polynomial Möbius correlation bounds. The quadratic-character sum is classical and not itself novel. The characteristic-three direct cancellation is a meaningful additional component.

## value

PASS

The exact zero over an infinite arithmetic class of finite fields is a sharp small-degree exception to generic square-root cancellation estimates, including characteristic three and extension fields. Precise finite-field correlations are natural arithmetic invariants; the excluded q≡1 (mod 3) boundary is substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
