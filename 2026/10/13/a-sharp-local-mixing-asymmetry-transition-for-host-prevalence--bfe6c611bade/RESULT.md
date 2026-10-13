# A sharp local mixing-asymmetry transition for host prevalence
## Finding
In the two-patch homogeneous Ross–Macdonald specialization of Gao and Lou (2025), set \(V=V_0>1\), fix total host-movement connectivity \(q=L_{12}+L_{21}>0\), and vary only directional asymmetry by \(L_{12}=q(1/2+d)\), \(L_{21}=q(1/2-d)\) with \(|d|<1/2\). Let \(\mathcal P(d)\) and \(\mathscr P(d)\) be the endemic global host and vector prevalences. Around balanced movement \(d=0\), writing \(D=V^2+2Vq-1\) and \(N=(V-1)^3+2(1+q)(V-1)^2-4q\), one has
\[
\mathcal P''(0)=-\frac{16V^2N}{(V+1)^2D^2},\qquad
\mathscr P''(0)=\frac{16Vq}{D^2}>0.
\]
For each \(q>0\), the equation \(y^3+2(1+q)y^2-4q=0\) has a unique positive root \(y_c(q)\). Hence balanced movement is a strict local minimum of host prevalence when \(1<V<1+y_c(q)\), a strict local maximum when \(V>1+y_c(q)\), and always a strict local minimum of vector prevalence. This gives an exact local phase boundary for the source paper's numerical observation that mixing asymmetry can raise host prevalence near the persistence threshold but lower it at larger vector abundance, while locally raising vector prevalence in both regimes.

## Assumptions and scope
The claim concerns Example 5.3 of Gao and Lou's two-patch homogeneous vector-borne disease model after their normalization \(a=b=c=\mu=\gamma=H=\varepsilon=1\) and \(V_1=V_2=V/2\). The connectivity convention is \(L_{12}>0\), \(L_{21}>0\), \(L_{11}=-L_{21}\), and \(L_{22}=-L_{12}\). Fix \(q=L_{12}+L_{21}>0\) and parameterize asymmetry by
\[
\alpha_1=\frac{L_{12}}q=\frac12+d,\qquad \alpha_2=\frac{L_{21}}q=\frac12-d,
\]
so that changing \(d\) redistributes directionality while keeping total connectivity fixed. The result assumes \(V>1\), for which the balanced point has a positive endemic equilibrium. It is a local statement near \(d=0\); it does not classify arbitrary large asymmetry.

The source's reduced endemic equations become
\[
F_i(I_1,I_2,d)=\frac{V}{2\alpha_i}\frac{\alpha_i-I_i}{\alpha_i+I_i}I_i-I_i+\sum_{{j=1}}^2L_{{ij}}I_j=0,
\]
with global host prevalence \(\mathcal P=I_1+I_2\). Since \(\sigma_i=1\) and \(V_i=V/2\), the global vector prevalence is
\[
\mathscr P=\frac12\left(\frac{I_1}{\alpha_1+I_1}+\frac{I_2}{\alpha_2+I_2}\right).
\]

## Proof
At \(d=0\), symmetry gives
\[
I_1=I_2=s:=\frac{V-1}{2(V+1)},
\]
which reproduces the source formula \(\mathcal P(0)=(V-1)/(V+1)\) and \(\mathscr P(0)=(V-1)/(2V)\). The derivative of the local nonlinear term with respect to \(I\) at \((I,\alpha)=(s,1/2)\) equals
\[
-\frac{(V-1)(V+1)}{2V}<0.
\]
The equilibrium Jacobian therefore has symmetric and antisymmetric eigenvalues equal to this quantity and this quantity minus \(q\), respectively. Both are negative, so the implicit-function theorem gives a unique analytic endemic branch near \(d=0\).

