# Review

## Correctness

PASS. After centering, symmetry immediately forces the conditional mean of the pair sum to vanish given the absolute difference. Conversely, the conditional-mean identity may be tested against the even function \(\cosh(t(Z_2-Z_1))\); exchangeability separately kills the corresponding odd \(\sinh\) term. Their sum yields an exponential identity that factors under independence into
\[
M'(-t)M(t)+M(-t)M'(t)=0.
\]
On a smaller exponential-moment neighborhood this implies that \(\log M(t)-\log M(-t)\) is constant and hence zero. Moment-generating-function uniqueness then proves central symmetry. The packaged exact-rational census independently confirms the equivalence on thousands of finite-support laws.

## Originality

PASS, with a specific residual risk from older midrange-characterization literature. Two full primary papers by Huang and Su were inspected at their regression-characterization theorem statements. They condition on specified order statistics or adjacent order statistics rather than on the absolute difference of a two-observation sample, and do not state the accepted symmetry criterion.

Akhundov--Balakrishnan--Nevzorov is the most plausible older source because it explicitly concerns midrange characterizations. Only its abstract was accessible for decisive comparison; that abstract describes different conditional regressions involving central order statistics and a Student-law characterization. It remains a named residual risk rather than being declared non-covering.

The modern mean/range independence theorem of Hu and Lin is not stronger in a way that covers the present statement: it assumes full independence, continuous positive density, and sample size at least three, and concludes normality. The accepted result concerns only constant conditional mean at sample size two and includes discrete laws.

## Value

PASS. Conditional mean independence is a natural intermediate notion between zero covariance and full independence. The theorem identifies exactly what this weaker dependence requirement detects for the most basic location-versus-spread pair: central symmetry.

The result is structural rather than a moment recomputation. It gives a two-observation diagnostic valid for discrete, continuous, and mixed laws under one transparent local-transform assumption, and sharply separates symmetry characterization from classical normal characterizations based on full independence.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK laws=9072 flat=396 symmetric=396`.
