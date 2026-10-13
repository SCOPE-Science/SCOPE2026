# Sharp one-update conditioning law for BFGS on two-curvature quadratics

## Finding
Let
\[
H=H^{\mathsf T}>0,
\qquad
\lambda_{\min}(H)=1,
\qquad
\lambda_{\max}(H)=\kappa.
\]
Initialize the direct BFGS Hessian approximation by
\[
B_0=I.
\]
For a nonzero secant step \(s\), a quadratic objective gives
\[
y=Hs,
\]
and the first update is
\[
B_1
=
I-\frac{ss^{\mathsf T}}{s^{\mathsf T}s}
+
\frac{Hss^{\mathsf T}H}{s^{\mathsf T}Hs}.
\]

For every dimension \(n\ge2\), the exact worst spectral condition number over all such \(H\) and \(s\) is
\[
\boxed{
\sup \kappa_2(B_1)
=
\Gamma(\kappa)
=
\frac{
\left[
(\kappa+2)^{3/2}
+
(\kappa-1)\sqrt{\kappa+8}
\right]^2
}{
27\kappa
}.
}
\]

The bound is attained already in two dimensions by
\[
H=\operatorname{diag}(1,\kappa)
\]
and
\[
s=
\begin{pmatrix}
\sqrt{\kappa/(\kappa+2)}\\[1mm]
\sqrt{2/(\kappa+2)}
\end{pmatrix}.
\]

For every nontrivial condition number,
\[
\boxed{\Gamma(\kappa)>\kappa\qquad(\kappa>1).}
\]
Thus a single standard BFGS update can make the Hessian approximation strictly more ill-conditioned than the true Hessian even though it starts from the perfectly conditioned identity matrix.

The effect becomes large:
\[
\Gamma(\kappa)
=
\frac4{27}\kappa^2+O(\kappa).
\]
Hence the worst one-update condition number grows quadratically in the true Hessian condition number.

For example, at
\[
\kappa=4,
\qquad
H=\operatorname{diag}(1,4),
\qquad
s=
\begin{pmatrix}
\sqrt{2/3}\\
1/\sqrt3
\end{pmatrix},
\]
one obtains
\[
B_1
=
\frac13
\begin{pmatrix}
2&\sqrt2\\
\sqrt2&10
\end{pmatrix}.
\]
Its eigenvalues are
\[
2-\sqrt2
\quad\text{and}\quad
2+\sqrt2,
\]
so
\[
\kappa_2(B_1)
=
3+2\sqrt2
=
5.828427\ldots
>
4
=
\kappa_2(H).
\]

## Assumptions and scope
The result concerns the direct BFGS Hessian update in exact arithmetic on a quadratic objective. The true Hessian is normalized to have smallest eigenvalue one, and the starting approximation is \(B_0=I\). Equivalently, before normalization one may take
\[
B_0=\lambda_{\min}(H)I.
\]

The step \(s\) may be any nonzero secant direction. This is not broader than the first exact-line-search BFGS iteration: every direction in the theorem is realizable as the first BFGS search direction by choosing the starting gradient appropriately.

The result is about the condition number of the Hessian approximation itself. It does not claim that the first BFGS search step has poor objective decrease, nor that later BFGS matrices follow the same one-step extremal law. Scaling \(B_0\) independently of the true Hessian introduces an additional scale parameter and is outside the theorem.

## Proof
Normalize
\[
\|s\|_2=1
\]
and define
\[
q=s^{\mathsf T}Hs,
\qquad
v=Hs-qs,
\qquad
m=\|v\|_2.
\]
Then
\[
1\le q\le\kappa
\]
and
\[
s^{\mathsf T}v=0.
\]

If \(m=0\), then \(s\) is an eigenvector of \(H\) and the update has eigenvalues \(q\) and \(1\); hence its condition number is at most \(\kappa\). Assume \(m>0\), and put
\[
t=\frac{v}{m}.
\]
In the orthonormal basis \((s,t)\), the nontrivial \(2\times2\) block of \(B_1\) is
\[
\widehat B_1
=
\begin{pmatrix}
q&m\\
m&1+m^2/q
\end{pmatrix}.
\]
On the orthogonal complement of \(\operatorname{span}\{s,Hs\}\), the update is exactly the identity. Thus
\[
\det \widehat B_1=q,
\qquad
\operatorname{tr}\widehat B_1
=
q+1+\frac{m^2}{q}.
\]

