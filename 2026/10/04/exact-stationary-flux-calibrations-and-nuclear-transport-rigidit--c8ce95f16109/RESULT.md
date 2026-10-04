# Exact stationary flux calibrations and nuclear-transport rigidity in Goldbeter's circadian clock
## Finding
Consider Goldbeter's five-variable model for circadian oscillations of Drosophila PER protein:
\[
\dot M=S(P_N)-D_M(M),
\]
\[
\dot P_0=k_sM+J_2(P_1)-J_1(P_0),
\]
\[
\dot P_1=J_1(P_0)+J_4(P_2)-J_2(P_1)-J_3(P_1),
\]
\[
\dot P_2=J_3(P_1)+k_2P_N-J_4(P_2)-k_1P_2-D_2(P_2),
\]
\[
\dot P_N=k_1P_2-k_2P_N,
\]
where
\[
S(P_N)=\frac{v_sK_I^n}{K_I^n+P_N^n},
\qquad
D_M(M)=\frac{v_mM}{k_m+M},
\]
\[
J_1(P_0)=\frac{V_1P_0}{K_1+P_0},
\qquad
J_2(P_1)=\frac{V_2P_1}{K_2+P_1},
\]
\[
J_3(P_1)=\frac{V_3P_1}{K_3+P_1},
\qquad
J_4(P_2)=\frac{V_4P_2}{K_4+P_2},
\]
and
\[
D_2(P_2)=\frac{v_dP_2}{k_d+P_2}.
\]

Assume all kinetic constants and \(n\) are positive and the state is in the nonnegative concentration orthant.

Every compactly supported invariant Borel probability measure \(\mu\) satisfies five exact state-slice flux calibrations:
\[
\boxed{
\mathbb E_\mu[S(P_N)\mid M]=D_M(M)
},
\]
\[
\boxed{
\mathbb E_\mu[k_sM+J_2(P_1)\mid P_0]=J_1(P_0)
},
\]
\[
\boxed{
\mathbb E_\mu[J_1(P_0)+J_4(P_2)\mid P_1]
=
J_2(P_1)+J_3(P_1)
},
\]
\[
\boxed{
\mathbb E_\mu[J_3(P_1)+k_2P_N\mid P_2]
=
J_4(P_2)+k_1P_2+D_2(P_2)
},
\]
and
\[
\boxed{
\mathbb E_\mu[k_1P_2\mid P_N]=k_2P_N
}.
\]

For every coordinate, the variance lost by replacing its total input flux with the state-determined output flux is exactly the mean-square coordinate speed. For example,
\[
\operatorname{Var}_\mu(S(P_N))
-
\operatorname{Var}_\mu(D_M(M))
=
\mathbb E_\mu[\dot M^2],
\]
and
\[
k_1^2\operatorname{Var}_\mu(P_2)
-
k_2^2\operatorname{Var}_\mu(P_N)
=
\mathbb E_\mu[\dot P_N^2].
\]

The two endpoint defects are rigid:
\[
\mathbb E_\mu[\dot M^2]=0
\]
or
\[
\mathbb E_\mu[\dot P_N^2]=0
\]
holds exactly when \(\mu\) is supported on equilibria.

Thus every non-equilibrium compact stationary state satisfies the strict endpoint attenuation laws
\[
\operatorname{Var}_\mu(S(P_N))
>
\operatorname{Var}_\mu(D_M(M))
\]
and
\[
k_1^2\operatorname{Var}_\mu(P_2)
>
k_2^2\operatorname{Var}_\mu(P_N).
\]
It also gives positive mass to both sides of the two endpoint balance surfaces
\[
S(P_N)=D_M(M)
\]
and
\[
k_1P_2=k_2P_N.
\]

The nuclear variable has a complementary exact memory representation on every bounded complete trajectory:
\[
\boxed{
P_N(t)
=
k_1\int_0^\infty e^{-k_2u}P_2(t-u)\,du
}.
\]
At stationarity this stable exponential memory is paired with the instantaneous projection law
\[
\boxed{
\mathbb E_\mu[P_2\mid P_N]
=
\frac{k_2}{k_1}P_N
}.
\]

