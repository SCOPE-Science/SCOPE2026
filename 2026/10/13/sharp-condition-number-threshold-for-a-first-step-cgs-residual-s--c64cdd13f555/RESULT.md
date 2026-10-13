# Sharp condition-number threshold for a first-step CGS residual spike

## Finding
Let \(A\) be a real symmetric positive-definite matrix whose spectrum lies in \([\mu,L]\), and write
\[
\kappa=\frac{L}{\mu}.
\]
Run unpreconditioned conjugate gradients squared (CGS) from an arbitrary initial guess with nonzero residual \(r_0\), using the standard shadow residual
\[
\widetilde r_0=r_0.
\]
Then the first completed CGS residual obeys the exact sharp envelope
\[
\boxed{
\frac{\|r_1\|_2^2}{\|r_0\|_2^2}
\le
\mathcal G(\kappa)
:=
\max_{t\ge0}
\frac{(\kappa-1)^4t(t^2-t+1)}{(1+\kappa t)^4}
}.
\]
Every value of the right-hand optimization is realized by a two-dimensional diagonal problem with eigenvalues \(\mu\) and \(L\), so the envelope is dimension-free and sharp.

The function \(\mathcal G\) is strictly increasing for \(\kappa>1\). Hence there is a unique threshold \(\kappa_*>1\) at which \(\mathcal G(\kappa_*)=1\), and
\[
\|r_1\|_2\le\|r_0\|_2
\quad\text{for every such SPD problem}
\quad\Longleftrightarrow\quad
1\le\kappa\le\kappa_*.
\]
The threshold is
\[
\boxed{\kappa_*=3.442815869257\ldots}.
\]
It is the unique root greater than one of
\[
P(\kappa)=
\kappa^{12}+8\kappa^{10}-72\kappa^9+122\kappa^8-436\kappa^7+322\kappa^6
-436\kappa^5+122\kappa^4-72\kappa^3+8\kappa^2+1.
\]
Because this polynomial is reciprocal, setting \(y=\kappa+\kappa^{-1}\) reduces it to
\[
Q(y)=y^6+2y^4-72y^3+99y^2-220y+92.
\]
The relevant root is the unique zero of \(Q\) with \(y>2\).

The worst first-step spike grows rapidly with conditioning:
\[
\mathcal G(\kappa)\sim\frac{27}{256}\kappa^3,
\qquad
\sup\frac{\|r_1\|_2}{\|r_0\|_2}
\sim\frac{3\sqrt3}{16}\kappa^{3/2}.
\]
Thus the familiar irregular residual behavior of CGS is already quantitatively visible in the first step on SPD matrices.

An exact two-dimensional witness at \(\kappa=4\) is
\[
A=\operatorname{diag}(1,4),
\qquad
x_0=0,
\qquad
b=(4,1)^{\mathsf T}.
\]
For this problem,
\[
\alpha_0=\frac{17}{20},
\qquad
r_1=
\left(\frac9{100},\frac{144}{25}\right)^{\mathsf T},
\]
and therefore
\[
\frac{\|r_1\|_2^2}{\|r_0\|_2^2}
=
\frac{331857}{170000}>1.
\]

## Assumptions and scope
The result is for exact arithmetic, unpreconditioned CGS, a real SPD coefficient matrix, and the conventional choice \(\widetilde r_0=r_0\). The initial guess is arbitrary; only its nonzero residual matters.

The theorem concerns the first completed CGS residual in the Euclidean norm. It does not assert a monotone residual history beyond the first step, and it does not give a comparable condition-number-only law for nonsymmetric or nonnormal matrices.

The condition number is the spectral SPD condition number \(\kappa=L/\mu\). Equality in the sharp envelope needs only a two-dimensional diagonal matrix, so no nonnormality is involved in the worst first-step behavior.

## Proof
At the first CGS step, with \(\widetilde r_0=r_0\), the scalar is
\[
\alpha_0=
\frac{r_0^{\mathsf T}r_0}{r_0^{\mathsf T}Ar_0}.
\]
The standard CGS update gives
\[
r_1=(I-\alpha_0A)^2r_0.
\]
This is the first-degree BiCG residual polynomial applied twice.

