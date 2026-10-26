# Review: Quadratic-alphabet existence for systematic burst-deletion codes

## Correctness

**PASS.** The conflict graph contains an edge exactly when two length-\(M\) words share a descendant after a permitted nonempty contiguous deletion burst. For each burst length \(r\), the number of descendants is at most \(B_r=M-r+1\), and the number of possible parents of a fixed descendant is at most \(B_rq^r\). Therefore

\[
d\le M^2\sum_{r=1}^{t}q^r < \frac{M^2q^{t+1}}{q-1}.
\]

The condition \(q>2M^2+1\) gives \(d<q^{t+1}/2\), so Haxell's criterion yields an independent transversal. Its selected words form a literal-systematic code with disjoint burst-descendant sets. The least power-of-two alphabet above the threshold satisfies the stated upper bound.

## Originality

**PASS, with residual risk.** published-finding corpus searches for the exact literal-systematic alphabet tradeoff returned related q-ary deletion-code redundancy results and finite burst-code profiles, but no matching bound. The closest primary paper, arXiv:2609.38259v1, gives a generic Haxell bound for arbitrary deletions and a uniform quartic-order adjacent-burst construction; the present proof counts only contiguous-burst descendants for every length from one through \(t\), obtaining a quadratic alphabet bound in the nonuniform existence model. Earlier non-binary burst-code work focuses on code size and bit redundancy rather than this exact trailer-symbol tradeoff. A prior unindexed equivalent construction remains possible.

## Value

**PASS.** For fixed or varying burst radius, the alphabet-size exponent is quadratic in \(n+t+1\), rather than growing with the burst radius as in the generic arbitrary-deletion graph bound. The construction preserves the entire message prefix and uses \(t+1\) exposed trailer symbols. For \(t=2\) and \(n\ge3\), this matches the known necessary trailer count in the literal-systematic at-most-two-burst model. The result is existential only and does not claim an efficient encoder, optimal alphabet size, or optimal trailer count for all \(t\).

## Closest literature and residual risks

- Valery, Grishin, and Zabokritskiy, arXiv:2609.38259v1: generic arbitrary-deletion independent-transversal benchmark; uniform adjacent-burst construction; different alphabet bound and access model.
- Wang et al., arXiv:2210.11818: non-binary burst-deletion codes optimizing code size/bit redundancy; different systematicity and trailer metric.
- Haxell and Wdowinski, DOI 10.1002/jgt.23085: maximum-degree independent-transversal criterion used in the proof.

Residual risk: an unindexed prior result may establish the same literal-systematic quadratic-alphabet tradeoff. The independent-transversal step does not supply an efficient pointwise encoder.

Self-review: passed. Independent audit: not yet performed.
