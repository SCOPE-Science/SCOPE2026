# Sharp complex-sector law for sketched Hermitian Ritz values

## Finding

Let \(A\in\mathbb C^{n\times n}\) be Hermitian positive definite with \(\mu I\preceq A\preceq LI\), where \(0<\mu\le L\), and put \(\kappa=L/\mu\). Let \(B\in\mathbb C^{n\times m}\) have full column rank. Suppose \(S\in\mathbb C^{s\times n}\) is an \(\varepsilon\)-squared-norm subspace embedding on \(\mathcal U=\operatorname{range}([B,AB])\), meaning

\[
(1-\varepsilon)\|v\|_2^2\le\|Sv\|_2^2\le(1+\varepsilon)\|v\|_2^2
\quad(v\in\mathcal U),\qquad 0\le\varepsilon<1.
\]

Define the ordinary sketched Rayleigh--Ritz matrix

\[
M=(SB)^\dagger(SAB)=(B^*S^*SB)^{-1}B^*S^*SAB.
\]

If \(\varepsilon<\tau_\kappa:=2\sqrt\kappa/(\kappa+1)\), then **every eigenvalue** \(\lambda\) of \(M\) obeys the sharp uniform sector law

\[
\boxed{\ |\arg\lambda|\le\Theta(\kappa,\varepsilon):=
\arcsin\!\left(\frac{\varepsilon(\kappa-1)}{2\sqrt\kappa\sqrt{1-\varepsilon^2}}\right)<\frac\pi2.\ }
\]

The constant is attained for each \(\kappa>1\) and \(0<\varepsilon<\tau_\kappa\) by a two-mode Hermitian system and a single trial vector with a complex sketch. It can also be attained with a dimension-reducing sketch \(S\in\mathbb C^{2\times3}\). The boundary is exact: for every \(\kappa>1\), at \(\varepsilon=\tau_\kappa\) a valid sketch can produce \(\lambda=0\), and at every \(\tau_\kappa<\varepsilon<1\) a valid sketch can produce a negative real Ritz value. When \(\kappa=1\), all sketched Ritz values equal \(\mu\) for every \(\varepsilon<1\).

In particular, when \(\kappa=9\) and \(\varepsilon=1/5\), the largest possible absolute argument is exactly \(\arctan(\sqrt2/5)\). Thus the formula controls *how nonreal* a sketched Ritz value may become, rather than merely its real-part sign.

## Assumptions and scope

All matrix products and inequalities are in exact complex arithmetic. The sketch need only preserve norms on \(\mathcal U\), not globally. The eigenspaces of \(M\) may be defective; the assertion applies to every algebraic eigenvalue because each admits an eigenvector. No probability distribution for \(S\) is assumed. Full column rank of \(SB\) follows from the embedding and \(\varepsilon<1\). The argument is the principal complex argument, well-defined below the strict threshold because the entire sector lies in the open right half-plane. For the boundary witnesses, \(\lambda=0\) is interpreted as failure of strict positive-real location, not assigned an argument.

The equality construction permits complex sketches. The upper bound also holds for real matrices and sketches, but sharpness within an exclusively real one-vector subclass is not asserted.

## Proof

**Step 1: every Ritz eigenvalue is a sketched quadratic-form quotient.** Take an eigenpair \(My=\lambda y\) with \(y\ne0\), and set \(u=By/\|By\|_2\). Write \(T=S^*S\). Since \(B^*TB\succ0\), the eigenvalue equation gives

\[
\lambda=\frac{u^*TAu}{u^*Tu},\qquad u^*Tu>0.
\]

Consequently, \(\arg\lambda=\arg(u^*TAu)\). Put \(a=u^*Au\in[\mu,L]\) and \(b=(\|Au\|_2^2-a^2)^{1/2}\ge0\). If \(b=0\), then \(Au=au\) and the quotient is the positive real number \(a\). Suppose \(b>0\) and choose \(v=(Au-au)/b\), so that \(u,v\) are orthonormal and \(Au=au+bv\).

**Step 2: an exact complex ellipse of permitted numerators.** On \(\operatorname{span}\{u,v\}\subseteq\mathcal U\), the embedding condition is exactly the operator inequality \(-\varepsilon I\preceq H\preceq\varepsilon I\) for the Hermitian compression of \(T-I\). Thus

\[
z:=u^*TAu=a+a h_{11}+b h_{12},\qquad H=(h_{ij})_{i,j=1}^{2}=H^*,\quad\|H\|_2\le\varepsilon.
\]

