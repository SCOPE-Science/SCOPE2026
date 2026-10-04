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

Run `python verify.py` with the standard library. The program constructs all \(128\) binary words of length \(7\), implements the zero-padded \(2\)-read vector both as sorted adjacent multisets and as their binary sums, and confirms the two representations induce identical pair distances.

It builds the compatibility graph for minimum read-vector distance \(5\). An exact coloring-bound maximum-clique search and an independent Bron--Kerbosch maximal-clique search both return maximum size \(8\). The displayed eight-word witness is then checked directly.

For the comparison with classical coding, the program verifies the radius-one counting identity \(16(1+7)=128\) and constructs the standard length-seven binary Hamming code as the kernel of the parity-check syndrome, confirming \(16\) words and minimum Hamming distance \(3\).

The computation is exhaustive only for the stated finite parameter. It is not evidence for any unstated infinite family or neighboring length.
