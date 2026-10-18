# Scientific review

## Correctness — PASS

The ordinary block identity \(s_b(bq+r)=s_b(q)+r\), the carry congruence \(s_b(q+1)-s_b(q)\equiv1+2t\pmod{b+1}\), and the count of complete blocks in a long interval give sharp upper bounds. The odd-base starting interval and even-base carry witness attain the bounds. Equality forces a unique starting residue; checking the neighboring block residues gives necessary and sufficient carry-pattern classifications. An elementary Fourier digit-box argument supplies conditional digit-sum equidistribution, and the geometric tails allow exact limiting frequencies. A standalone verifier independently checks more than two million finite starting positions and explicit arbitrary-length witnesses. No finite search is used to infer an infinite upper bound or existence of natural density.

## Originality — PASS within inspected evidence

The Waterloo October 2023 published solution establishes the decimal maximum \(38\) for modulus \(11\) and gives the first instance; those assertions are prior work. The July 2022 Stack Exchange problem and answer cover the distinct decimal modulus \(8\) maximum \(14\). Both were inspected at the relevant argument and conclusion sections, not merely their abstracts. Neither gives the general odd/even-base threshold, necessary-and-sufficient description of every extremal interval, or the exact densities. Searches of mathematical literature and published mathematical-result records under the terms recorded in `AUDIT.json` revealed no equivalent theorem; non-indexed or unpublished prior generalizations remain possible. Abstract digit-sum equidistribution alone does not imply the extremizer classification or density without the carry analysis.

## Value — PASS

The modulus \(b+1\) is singled out naturally: each full base-\(b\) digit block covers exactly all but one digit-sum residue modulo \(b+1\). This produces a sharp base-parity transition in maximal run lengths, a complete arithmetic characterization of *all* rare extremizers, and their exact positive limiting frequencies for an infinite family of bases. In decimal the maximal runs have density only \(10000/122222222221\), measuring a genuinely sparse extremal phenomenon that the previously known single-case maximum does not quantify. The theorem does not purport to solve every modulus or general digital-sequence gap problem.

## Residual limitations

The literature search may miss unindexed or differently named generalizations, and independent verification has not yet been undertaken. The theorem's domain, proof, and computational checks are explicitly stated in the result.

Self-review: passed. Independent audit: not yet performed.
