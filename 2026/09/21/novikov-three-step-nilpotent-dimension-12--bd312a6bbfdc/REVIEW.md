# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The displayed 12-dimensional algebra is a central quotient of the Burde--Dekimpe--Vercammen 13-dimensional Lie algebra, because the quotient relation is

\[
x_{13}=-2x_9-2x_{10}+2x_{11}.
\]

Substituting this relation into the three brackets containing `x13` gives exactly the new bracket table. Since the killed vector is central, the Jacobi identity is preserved. The lower-central series has dimensions `12, 8, 4, 0`, so the quotient remains three-step nilpotent and its abelianization has dimension four.

The nonexistence proof uses only necessary identities for a Novikov structure. Exact rational elimination of the lower-central-series ideal constraints, the commutator relation, the cyclic Novikov identity, and the standard operator identity leaves 50 free variables. Without imposing any further choice of those free variables, the `(11,2)` entry of `[R_2,R_3]` reduces identically to `-1/4`. This contradicts the defining commutation of right multiplications. `artifacts/verify.py` reconstructs the full exact calculation with standard-library rational arithmetic and asserts each intermediate rank.

The computation was also checked against the 13-dimensional source calculation during review: the same elimination scheme reproduces the source paper's counts of 1421 forced zeros, then 352, 156 and 210 further independent linear eliminations, leaving 58 variables, and recovers a `1/8` right-commutator contradiction. This is a consistency check on conventions and indexing, not an independent audit.

## Originality — PASS, to the best of our knowledge

The primary 2008 paper gives a 13-dimensional four-generated three-step nilpotent counterexample and emphasizes that three generators always suffice for existence. Searches were made for exact and synonymous formulations involving three-step/3-step nilpotent Lie algebras, four generators, absence of Novikov structures, dimensions 12 and 13, and central quotients of the Burde--Dekimpe--Vercammen example. Accessible later expository material still reproduces the 13-dimensional example. Vercammen's 2013 doctoral work also describes the four-generated three-step counterexample line.

No source located in these searches gives the 12-dimensional quotient above or another 12-dimensional three-step nilpotent counterexample. No overlapping SCOPE record was found for Novikov structures, the 2008 source example, or this central-quotient construction.

Residual risk remains: the literature on Novikov structures is dispersed, and an unindexed thesis, note, or differently phrased classification could contain a smaller example. The result therefore makes no minimality claim and states originality only to the best of our knowledge.

## Value — PASS

The result improves a longstanding explicit dimension bound in the first known obstruction family: a standard 13-dimensional example survives a carefully chosen one-dimensional central quotient. It also supplies a short algebraic certificate of nonexistence, with the final obstruction concentrated in one entry of one right-multiplication commutator. The construction is reusable for testing further central quotients and the unresolved dimension-at-most-11 range.

## Sources inspected

- Burde--Dekimpe--Vercammen (2008), including Proposition 3.3 and the full operator-elimination proof: https://arxiv.org/abs/0705.1316
- Burde--Dekimpe (2006), for the preceding existence/nonexistence context: https://arxiv.org/abs/math-ph/0502008
- KU Leuven record for Vercammen's 2013 dissertation: https://www.kuleuven.be/doctoraatsverdediging/fiches/3E07/3E070097.htm
- Later expository material located by targeted searches that continues to state the 13-dimensional example.

## Limitations

- No minimal dimension is claimed.
- The proof is stated in characteristic zero.
- The decisive elimination is computer-assisted, although it is exact and accompanied by a compact hand-checkable final certificate.
