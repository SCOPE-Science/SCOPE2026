---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

With b a cyclic permutation and c collapsing exactly {0,1}→2, every rank drop uses effective c, and after any c state 1 is missing, forcing at least one b between successive effective c uses. Thus deficiency s costs at least 2s-1 letters and equality forces the unique word c(bc)^(s-1). Its holes follow a direct induction: {1,3,...,2s-1} until the final odd-parity step, when odd n additionally loses 0. The next b sends the surviving set into positions omitting 0 or 1, so the following c is ineffective; uniqueness of any would-be bound-attaining word implies λ_n(ceil(n/2)+1)>2ceil(n/2)+1 for n>=4. Independent exhaustive subset BFS on n=3,...,10 reproduced every early unique optimum and strict next threshold. Finite data are corroboration; the universal lower and upper bounds use the hole induction.

## originality

PASS

The 2010 Wielandt construction and 2019 minimum-rank study establish the reset threshold and general derived automata, not exact intermediate-rank thresholds inside W_n with unique words and first saturation boundary. Related Resultary profiles are for Černý, D-prime, H, bactrian, and other distinct transition structures. No dominating theorem or exact W_n early-rank table located, but an older elementary unpublished observation remains possible.

## value

PASS

Early compression costs and uniqueness are natural combinatorial invariants for a canonical slowly synchronizing automaton; the proof identifies a full half-range regime and the precise failure boundary with a structural hole-dynamics argument, useful beyond reset-threshold alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
