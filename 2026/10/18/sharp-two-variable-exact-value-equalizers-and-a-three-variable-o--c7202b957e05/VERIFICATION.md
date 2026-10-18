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
# Verification of exact FOUR equality-locus claims

The included `verify.py` is executable using Python 3 and only its standard library. Run `python3 verify.py`. Expected first line: `FOUR_EQUALIZER_VERIFY_OK`.

For one variable: \(4\) term operations, \(4\) equality loci, agreement-count multiplicities \(\{2:4,3:8,4:4\}\).

For two variables: \(166\) term operations and exactly \(512\) different equality loci across \(27{,}556\) ordered pairs. The code independently constructs loci from (i) all term-pairs, (ii) all convex Boolean disagreement sets, and (iii) all involution-invariant subsets containing the forced bottom and top assignments. All three computed sets are asserted identical.

The independent term evaluator builds positive disjunctive normal forms and checks each resulting FOUR truth/falsity output against the bit normal form at every valuation, without assuming the dual identity as a program primitive. The counterexample check explicitly examines the six candidate assignments, their involution symmetry, interval obstructions, and all subsets for convexity.

Limit: the finite enumerations are only for arities one and two (and the particular three-variable obstruction). The universal structural theorem and higher-arity embedding are established by proof rather than by computation. No independent validation has been performed.
