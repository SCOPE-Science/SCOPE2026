---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For nonempty S in a tournament, internal arcs give |F_i(S) intersect S|>=|S|-1. For |S|>=2, the forward/backward neighbor image is terminal in its own direction: each omitted vertex points to/receives from a survivor. When direction switches, all vertices outside the previous terminal set and all but at most one inside are reached, giving n-1. Singleton terminal sets are necessarily global sink/source; the same-direction step that would empty them violates the run condition. Full induction on arbitrary length uses terminality and n-r, with transitive tournament attaining all r<n. The clique lower language follows from each orientation containing an oriented K_n; a proper n-coloring gives an increasing-color orientation ruling out n-runs. The run GF and Myhill–Nerode suffix distinguishability give exactly 2n complete DFA states. Independently exhaustively explored the endpoint powerset/run product for ALL 1,098 labeled tournaments with n=2..5, including arbitrarily long legal words per fixed n; finite tests do not establish general n.

## originality

PASS

The initiating 2026 Pujol paper defines all-vertices-initial graph automata and remanent orientation languages, and already connects chromatic number to all-forward walks. The K_n run-language statement alone is an elementary consequence of the setup and is not claimed as new. The substantial survivor is a sharp n-r surviving-endpoint inequality uniform over ALL tournaments and direction changes, with extension to every graph having omega=chi and exact DFA enumeration. Pujol full text was not available in this run; its abstract plus source self-review description do not justify claiming complete noncoverage, so a targeted primary-text priority risk remains.

## value

PASS

The endpoint count quantitatively measures resilience to adversarial orientation and arbitrary alternating walk directions; switching restores nearly all endpoints regardless of history. The omega=chi consequence and exact automaton complexity give an infinite natural graph class, not an arbitrary finite instance. Sharpness and all-length quantifiers make the bound independently reusable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
