# Mathematical review

## Correctness — PASS

The four-run representation of a positive \(0101\)-count is forced, and every five-run representation has exactly one unused endpoint run, giving the balanced product \(Q_n\). Direct, disjoint choices of the second matched symbol in the six-run witness give the count difference \((a-1)(b-1+d)-cd\). The four explicit residue polynomials are strictly positive for all \(n\ge9\). The cases \(n=6,7\) have concrete strictly better witnesses; every one of the \(2^n\) words at lengths \(4\le n\le8\) is exhausted by two distinct counting routines. The checker also verifies the low-run capacity in additional small cases. No finite sampling is used to infer the infinite conclusion.

## Originality — PASS, subject to residual risk

Menon and Singh (2023, arXiv:2306.07870v1, Section 4) already identify the failure at \(n=6\) for an alternating target of length four. That observation is not claimed as new. Their at-most-three-run theorem does not supply a four-run classification; their explicit \(n=6\) example does not imply the unexpected \(n=8\) equality or prove failure for all \(n\ge9\). Burstein–Hästö–Mansour (2003) treat other pattern classes and packing-density questions. Barton's clumpy-pattern structural result (2004) is inapplicable because \(0101\) interleaves equal letters. Specific statement, alias, database, and stronger-coverage searches revealed no equivalent all-length theorem. Unindexed equivalent work remains possible.

## Mathematical value — PASS

The alternating four-run pattern is the first natural boundary outside the cited three-run structural result. This theorem completely resolves when a low-run host can be globally optimal, establishes a strict structural obstruction from six runs onward, and finds a nonmonotone return to four-run optimality at \(n=8\) between two regions of failure. It is a full natural classification of a word-structure question, not an arbitrarily chosen parameter slice or merely an enumeration of examples.

## Closest sources and limitations

The main closest source is Menon–Singh, *Subsequence Frequency in Binary Words* (arXiv:2306.07870v1), Section 4 and its open-ended conclusions. Packing-density and clumpy-pattern works are related but do not imply the finite exceptional set. The unrestricted maximum count for general length remains open in this result, and priority requires independent literature review.

Self-review: passed. Independent audit: not yet performed.
