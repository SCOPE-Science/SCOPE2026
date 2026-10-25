# Sharp quadratic Hardy diagonal restriction: a cosine fixed point and a Hilbert-boundary slope

## Finding

The diagonal map \(DF(\zeta)=F(\zeta,\zeta)\) has an exact sharp norm on the entire homogeneous quadratic block of the bidisk Hardy space, for every \(1\le p<\infty\). Set
\[
\Phi_p(\lambda)=\frac{1}{2\pi}\int_0^{2\pi}|1-\lambda(1-\cos t)|^p\,dt.
\]
For every \(1\le p<\infty\), \(\Phi_p\) has a unique real minimizer \(\lambda_p\in(1/2,1)\), and the exact norm is
\[
K_p=\frac{1}{(p+1)^{1/p}\,\Phi_p(\lambda_p)^{1/p}}.
\]
A maximizer is \(F_p(z,w)=\lambda_p(z^2+w^2)/2+(1-\lambda_p)zw\), up to nonzero scalar multiplication. At the integrable endpoint \(p=1\), write \(\tau\in(0,\pi/2)\) for the unique root \(\cos\tau=\tau\). Then
\[
\lambda_1=\frac{1}{1+\sin\tau},\qquad K_1=\frac{\pi}{4\tau}=1.062662646156630\ldots.
\]
This strictly improves the homogeneous linear witness \(\pi/3=1.047197551\ldots\) for the norm of the unrestricted \(H^1\)-to-\(A^1\) diagonal map. At \(p=2\), \(K_2=1\), and the exact one-sided first-order law is
\[
K_p=1+\left(\frac7{12}-\frac12\log 3\right)(2-p)+o(2-p),\quad p\uparrow2.
\]

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and let normalized boundary and area measures be \(dt/(2\pi)\) and \(dA/\pi\), respectively. For \(1\le p<\infty\), consider exactly the three-dimensional complex vector space
\[
\mathcal H_2=\{F(z,w)=az^2+bzw+cw^2:a,b,c\in\mathbb C\}\subset H^p(\mathbb D^2).
\]
The norm \(K_p\) is the supremum over all nonzero members of this block; no statement about the unrestricted diagonal operator on the entire Hardy space is implicit. No positivity, symmetry, or reality is assumed for \(a,b,c\). The exponent range includes both endpoints \(p=1\) and \(p=2\) and all finite \(p>2\).

## Proof

**Step 1: exact norm reduction.** For \(F(z,w)=az^2+bzw+cw^2\), define \(P(\zeta)=a\zeta^2+b\zeta+c\). Rotational invariance of Haar measure on \(\mathbb T^2\) gives
\[
\|F\|_{H^p(\mathbb D^2)}^p=\frac1{2\pi}\int_0^{2\pi}|P(e^{it})|^p\,dt.
\]
On the diagonal, \(DF(\zeta)=P(1)\zeta^2\). Since normalized area satisfies \(\int_{\mathbb D}|\zeta|^{2p}dA/\pi=1/(p+1)\),
\[
\|DF\|_{A^p(\mathbb D)}=(p+1)^{-1/p}|P(1)|.
\]
If \(P(1)=0\), the ratio vanishes. Otherwise divide by \(P(1)\) and minimize the circle norm under \(P(1)=1\).

**Step 2: reduction from arbitrary complex coefficients.** The maps \(P(z)\mapsto\overline{P(\overline z)}\) and \(P(z)\mapsto z^2P(z^{-1})\) are commuting real-linear norm isometries for the circle \(L^p\) norm and both preserve \(P(1)=1\). Averaging over the four-element symmetry group cannot increase the norm because \(p\ge1\). Every averaged polynomial is of the form
\[
Q_\lambda(z)=\frac\lambda2(1+z^2)+(1-\lambda)z,\qquad \lambda\in\mathbb R.
\]
Conversely, every \(Q_\lambda\) is admissible and \(Q_\lambda(e^{it})=e^{it}[1-\lambda(1-\cos t)]\). Thus the full complex optimization, not merely a symmetric subclass, equals \(\min_{\lambda\in\mathbb R}\Phi_p(\lambda)\), establishing the norm formula and an extremizer.

**Step 3: uniqueness and interior location.** Put \(X(t)=1-\cos t\); then \(0<X<2\) almost everywhere. For \(p>1\), \(\lambda\mapsto\mathbb E|1-\lambda X|^p\) is strictly convex, its derivative at \(\lambda=1/2\) is negative, and its derivative at \(\lambda=1\) equals \(p\,\mathbb E|\cos t|^p>0\). It therefore has exactly one minimizer in \((1/2,1)\). For \(p=1\), \(\Phi_1(\lambda)=1-\lambda\) whenever \(\lambda\le1/2\). On \((1/2,\infty)\), its derivative increases strictly as the single sign-change threshold crosses a continuously distributed part of \(X\); it is negative at \(1/2\) and positive at \(1\). This proves the same existence, location and uniqueness at \(p=1\).

