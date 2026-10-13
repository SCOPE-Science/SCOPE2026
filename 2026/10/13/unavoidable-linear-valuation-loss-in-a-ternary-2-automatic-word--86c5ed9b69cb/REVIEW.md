# Scientific review: unavoidable valuation loss in a ternary automatic word

## Correctness

**PASS.** The theorem reduces to an exact geometric property of the occurring Parikh vectors: every two-letter side of the ternary Parikh triangle is realized at every factor length. The run description gives this without any finite-enumeration assumption. Ordering an arbitrary injective integral valuation and solving \(j\alpha=i\beta\) yields \(\lfloor n\gcd(\alpha,\beta)/\beta\rfloor\) disjoint collision classes, with quantifiers valid for every length. Noninjective weights fail at length one. The stated \(2\)-DFAO, factor-complexity bound, aperiodicity argument, and exact natural-sum count were independently reconstructed. `verify.py` checks finite examples, not the infinite theorem.

## Originality

**PASS, subject to ordinary priority uncertainty.** The closest source is Popoli–Shallit–Stipulanti, *Additive word complexity and Walnut* (arXiv:2410.02409v1), especially the explicit valuation question and its positive results for balanced words. Its Section 3 count bounds and Section 5 theorems do not force any loss for every valuation in a fixed ternary automatic word: choosing very widely separated weights defeats the elementary bound \(\rho_v(n)\leq n(\max v-\min v)+1\) at fixed \(n\), whereas the present theorem handles every fixed integer weight choice with a length-dependent collision. Shallit's *Abelian Complexity and Synchronization* (arXiv:2011.00453v3) treats bounded abelian complexity and synchronized Parikh-prefix counts and gives no comparable weighted obstruction. Searches for length-modulo-three automatic words, triangle-edge Parikh collisions, valuation equality, and stronger indexed classifications found no covering claim. The negative example is deliberately not described as the first negative example for arbitrary infinite words; general full-language examples have an immediate larger-complexity obstruction. An equivalent example under different terminology cannot be ruled out.

## Value

**PASS.** It marks an exact alphabet threshold and exhibits failure of valuation preservation within automatic words of linear factor complexity, beyond the easy quadratic Parikh-vector pigeonhole examples. The collision lemma gives a quantitative loss at **all sufficiently large lengths for every fixed valuation**, while \(\rho_v(n)=2n+1\) gives an exact nontrivial complexity for canonical weights. It complements the balanced-word positive theorem with a concrete sharp boundary rather than an arbitrary finite computation.

## Closest literature and limitations

The primary reference is arXiv:2410.02409v1, Sections 3 and 5; related automatic-sequence abelian complexity is arXiv:2011.00453v3. Only integer weights are covered; the example is not uniformly recurrent, and its full abelian complexity is not claimed. The proof does not settle classification of all automatic words admitting a preserving valuation. The independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
