# A sharp global period floor for the Hu–Sang–Wang hyperbolic-sine jerk family
## Finding
Consider the jerk family
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=\varepsilon-a x-b^2y-cz+d\sinh x,
\]
with \(b>0\) and \(d\ne0\). Every compactly supported invariant probability measure \(\mu\) satisfies the exact derivative-energy balance
\[
\int z^2\,d\mu=b^2\int y^2\,d\mu.
\]
Consequently, every nonconstant periodic orbit of minimal period \(T\) satisfies the strict global bound
\[
T>\frac{2\pi}{b}.
\]
For the four one-parameter cases emphasized by Hu, Sang, and Wang, \(b=1\), so every nonconstant periodic orbit has \(T>2\pi\). On the nondegenerate Hopf branches treated in their local theorem, the cycle periods tend to \(2\pi/b\), so the constant is a sharp infimum although it is never attained by a nonconstant cycle.

## Assumptions and scope
The vector field is the five-parameter family printed by Hu, Sang, and Wang. The period statement assumes a classical nonconstant periodic solution and uses its minimal period. The invariant-measure statement assumes a compactly supported invariant probability measure, which is enough to integrate smooth generator coboundaries.

No assertion is made about the existence, uniqueness, stability, or number of periodic orbits away from the Hopf branches already established in the source. The strictness proof uses only \(d\ne0\); it applies to both the symmetric case \(\varepsilon=0\) and the asymmetric case \(\varepsilon\ne0\).

## Proof
Define
\[
H(x,y,z)=yz+\frac a2x^2+\frac c2y^2-d\cosh x-\varepsilon x.
\]
Direct differentiation along the vector field gives
\[
\begin{aligned}
\dot H
&=z^2+y\bigl(\varepsilon-a x-b^2y-cz+d\sinh x\bigr)
   +a x y+c y z-d\sinh(x)y-\varepsilon y\\
&=z^2-b^2y^2.
\end{aligned}
\]
For a compactly supported invariant probability measure, integration of the generator identity yields
\[
0=\int \dot H\,d\mu
 =\int z^2\,d\mu-b^2\int y^2\,d\mu,
\]
which proves the stationary derivative-energy balance.

Now let a nonconstant periodic orbit have minimal period \(T\). Since \(y=\dot x\), its period mean is zero. Integrating the balance over one period gives
\[
\int_0^Tz(t)^2\,dt=b^2\int_0^Ty(t)^2\,dt.
\]
Because \(z=\dot y\), the sharp periodic Wirtinger inequality gives
\[
\int_0^Tz(t)^2\,dt
\ge
\left(\frac{2\pi}{T}\right)^2\int_0^Ty(t)^2\,dt.
\]
The orbit is nonconstant, so \(y\not\equiv0\). Cancellation therefore gives \(T\ge2\pi/b\).

It remains to exclude equality. Equality in Wirtinger's inequality forces \(y\) to be a pure first harmonic. If \(T=2\pi/b\), after a phase shift there are constants \(x_0\) and \(R>0\) such that
\[
x(t)=x_0+R\cos(bt),\qquad
 y(t)=-bR\sin(bt),\qquad
 z(t)=-b^2R\cos(bt).
\]
For this harmonic triple, \(\dot z=-b^2y\). Substitution into the third equation and cancellation of the common term \(-b^2y\) give
\[
0=\varepsilon-a x-cz+d\sinh x.
\]
Since \(z=-b^2(x-x_0)\), the real-analytic function
\[
F(u)=\varepsilon+(-a+cb^2)u-cb^2x_0+d\sinh u
\]
would have to vanish for every \(u\) in the nondegenerate interval \([x_0-R,x_0+R]\). But
\[
F''(u)=d\sinh u,
\]
which cannot vanish on a nondegenerate interval when \(d\ne0\). Thus equality is impossible and \(T>2\pi/b\).

Hu, Sang, and Wang's local Hopf theorem gives, on its nondegenerate bifurcating branches,
\[
T(a)=\frac{2\pi}{b}+O\bigl(|a-a_0|^2\bigr),
\]
so the strict lower edge is approached by actual cycles covered by the source. This proves sharpness of the constant within the family.

## Verification
The accompanying `verifier.py` symbolically differentiates \(H\), substitutes the printed vector field, and checks the identity \(\dot H=z^2-b^2y^2\) exactly. It also checks the second derivative of the equality-obstruction function \(F\). The period step is analytic and uses the equality characterization in the sharp periodic Wirtinger inequality.

For Cases A--D in the source, the coefficient of \(y\) in the third equation is \(-1\), hence \(b=1\). The theorem therefore gives the concrete diagnostic \(T>2\pi\) for every nonconstant periodic orbit in each of those four numerical families, independently of amplitude and of the symmetry-breaking constant.

## Relationship to prior work
Hu, Sang, and Wang analyze pitchfork and Hopf bifurcations, numerical period-doubling cascades, and chaotic transitions for this same jerk family. Their Theorem 5.3 gives the local Hopf period asymptotic used above, but the inspected article does not state a global derivative-energy identity or a finite-amplitude lower bound for every periodic orbit.

A published finding for the same symmetric hyperbolic-sine jerk family proves a different compact-recurrence threshold at \(a=d\) from the coboundary \(\dot P=c y^2+(d-a)x^2+d x(\sinh x-x)\). That theorem neither contains nor implies the stationary identity \(\int z^2=b^2\int y^2\) or the period floor, and it is restricted to \(d>0\) and the symmetric forcing \(\varepsilon=0\), whereas the present period statement allows \(d\ne0\) and arbitrary \(\varepsilon\).

The closest structural analogue located is a published result for the Genesio jerk system. It derives a system-specific balance and a strict sharp period floor from a different polynomial nonlinearity. Its statement is confined to the Genesio equation and does not cover the hyperbolic-sine family. Innocenti, Tesi, and Genesio study Hopf bifurcation and harmonic-balance approximations in quadratic jerk systems; the inspected full text is local and does not provide the exact global bound above. Classical minimum-period theorems based on a global Lipschitz constant are also not an implication here because \(\sinh x\) is not globally Lipschitz and those bounds depend on the full vector-field Lipschitz constant rather than exactly on \(b\).

## Limitations
The invariant-measure statement is restricted to compact support, and the period theorem concerns classical nonconstant periodic solutions. It does not classify unbounded trajectories or chaotic invariant sets and does not prove that a periodic orbit exists at any parameter away from the source's established local branches.

Originality is assessed against the inspected source, the closest same-family published finding, the closest jerk-system period-floor analogue, targeted literature searches, and an inspected quadratic-jerk paper. A specialized older minimum-period theorem for this exact nonlinear jerk family could remain unindexed; no such statement was located. The sharpness claim uses only the nondegenerate Hopf branches actually covered by the source.

## References
1. X. Hu, B. Sang, and N. Wang, “The chaotic mechanisms in some jerk systems,” *AIMS Mathematics* 7(9) (2022), 15714–15740. DOI: 10.3934/math.2022861. An author-uploaded public preprint is recorded on 2021-10-06.
2. G. Innocenti, A. Tesi, and R. Genesio, “Complex behavior analysis in quadratic jerk systems via frequency domain Hopf bifurcation,” *International Journal of Bifurcation and Chaos* 20 (2010). DOI: 10.1142/S0218127410025946.
3. A. A. Zevin, “The Least Distance between Extrema and the Minimum Period of Solutions of Autonomous Vector Differential Equations,” *Doklady Mathematics* 99(2) (2019), 143–144.
