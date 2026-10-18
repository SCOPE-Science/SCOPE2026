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

# Reproducing the finite evidence

Run `python3 verify_icosahedral_torsion.py` with Python 3.9 or later. No third-party Python package, internet connection, external file, or cached computation is needed. A successful run ends with `ICOSAHEDRAL_TORSION_ACTION_PASS` and prints the checked counts.

The program constructs the explicit twelve-vertex graph and enumerates all \(5888\) augmented matching faces. The simplicial integral boundary uses alternating signs from lexicographic edge order. It checks all original consecutive boundary compositions and then uses only unit \(\pm1\) boundary pivots in an exact algebraic chain cancellation. The final reduced chain groups have \(65\) generators in degree three and one in degree four, whose boundary has nonzero gcd \(3\). Since every pivot is a unit, this is an integral chain-homotopy calculation, not an extrapolation from tests modulo primes.

It independently finds the antipode from graph distance, enumerates all \(120\) graph automorphisms, checks that all their commutators comprise a subgroup of size \(60\), and computes the induced signed action on matching chains. Over \(\mathbb F_3\), the antipodal even/odd degree-four chain dimensions and ranks \((741,686,55)\) and \((741,670,70)\) yield homology dimensions \(0\) and \(1\); the latter corresponds naturally to the order-three integral torsion by universal coefficients. Over \(\mathbb F_5\), the third-homology eigenspace dimensions are \(40\) and \(24\), equal to rational dimensions because no five-torsion occurs and the involution has order two.

Every asserted finite result is recomputed from the source script. The scientific conclusion additionally invokes standard integral unit cancellation, naturality of the universal coefficient sequence, and the fact that a homomorphism to an abelian group annihilates commutators. No theorem-prover certification or independent audit is asserted.
