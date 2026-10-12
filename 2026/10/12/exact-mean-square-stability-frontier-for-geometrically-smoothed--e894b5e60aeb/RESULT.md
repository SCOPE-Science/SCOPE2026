# Exact mean-square stability frontier for geometrically smoothed Kaczmarz on orthogonal systems

## Finding

For the published Kaczmarz with geometrically smoothed momentum (KGSM), the exact **mean-square** stability boundary can be solved on every consistent diagonal system, for all row probabilities induced by row-norm sampling. This is different from the signed first-moment rate determined in the defining paper.

Let \(0<\pi<1\), \(0\le\beta<1\), and \(0\le M\le1\). Define
\[
 d=1-\beta,\qquad
 L=2\beta^2\pi-3\beta^2+2\beta-2\pi+1,\qquad
 C=\beta^2(1-\pi)-\beta\pi-1,
\]
\[
 M_*(\pi,\beta)=\frac{-L+\sqrt{L^2-8d^2C}}{4d^2}.
\]
For a nonzero initial error in a diagonal coordinate sampled with probability \(\pi\), mean-squared error converges geometrically to zero **exactly when** \(M<M_*(\pi,\beta)\). At equality it does not converge to zero; above equality it grows exponentially. The positive root is well-defined since \(C<0\).

In particular, for two equally weighted orthogonal rows,
\[
 M_*(1/2,\beta)=\frac{\sqrt{\beta+2}-\beta}{2(1-\beta)}.
\]
The critical smoothing parameter at which the entire allowed range \(M\le1\) becomes strictly stable is \(\beta_c=(5-\sqrt{17})/2\): for \(\beta>\beta_c\), all allowed masses are mean-square stable; at \(\beta=\beta_c\), \(M=1\) is a nondecaying boundary; and for \(0\le\beta<\beta_c\) a strict unstable mass interval exists. In particular, \(M_*(1/2,0)=1/\sqrt2\).

## Assumptions and scope

Fix any integer \(n\ge2\), an invertible diagonal real matrix \(A=\operatorname{diag}(a_1,\ldots,a_n)\), and a consistent system \(Ax=b\) with solution \(x_*\). Draw row indices independently with probabilities \(\pi_j=a_j^2/\sum_i a_i^2\in(0,1)\), exactly the source's row-norm sampling rule. Initialize \(x_0\) deterministically and momentum \(y_0=0\). At each iteration, follow the source's update exactly:
\[
 x_{k+1}=x_k-\frac{a_j(x_k)_j-b_j}{a_j^2}\,a_j e_j+My_k,
 \qquad y_{k+1}=\beta y_k+(1-\beta)(x_{k+1}-x_k),
\]
where \(a_j e_j\) is the \(j\)-th row vector and \(j\) is the selected row index. Here \(M\in[0,1]\) and \(\beta\in[0,1)\). There is no noise, sketching error, finite-precision effect, or nonorthogonality.

For each coordinate with \((x_0-x_*)_j\ne0\), its mean square converges to zero iff \(M<M_*(\pi_j,\beta)\). If an initial error vanishes in a coordinate, that coordinate stays identically zero. Consequently, the full expected squared Euclidean error converges to zero for **every** initial \(x_0\) iff
\[
 M<\min_{1\le j\le n}M_*(\pi_j,\beta).
\]

## Proof

**1. Exact second-moment recurrence.** Fix a coordinate and write \(u_k=(x_k-x_*)_j\), \(v_k=(y_k)_j\). The selection indicator \(I_k\) is independent of the past and has Bernoulli probability \(\pi\). Put \(d=1-\beta\) and \(c=\beta+dM\). The published update is precisely
\[
 (u_{k+1},v_{k+1})=\begin{cases}
 (u_k+Mv_k,\,cv_k),&I_k=0,\\
 (Mv_k,\,-du_k+cv_k),&I_k=1.
 \end{cases}
\]
Hence \(z_k=(\mathbb E u_k^2,\mathbb E(u_kv_k),\mathbb E v_k^2)^\mathsf T\) obeys \(z_{k+1}=T_{\pi,\beta,M}z_k\), where
\[
T_{\pi,\beta,M}=\begin{pmatrix}
1-\pi&2(1-\pi)M&M^2\\
0&(1-\pi)c-\pi Md&Mc\\
\pi d^2&-2\pi dc&c^2
\end{pmatrix}.
\]
This is an exact expectation identity, not a finite-data approximation.

