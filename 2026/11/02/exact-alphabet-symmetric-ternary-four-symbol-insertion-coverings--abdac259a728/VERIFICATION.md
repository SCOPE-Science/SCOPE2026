---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For length-four codewords over the labelled ternary alphabet, global S3 relabelling yields exactly 14 word orbits, one constant size-three orbit and thirteen nonconstant size-six orbits. Each of 41 target length-five orbits imposes a nonempty incidence-mask intersection on a selected source-orbit subset; constant target words force the constant source orbit. An independent from-scratch Python complete orbit enumeration counted no coverings for r=0,1,2,3,4,5 selected nonconstant orbits, and exactly 37 coverings for r=6 (total size 39). Reversal fixes five of those 37 and pairs the remaining 32, giving exactly 21 equivalence classes. It directly checked that all 243 length-five targets have a deletion yielding one of the 31 explicitly supplied unrestricted codewords, so symmetry penalty >=8, without asserting 31 unrestricted optimality. This is a finite exhaustive proof because the orbit equivalence and the 14/41 incidence parametrization are exhaustive; it is not inference from a sample. Independently computed counts agree with source Python/C++ algorithm descriptions.

## originality

PASS

The relevant literature studies general insertion-covering bounds and asymptotics, or a shorter source length, and a use of the term symmetric for coordinate permutations rather than global alphabet relabelling. The exact length-four ternary global-S3 minimum 39, number 37 and reversal count 21 were not found in Resultary or primary texts inspected. This is a bounded best-of-knowledge priority judgment.

## value

PASS

The finite extremum and complete 37-solution classification answer a natural symmetry-constrained error-covering problem, and the 31-word unrestricted witness demonstrates a provable cost of symmetry. The exact finite invariant is independently useful despite no claim about unrestricted global optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
