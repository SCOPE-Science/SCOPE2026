# Exact Hopf-threshold recurrence law for the tuned-collector chaotic oscillator
## Finding
For the normalized admittance-model tuned-collector flow with \(y_{12}=y_{22}=0\), \(L_1=L_2=C=1\), \(0<M<1\), \(Y:=y_{11}>0\), \(\alpha<0\), and \(\beta>0\), namely \(\dot x=-y+\alpha(z/Y)^3+\beta z/Y\), \(\dot y=(x-Mz/Y)/(1-M^2)\), \(\dot z=(Mx-z/Y)/(1-M^2)\), the linear Hopf threshold \(\beta=MY\) is also an exact global recurrence threshold. If \(0<\beta\le MY\), the origin is globally asymptotically stable. If \(\beta>MY\), every compactly supported invariant probability measure \(\mu\neq\delta_0\) satisfies \(\int z^4\,d\mu/\int z^2\,d\mu=Y^2(\beta-MY)/(-\alpha)=:K\), and in fact \(\int z^2\,d\mu<K<\max_{\operatorname{supp}\mu} z^2\); the same identity and strict bounds hold for the uniform measure on every nonconstant periodic orbit. For the published chaotic parameter set \(M=49/100\), \(Y=33/10\), \(\alpha=-10\), \(\beta=15\), one has \(K=14574087/1000000\), so every nontrivial compact recurrent statistical state has RMS \(i_2\)-current strictly below \(3.8176022579\) while its support reaches strictly beyond that magnitude.

## Assumptions and scope
Consider the normalized case-Y equations obtained from the published admittance model after setting \(L_1=L_2=C=1\) and the published near-ideal-current-source choice \(y_{12}=y_{22}=0\). Write \(x=v_C\), \(y=i_1\), \(z=i_2\), and \(Y=y_{11}\). The theorem assumes \(0<M<1\), \(Y>0\), \(\alpha<0\), and \(\beta>0\). It concerns classical trajectories and compactly supported invariant Borel probability measures of this polynomial flow. The source's parameter set (13) lies in this domain.

