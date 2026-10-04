# Exact equilibrium and stationary-moment geometry of a quadratic self-excited chaotic flow

## Finding

Consider the positive-parameter quadratic flow introduced by Xu, Shekofteh, Akgül, Li, and Panahi,
\[
\dot x=gz,\qquad
\dot y=d x^2+e y^2-f,\qquad
\dot z=-a x-bx^2+c y^2,
\]
with \(a,b,c,d,e,f,g>0\). Put
\[
A=be+cd,\qquad
\Delta=\sqrt{a^2e^2+4Acf},\qquad
x_\pm=\frac{-ae\pm\Delta}{2A}.
\]
Then the complete equilibrium geometry is explicit. The positive root \(x_+\) always produces the two equilibria
\[
E_{+}^{\pm}=\left(x_+,\ \pm\sqrt{\frac{f-dx_+^2}{e}},\ 0\right).
\]
The negative root \(x_-\) is admissible exactly when
\[
b\sqrt{\frac fd}\ge a.
\]
Consequently the system has exactly two, three, or four equilibria according as \(b\sqrt{f/d}<a\), \(b\sqrt{f/d}=a\), or \(b\sqrt{f/d}>a\). Every one of these equilibria is linearly unstable.

The same flow has an exact stationary-moment geometry. For every compactly supported invariant probability measure \(\mu\), define
\[
q=\int x^2\,d\mu.
\]
Then
\[
\int z\,d\mu=0,
\qquad
dq+e\int y^2\,d\mu=f,
\qquad
\int x\,d\mu=\frac{cf-Aq}{ae},
\]
and therefore
\[
\operatorname{Var}_\mu(x)
=q-\left(\frac{cf-Aq}{ae}\right)^2
=\frac{A^2}{a^2e^2}(q-x_+^2)(x_-^2-q).
\]
In particular,
\[
x_+^2\le q\le \min\left\{x_-^2,\frac fd\right\}.
\]
Equality \(q=x_+^2\) occurs exactly for invariant measures supported on the two equilibria \(E_+^+\) and \(E_+^-\). Thus every compact stationary state not supported on those two fixed points has the strict root-mean-square amplitude gap \(\sqrt{\int x^2\,d\mu}>x_+\).

For the parameter set used in the introducing article,
\[
(a,b,c,d,e,f,g)=(4,1,1,1,1,4,1),
\]
one obtains
\[
x_+=\sqrt3-1,\qquad x_-=-\sqrt3-1,
\qquad y^2=2\sqrt3.
\]
Only the positive root is admissible, so the two equilibria are
\[
\left(\sqrt3-1,\ \pm\sqrt{2\sqrt3},\ 0\right)
\approx (0.73205,\pm1.86121,0).
\]
The paper instead prints \((0.7321,\pm3.4641,0)\). Those printed points do not satisfy its own equilibrium equations: substituting the rounded values into \(x^2+y^2-4\) gives approximately \(8.53596\), not zero. The number \(3.4641\) is the rounded value of \(2\sqrt3=y^2\), so the printed ordinate is consistent with a missing square root. The paper's reported eigenvalues, however, match the corrected equilibria to the quoted precision.

## Assumptions and scope

All seven parameters are assumed strictly positive, exactly as in the natural positive-parameter regime containing the published example. The invariant-measure statements apply to compactly supported invariant Borel probability measures of the complete flow on their compact invariant support. No assertion is made here about the existence, uniqueness, basin size, or numerical Lyapunov exponents of any particular chaotic attractor.

The primary classification is MSC2020 37C10, dynamics induced by flows and semiflows. The result is about exact flow geometry, fixed points, linear instability, and invariant measures of a smooth autonomous vector field.

## Proof

At an equilibrium, \(z=0\) and
\[
dx^2+ey^2=f,
\qquad
ax+bx^2=cy^2.
\]
Eliminating \(y^2\) gives
\[
(be+cd)x^2+aex-cf=0,
\]
which is \(Ax^2+aex-cf=0\). Its roots are precisely \(x_\pm\). Let \(r=\sqrt{f/d}\). Since
\[
A r^2+ae r-cf=\frac{bef}{d}+ae r>0
\]
and the quadratic is negative at \(x=0\), the positive root always satisfies \(0<x_+<r\), hence it always yields two real values of \(y\).

At the negative endpoint \(-r\),
\[
A r^2-ae r-cf=e r(br-a).
\]
Because the quadratic opens upward and has exactly one negative root, \(x_-\) lies in the admissible interval \([-r,0)\) exactly when \(br\ge a\). Strict inequality gives two signs of \(y\), equality gives the single boundary point \((x_-,0,0)\), and failure of the inequality makes the negative root inadmissible. This proves the two/three/four equilibrium count.

The Jacobian is
\[
J(x,y)=
\begin{pmatrix}
0&0&g\\
2dx&2ey&0\\
-a-2bx&2cy&0
\end{pmatrix}.
\]
At an equilibrium its characteristic polynomial is
\[
p(\lambda)=\lambda^3-2ey\lambda^2+g(a+2bx)\lambda-2gy\bigl(ae+2Ax\bigr).
\]
For \(x=x_+\), one has \(ae+2Ax_+=\Delta\). If \(y>0\), the trace \(2ey\) is positive, so at least one eigenvalue has positive real part. If \(y<0\), write the cubic as \(\lambda^3+\alpha_1\lambda^2+\alpha_2\lambda+\alpha_3\). Then \(\alpha_1,\alpha_2,\alpha_3>0\), but
\[
e(a+2bx_+)-\Delta
=\frac{cd(ae-\Delta)}{A}<0,
\]
so \(\alpha_1\alpha_2-\alpha_3<0\). The cubic Routh-Hurwitz criterion therefore excludes Hurwitz stability and, in fact, gives two roots in the open right half-plane.

