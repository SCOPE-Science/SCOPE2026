# Forcing-selected RMS rigidity across multistability and offset boosting in a no-equilibrium hyperchaotic flow
## Finding
Consider the four-dimensional system introduced by Vaidyanathan, Moroz, and Sambas,
\[
\dot x=a(y-x),\qquad
\dot y=2x(1-z)+cy+w,\qquad
\dot z=xy-b,\qquad
\dot w=-d(x+y).
\]
Assume \(a\ne0\) and define
\[
Q(x,z)=z-\frac{x^2}{2a}.
\]
Then every classical solution obeys the exact pointwise identity
\[
\dot Q=x^2-b.
\]
The source's offset-boosted family replaces \(z\) by \(z+k\) only in the \(\dot y\) equation, so this identity is unchanged for every real offset \(k\).

Consequently, every bounded forward solution satisfies the exact finite-time formula
\[
\frac1T\int_0^T x(t)^2\,dt
=b+\frac{Q(T)-Q(0)}T,
\]
and therefore
\[
\lim_{T\to\infty}\frac1T\int_0^T x(t)^2\,dt=b.
\]
In particular, \(b<0\) permits no bounded forward solution.

For every compactly supported invariant Borel probability measure \(\mu\),
\[
\int x^2\,d\mu=b.
\]
If \(d\ne0\), invariance also gives
\[
\int x\,d\mu=\int y\,d\mu=0,
\qquad
\int xy\,d\mu=b,
\]
and the exact activity-defect law
\[
\int y^2\,d\mu
=b+\frac1{a^2}\int \dot x^{\,2}\,d\mu.
\]
When \(b>0\), the last inequality is strict:
\[
\int y^2\,d\mu>b.
\]

At the parameter values used by the source for its hyperchaotic and multistable examples,
\[
(a,b,c,d)=(31,25,15,3.3),
\]
every bounded trajectory has exact long-time RMS
\[
\operatorname{RMS}(x)=5.
\]
Every compact recurrent statistical state also has zero \(x\)- and \(y\)-means and satisfies
\[
\operatorname{RMS}(y)>5,
\qquad
\int y^2\,d\mu=25+\frac1{961}\int \dot x^{\,2}\,d\mu.
\]
Thus the three coexisting bounded branches displayed by the source, and every bounded member of its offset-boosted family, are constrained by the same forcing-selected \(x\)-RMS even though their phase-space locations or geometries differ.

## Assumptions and scope
The pointwise coboundary identity requires only \(a\ne0\). The long-time formula assumes the forward solution is bounded, so that \(Q(T)\) is bounded. The invariant-measure statements assume a compactly supported invariant Borel probability measure; the zero-mean and activity-defect statements additionally require \(d\ne0\). The strict inequality for \(y\) requires \(b>0\). No assertion is made that every initial condition at \(b>0\) is bounded, or that the reported numerical attractors have otherwise been independently reproduced.

The result applies unchanged to the source's offset parameter \(k\), because the transformation changes only the \(\dot y\) equation and leaves both \(\dot x\) and \(\dot z\) unchanged.

## Proof
Differentiate \(Q=z-x^2/(2a)\). Using \(\dot z=xy-b\) and \(\dot x=a(y-x)\),
\[
\begin{aligned}
\dot Q
&=xy-b-\frac xa\,a(y-x)\\
&=xy-b-x(y-x)\\
&=x^2-b.
\end{aligned}
\]
Integrating from \(0\) to \(T\) gives
\[
Q(T)-Q(0)=\int_0^T(x(t)^2-b)\,dt,
\]
which is exactly the displayed finite-time identity. If the trajectory is bounded, then \(Q(T)\) is bounded, so division by \(T\) and passage to the limit gives the long-time mean-square law. Since the left-hand side is a limit of averages of the nonnegative function \(x^2\), a bounded forward solution cannot exist when \(b<0\).

