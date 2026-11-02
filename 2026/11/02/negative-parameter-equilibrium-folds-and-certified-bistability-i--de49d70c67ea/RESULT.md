# Negative-parameter equilibrium folds and certified bistability in the ETM-3D flow
## Finding
Consider the quadratic differential system
\[
\dot x=-2x-\rho y+yz,\qquad
\dot y=x-y+\rho z-2xz,\qquad
\dot z=\rho y-5z+xy.
\]
Its original positive-parameter bifurcation analysis leaves the real negative-parameter branch open. Define
\[
\begin{aligned}
Q(\rho)={}&594\rho^8-2076\rho^7-5948\rho^6+20050\rho^5\\
&+25505\rho^4-66100\rho^3-63325\rho^2+77500\rho+75000.
\end{aligned}
\]
The polynomial \(Q\) has **exactly two simple negative real roots**, denoted \(\alpha<\beta\), with rigorously isolated intervals
\[
-2.012<\alpha<-2.011,\qquad -1.309<\beta<-1.308.
\]
For each \(\rho<0\), the number of distinct **nonzero** equilibria is

| Parameter | Number of distinct nonzero equilibria |
| --- | ---: |
| \(\rho<\alpha\) | 4 |
| \(\rho=\alpha\) | 3 |
| \(\alpha<\rho<\beta\), \(\rho\ne\rho_0^-\) | 2 |
| \(\rho=\rho_0^-=(5-\sqrt{105})/4\) | 1 |
| \(\rho=\beta\) | 1 |
| \(\beta<\rho<0\) | 0 |

The origin exists for every parameter. The exceptional value \(\rho=-\sqrt5\) lies in \(\rho<\alpha\); one of its four nonzero equilibria is \((0,5,-\sqrt5)\). The two discriminant values \(\alpha\) and \(\beta\) are ordinary pair-coalescence parameters for the nonzero equilibrium equations. The intermediate exception \(\rho_0^-\) is a crossing of a nonzero equilibrium branch through the origin.

More strongly, at the exact parameter \(\rho=-2\) there are **two distinct hyperbolic attracting nonzero equilibria** and the origin is unstable. The attracting states persist (with open attraction basins) under sufficiently small parameter perturbations.

## Assumptions and scope
All coordinates and parameters are real. The bifurcation census concerns \(\rho<0\) and counts different equilibria once, even at a multiple root; the origin is excluded from the table. No positivity or physical-population constraint is imposed on the coordinates. Local exponential attraction means that every eigenvalue of the Jacobian has negative real part. No claims are made about global attraction, limit cycles, or chaotic dynamics in the negative-parameter family.

The first publicly available source for the system is arXiv:2610.04768v1 (2026-10-03). Its published bifurcation study is explicitly restricted to \(\rho\ge0\), although it supplies an equilibrium quartic valid algebraically in the negative range.

## Proof
**1. Exact reduction and exceptional fibers.** Write
\[
D(x,\rho)=2x^2+\rho x+5-\rho^2.
\]
The last two equilibrium equations are linear in \((y,z)\). Whenever \(D\ne0\), they give
\[
y=\frac{5x}{D},\qquad z=\frac{x(\rho+x)}{D}.
\]
Substitution into the first equation gives \(-xP(x,\rho)/D^2=0\), with
\[
\begin{aligned}
P(x,\rho)={}&8x^4+8\rho x^3+(-6\rho^2+10\rho+35)x^2\\
&+(-4\rho^3+5\rho^2+15\rho)x\\
&+2\rho^4-5\rho^3-20\rho^2+25\rho+50.
\end{aligned}
\]
No nonzero equilibrium has \(D=0\): the second equation gives \(y=x+(\rho-2x)z\), and the third then gives \(Dz=x(\rho+x)\). With \(D=0\) and \(x\ne0\), this forces \(x=-\rho\), but \(D(-\rho,\rho)=5\), a contradiction. If \(x=0\), the equilibria are the origin, and additionally \((0,5,\rho)\) when \(\rho^2=5\). Thus the negative exceptional value is \(\rho=-\sqrt5\).

The identity
\[
P(0,\rho)=(\rho^2-5)(2\rho^2-5\rho-10)
\]
shows the only negative parameters at which a quartic root is zero are \(-\sqrt5\) and \(\rho_0^-=(5-\sqrt{105})/4\). At the first, the zero quartic root is replaced by the exceptional nonzero equilibrium; at the second, it corresponds to the already counted origin and is removed from the nonzero census.

