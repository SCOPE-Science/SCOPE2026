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

# Reproduction and scope

The public package contains two complete standalone source files. Run `python3 verify.py` (Python 3.8+) and `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt` (C++17 compiler). No nonstandard packages, downloads, pretrained models, or external certificates are needed.

The first program generates the five-regular graph with XOR differences \(\{1,2,4,8,15\}\), independently checks its strongly regular local data, then scans all four- and five-element subsets, constructs every fixed-size swap, checks the exact degree counts, and performs 1056 complete breadth-first searches. It also realizes the complete 1920-element automorphism group and computes its five-set orbits. Its last output line is `ALL_VERIFY_OK`.

The second program independently labels the folded five-cube by even-weight five-bit binary vectors and puts an edge at Hamming distance four. It scans all 65536 selection masks, computes all swap neighbors by a different implementation, checks the 80 and 1056 dominating-set counts, all 10320 edges, and recomputes distances from each state. Its last output line is `INDEPENDENT_VERIFY_OK`.

These checks certify the enumerated finite instance if the sources are executed as provided; they do not extrapolate to higher-dimensional folded cubes. Literature novelty and publication priority are not mechanically certified. No independent scholarly audit has been performed.
