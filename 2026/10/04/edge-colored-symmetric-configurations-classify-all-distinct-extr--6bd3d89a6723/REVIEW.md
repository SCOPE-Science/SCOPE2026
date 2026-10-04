# Same-model review

## Correctness
**PASS.** For two composition-\(\llbracket1^w\rrbracket\) words, the exact distance identity is \(d_H=2w-r-t\), where \(r\) is support intersection size and \(t\) counts equal nonzero symbols inside that intersection. Thus distance at least \(2w-1\) forces \(r+t\le1\). This gives the per-coordinate degree bound \(w\), and equality in the global incidence count forces a symmetric \(n_w\) configuration. The symbols are a proper Levi-graph edge-coloring. Conversely König's line-coloring theorem colors every \(w\)-regular bipartite Levi graph with \(w\) colors and yields a code whose pairwise distances are \(2w\) or \(2w-1\). The bundled verifier independently realizes the construction on \(PG(2,5)\).

## Originality
**PASS.** The closest primary coding source, arXiv:1008.1611, explicitly leaves \(A_7(33,11,\llbracket1^6\rrbracket)\) and \(A_7(34,11,\llbracket1^6\rrbracket)\) undetermined and records only \(N_{\mathrm{ccc}}(\llbracket1^6\rrbracket)\in[33,35]\). The closest configuration source proves the exact \(n_6\) existence spectrum but does not state a constant-composition coding correspondence. Targeted searches for the coding parameters, all-distinct composition, Levi graphs, symmetric configurations, and edge-coloring formulations returned no implication-equivalent indexed result. The residual risk is an older design/coding source using different terminology for the same bridge.

## Value
**PASS.** The bridge is not an arbitrary translation: it closes the only undetermined weight-at-most-six all-distinct case singled out by the 2010 coding tables, giving the exact threshold \(34\), and converts an entire equality problem into the established existence/classification theory of symmetric configurations. The structural correspondence also identifies the missing symbol assignment as precisely a bipartite edge-coloring, so every configuration in the known spectrum automatically supplies a valid code.

## Closest literature and limitations
Kaski–Östergård supply the line-size-six configuration spectrum; Chee–Dau–Ling–Ling supply the coding problem, upper-bound layer, and the unresolved \(33,34\) cases; Davydov et al. survey the configuration language and known spectrum. The result does not determine subextremal values at nonexistence lengths and does not enumerate code/configuration isomorphism classes. Originality remains subject to the possibility of an unindexed equivalent formulation in older design-coding literature.

Same-model review: passed. Independent audit: not yet performed.
