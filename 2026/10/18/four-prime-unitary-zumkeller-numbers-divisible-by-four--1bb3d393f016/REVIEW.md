# Review of the four-prime unitary Zumkeller classification

## Correctness — PASS

The proof specifies the exact domain \(\omega(n)=4\) and \(4\mid n\), proves the universal necessary inequality \(\sigma^*(n)\ge2n\), and enumerates **all** prime-power configurations meeting it. Its maximum-product estimates exclude \(\nu_2(n)\ge4\) and isolate one \(\nu_2(n)=3\) case. At \(\nu_2(n)=2\), exhaustive exponent restrictions yield exactly the infinite \(60r^e\) family and four isolated \(84r\) values. The displayed partition witnesses suffice for both unitary Zumkeller and unitary half-Zumkeller properties. The actual bundled `verify.py` reproduces every candidate and proper-partition result through \(100000\), and separately checks the finite witness sums. Limits: the computation is finite; the general theorem depends on the printed inequalities and witness formulas.

## Originality — PASS within inspected sources

The July 2024 originating article supplies the unitary-divisor definitions, abundance necessity and coprime multiplication construction, but its full relevant sections give only partial prime restrictions and state the half-Zumkeller conjecture as open. The ordinary-divisor 2020 study does not classify the unitary variant. Public OEIS tables A290466 and A290467 list examples, not a necessary-and-sufficient infinite formula; known three-prime-support statements do not encompass the four-prime theorem. Searches using 'four distinct prime factors', 'divisible by four', the infinite family and each exceptional integer revealed no equivalent covering theorem. Risk: an unindexed or inaccessible earlier proof could exist, so this self-review is not independent novelty certification.

## Value — PASS

The primary 2024 article explicitly motivates further prime-factor classifications and proposes the even unitary half-Zumkeller conjecture. This theorem fully resolves an infinite, nontrivial four-prime layer selected by its natural \(2\)-adic valuation and turns an abundance necessary condition into a sufficient one. It also proves the half-partition property throughout this layer, with sharp \(2\)-adic cutoff and complete exceptions, rather than merely listing the first few values. The omitted odd-valuation-one four-support case and larger support sizes remain open within this analysis.

## Closest literature and limitations

B. Das, “On unitary Zumkeller numbers,” *Notes on Number Theory and Discrete Mathematics* 30 (2024), 436–442, DOI 10.7546/nntdm.2024.30.2.436-442 (especially Propositions 2.1–2.7 and Conjecture 3.1); P. Mahanta, M. Saikia, D. Yaqubi (2020), DOI 10.1016/j.jnt.2020.05.003; OEIS A290466 and A290467. The proof does not claim the full even conjecture. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
