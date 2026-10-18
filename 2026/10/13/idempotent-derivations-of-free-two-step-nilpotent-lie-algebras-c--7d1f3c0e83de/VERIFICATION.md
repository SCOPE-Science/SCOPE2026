---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed the unique derivation form D=[[A,0],[f,L_A]] from the free bracket, where L_A(u∧v)=Au∧v+u∧Av; the idempotence equations are A²=A, L_A²=L_A and fA+L_A f=f. Writing V=U⊕W with r=dim U=rank A and s=n-r, L_A has eigenvalues 2,1,0 on Λ²U, U∧W, Λ²W. Thus char!=2 forces r<=1, while char2 permits all 0<=r<=n. The remaining restrictions on f(U),f(W) are necessary and sufficient, and central shears Ψ_h conjugate away f. GL(V) conjugates projections of the same rank, and quotient rank r separates all orbits. Full ranks equal n at r=1 in odd char and r(n-r+1) in char2. Counting r-projections by Gaussian binomial times q^(rs), and admissible f by free dimensions, independently recovers the stated q-exponents. Direct independent enumeration over GF(2) n=2,3 and GF(3) n=2 reproduced respectively {0:1,2:16}, {0:1,3:1408,4:448}, and {0:1,2:36}. Arbitrary-field statement rests on the algebra, not finite enumeration.

## originality

PASS

The general derivation block structure and shear automorphisms are known; the imposed D²=D equations, sharp characteristic-two orbit jump, and labeled finite-field ranks constitute a distinct all-parameter classification in inspected sources. An unindexed equivalent classification remains possible.

## value

PASS

Composition-idempotent derivations of the universal free class-two Lie algebra form a natural operator-theoretic family. The sharp, exceptional characteristic-two jump in orbit types and exact labeled rank distributions, including a rank-4 idempotent on six-dimensional L_3(F2) unavailable in odd characteristic, quantify substantive structure rather than a merely renamed classical fact. The full rank polynomial supports finite-algebra enumeration and representation comparisons. The known general derivation parametrization alone does not tabulate the rank spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
