# Scientific review

## Correctness — PASS

The central quantifier is all real \(0\le\alpha\le1/2\) and all independent probabilities \(\mathbf p\in[\alpha,1-\alpha]^6\). Pivotal probability is multiaffine in these parameters, making its pairwise extrema corner-attained. A direct exact coefficient enumeration of all \(64\) corners times all \(15\) pairs establishes a complete nine-class polynomial list; every class is bounded by \((1-2\alpha)^2\), and the specified corner achieves equality. The standalone checker independently recalculates pivotal indicators directly from the voting rule and checks integer coefficients and counts. This is a finite symbolic identity certificate combined with a valid continuous-domain reduction, not a finite numerical approximation. All boundary cases, including \(\alpha=0,1/2\), are included.

## Originality — PASS, with residual historical-priority uncertainty

Dhar–Mittal–Thomas (2026, arXiv:2602.13894v1, full preprint read), give fairness under common (identical) Bernoulli bias and introduce Icos as an established fair example, citing Loeb–Conway (2000). Those statements alone do not imply a sharp bound for six independently heterogeneous biases; the present claim measures a different six-dimensional perturbation and gives exact worst-case equality. Search comparisons against voting power, influence, heterogeneous turnout, and related six-player published research records found no matched bound. Loeb–Conway's abstract and citations were checked, but its full text could not be accessed; an earlier equivalent is possible. No guarantee of global novelty is claimed.

## Mathematical value — PASS

Fairness of this non-anonymous, resolute six-voter rule under a common vote bias raises a natural robustness question: how far can its voters' pivotal probabilities separate when participation/vote propensities differ? The exact \((1-2\alpha)^2\) law, complete coefficient chamber census, and attaining profile answer that question sharply for every allowed perturbation magnitude, separating an equal-bias design guarantee from worst-case heterogeneous operation. This is a natural quantitative stability boundary, not an arbitrary small-parameter recomputation.

## Limitations

Only one explicitly defined six-voter rule (up to relabeling), independent Bernoulli votes, and absolute pivotal probabilities are covered. The historical-primary-text gap leaves priority uncertainty. The polynomial certificate requires ordinary Python 3 but no third-party packages; an independent scientific review has not been performed.

Self-review: passed. Independent audit: not yet performed.
