---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The equation at vertex w is X_w=sum of the squares of its predecessors. Off-cycle vertices form an acyclic predecessor graph, so taking them in a topological order gives X_w=0 by a monic linear elimination in the full coordinate ring, not just on points. This leaves for each cycle one free parameter and the single relation T^(2^L)-T, so the affine product is scheme-theoretic and has degree the product of the monic degrees. In positive characteristic p, writing 2^L-1=p^a M yields simple zero and multiplicity p^a at each nonzero geometric root, since p does not divide M. Over an algebraic closure the tensor product of the cycle factors is reduced exactly if each factor is, because it is a tensor product of nonzero finite algebras over that field and a nonzero nilpotent in a factor survives. Cyclicity of the multiplicative group gives the finite-field formula. In characteristic two the gcd identity for powers of two gives F(m)=sum gcd(L_i,m); each geometric cycle factor has additive coordinates F_(2^L), and a normal basis gives its cyclic Frobenius action. For d<=n, the totient divisor identity writes F(m) as the divisor sum of phi(d) times the number B_d of lengths divisible by d. Möbius inversion gives B_d from F(a) with a|d, and a second inversion over multiples up to n gives the exact multiplicities. This includes loops and has no assumptions on noncycle depth. The two three-vertex witnesses have the same single loop but different dimensions of the square span, an algebra-isomorphism invariant. The verifier computes finite-field idempotents directly, but its separate reconstruction checks construct observations from cycle lengths, not from independent brute-force counts for all n extensions. The code was inspected, not executed; the inversion and full scheme statement are proven algebraically.

## originality

PASS

The cycle decomposition for permutation algebras and the general characteristic-two Frobenius count are covered and do not independently support a pass. The checked distinct result combines an all-characteristic coordinate-ring reduction (including nonperfect algebras and nonreduced factors) with a finite inverse theorem for the underlying recurrent graph and an explicit information-loss witness. No inspected statement gives that remaining claim. This is a bounded assessment, not an assertion of comprehensive priority.

## value

PASS

A single-field idempotent count need not reveal the recurrent graph. The full ring factorization explains what the locus retains even in nonreduced characteristics, and a finite extension-field cutoff recovers exactly the recurrent lengths while two nonisomorphic algebras show why no such scheme data recover the attached trees in general. This is a natural reconstruction result and a sharp distinction of invariants, rather than simply recomputing the known binary forward census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
