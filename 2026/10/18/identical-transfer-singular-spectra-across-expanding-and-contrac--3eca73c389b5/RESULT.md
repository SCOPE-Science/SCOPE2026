# Identical transfer singular spectra across expanding and contracting toral dynamics

## Finding
Let \(R\in M_d(\mathbb Z)\) be nonsingular and let \(U\in\mathrm{GL}_d(\mathbb Z)\) commute with \(R\). Put \(A_m=U^mR\) for every integer \(m\). For every integer \(n\geq0\), the mean-zero Perron–Frobenius operators \(P_{A_m}^n-\Pi\), considered from the same Fourier-weighted Hilbert space into \(L^2(\mathbb T^d)\), have **identical complete nonzero singular-value multisets**, independent of \(m\).

An explicit two-dimensional family makes this invariance hold despite sharply different hyperbolic geometry. Set
\[
R=\begin{pmatrix}0&2\\1&0\end{pmatrix},\qquad
U=I+R=\begin{pmatrix}1&2\\1&1\end{pmatrix},\qquad A_m=U^mR,\quad m\in\mathbb Z.
\]
All maps have degree two. The map \(A_0\) is expanding, whereas every \(A_m\) with \(m\ne0\) has one expanding and one contracting eigenvalue; the disparity becomes arbitrarily large as \(|m|\to\infty\). Nevertheless, their entire nonzero transfer singular spectra are exactly the same for every iterate.

In particular, for \(s>0\), use the standard isotropic Sobolev norm
\[
\|f\|_{H^s}^2=\sum_{k\in\mathbb Z^2}(1+|k|^2)^s|\widehat f(k)|^2.
\]
The nonzero singular values of \(P_{A_m}^{2j}-\Pi:H^s\to L^2\) are, with multiplicities,
\[
\big\{(1+4^j(a^2+b^2))^{-s/2}:(a,b)\in\mathbb Z^2\setminus\{0\}\big\};
\]
those of \(P_{A_m}^{2j+1}-\Pi\) are
\[
\big\{(1+4^j(a^2+4b^2))^{-s/2}:(a,b)\in\mathbb Z^2\setminus\{0\}\big\}.
\]
Consequently, for every \(m\in\mathbb Z\) and \(n\ge0\),
\[
\|P_{A_m}^n-\Pi\|_{H^s\to L^2}=(1+4^{\lfloor n/2\rfloor})^{-s/2}.
\]
For every \(p\ge1\), the operators belong to Schatten class \(S_p(H^s,L^2)\) exactly when \(sp>2\). In that regime their scaled Schatten norms have distinct finite limits along even and odd iterates:
\[
\begin{aligned}
\lim_{j\to\infty}2^{js}\|P_{A_m}^{2j}-\Pi\|_{S_p}
 &=\left(\sum_{(a,b)\ne(0,0)}(a^2+b^2)^{-sp/2}\right)^{1/p},\\
\lim_{j\to\infty}2^{js}\|P_{A_m}^{2j+1}-\Pi\|_{S_p}
 &=\left(\sum_{(a,b)\ne(0,0)}(a^2+4b^2)^{-sp/2}\right)^{1/p}.
\end{aligned}
\]
The second constant is strictly smaller than the first. Thus the full two-phase smoothing data fail to distinguish an expanding endomorphism from infinitely many hyperbolic nonexpanding ones.

## Assumptions and scope
The torus is \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), with normalized Haar measure. For an integer nonsingular matrix \(A\), let \(T_A(x)=Ax\pmod{\mathbb Z^d}\); it preserves Haar measure. Let \(K_Af=f\circ T_A\), let \(P_A=K_A^*\) on \(L^2\), and let \(\Pi f=\int f\,dx\) denote projection to constants.

More generally than Sobolev spaces, choose any Fourier weight \(\rho:\mathbb Z^d\to(0,\infty)\) bounded below by a positive number, and define the complex Hilbert space \(H_\rho\) by \(\|f\|_{H_\rho}^2=\sum_k\rho(k)^2|\widehat f(k)|^2\). For compactness, assume additionally \(\rho(k)\to\infty\) when \(|k|\to\infty\). The general invariance statement holds for arbitrary such weights, whether radial or not. Its nonzero singular-value formula does not require monotonicity; the explicit norm and asymptotics above use \(\rho(k)=(1+|k|^2)^{s/2}\). All assertions are for the complex Hilbert-space operators \(H_\rho\to L^2\), **not** for the eigenvalue spectrum of the same transfer operator on a single space.

## Proof
Write \(e_k(x)=\exp(2\pi i k\cdot x)\). Since \(K_Ae_l=e_{A^\mathsf T l}\), orthonormal Fourier duality gives
\[
P_A e_k=\begin{cases}e_l,&k=A^\mathsf Tl\text{ for }l\in\mathbb Z^d,\\0,&k\notin A^\mathsf T\mathbb Z^d.\end{cases}
\]
Iteration therefore yields \(P_A^n e_k=e_l\) exactly when \(k=(A^\mathsf T)^nl\). On the normalized Fourier basis \(e_k/\rho(k)\) of \(H_\rho\), the operator \(P_A^n-\Pi\) sends each nonconstant basis vector to either zero or a distinct output Fourier basis vector times \(\rho(k)^{-1}\). Thus its complete nonzero singular multiset is
\[
\big\{\rho(k)^{-1}:k\in(A^\mathsf T)^n\mathbb Z^d\setminus\{0\}\big\},
\]
with multiplicities. If \(\rho\) diverges at infinity, this diagonal injection is compact.

