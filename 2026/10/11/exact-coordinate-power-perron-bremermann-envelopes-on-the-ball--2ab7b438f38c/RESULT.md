# Exact coordinate-power Perron–Bremermann envelopes on the ball

## Finding

Let
\[
\mathbb B^n
=
\{z\in\mathbb C^n:\|z\|<1\},
\qquad
n\ge2,
\]
let \(v\in\mathbb C^n\) be a unit vector, and fix
\[
0<q\le1.
\]
Consider the finite continuous superharmonic obstacle
\[
\varphi_{q,v}(z)
=
-|\langle z,v\rangle|^{2q}.
\]

Its plurisubharmonic obstacle envelope has the exact closed form
\[
G_{\varphi_{q,v},\mathbb B^n}(z)
=
-\left(
1-\|P_{v^\perp}z\|^2
\right)^q.
\]

The same function is the Perron–Bremermann solution for the boundary datum
\[
\xi\longmapsto
-|\langle \xi,v\rangle|^{2q}.
\]

The solution is continuous and maximal,
\[
(dd^cG_{\varphi_{q,v},\mathbb B^n})^n=0,
\]
and its complete interior minimum set is the complex diameter
\[
\{\lambda v:|\lambda|<1\}.
\]
In particular, the boundary minimum circle
\[
\{e^{i\theta}v:\theta\in\mathbb R\}
\]
fills in to its holomorphic disk in the maximal solution.

The exponent range is sharp for this explicit orthogonal-shadow formula. For
\[
q>1,
\]
the same expression fails to be plurisubharmonic.

## Assumptions and scope

The obstacle envelope is
\[
G_{\varphi,\Omega}(z)
=
\sup
\{
w(z):
w\in\operatorname{PSH}(\Omega),
\ w\le\varphi\text{ on }\Omega
\}.
\]

The unit ball is a regular domain for the classical Perron–Bremermann problem with continuous boundary data. The recent source proves in a much more general obstacle setting that the envelope is maximal and gives boundary convergence at points admitting continuous plurisubharmonic barriers.

The result here is an explicit computation for a finite obstacle. It does not claim a formula for arbitrary functions of
\[
|\langle z,v\rangle|,
\]
nor does it determine the envelope of the same power obstacle when
\[
q>1.
\]
For \(q>1\), only failure of the displayed closed-form candidate is asserted.

## Proof

