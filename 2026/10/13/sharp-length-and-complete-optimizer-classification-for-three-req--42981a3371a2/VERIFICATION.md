---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The named symbols are unit vectors 1,2,4. A minimal recovery subset is independent (otherwise one column could be dropped from its span), has at most three positions, and in a binary independent set uses every column in the target expression. Zero columns thus never occur in a minimal recovery and can be deleted. The frozen exchange peeling computes the greatest exchange-closed triple family: a triple with a missing label over one of its faces cannot be in any such subfamily, and a nonempty stable core satisfies the cited exchange criterion. Reproduced by a different state-space computation using `python3 -B /workspace/reviews/replay_1.py /workspace/source/2026/10/13/sharp-length-and-complete-optimizer-classification-for-three-req--42981a3371a2`. It builds independent sets by updating the span and solves a safety game on all disjoint histories of sizes 0 to 3. A state survives if every legal completion of one process stays in the surviving family, and each possible request label when there is a free slot has some surviving successor. Multiple completions are successive deletions. States removed in a given round can be forced to a failure in finitely many moves by an adverse deletion or arrival label, while the fixed point gives a policy. The empty state wins for 0 of 1716 length-7 multisets and 79 of 3003 length-8 multisets. Any shorter encoder would extend to seven by appending unused coordinates, and any length-8 winner with a zero column would shorten; no such cases are omitted. Winning entails full row rank because all named unit vectors are recoverable. The independent replay checked the exact 79 keys and all minimal-mask strong selections from witnesses.json against every disjoint chosen history of size 0, 1 or 2. It checked all 17 actual displayed table rows, with ten size-six, six size-three and one size-one orbit, and profile counts 48,24,7. The frozen verifier was inspected as evidence, not executed. The equivalence only permutes storage coordinates and, for the orbit statement, message labels; not arbitrary information bases.

## originality

PASS

The length-eight existence witness and the general model/criteria are prior work. The supported addition is a sharp lower bound against all binary generators at (dimension,concurrency)=(3,3), the exhaustive set of optimal named generators and its orbit structure, and an admissible strongly-online selection at every optimum. The inspected exact static tables and service-family classifications do not establish it.

## value

PASS

Shortest length for small dimension and at least three active requests is an explicit prior research question. The first parameter beyond two active requests gives a meaningful model separator from the static length-six case. The complete list and the existence of a strong policy family for each optimum identify design options and resolve a model comparison exactly at the minimum, rather than merely reproducing an existing construction. No extension to longer lengths or other dimensions is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