Now \(R\) and \(U\) commute, \(U\) is an integral unimodular matrix, and so, for every integer \(m\) and nonnegative integer \(n\),
\[
(A_m^\mathsf T)^n\mathbb Z^d
=(R^\mathsf T)^n(U^\mathsf T)^{mn}\mathbb Z^d
=(R^\mathsf T)^n\mathbb Z^d.
\]
The last equality uses \((U^\mathsf T)^{mn}\mathbb Z^d=\mathbb Z^d\). This proves the general invariance without assuming expansion.

For the concrete matrices, direct multiplication gives \(R^2=2I\), \(\det U=-1\), and \(U=I+R\). Hence
\[
(R^\mathsf T)^{2j}\mathbb Z^2=2^j\mathbb Z^2,\qquad
(R^\mathsf T)^{2j+1}\mathbb Z^2=2^j(\mathbb Z\times2\mathbb Z).
\]
Substitution in the singular-value multiset yields the two displayed lists. The shortest nonzero vector in either parity lattice has Euclidean length \(2^j\), giving the stated operator norm.

The two eigenvalues of \(A_m\) are \(\sqrt2(1+\sqrt2)^m\) and \(-\sqrt2(1-\sqrt2)^m\). At \(m=0\), both have modulus \(\sqrt2>1\). For every \(m\ne0\), one has modulus below one and the other above one, because \(|1-\sqrt2|=(1+\sqrt2)^{-1}\). Their disparity is unbounded with \(|m|\), although the transfer singular multisets agree identically.

For the Schatten assertion, the sum of the \(p\)-th powers of singular values is precisely a positive two-dimensional lattice sum of \((1+4^jQ(a,b))^{-sp/2}\), with \(Q=a^2+b^2\) or \(Q=a^2+4b^2\). It converges if and only if \(sp>2\), by the elementary two-dimensional lattice counting test. If \(sp>2\), multiply by \(2^{jsp}\) and apply dominated convergence, using \((Q+4^{-j})^{-sp/2}\le Q^{-sp/2}\) for nonzero lattice points, to obtain the two limits. Strictness follows from all summands with \(b\ne0\).

## Verification
The standalone `check.py` uses only exact Python integers. It verifies \(R^2=2I\), the commutation and determinant identities, and equivalence between direct rational inverse-lattice membership and the predicted dyadic parity lattice, for \(-5\le m\le5\), \(0\le n\le12\), and \(-9\le k_1,k_2\le9\). There are 51,623 exact image-membership tests, plus finite frequency-label checks. Run with `python check.py` from the directory containing this result. Infinite lattice identities, compactness and limit statements are proved above and are not inferred from finite testing.

## Relationship to prior work
The October 1, 2026 preprint by Leuridan concerns exactness, Bernoulliness and generators for toral endomorphisms, and motivates distinguishing expanding from nonexpanding examples. The present result concerns a different invariant: **the complete singular-value data of all transfer iterates between weighted Fourier Hilbert spaces**. The full text of that preprint was not accessible here; no claim is made that its entire contents were searched.

Wormell (2017/2020) constructs Fourier and Chebyshev Galerkin approximations for transfer operators of one-dimensional expanding systems. Bandtlow and Slipantschuk (2020) analyze spectral-data approximation for transfer operators associated with holomorphic data. These results concern approximation of eigenvalues, resonances or statistical data under different hypotheses, and do not imply equality of the present full cross-space singular spectra among two-dimensional expanding and contracting endomorphisms. The Fourier action of toral maps and elementary lattice-sum techniques are classical, not claimed as new; the stated contribution is the explicit commuting-unit indistinguishability construction and its exact two-parity profiles.

## Limitations
The invariant is tied to the selected Fourier-weighted input geometry and \(L^2\) output; it does not assert the same Lyapunov exponents, entropy, Bernoulli properties, or ordinary operator eigenvalue spectra. Singular values do not determine conjugacy. Originality is provisional pending broader specialist literature comparison, particularly older work on commuting algebraic endomorphisms and Fourier multiplier methods, and inspection of the full motivating preprint. No independent mathematical validation has been performed.

## References
- Christophe Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators*, arXiv:2610.01642v1, first posted 2026-10-01, https://arxiv.org/abs/2610.01642.
- Caroline L. Wormell, *Spectral Galerkin methods for transfer operators in uniformly expanding dynamics*, arXiv:1705.04431v4, https://arxiv.org/html/1705.04431v4.
- Oscar F. Bandtlow and Julia Slipantschuk, *Lagrange approximation of transfer operators associated with holomorphic data*, arXiv:2004.03534v1, https://arxiv.org/html/2004.03534v1.
