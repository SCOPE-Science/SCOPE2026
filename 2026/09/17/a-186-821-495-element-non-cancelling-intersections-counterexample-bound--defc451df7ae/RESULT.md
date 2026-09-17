# A 186,821,495-element non-cancelling-intersections counterexample bound

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult `REVIEW.md` for limitations. Publication is not peer review or a guarantee of priority.

## Claim

For `p=571` there exists a marking of every affine line of `F_p^2` by exactly

`w = ceil(sqrt(2p))+1 = 35`

points such that no admissible set `T` has size from `2p` through `4p`. Consequently Wilhelm's lattice `P_{571,m}` has no winning dot-algebra tree and gives a Non-Cancelling Intersections counterexample with exactly

`571^3 + 2*571^2 + 2 = 186,821,495`

elements.

The marking is existential, obtained by the first-moment method; no explicit marking is produced.

## Probabilistic estimate

For `T subset F_p^2`, `|T|=t`, write `j_l=|T cap l|`. The affine-plane incidence identities give

`sum_l j_l = t(p+1)` and `sum_l j_l^2 = t(t+p)`.

If `N` is the number of lines with `j_l>=2`, Cauchy--Schwarz gives

`N >= A(t) := (p+1)^2 (t-p)^2 / (t(t+p))`.

With trace cutoff `K=19`, at most `t(p+1)/20` lines have `j_l>=20`. Thus at least

`S(t) := (p+1)^2 (t-p)^2/(t(t+p)) - t(p+1)/20`

lines have trace size between 2 and 19.

Mark each line independently by a uniformly random 35-subset. A fixed trace of size at most 19 is hit with probability at most

`q = 1 - C(552,35)/C(571,35) < 353/500`.

Therefore a fixed `T` is admissible with probability at most `(353/500)^S(t)`. Put

`b_t = C(p^2,t) (353/500)^S(t)`.

For `t in [2p,4p]`, differentiating `S` and minimizing the derivative over this interval gives

`S(t+1)-S(t) > 27`.

Hence

`b_{t+1}/b_t < (p/2)(353/500)^27 < 1/40`.

At `t=2p`,

`S(2p)=328042/15 > 21869`.

Using `C(n,k) <= (en/k)^k` and `e<11/4`, the source certificate checks exactly that

`b_{2p} < 7/20`.

Thus

`sum_{t=2p}^{4p} b_t < (7/20)/(1-1/40) = 14/39 < 1`.

So some marking has no admissible set in the required interval. Wilhelm's structural lemmas then rule out a winning dot-algebra tree for `P_{571,m}`, producing the stated NCI counterexample.

## Reproducibility

`artifacts/verify.py` uses exact integers and `fractions.Fraction` to certify the prime, marking size, hypergeometric inequality, derivative bound, ratio bound, initial-term estimate, geometric expectation bound, and final lattice size. The archived script executed successfully during packaging.

The complete source report is preserved verbatim in compressed form as `artifacts/research_note.md.gz`; `artifacts/research_note.md` gives the decompression command and uncompressed SHA-256.

## Prior work and scope

The direct source is Hermann Wilhelm, *Refutation of the Non-Cancelling-Intersections Conjecture*, arXiv:2608.27416. Wilhelm's published quantitative theorem uses `p>=10^5`; the displayed `p=100003` instance has `1,000,110,003,900,047` elements. The paper itself says the first-moment estimate has enormous slack and asks how small a counterexample lattice can be. The original NCI conjecture is due to Amarilli, Monet and Suciu, arXiv:2401.16210.

## Limitations

The conceptual mechanism is Wilhelm's existing first-moment construction; the claimed contribution is quantitative. The marking is nonconstructive and `p=571` is not claimed minimal. The source report identifies private or extremely recent work, including work mentioned by Wilhelm, as an unresolved originality threat. No independent validation is claimed.
