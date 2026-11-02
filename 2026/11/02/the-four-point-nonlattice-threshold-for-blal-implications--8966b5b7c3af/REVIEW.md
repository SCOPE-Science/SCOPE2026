# Scientific review: BLAL implication nonlattice threshold

## Correctness — PASS

The exact domain is all binary operations on bounded chains satisfying every equation E1–E11 and quasi-equation QE1–QE3 of Cornejo et al. (2026), Theorem 16. Proposition 21 proves that the fixed upper triangle is top-valued; the only finite free parameters are strict-lower-triangle entries. An exhaustive standard-library program checks 1, 1, 8 and 729 candidates at sizes 1, 2, 3 and 4 respectively. It yields 1, 1, 4 and 25 admissible operations, and a four-element list at size 3 totally ordered pointwise. On size 4, the four explicitly supplied valid tables have a common forbidden pointwise bound M. E8 fails on M at (3,2,0), so no join of C,D and no meet of A,B can exist. The symbolic order argument is complete once the finite certificates are established. No inference from finite tests to arbitrary sizes is made.

## Originality — PASS within inspected evidence

Cornejo et al. (2026), Theorem 16 and Proposition 21, establish the BLAL semantics and order characterization, not this exact finite census or poset obstruction. Section 5 of Cornejo–Medina–Ramírez-Poussa (2021) establishes lattice structure for residuated adjoint pairs and triples, a narrower class; its positive closure is not applicable to general BLAL operators. Searches for named BLAL algebra expansions, finite chain implication tables, pointwise orders, lattice bounds, and synonymous Rasiowa implications did not disclose an explicit covering theorem. This is a bounded novelty assessment, not a claim of exhaustive historical priority. Older results under other implication or operator terminology remain a residual risk.

## Mathematical value — PASS

The phenomenon is a sharp structural boundary in the **natural pointwise order of admissible truth-functional implications**, unlike an arbitrary finite statistic. Three-valued chains have only four operations forming a total order, whereas four-valued chains already admit no join or meet for specified pairs. The witness shows why lattice-aggregation results for residuated subclasses cannot be extended automatically to the broader algebraizable semantics, and makes the precise failure independently reproducible.

## Relevant sources and limitations

Cornejo et al., *Bounded and multi-adjoint lattice algebraizable logics*, DOI `10.1016/j.ijar.2026.109682`, full original open-access 16-page paper, Theorem 16 (PDF p. 7), Proposition 21 and Example 22 (PDF p. 8). Cornejo et al., *Algebraic structure and characterization of adjoint triples*, DOI `10.1016/j.fss.2021.02.002`, original author manuscript, Section 5 (PDF pp. 23–30). The result does not establish an all-rank sequence or a classification for arbitrary lattices. Historical priority outside inspected material remains uncertain.

Self-review: passed. Independent audit: not yet performed.
