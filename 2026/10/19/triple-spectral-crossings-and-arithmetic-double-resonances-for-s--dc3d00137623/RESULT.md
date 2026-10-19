# Triple spectral crossings and arithmetic double resonances for second-Hermite disk localization

## Finding

Let \(h_j\), \(j\ge0\), denote the unit \(L^2(\mathbb R)\)-normalized Hermite functions, and let \(V_{h_2}\) be the short-time Fourier transform with window \(h_2\), with convention
\[
V_{h_2}f(x,\xi)=\int_{\mathbb R}f(t)\overline{h_2(t-x)}e^{-2\pi i\xi t}\,dt.
\]
For \(a>0\), define the positive disk-localization operator by the quadratic form
\[
\langle T_a f,f\rangle=\int_{\pi(x^2+\xi^2)\le a}|V_{h_2}f(x,\xi)|^2\,dx\,d\xi.
\]
The Hermite basis diagonalizes \(T_a\). Write \(\lambda_k(a)=\langle T_a h_k,h_k\rangle\) for \(k\ge0\). Define \(Q_k(a)=(a-k)^2-k\) for nonnegative integers \(k\). For every \(k\ge0\) and \(a>0\),
\[
\boxed{\lambda_{k+1}(a)-\lambda_k(a)=-\frac{e^{-a}a^{k-1}}{2(k+1)!}\,Q_k(a)Q_{k+1}(a).}
\]
The expression is regular at \(k=0\) because \(Q_0(a)=a^2\).

**Complete consecutive-triple classification.** For every \(k\ge0\),
\[
\boxed{\lambda_k(a)=\lambda_{k+1}(a)=\lambda_{k+2}(a)\quad\Longleftrightarrow\quad a=k+1\pm\sqrt{k+1},\quad a>0.}
\]
At each such radius, the middle mode \(k+1\) switches from a strict local maximum to a strict local minimum of the discrete eigenvalue sequence as \(a\) increases past the crossing. No four consecutive eigenvalues coincide at any positive \(a\).

**Arithmetic double resonance.** A positive disk-area parameter admits two *different* consecutive-triple crossings precisely when
\[
\boxed{a=u(u+1),\qquad u=1,2,3,\ldots.}
\]
At that parameter the two triples begin at indices \(u^2-1\) and \((u+1)^2-1\), respectively. Every other positive parameter has at most one consecutive-triple crossing. These statements concern equality of consecutive eigenvalues; they do not assert that nonconsecutive eigenvalues can never coincide or that the triples attain the operator norm.

## Assumptions and scope

The normalized Hermite functions are defined using the Fourier convention in the displayed transform. The disk is centered at the phase-space origin and has Euclidean area \(a\). The assertion holds for every real \(a>0\) and every integer \(k\ge0\), with no large-index or asymptotic hypothesis. The normalizations ensure \(0<\lambda_k(a)<1\).

## Proof

**1. Exact radial eigenvalue density.** Rotational covariance of Hermite matrix coefficients gives diagonalization in the Hermite basis. In the variable \(t=\pi(x^2+\xi^2)\), the squared cross-Hermite spectrogram has radial density
\[
\lambda_k(a)=\frac1{2k!}\int_0^a e^{-t}t^{k-2}[t^2-2kt+k(k-1)]^2\,dt.
\tag{1}
\]
At \(k=0,1\) the negative apparent powers cancel exactly against the squared polynomial, leaving integrable densities. Formula (1) follows also from the normalized Laguerre form \(e^{-t}\,\min(k,2)!\,t^{|k-2|}[L_{\min(k,2)}^{(|k-2|)}(t)]^2/\max(k,2)!\).

**2. Exact adjacent difference.** Define \(F_{k+1}(a)=\int_0^a e^{-t}t^k/k!\,dt\). Direct differentiation and the vanishing of both sides at \(a=0\) give
\[
\lambda_k(a)=F_{k+1}(a)+\frac{e^{-a}a^{k-1}}{2k!}R_k(a),
\qquad R_k(a)=k^2(k-1)-3k(k-1)a+(3k-2)a^2-a^3.
\tag{2}
\]
For \(k=0\), the second term is understood after cancellation at the origin. Substitute (2) at indices \(k\) and \(k+1\), and use \(F_{k+2}-F_{k+1}=-e^{-a}a^{k+1}/(k+1)!\). Expansion and regrouping yield the factored difference in the Finding. This polynomial identity is valid for every nonnegative integer \(k\), including \(k=0,1\).