## Proof
Set \(d=1-M^2>0\), \(q=y-Mz\), and
\[
G(z)=\frac{\alpha z^4}{4Y^3}+\frac{\beta z^2}{2Y}.
\]
The last two differential equations give \(\dot q=x\), while \(M x=d\dot z+z/Y\). Define
\[
H=\frac{x^2+q^2}{2}+\frac{d z^2}{2}-\frac{d}{M}G(z).
\]
Since \(\dot x+q=G'(z)-Mz\), direct differentiation gives
\[
\dot H=x(G'(z)-Mz)+dz\dot z-\frac dM G'(z)\dot z
=\frac{\beta-MY}{MY^2}z^2+\frac{\alpha}{MY^4}z^4. \tag{1}
\]

If \(0<\beta\le MY\), then
\[
H=\frac{x^2+q^2}{2}+\frac d2\left(1-\frac{\beta}{MY}\right)z^2-\frac{d\alpha}{4MY^3}z^4
\]
is positive definite and radially unbounded, while (1) is nonpositive and vanishes only when \(z=0\). The largest invariant subset of \(z=0\) is the origin: invariance first forces \(\dot z=Mx/d=0\), hence \(x=0\), and then \(\dot x=-y=0\). LaSalle's invariance principle therefore makes the origin globally asymptotically stable, including the nonhyperbolic boundary \(\beta=MY\).

For comparison with the local boundary, the characteristic polynomial at the origin is
\[
p(\lambda)=\lambda^3+\frac{1}{Yd}\lambda^2+\frac{Y-M\beta}{Yd}\lambda+\frac{1}{Yd}.
\]
At \(\beta=MY\), this factors as
\[
p(\lambda)=(\lambda^2+1)\left(\lambda+\frac1{Yd}\right),
\]
so the same parameter is exactly the linear Hopf threshold.

Now let \(\mu\) be a compactly supported invariant probability measure. Invariance of the smooth observable \(H\) gives \(\int \dot H\,d\mu=0\), hence
\[
Y^2(\beta-MY)\int z^2\,d\mu+\alpha\int z^4\,d\mu=0. \tag{2}
\]
When \(\beta>MY\) and \(\mu\ne\delta_0\), one has \(\int z^2\,d\mu>0\): otherwise invariance would force \(z=x=y=0\) almost surely. Dividing (2) by this positive second moment proves the exact ratio
\[
\frac{\int z^4\,d\mu}{\int z^2\,d\mu}=K:=\frac{Y^2(\beta-MY)}{-\alpha}.
\]
Cauchy--Schwarz gives \(\int z^4\,d\mu\ge(\int z^2\,d\mu)^2\), so \(\int z^2\,d\mu\le K\). Equality would force \(z^2=K\) almost surely. The invariant support would then contain a trajectory with nonzero constant \(|z|\); along such a trajectory \(\dot z=0\) gives \(x=z/(MY)\), while persistence of constant \(x\) gives \(y=G'(z)\) and then \(\dot y=0\), contradicting \(\dot y=(x-Mz/Y)/d=z/(MY)\ne0\). Thus \(\int z^2\,d\mu<K\).

If \(R=\max_{\operatorname{supp}\mu}|z|\), then \(z^4\le R^2z^2\) on the support, so (2) gives \(K\le R^2\). Equality would again force \(z^2=K\) wherever \(z\ne0\) on a set of positive \(\mu\)-measure and leads to the same invariance contradiction. Hence \(K<R^2\). The invariant probability measure uniformly distributed on any nonconstant periodic orbit is nontrivial and compactly supported, so all conclusions apply to every such orbit.

For the published set \(M=49/100\), \(Y=33/10\), \(\alpha=-10\), \(\beta=15\), exact arithmetic yields
\[
K=\frac{(33/10)^2(15-(49/100)(33/10))}{10}=\frac{14574087}{1000000},
\]
with \(\sqrt K\approx3.81760225796245\).

## Verification
The bundled `verify.py` uses only the Python standard library. It checks the exact source-parameter value of \(K\), the factorization of the characteristic polynomial at \(\beta=MY\), and the differential identity (1) at several independent rational states using exact fractions. The exact general cancellation proving (1) is displayed above and does not rely on numerical sampling. Running the bundled script produces `VERIFY_OK`, recorded in `verification_output.txt`.

## Relationship to prior work
Petrzela's introducing article supplies the admittance equations, states that the origin is the unique equilibrium, derives the characteristic polynomial and divergence, and reports robust chaos for parameter set (13), where \(y_{12}=y_{22}=0\). It does not state the Lyapunov function \(H\), global stability through the Hopf boundary, or the invariant fourth-to-second current-moment law. Targeted searches for the exact title/DOI together with “moment”, “invariant measure”, “global stability”, and the symbolic threshold found no same-system statement of these conclusions. The closest located balance-law and global-threshold results concern different vector fields and do not imply this source-specific identity.

## Limitations
The theorem uses the normalized case-Y subfamily with \(y_{12}=y_{22}=0\); it does not cover the source's impedance-model cases or nonzero backward/output admittances. For \(\beta>MY\), the result constrains any compact recurrent state that exists but does not prove existence, uniqueness, ergodicity, chaos, basin size, or the exact maximum current of the reported attractor. The strict support excursion is a necessary condition, not an amplitude prediction. No independent audit has been performed.

## References
1. J. Petrzela, “Chaotic States of Transistor-Based Tuned-Collector Oscillator,” *Mathematics* 11 (2023), 2213. DOI: 10.3390/math11092213. First published 2023-05-08.
2. The article's public full text identifies MSC 37M05 and gives the normalized accumulation-element choice and parameter set (13) used above.
