---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For any epsilon-free, single-initial NFA recognizing precisely m+kp unary lengths, an accepting run with a repeat gives a repeatable directed simple cycle of even length d divisible by the eventual period p, yielding at least lcm(p,2) states. The shortest accepting run length m must be simple. If p is odd the accepting run of length m+p is also simple, because removing a nonempty repeated even closed walk divisible by p removes at least 2p letters and contradicts minimality of m. Thus odd p requires at least max(2p,m+p+1) and even p at least max(p,m+1). A directed path of t=max(0,m-p+1) edges into an even cycle of length l=lcm(p,2), accepting offsets e=m-t (and e+p for odd p), achieves exactly max(l,m+l-p+1) states and the required language. Underlying simple graph is cactus, including l=2 as a single undirected edge with reciprocal arcs. The source RESULT.md literally contains {claim} rather than the theorem in its Finding section: a full replacement RESULT.md with explicit quantifiers, complete proof and scientific scope has been staged and independently reassessed.

## originality

PASS

The general 2026 theorem proves existence of an equivalent bipartite-cactus NFA for any regular language, without computing minimal state count; the exact parity-sensitive formula over all p>=1,m>=0 is an independently useful restriction-specific state-complexity refinement. Originality is best-of-knowledge, with an explicit risk that an equivalent result may be known under unary automata with alternating state parity.

## value

PASS

State complexity under a bipartite cactus restriction is a natural quantitative question arising directly after a recently established universal existence theorem. The complete formula for a standard infinite family of unary arithmetic-progression languages locates a sharp parity-dependent obstruction, including how transient delay forces additional states. The exact cost is useful as a first benchmark for structural automata minimization. This is a motivated state invariant, not just a trivial renaming of the ordinary unary DFA bound: odd periods require a simple length-(m+p) accepting run.

The dated certificate retains the supplied scientific assessment, sources and limitations.
