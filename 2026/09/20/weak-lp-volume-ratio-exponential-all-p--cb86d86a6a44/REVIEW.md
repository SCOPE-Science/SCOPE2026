# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The key geometric translation is exact. For
`W_{p,n}=n^{1/p}B^{n,+}_{p,infinity}`, the rearrangement inequalities
`y_k^* <= (n/k)^{1/p}` are equivalent, by one-sided limits, to the empirical
survival bounds `N_y(t)<n t^{-p}`. Bounds for `t<1` are automatic.

The positive generalized-Gaussian density

\[
f_p(x)=\frac{e^{-x^p/p}}{p^{1/p}\Gamma(1+1/p)}
\]

has p-th moment one and entropy

\[
h_p=\log\Gamma(1+1/p)+(\log p+1)/p,
\]

which is also the limiting logarithmic volume per coordinate of
`n^{1/p}B_p^{n,+}`. Strict Markov inequality yields
`P(X>t)<t^{-p}` for every `t>0`.

Moving epsilon mass from an interval below 1 to an interval strictly above
1 preserves the weak-tail inequalities for sufficiently small epsilon,
because the original survival-function gap is positive uniformly on the
relevant compact interval. Its first entropy variation is

\[
\frac1p(\operatorname{avg}_B x^p-\operatorname{avg}_A x^p)>0,
\]

so an admissible density with entropy strictly greater than `h_p` exists.
Truncating far in the tail and reinserting the removed mass below 1 preserves
all constraints for `t>=1`; the entropy loss tends to zero because the
p-Gaussian tail has integrable `|f\log f|`.

For a compactly supported admissible density, strict tail inequalities have
a uniform positive margin. A sufficiently fine finite partition converts
this margin into a robust cumulative-bin inequality. Exact-count type sets
for bin masses are then contained in the scaled weak ball for all large n.
Their volume is a multinomial coefficient times bin lengths. Stirling's
formula gives the histogram differential entropy as the exponential rate,
and nonnegativity of relative entropy on each bin shows that histogram
entropy is at least the original density entropy. This rate is therefore
strictly above `h_p`.

Finally, the common scaling and the factor `2^n` from coordinate signs cancel
in the volume ratio. A positive liminf of `(1/n)log R_{p,n}` gives constants
`c_p>0` and `C_p>1` after finitely many small dimensions are absorbed into
`c_p`.

Potential edge cases were checked: the argument does not use convexity and
therefore remains valid for `0<p<1`; type-count rounding is `O(1/n)` because
the partition is fixed; bin endpoints are harmless because volume-zero
boundaries do not affect the type volume or the rearrangement constraints.

## Originality — PASS, to the best of our knowledge

The direct source is Dolezalova--Vybiral, Journal of Approximation Theory 255
(2020), 105407, DOI 10.1016/j.jat.2020.105407. Its introduction and volume
ratio section were inspected. Theorem 8 proves exponential growth for
`0<p<=2`, the text explicitly states the same assertion for `2<p<infinity`
as an open problem, and Remark 3 notes that the particular construction can
be extended only to `p<p_0` with `p_0 approximately 2.1086`.

Searches used the exact article title and DOI, `R_{p,n}`, weak Lebesgue and
weak-Lp volume ratio terminology, Lorentz-ball volume terminology, and the
p>2 formulation. No later source located in those searches states a solution
of the open range. The source currently lists five citing items in the
publisher index.

Two especially relevant later works were checked. Kabluchko--Prochno--
Sonnleitner, arXiv:2303.04728, develops probabilistic and maximum-entropy
methods for Lorentz balls `ell_{q,1}^n`; its stated scope is the second-index
1 family, rather than the weak family `ell_{p,infinity}^n`. Prochno--
Sonnleitner--Vybiral, Studia Mathematica 283 (2025), 105-131, DOI
10.4064/sm240409-15-2, studies entropy numbers of finite-dimensional Lorentz
embeddings. Its accessible manuscript cites the 2020 paper for volume-radius
estimates and uses those estimates only up to multiplicative constants; no
statement resolving the exponential weak-Lp/ell_p volume ratio was found.

Repository searches by Lorentz/weak-Lebesgue terminology, volume-ratio
phrases, and the source authors/title found no overlapping SCOPE record.
The principal residual originality risk is an unindexed paper or an
unexpectedly different formulation of the same entropy/type argument.

## Value — PASS

The result answers a concrete explicit open problem from the 2020 source for
every finite p, rather than only extending the numerical cutoff of the
source construction. It also gives a conceptually different reason for the
strict gap: the p-Gaussian sits strictly inside the empirical tail constraint
at the exact entropy rate of the ell_p ball, so an arbitrarily small outward
mass transfer creates a strictly larger admissible entropy rate.

The type-class step is elementary and portable. The same template can be
useful whenever a symmetric high-dimensional body can be expressed through
uniform empirical-tail inequalities and a reference density lies strictly
inside those inequalities at a comparison body's entropy rate.

## Limitations

- The proof establishes only a positive exponential gap; it does not compute
  the optimal exponent or the exact limit of `R_{p,n}^{1/n}`.
- It does not identify the entropy-maximizing measure under the weak-tail
  constraints, nor prove a complete large-deviation principle.
- The endpoint `p=infinity` is outside the statement.
- A non-indexed or differently formulated equivalent result may exist.
- Independent audit has not been performed.