Diagonalize \(A\) orthogonally and write the squared normalized spectral components of \(r_0\) as weights \(w_i\). If a random variable \(X\) takes eigenvalue \(\lambda_i\) with probability \(w_i\), then
\[
m=\mathbb E X
=\frac{r_0^{\mathsf T}Ar_0}{r_0^{\mathsf T}r_0},
\qquad
\alpha_0=\frac1m,
\]
and
\[
\frac{\|r_1\|_2^2}{\|r_0\|_2^2}
=
\mathbb E\left(1-\frac Xm\right)^4
=
\frac{\mathbb E(X-m)^4}{m^4}.
\]
Scale by \(\mu\), so \(X\in[1,\kappa]\).

For fixed mean \(m\), the function
\[
x\longmapsto(x-m)^4
\]
is convex on \([1,\kappa]\). Its secant line through the two endpoints lies above it. Taking expectations therefore shows that, among all spectral measures with the same mean, the fourth central moment is maximized by the endpoint distribution on \(\{1,\kappa\}\). Hence the global extremum is attained by a two-eigenvalue problem.

Let \(q\) be the weight at \(\kappa\). Then
\[
m=1+q(\kappa-1)
\]
and direct simplification gives
\[
\frac{\|r_1\|_2^2}{\|r_0\|_2^2}
=
\frac{(\kappa-1)^4q(1-q)\bigl(q^3+(1-q)^3\bigr)}{\bigl(1+q(\kappa-1)\bigr)^4}.
\]
Set
\[
t=\frac{q}{1-q}.
\]
This becomes
\[
G_\kappa(t)=
\frac{(\kappa-1)^4t(t^2-t+1)}{(1+\kappa t)^4},
\]
proving the sharp envelope.

For every fixed \(t>0\),
\[
\frac{\partial}{\partial\kappa}\log G_\kappa(t)
=
\frac{4(1+t)}{(\kappa-1)(1+\kappa t)}>0.
\]
The maximizing \(t\) is positive for every \(\kappa>1\), so \(\mathcal G(\kappa)\) is strictly increasing. Also \(\mathcal G(\kappa)\to0\) as \(\kappa\downarrow1\), while choosing \(t=1/(3\kappa)\) shows that \(\mathcal G(\kappa)\to\infty\). Thus a unique threshold \(\kappa_*>1\) exists.

At any interior maximizer,
\[
\frac{\partial}{\partial t}G_\kappa(t)=0
\]
is equivalent to
\[
\kappa t^3-(2\kappa+3)t^2+(3\kappa+2)t-1=0.
\]
At the threshold this equation holds together with \(G_\kappa(t)=1\). Exact elimination of \(t\) gives
\[
16\kappa(\kappa^2+\kappa+1)P(\kappa)=0,
\]
where \(P\) is the displayed reciprocal degree-twelve polynomial. Since \(\kappa_*>1\), it follows that \(P(\kappa_*)=0\).

Dividing \(P(\kappa)\) by \(\kappa^6\) and setting
\[
y=\kappa+\kappa^{-1}
\]
gives the displayed polynomial \(Q(y)\). To see uniqueness for \(\kappa>1\), put \(y=z+2\). Then
\[
Q(z+2)=z^6+12z^5+62z^4+104z^3-45z^2-432z-432.
\]
Its coefficient sequence has exactly one sign change. Descartes' rule therefore gives at most one positive zero. Since \(Q(2)=-432\) and \(Q(y)\to+\infty\), there is exactly one zero with \(y>2\), hence exactly one reciprocal pair of positive roots of \(P\), with exactly one member greater than one. Exact rational evaluation isolates that root as
\[
3.442815869<\kappa_*<3.442815870.
\]

For the asymptotic law set \(u=\kappa t\). Then
\[
\frac{G_\kappa(u/\kappa)}{\kappa^3}
=
\left(1-\frac1\kappa\right)^4
\frac{u\left(1-u/\kappa+u^2/\kappa^2\right)}{(1+u)^4}.
\]
For \(0\le u\le\kappa\), the parenthetical quadratic is at most one, while for \(u\ge\kappa\) the contribution is uniformly negligible after division by \(\kappa^3\). The limiting maximization is therefore
\[
\max_{u\ge0}\frac{u}{(1+u)^4}
=
\frac{27}{256},
\]
attained at \(u=1/3\). This proves the stated asymptotics.

