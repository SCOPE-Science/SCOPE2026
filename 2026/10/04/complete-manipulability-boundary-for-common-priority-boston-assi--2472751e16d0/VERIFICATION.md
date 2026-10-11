---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

With common priority \(1\succ2\succ3\), student 1 always receives her sincere first choice and cannot profit. If student 2's first choice differs from student 1's, the two high-priority students permanently occupy distinct schools and no profitable unilateral deviation remains. When both first choose \(A\) and student 2 ranks \(A\succ X\succ Y\), case analysis on student 3's first two choices gives exactly the two bad families stated in the package; the vulnerable student moves from sincere rank three to rank two by exactly the two reports with \(X\) first. An independent exhaustive implementation over all \(216\) truthful profiles and all false reports confirmed exactly \(36\) bad profiles, \(36\) vulnerable student-profile pairs, \(72\) profitable reports, the vulnerable-priority split, and zero two-student events.

## originality

PASS

The foundational Boston paper defines the mechanism and proves/illustrates its lack of strategy-proofness; later work characterizes priority or capacity domains where Boston becomes strategy-proof. Those theorem-level results establish susceptibility or immunity, not the exact profile-level geometry for one fixed three-by-three common-priority market. Targeted web and Resultary searches found no prior statement of the \(36\)-profile census, the exact vulnerable reports, or the six school-relabeling classes.

## value

PASS

Immediate acceptance is a canonical school-choice mechanism, and a common priority is a natural benchmark. The theorem completely resolves the smallest balanced square common-priority market where manipulation appears, including exact prevalence, unique vulnerable student, profitable reports, and symmetry classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
