# Exact two-variable classification for the Terrell-type quartic minimization problem
## Finding
Let \(\lambda,\gamma_1,\gamma_2>0\), and define
\[
f(x,y)=(\lambda+x^2+y^2)^2-(\gamma_1x+\gamma_2xy)^2,\qquad (x,y)\in\mathbb R^2.
\]
Then \((0,0)\) is the unique global minimizer of \(f\) exactly in the following two regimes:
\[
0<\gamma_2\le 1\quad\text{and}\quad \gamma_1^2\le 2\lambda,
\]
or
\[
1<\gamma_2<2\quad\text{and}\quad \gamma_1^2<2\lambda\gamma_2(2-\gamma_2).
\]
The distinction between strict and non-strict inequalities is sharp. If \(1<\gamma_2<2\) and
\[
\gamma_1^2=2\lambda\gamma_2(2-\gamma_2),
\]
then the origin is a global minimizer but is not unique. If \(\gamma_2\le1\) and \(\gamma_1^2=2\lambda\), the origin is still the unique global minimizer. If \(\gamma_2\ge2\), or if the relevant inequality above is violated, the origin is not a global minimizer.

This gives a necessary-and-sufficient answer for the first genuinely two-variable case of the arbitrary-parameter minimization question posed in Remark 3.3 of Papadatos.
## Assumptions and scope
All three parameters are strictly positive and the variables range over all of \(\mathbb R^2\). The conclusion concerns uniqueness of the global minimizer, not convexity of \(f\). The result solves the case called \(n=3\) in the source notation; no assertion is made here for the higher-dimensional chain \(n\ge4\).
## Proof
Put \(t=x^2\ge0\). Subtracting the value at the origin gives
\[
f(x,y)-\lambda^2=t^2+A(y)t+B(y),
\]
where
\[
A(y)=2(\lambda+y^2)-(\gamma_1+\gamma_2y)^2,
\qquad
B(y)=y^2(2\lambda+y^2).
\]
For fixed \(y\), minimization over \(t\ge0\) is elementary. If \(A(y)\ge0\), the minimum occurs at \(t=0\) and equals \(B(y)\). If \(A(y)<0\), it occurs at \(t=-A(y)/2\) and equals
\[
B(y)-\frac{A(y)^2}{4}.
\]
Hence \(f(x,y)\ge\lambda^2\) for every \((x,y)\) if and only if
\[
A(y)\ge-2|y|\sqrt{2\lambda+y^2}
\]
for every real \(y\). Equivalently,
\[
|\gamma_1+\gamma_2y|\le \sqrt{2\lambda+y^2}+|y|.
\]
For \(u\ge0\),
\[
|\gamma_1-\gamma_2u|\le \gamma_1+\gamma_2u,
\]
so the negative half-line imposes no condition beyond the positive half-line. Therefore it is necessary and sufficient that
\[
\gamma_1+\gamma_2y\le \sqrt{2\lambda+y^2}+y\qquad(y\ge0).
\]
Normalize by
\[
a=\frac{\gamma_1}{\sqrt{2\lambda}},\qquad b=\frac{\gamma_2}{\sqrt2},\qquad z=\frac{y}{\sqrt\lambda}.
\]
The condition becomes the supporting-line inequality
\[
a+bz\le h(z):=\frac{z+\sqrt{z^2+2}}{\sqrt2}\qquad(z\ge0).
\]
The function \(h\) is strictly convex, and
\[
h'(z)=\frac{1+z/\sqrt{z^2+2}}{\sqrt2}
\]
increases from \(1/\sqrt2\) to \(\sqrt2\).

