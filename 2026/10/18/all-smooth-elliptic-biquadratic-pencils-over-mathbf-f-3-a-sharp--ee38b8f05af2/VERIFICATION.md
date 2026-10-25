---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

For a bidegree-(2,2) form over F_3, writing it as A(U,V)S^2+B(U,V)ST+C(U,V)T^2 gives discriminant B^2-AC because 4=1 in characteristic three. A smooth connected (2,2) divisor is a genus-one double cover of P^1; squarefreeness of the binary quartic discriminant is equivalent to smoothness, with the endpoint-root multiplicities checked separately. The independent Jacobian-ideal check examines all four standard affine charts; Euler identities in bidegree two ensure vanishing of all homogeneous partials forces F=0. The projective coefficient space has 9841 nonzero forms up to scale; the Groebner check identifies 5184 smooth forms. Pair enumeration yields 3,594,672 bases, divisible by six, hence 599,112 pencils; the independent RREF subspace enumeration reports the same 599,112. Base-point counts are 0,1,2,3 with 115,848, 306,432, 153,792, 23,040 pencils respectively. Hasse gives b<=4; b=4 would force all four genus-one members to have seven rational points, but the complete joint-count output has no (7,7,7,7) tuple and the independent RREF distribution has no b=4. Source code and outputs were inspected, not treated as an infinite-proof substitute.

## originality

PASS

The result is a finite exact classification of rational base-locus sizes for all-smooth pencils of (2,2) curves on P1xP1 over F_3. Targeted Resultary queries did not return this object or count. The closest primary papers concern smooth hyperplane sections or pencils of quadric surfaces in P3; they motivate smooth pencils but do not imply the exact P1xP1 rational base-locus distribution. No broader table covering these 599,112 pencils was found.

## value

PASS

This is a natural finite-field moduli problem: all four rational members of a pencil are smooth genus-one curves, and the exact number of rational common base points is a geometrically meaningful invariant. The sharp maximum three, an explicit witness and the exact distribution are more than an arbitrary code slice; Hasse provides the natural initial bound four.

The dated certificate retains the supplied scientific assessment, sources and limitations.
