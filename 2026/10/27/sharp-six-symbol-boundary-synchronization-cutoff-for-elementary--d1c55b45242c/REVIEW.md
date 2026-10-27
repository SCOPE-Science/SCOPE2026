# Scientific review

## Correctness — PASS

The predecessor-pair graph uses four precisely defined states. Its output-letter transition is a non-deterministic set map, not an assumed deterministic reset action. Induction proves that each reachable nonempty subset equals the set of terminal pairs of all input blocks producing the observed output word. Hence a singleton is exactly the desired observation, and a fully closed 15-subset BFS decides both the shortest possible length and impossibility for all lengths. Reproduction of all 256 BFS classifications yields 24, 90, 72, 12, 4, 4, and 50 cases; the maximum six occurs only at Rules 37, 91, 164 and 218. A structurally different direct enumeration of input blocks matches all 32,256 checked output-word terminal sets through length six, and minimal lengths across the 256 rules. The unrestricted negative cases rely on closed finite-state reachability, not on short enumeration alone.

## Originality — PASS under available evidence

Actual indexed-record searches covered aliases for boundary-context synchronization, de Bruijn image-word synchronization, shortest reset words and the exceptional rule numbers. Closest records on road coloring, deterministic automata reset lengths, finite-period CA behavior, temporal traces and output-language entropy address different state maps or invariants. The complete original texts inspected for Kari (2002), Kisielewicz–Kowalski–Szykuła (2012), Fukś (2013) and relevant sections of Grigorchuk–Kogan–Vorobets (2021) did not state this 256-rule boundary-context census. The generic subset-search algorithm is prior art, and novelty is assigned **only** to this exhaustive sharp ECA-specific synchronization spectrum and its extremizers. Historical priority remains uncertain: unindexed comprehensive rule tables and a 2010 predecessor-counting paper whose full text was not obtained may contain an implicit equivalent result. The accessible comparisons did not supply a dominating theorem or identical catalog.

## Mathematical value — PASS

One-step preimage ambiguity and recovery of a boundary context are natural symbolic-dynamical properties of finite-window observations. The seven-part classification resolves the full classical elementary family, proves a sharp universal finite delay of six when synchronization is possible, isolates a four-rule extremal class, and distinguishes 50 rules for which no length can succeed. This is an exact natural invariant of a canonical complete family, not an arbitrary numerical slice or routine parameter increment. No analogous higher-radius theorem is asserted.

## Scope and review status

The proof uses a completely specified finite-state computation, reproducible without external packages. This is not a claim of external certification; incomplete access to some historical sources leaves residual novelty risk.

Self-review: passed. Independent audit: not yet performed.