If \(b\le1/\sqrt2\), equivalently \(\gamma_2\le1\), the minimum of \(h(z)-bz\) on \([0,\infty)\) is \(h(0)=1\). Thus global minimality at the origin is equivalent to \(a\le1\), or \(\gamma_1^2\le2\lambda\). Strict convexity shows that even when \(a=1\), equality in the supporting-line inequality occurs only at \(z=0\). At \(y=0\),
\[
f(x,0)-\lambda^2=x^2\bigl(x^2+2\lambda-\gamma_1^2\bigr),
\]
so the only equality point is still \(x=0\). Hence the origin is unique throughout this closed parameter region.

If \(1/\sqrt2<b<\sqrt2\), equivalently \(1<\gamma_2<2\), the strictly convex function \(h(z)-bz\) has one interior minimum. Writing \(q=\gamma_2-1\in(0,1)\), the minimizing point satisfies
\[
\frac{z}{\sqrt{z^2+2}}=q,
\]
and direct substitution gives
\[
\inf_{z\ge0}(h(z)-bz)=\sqrt{1-q^2}=\sqrt{\gamma_2(2-\gamma_2)}.
\]
Thus global minimality at the origin is equivalent to
\[
\gamma_1^2\le2\lambda\gamma_2(2-\gamma_2).
\]
At equality, the supporting line is tangent at a positive point, producing nonzero co-minimizers. Explicitly, the tangency level is
\[
y_*=rac{\sqrt{2\lambda}(\gamma_2-1)}{\sqrt{\gamma_2(2-\gamma_2)}},
\]
and the two associated values satisfy
\[
x_*^2=\frac{2\lambda(\gamma_2-1)}{\gamma_2(2-\gamma_2)}.
\]
Thus uniqueness requires the strict inequality stated in the finding.

Finally, if \(b\ge\sqrt2\), equivalently \(\gamma_2\ge2\), then
\[
\inf_{z\ge0}(h(z)-bz)\le0,
\]
whereas \(a>0\). The supporting-line condition therefore fails. This completes the classification.
## Verification
The algebraic reduction to a quadratic in \(t=x^2\), the parameter thresholds, the source examples, and representative boundary points were independently replayed with exact rational arithmetic in the accompanying checker. The checker is supplemental: the infinite classification follows from the analytic minimization and strict-convexity argument above, not from finite sampling.

For the source value obtained from its displayed formula when \(N=4\), namely \(\lambda=11/16\), the classification reproduces all four examples in Remark 3.3: \((\gamma_1,\gamma_2)=(4/3,2/3)\), \((1,2)\), and \((1,8/5)\) fail origin-minimality, whereas \((1,1)\) has the origin as unique global minimizer.
## Relationship to prior work
Papadatos derives this quartic family from the discrete Terrell problem and explicitly asks for necessary and sufficient conditions on arbitrary positive parameters that make the origin the unique global minimizer. The source gives examples already showing several qualitatively different behaviors, but does not classify the parameter region. The result above supplies the complete classification for its first two-variable case.

The closest directly related discrete-order-statistic optimization literature located in the search was López-Blázquez and Salamanca-Miño's work on automatic differentiation for maximal correlation from finite discrete parents. That work treats a different optimization problem and reports that closed forms are generally unavailable beyond the smallest supports; it does not imply the quartic supporting-line classification above.
## Limitations
The result is restricted to the two-variable quartic corresponding to \(n=3\). It does not classify the arbitrary positive-parameter chain for \(n\ge4\), and it does not claim a new maximal-correlation formula. The literature search found no covering statement under the equivalent quartic formulation, but a differently phrased or poorly indexed algebraic treatment remains a residual originality risk.
## References
1. N. Papadatos, *A discrete analogue of Terrell's characterization of rectangular distributions*, arXiv:2205.14360v1, 28 May 2022; journal version, *Mathematical Methods of Statistics* 32 (2023), 122--132, DOI:10.3103/S1066530723020035.
2. F. López-Blázquez and B. Salamanca-Miño, *Automatic differentiation and maximal correlation of order statistics from discrete parents*, *Computational Statistics* 36 (2021), 2889--2915, DOI:10.1007/s00180-021-01103-5.
