---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The cited source fixes the reset threshold and unique target of every shortest word. Reading a shortest word backward from that target and rotating the preimage set converts the two letters into a deterministic scheduled Boolean system: \(b\) is a no-op, while \(a\) copies the membership bit at offset \(q-p\). Coprimality makes that dependency map one cycle. The first possible creation times are \(1,1+p,\ldots,1+(q-2)p\); missing any such forced copy delays it by a full \(q>p\) steps and makes completion by the known threshold impossible. Exactly \(q-1\) positions therefore force \(a\). Before the last creation the sole present state whose dependency successor is absent is the initial endpoint, producing exactly \(p-1\) forced \(b\)-positions. At every other position the compared bits agree, so either letter has identical reverse action and the choices are independent. Subtracting the forced positions from \(L=pq-2p+1\) leaves \((p-1)(q-3)\) free bits, giving exactly \(2^{(p-1)(q-3)}\) shortest reset words. The actual verifier exhaustively checks all coprime pairs through \(q=13\) and symbolically checks the schedule through \(q=100\); these checks support but do not replace the all-parameter schedule proof.

## originality

PASS

Gusev and Pribavkina define this exact Wielandt-type automaton, prove the same reset threshold, prove the target of every shortest word, and exhibit an optimal word, but the inspected primary text does not count all shortest reset words. Exact current Resultary search for the family and multiplicity returned no same-result finding among the leading results; the closest hits concerned other synchronizing-automaton thresholds or general shortest-word algorithms. The multiplicity is not implied by knowing one optimal word or the threshold: it requires identifying every forced reverse-preimage event and proving that all remaining letters branch independently.

## value

PASS

The Wielandt-type automata are a standard slowly synchronizing family, and shortest-word multiplicity is a natural refinement of reset threshold: it measures how rigid the extremal synchronization mechanism is. The exact exponential count for every coprime parameter pair is structural, not a finite census, and the reverse-preimage schedule is reusable for related two-cycle families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
