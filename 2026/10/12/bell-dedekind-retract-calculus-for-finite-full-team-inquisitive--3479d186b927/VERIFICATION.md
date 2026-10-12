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

# Verification instructions and scope

Run `python3 verify_team.py` in the directory containing this file. The script uses the Python standard library only, constructs all nonempty lower families of subsets of each finite nonempty set of up to four worlds, and evaluates operations using bitmask representations of teams and families.

The check includes full enumeration of \(\mathcal I(W)\) for \(|W|=1,2,3,4\), giving \(2,5,19,167\) elements, and direct checking of the Boolean core equations. It reconstructs each induced map \(H_f\) for all \(56\) functions between nonempty sets of sizes up to three and operation-checks each homomorphism on every pair of algebra elements for intersection, union, Heyting implication, and tensor. It separately exhausts all \(5^5=3125\) possible maps from the five-element algebra to itself and checks that precisely the four predicted core-preserving algebra homomorphisms survive. For all \(n\le4\), it enumerates all \(n^n\) world self-maps, independently reconstructs their endomorphic image sets, checks equality iff identical kernel partitions, checks inclusion iff opposite partition refinement, and verifies the Stirling/Dedekind rank statistics, Bell count, and idempotent formula.

Expected final line:

`VERIFY_OK 58536 assertions; 56 constructed cross-size homomorphisms; 3125 scalar set maps screened`

The exhaustive \(n=2\) map check does **not** constitute a full exhaustive classification of all functions between the larger algebras; those rely on the general core/Boolean-homomorphism proof. No external formal theorem prover or independently executed audit is claimed.