**2. Exact determinant and unique positive boundary.** Expanding the displayed matrix yields
\[
\det(I_3-T_{\pi,\beta,M})
=\pi(\beta-1)\bigl(2d^2M^2+LM+C\bigr).
\]
Since \(d>0\) and \(C=\beta^2(1-\pi)-\beta\pi-1<0\), the quadratic has exactly one positive real root, namely \(M_*\) above. At \(M=0\), the eigenvalues of \(T\) are \(1-\pi\), \((1-\pi)\beta\), and \(\beta^2\), all strictly inside the unit disk.

**3. A positive-matrix-map stability argument.** The recurrence is the action on symmetric \(2\times2\) covariance matrices of the positive linear map \(\mathcal L(X)=(1-\pi)J_0XJ_0^\mathsf T+\pi J_1XJ_1^\mathsf T\), with
\[
J_0=\begin{pmatrix}1&M\\0&c\end{pmatrix},\qquad
J_1=\begin{pmatrix}0&M\\-d&c\end{pmatrix}.
\]
The spectral radius of such a positive map is a nonnegative real eigenvalue with a nonzero positive-semidefinite eigenmatrix. For completeness, this finite-dimensional fact follows by perturbing the map by \(X\mapsto\epsilon\operatorname{tr}(X)I\), applying Brouwer's fixed-point theorem to the compact convex set of trace-one positive-semidefinite matrices, and noting that a positive-definite eigenmatrix forces its eigenvalue to equal the spectral radius by order bounds. Passing to a subsequence as \(\epsilon\downarrow0\) gives the stated eigenmatrix at the unperturbed spectral radius. Thus, whenever the spectral radius reaches one, \(\det(I_3-T)=0\).

The spectral radius depends continuously on \(M\), starts strictly below one at \(M=0\), and cannot equal one before \(M_*\) because the determinant has no zero in that interval. It is therefore strictly below one for \(M<M_*\). At \(M=M_*\), continuity gives spectral radius exactly one. For \(M>M_*\), the displayed determinant is negative, so \(T\) has a real eigenvalue exceeding one (a negative product of the three factors \(1-\lambda_i\) forces at least one real \(\lambda_i>1\)); hence the spectral radius exceeds one.

**4. Excitation by every nonzero initial error.** For initial \(v_0=0\) and \(u_0\ne0\), after a single step the covariance is the strictly positive-definite matrix
\[
X_1=u_0^2\operatorname{diag}(1-\pi,\pi d^2).
\]
Let \(V\succeq0\), \(V\ne0\), be the positive-semidefinite eigenmatrix of \(\mathcal L\) at its spectral radius \(\rho\). As \(X_1\succ0\), there exists \(\delta>0\) with \(X_1\succeq\delta V\). Positivity gives \(X_{k+1}\succeq\delta\rho^kV\). Whenever \(M>0\), necessarily \(V_{11}>0\), since a positive-semidefinite \(V\) with \(V_{11}=0\) has \(V_{12}=0\) and \((\mathcal L V)_{11}=M^2V_{22}>0\), contradicting the eigenvector equation. Consequently \(\mathbb E u_{k+1}^2\ge\delta\rho^kV_{11}\): it remains bounded away from zero when \(\rho=1\) and grows exponentially when \(\rho>1\). This proves the sharp coordinatewise classification, including endpoints. Summing over finitely many orthogonal coordinates yields the full-system statement.

