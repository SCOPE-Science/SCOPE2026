# Mathematical review

## Correctness — PASS
The binomial coefficients \(\binom{p^m-1}{k}\) are units modulo \(p\). Among the denominators \(r+k\), exactly one is divisible by \(p^m\), namely at \(k=p^m-r\). This summand has valuation \(\nu_p(r)-m\); ultrametric comparison puts every other nonzero term strictly higher. The same unique term supplies the explicit normalized residue. The denominator bound is independently derived from an exact product of two ordinary binomial coefficients, and the upper bound's \(p\)-valuation is computed directly. The proof covers endpoints \(m=1\), \(r=1\), and \(r=p^m-1\). Exact rational checks in `verify.py` separately corroborate these claims, without serving as an infinite proof.

## Originality — PASS, with literature risk
The closest paper with the same rational sums is López-Aguayo and Luca (arXiv:1508.02927), whose results show nonintegrality for six fixed shifts and for the opposite range \(n\le r-1\). Laishram et al. (arXiv:1903.08043) prove nonintegrality for \(r\le22\), and a density theorem, not the odd-prime valuation or leading residue for an unbounded shift. Kellner (INTEGERS 23 (2023), #A45) supplies the general denominator bound and, when the prime divides the evaluation argument, certain exact denominator valuations. At the present evaluation \(\ell=2\) the latter statement concerns prime \(2\), not the odd primes of this theorem. The odd-prime saturation and leading-digit congruence do not follow from the cited nonintegrality statements. Literature search and mathematical-record comparison found no same-statement coverage, but this is not a uniqueness proof. The 2018 Thongjunthug article was located by publisher/abstract and cited for its published algorithm; its complete text was not confirmed accessible in this inspection, leaving a limited residual risk.

## Mathematical value — PASS
The conjectural nonintegrality of the binomial sum is a named arithmetic problem. This theorem settles the exact \(p\)-part of the reduced denominator (including its first nonzero unit) for an infinite two-parameter family in every odd characteristic, with arbitrarily large shifts beyond the fixed-shift literature. It establishes equality in an independently proved universal denominator bound. The parameter restriction \(n=p^m-1\) is structurally forced by complete modular nonvanishing of the binomial row and the unique denominator multiple; it is not an arbitrary slice. The statement does not settle arbitrary rows or all denominator primes.

## Residual risks and limits
Broader character-sum or \(p\)-adic denominator literature could imply the result without mentioning these parameters verbatim. The 2018 algorithm source was not inspected in full. An independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
