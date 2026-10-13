# Three endemic equilibria and an unstable saddle under the published SVI hypotheses

## Finding

Consider
\[
S'=(1-\pi)\Lambda-\mu S-\beta_b S f(I),
\]
\[
V'=\pi\Lambda-\mu V-\beta_v V g(I),
\]
\[
I'=\beta_b S f(I)+\beta_v V g(I)-(\mu+\delta)I.
\]

The published incidence assumptions require
\[
f(0)=g(0)=0,
\qquad
f'(I)>0,
\qquad
g'(I)>0,
\]
and
\[
f(I)\le f'(0)I,
\qquad
g(I)\le g'(0)I.
\]

Choose
\[
f(I)=g(I)=I\left(1-\frac{3I}{(1+I)^2}\right)
\]
and
\[
\Lambda=96,\qquad
\pi=\frac12,\qquad
\mu=1,\qquad
\delta=2,\qquad
\beta_b=\beta_v=\frac1{10}.
\]
These functions satisfy every printed incidence hypothesis, while the source reproduction number is
\[
\mathcal R_0=\frac{16}{5}>1.
\]

The positive-equilibrium equation factors exactly as
\[
-\frac{3I(I-2)(I^2-21I+11)}
{I^3+9I^2+21I+10}=0.
\]
Therefore the system has three distinct positive endemic equilibria, with infected coordinates
\[
I_1=\frac{21-\sqrt{397}}2,
\qquad
I_2=2,
\qquad
I_3=\frac{21+\sqrt{397}}2.
\]

At the middle equilibrium,
\[
E_2=(45,45,2),
\]
the Jacobian has one positive eigenvalue. Thus the source's claimed uniqueness and its blanket local-stability conclusion for the endemic equilibrium when \(\mathcal R_0>1\) are both false under the assumptions as printed.

## Assumptions and scope

All demographic and transmission parameters are positive, with
\[
0<\pi<1.
\]
The incidence functions are continuously differentiable on the nonnegative half-line.

The claim addresses the deterministic equilibrium theorem under the source's stated incidence assumptions. It does not classify the stability of the other two endemic equilibria.

The result also does not assert that the theorem cannot be repaired. A stronger condition controlling the ratio
\[
\frac{f(I)}I
\]
and its \(g\)-analogue is a natural repair direction.

## Proof

Let
\[
h(I)=I\left(1-\frac{3I}{(1+I)^2}\right).
\]
Then
\[
h'(I)=1-\frac{6I}{(1+I)^3}.
\]
The function
\[
\frac{6I}{(1+I)^3}
\]
has maximum \(8/9\) on the nonnegative half-line, attained at \(I=1/2\). Therefore
\[
h'(I)\ge\frac19>0.
\]

Also,
\[
0\le\frac{3I}{(1+I)^2}\le\frac34,
\]
so
\[
0<h(I)\le I
\]
for every \(I>0\), and
\[
h'(0)=1.
\]
Thus \(f=g=h\) satisfy the source assumptions.

At the disease-free equilibrium,
\[
S_0=V_0=48.
\]
Hence
\[
\mathcal R_0
=
\frac{
\beta_b f'(0)S_0+\beta_vg'(0)V_0
}{
\mu+\delta
}
=
\frac{16}{5}.
\]

At a positive equilibrium,
\[
S=\frac{48}{1+h(I)/10},
\qquad
V=\frac{48}{1+h(I)/10}.
\]
Substitution into the infected equation gives
\[
\frac{1}{10}Sh(I)+\frac{1}{10}Vh(I)-3I
=
-\frac{3I(I-2)(I^2-21I+11)}
{I^3+9I^2+21I+10}.
\]
The denominator is positive for \(I>0\). The positive roots are exactly
\[
\frac{21-\sqrt{397}}2,
\qquad
2,
\qquad
\frac{21+\sqrt{397}}2.
\]
Both quadratic roots are positive because
\[
21>\sqrt{397}.
\]