**5. Simplified frontier and failure of signed means to diagnose mean-square growth.** Substituting \(\pi=1/2\) into the quadratic yields the unique positive root
\[
M_*(1/2,\beta)=\frac{\sqrt{\beta+2}-\beta}{2(1-\beta)};
\]
setting it equal to one gives \(\beta^2-5\beta+2=0\) and the permitted root \(\beta_c=(5-\sqrt{17})/2\).

For general \(\pi\), signed first moments evolve with the matrix
\[
H=\begin{pmatrix}1-\pi&M\\-\pi(1-\beta)&\beta+(1-\beta)M\end{pmatrix}.
\]
Its trace and determinant satisfy the strict degree-two Schur conditions \(1-\det H>0\), \(1-\operatorname{tr}H+\det H=\pi(1-\beta)>0\), and \(1+\operatorname{tr}H+\det H>0\), whenever \(M<1\). Therefore every signed coordinate mean converges geometrically for all \(0\le M<1\), whether or not its mean square converges. As a rational witness, take \(A=I_2\), \(b=0\), \(\beta=0\), \(M=9/10\), and a nonzero initial error. The two signed-mean eigenvalues have modulus \(\sqrt{9/10}<1\), while \(\det(I_3-T)=-31/100<0\), so the actual mean-squared error grows exponentially. No assumption about the sign of individual errors is used.

## Verification

The standalone Python 3 standard-library `verify.py` reconstructs the source-form two-branch recurrence, checks the symbolic determinant identity at 64 exact rational triples, and reproduces each of the first five second-moment vectors through complete enumeration of Bernoulli row histories (320 exact checks). It also tests the equal-probability closed root and the rational divergence witness. Run `python3 verify.py` in the directory containing this document. The program is corroboration; the all-parameter conclusions follow from the displayed algebra and covariance-cone proof, not from finite tests.

## Relationship to prior work

Alderman, Luikart, and Marshall (arXiv:2401.09415, first public 17 January 2024) define KGSM by the identical iteration and derive a \(2\times2\) **signed first-moment** recurrence. In Section 4.2 they explicitly ask for the critical momentum parameter and convergence of expected absolute or Euclidean errors. The present calculation answers that question in the natural exact orthogonal-row family, including an arbitrary number of distinct row probabilities and a sharp mean-square/nondecay boundary. The first-moment result cannot imply this conclusion: the rational example has convergent first moments but divergent second moments. Bollapragada, Chen, and Ward (arXiv:2206.07553) study minibatch heavy-ball momentum with a different update and primarily sufficient acceleration estimates; their method is not KGSM with the displayed geometric smoothing state. Classical randomized Kaczmarz bounds concern \(M=0\), for which this frontier reduces to convergence.

## Limitations

Only consistent diagonal systems with positive row probabilities, independent sampling, \(y_0=0\), and exact arithmetic are included. The theorem characterizes second moments, not almost-sure convergence, finite-precision behavior, or optimal acceleration on nonorthogonal systems. Nonzero initial momentum and inconsistent data are not covered. While no inspected source established this sharp KGSM frontier, a specialized unindexed derivation cannot be excluded.

## References

1. S. J. Alderman, R. W. Luikart, N. F. Marshall, *Randomized Kaczmarz with geometrically smoothed momentum*, arXiv:2401.09415v1 (17 January 2024), full text arXiv:2401.09415v3, Sections 1.2, 1.5, 2.7, 3 and 4.2, https://arxiv.org/html/2401.09415v3.
2. R. Bollapragada, T. Chen, R. Ward, *On the fast convergence of minibatch heavy ball momentum*, arXiv:2206.07553v1 (15 June 2022), https://arxiv.org/html/2206.07553v5.
3. T. Strohmer, R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, Journal of Fourier Analysis and Applications 15 (2009), 262–278 (classical \(M=0\) result cited in reference 1).
