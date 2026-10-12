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

The correctness check has two layers. First, the published Levenshtein lower bound and its equality condition reduce an optimal binary index-one length-\(19\) system to two disjoint triples whose ordered external differences contain each nonzero residue once. Second, `verify.py` performs the resulting finite classification directly from that definition.

The verifier exhausts every unordered pair of disjoint triples, verifies all \(18\) differences, and obtains \(1{,}482\) unordered or \(2{,}964\) ordered systems. It then exhausts all \(342\) affine coordinate maps and the order-\(684\) action obtained by adjoining block interchange. It checks the five orbit representatives, orbit sizes \(684,684,684,684,228\), stabilizer orders \(1,1,1,1,3\), and the exceptional stabilizer generator \(x\mapsto7x+1\).

Recorded replay output:

`VERIFY_OK unordered=1482 ordered=2964 ordered_group=684 orbits=5 orbit_sizes=684,684,684,684,228 stabilizers=1,1,1,1,3 special_generator=u7_t1 census_sha256=2c153b1f18f4891ec972fcd7110635049b278dfcbac66820726fd774ef7b5e89 small_m1_m2_orbits=1,1`

The census digest is over the complete lexicographically sorted unordered list, one line per system in the format `A|B`. The digest anchors the exact enumerated set but is not used in place of the defining checks.

The proof does not claim that affine equivalence is the largest possible abstract equivalence relation. The literature comparison also retains the stated residual risks concerning historical extended tables and unindexed classifications.
