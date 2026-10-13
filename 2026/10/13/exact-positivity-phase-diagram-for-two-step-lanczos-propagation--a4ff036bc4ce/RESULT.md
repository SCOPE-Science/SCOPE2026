# Exact positivity phase diagram for two-step Lanczos propagation on two reversible Markov links

## Finding
A symmetric continuous-time Markov generator can have an exactly stochastic and positive exponential semigroup while its ordinary two-step Lanczos approximation produces a negative probability. The failure has an exact phase diagram on the natural model consisting of two independent reversible two-state links with different rates.

For a rate contrast \(R>1\), put
\[
G_R=\begin{pmatrix}
-1&1&0&0\\1&-1&0&0\\0&0&-R&R\\0&0&R&-R
\end{pmatrix},
\qquad
\pi_0=\frac{(1,0,\varepsilon,0)^{\mathsf T}}{1+\varepsilon},
\quad \varepsilon>0.
\]
The slow link initially carries mass \(1/(1+\varepsilon)\); the fast link carries the remaining \(\varepsilon/(1+\varepsilon)\). The exact semigroup \(e^{tG_R}\) is stochastic and entrywise nonnegative for every \(t\ge0\).

Let \(Q_2\) be the two-column orthonormal Lanczos basis generated from \(\pi_0\) and \(G_R\pi_0\), and define
\[
y_2(t)=Q_2\exp(tQ_2^{\mathsf T}G_RQ_2)Q_2^{\mathsf T}\pi_0.
\]
Write \(u=\varepsilon^2\) and set
\[
P_R(u)=R^3u^2+2R(R^2-2R+2)u+2-R.
\]
Then the exact all-time positivity classification is
\[
\boxed{
y_2(t)\ge0\ \text{for every }t\ge0
\iff P_R(\varepsilon^2)\ge0.
}
\]
The first, second, and fourth computed components are strictly positive for every \(t>0\), so the classification concerns only the probability assigned to the initially rare fast-link state.

For \(1<R\le2\), positivity holds for all rare-block masses. For every \(R>2\), the polynomial \(P_R\) has exactly one positive root \(u_*(R)\). At and above \(u_*(R)\), the Lanczos approximation stays nonnegative at all times. Below it, the fast state becomes exactly zero at one finite time \(t_*\), then strictly negative for every later time.

If \(\lambda_-<\lambda_+<0\) denote the two Ritz values of the projected generator, the unique crossing time in the negative regime is
\[
\boxed{
t_*=
\frac{\log\big((R+\lambda_+)/(R+\lambda_-)\big)}
{\lambda_+-\lambda_-}.
}
\]
For every fixed \(R>2\), as \(\varepsilon\downarrow0\), this tends to
\[
\boxed{\frac12\log\left(\frac R{R-2}\right).}
\]
An arbitrarily small but nonzero probability assigned to a sufficiently fast link can therefore make low-order Lanczos propagation negative at a time bounded away from infinity.

A rational witness is \(R=4\), \(\varepsilon=1/8\). The exact threshold is
\[
u_*(4)=\frac{3\sqrt3-5}{8},
\]
and
\[
P_4(1/64)=-47/64<0.
\]
The third computed component is provably negative already at \(t=1\).

## Assumptions and scope
The setting is exact arithmetic, the standard nonrestarted two-dimensional Krylov projection, and the real symmetric generator displayed above. The generator is reducible because the two links are independent; the theorem is not a universal classification of all four-state or all reversible Markov generators.

The initial distribution is normalized by \(1+\varepsilon\) and has two zero components. The starting vector has support in both links for every \(\varepsilon>0\). Both Ritz values are then strictly negative, despite the full generator having a two-dimensional zero eigenspace. The limiting case \(\varepsilon=0\) is different: Krylov propagation is exact on the single active two-state block.

The approximation considered is exactly
\[
Q_2\exp(tQ_2^{\mathsf T}G_RQ_2)Q_2^{\mathsf T}\pi_0,
\]
not a polynomial Taylor truncation and not a stochasticity-corrected Krylov scheme. By symmetry, Arnoldi and Lanczos give the same approximation.

## Proof
Scale away the positive normalization and put
\[
z=(1,0,\varepsilon,0)^{\mathsf T},
\qquad
Z=[z,G_Rz].
\]
As \(R>1\) and \(\varepsilon>0\), these columns are independent. The two Ritz eigenvalues are those of the restriction of \(G_R\) to \(\operatorname{ran} Z\), so they are the generalized eigenvalues of
\[
H=Z^{\mathsf T}G_RZ,
\qquad
M=Z^{\mathsf T}Z.
\]
The original generator is symmetric and negative semidefinite. Its kernel consists of vectors constant on each link. An element \(\alpha z+\beta G_Rz\) is constant on the first link only if \(\alpha=2\beta\), and on the second link only if \(\alpha=2R\beta\). Since \(R>1\), the only possibility is the zero vector. Thus the restricted generator is negative definite and its Ritz values obey
\[
\lambda_-<\lambda_+<0.
\]
There are two distinct values because the second Lanczos off-diagonal coefficient is positive.

