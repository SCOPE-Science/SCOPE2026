# Exact Ptolemy and Euclidean distortion of the cross-exponent \(Z_{1,\infty}\) family
## Finding
For every real \(\lambda>0\), let \(Z_{1,\infty}^{(\lambda)}\) be \(\mathbb R^2\) with
\[
N_\lambda(x,y)=\left(\|(x,y)\|_1^2+\lambda\|(x,y)\|_\infty^2\right)^{1/2}.
\]
Put
\[
M_\lambda=\frac{\lambda+2+\sqrt{\lambda^2+4}}2,
\qquad
m_\lambda=
\begin{cases}
1+\lambda,&0<\lambda\le2,\\
(\lambda+4)/2,&\lambda\ge2.
\end{cases}
\]
Then
\[
C_{\mathrm{Pt}}\!\left(Z_{1,\infty}^{(\lambda)}\right)
=
d_{\mathrm{BM}}\!\left(Z_{1,\infty}^{(\lambda)},\ell_2^2\right)^2
=
\frac{M_\lambda}{m_\lambda}.
\]
Equivalently,
\[
C_{\mathrm{Pt}}\!\left(Z_{1,\infty}^{(\lambda)}\right)
=
\begin{cases}
\dfrac{\lambda+2+\sqrt{\lambda^2+4}}{2(1+\lambda)},&0<\lambda\le2,\\[2mm]
\dfrac{\lambda+2+\sqrt{\lambda^2+4}}{\lambda+4},&\lambda\ge2.
\end{cases}
\]
This is exactly the published Jordan--von Neumann constant of the same family, so
\[
C_{\mathrm{Pt}}\!\left(Z_{1,\infty}^{(\lambda)}\right)
=
d_{\mathrm{BM}}\!\left(Z_{1,\infty}^{(\lambda)},\ell_2^2\right)^2
=
C_{\mathrm{NJ}}\!\left(Z_{1,\infty}^{(\lambda)}\right)
\qquad(\lambda>0).
\]

The phase transition at \(\lambda=2\) is geometric: below it the least Euclidean comparison occurs on the coordinate axes, while above it the least comparison occurs on the diagonals. The sharp direction is always the unique interior direction
\[
t_\lambda=\frac{\sqrt{\lambda^2+4}-\lambda}{2}\in(0,1),
\]
which solves \(t_\lambda^2+\lambda t_\lambda=1\).

## Assumptions and scope
All scalars are real and the dimension is exactly two. The norm is
\[
N_\lambda(x,y)=\left((|x|+|y|)^2+\lambda\max\{|x|,|y|\}^2\right)^{1/2},
\qquad \lambda>0.
\]
The Ptolemy constant is
\[
C_{\mathrm{Pt}}(X)=
\sup
\frac{\|x-y\|\,\|z\|}
{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|},
\]
where the supremum is over nonzero pairwise distinct \(x,y,z\in X\). The Euclidean Banach--Mazur distance is the infimum of \(\|T\|\,\|T^{-1}\|\) over linear isomorphisms from the plane onto \(\ell_2^2\).

The theorem concerns the cross-exponent endpoint \(p=1\), \(q=\infty\) of the mixed family
\[
\left(\|\cdot\|_p^2+\lambda\|\cdot\|_q^2\right)^{1/2}.
\]
No formula is asserted here for general \(1<p<2<q<\infty\).

## Proof
Because \(N_\lambda\) is invariant under coordinate sign changes and coordinate interchange, every nonzero direction is equivalent to \((1,t)\) with \(0\le t\le1\). Relative to the Euclidean norm \(E(x,y)=\sqrt{x^2+y^2}\), put
\[
Q_\lambda(t)
=
\frac{N_\lambda(1,t)^2}{E(1,t)^2}
=
\frac{\lambda+(1+t)^2}{1+t^2}.
\]
Differentiation gives
\[
Q_\lambda'(t)
=
\frac{2(1-\lambda t-t^2)}{(1+t^2)^2}.
\]
Hence \(Q_\lambda\) increases up to the unique point
\[
t_\lambda=\frac{\sqrt{\lambda^2+4}-\lambda}{2}
\]
and decreases afterwards. The maximum is therefore
\[
M_\lambda=Q_\lambda(t_\lambda)
=
\frac{\lambda+2+\sqrt{\lambda^2+4}}2.
\]
The minimum is one of the endpoint values
\[
Q_\lambda(0)=1+\lambda,
\qquad
Q_\lambda(1)=2+\frac\lambda2.
\]
Thus
\[
m_\lambda=
\begin{cases}
1+\lambda,&0<\lambda\le2,\\
(\lambda+4)/2,&\lambda\ge2.
\end{cases}
\]
Consequently
\[
\sqrt{m_\lambda}\,E(w)
\le
N_\lambda(w)
\le
\sqrt{M_\lambda}\,E(w)
\qquad(w\in\mathbb R^2).
\]
Euclidean Ptolemy now gives
\[
C_{\mathrm{Pt}}\!\left(Z_{1,\infty}^{(\lambda)}\right)
\le
\frac{M_\lambda}{m_\lambda}.
\]

The comparison is also Banach--Mazur optimal. Indeed, let \(H_Q(w)^2=Q(w)\) be any positive-definite quadratic pullback satisfying
\[
aN_\lambda(w)^2\le Q(w)\le bN_\lambda(w)^2.
\]
Average \(Q\) over the signed-permutation isometry group of \(N_\lambda\). The averaged quadratic form satisfies the same inequalities and is invariant under both coordinate sign changes and interchange. Hence it is a positive scalar multiple of \(x^2+y^2\). Therefore no ellipse has smaller squared distortion than the Euclidean comparison above, and
\[
d_{\mathrm{BM}}\!\left(Z_{1,\infty}^{(\lambda)},\ell_2^2\right)^2
=
\frac{M_\lambda}{m_\lambda}.
\]

