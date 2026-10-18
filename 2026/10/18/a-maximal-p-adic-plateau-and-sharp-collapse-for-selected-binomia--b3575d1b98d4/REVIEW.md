# Scientific review

## Correctness — PASS
The claim is restricted to primes \(p\), integers \(r\ge2\), and multipliers \(2\le q\le p^r+1\). The cyclic carrying lemma rigorously proves that every positive multiple of \(p^r-1\) has base-\(p\) digit sum at least \(r(p-1)\); digitwise complementation gives exactly \(r(p-1)\) for each row up to the sharp boundary. Legendre's formula then proves every selected coefficient has valuation at least \(r\), and the explicit selected coefficient at index \(m\) attains it. At the next row that same index has valuation zero. The executable arithmetic checks reproduce small instances using a different factorial-valuation method; no infinite inference rests on enumeration.

## Originality — PASS, with residual risks
The closest antecedents are Fairfax-Ball's upper bound and \(p^a+1\) least-row formula, Guo et al.'s cross-row GCD, the known uniform valuation/congruence for the **one** coefficient \(\binom{q(p^r-1)}{p^r-1}\), and Wu/McTague's fixed-index restriction family. A one-coefficient formula does not imply divisibility of all the other selected coefficients. The new comparison is made at the implication level: the simultaneous valuation lower bound across every index and sharp zero boundary are not supplied by the inspected results. Several published-finding corpus searches found no equivalent claim. Unindexed calculations and inaccessible full supplementary text remain residual risks, not proof of uniqueness.

## Mathematical value — PASS
The recently introduced least-extremal-row framework naturally asks how long maximal valuation can persist consecutively. In the structurally distinguished family \(m=p^r-1\), this theorem determines the entire, exponentially long initial plateau of rows—not merely a single best row—and its exact arithmetic stopping point. The collapse to zero rather than a smaller positive exponent is informative and arises from an exact digit-complement duality. A known single-coefficient congruence is explicitly acknowledged; the mathematical addition is the all-index uniform result.

## Closest literature and scope
See arXiv:2610.01328v1, arXiv:2606.22997v1, arXiv:2606.20940v2, and McTague (2017). The theorem does not assert a full GCD formula, values for later multipliers, or independent confirmation.

Self-review: passed. Independent audit: not yet performed.