For any \(\phi\in\mathbb R\), the exact support function of \(w=a h_{11}+b h_{12}\) is

\[
\max_{\|H\|_2\le\varepsilon}\operatorname{Re}(e^{-i\phi}w)
=\varepsilon\left\|\begin{pmatrix}
 a\cos\phi&\tfrac b2 e^{i\phi}\\
 \tfrac b2 e^{-i\phi}&0
\end{pmatrix}\right\|_*
=\varepsilon\sqrt{a^2\cos^2\phi+b^2}.
\]

Here \(\|\cdot\|_*\) denotes the nuclear norm. Both eigenvalues of the displayed Hermitian matrix have opposite signs because \(b>0\); their absolute values sum to \(\sqrt{a^2\cos^2\phi+b^2}\). The maximizing \(H\) is the signed spectral projector difference scaled by \(\varepsilon\), so equality is realized, not merely bounded. The set of all such \(w\) is compact and convex, and its support function identifies precisely the filled ellipse centered at zero with horizontal semiaxis \(\varepsilon\sqrt{a^2+b^2}\) and vertical semiaxis \(\varepsilon b\). The possible values of \(z\) form that ellipse translated right by \(a\).

If \(\varepsilon\|Au\|_2< a\), the origin lies strictly left of the ellipse. The supporting tangent lines from the origin yield the **exact** largest angle

\[
\theta(a,b,\varepsilon)
=\arcsin\!\left(\frac{\varepsilon b}{a\sqrt{1-\varepsilon^2}}\right).
\]

For completeness, the upper-sector line \(\operatorname{Im}z\cos\theta-\operatorname{Re}z\sin\theta=0\) supports this ellipse exactly when

\[
-a\sin\theta+\varepsilon\sqrt{a^2\sin^2\theta+b^2}=0,
\]

which, after squaring with both sides nonnegative, gives the displayed sine formula. Complex conjugation gives the lower-sector line. The relevant boundary points are attained by the Hermitian support-function maximizers. The condition \(\varepsilon\|Au\|_2<a\) is equivalent to the sine argument being less than one.

**Step 3: optimize over the positive spectrum.** The elementary positive-semidefinite polynomial inequality

\[
(A-\mu I)(LI-A)\succeq0
\]

implies \(A^2\preceq(\mu+L)A-\mu LI\). Hence, for unit \(u\),

\[
\frac{b^2}{a^2}=\frac{\|Au\|_2^2}{a^2}-1
\le\frac{\mu+L}{a}-\frac{\mu L}{a^2}-1
\le\frac{(L-\mu)^2}{4\mu L}.
\]

The final maximum over \(a\in[\mu,L]\) is attained at \(a=2\mu L/(\mu+L)\). Therefore \(b/a\le(\kappa-1)/(2\sqrt\kappa)\) and \(\|Au\|_2/a\le(\kappa+1)/(2\sqrt\kappa)\). For \(\varepsilon<\tau_\kappa\), Step 2 applies uniformly and yields the claimed sector.

**Step 4: optimality, with actual sketches.** Let \(\mu<L\), choose

\[
A_0=\operatorname{diag}(\mu,L),\qquad
u=\frac1{\sqrt{L+\mu}}\begin{pmatrix}\sqrt L\\\sqrt\mu\end{pmatrix}.
\]

Then \(a=2\mu L/(\mu+L)\) and \(b/a=(L-\mu)/(2\sqrt{\mu L})\), so Step 3 is an equality. Step 2 supplies a Hermitian \(2\times2\) matrix \(H\), with eigenvalues \(\pm\varepsilon\), at the upper ellipse tangent. Define \(T_0=I_2+H\succ0\) and \(S_0=T_0^{1/2}\). Thus \(S_0\) satisfies the embedding exactly at distortion \(\varepsilon\), and the one-dimensional projected eigenvalue has argument \(\Theta(\kappa,\varepsilon)\).

For a concrete algebraic equality case, take

\[
A_0=\begin{pmatrix}1&0\\0&9\end{pmatrix},\quad
u=\frac1{\sqrt{10}}\begin{pmatrix}3\\1\end{pmatrix},\quad
T_0=\begin{pmatrix}
1&\frac{-1+2\sqrt2\,i}{15}\\
\frac{-1-2\sqrt2\,i}{15}&1
\end{pmatrix}.
\]

The eigenvalues of \(T_0\) are \(4/5\) and \(6/5\), so \(S_0=T_0^{1/2}\) is a valid \(1/5\)-embedding on the entire plane. Direct calculation gives \(u^*T_0u=24/25\) and \(u^*T_0A_0u=8/5+(8\sqrt2/25)i\), whence

