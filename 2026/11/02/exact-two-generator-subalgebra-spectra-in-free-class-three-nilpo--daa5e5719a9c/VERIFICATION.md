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
# Reproducibility and scope

Run `python3 verify.py` with Python 3.9 or newer. The program constructs the free class-three Lie algebra directly as a commutator subspace of noncommutative words of degrees one through three, in each tested prime field. It does not import the written closed forms to obtain generated dimensions: it independently computes \(\dim\langle x,y,[x,y],[x,[x,y]],[y,[x,y]]\rangle\), and canonically reduces the actual spans to count distinct subalgebras.

Full enumeration: over \(\mathbb F_2\), at \(n=2\), all \(1024\) ordered pairs of the \(32\)-element algebra produce pair counts \((1,93,258,288,384)\) in dimensions \((0,1,2,3,5)\), and distinct-subalgebra counts \((1,31,43,12,1)\). Over \(\mathbb F_3\), at \(n=2\), all \(59049\) ordered pairs of the \(243\)-element algebra give \((1,968,7536,15552,34992)\), with distinct-subalgebra counts \((1,121,157,36,1)\). All match the exact formulas.

Further seeded \(1500\)-pair samples each cover \((n,q)=(3,2),(3,3),(4,2)\); these are tests, not exhaustive censuses. The program ends with the exact marker `FREE_CLASS3_TWO_GENERATOR_CENSUS_OK` only if all assertions pass. No external packages are required. The written proof, not the finite computations, establishes the result for arbitrary finite fields and unbounded \(n\).
