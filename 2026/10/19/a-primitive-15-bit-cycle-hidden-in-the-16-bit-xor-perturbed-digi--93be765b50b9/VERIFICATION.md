---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The primary paper’s Figure 2 description and Eqs. (6)–(8) confirm that the feedback is the XOR of the two conditionally complemented tail bits; the two occurrences of the selector cancel. This gives the stated autonomous update, not a rule about the initial-seed selector. The image lies in the three-bit parity hyperplane, and the kernel is exactly {0,1^k} from the first k−1 equations. Rank and the odd tail parity of 1^k show that the image is the hyperplane and the restriction to it is bijective; all outside states have exactly one step of transient, and each image point has one outside predecessor. For the characteristic polynomial, elimination with unit pivot coefficients gives b_j=(t^{j−1}+⋯+1)b_1; the final row is (t+1)b_k+b_{k−1}, giving t^k+∑_{j=1}^{k−2}t^j. Removing the zero quotient gives the stated Q at k=16. The private replay /workspace/branches/review5_exact.py verified all 65,536 states by exact indegree peeling and orbit traversal, giving cycles [1,32767] and 32,768 one-step tails. It separately obtained t^32768=t and t^32767=1 modulo Q, both Rabin gcds equal to 1, and residues 021F, 5193, 355C for the three order tests. Irreducibility and these nonidentity residues prove primitivity; multiplication by the primitive element acts transitively on the nonzero field elements. The basin sizes are 2 and 65,534. The frozen word ‘nonunit’ in the polynomial certificate is an editorial misuse: all three residues are units but not the identity, and the proof explicitly uses only the latter. Uploaded code was inspected, not executed.

## originality

PASS

The pass is for the exact identification and state-transition classification of this particular published architecture, including the nonperiodic part. The circuit itself, maximal-length shift-register theory, and the primitive polynomial considered by itself are not new. The same-circuit article and thesis passages inspected describe the update and empirical behavior, not this exact classification. Continuous full-tent cycle theory does not apply to the gated bit update as a substitute for the claimed result.

## value

PASS

This is a complete and independently checkable classification of a motivated published digital architecture, distinguishing empirical coarse histograms from a precise output support restriction and distinguishing period from the basin and transient structure. The reduction reveals a lost dimension at any stated word length and quantifies the entire published 16-bit state graph. It is useful without novel LFSR theory or claims about an application attack.

The dated certificate retains the supplied scientific assessment, sources and limitations.
