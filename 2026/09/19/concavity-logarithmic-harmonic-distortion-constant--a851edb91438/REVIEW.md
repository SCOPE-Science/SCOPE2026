# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The argument was checked against the exact formulas in Section 8 of Knežević--Mateljević, arXiv:2609.19609.

The source defines
\[
J(\tau)=\int_{\mathbb T}\sqrt{\cos^2t+\tau^2\sin^2t}\,dm(t)
\]
and establishes
\[
\beta=2J',\qquad
\alpha=2J-2\tau J',\qquad
Q=\frac{\alpha}{\beta}=\frac{J}{J'}-\tau,
\qquad
Q(\tau_K)=K,\qquad M_K=\alpha(\tau_K).
\]
Differentiating gives
\[
J''(\tau)=\int_{\mathbb T}
\frac{\sin^2t\cos^2t}{(\cos^2t+\tau^2\sin^2t)^{3/2}}\,dm>0,
\]
\[
Q'=-\frac{JJ''}{(J')^2}<0,\qquad
\alpha'=-2\tau J''.
\]
These identities imply
\[
M_K'=\frac{2\tau_K(J'(\tau_K))^2}{J(\tau_K)}
=\frac{\tau_KM_K}{K(K+\tau_K)}.
\]
For
\[
G(\tau)=2\tau(J')^2/J
\]
one obtains
\[
G'
=
\frac{2(J')^2}{J}\left(1-\frac{\tau J'}J\right)
+
\frac{4\tau J'J''}{J}>0,
\]
because
\[
J-\tau J'=\int_{\mathbb T}\frac{\cos^2t}{D_\tau(t)}\,dm>0.
\]
Since \(Q'<0\), this proves \(M''<0\) without an unproved sign step.

At \(\tau=1\), the source values \(J=1\), \(J'=1/2\), \(J''=1/8\) give \(Q'(1)=-1/2\), \(G'(1)=1/2\), hence \(M''(1^+)=-1\). This yields the stated second-order conformal-endpoint expansion.

For \(\tau\to0^+\), the complete elliptic-integral expansions were checked against DLMF §19.12. Substitution into the source formulas gives
\[
\alpha=\frac4\pi\left[1+\tau^2(3/4-L/2)+O(\tau^4L)\right],
\]
\[
\beta=\frac{4\tau}{\pi}\left[L-1+\tau^2(3L/4-1)+O(\tau^4L)\right],
\qquad L=\log(4/\tau).
\]
Thus
\[
Q(\tau)=\frac{1}{\tau y(\tau)}(1+O(\tau^2y(\tau))),
\qquad
y(\tau)=\log(4/(e\tau)).
\]
The lower real Lambert branch is the correct inverse because the relevant solution has \(Y_K\to\infty\). The relation
\[
Y_Ke^{-Y_K}=e/(4K)
\]
makes \(\tau_0=(KY_K)^{-1}\) satisfy \(y(\tau_0)=Y_K\). Since
\[
(\tau y(\tau))'=y(\tau)-1\asymp Y_K
\]
near \(\tau_0\), the stated relative error for \(\tau_K\) follows by the mean-value theorem. Substitution into \(\alpha\) gives the deficit expansion with the correct sign and scale.

The boundary \(L^2\) identity was checked directly. The normalized inner product with the two-valued limit equals
\[
\frac2\pi\int_0^{\pi/2}
\frac{\cos t}{\sqrt{\cos^2t+\tau^2\sin^2t}}\,dt
=
\frac2\pi\frac{\arccos\tau}{\sqrt{1-\tau^2}},
\]
so the exact squared distance and its \((K\log K)^{-1/2}\) consequence follow.

## Originality

**PASS, to the best of our knowledge.**

The closest source is Knežević--Mateljević, arXiv:2609.19609. Its full accessible text was inspected at Theorem 8.1, Corollaries 8.3, 8.5, and 8.6, and the surrounding endpoint discussion. It proves the exact extremal representation, uniqueness of \(\tau_K\), strict monotonicity of \(M_K\), the limit \(M_K\to4/\pi\), qualitative boundary convergence, and only the first-order expansion
\[
M_K=1+\tfrac12(K-1)+O((K-1)^2)
\]
at \(K\to1^+\). No strict-concavity statement, large-\(K\) rate, Lambert-\(W\) inversion, or quantitative boundary-degeneration rate was found there.

Exact and synonymous literature searches included combinations of: harmonic Schwarz lemma, pointwise distortion, \(M_K\), \(\tau_K\), strict concavity, \(4/\pi\), elliptic-integral extremals, Lambert \(W\), \(K^2\log K\), harmonic quasiconformal derivatives, and ellipse Fourier coefficients. No source stating the present conclusions was found.

Wegmann's 1993/1994 paper is the main older source plausibly adjacent to the elliptic formulas. The full article was not independently inspected. Bibliographic records identify it as an extremal/Fourier-coefficient paper for harmonic mappings into convex regions, and arXiv:2609.19609 explicitly states that its ellipse boundary family and the two first Fourier coefficients coincide with Wegmann's formula (55), while distinguishing the new constrained pointwise-distortion problem. Residual originality risk remains that an asymptotic consequence of those classical coefficient formulas was recorded elsewhere under different terminology, but no such record was found.

Li (2016) was inspected in accessible full text. It studies coefficient bounds for harmonic globally \(K\)-quasiconformal self-mappings of the disk and Heinz-type inequalities, not the sharp pointwise-at-the-origin distortion optimization defining \(M_K\). It does not cover the theorem above.

Current SCOPE records were searched by the source identifier, pointwise-distortion terminology, harmonic Schwarz terminology, Lambert-\(W\) terminology, and equivalent claim phrases, with no collision found. Because arXiv:2609.19609 is very recent, unindexed contemporaneous follow-up observations remain the principal residual risk.

## Value

**PASS.**

The source theorem determines the extremal constant implicitly but leaves its global shape and large-distortion approach to the endpoint unresolved quantitatively. Strict concavity supplies a new structural property and an exact derivative law. The Lambert-\(W\) inversion identifies a non-power boundary layer,
\[
\tau_K\sim(K\log K)^{-1},
\]
and converts the qualitative limit \(M_K\to4/\pi\) into the sharp first-order deficit
\[
4/\pi-M_K\sim2/(\pi K^2\log K).
\]
The exact \(L^2\) identity simultaneously quantifies degeneration of the extremizers themselves. These conclusions sharpen both endpoints of the newly determined constant without changing the underlying extremal theorem.
