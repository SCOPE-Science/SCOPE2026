---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For crisp directed R-path height<=H (paths allow repeat so no cycles), modal-height truncation T_b replaces modal subformulas by truth constants at bound zero and decreases budget under modalities. Induction on formula and remaining height gives e(w,phi)=e(w,T_b phi) at worlds of height<=b. Hence at every successor of world height h the unrestricted operand agrees with depth<=h-1 transform; H-witnessing attains its extrema, giving full witnessing. Explicit height-exactly H countable model has infinitely branching root to chains of H-1 edges; leaf p=1/n, all other p=1. Every depth<=H-2 operand is constant across root successors, while root inf of Box^(H-1)p equals0 never attained: (H-1)-witnessed but not H-witnessed. Finitely branching and globally finite atomic ranges ensure all infima/suprema attained. Covers H=0 and H=1 boundary cases, with infinite nonattainment proved analytically rather than via finite truncation.

## originality

PASS

Witnessed crisp Gödel models and finite-model completeness are previously published; general bounded-depth modal locality is classical. The exact model-level height-H all-formula criterion and explicit one-variable sharp (H-1)-witnessed countermodels were not seen in inspected prior work. This narrow structural boundary is assessed at the same C/O/V bar, with adjacent model-theoretic equivalence risk.

## value

PASS

The precise finite check depth required to certify full witnessing over bounded-height infinite branching frames is a useful semantic invariant. Sharp countable countermodels isolate why infinite branch values, rather than mere finite height, cause failure; this is motivated semantic boundary work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
