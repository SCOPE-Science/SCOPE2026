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

# Reproducible checks

Run `python3 verify_interval_union.py` using standard Python 3. The script needs no external modules or files. The direct test enumerates all admissible two-valued maps and every partition on carriers of sizes \(4\) through \(7\), testing the implication \((x,y)\in\theta\Rightarrow(f(x),f(y))\in\theta\). The separate kernel-criterion test enumerates all partitions on sizes \(4\) through \(8\), reconstructs the join of all prescribed congruences separating each output pair, and checks Galois closure without enumerating the operation family.

Observed operation counts for \(m=4,5,6,7\) were \(4,24,98,330\), and the full congruence count was six throughout. The independent kernel tests covered respectively \(15,52,203,877,4140\) partitions on sizes \(4,5,6,7,8\) and returned exactly six congruences in each case. The recorded output is in `verification_interval_output.txt`; the final line is `VERIFY_OK`.

The mathematical theorem holds for every integer \(m\ge4\) by the symbolic interval-union argument and sharp height bound in `RESULT.md`; finite verification is not proof of those infinite quantifiers. The code does not test arbitrary separate choices of equivalences in the lemma beyond the specified construction, and does not minimize the number of operations.
