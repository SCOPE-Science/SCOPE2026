# Mean-selection laws for recurrent states in a shared-predation fear model
## Finding
Consider the shared-predation model
\[
\dot u_i=u_i\!\left(\frac{r_i}{1+k_i v}-d_i-a_i u_i-p_i v\right)\quad(i=1,2),\qquad
\dot v=v(c_1p_1u_1+c_2p_2u_2-m),
\]
with all parameters positive. This is the linear-functional-response case of Wang and Smit's two-prey/one-predator fear model. Assume that the positive equilibrium \(E_*=(u_{1*},u_{2*},v_*)\) exists and is unique. Set \(A_i=c_ip_i\).

Let \(\mu\) be any compactly supported invariant Borel probability measure whose support is a compact subset of the strict positive octant. With
\[
\bar u_i=\int u_i\,d\mu,\qquad \bar v=\int v\,d\mu,
\]
define
\[
J_i=\frac{k_i^2}{(1+k_i\bar v)^2}\int\frac{(v-\bar v)^2}{1+k_i v}\,d\mu,
\qquad
C_i=\frac{k_i}{(1+k_i v_*)(1+k_i\bar v)}.
\]
Then
\[
A_1\bar u_1+A_2\bar u_2=m=A_1u_{1*}+A_2u_{2*},
\]
\[
a_i(\bar u_i-u_{i*})=r_iJ_i-(p_i+r_iC_i)(\bar v-v_*)\quad(i=1,2),
\]
and therefore
\[
\boxed{\;\bar v-v_*=\frac{\displaystyle\sum_{i=1}^2 A_i r_iJ_i/a_i}{\displaystyle\sum_{i=1}^2 A_i(p_i+r_iC_i)/a_i}\;}.
\]
If \(\mu\ne\delta_{E_*}\), then \(J_1,J_2>0\), so
\[
\boxed{\bar v>v_*}.
\]
Thus every non-equilibrium compact interior recurrent statistical state has predator mean strictly above the coexistence-equilibrium predator coordinate, while its weighted prey mean remains exactly fixed by \(A_1\bar u_1+A_2\bar u_2=m\).

There is a sharper law when the two similar prey have the same fear sensitivity, \(k_1=k_2=k>0\). In that case \(J_1=J_2=:J\) and \(C_1=C_2=:C\). If \(r_1p_2\ne r_2p_1\), then
\[
\boxed{\operatorname{sgn}(\bar u_1-u_{1*})=\operatorname{sgn}(r_1p_2-r_2p_1),\qquad
\operatorname{sgn}(\bar u_2-u_{2*})=-\operatorname{sgn}(r_1p_2-r_2p_1)}.
\]
If \(r_1p_2=r_2p_1\), then both prey means equal their equilibrium coordinates even though \(\bar v>v_*\). In particular, every strictly positive nonconstant periodic orbit, if one exists, obeys these identities with period averages.

## Assumptions and scope
All parameters are strictly positive. The measure is required to have compact support contained in \((0,\infty)^3\); this makes \(\log u_1\), \(\log u_2\), and \(\log v\) legitimate bounded \(C^1\) observables on a neighborhood of the support. The positive equilibrium is assumed to exist and be unique, as in the existence regime identified for the linear-response system by Wang and Smit.

The strict conclusion concerns non-equilibrium invariant measures supported wholly in the interior. Boundary invariant sets are outside the claim. The equal-fear sorting rule is a corollary for the symmetric sensitivity case \(k_1=k_2\), not an assumption needed for the general predator-mean inequality.

## Proof
For an invariant probability measure and any \(C^1\) observable \(\phi\) on the compact invariant support, \(\int L\phi\,d\mu=0\), where \(L\) is the Lie derivative of the vector field. Applying this to \(\log u_i\) gives
\[
0=r_i\int\frac{1}{1+k_i v}\,d\mu-d_i-a_i\bar u_i-p_i\bar v.
\]
Applying it to \(\log v\) gives
\[
A_1\bar u_1+A_2\bar u_2=m.
\]
At the positive equilibrium,
\[
0=\frac{r_i}{1+k_i v_*}-d_i-a_i u_{i*}-p_i v_*,
\qquad
A_1u_{1*}+A_2u_{2*}=m.
\]

For any \(k>0\), \(v>0\), and mean \(\bar v\), the algebraic identity
\[
\frac{1}{1+kv}=
\frac{1}{1+k\bar v}
-\frac{k(v-\bar v)}{(1+k\bar v)^2}
+\frac{k^2(v-\bar v)^2}{(1+k\bar v)^2(1+kv)}
\]
is exact. Averaging removes the linear term, so
\[
\int\frac{1}{1+k_i v}\,d\mu=\frac{1}{1+k_i\bar v}+J_i.
\]
Also
\[
\frac{1}{1+k_i\bar v}-\frac{1}{1+k_i v_*}
=-C_i(\bar v-v_*).
\]
Subtracting the equilibrium prey equations from the averaged prey equations therefore yields
\[
a_i(\bar u_i-u_{i*})=r_iJ_i-(p_i+r_iC_i)(\bar v-v_*).
\]
Subtracting the equilibrium predator balance from the averaged predator balance gives
\[
A_1(\bar u_1-u_{1*})+A_2(\bar u_2-u_{2*})=0.
\]
Substitution and solution for \(\bar v-v_*\) prove the displayed quotient formula. Its denominator is positive and each \(J_i\ge0\).

