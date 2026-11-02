# Scientific review

## Correctness — PASS

The cyclic predecessor criterion is precisely a nonzero diagonal in the four-pair Boolean transfer product. Every one of the four classical forbidden words yields the zero relation, proving necessity. The 13-state suffix-prefix avoidance automaton gives a canonical closed path for every cyclic avoiding word. Exact breadth-first closure of the product of this automaton with the 4-by-4 Boolean relation state, with path length capped at two, checks every possible returning cycle and proves period-preserving preimages for all lengths at least two. The one-cell exception follows immediately from the local truth table. The same 13-state integer transfer matrix, with exact Newton identities rather than polynomial fitting, proves the rational generating function and spectral growth. A second brute-force implementation checked all input rings through length sixteen. `verify.py` reproduced `VERIFY_OK`.

## Originality — PASS (qualified historical priority)

Jen (1989) established the forbidden basis for **linear** one-step Rule-54 image words; that part is explicitly credited, not republished as new. Martínez–Adamatzky–McIntosh (2014) gave Rule-54 glider, de Bruijn and subset diagrams, plus specific Garden-of-Eden configurations, not an all-length periodic-image characterization or exact rational image census in the inspected sections. Salo (2022/2023) established general finite-state decidability and weak periodic lifting concepts; these do not calculate the stated Rule-54 all-ring boundary or enumerator. Specific research-record searches and direct comparison with the preceding Rule-184 and Rule-110 claims found no equivalent. The possibility of an unpublished or unindexed older period-count table remains; the attribution is not an independent historical-priority certification.

## Value — PASS

On a finite ring, membership in the bi-infinite image shift need not guarantee a predecessor of the same period. The theorem settles that issue at **every** ring size for a well-studied nonlinear cellular automaton, isolates an exact one-cell obstruction, supplies a constant-size constructive feasibility criterion, and derives the exact finite-volume number and asymptotic rate of possible outputs. These are natural reachability and information-loss invariants, not a finite table extension or a routine recomputation of the already-known forbidden patterns.

## Verification scope and limitations

The finite-state closure is mathematically exhaustive for arbitrarily long cycles because the complete relation and suffix states are retained. The length-sixteen direct census is not itself an all-length proof. We did not resolve multi-step image sets, precursor multiplicities, or the possibility of a historically prior equivalent result in less accessible sources.

Self-review: passed. Independent audit: not yet performed.
