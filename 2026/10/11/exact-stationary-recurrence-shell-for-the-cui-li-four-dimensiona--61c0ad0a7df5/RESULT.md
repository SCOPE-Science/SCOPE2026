# Exact stationary recurrence shell for the Cui–Li four-dimensional flow
## Finding
Consider the autonomous system
\[
\dot u=a(v-u)+evw,\qquad
\dot v=cu+dv-uw+mp,\qquad
\dot w=-bw+uv,\qquad
\dot p=-k(u+v),
\]
with \(a,b,e,m>0\) and \(c,d,k\in\mathbb R\). Every compactly supported invariant probability measure \(\mu\) satisfies
\[
\int\!\left(w+\frac{a}{2e}\right)^2\,d\mu
=\left(\frac{a}{2e}\right)^2+\frac{a}{be}\int u^2\,d\mu.
\]
The equality
\[
\int\!\left(w+\frac{a}{2e}\right)^2\,d\mu
=\left(\frac{a}{2e}\right)^2
\]
holds if and only if \(\mu=\delta_{(0,0,0,0)}\). Hence every other compactly supported invariant probability measure assigns positive mass to
\[
\{w<-a/e\}\cup\{w>0\}.
\]
Equivalently, no non-equilibrium compact recurrent statistical state can be supported entirely in the slab \(-a/e\le w\le0\).

For the published parameter vector
\[
(a,b,c,d,e,m,k)=(15,43,1,16,5,5,2),
\]
the identity becomes
\[
\int (w+3/2)^2\,d\mu
=9/4+\frac{3}{43}\int u^2\,d\mu.
\]
Thus every nontrivial compact stationary state at the showcased parameters places positive mass at \(w<-3\) or \(w>0\).

## Assumptions and scope
A compactly supported invariant probability measure means a Borel probability measure invariant under the flow and supported on a compact invariant set on which the classical flow is defined. Compact support ensures that the polynomial observables used below and their Lie derivatives are integrable, so stationarity gives \(\int Lf\,d\mu=0\).

The sign assumptions \(a,b,e,m>0\) are exactly what is needed for the strict equality classification. The coefficients \(c,d,k\) do not enter the shell identity. The source's positive-parameter regime, including its displayed baseline, is therefore covered.

The result is a necessary constraint on compact recurrent dynamics. It does not prove existence, uniqueness, or hyperchaoticity of any non-equilibrium invariant set, and it does not infer an invariant probability measure from a finite numerical trajectory.

## Proof
Set
\[
Q(u,v,w,p)=\frac12\left(u^2-ew^2\right).
\]
A direct Lie-derivative calculation gives
\[
LQ=u\dot u-ew\dot w
=-au^2+auv+bew^2.
\]
Stationarity of \(Q\) and of \(w\) gives
\[
0=\int LQ\,d\mu=-a\int u^2\,d\mu+a\int uv\,d\mu+be\int w^2\,d\mu,
\]
and
\[
0=\int \dot w\,d\mu=-b\int w\,d\mu+\int uv\,d\mu.
\]
Eliminating \(\int uv\,d\mu\) yields
\[
a\int u^2\,d\mu=ab\int w\,d\mu+be\int w^2\,d\mu.
\]
After division by \(be>0\) and completion of the square, this is exactly
\[
\int\!\left(w+\frac{a}{2e}\right)^2\,d\mu
=\left(\frac{a}{2e}\right)^2+\frac{a}{be}\int u^2\,d\mu.
\]

It remains to identify the equality case. Equality with the radius term forces \(\int u^2\,d\mu=0\), hence \(u=0\) \(\mu\)-almost everywhere. Stationarity of \(w^2\) then gives
\[
0=\int L(w^2)\,d\mu=-2b\int w^2\,d\mu,
\]
so \(w=0\) \(\mu\)-almost everywhere. Next,
\[
L(uv)=\dot u\,v+u\dot v
\]
reduces \(\mu\)-almost everywhere to \(av^2\), and stationarity gives \(v=0\) \(\mu\)-almost everywhere. Finally,
\[
L(vp)=\dot v\,p+v\dot p
\]
reduces to \(mp^2\), so \(p=0\) \(\mu\)-almost everywhere. Because \(m>0\), the only equality measure is \(\delta_{(0,0,0,0)}\). The converse is immediate.

For every non-origin invariant measure the shell expectation is therefore strictly larger than \(\left(a/(2e)\right)^2\). On the closed slab \(-a/e\le w\le0\), however,
\[
\left(w+\frac{a}{2e}\right)^2\le\left(\frac{a}{2e}\right)^2.
\]
Hence a non-origin invariant measure cannot give full mass to that slab; it must assign positive mass to \(w<-a/e\) or \(w>0\).

## Verification
The bundled `verify.py` uses only the Python standard library and a small exact multivariate-polynomial implementation. It reconstructs the vector field, differentiates \(Q\), verifies the polynomial identity
\[
LQ=-au^2+auv+bew^2,
\]
checks the algebraic elimination underlying the stationary shell, and confirms the exact baseline coefficients \(3/2\), \(9/4\), and \(3/43\). Running

`python3 verify.py`

prints `VERIFY_OK`. The checker certifies the algebraic identities; the invariant-measure and equality arguments are the analytic steps given above and do not rely on finite numerical experiments.

## Relationship to prior work
Cui and Li introduce exactly this four-dimensional controller extension of the Qi system and analyze dissipativity, invariance, equilibria, bifurcations, and numerical chaotic and hyperchaotic regimes. Their article does not state the invariant-measure shell or the resulting recurrence exclusion for the slab \(-a/e\le w\le0\).

Qi and Zhang's earlier energy analysis of the three-dimensional Qi system develops Casimir-energy balance laws and pointwise attractor bounds. That work is the closest methodological antecedent found: it shows that quadratic energy identities are natural for the Qi family. The inspected full text does not state the signed quadratic observable \(Q=(u^2-ew^2)/2\), the four-dimensional stationary shell above, or the strict equality classification for compact invariant measures of the Cui–Li extension.

A published same-system correction was also compared at statement level. It gives corrected nonzero equilibria and their local characteristic polynomial; it does not state or imply the global invariant-measure shell. Conversely, the shell does not determine that local spectrum. Exact-source, formula, slab, stationary-measure, and Qi-energy searches found no stronger result covering the present statement.

## Limitations
The theorem is conditional on compactly supported invariant probability measures and therefore does not establish boundedness of arbitrary trajectories. It does not validate or invalidate the source's numerical Lyapunov exponents or the existence of its displayed attractors. The slab conclusion is a necessary support condition, not a pointwise trapping theorem.

The literature search cannot exclude an unindexed note, thesis, or differently phrased prior derivation. In particular, the Qi-system energy literature makes the quadratic-balance technique non-novel in itself; the originality claim concerns the specific signed coboundary, exact stationary shell, equality classification, and four-dimensional recurrence consequence for this vector field.

## References
1. Ning Cui and Junhong Li, “A new 4D hyperchaotic system and its control,” *AIMS Mathematics* 8(1), 905–923. DOI 10.3934/math.2023044. Published 13 October 2022.
2. Guoyuan Qi and Jiangfeng Zhang, “Energy cycle and bound of Qi chaotic system,” *Chaos, Solitons & Fractals* 99 (2017), 7–15. DOI 10.1016/j.chaos.2017.03.044.
