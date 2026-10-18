# Scientific assessment

## Correctness — PASS

The precise claim concerns ordinary overlapping contiguous-factor occurrences in an explicitly constructed binary length-\(n\) word. A cyclic de Bruijn word exists for every positive order by an Eulerian circuit; its length-\(d\) phase blocks are unique. The least number of positions in a residue class among \(n-\ell+1\) consecutive starts is \(\lfloor(n-\ell+1)/p\rfloor\). The cutoff \(\ell\le\lfloor(n-p+1)/(p+1)\rfloor\) forces this count to exceed \(\ell\), yielding \(p(L-d+1)\) distinct qualifying factors. The parameter choice for every \(n\ge64\) satisfies \(L\ge d\) and gives the claimed square-root-logarithm error term by explicit inequalities. The published \(n\)-factor upper bound supplies the complementary inequality. The verifier's finite counts agree, but are not treated as the general proof.

## Originality — PASS within the consulted record

Bals et al. (ESA 2026, Theorem 1 and Proposition 6) proved the upper bound and an asymptotically matching example **on an alphabet of growing size**. Their construction needs \(r\) distinct symbols at length \(r^2\), so the existence of fixed-binary asymptotically matching witnesses is not an implication of that proposition. The binary de Bruijn construction and explicit for-all-length bound fill that narrower but structurally different gap. Published-search results on ordinary distinct-substring complexity and string attractors concern different parameters. No matching statement was located in the searched published record, but searches cannot establish global priority, and an unindexed equivalent remains a risk.

## Value — PASS

The 2026 counting-index framework stores exceptional factors and needs a linear worst-case allowance. Its reported tightness witness uses alphabets expanding with input length, whereas most deployed text indexes handle fixed alphabets. Demonstrating that the coefficient one remains sharp even for binary strings rules out reducing the combinatorial allowance by a fixed multiplicative factor merely by restricting alphabet size. The explicit de Bruijn construction has precise length and frequency cutoffs and is an easily reproduced stress-test family; no optimal second-order deficit is claimed.

## Closest literature and limits

Bals et al., *Text Indexing: From Reporting to Counting*, ESA 2026, DOI 10.4230/LIPIcs.ESA.2026.68, full published PDF pp. 1–4 inspected for Theorem 1, Proposition 6 and its proof; targeted searches of the complete document found no binary/de Bruijn sharpness construction. Tesler, *Multi de Bruijn Sequences*, arXiv:1708.03654, supplies standard combinatorial context; only its abstract was checked, so no whole-document exclusion is claimed. Bernardini et al., *Indexing Strings with Utilities*, arXiv:2504.05917, treats top-\(K\) frequent substring indexing, not the equality of factor length and occurrence count; comparison used abstract-level material. The rate \(O(\sqrt{n\log n})\) need not be optimal; no assertion is made about \(n<64\) or random texts.

Self-review: passed. Independent audit: not yet performed.
