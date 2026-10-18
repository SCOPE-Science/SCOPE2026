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
# Computational verification

The two stand-alone C++17 certificate sources enumerate the orbit-reduced ordered first-four source tuples, not a sample of quadruples. For each dimension \(6,8,10,12,14\), the bitset implementation independently constructs every relevant Hamming ball, while the binomial implementation counts test words according to eight coordinate types. Each agrees on the orbit totals and on the minimum number of uncovered vertices for every possible second-source distance strictly smaller than the dimension.

Verified minimum uncovered values: \(5,16,53,185,650\) in dimensions \(6,8,10,12,14\). Corresponding total capacities of the later balls are \(0,1,12,93,592\). Hence every finite non-antipodal case fails to cover. In dimension fourteen, a normalized ordered quadruple encoded as \((0,4095,12415,16257)\) leaves exactly \(650\) vertices; an additional direct integer enumeration of all \(16384\) test vertices confirms it.

To reproduce: compile `certificate_bitset.cpp` and `certificate_binomial.cpp` with `g++ -O3 -std=c++17`; run each executable with command-line arguments `6`, `8`, `10`, `12`, `14`, and compare its per-distance outputs to the two recorded text files. The small cases \(n=2\) and \(n=4\) have elementary proofs in the result document. The programs certify only dimensions explicitly executed; no infinite conclusion or independent external audit is implied.