It remains to justify strictness. Suppose \(J_i=0\) for one, hence every, \(i\). Because \(k_i>0\) and the integrand is nonnegative with a strictly positive denominator, this is equivalent to \(v=\bar v\) \(\mu\)-almost surely. The support of an invariant measure is invariant, so every complete trajectory in the support has constant predator coordinate \(v_0\). Along such a trajectory the two prey equations become independent scalar logistic equations
\[
\dot u_i=u_i(b_i-a_i u_i),\qquad b_i=\frac{r_i}{1+k_i v_0}-d_i-p_i v_0.
\]
A nonconstant scalar logistic trajectory cannot remain for all positive and negative time in a compact interval bounded away from zero. Hence each \(u_i\) is constant on every trajectory in the support. The support therefore consists of positive equilibria; uniqueness forces it to be \(\{E_*}\). Consequently every non-equilibrium interior invariant measure has \(J_i>0\) and \(\bar v>v_*\).

For the equal-fear case, let
\[
B_i=p_i+r_iC,\qquad W_i=\frac{A_iB_i}{a_i},\qquad q_i=\frac{r_i}{B_i}.
\]
The quotient formula becomes
\[
\frac{\bar v-v_*}{J}=\frac{W_1q_1+W_2q_2}{W_1+W_2},
\]
a strict weighted average of \(q_1\) and \(q_2\) when they differ. Moreover
\[
q_1-q_2=
\frac{r_1p_2-r_2p_1}{(p_1+r_1C)(p_2+r_2C)}.
\]
Since
\[
\bar u_i-u_{i*}=\frac{B_iJ}{a_i}\left(q_i-\frac{\bar v-v_*}{J}\right),
\]
the stated opposite-sign sorting rule follows. If \(q_1=q_2\), both prey shifts vanish.

## Verification
The accompanying symbolic checker verifies the exact reciprocal expansion, the cancellation producing the predator-mean quotient, and the cancellation of \(C\) from the sign of \(q_1-q_2\). These computations are algebraic checks only; the strictness step is proved analytically above from invariance, compactness, and the scalar logistic dynamics.

The result uses no small-amplitude approximation, no linearization about a cycle, and no finite numerical experiment. For a periodic orbit, the invariant measure is normalized time measure on the orbit, so the theorem immediately yields the corresponding period-average statements.

## Relationship to prior work
Wang and Smit formulate the shared-predation fear model and, for the linear functional response, prove existence and local asymptotic stability of a unique positive equilibrium in their stated parameter regime. They explicitly conjecture global asymptotic stability of that equilibrium. Their paper does not state the invariant-measure identities, the strict predator-mean uplift, or the equal-fear prey sorting law proved here.

The earlier one-prey fear model of Wang, Zanette, and Zou proves global stability for its linear-response planar system by a Dulac argument. That result neither contains the two-prey shared-predator balance nor implies the present mean-selection formulas. Abrams, Holt, and Roth study how population cycles can alter mean prey densities under shared predation in a broader ecological setting; the publicly accessible abstract establishes conceptual proximity, but a complete statement-level comparison of that older article was not available during this verification. It is therefore retained as a residual literature risk rather than treated as evidence of noncoverage.

## Limitations
The theorem is conditional on a compact invariant measure supported strictly inside the positive octant and on existence and uniqueness of the positive equilibrium. It does not establish that a non-equilibrium recurrent interior set exists. In particular, it does not prove or disprove Wang and Smit's conjecture that the positive equilibrium of the linear-response model is globally asymptotically stable whenever it exists.

The distribution-independent prey ordering is proved only for the natural equal-fear case \(k_1=k_2\). For unequal fear sensitivities, the general exact defect identities and strict predator-mean uplift still hold, but the individual prey shifts depend on the two distinct defects \(J_i\).

The comparison with Abrams, Holt, and Roth is limited by incomplete full-text access; their abstract concerns mean-density changes under cycling shared predation, so a possibility of an older related formulation remains a specific residual originality risk.

## References
1. X. Wang and A. Smit, “Studying the fear effect in a predator-prey system with apparent competition,” *Discrete and Continuous Dynamical Systems - B* 28 (2023), 1393–1413. DOI: 10.3934/dcdsb.2022127. First public online date verified as 2022-07-04.
2. X. Wang, L. Y. Zanette, and X. Zou, “Modelling the fear effect in predator–prey interactions,” *Journal of Mathematical Biology* 73 (2016), 1179–1204. DOI: 10.1007/s00285-016-0989-1.
3. P. A. Abrams, R. D. Holt, and J. D. Roth, “Apparent competition or apparent mutualism? Shared predation when populations cycle,” *Ecology* 79 (1998), 201–212. DOI: 10.1890/0012-9658(1998)079[0201:ACOAMS]2.0.CO;2.
