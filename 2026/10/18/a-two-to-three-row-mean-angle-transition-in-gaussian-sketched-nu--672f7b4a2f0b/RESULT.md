# A two-to-three-row mean-angle transition in Gaussian sketched null-space extraction

## Finding

Let \(m\ge s\ge2\) be integers, let \(U\in\mathbb R^{m\times2}\) have orthonormal columns, and let
\[A_\varepsilon=U\operatorname{diag}(1,\varepsilon),\qquad 0<\varepsilon<1.\]
Draw \(S\in\mathbb R^{s\times m}\) with independent standard-normal entries. Let \(v_s(\varepsilon)\) be either unit right singular vector of \(SA_\varepsilon\) associated with its smallest singular value (almost surely simple), and define the expected squared principal-angle error
\[R_s(\varepsilon)=\mathbb E\bigl[1-|e_2^{\mathsf T}v_s(\varepsilon)|^2\bigr].\]
Then the three-row sketch has the **exact** risk law, for every \(0<\varepsilon<1\),
\[\boxed{R_3(\varepsilon)=\frac{\varepsilon^2}{1+\varepsilon^2}.}\]
The smallest full-column-rank sketch has a sharp logarithmic penalty, whereas every larger sketch has a finite quadratic constant:
\[\boxed{R_2(\varepsilon)=\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2),\qquad R_s(\varepsilon)=\frac{\varepsilon^2}{s-2}+o(\varepsilon^2)\quad(s\ge3\text{ fixed}).}\]
In particular, adding one row, from two to three, eliminates the logarithmic deterioration of the mean-square trailing-singular-vector angle. The formulas concern the squared sine of the *true* principal angle, not its small-angle linearization.

## Assumptions and scope

The sketch is a fresh real Gaussian left sketch, not a column sketch. The matrix has exactly two positive singular values \(1\) and \(\varepsilon\), with arbitrary fixed orthonormal left singular vectors and arbitrary ambient row dimension \(m\ge s\). The two right singular directions are the standard coordinate axes after a harmless orthogonal change of basis. The number of sketch rows \(s\) is fixed when \(\varepsilon\downarrow0\); the \(O(\varepsilon^2)\) constant in the two-row statement is absolute, while the higher-row \(o\)-term may depend on \(s\). No floating-point claim is made.

## Proof

**Gaussian reduction and exact angle kernel.** Rotational invariance shows that the two columns of \(SU\) are independent \(g_1,g_2\sim N(0,I_s)\). Write \(a=\|g_1\|^2\), \(c=\|g_2\|^2\), and \(t=g_1^{\mathsf T}g_2/\sqrt{ac}\). The sketched Gram matrix is
\[B_\varepsilon=\begin{pmatrix}a&\varepsilon\sqrt{ac}\,t\\ \varepsilon\sqrt{ac}\,t&\varepsilon^2c\end{pmatrix}.\]
The eigenprojector formula for any real symmetric \(2\times2\) matrix gives, outside a probability-zero repeated-eigenvalue event,
\[1-|e_2^{\mathsf T}v_s|^2=H\!\left(\frac a{\varepsilon^2c},t\right),\qquad H(x,t)=\frac12\left(1-\frac{x-1}{\sqrt{(x-1)^2+4xt^2}}\right).\tag{1}\]
The ratio \(r=a/c\) and direction cosine \(t\) are independent. With \(\alpha=s/2\), their laws are
\[f_s(r)=\frac{\Gamma(s)}{\Gamma(\alpha)^2}\frac{r^{\alpha-1}}{(1+r)^s},\quad r>0;\qquad t^2\sim\operatorname{Beta}\bigl(\tfrac12,\tfrac{s-1}{2}\bigr),\quad\mathbb Et^2=\frac1s.\tag{2}\]
Therefore the double integral of \(H(r/\varepsilon^2,t)\) against (2) is also an exact nonasymptotic expression for every \(R_s\).

**The exact three-row identity.** At \(s=3\), the \(2\times2\) Wishart density of \(B_\varepsilon\) is proportional to \(\exp[-\operatorname{tr}(\Sigma^{-1}B)/2]\), since the determinant exponent \((s-3)/2\) vanishes, where \(\Sigma=\operatorname{diag}(1,\varepsilon^2)\). Diagonalize \(B=Q_\theta\operatorname{diag}(\lambda_+,\lambda_-)Q_\theta^{\mathsf T}\), \(\lambda_+>\lambda_->0\), with \(Q_\theta\)'s first column \((\cos\theta,\sin\theta)^{\mathsf T}\). The eigenvalue Jacobian is proportional to \(\lambda_+-\lambda_-\). Writing \(u=\lambda_-\), \(v=\lambda_+-\lambda_-\), the eigenvalue integral factors as
\[\int_0^\infty e^{-(a_\theta+b_\theta)u/2}\,du\int_0^\infty v e^{-a_\theta v/2}\,dv=\frac8{(a_\theta+b_\theta)a_\theta^2},\]
where \(a_\theta=\cos^2\theta+\varepsilon^{-2}\sin^2\theta\) and \(b_\theta=\sin^2\theta+\varepsilon^{-2}\cos^2\theta\). Since \(a_\theta+b_\theta=1+\varepsilon^{-2}\), the top-eigenvector angle has density proportional to \(a_\theta^{-2}\). The bottom-vector squared sine error is \(\sin^2\theta\). Put \(k=\varepsilon^{-1}\) and \(z=\tan\theta\); integrals over any full period reduce to
\[I_0=\int_{\mathbb R}\frac{1+z^2}{(1+k^2z^2)^2}\,dz=\frac{\pi(k^2+1)}{2k^3},\qquad I_1=\int_{\mathbb R}\frac{z^2}{(1+k^2z^2)^2}\,dz=\frac{\pi}{2k^3}.\]
Thus \(R_3=I_1/I_0=1/(1+k^2)=\varepsilon^2/(1+\varepsilon^2)\) exactly.