For an admissible negative-root equilibrium with \(y<0\), the constant term is negative because \(ae+2Ax_-=-\Delta\); hence \(p(0)<0\) while \(p(\lambda)\to+\infty\) as \(\lambda\to+\infty\), so a positive real eigenvalue exists. For \(y>0\), the positive trace again implies instability. At the boundary case \(b\sqrt{f/d}=a\), the negative equilibrium has \(x_-=-\sqrt{f/d}\), \(y=0\), and
\[
p(\lambda)=\lambda(\lambda^2-ag),
\]
so the eigenvalues include \(+\sqrt{ag}\). Thus every equilibrium is linearly unstable.

Now let \(\mu\) be a compactly supported invariant probability measure. Invariance gives zero mean Lie derivative for each coordinate. Applying this to \(x\), \(y\), and \(z\) gives
\[
g\int z\,d\mu=0,
\]
\[
d\int x^2\,d\mu+e\int y^2\,d\mu-f=0,
\]
and
\[
-a\int x\,d\mu-b\int x^2\,d\mu+c\int y^2\,d\mu=0.
\]
With \(q=\int x^2\,d\mu\), the first three stationary identities follow. Substitution gives
\[
\int x\,d\mu=\frac{cf-Aq}{ae}.
\]
Therefore
\[
\operatorname{Var}_\mu(x)=q-\left(\frac{cf-Aq}{ae}\right)^2.
\]
The numerator factors because \(x_\pm\) are the two roots of \(Ax^2+aex-cf=0\):
\[
\operatorname{Var}_\mu(x)
=\frac{A^2}{a^2e^2}(q-x_+^2)(x_-^2-q).
\]
Nonnegativity of variance gives \(x_+^2\le q\le x_-^2\), while the stationary \(y\)-identity gives \(q\le f/d\). This proves the amplitude bounds.

If \(q=x_+^2\), equality in Cauchy-Schwarz forces \(x=x_+\) almost surely. An invariant measure supported on the hyperplane \(x=x_+\) must also have \(z=0\) on its support because \(\dot x=gz\). The equation \(\dot z=0\) then fixes \(y^2=(f-dx_+^2)/e\), and \(\dot y=0\) follows. Hence the support is contained in \(\{E_+^+,E_+^-\}\). Conversely every probability mixture of these two fixed points is invariant and attains equality.

For the published parameters, direct substitution gives \(A=2\), \(\Delta=4\sqrt3\), \(x_+=\sqrt3-1\), and \(y^2=2\sqrt3\). The packaged symbolic checker verifies the general characteristic polynomial, the Routh-Hurwitz obstruction, the stationary variance factorization, the corrected fixed points, the source eigenvalues, and the nonzero residual of the printed coordinates.

## Verification

The symbolic checker uses exact algebra for the equilibrium polynomial, characteristic polynomial, Routh-Hurwitz expression, and stationary variance factorization. At the source parameters it verifies
\[
x_+=\sqrt3-1,
\qquad
x_-=-\sqrt3-1,
\qquad
|y|=\sqrt{2\sqrt3}\approx1.8612097182,
\]
and numerically reconstructs the eigenvalues
\[
3.9783880614,
\qquad
-0.1279843125\pm2.5428456801i,
\]
matching the paper's quoted spectrum at the positive-\(y\) corrected equilibrium. Substitution of the printed coordinate \((0.7321,3.4641,0)\) into the paper's equation \(x^2+y^2-4=0\) gives residual approximately \(8.53595922\).

## Relationship to prior work

The introducing article states the same seven-parameter vector field and, for its numerical parameter set, prints two equilibria \((0.7321,\pm3.4641,0)\), followed by the eigenvalues quoted above and the conclusion that both equilibria are saddle-foci. Its own equilibrium equations show that the printed ordinates are inconsistent. The corrected ordinates explain why the eigenvalues nevertheless agree: the paper appears to have printed \(y^2=2\sqrt3\) where \(|y|=\sqrt{2\sqrt3}\) was required.

The article does not give the complete positive-parameter equilibrium-count threshold \(b\sqrt{f/d}=a\), the proof that every admissible equilibrium is linearly unstable, or the invariant-measure moment identities and variance factorization above. Targeted searches using the exact title, DOI, printed coordinates, vector-field monomials, equilibrium formula, stationary-moment formula, and close semantic variants did not surface an indexed source containing these exact statements. Related indexed work on stationary balance laws concerns different vector fields and does not imply this theorem.

## Limitations

The result does not independently validate the existence of the paper's numerical chaotic attractor, its bifurcation diagram, entropy calculations, circuit implementation, or parameter-estimation application. Linear instability of all equilibria does not by itself prove that any attractor is self-excited; that classification still depends on basin intersection. Search-based originality checks cannot exclude an unindexed derivation or an equivalent calculation buried in a source not surfaced by the inspected databases.

## References

1. G. Xu, Y. Shekofteh, A. Akgül, C. Li, and S. Panahi, “A New Chaotic System with a Self-Excited Attractor: Entropy Measurement, Signal Encryption, and Parameter Estimation,” *Entropy* 20(2), 86 (2018). DOI: 10.3390/e20020086. Published 27 January 2018.
2. PubMed Central record PMC7512649, full-text mirror of the same article, including Equations (1)–(4) and the printed equilibrium coordinates.
3. MSC2020, 37C10, “Dynamics induced by flows and semiflows.”
