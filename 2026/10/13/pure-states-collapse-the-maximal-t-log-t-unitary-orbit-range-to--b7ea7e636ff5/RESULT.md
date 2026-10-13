# Pure states collapse the maximal \(t\log t\) unitary-orbit range to two values

## Finding
Let \(P\) be a rank-one projector on a finite-dimensional Hilbert space of dimension at least \(2\), and set
\[
f(t)=t\log t.
\]
For the maximal quantum \(f\)-divergence \(\widehat S_f\) defined by the standard epsilon regularization, the entire unitary-orbit profile is
\[
\widehat S_f(P\|U^*PU)=
\begin{cases}
0,&U^*PU=P,\\
+\infty,&U^*PU\ne P.
\end{cases}
\]
Consequently,
\[
\left\{\widehat S_f(P\|U^*PU):U\in\mathbb U_n\right\}=\{0,+\infty\}.
\]
Nguyen, Nguyen, and Le state in Corollary 3.3 that for arbitrary quantum states this orbit image is exactly the interval between the same-order and opposite-order spectral endpoints. For \(\rho=\sigma=P\), those endpoints are \(0\) and \(+\infty\), so the claimed interval is \([0,+\infty]\), whereas every finite positive value is absent. Thus Corollary 3.3 is false on singular states for the Belavkin--Staszewski choice \(f(t)=t\log t\).

## Assumptions and scope
The dimension is finite and at least \(2\). The state \(P\) has rank one. The function is exactly \(f(t)=t\log t\), an operator-convex function on \((0,\infty)\) with \(f(1)=0\). The maximal divergence is the regularized commutant-Radon--Nikodym divergence used by the source. The claim concerns the orbit-range and continuity assertions for singular states; it does not assert that the source's minimum and maximum values are wrong in this example.

A direct sufficient repair of the affected range statement is to restrict it to faithful states \(\rho,\sigma>0\), where the orbit remains inside a compact positive-definite spectral class and the inverse/square-root functional calculus used in the source's continuity argument stays away from the singular boundary. No broader optimal repair for all singular pairs is claimed.

## Proof
Write \(Q=U^*PU\). If \(Q=P\), then the two arguments coincide, and since \(f(1)=0\), one has \(\widehat S_f(P\|P)=0\).

Assume \(Q\ne P\). Put
\[
c=\operatorname{Tr}(PQ).
\]
Because \(P\) and \(Q\) are distinct rank-one projectors, \(0\le c<1\). Consider the two-outcome projective measurement channel in the \(Q\)-support decomposition,
\[
\Phi(X)=\bigl(\operatorname{Tr}(QX),\operatorname{Tr}((I-Q)X)\bigr).
\]
Then
\[
\Phi(P)=(c,1-c),\qquad \Phi(Q)=(1,0).
\]
For \(f(t)=t\log t\), the classical \(f\)-divergence is the Kullback--Leibler divergence. Therefore
\[
S_f(\Phi(P)\|\Phi(Q))
=c\log c+(1-c)\log\frac{1-c}0
=+\infty,
\]
where the last equality is the usual extended-value convention because \(1-c>0\).

Maximal quantum \(f\)-divergence is monotone non-increasing under quantum channels. Hence
\[
+\infty
=S_f(\Phi(P)\|\Phi(Q))
=\widehat S_f(\Phi(P)\|\Phi(Q))
\le \widehat S_f(P\|Q),
\]
which forces \(\widehat S_f(P\|Q)=+\infty\). This proves the two-valued orbit formula.

The same conclusion is consistent with the standard Belavkin--Staszewski support criterion: \(\widehat D(\rho\|\sigma)\) is finite only when \(\ker\sigma\subseteq\ker\rho\). For rank-one \(P,Q\) of equal rank, that inclusion holds exactly when \(P=Q\).

Finally, the source's Corollary 3.3 explicitly claims that the orbit image for arbitrary quantum states is the interval between the same-order and opposite-order spectral configurations. For \(P\), the same-order endpoint is \(0\) and the opposite-order endpoint is \(+\infty\); the proved image \(\{0,+\infty\}\) omits, for example, \(1\). The source's continuity step therefore cannot apply at this singular boundary.

## Verification
The proof is analytic and contains no finite enumeration. The critical nonstandard input is the data-processing inequality for maximal quantum \(f\)-divergence, documented in Hiai--Mosonyi's full treatment of maximal \(f\)-divergences. Their treatment also defines the singular extension by epsilon regularization and allows extended-real values. Independently, the standard Belavkin--Staszewski formula records \(+\infty\) when the support condition fails.

The counterexample is stress-tested against the source's endpoints rather than against an inferred formula: the source itself states Corollary 3.3 for arbitrary quantum states and proves it by continuity of the orbit objective. In the present example the objective is \(0\) on the stabilizer of \(P\) and \(+\infty\) everywhere else on the pure-state orbit, so it is not continuous there and no intermediate finite value occurs.

## Relationship to prior work
Nguyen, Nguyen, and Le define the maximal quantum \(f\)-divergence for general positive semidefinite states by epsilon regularization and state Theorems 3.1--3.2 plus Corollary 3.3 for arbitrary quantum states. Corollary 3.3 says the full orbit range is exactly the interval between the two spectral extrema, and its proof invokes continuity of the expression containing \((U^*\sigma U)^{-1/2}\). The source does not separate the singular case in that argument.

Hiai and Mosonyi give the foundational treatment of maximal quantum \(f\)-divergences, including the singular regularization and monotonicity under positive maps. Their results supply the data-processing premise used above, not the source-specific orbit counterexample. Later literature on Belavkin--Staszewski entropy records the same support condition explicitly. Searches for the exact source identifier, Corollary 3.3, pure-projector orbit formulations, support-mismatch formulations, and the two-point range \(\{0,+\infty\}\) found no published correction of this source-specific statement.

## Limitations
The counterexample uses singular pure states and the specific operator-convex generator \(f(t)=t\log t\). It disproves the all-quantum-state interval-range statement as written but does not invalidate the faithful-state version, and it does not by itself disprove the source's endpoint values. The literature search cannot exclude an unindexed independent observation. The exact best extension of the interval theorem to partially singular states for general operator-convex \(f\) is not classified here.

## References
1. H. M. Nguyen, H. A. Nguyen, and C. T. Le, “Optimization of maximal quantum \(f\)-divergences between unitary orbits,” arXiv:2601.08268v2, first public 13 January 2026.
2. F. Hiai and M. Mosonyi, “Different quantum \(f\)-divergences and the reversibility of quantum operations,” Reviews in Mathematical Physics 29 (2017), 1750023; arXiv:1604.03089.
3. “Belavkin--Staszewski Quantum Markov Chains,” Annales Henri Poincaré, 2025/2026 online article; preliminary section records the finite-support condition and \(+\infty\) otherwise for Belavkin--Staszewski entropy.
