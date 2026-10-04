# Exact equilibrium skeleton of the symmetry-broken hyperbolic-sine jerk cases

## Finding

Consider
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=0.01-a x-y-0.2z+d\sinh x.
\]
For the two asymmetric cases studied in the source, the equilibrium count and linear stability can be classified exactly across the full plotted parameter intervals.

For Case C, \(d=1\) and \(a\in[1.1,1.656]\), there are exactly three equilibria for every parameter value in the interval. The two outer equilibria have one unstable eigenvalue. The middle equilibrium is asymptotically stable for
\[
1.1\le a<a_C,\qquad a_C=1.201239986249802\ldots,
\]
has spectrum \(\{-0.2,\pm i\}\) at \(a=a_C\), and has unstable dimension two for \(a>a_C\).

For Case D, \(d=-1\) and \(a\in[-1.42,-0.83]\), the saddle-node threshold is
\[
a_{\mathrm{SN}}=-1.048351831276690\ldots.
\]
There are three equilibria for \(a<a_{\mathrm{SN}}\), two distinct equilibria at \(a=a_{\mathrm{SN}}\) with one double equilibrium, and one equilibrium for \(a>a_{\mathrm{SN}}\). The middle equilibrium, whenever it exists, has one unstable eigenvalue. The left and right outer equilibria cross the imaginary axis at
\[
a_L=-1.116233346441185\ldots,\qquad
a_R=-1.076996927969895\ldots,
\]
respectively, each with spectrum \(\{-0.2,\pm i\}\). Thus both outer equilibria are simultaneously asymptotically stable precisely for
\[
a_R<a<a_{\mathrm{SN}}.
\]

## Assumptions and scope

The claim concerns only the printed asymmetric systems with constant forcing \(0.01\), damping coefficient \(0.2\), unit coefficient of \(y\), and \(d=1\) or \(d=-1\). It classifies equilibria and their linear stability over the parameter windows plotted by the source. It does not assert the nonlinear criticality of the imaginary-pair crossings, nor does it classify periodic or chaotic attractors or their basins.

## Proof

At an equilibrium, \(y=z=0\), so \(x\) solves
\[
a x-d\sinh x=0.01.
\]
The Jacobian at \((x,0,0)\) has characteristic polynomial
\[
p(\lambda)=\lambda^3+0.2\lambda^2+\lambda+k,\qquad k=a-d\cosh x.
\]
The cubic Routh--Hurwitz criterion gives asymptotic stability exactly when
\[
0<k<0.2.
\]
If \(k<0\), the Routh array has one sign change, hence exactly one eigenvalue in the open right half-plane. If \(k>0.2\), it has two sign changes. At \(k=0.2\),
\[
p(\lambda)=(\lambda+0.2)(\lambda^2+1).
\]
At \(k=0\), zero is an eigenvalue and the other quadratic factor has negative-real-part roots.

For Case C, put
\[
F_a(x)=a x-\sinh x.
\]
When \(a>1\), its critical points are \(\pm u\), where \(u=\operatorname{arcosh}a\), and
\[
F_a(u)=a\,\operatorname{arcosh}a-\sqrt{a^2-1}=:M(a).
\]
The function \(M\) is strictly increasing for \(a>1\). The fold equation \(M(a)=0.01\) has the unique solution
\[
a=1.048351831276690\ldots<1.1.
\]
Therefore three simple equilibria exist throughout the source's Case-C interval. On the two outer branches, \(k=F_a'(x)<0\). On the middle branch, \(k>0\), and the stability boundary \(k=0.2\) is equivalent to
\[
0.2x+x\cosh x-\sinh x=0.01.
\]
For \(x>0\), the left-hand side before subtracting \(0.01\) has derivative \(0.2+x\sinh x>0\), so there is a unique positive root \(x_C\). It gives
\[
a_C=0.2+\cosh x_C=1.201239986249802\ldots.
\]

For Case D, write \(q=-a\). When \(a<-1\), the equilibrium equation is
\[
-qx+\sinh x=0.01.
\]
Its two critical points are \(\pm\operatorname{arcosh}q\), and the local maximum equals
\[
M(q)=q\,\operatorname{arcosh}q-\sqrt{q^2-1}.
\]
Thus the unique fold condition \(M(q)=0.01\) gives
\[
a_{\mathrm{SN}}=-1.048351831276690\ldots.
\]
For three-root parameters, the middle branch has \(k<0\) and the two outer branches have \(k>0\). On an outer branch, the stability boundary \(k=0.2\) is obtained by eliminating \(a\):
\[
0.2x-x\cosh x+\sinh x=0.01.
\]
The two roots relevant to the outer branches in the three-equilibrium interval are
\[
x_L=-0.775684353712710\ldots,\qquad
x_R=0.728116791582367\ldots,
\]
which yield
\[
a_L=0.2-\cosh x_L=-1.116233346441185\ldots,
\]
\[
a_R=0.2-\cosh x_R=-1.076996927969895\ldots.
\]
The remaining positive root of the same eliminated equation corresponds to a later imaginary-pair crossing at \(a=-0.8012608389\ldots\), outside the source's plotted Case-D interval. The Routh classification then gives the stated stability partition.

## Verification

The bundled `verify.py` independently bisects the fold and imaginary-pair equations, checks the displayed numerical intervals, verifies their ordering relative to the source parameter windows, and checks representative Routh-sign regimes. Running it with the Python standard library prints `VERIFY_OK`.

## Relationship to prior work

Hu, Sang and Wang introduce the five-parameter hyperbolic-sine jerk family and explicitly define the asymmetric Cases C and D by adding the constant \(0.01\). Their Sections 3.2 and 4.2 study the corresponding forward and backward period-doubling diagrams numerically. The source gives a detailed local bifurcation analysis only for the symmetric family. The exact asymmetric equilibrium count, the Case-D saddle-node threshold, the three imaginary-pair stability thresholds above, and the stable-equilibrium bistability window are not stated there.

A prior result on the symmetric \(0.01=0\) member establishes a different compact-recurrence threshold and does not imply this imperfect-symmetry equilibrium unfolding. Focused searches also returned general recurrence and Hopf-balance results for other third-order systems; those do not determine the roots of the forced hyperbolic-sine equilibrium equation or their Routh indices.

## Limitations

This is a complete equilibrium and linear-stability classification only for the two printed asymmetric one-parameter cases and their plotted intervals. The proof does not establish first Lyapunov coefficients at the imaginary-pair crossings, global basin boundaries, existence or uniqueness of periodic or chaotic attractors, or the fate of all invariant sets at the saddle-node. Numerical decimal values are certified by monotone scalar root bracketing, while the qualitative count and stability statements are analytic.

## References

1. X. Hu, B. Sang, N. Wang, “The chaotic mechanisms in some jerk systems,” AIMS Mathematics 7 (2022), 15714–15740, DOI 10.3934/math.2022861. The author-uploaded preprint became public on 6 October 2021.
2. AIMS Press article record for DOI 10.3934/math.2022861, including MSC 34C05, 34C07, 34C23, 34C28, 34C29 and the final published version.
