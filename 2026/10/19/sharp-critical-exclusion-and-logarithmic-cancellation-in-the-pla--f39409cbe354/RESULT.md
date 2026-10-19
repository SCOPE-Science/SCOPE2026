# Sharp critical exclusion and logarithmic cancellation in the planar Ricker map

## Finding
Consider the two-species planar Ricker map
\[
x_{n+1}=x_n\exp(r-x_n-\alpha y_n),\qquad
 y_{n+1}=y_n\exp(\beta r-\beta x_n-y_n).
\]
Set \(\gamma=1-\alpha\beta\). For every \(\alpha,\beta>0\) and \(r>0\) satisfying \(\alpha\beta<1\), \(0<r<2\), and \(0<\beta r<2\), and every strictly positive initial state \((x_0,y_0)\), there is a finite real number \(C=C(x_0,y_0;r,\alpha,\beta)\) such that
\[
\boxed{\frac1{y_n}=\gamma n+
\left(\frac\gamma2-\frac{\alpha\beta}{r}\right)\log n+C+o(1)}
\qquad(n\to\infty).
\]
In addition,
\[
\boxed{\quad n y_n\longrightarrow\gamma^{-1},\qquad
 x_n=r-\alpha y_n-\frac{\alpha\gamma}{r}y_n^2+O(y_n^3).\quad}
\]
The coefficient of the logarithmic correction is universal (independent of the initial state) and vanishes exactly when \(r=2\alpha\beta/(1-\alpha\beta)\), provided this equality lies within the stated parameter range. On that cancellation surface, \(1/y_n-\gamma n\) has a finite limit. On either side, its leading unbounded correction has opposite signs.

## Assumptions and scope
The parameters \(r,\alpha,\beta\) are fixed as \(n\to\infty\); no uniformity is claimed as they approach the boundary of their range. The recurrence is on the positive quadrant, so every iterate has positive coordinates. The second intrinsic growth parameter is fixed at the invasion-neutral threshold \(s=\beta r\). The strict condition \(\alpha\beta<1\) makes the coexistence branch collide nondegenerately with the axial state \((r,0)\). The restrictions on \(r\) and \(\beta r\) preclude simultaneous flip degeneracies. No claim is made for boundary initial data.

## Proof
**Global reduction.** Theorem 3.6, case R3, of Baigent–Hou–Elaydi–Balreira–Luís [1] states that for \(0<r,s<2\), \(\alpha s\le r\), \(s\le\beta r\), and away from coincident isoclines, every orbit from the strictly positive quadrant converges to \((r,0)\). Here \(s=\beta r\), \(\alpha s=\alpha\beta r<r\), and the isoclines do not coincide. Thus \(x_n\to r\) and \(y_n\to0\). The applicable theorem's proof uses a decreasing quadratic Lyapunov function and the exact ratio monotonicity \(y_{n+1}/x_{n+1}^{\beta}=(y_n/x_n^{\beta})\exp(-\gamma y_n)\); in particular its hypotheses cover the nonhyperbolic equality \(s=\beta r\), not merely the strict exclusion region.

**A stable slaving lemma.** Suppose \(v_n>0\), \(v_{n+1}/v_n\to1\), \(a_n\to a\) with \(|a|<1\), and \(b_n\to b\). If \(z_{n+1}=a_n z_n+b_n v_n\), then \(z_n/v_n\to b/(1-a)\). Indeed the quotient satisfies
\[
\frac{z_{n+1}}{v_{n+1}}
=\left(a_n\frac{v_n}{v_{n+1}}\right)\frac{z_n}{v_n}
 +b_n\frac{v_n}{v_{n+1}};
\]
its affine coefficients converge to a strict contraction, proving boundedness and convergence to its unique fixed point. The same argument with merely bounded \(b_n\) gives \(z_n=O(v_n)\).

**Second-order stable coordinate.** Write
\[
q_n=x_n-r+\alpha y_n,\qquad \gamma=1-\alpha\beta.
\]
The original equations become the exact recurrences
\[
q_{n+1}=(r-\alpha y_n+q_n)e^{-q_n}-r
 +\alpha y_n e^{-\gamma y_n-\beta q_n},\qquad
 y_{n+1}=y_n e^{-\gamma y_n-\beta q_n}.
\]
As \((q_n,y_n)\to(0,0)\), \(y_{n+1}/y_n\to1\). Taylor expansion with a uniform remainder for sufficiently small \((q,y)\) gives
\[
q_{n+1}=(1-r)q_n-\alpha\gamma y_n^2
 +O(q_n^2+y_n|q_n|+y_n^3).
\]
Rewrite this as \(q_{n+1}=a_nq_n+b_n y_n^2\) with \(a_n\to1-r\), \(b_n\to-\alpha\gamma\). Since \(0<r<2\), the slaving lemma yields
\[
q_n/y_n^2\to c:=-\frac{\alpha\gamma}{r}.
\]
For the sharper remainder, let \(t_n=q_n-cy_n^2\). Now \(q_n=O(y_n^2)\), and the exact recurrences imply \(y_{n+1}^2=y_n^2+O(y_n^3)\). Substituting and using \((1-r)c-\alpha\gamma=c\) gives
\[
t_{n+1}=(1-r)t_n+O(y_n^3).
\]
Apply the bounded-forcing form of the same lemma with \(v_n=y_n^3\), whose successive ratio tends to one. Therefore \(t_n=O(y_n^3)\), proving
\[
q_n=-\frac{\alpha\gamma}{r}y_n^2+O(y_n^3).
\]

