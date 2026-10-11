# Finite-amplitude mean–variance shell for an oscillatory SI epidemic model
## Finding
Consider the normalized epidemic system
\[
\dot X=X\left[k(1+\varepsilon X)(Y-X)-(n+1)\right],
\qquad
\dot Y=m-nY-X,
\]
with \(m,n,k,\varepsilon>0\). Let \(\mu\) be a compactly supported invariant Borel probability measure with support contained in the strict epidemiological region
\[
0<X<Y<\frac{m}{n}.
\]
Write
\[
\bar X=\int X\,d\mu,
\qquad
\bar Y=\int Y\,d\mu,
\qquad
V_X=\operatorname{Var}_\mu(X),
\qquad
V_Y=\operatorname{Var}_\mu(Y).
\]
Then
\[
n\bar Y+\bar X=m,
\qquad
\operatorname{Cov}_\mu(X,Y)=-nV_Y,
\]
and the exact finite-amplitude mean–variance law is
\[
\frac{m-(n+1)\bar X}{n}(1+\varepsilon\bar X)
=
\frac{n+1}{k}+\varepsilon(V_X+nV_Y).
\]

Suppose the endemic-equilibrium equation
\[
\frac{m-(n+1)x}{n}(1+\varepsilon x)=\frac{n+1}{k}
\]
has two roots
\[
0<x_-<x_+<\frac{m}{n+1}.
\]
These are precisely the infective coordinates of the two endemic equilibria. The preceding identity factors to
\[
V_X+nV_Y=\frac{n+1}{n}(x_+-\bar X)(\bar X-x_-).
\]
Therefore every non-Dirac compact invariant measure in the strict epidemiological region satisfies
\[
x_-<\bar X<x_+.
\]
In particular, every positive nonconstant periodic orbit has mean infective density strictly between the two endemic-equilibrium infective coordinates.

At the parameter values used for Figure 5(c) of the source,
\[
m=2,
\qquad n=\frac13,
\qquad \varepsilon=\frac54,
\qquad k=0.205=\frac{41}{200},
\]
the source reports a stable limit cycle. The two endemic infective coordinates are exactly
\[
x_-=\frac7{20}-\frac{\sqrt{131241}}{2460}
\approx0.202734960462713,
\]
\[
x_+=\frac7{20}+\frac{\sqrt{131241}}{2460}
\approx0.497265039537287.
\]
Hence every such stable cycle at those parameters obeys
\[
0.202734960462713\ldots<\bar X<0.497265039537287\ldots.
\]

## Assumptions and scope
The measure is required to have compact support inside \(0<X<Y<m/n\). This ensures that \(\log X\) is smooth on a neighborhood of the support and that its generator has zero invariant mean. No assumption of ergodicity is needed for the identities. The strict mean trap requires a non-Dirac measure and the existence of two endemic roots in \((0,m/(n+1))\).

The result applies to finite-amplitude recurrent dynamics, including positive periodic orbits. It does not assert existence or uniqueness of a cycle, determine its period, or replace the source's local bifurcation analysis.

## Proof
Invariance applied to \(Y\) gives
\[
0=\int (m-nY-X)\,d\mu,
\]
so
\[
n\bar Y+\bar X=m.
\]
Applying invariance to \(Y^2/2\) gives
\[
0=\int Y(m-nY-X)\,d\mu.
\]
Substituting \(m=n\bar Y+\bar X\) yields
\[
\int XY\,d\mu=\bar X\bar Y-nV_Y,
\]
which is equivalent to
\[
\operatorname{Cov}_\mu(X,Y)=-nV_Y.
\]