It remains to attain the Ptolemy upper bound. First suppose \(0<\lambda\le2\) and write \(t=t_\lambda\). Take
\[
x=(1,0),
\qquad
y=(0,t),
\qquad
z=x+y=(1,t).
\]
The axis directions realize the minimum comparison, while both \(x+y\) and \(x-y\) realize the maximum. Hence
\[
N_\lambda(x)^2=m_\lambda,
\qquad
N_\lambda(y)^2=m_\lambda t^2,
\]
and
\[
N_\lambda(x+y)^2
=
N_\lambda(x-y)^2
=
M_\lambda(1+t^2).
\]
Since \(x-z=-y\) and \(z-y=x\), the Ptolemy ratio is exactly
\[
\frac{M_\lambda(1+t^2)}{m_\lambda(1+t^2)}
=
\frac{M_\lambda}{m_\lambda}.
\]

Now suppose \(\lambda>2\), again writing \(t=t_\lambda\), and take
\[
x=(1+t,1+t),
\qquad
y=(1-t,-(1-t)),
\qquad
z=x+y=(2,2t).
\]
The two vectors \(x\) and \(y\) lie on diagonal minimum directions, whereas
\[
x+y=(2,2t),
\qquad
x-y=(2t,2)
\]
lie on the two symmetric maximum directions. Therefore
\[
N_\lambda(x-y)N_\lambda(z)=4M_\lambda(1+t^2),
\]
while
\[
N_\lambda(x-z)N_\lambda(y)+N_\lambda(z-y)N_\lambda(x)
=
N_\lambda(y)^2+N_\lambda(x)^2
=
4m_\lambda(1+t^2).
\]
The ratio is again \(M_\lambda/m_\lambda\). This proves the Ptolemy formula in both regimes.

Yang's published endpoint formula for \(C_{\mathrm{NJ}}(Z_{1,\infty})\) is precisely the same two-branch expression, which yields the final three-way equality.

## Verification
The directional reduction is exhaustive because the norm has the full signed-permutation symmetry of the square. The derivative of \(Q_\lambda\) has exactly one zero on \((0,1)\), since \(1-\lambda t-t^2\) is strictly decreasing there. The global minimum is therefore necessarily one of the two endpoints, and their ordering changes exactly at \(\lambda=2\).

The Banach--Mazur lower bound does not assume that an optimal ellipse is Euclidean: arbitrary positive-definite quadratic forms are first averaged over actual isometries of the norm, and the resulting invariant form must be scalar Euclidean.

Both Ptolemy witnesses are exact symbolic configurations. At \(\lambda=2\), the first witness applies and the two minimum directions tie. No finite sampling or numerical optimization is used as proof.

## Relationship to prior work
Yang's 2015 paper computes the Jordan--von Neumann constant of the mixed \(Z_{p,q}\) family in the cross-exponent regime. Its Theorem 2.2 gives, in particular,
\[
C_{\mathrm{NJ}}(Z_{1,\infty})
=
\begin{cases}
\dfrac{\lambda+2+\sqrt{\lambda^2+4}}{2(1+\lambda)},&0<\lambda\le2,\\[2mm]
\dfrac{\lambda+2+\sqrt{\lambda^2+4}}{\lambda+4},&\lambda\ge2.
\end{cases}
\]
That result concerns a two-point parallelogram invariant and does not supply either the Ptolemy lower-bound triples or the affine optimality statement proved here.

Zuo's 2012 paper develops exact Ptolemy criteria for planar absolute normalized norms, chiefly through midpoint extremality relative to Euclidean comparison. The present cross-exponent family has its sharp comparison at the off-midpoint direction \(t_\lambda\), so those midpoint formulas do not produce the result.

Most decisively, Zuo's 2018 full-text treatment studies means of \(\ell_p\) and \(\ell_q\) norms and states after its weighted-mean example that the exact Ptolemy constants for the cross regime
\[
1\le p<2<q\le\infty
\]
remain undiscovered. The family here is the endpoint \(p=1\), \(q=\infty\), with mean exponent \(2\). The 2018 general comparison theorems do not imply this endpoint because the normalized comparison is off-midpoint; for \(\lambda>2\) it also crosses the Euclidean comparison rather than lying globally on one side.

A separate exact Euclidean-distortion result for mixed \(\ell_p\)-\(\ell_q\) planes covers the two same-side regimes \(1\le p\le q\le2\) and \(2\le p\le q\le\infty\), not the cross-exponent endpoint treated here.

## Limitations
The theorem resolves only the endpoint \(p=1\), \(q=\infty\) of the cross-exponent mixed family. The general region \(1<p<2<q<\infty\) is not classified.

The literature comparison is bounded by the inspected primary sources and targeted searches. A later or differently named calculation of this endpoint may exist outside the checked indexes, although no such statement was located.

## References
1. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2012, Article 107, DOI 10.1186/1029-242X-2012-107; published 2012-05-17.
2. C. Yang, “A note on Jordan--von Neumann constant for \(Z_{p,q}\) space,” *Journal of Mathematical Inequalities* 9 (2015), 499--504, DOI 10.7153/jmi-09-44.
3. Z.-F. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” *Mathematical Inequalities & Applications* 21 (2018), 945--956, DOI 10.7153/mia-2018-21-64.