Finally, for the exact witness \(A=\operatorname{diag}(1,4)\) and \(r_0=b=(4,1)^{\mathsf T}\),
\[
\alpha_0=\frac{17}{20}
\]
and the identity \(r_1=(I-\alpha_0A)^2r_0\) gives the displayed rational residual and norm ratio.

## Verification
The embedded `verify.py` uses only Python's standard library and exact rational arithmetic for all certificate checks except the printed decimal approximation.

It verifies the first-step rational witness exactly, checks the reciprocal-polynomial reduction \(P(\kappa)/\kappa^6=Q(\kappa+\kappa^{-1})\) by Laurent-coefficient identities, verifies the Descartes coefficient pattern of \(Q(z+2)\), and certifies opposite exact signs of \(P\) at
\[
\kappa=3.442815869
\quad\text{and}\quad
\kappa=3.442815870.
\]
It also checks the stationary-point algebra and the exact elimination polynomial with symbolic integer-polynomial arithmetic implemented in the checker.

The universal endpoint reduction and monotonicity argument are analytic; finite tests are not used as substitutes for those steps.

## Relationship to prior work
Sonneveld introduced CGS as a transpose-free Lanczos-type method based on a polynomial variant of conjugate gradients. The original paper appeared in the January 1989 issue of SIAM Journal on Scientific and Statistical Computing and is classified under MSC 65F10 and 65N20. The exact day recorded in bibliographic metadata is 1989-01-01.

Freund later emphasized that both BiCG and CGS can show irregular convergence with wild oscillations in the residual norm and introduced TFQMR to smooth that behavior. This establishes that residual spikes are a recognized structural drawback of CGS, but it does not give a sharp SPD first-step condition-number frontier.

Aihara's full-text treatment of Lanczos-type product methods states explicitly that the CGS residual is the square of the BiCG residual polynomial,
\[
r_k^{\mathrm{CGS}}=R_k(A)^2r_0,
\]
and again notes the larger residual oscillations of CGS. That identity supplies the standard algorithmic context for the first-step calculation here. The present result specializes the first polynomial to an SPD spectral measure, solves the exact worst-case moment problem, and obtains the threshold and asymptotic growth law.

Searches using CGS, squared residual polynomial, first residual, SPD, positive definite, condition number, residual amplification, residual spike, endpoint spectrum, and the numerical threshold did not locate an implication-equivalent theorem. The closest retrieved results concern other Krylov or stationary methods and do not determine the CGS envelope.

## Limitations
The theorem is first-step only. Later CGS coefficients depend on the evolving biorthogonal recurrences and are not controlled by the one-variable envelope proved here.

The result assumes exact arithmetic and no preconditioner. Finite-precision residual gaps and preconditioned spectra can alter observed behavior.

The SPD assumption is essential to the spectral-probability reduction. Nonnormal CGS can exhibit much more complicated behavior, so the threshold is not a universal nonsymmetric guarantee.

The original 1989 CGS article was inspected through publisher abstract and bibliographic material rather than complete public full text. The central squared-polynomial identity was independently checked in a later full-text source. Residual originality risk remains that an older convergence analysis may contain the same first-step extremum under different terminology.

## References
1. P. Sonneveld, “CGS, A Fast Lanczos-Type Solver for Nonsymmetric Linear Systems,” SIAM Journal on Scientific and Statistical Computing 10 (1989), 36–52, DOI 10.1137/0910004. Bibliographic date: 1989-01-01.
2. R. W. Freund, “A Transpose-Free Quasi-Minimal Residual Algorithm for Non-Hermitian Linear Systems,” SIAM Journal on Scientific Computing 14 (1993), 470–482, DOI 10.1137/0914029.
3. K. Aihara, “GPBi-CGstab(L): A Lanczos-type product method unifying Bi-CGstab(L) and GPBi-CG,” Numerical Linear Algebra with Applications 27 (2020), e2298, DOI 10.1002/nla.2298.
