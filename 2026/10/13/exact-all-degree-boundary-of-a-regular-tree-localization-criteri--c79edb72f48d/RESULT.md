# Exact all-degree boundary of a regular-tree localization criterion
## Finding
For an integer \(d\ge 2\), consider the two-parameter set
\[
G_d=\left\{(\gamma,\delta)\in(1,\infty)\times(0,\infty):\exists\varepsilon>0,\ \delta+\gamma\varepsilon^d\le\varepsilon,\ 2d\gamma\varepsilon^{d-1}+2d\delta\varepsilon^d<1\right\}.
\]
This is the model-independent sufficient region introduced by Henning and Külske for localization and reused for large-period gradient Gibbs measures. Define, for \(0<x<1/(2d)\),
\[
\Gamma_d(x)=x\left(\frac{2d(1-x)}{1-2dx}\right)^{\frac{d-1}{d+1}},
\qquad
\Delta_d(x)=\left(\frac{(1-x)^d(1-2dx)}{2d}\right)^{\frac1{d+1}}.
\]
Then \(\Gamma_d\) is a strictly increasing bijection from \((0,1/(2d))\) onto \((0,\infty)\). For every \(\gamma>1\), let \(x_\gamma\) be the unique point satisfying \(\Gamma_d(x_\gamma)=\gamma\), and set \(D_d(\gamma)=\Delta_d(x_\gamma)\). The good set is exactly
\[
G_d=\{(\gamma,\delta):\gamma>1,\ 0<\delta<D_d(\gamma)\}.
\]
Moreover \(D_d\) is strictly decreasing, and
\[
D_d(\gamma)\sim \frac{2d-1}{(2d)^{d/(d-1)}}\,\gamma^{-1/(d-1)}
\qquad(\gamma\to\infty).
\]
For \(d=2\), eliminating the parameter recovers the published quartic boundary and its leading asymptotic coefficient \(3/16\).

## Assumptions and scope
The statement concerns the exact geometry of the sufficient contraction region \(G_d\), not the true thermodynamic phase boundary of any particular spin model. The integer \(d\ge2\) is the tree order used in the source convention, so each vertex has \(d+1\) neighbours. The variables satisfy \(\gamma>1\) and \(\delta>0\). No assumption on a specific interaction is needed until a model maps its transfer-operator norms to \((\gamma,\delta)\).

## Proof
For fixed \(\gamma>1\) and \(\varepsilon>0\), the first defining inequality is equivalent to
\[
\delta\le A(\varepsilon):=\varepsilon-\gamma\varepsilon^d,
\]
while the second is equivalent to
\[
\delta<B(\varepsilon):=\frac{1-2d\gamma\varepsilon^{d-1}}{2d\varepsilon^d}.
\]
A positive feasible \(\delta\) forces
\[
0<\varepsilon<\varepsilon_0:=(2d\gamma)^{-1/(d-1)}.
\]
On this whole interval,
\[
A'(\varepsilon)=1-d\gamma\varepsilon^{d-1}>\frac12,
\]
so \(A\) is strictly increasing. Also
\[
B'(\varepsilon)=\varepsilon^{-d-1}\left(\gamma\varepsilon^{d-1}-\frac12\right)<0,
\]
because \(\gamma\varepsilon^{d-1}<1/(2d)\le1/4\). Hence \(B\) is strictly decreasing. As \(\varepsilon\downarrow0\), one has \(A(\varepsilon)\downarrow0\) and \(B(\varepsilon)\to\infty\); as \(\varepsilon\uparrow\varepsilon_0\), one has \(B(\varepsilon)\downarrow0\) while \(A(\varepsilon)>0\). There is therefore a unique crossing \(\varepsilon_*\), and
\[
\sup_{0<\varepsilon<\varepsilon_0}\min\{A(\varepsilon),B(\varepsilon)\}=A(\varepsilon_*)=B(\varepsilon_*).
\]
The strictness of the second defining inequality means that equality is excluded, giving the strict hypograph.

