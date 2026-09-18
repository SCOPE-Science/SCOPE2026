# Ordered-product spectral growth need not converge to the top Lyapunov exponent

## Result

Consider the ordered-product spectral rate introduced in Sornette, Saiprasad and Troude, *A New Route to Chaos through the Geometric Composition of Non-Normal Amplification* (arXiv:2609.18017v1):

\[
h_L=\frac1L\left\langle\log\rho\!\left(J_{n+L-1}\cdots J_n\right)\right\rangle.
\]

The paper states that, when the top Lyapunov exponent is non-degenerate, \(h_L\to\lambda_1\) and attributes this to alignment of the leading eigenvector of the product with the leading Oseledets direction at a rate controlled by \(\lambda_1-\lambda_2\). That implication is false in general, even for a smooth deterministic map with a period-four orbit and a simple top Lyapunov exponent.

Fix
\[
0<b<a,
\qquad
Q=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
D=\operatorname{diag}(e^a,e^b).
\]
For \(u=(u_1,u_2)\in\mathbb R^2\), write
\[
C(u)=\begin{pmatrix}u_1&-u_2\\u_2&u_1\end{pmatrix}.
\]
Define the smooth polynomial map \(F:\mathbb R^4\to\mathbb R^4\), with \((u,v)\in\mathbb R^2\times\mathbb R^2\), by
\[
F(u,v)=\left(Qu,\ C(Qu)D C(u)^\top v\right).
\]
The points
\[
(u_n,v_n)=(Q^n e_1,0),\qquad n\in\mathbb Z,
\]
form a period-four orbit. Along it,
\[
DF(u_n,0)=
\begin{pmatrix}
Q&0\\
0&J_n
\end{pmatrix},
\qquad
J_n=Q^{n+1}D Q^{-n}.
\]
The fiber products telescope exactly:
\[
P_n^{(L)}:=J_{n+L-1}\cdots J_n
=Q^{n+L}D^LQ^{-n}.
\]
Hence the singular values of the fiber product are \(e^{aL}\) and \(e^{bL}\), so the Lyapunov exponents of the full four-dimensional orbit are
\[
a,
\quad b,
\quad 0,
\quad 0.
\]
In particular the top exponent is simple and \(\lambda_1-\lambda_2=a-b>0\).

However, spectral-radius growth oscillates by parity. Since spectral radius is unchanged by conjugation,
\[
\rho(P_n^{(L)})=\rho(Q^L D^L).
\]
For even \(L\), \(Q^L=\pm I\), so
\[
\rho(P_n^{(L)})=e^{aL}.
\]
For odd \(L\), \(Q^L=\pm Q\), and, up to an overall sign,
\[
QD^L=
\begin{pmatrix}
0&-e^{bL}\\
e^{aL}&0
\end{pmatrix},
\]
whose eigenvalues are \(\pm i e^{(a+b)L/2}\). Thus
\[
\rho(P_n^{(L)})=e^{(a+b)L/2}.
\]
The value is independent of the starting phase \(n\), and the base block \(Q^L\) has spectral radius one, so for the full Jacobian cocycle
\[
\boxed{
 h_{2k}=a=\lambda_1,
 \qquad
 h_{2k+1}=\frac{a+b}{2}<\lambda_1.
}
\]
Therefore \(h_L\) does not converge although the top Lyapunov exponent is non-degenerate.

The same example also shows why the proposed eigenvector-alignment explanation fails. The leading covariant direction at phase \(n\) is \(Q^n e_1\), and
\[
P_n^{(L)}Q^ne_1=e^{aL}Q^{n+L}e_1.
\]
For odd \(L\), the output direction is orthogonal to the input direction, while the two eigenvalues of the dominant fiber block are non-real. Oseledets alignment controls singular/covariant growth between the initial and final tangent fibers; it does not force a finite-time propagator to acquire a dominant eigenvalue with the same exponential rate.

## A periodic transversality condition

The obstruction has a simple general form for a period-\(p\) cocycle. Let
\[
M_n=P_n^{(p)}
\]
be the monodromy matrix at phase \(n\), and suppose its dominant multiplier \(\mu_1\) is simple. Let \(v_n,w_n\) be corresponding right and left eigenvectors, with \(w_n^\top v_n\ne0\). For \(0\le r<p\), let
\[
A_{n,r}=J_{n+r-1}\cdots J_n,
\qquad A_{n,0}=I.
\]
For \(L=kp+r\), periodicity gives
\[
P_n^{(L)}=A_{n,r}M_n^k.
\]
If
\[
\boxed{
 c_{n,r}:=\frac{w_n^\top A_{n,r}v_n}{w_n^\top v_n}\ne0,
}
\]
then the rank-one dominant term in \(A_{n,r}M_n^k\) has nonzero eigenvalue \(\mu_1^k c_{n,r}\), and consequently
\[
\lim_{k\to\infty}\frac1{kp+r}\log\rho(P_n^{(kp+r)})
=\frac1p\log|\mu_1|=\lambda_1.
\]
Thus a spectral transversality condition, not merely a Lyapunov gap, is sufficient along each residue class. If \(c_{n,r}=0\), the dominant norm-growing rank-one term is spectrally nilpotent and the spectral radius may be controlled by smaller terms. In the example above this cancellation occurs for every odd residue and produces the persistent parity gap.