**2. Exact root topology.** Direct polynomial elimination gives
\[
\operatorname{disc}_x P(x,\rho)=12000Q(\rho).
\]
The rational Sturm chain for \(Q\) has \(6\) sign variations at \(-\infty\) and \(4\) at \(0\). Therefore \(Q\) has exactly two distinct negative real zeros. Furthermore \(\gcd(Q,Q')=1\), so they are simple. Exact rational evaluations give the sign patterns
\[
\begin{array}{c|cccc}
\rho &-503/250&-2011/1000&-1309/1000&-327/250\\\hline
\operatorname{sign}Q(\rho)&+&-&-&+
\end{array}
\]
which isolate \(\alpha\) and \(\beta\) in the stated disjoint intervals. The quartic has exactly \(4\), \(2\), and \(0\) distinct real roots at the rational sample parameters \(\rho=-3\), \(\rho=-3/2\), and \(\rho=-1\), respectively (verified by rational Sturm counting). Since the leading coefficient is the constant \(8\), its real-root count cannot change away from zeros of its discriminant. Each discriminant zero is simple and hence a unique ordinary double-root collision, with \(3\) and \(1\) distinct real roots at the respective boundaries. Applying the two exceptional-fiber corrections from Step 1 proves the entire table.

**3. Two exact attracting equilibria at \(\rho=-2\).** Here
\[
P(x,-2)=(x-2)(8x^3-9x+4).
\]
The cubic has discriminant \(-4320<0\), hence exactly one real root \(\xi\). Its signs at \(-5/4\) and \(-6/5\) are \(-3/8\) and \(122/125\), so
\[
-\frac54<\xi<-\frac65.
\]
The two nonzero equilibria are
\[
E_1=(2,2,0),\qquad
E_2=\left(\xi,\frac{5\xi}{2\xi^2-2\xi+1},\frac{\xi(\xi-2)}{2\xi^2-2\xi+1}\right).
\]
At \(E_1\), the Jacobian characteristic polynomial is
\[
\lambda^3+8\lambda^2+11\lambda+20,
\]
which is Hurwitz by the cubic Routh--Hurwitz inequalities. For \(E_2\), set \(t=-\xi\in(6/5,5/4)\), \(H=(2t^2+2t+1)^2\). The characteristic polynomial is
\[
\lambda^3+8\lambda^2+\frac{B(t)}{H}\lambda+\frac{C(t)}{H},
\]
where
\[
\begin{aligned}
B(t)={}&8t^6+24t^5+84t^4+138t^3+96t^2+52t+11,\\
C(t)={}&16t^6+48t^5+122t^4+134t^3+21t^2-28t-8.
\end{aligned}
\]
Clearly \(B(t)>0\). Also \(C(t)>0\) because \(134t^3-28t-8>0\) on this interval. Finally
\[
8B(t)-C(t)=48t^6+144t^5+550t^4+970t^3+747t^2+444t+96>0.
\]
The cubic Routh--Hurwitz criterion proves that \(E_2\) is a hyperbolic sink too. The origin has characteristic polynomial \(\lambda^3+8\lambda^2+11\lambda-8\), which has a positive real root, so it is unstable. Local attraction basins of the two sinks are disjoint and open. Hyperbolicity and the implicit-function theorem preserve both sinks for parameters in a neighborhood of \(-2\).

## Verification
The standalone file `check_negative_etm.py` recomputes the equilibrium reduction, the exact degree-eight discriminant, rational Sturm variations, isolating intervals, sample root counts, the special zero-root factors, and both cubic Hurwitz certificates. Run it with Python 3 and SymPy using `python check_negative_etm.py`. All checks use symbolic or rational arithmetic; decimal approximations are not required for the argument.

## Relationship to prior work
Khalili-Amirabadi and Jalaeian-Farimani (2026) introduce this exact flow, prove a global absorbing set for all real parameters, and analyze bifurcations only for \(\rho\ge0\). Their formulas include the equilibrium quartic and mention the isolated equilibrium at \(\rho=-\sqrt5\); they do not give a negative-parameter root-count phase diagram or exhibit the two negative-parameter sinks.

A publicly available 2026 mathematical note, *Exact global-stability threshold at the first ETM-3D saddle-node* (record `997f2098aca6`), computes the same degree-eight discriminant and its positive roots. Its theorem and proof explicitly assume \(\rho\ge0\), and it does not classify negative roots, exceptional branch counting, or stability at \(\rho=-2\). The discriminant polynomial itself is therefore inherited rather than claimed as an original algebraic object; the **negative-branch classification and certified bistability** are the contributions here.

## Limitations
The result is an equilibrium census plus local stability at one explicit parameter and nearby values. It does not give a complete stability-type classification across the negative branch, nor does it exclude other invariant sets, chaotic attractors, or periodic orbits. The negative-parameter range is an algebraic continuation of a benchmark model, not a validated physical scenario. Priority beyond the specifically inspected sources requires independent assessment.

## References
1. R. Khalili-Amirabadi and M. Jalaeian-Farimani, *ETM-3D: A One-Parameter Multistable Quadratic Flow with an Explicit Absorbing Set and Intermittent Chaos*, arXiv:2610.04768v1, submitted 2026-10-03, https://arxiv.org/abs/2610.04768.
2. *Exact global-stability threshold at the first ETM-3D saddle-node*, publicly indexed mathematical result, 2026-10-11, record `997f2098aca6`.
