# Scientific review: exact three-factor deletion universal-word probability

## Correctness — PASS

The claimed all-length value is supported by a directed Euler-trail equivalence and an exhaustive symbolic partition of compatible deleted triples: four balanced triples, and unbalanced subclasses of \(N-2\), \(N-4\), \(4N-16\), and \(4N-28\), where \(N=2^n\). This gives \(10N-46\) degree-compatible triples. The super-edge-connectivity result of Xu and Lü reduces all residual-graph disconnections to constant vertices; direct local divergence analysis leaves five failures per constant vertex, subtracting ten. The standalone verifier independently checks every deleted triple for \(4\le n\le7\). Its finite enumeration cannot replace the infinite symbolic argument. The nonstandard connectivity lemma is explicitly attributed and its parameter regime \(m=n-1\ge3\) verified.

## Originality — PASS (best knowledge, residual risk)

The closest direct predecessor is Chen–Kitaev–Sun (arXiv:1908.01116, 2019), which defines these exact universal-word probabilities, derives general lower bounds and exact \(s=2\) results, and tabulates small binary cases. Its tabulated \(n=4,s=3\) probability \(13/70\) is a special instance, while its theorems do not imply the count for every \(n\ge4\). A prior exact three-deletion *cyclic* enumeration counts balanced Euler circuits rather than the present linear semi-Eulerian case and does not entail the latter. The published Xu–Lü theorem supplies only connectivity, not this deletion-triple enumeration. Searches for equivalent terminology (linear de Bruijn universal words, three forbidden factors, Euler-trail edge deletion, \(P_{\mathrm w}(n,2,3)\)) found no matching all-length result. An unindexed equivalent enumeration or an overlooked implication in broader graph-flow literature remains possible; no independent priority certification is claimed.

## Value — PASS

The result solves a naturally posed exact probability question left at a lower-bound stage in its guiding paper: after exactly three deletions over the binary alphabet, when does a linear universal word survive? It provides both the first all-length expression for this slice and a structural decomposition of ten exceptional connectivity failures. The sharp contrast between the degree-compatible count and realizable count is mathematically explanatory and reproducible, rather than a routine parameter increment.

## Sources and limitations

The original research question and exact \(s=2\) scope come from Chen, Kitaev and Sun, arXiv:1908.01116, Sections 1, 3 and 4. The necessary nonstandard edge-connectivity theorem is Xu and Lü, *Ars Combinatoria* 87 (2008), Corollary 1. The claim is limited to three distinct deleted binary words with factor length at least four and exact-once linear coverage. There is no formula here for larger alphabets, cyclic coverage, multiplicity of witnesses, or other deletion counts. The verifier supports only the stated finite checks, not an independent infinite proof.

Self-review: passed. Independent audit: not yet performed.
