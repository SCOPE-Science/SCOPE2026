# Self-review

**Correctness — PASS.** The digit-sum/carry identity is exact. A carry chain bridging two distinct nonzero positions under the stated gap would already require more than \(h\) carries. Consequently on the event \(K\le h\), independent fair-bit blocks around the occupied positions give independent geometric chains. Their sum is negative binomial, producing the exact central-binomial expression. Exact rational checks for six values of \(h\) are supporting checks only.

**Originality — PASS, with a bibliographic risk.** Cheng (arXiv:2606.23398) proved Cusick's universal positive bias and developed exact recurrences. Cheng (arXiv:2608.25899) studied fixed-weight extremal asymptotics. Sobolewski–Spiegelhofer (arXiv:2411.07779) developed general decompositions and detailed cases with at most two one-blocks. The inspected theorems do not state uniform finite-gap plateau invariance for all \(h\ge3\). General recurrences could yield individually covered computations and earlier specialized formulations may exist; independent priority comparison remains necessary.

**Mathematical value — PASS.** Binary digit-sum biases are natural arithmetic statistics. The result gives a uniform structural classification under a motivated separation threshold, rather than a single numerical case; its exact bias behaves as \(1/(2\sqrt{\pi h})\), distinct from the extreme small-bias patterns analyzed in recent work.

The result applies at fixed binary shifts only and does not claim optimality of the spacing threshold for every weight.

Self-review: passed. Independent audit: not yet performed.
