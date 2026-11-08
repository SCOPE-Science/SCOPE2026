---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The mod-3 square is nonzero indicator, so d_i=b_{i-r}; sum around any period gives Z divisible by 3 and at least one zero per complete 0->1->2 circuit, leaving only Z=3 and Z=6 for m<=9. The one-circuit support forces m=4. Remaining 77 six-run compositions at lengths 8,9 are exhaustively testable. An independently written literal enumeration over all 3^m primitive words and m lag residues for m=1..9 produced only (1,0):1,(4,2):4,(4,3):4,(9,4):9,(9,6):9. Thus arbitrary k reduces rigorously to residues.

## originality

PASS

Qualified best-knowledge original contribution; prior tools and claimed antecedents are explicitly excluded. Finch addresses the distinguished initial orbit and four-periodic patterns; this theorem classifies all primitive short cycles regardless of initial state.

## value

PASS

The finite cutoff nine is motivated by the gap after the known period four and a reported nine-cycle; excluding all intermediate lengths for every lag and finding exactly two lag residue families is a natural exact finite cycle classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
