---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

G_N=Aut_Fq(F_q[x,y]/(x,y)^N) for odd prime-power q and N>=3 splits U_N semidirect GL2(q), with |U_N|=q^D, D=N(N+1)-6. For every order-two f, linear part A is semisimple and h=(id+A^-1 f)/2 is identity-tangent and conjugates f to A. The centralizer coefficient restrictions are odd degrees for -I, and exactly one out of two output monomials for diag(1,-1); hence |fiber(-I)|=q^E and |fiber(mixed A)|=q^(D/2), times q(q+1) mixed linear parts. The other single class is identity, giving 1+q^E+q(q+1)q^(D/2); even/odd N parity exponent differences 1-r and r+2 establish alternating dominance. Independently counted homogeneous centralizer coefficient dimensions for q=3,5,7 at N=3..14. This is not an extension to q even.

## originality

PASS

Finite-order formal linearization is classical; O’Farrell–Zaitsev Lemma 2.1 gives it in characteristic zero. Here the finite-field truncated two-variable group’s explicit centralizer orbit sizes and alternating dominance are the claim, not linearization. Resultary’s truncated coordinate-cross automorphisms involve another quotient, and indexed broader group results inspected do not supply these exact counts. Earlier unindexed group enumerations remain possible.

## value

PASS

Natural finite jet automorphism group has a new complete conjugacy-class enumeration for involutions and a counterintuitive parity switch of dominant linear type with cutoff N. The explicit all-q all-N formula is a useful structural finite-group invariant, not merely a single numerical tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
