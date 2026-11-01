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

# Reproduction of the integral homotopy calculation

Run `python3 verify.py` from the directory containing this file. The program uses Python 3 and SymPy, enumerates all edge-disjoint subsets of the 32 edges of \(Q_4\), verifies both full reversed-Hasse digraphs are acyclic, constructs their complete signed integral Morse degree matrices, and computes Smith normal forms over \(\mathbb Z\). The expected output appears in `verify_output.txt`; its final marker is `ALL_CHECKS_PASS`.

The exact forward Morse boundary is a 39-by-168 integer matrix with 909 nonzero entries and 38 nonzero Smith factors, all one. The reverse Morse boundary is 12-by-141 with 512 nonzero entries and eleven nonzero unit factors. These establish the absence of torsion and the **primitivity of all independent attaching vectors**. A continuous homotopy conclusion follows by Hurewicz because there are no cells between dimension zero and four.

Run `python3 mod2_crosscheck.py` using only the Python standard library. This program independently enumerates the full original complex and computes all mod-two simplicial boundary ranks, recorded in `mod2_crosscheck_output.txt`, with final marker `MOD2_CHECK_PASS`. Its computed ranks are \(1,31,369,2127,6129,8078,3440,272\) for boundaries from cardinalities one to eight, yielding mod-two Betti numbers one in degree four and 130 in degree five. It cannot establish integral torsion-freeness or homotopy type by itself.

Both programs inspect the whole finite complex; no sample is used to replace an exhaustive proof. Computational resource requirements and integer-arithmetic library versions can affect running time but not the specified deterministic arithmetic. No external mathematical audit is claimed.