This criterion also explains the statement in the source paper that \(h_{kp}=\lambda_1\) exactly on a period-\(p\) orbit: the return product acts from a tangent space back to the same phase, so the relevant endpoint pairing is automatically nonzero for the dominant Floquet direction.

## Frame dependence

There is a related structural issue. Under a moving orthogonal frame \(R_n\), a finite propagator transforms as
\[
P_n^{(L)}\mapsto R_{n+L}^{-1}P_n^{(L)}R_n,
\]
which is not a similarity transform unless the endpoint frames agree. Its spectral radius is therefore not invariant under such a change of frame. Singular values are invariant under orthogonal endpoint frames.

For the counterexample, choosing the co-rotating frame \(R_n=Q^n\) converts every fiber step to the fixed diagonal map \(D\). In that frame the finite products are \(D^L\) and the spectral rate equals \(a\) for every \(L\); in the original frame the same cocycle has the parity oscillation above. Thus finite-horizon spectral-radius growth is not an intrinsic cocycle invariant away from return times.

## Consequences for arXiv:2609.18017v1

The counterexample does **not** invalidate the paper's numerical values of \(h_L\) for its particular Hénon and Ikeda trajectories. The paper itself reports that its measured \(h_{1024}\) values happen to be close to \(\lambda_1\), and it correctly notes that \(h_{kp}=\lambda_1\) for multiples of a periodic orbit's minimal period.

What fails is the unrestricted theoretical statement that a non-degenerate top exponent alone implies \(h_L\to\lambda_1\), together with the claimed eigenvector-alignment justification. Consequently, the comparison between a Lyapunov-gap alignment time and the empirically measured separation length \(L^*\) is not a general consequence of Oseledets theory. For the specific examples in the source it remains an empirical observation unless an additional non-cancellation hypothesis is established.

If asymptotic convergence to the top Lyapunov exponent is the desired property, the standard finite-time quantity is
\[
\Lambda_n^{(L)}=\frac1L\log\sigma_{\max}(P_n^{(L)}),
\]
whose asymptotic behavior is governed by multiplicative/subadditive ergodic theory under the usual integrability assumptions. The source paper already defines this singular-value quantity, but its spectral-radius diagnostic \(h_L\) is not interchangeable with it.

## Relation to prior literature

No broad claim of novelty is made for failure of spectral-radius convergence. Aoun and Sert proved a law of large numbers for spectral radius for i.i.d. random matrix products and also gave an ergodic stationary Markov example in which the normalized log spectral radius has distinct liminf and limsup. Martínez Ramos (2026) explicitly emphasizes that for general linear cocycles one has a limsup formula, while existence of a true spectral-radius limit requires additional hypotheses; his Theorem 1.1 proves convergence for strongly irreducible locally constant cocycles over a mixing subshift with a simple top exponent.

The contribution here is source-specific: an explicit smooth deterministic period-four counterexample to the unrestricted convergence statement in arXiv:2609.18017v1, together with the periodic endpoint-transversality mechanism and its frame-dependence interpretation.

## Reproducibility

`artifacts/verify_counterexample.py` evaluates the period-four matrices for \(a=2,b=1\), checks \(L=1,\dots,12\) from all four starting phases, and verifies to floating-point precision that the spectral rate alternates between \(3/2\) and \(2\) while the largest-singular-value rate remains \(2\). `artifacts/verification_output.txt` records the executed output.

## Limitations

The result is a correction to a general asymptotic claim about the diagnostic \(h_L\), not a refutation of the source paper's observed finite-\(L\) separation on its reported data sets or of its control experiments. The periodic transversality condition above is sufficient for convergence along residue classes; it is not asserted to be a necessary-and-sufficient characterization for arbitrary nonperiodic cocycles. The frame-dependence statement concerns finite-horizon spectral radius; Lyapunov exponents themselves remain invariant under bounded smooth changes of coordinates.

## References

1. D. Sornette, V. R. Saiprasad, V. Troude, *A New Route to Chaos through the Geometric Composition of Non-Normal Amplification*, arXiv:2609.18017v1 (2026). https://arxiv.org/abs/2609.18017
2. R. Aoun, C. Sert, *Law of large numbers for the spectral radius of random matrix products*, American Journal of Mathematics 143 (2021), 995–1010. https://arxiv.org/abs/1908.07469
3. N. Martínez Ramos, *Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles*, International Mathematics Research Notices 2026(5), rnag038 (2026). https://arxiv.org/abs/2507.19624
