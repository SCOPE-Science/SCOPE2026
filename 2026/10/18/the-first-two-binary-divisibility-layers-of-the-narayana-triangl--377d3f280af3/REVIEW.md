# Scientific review: binary Narayana valuation layers

## Correctness — PASS

The claim is for every dyadic cutoff \(L\ge1\) for valuation zero and every \(L\ge2\) for valuation one, with the exceptional first cutoff explicitly handled. The proof decomposes every Narayana row by parity into Kummer valuations of two ordinary binomial coefficients. Counting submasks yields exact geometric sums for all binary lengths; in particular, the two independent valuation-one contributions \(E\) and \(O\) each total \(3^{h-1}-1\) for \(h\ge1\). Both branches and all boundary indices were separately checked. The attached integer-only checker evaluates every entry of the first 127 rows from the defining formula, validates the per-row branch identities through index 256, and reproduces the first ten dyadic cutoffs. Finite replay is supporting evidence, not an infinite proof.

## Originality — PASS, qualified

Bóna–Sagan's fully inspected 2005 manuscript determines parity at individual triangle positions and says general prime-adic orders become complicated; it does not give the aggregate valuation-one formula. OEIS A335965 and Eu–Liu–Yeh are relevant to the known odd-entry layer, which is not claimed independently as novel. Pinheiro–Vascon–Craveiro (2026) work on central-column congruences, which do not determine the count throughout all rows. The exact integers in the valuation-one sequence coincide with OEIS A058809, but its listed interpretations do not establish the Narayana divisibility statistic. The full Eu–Liu–Yeh article was not available for inspection, so an implicit earlier general valuation result remains a priority risk; published-record searches did not identify one.

## Mathematical value — PASS

The result resolves a natural first nontrivial prime-power layer of the classical Narayana triangle, whose entries count Dyck paths with specified peaks. It refines the previously studied parity pattern to exact divisibility by two but not four across all entries up to a binary-length cutoff. The exact count and the limiting \(2/7\) proportion expose a persistent arithmetic distribution not determined by rowwise parity information alone. Dyadic cutoffs are forced by the binary carry structure, rather than an arbitrary numerical slice. The novelty and value are the *Narayana interpretation and all-length proof*, not novelty of the standalone integer sequence \(3^{L-1}-3\).

## Sources and residual risks

Closest primary source: M. Bóna and B. E. Sagan, *On divisibility of Narayana numbers by primes* (2005), https://arxiv.org/abs/math/0505382. Additional comparisons: S.-P. Eu, S.-C. Liu and Y.-N. Yeh, *On the Congruences of Some Combinatorial Numbers* (2006), https://doi.org/10.1111/j.1467-9590.2006.00337.x; OEIS A335965, https://oeis.org/A335965; G. F. Pinheiro, G. M. Vascon and I. M. Craveiro (2026), https://periodicos.ufs.br/ReviSe/article/download/23795/18603; OEIS A058809, https://oeis.org/A058809. The Eu–Liu–Yeh complete article could not be read, and independent assessment may locate a broader theorem. Only valuations zero and one are classified.

Self-review: passed. Independent audit: not yet performed.
