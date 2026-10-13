# A polar-intersection counterexample to variable-order KKT multipliers
## Finding

The necessary multiplier statement in Theorem 4.1(a) of *Linear scalarization techniques for deriving optimality criteria of quasi-proper solutions in vector optimization with variable polyhedral orders* is false under its stated hypotheses.

Fix
\[
\rho=\frac{1}{10},\qquad q=(1,1),
\]
and define
\[
f(t)=(t,-t),\qquad h(u,v)=(u-v)^2.
\]
Take \(M=\mathbb R\) and the single convex constraint \(g(t)=-1\), so the feasible set is all of \(\mathbb R\) and Slater holds strictly.

For \(y=(y_1,y_2)\), define
\[
A_y=
\begin{cases}
A^+:=\begin{pmatrix}2&1\\1&0\end{pmatrix},&y_1>0,\\[4pt]
A^0:=I_2,&y_1=0,\\[4pt]
A^-:=\begin{pmatrix}1&2\\0&1\end{pmatrix},&y_1<0.
\end{cases}
\]
Let
\[
D(y)=\{z\in\mathbb R^2:A_yz\ge0\},
\]
and, with \(U\) the all-ones \(2\times2\) matrix,
\[
D_\rho(y)=\{z:(A_y+\rho U A_y)z\ge0\},\qquad
C_\rho(y)=q+D_\rho(y).
\]

Then \(\bar t=0\) is a Ch-quasi-proper non-dominated point and all hypotheses of Theorem 4.1(a) are satisfied. Nevertheless, for every \(t>0\),
\[
a^{f(t)}_1\circ f(s)=s,\qquad a^{f(t)}_2\circ f(s)=s.
\]
At \(s=0\) all remaining terms in the asserted stationarity inclusion vanish, so the theorem would require
\[
0=\lambda_1+\lambda_2
\]
with
\[
\lambda_1>0,\qquad\lambda_2>0,
\]
which is impossible.

The structural reason is that the proof moves from a scalarizer in the positive polar of a common intersection to a row decomposition in every pointwise cone polar. Those are different requirements. In this example,
\[
\xi=\left(\frac12,\frac12\right)
\]
satisfies
\[
\xi\in(\operatorname{cl}\widehat C_\rho)^+,\qquad
\langle\xi,q\rangle=1,
\]
but
\[
\xi\notin D_\rho(f(t))^+
\]
for every \(t\ne0\).

## Assumptions and scope

Each matrix \(A^+\), \(A^-\), and \(A^0\) is full rank and has no zero row, so every \(D(y)\) is a closed, convex, pointed, solid polyhedral cone. Moreover
\[
A^+q=(3,1),\qquad A^-q=(3,1),\qquad A^0q=(1,1),
\]
so \(q\) is interior to every original cone.

The objective \(f\) is affine, hence the source cone-convexity condition holds with equality for every pointwise order. The constraint \(g=-1\) is convex and strictly feasible. The function \(h(u,v)=(u-v)^2\) is nonnegative, positive off the diagonal, diagonal-null, and convex in its first argument.

The counterexample concerns only the necessary non-dominated multiplier statement in Theorem 4.1(a). No claim is made here about the fixed-point minimal theorem.

## Proof

For the theorem parameter \(\rho=1/10\), the two sign-dependent dilated matrices are
\[
A_{\rho,+}
=
\begin{pmatrix}
23/10&11/10\\
13/10&1/10
\end{pmatrix},
\qquad
A_{\rho,-}
=
\begin{pmatrix}
11/10&23/10\\
1/10&13/10
\end{pmatrix}.
\]
Both are invertible.

Let
\[
w=(1,1),\qquad c=q+w=(2,2).
\]
Then
\[
A_{\rho,+}w=(17/5,7/5),\qquad
A_{\rho,-}w=(17/5,7/5),
\]
while the zero-sign matrix gives
\[
A_{\rho,0}w=(6/5,6/5).
\]
Hence
\[
c\in\bigcap_{t\in\mathbb R}\operatorname{int}C_\rho(f(t)),
\]
so the required common interior is nonempty.

To verify Ch-quasi-proper non-domination, use the further source dilation
\[
\tau=\frac15
\]
and set \(K(y)=D_\tau(y)\). For any nonzero \(z\in D(y)\), the vector \(A_yz\) is nonzero and nonnegative, so
\[
(A_y+\tau U A_y)z
\]
is strictly positive componentwise. Thus
\[
D(y)\setminus\{0\}\subset\operatorname{int}K(y).
\]
Since \(0<\rho<\tau\), the same calculation gives
\[
D_\rho(y)\setminus\{0\}\subset\operatorname{int}K(y),
\]
and consequently
\[
C_\rho(y)\subset\operatorname{int}K(y).
\]
The matrices defining \(K(y)\) are invertible, so the cones are pointed; therefore \(K\) belongs to the dilating-cone family required in the Ch-quasi-proper definition.

For \(t>0\),
\[
f(0)-f(t)=t(-1,1).
\]
The auxiliary positive-sign matrix is
\[
A_{\tau,+}
=
\begin{pmatrix}
13/5&6/5\\
8/5&1/5
\end{pmatrix},
\]
and
\[
A_{\tau,+}(-1,1)=(-7/5,-7/5).
\]
Thus this difference direction is outside \(K(f(t))\).