\[
\lambda=\frac{5+\sqrt2\,i}{3},\qquad
\arg\lambda=\arctan\!\left(\frac{\sqrt2}{5}\right)
=\arcsin\!\left(\frac{(1/5)(9-1)}{2\sqrt9\sqrt{1-1/25}}\right).
\]

The general two-mode equality construction also gives a dimension-reducing sketch: extend \(A_0\) by a third eigenvalue in \([\mu,L]\), append a zero to \(u\), and take \(S=[S_0\ \ 0]\in\mathbb C^{2\times3}\). The relevant \(\mathcal U\) remains two-dimensional, so the embedding and equality persist.

**Step 5: exact strict-positivity threshold.** Retain \(A_0,u\), but use the real positive-definite sketch Gram matrix

\[
T_\varepsilon=\begin{pmatrix}1&-\varepsilon\\-\varepsilon&1\end{pmatrix},
\qquad S_\varepsilon=T_\varepsilon^{1/2}.
\]

It has eigenvalues \(1\pm\varepsilon\). The one-dimensional Ritz value is

\[
\lambda_\varepsilon=
\frac{\frac{2\mu L}{\mu+L}-\varepsilon\sqrt{\mu L}}
{1-\frac{2\varepsilon\sqrt{\mu L}}{\mu+L}}.
\]

The denominator is strictly positive for every \(\varepsilon<1\). The numerator is zero precisely at \(\varepsilon=\tau_\kappa\) and is negative above it. This establishes the exact boundary, including the case where the embedding is genuinely dimension-reducing by the same three-dimensional extension. \(\square\)

## Verification

The supplied Python standard-library file `verify.py` checks the explicit \(\kappa=9\) equality witness through rational identities, the exact real zero/negative witnesses on the threshold, and 8,750 reproducible finite random complex-Hermitian sketch cases over seven condition numbers and five relative distortions. Invoke with `python3 verify.py`. Successful output is:

`VERIFY_OK exact_fraction_identities=6 sharp_complex_equality=1 sharp_threshold_witnesses=2 random_complex_embedding_cases=8750`

The finite tests are reproducibility aids only. The proof of the theorem is Steps 1--5; simulations are not invoked to justify infinitely many dimensions or sketch matrices.

## Relationship to prior work

Bergermann (2026) defines the ordinary sketched Rayleigh--Ritz problem in Section 2.4 and studies general subspace embeddings in Section 3. Nakatsukasa and Tropp (2021/2023) define the same sketched projection in Section 6.3 and note in Section 6.8 that Hermitian matrices can have nonreal sketched Ritz values; the inspected sections instead provide residual and stability comparisons. The present claim gives an explicit **best possible angular location bound** for positive-definite inputs under a squared-norm embedding assumption, including attainment and the sharp loss-of-positive-real-location threshold.

Gustafson's 1968 positive-operator-products paper develops classical antieigenvalue and accretivity criteria. Its Section 4 already addresses positivity of products of noncommuting positive operators, so such positivity criteria and the underlying Kantorovich-style quadratic inequality are not claimed as new. The present analysis specializes to the **non-Hermitian sketched Ritz pencil**, derives its exact complex numerator ellipse and sharp sector, and identifies its sketch-distortion parameter explicitly.

## Limitations

The assertion concerns eigenvalue sector location in exact arithmetic, not convergence or eigenvector accuracy of an entire Krylov iteration, probability under a particular sketch distribution, or finite-precision effects. The bound assumes a squared-norm embedding of the joint trial/image space; preserving the trial space alone does not suffice. The sharpness example uses complex sketches, although the inequality itself holds in the real case. Earlier matrix-angle literature could contain an equivalent reparameterized inequality; independent verification of novelty is not asserted. The strict threshold is specifically for positive-definite \(A\), and must not be transferred to indefinite or nonnormal matrices without further argument.

## References

1. Kai Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158v1 (first posted 2026-04-08), Sections 2.4, 3, and 5.3. https://arxiv.org/html/2604.07158v1
2. Yuji Nakatsukasa and Joel A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113v2 (original 2021), Sections 6.3, 6.6, and 6.8. https://arxiv.org/html/2111.00113v2
3. Karl Gustafson, *The angle of an operator and positive operator products*, Bulletin of the American Mathematical Society **74** (1968), 488--492, especially Sections 2, 4, and 5. DOI:10.1090/S0002-9904-1968-11974-3
