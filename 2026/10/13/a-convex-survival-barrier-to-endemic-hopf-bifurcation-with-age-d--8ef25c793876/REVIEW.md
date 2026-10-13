# Scientific review

## Correctness — PASS

The calculation expands the original nonlinear renewal incidence equation without approximation, deriving \(\Delta(z)=1-\widehat{\beta F}(z)/\mathcal R_0+(\mathcal R_0-1)\widehat F(z)/m\). A nonincreasing residence-time density makes the survival function convex. The derived curvature-measure representation proves \(\Re\widehat F(z)\geq0\) on the entire closed right half-plane; positivity of \(\beta F\) makes the complementary normalized transform's real part strictly less than one except at zero, where the feedback term is positive. This establishes \(\Re\Delta(z)>0\) for every admissible parameter, including the boundary \(\Re z=0\). Under an exponential tail, a spectral-gap and weighted causal convolution-resolvent argument proves local exponential incidence stability. The executable tests independently sample finite mixture closures but are not substituted for the proof.

## Originality — PASS, confined to the explicit model and shape class

Scarabel–Coldwell–Cassidy (arXiv:2511.09196v1, sections 2 and 4) give the renewal equation, characteristic equation and numerical Hopf evidence for more concentrated residence-time distributions, but do not establish this unrestricted-infectivity decreasing-density barrier. Nakata–Röst (arXiv:1704.04225, sections 2 and 4) prove global stability for *constant* infection-age infectivity; their characteristic equation is different. Diekmann–Montijn (CWI TW215/81, sections 1–3) analyze deterministic immunity periods; their deterministic return-time condition is not the decreasing-density condition proved here. Chen–Yang–Zhang (2014) consider a different SIRS compartment structure; only abstract-level comparison was accessible. These differences were checked as statements and assumptions rather than as title differences. A residual possibility is broader unindexed nonlinear-renewal stability theory or unavailable full text supplying the same criterion.

## Mathematical value — PASS

The motivating model exhibits age-dependent-transmission-induced Hopf bifurcations. The theorem identifies an analytically checkable **entire distributional class** where such a local transition cannot occur, without restricting the nonnegative infectivity curve. The gamma \(0<j\leq1\), hyperexponential and uniform-duration examples make the boundary biologically interpretable; a uniform duration has variance below that of an exponential yet remains protected, showing that this barrier is not simply a variance threshold. The result does not claim global dynamics or exclude detached cycles.

Self-review: passed. Independent audit: not yet performed.