For \(t<0\), writing \(a=-t>0\),
\[
f(0)-f(t)=a(1,-1),
\]
and
\[
A_{\tau,-}
=
\begin{pmatrix}
6/5&13/5\\
1/5&8/5
\end{pmatrix},
\qquad
A_{\tau,-}(1,-1)=(-7/5,-7/5).
\]
Again the difference direction is outside \(K(f(t))\).

Because
\[
C_\rho(f(t))+\operatorname{int}K(f(t))
\subset\operatorname{int}K(f(t))
\]
and \(h(t,0)=t^2>0\) for \(t\ne0\), neither difference can lie in the forbidden Ch-quasi-proper domination set. Thus \(f(0)\) is Ch-quasi-proper non-dominated.

Now take any \(t>0\). The original rows are
\[
a^{f(t)}_1=(2,1),\qquad a^{f(t)}_2=(1,0).
\]
Since \(f(s)=(s,-s)\),
\[
a^{f(t)}_1\circ f(s)=s,\qquad
a^{f(t)}_2\circ f(s)=s.
\]
Therefore
\[
\partial(a^{f(t)}_1\circ f)(0)=\{1\},
\qquad
\partial(a^{f(t)}_2\circ f)(0)=\{1\}.
\]
Also
\[
\partial h(\cdot,0)(0)=\{0\},\qquad
N(\mathbb R,0)=\{0\},
\]
and complementary slackness for \(g=-1\) forces the constraint multiplier to be zero. The necessary inclusion in Theorem 4.1(a) therefore reduces to
\[
0\in\{\lambda_1+\lambda_2\},
\]
contradicting strict positivity of both multipliers.

The exact proof gap is visible from
\[
\xi=\left(\frac12,\frac12\right).
\]
If \(z\) lies in both closed sign-dependent dilated cones, their second-row inequalities imply
\[
13z_1+z_2\ge0,\qquad z_1+13z_2\ge0,
\]
so
\[
z_1+z_2\ge0.
\]
Every element \(c'\in\operatorname{cl}\widehat C_\rho\) has the form \(q+z\) with such a \(z\), hence
\[
\langle\xi,c'\rangle\ge1.
\]
Thus
\[
\xi\in(\operatorname{cl}\widehat C_\rho)^+,
\qquad
\langle\xi,q\rangle=1.
\]

On the other hand, expressing \(\xi\) as a row combination of \(A_{\rho,+}\) requires
\[
(\mu_1,\mu_2)=\left(\frac12,-\frac12\right),
\]
and the same coefficients occur for \(A_{\rho,-}\). Hence \(\xi\) is not in either pointwise positive polar. The proof's row-representation step therefore cannot be inferred from common-intersection polar membership.

## Verification

The standalone script `artifacts/verify_variable_order_kkt.py` uses exact rational arithmetic to check all displayed matrices, determinants, the common interior witness, the two excluded difference directions, the normalized scalarizer, the failed pointwise polar representations, and the row-scalarization derivatives.

The script is supporting evidence only. The counterexample is proved symbolically above.

## Relationship to prior work

The 2026 source extends a fixed-polyhedral-cone multiplier construction to point-dependent polyhedral orders. Its proof of Theorem 4.1(a) obtains a scalarizer in the positive polar of the closed common intersection and then invokes the row representation of each pointwise \(D_\rho(f(t))^+\). The example above shows that this implication fails.

The closest fixed-cone predecessor of Huerga--Jiménez--Novo does not make this transition. Its scalarization theorem first places the scalarizer in one fixed \(D_\rho^+\), and its multiplier theorem then applies the row representation to that same fixed cone. Hence the fixed-cone theorem does not imply the variable-order claim.

Related work on variable ordering structures studies continuity of oriented-distance scalarizations, and related work on variable coradiant sets uses nonlinear scalarization and duality. Targeted searches by title, DOI, theorem number, common multipliers, pointwise polars, polar intersections, and counterexample terminology did not locate a published correction or an equivalent counterexample.

## Limitations

The ordering map in the witness is piecewise constant in the sign of the first objective coordinate. The source theorem imposes no continuity assumption on the ordering map, so this lies within its stated scope. A strengthened theorem with additional compatibility or continuity assumptions may survive.

The result does not identify the weakest repair. Any repair of the displayed proof must justify the pointwise polar memberships needed for the row decompositions or replace the common-multiplier statement by a formulation compatible with genuinely variable cones.

## References

1. M. Samareh Bagheri, A. Hoseini Dehmiry, *Linear scalarization techniques for deriving optimality criteria of quasi-proper solutions in vector optimization with variable polyhedral orders*, Optimization Methods and Software, published online 3 September 2026. DOI: 10.1080/10556788.2026.2722979.
2. L. Huerga, B. Jiménez, V. Novo, *Optimality Conditions for Quasi Proper Solutions in Multiobjective Optimization with a Polyhedral Cone*, in *Functional Analysis and Continuous Optimization*, Springer Proceedings in Mathematics & Statistics 424, 2023, pp. 195--211. DOI: 10.1007/978-3-031-30014-1_9.
3. L. Huerga, B. Jiménez, V. Novo, A. Vílchez, *Continuity of a scalarization in vector optimization with variable ordering structures and application to convergence of minimal solutions*, Optimization 72(4), 957--978, 2023. DOI: 10.1080/02331934.2022.2081569.
4. M. You, G. Li, *Approximate properly solutions of constrained vector optimization with variable coradiant sets*, Optimization Letters 17(3), 721--738, 2023. DOI: 10.1007/s11590-022-01902-9.
