# Scientific review

## Correctness — PASS

The proof identifies the unique occurrence of each consecutive-one pair through its power-of-two gap. This forces the shared middle of a minimal absent word to contain at most one one, reducing all possibilities to exhaustive two- and three-one cases. Each remaining case is bounded by exact preceding/following zero-run lengths, including the one-sided initial boundary. The four families have both proper deletions present and themselves absent. The separate program compares direct factor-language minimal absent sets with the proposed sets for every length through 160, and passed. Finite verification is not a substitute for the all-length argument.

## Originality — PASS, qualified

The subword-complexity framework of Gheorghiciuc (arXiv:math/0512256v1) applies to increasing-gap words and gives factor counts, but does not in the inspected material assert their full minimal-absent factors. Pinho et al. (DOI 10.1186/1471-2105-10-137) give general minimal-absent methods for finite strings without a powers-of-two exact infinite-language classification. Mignosi–Restivo–Sciortino (DOI 10.1016/S0304-3975(00)00436-9) discuss forbidden-factor theory and Sturmian languages; the available abstract does not resolve this particular sparse language. Comparisons of the actual claims and corresponding mathematical research records found no established implication of the theorem. The uninspected full 2002 article remains a genuine historical-priority risk; absence from search results is not proof of novelty.

## Value — PASS

Minimal absent words are the antichain of shortest local obstructions determining a factorial language. The word is the standard lacunary binary automatic sequence with exponential support. The classification resolves its **entire** antichain, including asymmetric one-sided-boundary exceptions and the sharp geometric spike locations in its length spectrum. It refines subword-complexity information into explicit essential forbidden patterns, a natural invariant useful in language and anti-dictionary descriptions; no unsupported application theorem is asserted.

## Scope and limitations

Only contiguous factors in the one-sided infinite characteristic word are addressed. The computational check covers lengths through 160; the unrestricted conclusion follows from the direct proof. Full-text historical comparison is incomplete for one plausible reference. No independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