## Assumptions and scope
The invariant measure is supported on a compact subset of the nonnegative concentration orthant. Compact support justifies the one-variable antiderivative tests below.

The model is the five-variable PER clock introduced by Goldbeter in 1995. Its mechanism combines transcriptional negative feedback, multiple phosphorylation of PER, degradation, and reversible nuclear transport. Later full mathematical treatments write exactly the five equations used here.

The earliest verified public source date is 22 September 1995.

The statement is classified under MSC \(37N25\), dynamical systems in biology. Same-object mathematical work on Goldbeter's five-variable circadian oscillator lists \(37N25\) among its dynamical-systems classifications.

The theorem does not assume ergodicity and therefore applies componentwise to any compact invariant statistical state.

## Proof
Write each equation as
\[
\dot X=A-B(X),
\]
where \(A\) is the total input flux and \(B(X)\) is the total output flux depending only on the coordinate \(X\).

Let \(\phi\) be any continuous function on the compact \(X\)-range and let \(H\) be a continuously differentiable antiderivative:
\[
H'(X)=\phi(X).
\]
For the flow generator \(L\),
\[
LH=\phi(X)(A-B(X)).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(X)(A-B(X))]=0
\]
for every continuous \(\phi\). Hence
\[
\mathbb E_\mu[A\mid X]=B(X).
\]
Applying this separately to \(M,P_0,P_1,P_2,P_N\) gives the five displayed flux calibrations.

A conditional expectation is an orthogonal projection in \(L^2\). Therefore
\[
\operatorname{Var}_\mu(A)
=
\operatorname{Var}_\mu(B(X))
+
\mathbb E_\mu[(A-B(X))^2].
\]
Since
\[
A-B(X)=\dot X,
\]
we obtain the exact variance-speed defect for every coordinate.

For \(M\),
\[
A=S(P_N),
\qquad
B=D_M(M),
\]
so
\[
\operatorname{Var}(S(P_N))
-
\operatorname{Var}(D_M(M))
=
\mathbb E[\dot M^2].
\]

For \(P_N\),
\[
A=k_1P_2,
\qquad
B=k_2P_N,
\]
so
\[
k_1^2\operatorname{Var}(P_2)
-
k_2^2\operatorname{Var}(P_N)
=
\mathbb E[\dot P_N^2].
\]

We now prove endpoint rigidity.

Suppose
\[
\mathbb E[\dot P_N^2]=0.
\]
Then \(\dot P_N=0\) on the invariant support. Along every support trajectory, \(P_N\) is constant and
\[
k_1P_2=k_2P_N,
\]
so \(P_2\) is constant. The \(P_2\)-equation reduces to
\[
J_3(P_1)=J_4(P_2)+D_2(P_2).
\]
The function \(J_3\) is strictly increasing on the nonnegative half-line, so \(P_1\) is constant. Then the \(P_1\)-equation forces \(J_1(P_0)\) to be constant; strict monotonicity of \(J_1\) makes \(P_0\) constant. The \(P_0\)-equation then makes \(M\) constant. Thus the whole trajectory is an equilibrium.

Conversely, every equilibrium-supported probability measure has
\[
\dot P_N=0.
\]

Suppose instead that
\[
\mathbb E[\dot M^2]=0.
\]
Then \(M\) is constant on every support trajectory and
\[
S(P_N)=D_M(M)
\]
is constant. The Hill repression function \(S\) is one-to-one on the nonnegative half-line, so \(P_N\) is constant. The preceding propagation argument again forces all five coordinates to be constant. Hence this endpoint defect also vanishes exactly on equilibrium-supported measures.

For a non-equilibrium compact invariant measure, both endpoint speeds therefore have strictly positive second moments. Invariance of the coordinate functions gives
\[
\mathbb E[\dot M]=0,
\qquad
\mathbb E[\dot P_N]=0.
\]
A nonzero square-integrable zero-mean random variable must be positive and negative on sets of positive measure. Thus the measure crosses both endpoint flux-balance surfaces.

