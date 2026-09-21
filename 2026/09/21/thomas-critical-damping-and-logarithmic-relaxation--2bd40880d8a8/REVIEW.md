# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For
\[
\dot x_i=\sin x_{i+1}-b x_i,
\]
the proper Lyapunov function \(V=\frac12\sum x_i^2\) satisfies
\[
\dot V\le -(b-1)\sum_i x_i^2-\frac12\sum_i(|x_i|-|x_{i+1}|)^2.
\]
At \(b=1\), equality in the cyclic quadratic inequality forces all coordinate magnitudes to coincide; for any positive common magnitude, \(|\sin s|<|s|\) makes the preceding inequality strict. Hence \(\dot V<0\) for every nonzero state, proving global asymptotic stability at the nonhyperbolic endpoint. For \(b<1\), the common-mode linear eigenvalue \(1-b\) is positive. This establishes the exact closed threshold.

The critical-rate proof is separate from the global Lyapunov argument. At \(b=1\), the Jacobian \(P-I\) has one simple zero eigenvalue along the diagonal and all other eigenvalues strictly in the left half-plane. The diagonal is exactly invariant and carries \(u'=\sin u-u\). Standard strong-stable foliation theory then gives a codimension-one exceptional set of exponentially decaying trajectories and exponential shadowing of a nonzero diagonal trajectory otherwise.

For the scalar center flow, setting \(w=u^{-2}\) gives
\[
\dot w=\frac13-\frac1{60w}+O(w^{-2}).
\]
The first consequence \(w\sim t/3\) feeds back to yield an integrable remainder after subtracting \(t/3-(1/20)\log t\). The symbolic artifact checks the Taylor coefficients used here. Exponential transverse shadowing is much smaller than the \(t^{-1/2}\) center amplitude, so all coordinates inherit the same sign and the same finite renormalized constant.

Stress tests included arbitrary signs in the Lyapunov inequality, even and odd ring lengths, the exact equilibrium equation at \(b=1\), and the possibility of an exceptional center amplitude equal to zero. The latter is precisely the strong-stable manifold rather than a contradiction to the generic algebraic law.

## Originality

**PASS, to the best of our knowledge.** Thomas (1999) introduced the three-dimensional system. Sprott--Chlouverakis (2007) studied its labyrinth dynamics. Chlouverakis--Sprott (2007) gives the higher-dimensional ring \(\dot x_i=-b x_i+\sin x_{i+1}\), identifies the common-mode eigenvalue crossing at \(b=1\), and describes the pitchfork branches for \(b<1\). That paper's relevant stability/bifurcation section was inspected directly. It says the origin becomes unstable at \(b=1\), but its displayed nonzero branches satisfy \(x^*\approx\pm\sqrt{6(1-b)}\) and therefore lie on the \(b<1\) side. Searches in the paper for center-manifold, asymptotic, algebraic, slow, and decay formulations did not locate a critical endpoint rate theorem.

Sorin--Tulchinsky (2024) was also inspected at the relevant primary-readable section. It proves/argues global stability in the strict \(b>1\) regime and then discusses the \(b<1\) pitchfork. Its displayed fixed-point equation is \(b x=\sin x\), which at exactly \(b=1\) has only the zero real solution. No endpoint algebraic-rate law was found there. Ho (2019) studies the high-dimensional Thomas generalization in low-damping chaotic/random-walk regimes rather than the \(b=1\) nonhyperbolic relaxation problem.

Targeted searches included critical Thomas stability, nonhyperbolic \(b=1\), algebraic decay, critical slowing, reciprocal-square asymptotics, and the higher-dimensional hyperlabyrinth ring. They did not locate the formula
\[
1/x_i(t)^2=t/3-(1/20)\log t+C+o(1)
\]
or the global endpoint closure stated here. General center-manifold and strong-stable theory supplies the qualitative reduction mechanism, so no methodological novelty is claimed for that theory.

The main residual priority risk is Thomas (1999), DOI 10.1142/S0218127499001383. Its bibliographic record and secondary citations were available, but the complete theorem-level text was not inspected. It is the most plausible older source that could reduce priority for the three-dimensional endpoint statement. The accessible 2007 papers are later detailed treatments and substantially reduce, but do not eliminate, that risk.

## Value

**PASS.** The classical route-to-chaos literature organizes the first transition at \(b=1\), but a zero linear eigenvalue does not decide what happens at the parameter value itself. The theorem closes that gap globally: the origin remains attracting at the threshold and loses stability only on the \(b<1\) side.

The rate theorem adds more than endpoint classification. It distinguishes the codimension-one exponential exceptional set from generic trajectories, proves exponential synchronization across the cyclic ring, and identifies both the universal leading constant \(\sqrt3\) and the first non-summable correction \(-(1/20)\log t\) in reciprocal square. This gives a quantitative critical-slowing law for every ring dimension \(N\ge3\).

## Scientific limitations

The result concerns the unforced deterministic cyclic sine ring exactly at \(b=1\). It does not provide a uniform crossover law as \(b\to1\), nor does it cover delayed, fractional, externally forced, or more general network-coupled Thomas systems. The sharp coefficients follow from the sine Taylor series and will change under nonlinear perturbations. The literature search cannot exclude every older source, especially the incompletely inspected 1999 original article. Originality is therefore explicitly limited to the best of our knowledge.
