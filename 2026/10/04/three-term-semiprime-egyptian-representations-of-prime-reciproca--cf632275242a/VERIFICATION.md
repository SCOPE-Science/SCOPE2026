---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof is symbolic and valid for every prime. Its critical steps are:

1. A representation by distinct squarefree semiprimes is a finite simple graph on prime vertices.
2. The target prime \(p\) must occur among those vertices.
3. For every other vertex \(q\), multiplication by the product of all support primes and reduction modulo \(q\) rules out degree one.
4. Therefore one and two edges are impossible, while three edges force a triangle.
5. A triangle on \(p,q,r\) represents \(1/p\) exactly when \((q-1)(r-1)=p+1\).
6. If \(p\equiv1\pmod4\), the product on the left can be \(2\pmod4\) only when one of \(q,r\) is \(2\), forcing the other to be \(p+2\).

`verify.py` provides finite exact-arithmetic corroboration. It enumerates one-, two-, and three-edge subsets on a fixed finite prime set, checks every prime-reciprocal equality against the triangle criterion, tests the factorization criterion for every prime through \(5000\), and checks the twin-prime corollary on the same range. Its output is stored in `verification_output.txt`.

The finite range is not an exhaustive proof for arbitrary primes and is not presented as one. No external certificate or independent validation is claimed.