Put \(x=\gamma\varepsilon_*^{d-1}\). Then \(0<x<1/(2d)\), and the crossing equation becomes
\[
2d\varepsilon_*^{d+1}(1-x)=1-2dx.
\]
Combining this with \(\varepsilon_*^{d-1}=x/\gamma\) gives exactly
\[
\gamma=\Gamma_d(x),\qquad A(\varepsilon_*)=B(\varepsilon_*)=\Delta_d(x).
\]
It remains to show that the parameter is single-valued. Direct differentiation gives
\[
\frac{\Gamma_d'(x)}{\Gamma_d(x)}=
\frac{2d(d+1)x^2-6dx+d+1}{x(d+1)(x-1)(2dx-1)}.
\]
The denominator is positive on \((0,1/(2d))\). The numerator is decreasing there because its derivative is at most \(2-4d<0\), and at the right endpoint it equals
\[
d-\frac32+\frac1{2d}>0.
\]
Thus \(\Gamma_d'(x)>0\). Its endpoint limits are \(0\) and \(+\infty\), proving bijectivity. Meanwhile
\[
\frac{d}{dx}\log\Delta_d(x)=
-\frac{d}{(d+1)(1-x)}-\frac{2d}{(d+1)(1-2dx)}<0,
\]
so \(D_d\) decreases strictly with \(\gamma\).

For the large-\(\gamma\) limit, write \(y=1-2dx\). Then \(x\to1/(2d)\), and the formulas imply
\[
y\sim(2d-1)(2d\gamma)^{-(d+1)/(d-1)}.
\]
Substitution into \(\Delta_d\) yields
\[
D_d(\gamma)\sim \frac{2d-1}{(2d)^{d/(d-1)}}\gamma^{-1/(d-1)}.
\]
For \(d=2\), eliminating \(x\) gives
\[
16\gamma^2\delta^4+24\gamma^3\delta^2+(16\gamma^5-4\gamma^2)\delta-3\gamma^4=0,
\]
which is the quartic printed in the source.

## Verification
The accompanying `verify.py` independently evaluates the parameterization for \(2\le d\le40\) and several \(\gamma\)-values, reconstructs the unique crossing \(A=B\), checks a strict interior witness, verifies positivity of the analytic derivative numerator, reproduces the published \(d=2\) quartic numerically, and checks the large-\(\gamma\) coefficient in representative degrees. Its finite computations corroborate the algebra but are not used to infer the all-degree result.

## Relationship to prior work
Henning and Külske define \(G_d\) by the two inequalities above and use it as a common sufficient region for localized Gibbs measures and for large-period delocalized gradient Gibbs measures. Their applications section gives an explicit boundary only for \(d=2\), where they obtain a quartic, and for \(d=3\) their figure describes the upper boundary as numerically computed. They also prove a separate large-degree existence theorem. The present result instead gives a closed parametric boundary for every fixed integer \(d\ge2\), together with monotonicity and the fixed-degree large-\(\gamma\) asymptotic. A later paper on irreducible localization sets uses a different strong-coupling criterion and does not provide this two-parameter boundary.

## Limitations
This result exactly characterizes the source's sufficient contraction criterion; it does not prove that the criterion is necessary for Gibbs-state localization or delocalization, and it does not identify an exact physical critical temperature for a concrete model. The originality comparison cannot rule out an equivalent elementary elimination in weakly indexed notes or unpublished material. The numerical verifier is supplementary only.

## References
1. F. Henning and C. Külske, *Coexistence of localized Gibbs measures and delocalized gradient Gibbs measures on trees*, arXiv:2002.09363; Ann. Appl. Probab. 31 (2021), DOI:10.1214/20-AAP1647.
2. A. Abbondandolo, F. Henning, C. Külske, and P. Majer, *Infinite-Volume States with Irreducible Localization Sets for Gradient Models on Trees*, arXiv:2302.05398; J. Stat. Phys. 191 (2024), DOI:10.1007/s10955-024-03278-9.
