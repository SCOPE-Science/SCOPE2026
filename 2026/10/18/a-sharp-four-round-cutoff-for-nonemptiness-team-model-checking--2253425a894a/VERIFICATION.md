---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For exact occurrence-labelled, odd-bottom-up/even-top-down Anttila–Kontinen–Yang algorithm, established flat support F_u and existential NE obligations W_u by structural induction over literals, constants, conjunction, lax split. Formula satisfaction iff S subset F_root and S meets all NE witness sets. After first and second updates the labels are f1(u)=T cap F_u and f2(u)=T cap F_u cap C_u (contexts accumulate flat support of siblings at conjunctions). If every nonempty-team obligation survives, stage three preserves stage two and thus all later stages. Otherwise a null NE leaf at update three propagates null up to root, and top-down fourth update propagates null globally. Empty input team follows separately, null is distinguished from empty actual subteam; phi=NE and BOT conjunction with singleton T forces f3 not equal f4. The direct two-pass context checker is O(|phi||T|) elementary operations on explicit teams. Read the actual bundled simulation/semantic verifier and reconstructed the inductive argument; finite tests do not prove unbounded depth.

## originality

PASS

The source paper Anttila–Kontinen–Yang 2025 explicitly says the same algorithm seems to converge by fourth iteration but identifies that assertion as unproved and open; it supplies only polynomial iteration complexity. The new rigorous four-step universal and sharpness theorem settles that question and adds a flat-support witness checker. Prior Convex Team Logics characterizes expressibility, not this update count; original coNP entailment result is not re-claimed.

## value

PASS

Sharp constant-round termination resolves a specific published algorithmic gap; direct context check materially improves a polynomial iterative model checker for the natural fragment with nonemptiness, even though previous polynomial-time decidability was known. The precise best possible fourth round has conceptual content beyond mechanical substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