For every eigenvalue
\[
1\le\lambda\le\kappa,
\]
\[
(\lambda-1)(\kappa-\lambda)\ge0,
\]
so
\[
\lambda^2\le(\kappa+1)\lambda-\kappa.
\]
Averaging this inequality with the spectral weights of \(s\) gives
\[
s^{\mathsf T}H^2s
\le
(\kappa+1)q-\kappa.
\]
Since
\[
m^2=s^{\mathsf T}H^2s-q^2,
\]
we obtain the sharp variance bound
\[
m^2\le(q-1)(\kappa-q).
\]
Equality holds exactly when the spectral support of \(s\) is contained in the endpoint eigenspaces.

Let the two eigenvalues of \(\widehat B_1\) be
\[
\lambda_-\le\lambda_+.
\]
Because
\[
\det(I-\widehat B_1)
=
-\frac{m^2}{q}\le0,
\]
one has
\[
\lambda_-\le1\le\lambda_+.
\]
Therefore the condition number of the full update is
\[
\frac{\lambda_+}{\lambda_-}.
\]

For fixed determinant \(q\), this ratio is a strictly increasing function of
\[
\frac{\operatorname{tr}\widehat B_1}{\sqrt q}.
\]
The variance bound therefore reduces the global problem to maximizing
\[
R_\kappa(q)
=
\frac{\kappa+2-\kappa/q}{\sqrt q},
\qquad
1\le q\le\kappa.
\]
Its derivative has the sign of
\[
3\kappa-(\kappa+2)q,
\]
so the unique maximizer for \(\kappa>1\) is
\[
q_*=\frac{3\kappa}{\kappa+2}.
\]
Endpoint support realizes this mean with squared weight
\[
\frac{2}{\kappa+2}
\]
on the \(\kappa\)-eigenspace and
\[
\frac{\kappa}{\kappa+2}
\]
on the \(1\)-eigenspace.

At \(q_*\),
\[
R_\kappa(q_*)
=
\eta_\kappa
=
\frac{2(\kappa+2)^{3/2}}{3\sqrt{3\kappa}}.
\]
If
\[
K=\frac{\lambda_+}{\lambda_-},
\]
then
\[
\eta_\kappa
=
\sqrt K+\frac1{\sqrt K}.
\]
Solving this equation gives
\[
K
=
\left(
\frac{\eta_\kappa+\sqrt{\eta_\kappa^2-4}}{2}
\right)^2.
\]
Using
\[
(\kappa+2)^3-27\kappa
=
(\kappa-1)^2(\kappa+8)
\]
yields
\[
K=\Gamma(\kappa)
=
\frac{
\left[
(\kappa+2)^{3/2}
+
(\kappa-1)\sqrt{\kappa+8}
\right]^2
}{
27\kappa
}.
\]

To compare with the true Hessian, note that
\[
\left(\sqrt\kappa+\frac1{\sqrt\kappa}\right)^2
=
\frac{(\kappa+1)^2}{\kappa},
\]
while
\[
\eta_\kappa^2
=
\frac{4(\kappa+2)^3}{27\kappa}.
\]
Their difference is
\[
\frac{
(\kappa-1)^2(4\kappa+5)
}{
27\kappa
},
\]
which is positive for every \(\kappa>1\). Since
\[
K\longmapsto \sqrt K+\frac1{\sqrt K}
\]
is strictly increasing for \(K>1\), it follows that
\[
\Gamma(\kappa)>\kappa.
\]

Finally, expanding the closed form gives
\[
\Gamma(\kappa)=\frac4{27}\kappa^2+O(\kappa).
\]

