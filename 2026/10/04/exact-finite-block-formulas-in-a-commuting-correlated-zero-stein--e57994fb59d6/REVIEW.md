# Review: Exact finite-block formulas in a commuting correlated zero-Stein-rate family

## Correctness
PASS. The proof reduces every extreme free state's target overlap to a product of block factors. The exact identity \(g_{a+b}-g_ag_b=c(1-c)(1-q^a)(1-q^b)\ge0\) proves that a single \(\zeta_n\) block maximizes overlap. Commutation makes the target ray an eigenvector of every free state, which turns Umegaki and max-relative entropy into exact functions of that overlap. The testing lower bound is attained by the scaled target projector. The smoothing lower bound follows from the trace-distance projector inequality, and the explicit interpolation between the target and \(\zeta_n\) attains it. Boundary cases \(\varepsilon=0\), \(\delta=0\), and \(\delta=2\) are included consistently.

## Originality
PASS. The motivating source's Example 24 states only \(0\le E_n\le\log_2(1/c)\), \(\beta_{\varepsilon,n}\ge c(1-\varepsilon)\), and zero regularized rate. It does not compute the finite-block optimum, the exact testing coefficient, or the smoothed max-relative entropy for the commuting specialization. Searches for exact formulas, correlated alternatives, and smoothing thresholds returned no result implying this joint profile. The closest broader composite-testing paper treats i.i.d. hypothesis families rather than the partition-generated correlated family.

## Value
PASS. Example 24 is the source's concrete demonstration that persistent correlations destroy an otherwise positive Stein exponent. The exact formulas reveal what the vanishing rate hides: a finite nonzero entropy ceiling, an exact type-II floor, and a block-dependent trace-distance threshold at which the smoothed domination cost becomes zero. Determining all three quantities on the classical/commuting boundary gives a complete finite-block benchmark for the paper's correlated obstruction rather than a routine restatement of its asymptotic zero rate.

## Closest literature and limitations
The direct comparison is Gao--Ji--Liu, arXiv:2609.30762v1, Example 24. Frenkel--Mosonyi--Vrana--Weiner, arXiv:2503.13379v1, gives broader composite i.i.d. error-exponent theory and commuting-case structure but does not cover this correlated partition family. Kanazawa--Yamasaki, arXiv:2605.20776v1, addresses mixed sources asymptotically. The present result requires \([\rho,\omega]=0\); the noncommuting Example 24 remains outside the claim. A residual terminology risk remains for older classical correlated-source literature.

Same-model review: passed. Independent audit: not yet performed.