**The critical two-row logarithm.** For \(s=2\), (2) simplifies to \(f_2(r)=(1+r)^{-2}\) and \(\mathbb Et^2=1/2\). Let \(h(x)=\mathbb E_tH(x,t)\). Formula (1) is between zero and one, and rationalization gives, uniformly over \(|t|\le1\) for \(x>2\),
\[H(x,t)=\frac{2xt^2}{\sqrt{(x-1)^2+4xt^2}\,[\sqrt{(x-1)^2+4xt^2}+x-1]}=\frac{t^2}{x}+O(x^{-2}).\]
Consequently \(h(x)=1/(2x)+O(x^{-2})\). Substituting \(r=\varepsilon^2x\) into (2),
\[R_2(\varepsilon)=\varepsilon^2\int_0^\infty\frac{h(x)}{(1+\varepsilon^2x)^2}\,dx=\frac{\varepsilon^2}{2}\int_2^\infty\frac{dx}{x(1+\varepsilon^2x)^2}+O(\varepsilon^2)\]
\[=\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).\]
The omitted \(x\le2\) integral and the integrated \(O(x^{-2})\) remainder are both uniformly bounded before multiplication by \(\varepsilon^2\).

**More than two rows.** When \(x\ge2\), rationalization bounds \(0\le H(x,t)\le4t^2/x\). In the small-ratio region \(r<2\varepsilon^2\), (2) gives probability \(O(\varepsilon^s)\), which is \(o(\varepsilon^2)\) for any fixed \(s>2\). Elsewhere \(\varepsilon^{-2}H(r/\varepsilon^2,t)\le4t^2/r\) and tends pointwise to \(t^2/r\). Dominated convergence applies because, by (2),
\[\mathbb E\frac{t^2}{r}=\frac1s\,\mathbb E\frac ca=\frac1s\cdot\frac{s}{s-2}=\frac1{s-2}.\]
This proves the remaining asymptotics, with no use of a finite experiment as a substitute for a limit argument.

## Verification

Run `python verify.py` after installing `requirements.txt`. The verifier independently constructs 1,500 Gaussian Gram eigenproblems, checks the angle identity, integrates the exact three-row Wishart angular density, and checks the beta-prime integral asymptotics for sample sketch sizes. These tests are finite sanity checks only. The analytic integral identities and dominated-convergence argument above establish the continuum and asymptotic claims.

## Relationship to prior work

Gilbert, Park, and Wakin (2012) introduced and analyzed sketched SVD singular-vector recovery with perturbation bounds. Nakatsukasa and Park (2022) analyze trailing right-singular-subspace recovery from left sketches using multiplicative perturbation bounds, explicitly motivating null-space and total-least-squares tasks. Neither of those inspected works states the exact expected squared angle in the three-row case or the two-row logarithmic mean-risk transition.

Takemura and Sheena (2002 manuscript; published 2005) prove a general **weak limiting distribution** of properly rescaled Wishart eigenvector coordinates under extreme population spectral separation. Their limiting random ratio underlies the leading-order intuition here. Weak convergence, however, neither provides the finite-\(\varepsilon\) three-row identity nor permits exchanging limits with expectation at two rows, where the putative limiting squared ratio is nonintegrable. The present moment-level calculation handles that critical boundary. Dong, Martinsson, and Nakatsukasa (2022) study canonical-angle bounds for leading subspace approximation by a different randomized-SVD construction; those bounds do not directly give this trailing-vector left-sketch risk law.

## Limitations

This is a two-singular-mode benchmark with independent real Gaussian sketches and an exact trailing SVD, not a bound for arbitrary spectra, non-Gaussian embeddings, or floating-point implementations. The result concerns mean squared principal angles, not a high-probability guarantee or almost-sure error. The expected-angle formula may be derivable from other classical Wishart eigenvector integrals not identified here; mathematical priority requires outside review. The earliest motivating public source date is the 2022 arXiv submission, not the date of a later revision.

## References

- A. Gilbert, J. Y. Park, and M. B. Wakin, *Sketched SVD: Recovering Spectral Features from Compressive Measurements*, arXiv:1211.0361 (2012), https://arxiv.org/abs/1211.0361.
- Y. Nakatsukasa and T. Park, *A Fast Randomized Algorithm for Computing an Approximate Null Space*, arXiv:2206.00975 (first public June 2, 2022), https://arxiv.org/abs/2206.00975.
- A. Takemura and Y. Sheena, *Distribution of Eigenvalues and Eigenvectors of Wishart Matrix When the Population Eigenvalues Are Infinitely Dispersed*, University of Tokyo METR02-13 (2002), https://www.keisu.t.u-tokyo.ac.jp/data/2002/METR02-13.pdf; journal version, *J. Multivariate Analysis* 94 (2005), 271–299.
- Y. Dong, P.-G. Martinsson, and Y. Nakatsukasa, *Efficient Bounds and Estimates for Canonical Angles in Randomized Subspace Approximations*, arXiv:2211.04676 (first public November 9, 2022), https://arxiv.org/abs/2211.04676.