The standard Arnoldi/Lanczos polynomial-interpolation identity gives
\[
y_2(t)=\frac1{1+\varepsilon}p_t(G_R)z,
\]
where \(p_t\) is the unique affine polynomial satisfying
\[
p_t(\lambda_-)=e^{t\lambda_-},
\qquad p_t(\lambda_+)=e^{t\lambda_+}.
\]
Explicitly,
\[
p_t(s)=
\frac{(\lambda_+-s)e^{t\lambda_-}+(s-\lambda_-)e^{t\lambda_+}}
{\lambda_+-\lambda_-}.
\]
For \(t>0\) its slope \(c_t\) is strictly positive:
\[
c_t=\frac{e^{t\lambda_+}-e^{t\lambda_-}}{\lambda_+-\lambda_-}>0.
\]
Using
\[
G_Rz=(-1,1,-R\varepsilon,R\varepsilon)^{\mathsf T},
\]
one obtains the exact components
\[
(1+\varepsilon)y_2(t)=
\big(p_t(-1),\ c_t,\ \varepsilon p_t(-R),\ R\varepsilon c_t\big)^{\mathsf T}.
\]
The Rayleigh quotient of \(G_R\) at \(z\) is
\[
-\frac{1+R\varepsilon^2}{1+\varepsilon^2}<-1.
\]
Hence \(\lambda_-\) is even smaller, and \(-1>\lambda_-\). As \(p_t\) is increasing with positive value at \(\lambda_-\), \(p_t(-1)>0\). The second and fourth components are also positive. Only \(p_t(-R)\) can change sign.

The Rayleigh quotient at \(z\) is also strictly greater than \(-R\), so \(\lambda_+>-R\). If \(\lambda_-\le-R\), then \(p_t(-R)>0\) for every time because \(-R\) lies to the right of the lower Ritz node. If \(\lambda_->-R\), evaluating the interpolating line to the left of both Ritz nodes gives
\[
p_t(-R)=
\frac{(R+\lambda_+)e^{t\lambda_-}-(R+\lambda_-)e^{t\lambda_+}}
{\lambda_+-\lambda_-}.
\]
Both \(R+\lambda_+\) and \(R+\lambda_-\) are positive, and their ratio exceeds one. Therefore this expression changes sign exactly once at the stated \(t_*\), being positive before and negative afterwards.

It remains to classify when \(\lambda_->-R\). This holds precisely when \(G_R+RI\) is positive definite on \(\operatorname{ran}Z\), equivalently when \(H+RM\) is positive definite. Direct multiplication gives its first leading principal minor
\[
z^{\mathsf T}(G_R+RI)z=R-1>0
\]
and its determinant
\[
\boxed{
\det(H+RM)=-R\,P_R(\varepsilon^2).
}
\]
Sylvester's criterion therefore yields
\[
\lambda_->-R \iff P_R(\varepsilon^2)<0.
\]
The coefficient of \(u\) in \(P_R(u)\) is strictly positive for \(R>1\), since
\[
R^2-2R+2=(R-1)^2+1>0.
\]
Its leading coefficient is positive. When \(1<R\le2\), the constant term is nonnegative, so \(P_R(u)>0\) for all \(u>0\). When \(R>2\), its constant term is negative, and monotonicity in \(u\ge0\) gives exactly one positive zero and the asserted sign phases.

As \(\varepsilon\to0^+\), the Krylov space tends to the first link's two-dimensional invariant subspace. Its Ritz values tend to \(-2\) and \(0\). Substituting these limits into the crossing-time expression gives
\[
\lim_{\varepsilon\downarrow0}t_*=
\frac12\log\frac R{R-2}.
\]
There is no assertion of sign loss at \(\varepsilon=0\) itself: there the fast-block mass is exactly zero.

Finally, the row-sum property \({\boldsymbol 1}^{\mathsf T}G_R=0\) gives
\[
\sum_{i=1}^4(y_2(t))_i=p_t(0).
\]
For \(t>0\), strict convexity of \(s\mapsto e^{ts}\) and both negative Ritz nodes imply \(p_t(0)<e^0=1\); positivity of \(p_t(0)\) follows from its positive slope and \(0>\lambda_+\). Thus \(0<p_t(0)<1\). Positive scalar renormalization restores the mass but cannot change the sign of a negative component.

