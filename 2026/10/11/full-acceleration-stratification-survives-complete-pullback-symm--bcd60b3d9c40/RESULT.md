# Full acceleration stratification survives complete pullback-symmetry breaking
## Finding
Fix a strip width \(\rho>0\), a Diophantine frequency \(\alpha\), an integer \(N\ge2\), and \(\lambda>1\). Let \(X=C^\omega_\rho(\mathbb T,\mathbb R)\) be the real Banach space of one-periodic real-analytic strip-\(\rho\) potentials, and put
\[
B(x)=2\lambda\cos(2\pi N x).
\]
There is a prevalent subset \(\mathcal P\subset X\) such that, for every \(\delta\in\mathcal P\), there is \(\varepsilon_0(\delta)>0\) for which every \(0<\varepsilon<\varepsilon_0(\delta)\) satisfies both of the following statements.

First, for every \(s\in\{{1,\ldots,N\}}\), the set of spectral energies with acceleration \(s\) has positive Lebesgue measure. Second, the potential
\[
V_{{\varepsilon,\delta}}(x)=B(x)+\varepsilon\delta(x)
\]
has no nonzero translational period on \(\mathbb T\). Equivalently, it is not a pullback through any nontrivial finite covering of the circle.

Hence the acceleration strata \(1,\ldots,N\) produced from an \(N\)-fold almost-Mathieu seed survive prevalently even when all exact finite pullback symmetry is destroyed.

## Assumptions and scope
The acceleration statement is the theorem of Liang, Wang, and Xu for their open prevalent set \(\mathcal P_{{\rm strat}}\subset X\). The new point is a simultaneous prevalent symmetry-breaking condition on the perturbation. No statement is made about perturbations outside the resulting prevalent set, about \(\lambda\le1\), about non-Diophantine \(\alpha\), or about regularity weaker than the analytic strip space used in the source.

A nontrivial translational period means a nonzero element \(t\in\mathbb T\) such that \(V(x+t)=V(x)\) for every \(x\). For a nonconstant continuous one-periodic function, the period subgroup is a proper closed subgroup of \(\mathbb T\), hence is finite cyclic. Therefore a nontrivial period exists exactly when there is some integer \(q\ge2\) for which \(1/q\) is a period. A one-periodic analytic function has period \(1/q\) exactly when it factors through the covering \(x\mapsto qx\pmod1\).

## Proof
For each integer \(q\ge2\), define the bounded linear difference operator
\[
D_q f(x)=f(x+1/q)-f(x)
\]
and let \(b_q=D_qB\). Define
\[
S_q=\{\delta\in X:D_q\delta\in\operatorname{{span}}\{{b_q\}}\}.
\]
Because \(D_q\) is continuous and \(\operatorname{{span}}\{{b_q\}}\) is finite-dimensional and closed, \(S_q\) is a closed linear subspace of \(X\).

It is proper. If \(q\mid N\), then \(b_q=0\), so \(S_q=\ker D_q\); an analytic Fourier mode whose frequency is not divisible by \(q\) lies outside this kernel. If \(q\nmid N\), then \(b_q\ne0\) and has only Fourier frequencies \(\pm N\). Choose an integer \(m\ne N\) with \(q\nmid m\). Then \(D_q\cos(2\pi m x)\) is nonzero and has only frequencies \(\pm m\), so it cannot be a scalar multiple of \(b_q\). Thus \(S_q\ne X\) in all cases.

Every proper closed linear subspace of a Banach space is shy. Indeed, for \(w_q\notin S_q\), normalized one-dimensional Lebesgue measure on a compact segment of the line \(\mathbb R w_q\) is transverse to every translate of \(S_q\): a translate can meet that line in at most one parameter value. Shy Borel sets form a sigma-ideal in the prevalence theory of Hunt, Sauer, and Yorke. Hence
\[
S=\bigcup_{{q=2}}^\infty S_q
\]
is shy and
\[
\mathcal P_{{\rm prim}}=X\setminus S
\]
is prevalent.

