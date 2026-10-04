# Same-model scientific review

## Correctness
**PASS.** For \(H=x_3+x_1^2/(2a)\), direct differentiation gives \(\dot H=b-x_1^2\) with exact cancellation of the mixed term. Bounded forward motion then forces the long-time mean \(T^{-1}\int_0^T x_1(t)^2\,dt\) to converge to \(b\), immediately excluding \(b<0\). At \(b=0\), recurrence returns the continuous function \(H\) to its initial value while \(H\) is nonincreasing; hence \(x_1\equiv0\), and the vector field then forces \(x_2=x_4=0\) and constant \(x_3\). For a compactly supported invariant measure, integrating the Lie derivatives of \(x_4\), \(x_1\), \(H\), and \(x_3\) yields the stated first- and second-moment identities. The bundled symbolic checker reproduces the exact algebra. No finite simulation is used as an infinite proof.

## Originality
**PASS.** The introducing 2020 article was inspected in full accessible text at the defining equations, boundedness discussion, symmetry discussion, and multistability section. Searches for stationary mean-square laws, forcing-selected root-mean-square amplitude, and the exact balance did not locate an equivalent claim. The paper already explains that periodic nonlinearities replicate attractors with the same properties, so that symmetry mechanism is treated as prior work and is not claimed here. The closest inspected 2016 Sprott-B predecessor was available only through abstract/publisher-preview material; that incomplete access is retained as a residual risk rather than being used to assert noncoverage. Database hits on exact recurrence balances for other named chaotic flows do not imply the present object-specific identity.

## Value
**PASS.** The source explicitly identifies analytic boundedness as difficult and relies on simulations for the displayed bounded regimes. The balance provides a parameter-level structural law that applies to every bounded forward trajectory and every compact stationary state: negative forcing is impossible for bounded motion, zero forcing has only equilibrium recurrence, and positive forcing fixes the exact stationary variance \(\operatorname{Var}(x_1)=b\) independently of the sinusoidal gain. This is a meaningful global restriction and a direct consistency condition for any claimed periodic or chaotic attractor.

## Closest literature and limitations
The primary source is Lai, Kuate, Pei, and Fotsin, *Complexity* 2020, DOI 10.1155/2020/8175639. The closest explicit predecessor inspected is Lai and Chen, *International Journal of Bifurcation and Chaos* 2016, DOI 10.1142/S0218127416501777, but only abstract-level material was lawfully accessible in the inspected source. The theorem does not prove existence of a bounded attractor, validate Lyapunov computations, determine basin sizes, or classify every bounded trajectory at \(b=0\). Unindexed or inaccessible literature remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
