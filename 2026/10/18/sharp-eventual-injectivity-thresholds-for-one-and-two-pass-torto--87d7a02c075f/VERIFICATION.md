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

For each word with at least k ones, iterating the specified operation deletes the original first k ones before the appended ones can be selected, and appends k terminal ones. Thus the prefix of length m−k of an image at length n≥m is exactly the deleted version of the original m-prefix when that prefix contains k ones. Injectivity at m reconstructs the identical original prefixes, including all positions of the deletions, and the rest of the image gives the original tails. This proves the universal lifting lemma. Independently generated the exact factor language without a finite-prefix exhaustion assumption: the period-doubling digit recurrence gives v₂(j+1) mod 2, fixes even positions at zero, and gives adjacent pairs 00,01,10 (each in the first six digits). In the aligned length-32 blocks μ⁵(0), μ⁵(1), the first 31 positions are determined independently of the input symbol by that recurrence, and only the last position uses the fivefold complement of the input symbol. Every window of length at most 18 meets at most two blocks, and every allowed adjacent block pair occurs. The resulting exact factor sets agree with all 28 listed 18-factors, the original substitution-closure equality and all 18 table rows. At m=10 all factors have one or more ones and all 16 first images are distinct; at m=18 all have at least two ones and all 28 second images are distinct. Both claimed pairs have the exact common images and belong to the factor language. Lift from 10 and 18 and use the collisions at 9 and 17 to prove sharpness.

## originality

PASS

Best-of-knowledge pass for the sharp one- and two-pass analysis as a whole, with a concrete exact later catalogue overlap on the entire one-pass part. No earlier coverage of that threshold was established; the strongest exact later match does not give the genuinely iterated threshold or its profile. Ordinary factor complexity and the tortoise invariant are already known and are not credited as new.

## value

PASS

This uses fixed-iteration image complexity to measure information loss on a classical automatic word for which ordinary complexity is known. A second pass significantly extends the exceptional regime and the result locates the exact last collision, then proves absence at every longer length. Both the finite boundary and the lifting argument matter: an ordinary complexity count, bounded deficit, or long-prefix numerical profile does not answer the rigidity question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
