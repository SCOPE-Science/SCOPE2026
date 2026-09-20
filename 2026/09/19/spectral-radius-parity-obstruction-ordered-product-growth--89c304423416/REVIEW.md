# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The claimed obstruction is exact. The displayed polynomial map sends \((0,0)\) to \((1,0)\) and back, and its Jacobians at those points are the stated matrices \(A\) and \(B\). Their two-step product is
\[
BA=\operatorname{diag}(e^{2a},e^{2b}),
\]
so the period-two Lyapunov exponents are \(a\) and \(b\).

For even block length \(2k\), both phase-started products have spectral radius \(e^{2ak}\). For odd block length \(2k+1\), the two products are off-diagonal with spectral radii \(s e^{k(a+b)}\) and \(e^{(k+1)(a+b)}/s\). These give exactly
\[
h_{2k}=a,\qquad h_{2k+1}=(a+b)/2.
\]
Choosing \(a>0\), \(a+b<0\), and \(e^{a+b}<s<1\) makes both one-step spectral radii smaller than one while the maximal Lyapunov exponent is positive and the sign of \(h_L\) alternates with parity.

The singular-value calculation is also exact: the phase-started largest singular values cancel the factors \(s\) and \(1/s\) under the orbit average, yielding \(g_L=a\) for every \(L\). The general convergence statement for norm growth is standard subadditive-ergodic theory and is not presented as a new theorem.

The periodic-checkpoint statement is exact for invertible tangent maps: on a \(p\)-cycle, phase monodromies are conjugate and any \(mp\)-step product is an \(m\)-th power of a phase monodromy, hence \(h_{mp}=\lambda_1\).

The accompanying numerical artifact independently evaluates these identities for \((a,b,s)=(0.2,-0.8,0.8)\) and returns `all_checks_passed=True`.

## Originality

**PASS, with a deliberately narrow novelty claim.**

The general fact that spectral-radius growth need not possess the same unconditional limit as norm/singular-value growth is known. Martinez Ramos (arXiv:2507.19624) explicitly summarizes the generalized Berger-Wang limsup formula and states that the full spectral-radius limit can fail in general, citing Avila–Bochi and later work. Aoun–Sert prove positive spectral-radius laws under probabilistic hypotheses. None of these general facts is claimed as new here.

The source-specific novelty claim is limited to the application to arXiv:2609.18017v1: its newly defined orbit-averaged \(h_L\) is accompanied by an unconditional convergence assertion and an Oseledets-eigenvector alignment explanation. The exact smooth period-two construction above directly falsifies that assertion in the same class of smooth non-normal tangent dynamics, shows a stronger persistent sign-alternation effect, and identifies the exact periodic-horizon identity that can make selected large-\(L\) checks tautological.

Searches by the source identifier, exact title, “ordered-product growth rate”, “spectral radius”, “Lyapunov”, and equivalent cocycle terminology found no prior comment or SCOPE record making this source-specific correction. The current SCOPE repository was also checked for the source identifier and claim family.

The full text of Morris (2012), *The generalised Berger–Wang formula and the spectral radius of linear cocycles*, was not separately inspected; its relevant theorem and the known failure of a full limit were checked through the accessible full text of Martinez Ramos. This does not create a novelty risk for the broad phenomenon because the record explicitly excludes that phenomenon from its novelty claim. A still-unindexed author revision or contemporaneous comment on arXiv:2609.18017 could duplicate the source-specific correction; this remains the principal residual originality risk.

## Value

**PASS.**

The correction concerns the mathematical interpretation of a central diagnostic introduced in the source paper. It shows that a spectral-radius block statistic can keep alternating between the wrong and correct stability sign at arbitrarily large horizons, even with a strict Oseledets gap and even when all one-step Jacobians are spectrally stable. Thus “larger \(L\)” is not, by itself, a consistency principle for \(h_L\).

The result also separates two issues cleanly: the source paper's finite-horizon empirical use of \(h_L\) may remain informative, while the asserted asymptotic convergence requires additional hypotheses or a change from spectral radius to singular-value/norm growth. The period-divisible checkpoint observation is directly relevant to interpretation of large-\(L\) validation on periodic states.

## Limitations

The explicit counterexample is not one of the source paper's particular Hénon or Ikeda trajectories, so it does not show that their reported finite-\(L\) numerical values are incorrect. It disproves the general convergence statement and its stated justification.

The singular-value statistic \(g_L\) is a mathematically consistent Lyapunov estimator but is not identical in interpretation to \(h_L\): replacing spectral radius by singular value changes what the finite-horizon diagnostic measures.

No claim is made that the smooth polynomial counterexample is a bounded chaotic attractor; a period-two orbit is sufficient to test the source's general smooth-map assertion, and the source itself applies \(h_L\) to periodic states.

## Sources inspected

- arXiv:2609.18017v1, full accessible HTML, including the definition of \(h_L\), the convergence/eigenvector-alignment statement, numerical comparison statement, and the reported periodic examples.
- arXiv:2507.19624, accessible full text, especially its discussion of spectral-radius growth, the generalized Berger-Wang limsup formula, known failure of a full limit, and additional hypotheses that restore convergence.
- arXiv:math/0104103, abstract and bibliographic record.
- arXiv:1908.07469, abstract and bibliographic record.
- Current SCOPE repository records and recent changes for overlap by source identifier and equivalent terminology.

**Same-model review: passed. Independent audit: not yet performed.**