Every extremal direction is realizable by an actual first exact-line-search BFGS step. On
\[
f(x)=\frac12x^{\mathsf T}Hx,
\]
choose
\[
x_0=-H^{-1}s.
\]
Then the initial gradient is \(-s\), so the search direction from \(B_0=I\) is \(s\). Exact line search scales this direction by a positive scalar, and the common scaling of the secant pair cancels from the BFGS update.

## Verification
The embedded `verify.py` uses exact rational arithmetic for the determinant, trace, maximizing Rayleigh quotient, and the endpoint-weight identities. It checks the derivative sign around
\[
q_*=\frac{3\kappa}{\kappa+2}
\]
for several rational \(\kappa\), and it uses high-precision decimal arithmetic to compare the closed-form \(\Gamma(\kappa)\) with the eigenvalue ratio of the corresponding \(2\times2\) block.

For the exact witness \(\kappa=4\), the script verifies
\[
\operatorname{tr}(B_1)=4,
\qquad
\det(B_1)=2,
\]
and hence the eigenvalues
\[
2\pm\sqrt2.
\]

These computations replay algebraic consequences of the proof. The all-dimension supremum follows from the spectral secant inequality and is not inferred from finite experiments.

## Relationship to prior work
The BFGS update and scalar-identity initialization are classical. Erway, Jain, and Marcia review the direct BFGS formula and note that BFGS matrices remain positive definite when the curvature condition holds.

Conditioning of quasi-Newton matrices is also classical. Shanno explicitly formulated quasi-Newton update selection as a conditioning problem. Dennis and Wolkowicz developed condition-related least-change and sizing criteria, and their full analysis notes that low-rank secant updates can become ill-conditioned and that scaling can be used to correct that behavior.

Powell analyzed a different two-dimensional quadratic pathology in depth: the true Hessian there is the identity, while the initial Hessian approximation is poorly conditioned, and the paper studies recurrence relations for successive approximate-Hessian eigenvalues and slow correction. That result does not imply the present theorem, whose initial approximation is the identity and whose true Hessian has condition number \(\kappa\).

The present statement is a sharp one-update comparison between the condition number learned by ordinary unsized BFGS and the condition number of the true quadratic Hessian. Targeted searches under one-update conditioning, identity initialization, secant directions, quadratic Hessians, trace-determinant formulas, and BFGS scaling did not locate the closed form
\[
\Gamma(\kappa)
\]
or the fact that
\[
\Gamma(\kappa)>\kappa
\]
for every \(\kappa>1\).

## Limitations
The theorem normalizes the scalar initialization to the smallest Hessian eigenvalue. A different scalar initialization introduces a second dimensionless parameter and can have a different sharp law.

Only the first BFGS update is classified. Later updates incorporate multiple secant directions and exact-line-search conjugacy, so this theorem is not a multi-step convergence-rate statement.

The exact extremizer uses only the endpoint eigenspaces, which makes the bound dimension independent and attained in dimension two. Additional structural restrictions on the Hessian or the available search directions can reduce the worst case.

The literature comparison leaves a specific residual risk: older conditioning and self-scaling papers may encode this one-update formula in different notation even though the inspected statements and full-text sections did not expose an implication-equivalent theorem.

## References
1. J. B. Erway, V. Jain, and R. F. Marcia, “Shifted L-BFGS Systems,” arXiv:1209.5141, first submitted 2012-09-24; Optimization Methods and Software 29 (2014), 992–1004. DOI 10.1080/10556788.2014.894045.
2. D. F. Shanno, “Conditioning of Quasi-Newton Methods for Function Minimization,” Mathematics of Computation 24 (1970), 647–656. DOI 10.1090/S0025-5718-1970-0274029-X.
3. M. J. D. Powell, “How Bad Are the BFGS and DFP Methods When the Objective Function Is Quadratic?,” Mathematical Programming 34 (1986), 34–47. DOI 10.1007/BF01582161.
4. J. E. Dennis, Jr. and H. Wolkowicz, “Sizing and Least-Change Secant Methods,” SIAM Journal on Numerical Analysis 30 (1993), 1291–1314. DOI 10.1137/0730067.