## Verification
The included `verify.py` uses only Python's standard library and exact rational arithmetic to verify the Gram and projected matrices, the determinant identity on several rational rate/mass pairs, and the exact witness
\[
R=4,\qquad \varepsilon=1/8.
\]
For that witness,
\[
M=\begin{pmatrix}65/64&-17/16\\-17/16&5/2\end{pmatrix},
\quad
H=\begin{pmatrix}-17/16&5/2\\5/2&-8\end{pmatrix},
\]
and
\[
\det(H-sM)=\frac{361s^2+1400s+576}{256}.
\]
The exact Ritz roots are
\[
\lambda_\pm=\frac{-700\pm68\sqrt{61}}{361}.
\]
The checker proves \(\lambda_->-7/2\), \(\lambda_+<0\), and \(\lambda_+-\lambda_->29/10\) by rational bounds \(39/5<\sqrt{61}<8\). Consequently,
\[
\frac{4+\lambda_+}{4+\lambda_-}<8,
\quad
e^{\lambda_+-\lambda_-}>1+\frac{29}{10}+\frac12\left(\frac{29}{10}\right)^2>8.
\]
The crossing inequality is therefore strict already at \(t=1\), proving \((y_2(1))_3<0\) without relying on a floating-point sign.

The checker is corroboration of the exact algebraic witness; the general phase diagram is proved symbolically above. The exact semigroup remains stochastic because \(G_R\) is a symmetric Markov generator with nonnegative off-diagonals and zero row sums.

## Relationship to prior work
The Ritz-interpolation identity and the standard Krylov approximation \(Q_m e^{tQ_m^{\mathsf T}GQ_m}Q_m^{\mathsf T}v\) are classical. Saad's original full paper develops the method and proves the interpolation formulation and error estimates. Frommer, Güttel, and Schweitzer present the same Arnoldi-polynomial characterization and a quadrature-based restarting framework in their publicly archived 2013 preprint. Neither inspected full text develops positivity or mass conservation for Markov-generator propagation, much less the present rate/mass/time phase diagram.

Classical uniformization and the theory of Metzler generators ensure that the exact exponential semigroup is stochastic and nonnegative. Those statements are about \(e^{tG}\), not about the nonorthogonal rowwise coefficients of a projected Krylov exponential approximation.

A previously recorded sharp spectral-width condition for two-step Lanczos positivity on diagonal positive matrices bounds universal safety when the product of elapsed time and spectral width is small. That theorem controls arbitrary positive diagonal data at a fixed time; it does not classify this fixed stochastic generator, where unconditional positivity persists for every \(t\) when \(1<R\le2\) and an exact mass-dependent late-time transition occurs above that threshold.

The new claim is the complete three-parameter sign law on two reversible Markov links, including an exact radical mass threshold, the unique first-negative time, and the rare-state limit. Search for equivalent Markov-chain, Krylov exponential, mass-defect, negative-component, rate-contrast, and interpolation formulations did not locate a statement implying this classification.

## Limitations
The model deliberately has two independent communicating classes. Neither an irreducible-chain threshold nor a claim of minimum state dimension is asserted.

The theorem concerns the ordinary two-step Lanczos/Arnoldi Galerkin approximation. It does not evaluate Krylov restarting, positivity-preserving exponential integrators, uniformization approximations, modified projection bases, or rounding-error corrections.

The exact positivity threshold is for the specified initial mass allocation and link-rate family. It does not supply a universal criterion for all symmetric Markov generators or all nonnegative initial vectors.

The negative rare component tends to zero in absolute magnitude with the rare initial mass. This is nevertheless decisive for the probability constraint and can persist as a relative sign failure for the rare state.

## References
1. Y. Saad, “Analysis of Some Krylov Subspace Approximations to the Matrix Exponential Operator,” SIAM Journal on Numerical Analysis 29 (1992), 209–228, DOI 10.1137/0729014. Author-hosted full preprint at `https://www-users.cse.umn.edu/~saad/PDF/RIACS-90-ExpTh.pdf`.
2. A. Frommer, S. Güttel, and M. Schweitzer, “Efficient and Stable Arnoldi Restarts for Matrix Functions Based on Quadrature,” MIMS EPrint 2013.48, publicly deposited 2013-08-28, revised 2014; SIAM Journal on Matrix Analysis and Applications 35 (2014), 661–683, DOI 10.1137/13093491X.
3. M. Hochbruck and C. Lubich, “On Krylov Subspace Approximations to the Matrix Exponential Operator,” SIAM Journal on Numerical Analysis 34 (1997), 1911–1925, DOI 10.1137/S0036142995280572.