Patch exchange sends \(d\) to \(-d\), so write
\[
I_1=s+A d+B d^2+O(d^3),\qquad
I_2=s-A d+B d^2+O(d^3).
\]
Substitution into the two equilibrium equations and comparison of the first two powers of \(d\) gives
\[
A=\frac{(V-1)(V^2+2Vq-2V-1)}{(V+1)(V^2+2Vq-1)}
\]
and
\[
B=-\frac{4V^2\left[V^3+2V^2q-V^2-4Vq-V-2q+1\right]}{(V+1)^2(V^2+2Vq-1)^2}.
\]
The bracket factors after setting \(y=V-1\) as
\[
N=y^3+2(1+q)y^2-4q.
\]
Because \(\mathcal P(d)=I_1(d)+I_2(d)\) is even in \(d\),
\[
\mathcal P(d)=\frac{V-1}{V+1}-\frac{8V^2N}{(V+1)^2D^2}d^2+O(d^4),
\qquad D=V^2+2Vq-1,
\]
which yields the displayed formula for \(\mathcal P''(0)\).

Using the source's vector-prevalence formula and the same expansion gives
\[
\mathscr P(d)=\frac{V-1}{2V}+\frac{8Vq}{D^2}d^2+O(d^4),
\]
so \(\mathscr P''(0)=16Vq/D^2>0\).

Finally, for fixed \(q>0\), define \(G_q(y)=y^3+2(1+q)y^2-4q\). On \(y>0\),
\[
G_q'(y)=3y^2+4(1+q)y>0,
\]
while \(G_q(0)=-4q<0\) and \(G_q(y)\to\infty\). Thus there is exactly one positive root \(y_c(q)\), and the sign of \(\mathcal P''(0)\) changes exactly once as stated.

## Verification
The standalone checker `verify.py` symbolically substitutes the second-order ansatz into the exact normalized equilibrium equations, verifies both coefficient formulas, verifies the host and vector curvature formulas, checks the factorization of \(N\), and performs independent numerical finite-difference checks for representative parameter pairs on opposite sides of the transition. No finite experiment is used as proof; the symbolic identities and monotonicity argument establish the claim.

For example, at fixed \(q=1\), the unique transition is \(V_c\approx1.9032119259\). Thus \(V=1.2\) lies in the local host-minimum regime and \(V=2\) in the local host-maximum regime, matching the direction of the source paper's two numerical abundance examples near balanced movement.

## Relationship to prior work
Gao and Lou derive the reduced endemic equations, define both global prevalences, and in Example 5.3 numerically compare asymmetric connectivity at \(V=1.2\) and \(V=2\). They report that nonhomogeneous mixing generally raises both prevalences at the smaller vector abundance but generally lowers host prevalence while raising vector prevalence at the larger abundance. Their article does not state a local curvature formula or an exact abundance/connectivity boundary separating these host responses.

Gao, van den Driessche, and Cosner prove that nonhomogeneous host/vector distributions in a homogeneous Ross–Macdonald environment increase the basic reproduction number; that persistence result does not determine endemic host or vector prevalence curvature. Gao and Li prove a prevalence-reduction theorem for a different SIS setting in which susceptible and infected hosts use different movement patterns; it does not imply the Ross–Macdonald host/vector phase boundary here.

## Limitations
This is a local theorem about directional asymmetry at fixed \(q\), not a global classification over the full \((L_{12},L_{21})\) plane. At the codimension-one boundary \(V=1+y_c(q)\), the quadratic host-prevalence term vanishes; no claim is made here about the sign of the next nonzero even term. The theorem uses the normalized homogeneous parameter choice of Example 5.3 and does not assert the same formula under heterogeneous biting, recovery, vector mortality, vector abundance, or patch demography. The mathematical result concerns equilibrium prevalence, not transient incidence or intervention outcomes.

## References
1. D. Gao and Y. Lou, “Effect of host movement on the prevalence of vector-borne diseases,” *Journal of Mathematical Biology* 91, 33 (2025), DOI: 10.1007/s00285-025-02254-5.
2. D. Gao, P. van den Driessche, and C. Cosner, “Habitat fragmentation promotes malaria persistence,” *Journal of Mathematical Biology* 79, 2255–2280 (2019), DOI: 10.1007/s00285-019-01428-2.
3. D. Gao and X. Li, “Nonhomogeneous mixing reduces disease prevalence,” *Mathematical Biosciences* 388, 109521 (2025), DOI: 10.1016/j.mbs.2025.109521.
