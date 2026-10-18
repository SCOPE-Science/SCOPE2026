---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For two exact prime-power blocks X,Y the identity phi*(XY)=(X-1)(Y-1) follows multiplicatively. Writing even=AB with A=2^a and odd=CD, C<D, the orientation AB+1=CD gives C+D=A+B+1 and (D-C)^2-(B-A+1)^2=4(A-1); the reverse orientation gives C+D=A+B-1 and (B-A-1)^2-(D-C)^2=4(A-1). Both even differences factor into positive integers u,v with uv=2^a-1, and solving back produces precisely the three claimed branches with converses verified by products and sums. Filtering exact positive odd prime-power blocks and distinct supports is essential. Under Omega(n),Omega(n+1)<=3 the even block has a<=2; A=2 gives no valid blocks; A=4 gives only (20,21), while (35,36) fails the multiplicity bound. A newly written direct sieve below 300000 recovered [20,35,143,208,2623,5183] and the unique low-Omega point 20. This finite check supports but does not replace the factorization proof.

## originality

PASS

Known definitions and small collision values are credited. A direct search of the exact collision database OEIS A287055, the primary unitary-totient literature, published mathematical research records and aliases under consecutive equal unitary Euler phi values located no prior unrestricted exact classification of the two-distinct-prime-support subfamily by Mersenne factor pairs with all orientation branches. OEIS lists instances but does not entail the exhaustive factorization converse. Originality is best of knowledge, with unindexed elementary number-theory notes remaining a plausible priority risk.

## value

PASS

The subfamily with exactly two distinct prime supports on both adjacent integers is a natural arithmetic stratum of the established unitary-totient collision problem. The explicit bijective factor-pair classification includes both parity orientations, identifies necessary exact prime-power filters, and yields a non-computational unique low-total-multiplicity theorem; those facts are useful for collision sieves and are not simply table recomputations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
