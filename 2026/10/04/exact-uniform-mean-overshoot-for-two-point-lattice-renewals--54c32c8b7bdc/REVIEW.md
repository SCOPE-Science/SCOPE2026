# Review

## Correctness

PASS. The proof separates real boundaries into integer intervals, derives the
initial-window expectation exactly, obtains
\[
e_b-e_{b-1}=\mu q^b-1,
\]
proves the maximizing index lies below \(m-1\), and then uses the renewal
recursion
\[
e_b=q e_{b-1}+p e_{b-m}
\]
as a maximum principle for all later boundaries. The rare-long-jump asymptotic
is obtained directly from the same exact formula. Exact-rational replay agrees
with the theorem over 4560 rational parameter choices.

## Originality

PASS, with a stated residual historical-literature risk. Searches covered exact
two-point overshoot formulas, sharp Lorden constants, renewal residual-life
maxima, and rare-long-jump scaling. The closest general sources provide
distribution-free inequalities rather than the exact two-point uniform
constant. The closest inspected public related result uses pairwise-independent
increments and higher-order dependence, while another concerns stationary
age/residual-life correlation; neither implies the claim here.

The full two-page Carlsson--Nerman renewal-inequality proof was inspected.
Lorden's repository abstract and bibliographic record were inspected, but its
full article was not available through that repository view. This access gap is
retained as a residual originality risk rather than treated as evidence of
novelty.

## Value

PASS. The support \(\{1,m\}\) is the simplest nondegenerate lattice renewal
family with a tunable jump scale. Determining the exact uniform overshoot
constant and its maximizing boundary is a natural refinement of the classical
uniform-bound problem, and the rare-long-jump limit quantifies a persistent
gap between the exact family constant and the generic second-moment bound.

Same-model review: passed. Independent audit: not yet performed.
