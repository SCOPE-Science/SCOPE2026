# Scientific review: exact leading-bit uniformity for Pell residues

## Correctness — PASS

The recurrence matrix is explicit. The base congruence at exponent four is checked directly, and the squaring induction uses the exact fact that the fixed matrix \(B\) has even square. This yields \(\nu_2(P_{n+d}-P_n)=\nu_2(d)\) whenever \(4\mid d\). Within each index class modulo \(2^{k-r}\), this valuation identity makes the \(2^r\) values pairwise distinct modulo \(2^k\); all share the same residue modulo \(2^{k-r}\), so they exhaust that residue class. Counting classes proves the stated exact interval multiplicities for every permitted \(k,r\). Finite checks are supplementary only.

## Originality — PASS, with a named literature risk

The accessible primary literature inspected treats Pell sums, recurrence periods, and modular-period relations, not the full leading-bit distribution. The later Pell-prefix discussion states a one-bit toggle, while the present statement covers every \(r\le k-2\). The prior all-state cycle census concerns cycles of pairs, a distinct invariant. The 2015 Pell-period article was not fully inspected through a verified lawful OA/official route, and a broader 2-adic recurrence theorem could imply this result; those remain explicit risks rather than a claim of absolute priority.

## Value — PASS

Exact uniformity of every allowed leading-bit prefix is a natural and stronger statistic than the one-bit balance alone. The boundary \(r=k-1\) can fail, already at modulus \(16\), so the proven range has mathematical content. The result gives a concise structural explanation for a full-block digital distribution property of a classical recurrence and does not overclaim short-prefix equidistribution.

## Closest literature and limitations

The relevant comparison sources are the 2016 Pell-sum preprint, the 2016 open-access Pell-polynomial period paper, the 2015 Pell-period article record, the Pell sequence entry A000129, and a later discussion of Pell-prefix distribution. The 2015 article's full text remains an access limitation. The theorem is confined to \(0\le n<2^k\) and \(1\le r\le k-2\).

Self-review: passed. Independent audit: not yet performed.