Let \(\mu\) be a compactly supported invariant probability measure. For every smooth observable used below, invariance gives zero integral of its Lie derivative. Applying this to \(Q\) yields
\[
0=\int LQ\,d\mu=\int(x^2-b)\,d\mu,
\]
so \(\int x^2\,d\mu=b\).

Assume \(d\ne0\). Applying invariance to \(x\) and \(w\) gives
\[
0=a\left(\int y\,d\mu-\int x\,d\mu\right),
\]
\[
0=-d\left(\int x\,d\mu+\int y\,d\mu\right),
\]
so both means vanish. Applying invariance to \(z\) yields
\[
\int xy\,d\mu=b.
\]
Finally, because \(\dot x=a(y-x)\),
\[
\frac1{a^2}\int \dot x^{\,2}\,d\mu
=\int(y-x)^2\,d\mu
=\int y^2\,d\mu-b,
\]
which proves the activity-defect law.

If \(b>0\) and equality \(\int y^2\,d\mu=b\) held, then \(\dot x=0\) on the support of \(\mu\), hence \(y=x\) there. The support of an invariant measure is invariant. Along any orbit in that compact support, \(x\) would therefore be constant and
\[
\dot w=-2dx.
\]
Compactness forces \(x=0\) on the support, contradicting \(\int x^2\,d\mu=b>0\). Hence the inequality is strict.

## Verification
The accompanying `verify.py` implements exact polynomial arithmetic over rational coefficients and verifies
\[
xy-b-x(y-x)=x^2-b
\]
without floating-point evaluation. It also checks the moment reduction
\[
(y-x)^2=y^2-2xy+x^2
\]
and the published specialization \(a=31\), \(b=25\), which gives \(\sqrt b=5\) and \(a^2=961\).

Run `python verify.py`; a successful replay prints `VERIFY_OK`.

The bounded-orbit limit and invariant-measure statements are analytic consequences of the exact coboundary and invariance. The script is not used to infer an infinite-time statement from a finite numerical experiment.

## Relationship to prior work
Vaidyanathan, Moroz, and Sambas introduce the exact vector field, prove that it has no equilibrium when their parameters are nonzero, compute bifurcation and Lyapunov diagrams, display three coexisting hyperchaotic attractors at \((31,25,15,3.3)\), and introduce the offset transformation \(z\mapsto z+k\). The inspected primary text does not state the coboundary \(\dot Q=x^2-b\), the bounded-orbit mean-square law, the sign obstruction at \(b<0\), or the invariant-measure activity-defect law.

Published-result searches for the exact title, DOI, equations, aliases, RMS/time-average language, and the polynomial balance found no result covering this source and claim. The closest retrieved balance law is for a different sine-modified Sprott-B flow, where a different observable also fixes a mean square; that result does not imply the present identity. A second close result concerns a different Dong–Wang four-dimensional flow with \(\dot z=-b+xy\), but its \(\dot x\) equation contains additional terms and its stationary law is different.

The result therefore supplies a source-specific constraint complementary to the paper's numerical multistability and offset-boosting analysis: the geometry may change, but the exact long-time \(x\)-RMS cannot.

## Limitations
The novelty search cannot exclude an unindexed or inaccessible source that independently noticed the same coboundary. The result does not prove existence of a bounded attractor for \(b>0\), does not classify all unbounded solutions, and does not independently validate the source's reported Lyapunov exponents. The strict \(y\)-RMS inequality is a statement about compactly supported invariant probability measures, not an arbitrary finite transient.

## References
1. S. Vaidyanathan, I. M. Moroz, and A. Sambas, “A new 4-D hyperchaotic system with no equilibrium, its multistability, offset boosting and circuit simulation,” *Archives of Control Sciences* 30(3), 575–597 (2020), DOI 10.24425/acs.2020.134678.
2. Oxford University Research Archive record, ark:/29072/ora_1df9d972377f45f6923a1a13f0912aeb, version-of-record metadata and publication date 2020-09-30.
3. MaRDI record Q5150038zb, classification 34C28 for the source article.