For every positive equilibrium,
\[
S+V+I
=
\frac{\Lambda}{\mu}-\frac{\delta}{\mu}I
=
96-2I.
\]
The largest infected root is below \(21\), so every listed equilibrium has positive total population and lies below the source bound
\[
S+V+I\le96.
\]
The explicit formulas also give \(S>0\) and \(V>0\).

At \(I=2\),
\[
h(2)=\frac23,
\qquad
h'(2)=\frac59,
\]
and
\[
S=V=45.
\]
The exact Jacobian is
\[
J(E_2)=
\begin{pmatrix}
-\frac{16}{15}&0&-\frac52\\
0&-\frac{16}{15}&-\frac52\\
\frac1{15}&\frac1{15}&2
\end{pmatrix}.
\]
Its characteristic polynomial factors as
\[
\left(\lambda+\frac{16}{15}\right)
\left(
\lambda^2-\frac{14}{15}\lambda-\frac95
\right),
\]
so its eigenvalues are
\[
-\frac{16}{15},
\qquad
\frac{7-\sqrt{454}}{15},
\qquad
\frac{7+\sqrt{454}}{15}.
\]
The last value is positive, proving that \(E_2\) is a saddle.

The source proof defines
\[
\widehat l_{33}
=
-\beta_bS^*f'(I^*)
-\beta_vV^*g'(I^*)
+\mu+\delta
\]
and claims it is positive by replacing the derivatives with the ratios \(f(I^*)/I^*\) and \(g(I^*)/I^*\). At the exact witness,
\[
\frac{h(2)}2=\frac13
<
\frac59=h'(2),
\]
and
\[
\widehat l_{33}
=
-2.
\]
Thus the sign step used in the local-stability proof is not implied by the printed hypotheses.

## Verification

The bundled `verify.py` uses exact symbolic arithmetic.

It verifies the derivative lower bound algebraically, reconstructs the reproduction number, factors the endemic-equilibrium equation, checks the three positive roots, and reconstructs the Jacobian and its characteristic polynomial at \(E_2\).

It also verifies
\[
\widehat l_{33}=-2.
\]

No finite simulation or floating-point root search is used to establish the accepted claim.

## Relationship to prior work

The motivating article states that, under its general incidence assumptions, the disease-free and endemic equilibrium behavior is determined by the reproduction number. Its Theorem 2.1(ii) asserts uniqueness and local asymptotic stability of the endemic equilibrium when \(\mathcal R_0>1\).

The missing ratio condition is not merely technical. In related epidemic modeling, stronger assumptions are explicitly imposed. For example, Zhang, Ma, and Din require the incidence ratio to be non-increasing and require
\[
f(I)>If'(I),
\]
which directly supplies the inequality used but not assumed in the motivating proof.

Broader nonlinear-incidence epidemic literature also documents multiple endemic equilibria and bifurcation phenomena. Those results concern different models and do not imply the exact SVI counterexample above.

The new content is the source-specific admissible incidence function, the exact three-endemic-equilibrium factorization, the exact saddle spectrum, and the explicit identification of the hypothesis gap in the published proof.

## Limitations

The other two endemic equilibria are not classified here.

The result does not provide necessary and sufficient replacement hypotheses for uniqueness and local stability.

A stronger decreasing-incidence-ratio assumption may repair the theorem, but that repaired theorem is not proved here.

## References

1. X. Wang, K. Wang, Z. Teng, “Global dynamics and density function in a class of stochastic SVI epidemic models with Lévy jumps and nonlinear incidence,” AIMS Mathematics 8 (2023), 2829–2855. DOI: 10.3934/math.2023148.
2. Y. Zhang, X. Ma, A. Din, “Stationary distribution and extinction of a stochastic SEIQ epidemic model with a general incidence function and temporary immunity,” AIMS Mathematics 6 (2021), 12359–12378. DOI: 10.3934/math.2021715.
3. S. Ruan, W. Wang, “Dynamical behavior of an epidemic model with a nonlinear incidence rate,” Journal of Differential Equations 188 (2003), 135–163. DOI: 10.1016/S0022-0396(02)00089-X.