By unitary invariance it is enough to take
\[
v=e_n.
\]
Write
\[
z=(z',z_n),
\qquad
s=\|z'\|^2,
\qquad
t=|z_n|^2.
\]
Inside the unit ball,
\[
s+t<1.
\]

Define
\[
u_q(z)
=
-(1-s)^q.
\]
Let
\[
g_q(s)=-(1-s)^q.
\]
For
\[
0<q\le1,
\]
\[
g_q'(s)
=
q(1-s)^{q-1}>0
\]
and
\[
g_q''(s)
=
q(1-q)(1-s)^{q-2}\ge0.
\]
The Levi matrix in the \(z'\)-variables is
\[
g_q'(s)I
+
g_q''(s)\,\overline{z'}(z')^{\mathsf T},
\]
so it is positive semidefinite. The function is independent of \(z_n\), hence
\[
u_q\in\operatorname{PSH}(\mathbb B^n).
\]

Its Levi form has a zero complex direction everywhere. Thus its rank is at most
\[
n-1,
\]
and
\[
(dd^cu_q)^n=0.
\]
Since \(u_q\) is locally bounded, it is maximal in the standard pluripotential sense.

On the unit sphere,
\[
t=1-s,
\]
so
\[
u_q(\xi)
=
-(1-s)^q
=
-t^q
=
-|\xi_n|^{2q}
=
\varphi_{q,e_n}(\xi).
\]
Thus \(u_q\) is a maximal plurisubharmonic function with exactly the prescribed continuous boundary trace.

It is also an admissible obstacle minorant. Indeed, in the open ball,
\[
t<1-s,
\]
so
\[
t^q<(1-s)^q
\]
and therefore
\[
u_q(z)
<
-t^q
=
\varphi_{q,e_n}(z).
\]

Now let \(w\in\operatorname{PSH}(\mathbb B^n)\) satisfy
\[
w\le\varphi_{q,e_n}.
\]
At each boundary point,
\[
\limsup_{\mathbb B^n\ni z\to\xi}w(z)
\le
\varphi_{q,e_n}(\xi)
=
u_q(\xi).
\]
Maximal comparison with \(u_q\) gives
\[
w\le u_q
\]
throughout the ball. Taking the supremum over all admissible \(w\) gives
\[
G_{\varphi_{q,e_n},\mathbb B^n}
\le u_q.
\]
The reverse inequality follows because \(u_q\) itself is admissible. Hence
\[
G_{\varphi_{q,e_n},\mathbb B^n}
=
u_q.
\]

Since
\[
-1\le u_q<0,
\]
the minimum is \(-1\), and
\[
u_q(z)=-1
\quad\Longleftrightarrow\quad
s=0.
\]
Thus the interior minimum set is precisely
\[
\{(0,\ldots,0,\lambda):|\lambda|<1\}.
\]
Undoing the unitary change of coordinates gives
\[
\{\lambda v:|\lambda|<1\}.
\]

Finally, suppose
\[
q>1.
\]
For the same radial expression, the radial Levi eigenvalue in the \(z'\)-space is
\[
g_q'(s)+s g_q''(s)
=
q(1-s)^{q-2}(1-qs).
\]
It is negative whenever
\[
s>\frac1q.
\]
Because such points occur in the unit ball, this candidate is not plurisubharmonic. Therefore
\[
q=1
\]
is the sharp upper threshold for this explicit orthogonal-shadow solution mechanism.

## Verification

The recent primary source was inspected at its definition of the obstacle envelope, its maximality theorem, its strict obstacle separation statement, its boundary convergence theorem, its comparison lemma, its hull theorem, and the examples involving the unit ball and complex disks.

The proof above does not infer the formula from numerical evidence. It directly checks plurisubharmonicity through the complete Levi matrix, maximality through the missing complex direction, exact boundary agreement on the sphere, strict domination by the obstacle in the interior, the comparison argument giving equality with the envelope, and the exact minimum locus.

For \(q>1\), the negative radial Levi eigenvalue gives a direct obstruction to extending the same formula.

## Relationship to prior work

The 2026 paper of Dao and Nguyen develops a general theory for finite and unbounded superharmonic obstacles, including interior continuity, maximality, hull representations, stability, and uniqueness. Its explicit constructions focus mainly on logarithmic singularities and geometric deformation tests. The exact coordinate-power family above is not stated there.

Classical Perron–Bremermann theory establishes existence and uniqueness of maximal plurisubharmonic solutions for continuous data on regular domains, but does not by itself provide this closed formula.

Darvas and Rubinstein give a general Legendre-transform framework for certain Bremermann-type envelopes arising in homogeneous complex Monge–Ampère problems. Their formulation is structurally broader in another direction, but the located theorem does not state or imply by an identified specialization the coordinate-power formula on the Euclidean ball.

Targeted literature searches for coordinate-power boundary data, orthogonal-projection formulas, and exact ball envelopes found no published statement matching
\[
-\left(1-\|P_{v^\perp}z\|^2\right)^q.
\]

## Limitations

The formula is proved only for
\[
0<q\le1.
\]
When
\[
q>1,
\]
the displayed candidate is not plurisubharmonic, but the actual Perron–Bremermann envelope is not computed here.

The result concerns one complex coordinate, equivalently one complex line and its orthogonal complement. No multi-coordinate anisotropic analogue is asserted.

The explicit solution is degenerate in one complex direction, so it is maximal rather than strictly plurisubharmonic.

## References

1. H. H. Dao and Q. D. Nguyen, *Complex Dirichlet problem with unbounded boundary values*, arXiv:2610.00914v1, 2026.
2. T. Darvas and Y. A. Rubinstein, *Kiselman's principle, the Dirichlet problem for the Monge–Ampère equation, and rooftop obstacle problems*, arXiv:1405.6548v1; Journal of the Mathematical Society of Japan 68 (2016), 773–796.
3. M. Nilsson, *Continuity of envelopes of unbounded plurisubharmonic functions*, arXiv:2109.13625; Mathematische Zeitschrift 301 (2022), 3959–3971.
4. F. Wikström, *The Dirichlet problem for maximal plurisubharmonic functions on analytic varieties in \(\mathbb C^n\)*, International Journal of Mathematics 20 (2009), 521–528.
