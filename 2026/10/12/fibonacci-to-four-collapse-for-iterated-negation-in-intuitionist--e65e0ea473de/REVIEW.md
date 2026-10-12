# Self-review

## Correctness

PASS. The full initial table for the negation tower is governed by a three-state linear recurrence read directly from the source's negation multioperation. The atomic-value restriction supplies the base vector \((1,0,1)\), giving the exact Fibonacci distribution. The support condition then has a complete parity-based analysis: one deletion round leaves exactly the rows with a single initial \(\mathbf U\)-block, and the second leaves only four explicit patterns.

The standalone replay independently generates and prunes finite tables and agrees exactly with the symbolic classification.

## Originality

PASS with residual risk. The primary paper states the general upper bound \(2^{|sub(\alpha)|}\), emphasizes that table size depends on subformula shape, and gives the deletion procedure, but it does not state the negation-tower profile. Its full text contains no occurrence of "Fibonacci" or "iterated negation." Targeted literature and mathematical-result-index searches using the exact source, negation-tower aliases, initial-row terminology, Fibonacci formulas, and golden-ratio formulations did not locate an equivalent result.

The result is a concise derived specialization of published ingredients, so an unindexed observation remains possible.

## Value

PASS. Pure iterated negation is the simplest family in which formula depth grows without increasing the number of atoms. It therefore directly tests the source's observation that one-variable formulas can still generate large non-deterministic tables. The exact \(F_{n+3}\)-to-\(4\) profile sharply separates branching in the initial semantics from the effect of support refinement and supplies a useful benchmark for implementations and further complexity analysis.

## Closest literature and limitations

The closest source is Leme--Coniglio--Lopes, arXiv:2308.13664, which provides all semantic ingredients and the general complexity bound. No inspected source supplied the exact iterated-negation recurrence or final four-row normal form.

The theorem does not extend automatically to formulas containing implication, conjunction, or disjunction, and it does not claim that an implementation explicitly materializing the initial table runs in constant time or space.

Self-review: passed. Independent audit: not yet performed.
