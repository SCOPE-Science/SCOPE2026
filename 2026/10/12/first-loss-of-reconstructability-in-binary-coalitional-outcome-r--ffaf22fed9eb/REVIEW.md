# Scientific review

## Correctness — PASS

The concrete invariant is defined for all coalitions and all fixed-action partial profiles, without upward closure. For one/two players, the two-by-two Boolean matrix classification accounts for all action-flip classes. At three players the explicit tables have the same eight coalition signatures but three and two positive entries, which cannot be made equal even under agent and outcome exchange. A standard-library exhaustive verifier checks all \(256\) three-player tables and independently computes action-flip representatives; its three counts are \(41\) signatures, \(46\) orbits and \(3\) ambiguous signatures, with orbit multiplicities \(2,2,4\). Burnside's independent orbit formula gives \(46\). Finite exhaustivity is sufficient because the theorem's exact census explicitly concerns this finite domain.

## Originality — PASS, with material residual risk

The full 2026 article *Inquisitive Action Logic*, Theorem 2.2, characterizes representability of individual-agent actual-effectivity systems, not this reconstruction of action classes from all exact coalition outcome ranges. Earlier state/path coalition effectivity models and the Stanford survey explain abstract game-representation nonuniqueness, predominantly for upward-closed powers, which is acknowledged as known rather than asserted new. Targeted search of possible cube-face-range aliases and the published mathematical database did not identify the 41/46 fixed-alphabet census. Wang's 2026 *Value Coalition Logic* explicitly studies the same type of coalition value-range hypergraphs, and its **full text could not be inspected**. An equivalent finite census there or in earlier combinatorics cannot be excluded; this is the leading remaining novelty risk. The audit records actual comparison queries, the source material inspected, and the statement-level distinctions.

## Value — PASS

Reconstruction of concrete action profiles from abstract exact coalitional observations is an important semantic question, particularly because exact non-monotone outcome sets appear to retain much more information than classic coalition powers. The smallest nontrivial binary action/outcome domain is fully classified: first loss of faithfulness at three agents, an explicit robust obstruction and exact collapse statistics. This provides a precise structural boundary rather than an arbitrary data table and does not purport to resolve general representability.

## Limits

Results are local and deterministic, with two actions per agent, two labelled outcomes and at most three agents for the census. Exact range families omit action multiplicity, which is essential to the negative result. The numerical classification comes from a fully enumerated 256-case certificate; the proof does not give a noncomputational generating formula for the 41 signatures. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.