Because \(X>0\) on the compact support, invariance applied to \(\log X\) gives
\[
0=\int\left[k(1+\varepsilon X)(Y-X)-(n+1)\right]d\mu.
\]
Thus
\[
\frac{n+1}{k}
=\int (1+\varepsilon X)(Y-X)\,d\mu.
\]
Expanding the right-hand side and using the covariance identity,
\[
\int X(Y-X)\,d\mu
=\bar X(\bar Y-\bar X)-V_X-nV_Y.
\]
Therefore
\[
\frac{n+1}{k}
=(1+\varepsilon\bar X)(\bar Y-\bar X)-\varepsilon(V_X+nV_Y).
\]
Using \(\bar Y=(m-\bar X)/n\) gives
\[
\frac{m-(n+1)\bar X}{n}(1+\varepsilon\bar X)
=
\frac{n+1}{k}+\varepsilon(V_X+nV_Y).
\]

Let
\[
H(x)=\frac{m-(n+1)x}{n}(1+\varepsilon x)-\frac{n+1}{k}.
\]
Its leading coefficient is \(-\varepsilon(n+1)/n\). If its roots are \(x_-<x_+\), then
\[
H(x)=\frac{\varepsilon(n+1)}{n}(x_+-x)(x-x_-).
\]
Evaluating at \(x=\bar X\) and using the mean–variance identity gives
\[
V_X+nV_Y=\frac{n+1}{n}(x_+-\bar X)(\bar X-x_-).
\]
For a non-Dirac invariant measure, \(V_X+nV_Y>0\): if both variances vanished, both coordinates would be constant on the support and the measure would be an equilibrium atom. Hence both factors on the right are positive and \(x_-<\bar X<x_+\).

## Verification
The accompanying `verify.py` symbolically checks the algebraic reduction and the exact Figure 5(c) root formula. Running it produces `VERIFY_OK`. No numerical trajectory is used in the proof.

For an independent numerical stress test, integration near the reported Figure 5(c) attracting cycle gives an infective time mean near \(0.44\), well inside the exact interval above, and the two sides of the mean–variance identity agree to numerical integration error. This numerical check is supplementary only.

## Relationship to prior work
Zeng and Yu study this exact normalized SI system, give the invariant epidemiological region, classify endemic equilibria and Hopf bifurcations, and report stable and unstable limit cycles. Their Figure 5(c) uses \(m=2\), \(n=1/3\), \(\varepsilon=5/4\), and \(k=0.205\), with a stable limit cycle. The inspected full text does not state an invariant-measure mean–variance identity, a variance-gap factorization, or the finite-amplitude conclusion that the mean infective density lies strictly between the two endemic infective coordinates.

The earlier paper of Li, Zhou, Wu, and Ma introduces the same nonlinear-incidence epidemic model and reports backward, Hopf, and Bogdanov–Takens bifurcations with stable or unstable limit cycles. Its publicly accessible abstract does not state the present mean–variance law. A later paper by Li, Li, and Ma analyzes higher-codimension Bogdanov–Takens behavior for the same model; its accessible abstract likewise concerns local/global bifurcation structure rather than stationary finite-amplitude averages.

## Limitations
The theorem does not establish that a nontrivial compact invariant measure exists for a given parameter set. The strict trap is conditional on two endemic roots in the epidemiological interval. The claim is about invariant statistics, not pointwise bounds: a cycle may cross outside the interval \([x_-,x_+]\) even though its mean lies inside it. The 2007 introducing article was not available in full text during this check, so an unindexed equivalent statement there remains a residual originality risk; its abstract and the complete 2022/2023 source text were compared at statement level.

## References
B. Zeng and P. Yu, “A hierarchical parametric analysis on Hopf bifurcation of an epidemic model,” *Discrete and Continuous Dynamical Systems - S* 16 (2023), 708–724, DOI 10.3934/dcdss.2022069. Early access 21 March 2022.

J. Li, Y. Zhou, J. Wu, and Z. Ma, “Complex dynamics of a simple epidemic model with a nonlinear incidence,” *Discrete and Continuous Dynamical Systems - B* 8 (2007), 161–173, DOI 10.3934/dcdsb.2007.8.161.

C. Li, J. Li, and Z. Ma, “Codimension 3 B-T bifurcations in an epidemic model with a nonlinear incidence,” *Discrete and Continuous Dynamical Systems - B* 20 (2015), 1107–1116, DOI 10.3934/dcdsb.2015.20.1107.