**Scalar expansion and summation.** Substitute this expression into the second recurrence and expand the exponential:
\[
y_{n+1}=y_n-\gamma y_n^2+
 \left(\frac{\gamma^2}{2}+\frac{\alpha\beta\gamma}{r}\right)y_n^3
 +O(y_n^4).
\]
With \(w_n=1/y_n\), reciprocal expansion gives
\[
w_{n+1}=w_n+\gamma+
\frac{A}{w_n}+O(w_n^{-2}),
\qquad A=\frac{\gamma^2}{2}-\frac{\alpha\beta\gamma}{r}.
\]
Because \(w_n\to\infty\) and \(\gamma>0\), its differences tend to \(\gamma\), so \(w_n/n\to\gamma\). Consequently \(1/w_n=O(1/n)\), and the same recurrence gives \(w_n=\gamma n+O(\log n)\). Hence
\[
\frac{1}{w_n}-\frac{1}{\gamma n}=O\!\left(\frac{\log n}{n^2}\right).
\]
For \(n\ge1\), define
\[
D_n=w_n-\gamma n-\frac A\gamma\log n.
\]
Using \(\log(n+1)-\log n=1/n+O(n^{-2})\), the reciprocal recurrence yields
\[
D_{n+1}-D_n=O\!\left(\frac{\log n}{n^2}\right).
\]
This is absolutely summable; therefore \(D_n\to C\in\mathbb R\). Since \(A/\gamma=\gamma/2-\alpha\beta/r\), the claimed expansion follows, as does the asymptotic for \(x_n\). The logarithmic coefficient is zero precisely at the stated \(r\)-value. This completes the proof.

## Verification
The accompanying standard-library program `verify.py` checks the exact rational coefficient identities for four admissible parameter triples and iterates the original two-dimensional recurrence through \(240{,}000\) steps per triple. It compares the empirical two-scale logarithmic slope, the stable-coordinate ratio, and the leading population amplitude with the theorem; all four checks pass, including \((r,\alpha,\beta)=(2/3,1/2,1/2)\) on the cancellation surface. These finite calculations corroborate but do not prove the asymptotic theorem. The full proof above supplies the infinite-time quantifiers.

## Relationship to prior work
Baigent et al. [1], available online June 26, 2023, establish global convergence to the boundary state on this transcritical parameter line; their Theorem 3.6 R3 supplies the global input, but does not state the \(n^{-1}\) extinction amplitude, the logarithmic correction, or its cancellation surface. Luís–Elaydi–Oliveira [2] establish local bifurcation and center-manifold theory for the same competition map. Kulakov–Neverova–Frisman [3] study dynamic modes and multistability, including transcritical boundaries, in the related two-species model. The contribution here is not the existence of the transcritical bifurcation or a generic center-manifold normal form: it is the global, initial-condition-independent **explicit coefficient**, the existence of a finite corrected constant for every positive trajectory, and the parameter surface eliminating the logarithmic drift.

## Limitations
This does not extend to \(\gamma\le0\), to either flip endpoint, to noncritical invasion parameters \(s\ne\beta r\), or to parameter-uniform double scaling. The orbit-dependent constant \(C\) is asserted to exist but is not given in elementary closed form. Some older center-manifold literature was not available in full text; equivalent previously implicit asymptotics remain a priority risk. The proof depends on the published global-attraction theorem [1]; it independently derives all asymptotic coefficients and summability estimates.

## References
[1] S. Baigent, Z. Hou, S. Elaydi, E. C. Balreira and R. Luís, *A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds*, Journal of Difference Equations and Applications 29 (2023), 575–591, https://doi.org/10.1080/10236198.2023.2222855. First verified public version: June 26, 2023.

[2] R. Luís, S. Elaydi and H. Oliveira, *Stability of a Ricker-type competition model and the competitive exclusion principle*, Journal of Biological Dynamics 5 (2011), 636–660, https://doi.org/10.1080/17513758.2011.581764.

[3] M. Kulakov, G. Neverova and E. Frisman, *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, Mathematics 10 (2022), 1076, https://doi.org/10.3390/math10071076.