Now take \(\delta\in\mathcal P_{{\rm prim}}\) and \(\varepsilon\ne0\). If \(V_{{\varepsilon,\delta}}\) had period \(1/q\) for some \(q\ge2\), then
\[
0=D_qV_{{\varepsilon,\delta}}=b_q+\varepsilon D_q\delta,
\]
so
\[
D_q\delta=-\varepsilon^{{-1}}b_q\in\operatorname{{span}}\{{b_q\}},
\]
which means \(\delta\in S_q\), a contradiction. Thus \(V_{{\varepsilon,\delta}}\) has no nontrivial translational period for every nonzero \(\varepsilon\).

The focal paper supplies an open prevalent set \(\mathcal P_{{\rm strat}}\) such that every \(\delta\in\mathcal P_{{\rm strat}}\) has an \(\varepsilon_0(\delta)>0\) for which every acceleration level \(s=1,\ldots,N\) occupies a positive-measure spectral set whenever \(0<\varepsilon<\varepsilon_0(\delta)\). Since countable intersections of prevalent sets are prevalent, in particular
\[
\mathcal P=\mathcal P_{{\rm strat}}\cap\mathcal P_{{\rm prim}}
\]
is prevalent. Both conclusions therefore hold simultaneously on \(\mathcal P\).

## Verification
The proof uses no finite experiment. The source theorem was checked in the first public version of the paper, including its analytic perturbation space, prevalence definition, the \(N\)-fold seed, and the assertion of positive-measure acceleration strata for every \(s=1,\ldots,N\). The source's prevalence proof also explicitly uses one-dimensional probes for complements of finitely many linear kernels, matching the elementary subspace-shyness argument above.

The only additional general prevalence fact is that shy Borel sets form a sigma-ideal, equivalently that countable intersections of prevalent sets are prevalent; this is part of the standard Hunt--Sauer--Yorke framework. The period-group step is exact: a closed subgroup of the circle is either the whole circle or a finite cyclic group, and the whole-circle case makes the potential constant and therefore also gives a period \(1/q\).

## Relationship to prior work
Liang, Wang, and Xu prove that prevalent perturbations of the \(N\)-fold supercritical almost-Mathieu seed exhibit all positive acceleration levels \(1,\ldots,N\) on positive-measure spectral sets. Their construction begins from a potential with exact translation period \(1/N\), and translation symmetry of the unperturbed model is used in the analysis. The statement above separates the resulting acceleration multiplicity from any surviving exact finite translation symmetry: after intersecting with a second prevalent set, the perturbed potential has fundamental period exactly one for every nonzero perturbation amplitude.

Targeted searches for the focal source identifier, acceleration strata with symmetry breaking, fundamental-period formulations, and finite-cover pullback formulations located no published statement implying this simultaneous prevalent conclusion. The closest standard ingredient is prevalence theory itself, which supplies the sigma-ideal property but says nothing about acceleration.

## Limitations
The result is a structural corollary of the focal acceleration theorem plus a new prevalence argument; it does not alter the source's spectral estimates or extend its parameter regime. The prevalent set \(\mathcal P_{{\rm prim}}\) constructed here is not asserted to be open. The conclusion rules out exact finite translational periods, not approximate symmetries, measurable factor structures, or other non-translation symmetries. A later revision of the very recent focal preprint or an unindexed note could contain an equivalent symmetry-breaking corollary.

## References
1. J. Liang, Y. Wang, and J. Xu, “Positive-Measure Acceleration Strata for Prevalent Perturbations of N-Fold Pullbacks of Supercritical Almost Mathieu Potentials,” arXiv:2610.05243v1, first public 2026-10-04.
2. B. R. Hunt, T. Sauer, and J. A. Yorke, “Prevalence: a translation-invariant ‘almost every’ on infinite-dimensional spaces,” Bulletin of the American Mathematical Society 27 (1992), 217–238, DOI 10.1090/S0273-0979-1992-00328-2.
