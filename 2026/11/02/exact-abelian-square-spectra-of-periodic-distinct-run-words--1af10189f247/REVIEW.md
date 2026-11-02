# Review of the distinct-run Abelian-square theorem

## Correctness — PASS

The circular adjacent-window lemma supplies the critical nonstandard step: with at least three unique-letter circular runs, equal Parikh vectors on disjoint consecutive arcs force both arcs to be monochromatic. Period reduction then turns every half-length into an explicit residue test. Full-period factors have distinct rotations, so counting starting residues gives distinct *strings*, not occurrences. Summing the available phases yields the exact increment. The boundary cases \(k=1,2,3\) are worked out separately, including the first/last run correction. A standalone independent literal-enumeration checker matched 997 cases and every half-length profile in those cases. These computations are finite checks and are not misrepresented as an infinite certificate.

## Originality — PASS (subject to residual literature risk)

Relevant primary texts were compared at theorem level: Fici–Mignosi–Shallit (2017) counts abelian squares in Thue–Morse and Sturmian words and proves general bounds; Sugimoto et al. (2017) gives algorithms to *locate* abelian squares in arbitrary RLE strings, not the present symbolic number of distinct factors in cyclic run powers; Simpson (2018) surveys extremal and circular-word problems; Fici–Puzynina (2022) surveys the same literature. No matching fixed-family closed formula or two-power law was found in inspected portions. The closest accessible earlier run-power Parikh-factor formula concerns counts of Parikh vectors for single factors, not the adjacent-window equality relation. Their distinction is witnessed by run vectors \((4,1,2)\) and \((1,4,2)\), which agree in the former statistic but yield square totals \(7\) and \(5\) for two copies. Searches can miss equivalent specializations, especially in earlier periodic-word enumeration literature.

## Value — PASS

Distinct Abelian-square *strings* constitute a natural structural invariant of compressed periodic input, different from the number of occurrences or the number of Parikh classes. A full length-by-length classification and exact two-period increment yield a closed benchmark for Abelian-square reporting algorithms. The phase-sensitive boundary correction and the distinction between nonbinary and binary cyclic runs make this more than a straightforward rescaling of a known general bound. No downstream theorem is claimed or required.

## Closest literature and scope boundaries

- Fici, Mignosi, Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948, §§3–5.
- Sugimoto et al., *Computing Abelian regularities on RLE strings*, arXiv:1701.02836, §4, especially Theorem 2.
- Simpson, *Solved and Unsolved Problems about Abelian Squares*, arXiv:1802.04481, discussion of distinct and circular-square counts.
- Fici and Puzynina, *Abelian Combinatorics on Words: a Survey*, arXiv:2207.09937, §4.3.

The result excludes two-run periods and periods whose symbol repeats in more than one cyclic run. No independent validation or comprehensive historical originality guarantee is asserted.

Self-review: passed. Independent audit: not yet performed.