Finally solve the stable linear nuclear-transport equation along a bounded complete trajectory:
\[
\dot P_N+k_2P_N=k_1P_2.
\]
Variation of constants gives
\[
P_N(t)
=
e^{-k_2T}P_N(t-T)
+
k_1\int_0^T e^{-k_2u}P_2(t-u)\,du.
\]
Boundedness and \(k_2>0\) let \(T\to\infty\), yielding
\[
P_N(t)
=
k_1\int_0^\infty e^{-k_2u}P_2(t-u)\,du.
\]
The final instantaneous projection follows from the \(P_N\)-slice calibration after division by \(k_1\).

## Verification
The accompanying checker verifies the residual-variance algebra and the nuclear scaling identity using exact rational arithmetic.

It checks that the two moment consequences of
\[
\mathbb E[A\mid X]=B(X),
\]
namely
\[
\mathbb E[A]=\mathbb E[B]
\]
and
\[
\mathbb E[AB]=\mathbb E[B^2],
\]
give exactly
\[
\mathbb E[(A-B)^2]
=
\operatorname{Var}(A)-\operatorname{Var}(B).
\]

It also verifies the coefficient conversion
\[
\operatorname{Var}(k_1P_2)-\operatorname{Var}(k_2P_N)
=
k_1^2\operatorname{Var}(P_2)-k_2^2\operatorname{Var}(P_N).
\]

The stored checker output is `VERIFY_OK`.

The five conditional laws, endpoint equality classification, crossing result, and exponential-memory representation are analytic proofs and are not inferred from finite numerical experiments.

## Relationship to prior work
Goldbeter's 1995 paper introduced the five-stage PER clock and identified multiple phosphorylation, transcriptional negative feedback, PER degradation, and nuclear transport as mechanisms controlling circadian oscillation. The original article's abstract and bibliographic record were inspected; the full article was not securely available in the inspected route, so no whole-document noncoverage assertion is made.

The curated Physiome implementation reproduces the original published model and its Figure 2, supporting equation-level provenance.

A complete 2021 mathematical model-reduction article writes all five Goldbeter equations explicitly and studies their stable limit-cycle behavior using differential balancing. Its Goldbeter section and the full article were searched for invariant-measure and average statements; no such formulation was located. The occurrence of the word “variance” is in unrelated model-reduction references, not a stationary biochemical flux theorem.

Forger and Kronauer apply averaging to Goldbeter's five-variable clock and relate it to van der Pol-type circadian models. The accessible abstract and classification metadata establish a close mathematical treatment of the same object, but the complete article was not available in the inspected route.

Targeted literature searches for invariant measures, stationary fluxes, phosphorylation-chain variance identities, and nuclear-transport conditional laws did not reveal a statement implying the five simultaneous calibrations or the endpoint rigidity result.

## Limitations
The theorem concerns compactly supported invariant probability measures in the nonnegative concentration orthant.

The three interior flux defects are proved nonnegative but are not individually claimed to have equilibrium-only equality; endpoint rigidity is asserted only for the \(M\) and \(P_N\) defects.

The result does not determine the oscillation period, phase lag, bifurcation interval, or full invariant density.

The original 1995 article was not available as a securely readable full text in the inspected route. It remains a residual originality risk, although the accepted claim is stronger than a global time-average balance because it consists of conditional flux laws plus variance defects and endpoint equality rigidity.

Because the generator argument is concise, an equivalent formulation could remain in unindexed biochemical-oscillator literature.

## References
1. A. Goldbeter, “A Model for Circadian Oscillations in the Drosophila Period Protein (PER),” Proceedings of the Royal Society of London. Series B 261, 319–324 (1995), DOI 10.1098/rspb.1995.0153.
2. Physiome Model Repository, “Goldbeter, 1995,” curated CellML implementation of the published five-variable model.
3. A. Padoan, F. Forni, and R. Sepulchre, “Balanced truncation for model reduction of biological oscillators,” Biological Cybernetics 115, 383–395 (2021), DOI 10.1007/s00422-021-00888-4.
4. D. B. Forger and R. E. Kronauer, “Reconciling Mathematical Models of Biological Clocks by Averaging on Approximate Manifolds,” SIAM Journal on Applied Mathematics 62, 1281–1296 (2002), DOI 10.1137/S0036139900373587.