**3. All triple roots.** Equality of three consecutive eigenvalues is equivalent to vanishing of the adjacent differences. The factored difference shows that either \(Q_{k+1}(a)=0\), or both \(Q_k(a)=Q_{k+2}(a)=0\). In the latter alternative, the equations \((a-k)^2=k\) and \((a-k-2)^2=k+2\) force \(a-k=1/2\) and then \(k=1/4\), impossible for integer \(k\). Thus all triples come precisely from \(Q_{k+1}(a)=0\), whose roots are \(k+1\pm\sqrt{k+1}\); the zero root at \(k=0\) is excluded.

Writing \(n=k+1\) and \(a_0=n+s\sqrt n\), \(s\in\{-1,1\}\), with \(a_0>0\), gives
\[
Q_{n-1}(a_0)=2(1+s\sqrt n),\quad Q_{n+1}(a_0)=-2s\sqrt n,\quad Q_n'(a_0)=2s\sqrt n.
\]
None of these numbers vanishes at a permitted root. Consequently the derivatives of \(\lambda_n-\lambda_{n-1}\) and \(\lambda_{n+1}-\lambda_n\) at \(a_0\) are strictly negative and strictly positive, respectively. This establishes the local peak-to-trough transition. Four consecutive equal eigenvalues would require common roots of \(Q_n\) and \(Q_{n+1}\) for some \(n\ge1\); subtracting their two defining equations forces \(a=n\) and then \(n=0\), a contradiction.

**4. Simultaneous triples.** The sequences \(n+\sqrt n\) and \(n-\sqrt n\) are strictly increasing for positive integers \(n\); a repeated positive parameter for different \(n<m\) must therefore satisfy \(n+\sqrt n=m-\sqrt m\). Put \(d=m-n\). Then \(\sqrt n+\sqrt m=d\), and squaring after isolating one square root shows \(\sqrt n=(d^2+n-m)/(2d)\in\mathbb Q\). Hence \(n=u^2\), \(m=v^2\) for positive integers \(u<v\). Their equality becomes \(u(u+1)=v(v-1)\), so \(v=u+1\). Conversely, every \(u\ge1\) gives the common parameter \(u(u+1)\). Strict monotonicity of both root branches excludes three distinct triples at one parameter.

## Verification

The accompanying `checker.py` uses exact rational polynomial arithmetic and the standard library only. It verifies the factored adjacent-eigenvalue identity at indices \(0\) through \(100\), the integer root restrictions, and the arithmetic double-resonance pattern in bounded ranges; all 403 exact assertions passed. Separate high-precision quadratures verified the triple equalities at indices corresponding to \(n=1,2,3,4,5,9,16,25\), and distinct paired triple values at \(a=2,6,12\). The proof above, rather than finite checks, establishes the unrestricted theorem.

Reproduce the exact checks with `python3 checker.py` from the package directory. No external data or network service is required.

## Relationship to prior work

Daubechies (1988) proves radial Hermite diagonalization for the Gaussian analysis window, establishing the model. Abreu and Gröchenig (2010 preprint) develop the Hermite-window/polyanalytic Bargmann framework. Maximenko and Tellería-Romero (2019, Proposition 6.3) give the general radial Toeplitz eigenvalue integral on true-polyanalytic Fock spaces, from which formula (1) specializes. Those works supply the eigenvalue representation; the contribution here is the explicit all-index **consecutive-triple collision locus**, the local peak-to-trough crossing orientation, and the complete number-theoretic classification of simultaneous collision parameters. A previously established special case at disk area two already recognizes the first triple involving indices zero, one, and two; it is not asserted to be new here.

## Limitations

The classification addresses triples of *consecutive* modes only. It does not classify every equality among nonconsecutive eigenvalues, prove that any triple consists of globally top eigenvalues, or determine norm-maximizing modes at arbitrary area. Although no equivalent full arithmetic collision classification was located in the inspected literature, earlier implicit Laguerre or radial Toeplitz analyses remain a publication-priority risk. Independent mathematical validation is not claimed.

## References

1. I. Daubechies, “Time-frequency localization operators: A geometric phase space approach,” *IEEE Transactions on Information Theory* 34 (1988), 605–612, doi:10.1109/18.9761. Full text: https://sites.math.duke.edu/~ingrid/publications/ieee34-1988.pdf.
2. L. D. Abreu and K. Gröchenig, “Banach Gabor frames with Hermite functions: polyanalytic spaces from the Heisenberg group,” arXiv:1012.4283, publicly submitted 2010-12-20, https://arxiv.org/abs/1012.4283.
3. E. A. Maximenko and A. M. Tellería-Romero, “Radial operators on polyanalytic Bargmann–Segal–Fock spaces,” arXiv:1905.00978, 2019, especially Proposition 6.3, https://arxiv.org/abs/1905.00978.
