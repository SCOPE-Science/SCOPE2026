# Review: homocyclic top-coefficient rigidity

## Correctness — PASS

Delsarte's conjugate-height enumeration gives an exact polynomial identity, and reciprocal Gaussian binomials convert it into a positive codegree expansion. In even rank, deleting central entries reduces every chain to two monotone tails. Adding back a central entry changes the Gaussian product by one Gaussian factor of positive parameters. The omitted-pattern decomposition is coefficientwise nonnegative; its first nonzero coefficient is the sum of exactly \(a+1\) split-jump contributions and \(a+2\) new noncentral patterns, yielding \(2a+3\). In odd rank, each noncentral height costs at least two powers of the codegree variable, so only bounded prefixes/suffixes affect a fixed coefficient. Each remaining central block has two boundary and \(L-1\) identical interior-switch terms, proving eventual affine dependence. The leading and subleading coefficients follow by direct enumeration of defect-zero and defect-one chains. No finite experiment is used to justify an infinite quantifier.

A standalone exact-arithmetic implementation checked the complete Delsarte and transfer-recursion polynomials for 49 rank/exponent pairs. A separate coefficient expansion of the known limiting product checked all 28 tested sharp-boundary instances. Both checks passed. The complete proof is in `RESULT.md` and the executable is `verify.py`.

## Originality — PASS, with explicitly limited historical certainty

The nearest primary work is S. Aivazidis, *Subgroup bounds for abelian p-groups with applications*, arXiv:2606.03320v1 (June 2, 2026), especially Theorem A, Proposition 4.2, and Section 9. It gives the leading term, a homocyclic bound, and its analytic limiting series, all of which are treated as known here. Its insertion lemma is also prior work. Those results do not state finite-exponent agreement through exactly codegree \(a\), the universal first shortfall \(2a+3\), or eventual affine dependence of all fixed odd-rank coefficients with an explicit threshold. The sharp first deficit and affine law require the distinct first-excluded-pattern and central-switch analyses.

Chew–Chin–Lim, *The number of subgroups of finite abelian p-groups of rank 4 and higher* (2020), DOI 10.1080/00927872.2019.1691571, has a special-rank exact formula that may imply selected cases, but its accessible abstract does not establish the all-rank statement. The complete text could not be inspected; that is a specific residual risk. Searches for exact coefficient stabilization, an all-rank universal deficit, odd-rank affine laws, and equivalent Gaussian-polynomial statements did not identify a covering published result. Lack of a search hit is not proof of absolute priority. Delsarte's general formula itself contains all relevant polynomial data but does not state the finite coefficient structure.

## Mathematical value — PASS

The first-prime-order asymptotic in the recent source is promoted to a sharp and effective **coefficientwise truncation theorem**, not just an additional small numerical coefficient. The universal \(2a+3\) first discrepancy makes the cutoff optimal and independent of the even rank. In odd rank, every fixed upper polynomial coefficient has eventual degree at most one in the cyclic exponent, with a usable uniform threshold. Together these provide a finite-polynomial sensitivity result distinguishing the unique central height at even rank from the two central heights at odd rank. They can be used to extract any fixed number of highest powers without enumerating arbitrarily long subgroup-type chains. No claim is made to settle the source's separate open problems for arbitrary abelian shapes.

## Limits and closest comparisons

The primary 2026 paper was materially read in its enumeration, homocyclic-bound, limiting-constant, leading-term, and open-problem sections through its openly available full text. Chew–Chin–Lim's full text was not accessible, so the review only compares the verified scope of its abstract. Older symmetric-function literature could contain another route to the same finite truncation identity. The result is a self-reviewed mathematical claim, not an independent audit or priority certificate.

Self-review: passed. Independent audit: not yet performed.
