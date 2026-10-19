# Mathematical review

## Correctness — PASS

The theorem is for all positive integers \(a,b,c,d\); neither a finite table nor a numerical conjecture is used to prove it. Factor types reduce to constant blocks, two adjacent-run boundaries, and factors containing a full intermediate run. The four possible placements of a zero and a one reduce to three viable families, with exact forcing by the factors \(10\), \(01\), \(01^{d+1}\), and \(0^{a+1}1\), where the latter two are invoked only in their respective nontrivial parameter regions. The proof checks sufficiency for all factor types, gives explicit three-position witnesses, and derives the exhaustive classification, count and sharp threshold. Two separate finite check implementations agreed over the stated parameter boxes. Finite checks support, but are not substitutes for, the general proof.

## Originality — PASS (qualified)

The closest primary sources are Kempa et al. (ESA 2018, DOI 10.4230/LIPIcs.ESA.2018.52), Mantaci et al. (arXiv:1907.04660 and its expanded TCS 2021 treatment), and Dvořáková–Hendrychová (arXiv:2308.00850). They establish the attractor framework, general verification machinery, and results for special families, but the inspected results do not state or imply an arbitrary-four-run formula. Indexed particular-word results can cover isolated cases such as \(0101\); no independent novelty is claimed for those special cases. The contribution is the complete four-parameter classification and its phase boundary. Semantic-record searches and relevant literature searches did not locate a stronger covering theorem; this is evidence, not proof of global novelty. Residual risk: equivalent earlier work might be unindexed or use different terminology.

## Mathematical value — PASS

A length-four run decomposition is the first alternating binary run family allowing an optimal attractor larger than the two-symbol lower bound. The theorem supplies an exact, parameter-wide dichotomy and identifies every two-point witness with a closed count; the one-unit survival region gives a meaningful boundary not captured by comparing run lengths alone. It replaces general substring enumeration by a constant-size set of arithmetic comparisons for a natural compression-related invariant. It does not claim a general result for arbitrary numbers of runs or a census of the three-position minimizers.

## Remaining limitations

All four run lengths must be positive, the alphabet must be binary, and positions are linear rather than circular. A full independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