**Step 4: exact integrable endpoint.** Write \(a=2(1-\lambda)/\lambda\in(0,2)\), so that \(Q_\lambda=(1+az+z^2)/(a+2)\). Direct integration gives
\[
N(a)=\frac1{2\pi}\int_0^{2\pi}|a+2\cos t|\,dt
=\frac2\pi\left(\sqrt{4-a^2}+a\arcsin(a/2)\right).
\]
The ratio to maximize is \((a+2)/(2N(a))\). As \(N'(a)=2\arcsin(a/2)/\pi\), its sole stationary point satisfies \(\sqrt{4-a^2}=2\arcsin(a/2)\). With \(\tau=\arcsin(a/2)\), this becomes \(\cos\tau=\tau\). The left side strictly decreases and the right side strictly increases on \((0,\pi/2)\), so the root is unique. Substitution gives the exact values \(\lambda_1=(1+\sin\tau)^{-1}\) and \(K_1=\pi/(4\tau)\). Since \(\cos(3/4)<3/4\), we have \(\tau<3/4\) and hence \(K_1>\pi/3\). The unnormalized extremizer is \(z^2+2\sin\tau\,zw+w^2\).

**Step 5: Hilbert endpoint and sharp slope.** For \(p=2\), \(\Phi_2(\lambda)=1-2\lambda+3\lambda^2/2\), hence \(\lambda_2=2/3\), \(\Phi_2(\lambda_2)=1/3\), and \(K_2=1\). For \(p\) near \(2\), strict convexity and local integrability of the differentiated integrands give a differentiable minimizing branch. By the envelope identity,
\[
\left.\frac{d}{dp}\Phi_p(\lambda_p)\right|_{p=2}
=\frac1{2\pi}\int_0^{2\pi}g(t)^2\log|g(t)|\,dt,
\quad g(t)=\frac{1+2\cos t}{3}.
\]
The factorization \(1+z+z^2=(1-z^3)/(1-z)\) implies that \(\log|1+2\cos t|\) has mean zero and its first two cosine Fourier coefficients are \(1\) and \(1/2\). Abel regularization justifies testing these coefficients against \((1+2\cos t)^2=3+4\cos t+2\cos2t\), yielding
\[
\mathbb E[(1+2\cos t)^2\log|1+2\cos t|]=\frac52.
\]
Consequently \(\left.\frac{d}{dp}\Phi_p(\lambda_p)\right|_{2}=(5/2-3\log3)/9\). Differentiating \(\log K_p=-p^{-1}\log[(p+1)\Phi_p(\lambda_p)]\) at \(p=2\) gives \(K'_2=\frac12\log3-\frac7{12}\). The asserted one-sided expansion follows. Its coefficient is positive because \(\log3<7/6\), and is sharp because \(K_p\) is an exact norm for every \(p\).

## Verification

The standalone `checker.py` uses only Python's standard library. Run `python3 checker.py` from the extracted package. It verifies high-resolution circle quadrature against the exact \(p=1\) integral, symmetry reduction on nonreal randomized coefficients, the all-exponent one-variable optimization on a representative grid, the exact \(p=2\) optimizer, and the endpoint gap. A total of 848 deterministic assertions passed. These checks are finite diagnostics; the unrestricted coefficient quantifiers and limiting slope follow from the preceding analytical steps, not from samples.

## Relationship to prior work

Brevig, Gómez-Serrano, Ortega-Cerdà, and Seip (arXiv:2610.16227v1, publicly posted 12 October 2026) establish contractivity of the unrestricted diagonal operator for \(p\ge2\) and show its failure for \(p<2\) using the linear polynomial \(z+w\). They do not give the sharp norm on the quadratic homogeneous block for \(p=1\), its fixed-point extremizer, or the near-Hilbert sharp slope. Gorbachev's arXiv:2609.32072v1 reviews classical Nikolskii inequalities, including the Ziegler/Geronimus general uniqueness and orthogonality characterizations. Multiplication by a unimodular character converts this specific block to the degree-one trigonometric evaluation problem, so those characterizations are mathematically related; this result evaluates the exact \(p=1\) constant and first-order \(p=2\) coefficient rather than claiming to invent the general extremal characterization. The older low-degree literature may contain an equivalent evaluated expression and remains a publication-priority risk.

## Limitations

The theorem concerns precisely the three-dimensional homogeneous quadratic block and does not determine the unrestricted \(H^p\)-to-\(A^p\) diagonal norm for any \(p<2\). The scalar formula is implicit for general \(p\), explicit at \(p=1\) and \(p=2\), and its asymptotic expansion is local to \(p=2\). No uniqueness assertion is made about every complex polynomial attaining the operator norm. The available prior-literature comparison does not certify priority against every historical Nikolskii special case; independent mathematical review remains to be done.

## References

1. O. F. Brevig, J. Gómez-Serrano, J. Ortega-Cerdà, and K. Seip, *Contractivity of Rudin's diagonal restriction operator for H^p of the polydisc*, arXiv:2610.16227v1 (12 October 2026), especially Theorem 1.1, the introduction, and Corollary 4.1.
2. D. V. Gorbachev, *Sharp Bernstein–Nikolskii inequalities for polynomials and entire functions of exponential type*, arXiv:2609.32072v1 (25 September 2026), especially the classical degree-one extremality characterization, Sections 3.3 and 4.9.
