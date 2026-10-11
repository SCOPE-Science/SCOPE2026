# Exact endpoint norm of the second Johnson spherical projector
## Finding
Let \(n\ge4\) and \(2\le k\le\lfloor n/2\rfloor\). Write \(X_{n,k}=\{S\subset[n]:|S|=k\}\) with normalized counting measure, and let \(P^{(2)}_{n,k}\) be the orthogonal projector onto the Johnson component carrying the irreducible \(S_n\)-module of shape \((n-2,2)\). Its dimension is \(d_2=n(n-3)/2\).

Define
\[
q_{n,k}(x)=x(x-1)-\frac{2(k-1)^2}{n-2}x+\frac{k^2(k-1)^2}{(n-1)(n-2)}.
\]
Let \(\alpha<\beta\) be the two roots of \(q_{n,k}\), set \(a=\lceil\alpha\rceil-1\) and \(b=\lfloor\beta\rfloor\), and put
\[
w_j=\binom{k}{j}\binom{n-k}{k-j},\qquad
F_{n,k}(j)=(k-j)^2\bigl((n-2)j-(k-1)^2\bigr)w_j.
\]
Then
\[
\|P^{(2)}_{n,k}\|_{\ell^1\to\ell^1}
=\|P^{(2)}_{n,k}\|_{\ell^\infty\to\ell^\infty}
=\frac{n(n-3)\bigl(F_{n,k}(b)-F_{n,k}(a)\bigr)}{k(k-1)(n-k)(n-k-1)\binom nk}.
\]
Moreover, whenever \(k/n\to\rho\in(0,1/2]\),
\[
\frac{\|P^{(2)}_{n,k}\|}{n}\to\sqrt{\frac{2}{\pi e}}.
\]
By complementation, the same result covers \(k>n/2\) after replacing \(k\) with \(n-k\).

## Assumptions and scope
The operator acts on all complex-valued functions on \(X_{n,k}\), equipped with normalized counting measure. The endpoint norms are the induced norms on the finite \(\ell^1\) and \(\ell^\infty\) spaces. The result concerns the canonical degree-two Johnson primitive idempotent, not the first Johnson component and not an arbitrary projection onto an isomorphic copy.

## Proof
Fix \(S\in X_{n,k}\) and let \(T\) be uniform on \(X_{n,k}\). Then \(J=|S\cap T|\) has weights \(\Pr(J=j)=w_j/\binom nk\). Its first two factorial moments are
\[
\mathbb E J=\frac{k^2}{n},\qquad
\mathbb E[J(J-1)]=\frac{k^2(k-1)^2}{n(n-1)}.
\]
The third factorial moment is \(\mathbb E[J(J-1)(J-2)]=k^2(k-1)^2(k-2)^2/[n(n-1)(n-2)]\). Substitution gives
\[
\mathbb E q_{n,k}(J)=0,\qquad \mathbb E[Jq_{n,k}(J)]=0.
\]
As a function of \(T\), the radial function \(q_{n,k}(|S\cap T|)\) is a polynomial of slice degree at most two. Stabilizer symmetry and the two displayed orthogonality relations make it orthogonal to the constant component and to every degree-one slice harmonic, hence it lies in the \((n-2,2)\) component. Therefore the symmetric kernel \(Aq_{n,k}(|S\cap T|)\), where
\[
A=\frac{n(n-3)(n-2)(n-1)}{2k(k-1)(n-k)(n-k-1)},
\]
defines an equivariant self-adjoint operator with range in that irreducible component. Since \(Aq_{n,k}(k)=d_2\), its trace with normalized counting measure is \(d_2\), so Schur's lemma forces the operator to be exactly \(P^{(2)}_{n,k}\). Thus its reproducing kernel is
\[
Q_{n,k}(x)=Aq_{n,k}(x).
\]
Transitivity and symmetry give both endpoint norms as one row's absolute mass:
\[
\|P^{(2)}_{n,k}\|=\mathbb E|Q_{n,k}(J)|.
\]
Now \(q_{n,k}(0)>0\), \(q_{n,k}(k)>0\), and its weighted mean is zero, so its monic quadratic has two roots \(0<\alpha<\beta<k\), with negative values exactly between them. The exact discrete antiderivative
\[
(n-1)(n-2)q_{n,k}(j)w_j=F_{n,k}(j-1)-F_{n,k}(j)
\]
uses the convention \(F_{n,k}(-1)=F_{n,k}(k)=0\). Hence the positive part telescopes to
\[
\sum_j(q_{n,k}(j))_+w_j=\frac{F_{n,k}(b)-F_{n,k}(a)}{(n-1)(n-2)}.
\]
Because the signed weighted sum is zero, the absolute sum is twice the positive sum. Multiplying by \(A/\binom nk\) yields the stated finite formula.

For the asymptotic, let \(\mu=k^2/n\) and \(\sigma^2=k^2(n-k)^2/[n^2(n-1)]\). The quadratic has the exact centered form
\[
q_{n,k}(x)=(x-\mu)^2-\frac{(n-2k)^2}{n(n-2)}(x-\mu)-\sigma^2.
\]
If \(k/n\to\rho\in(0,1/2]\), the hypergeometric central limit theorem gives \((J-\mu)/\sigma\Rightarrow Z\), with \(Z\) standard normal. Since \(A\to[2\rho^2(1-\rho)^2]^{-1}\), it follows that \(Q_{n,k}(J)/n\Rightarrow(Z^2-1)/2\). Also \(\mathbb E Q_{n,k}(J)^2=d_2\), so the normalized absolute values are uniformly integrable. Consequently
\[
\frac{\|P^{(2)}_{n,k}\|}{n}\to\frac12\mathbb E|Z^2-1|=\sqrt{\frac{2}{\pi e}}.
\]

## Verification
The bundled verifier uses exact rational arithmetic for every \(4\le n\le120\) and \(2\le k\le n/2\). It checks the discrete antiderivative, the two-tail sign pattern, kernel normalization, zero mean, the exact identity \(\mathbb E Q_{n,k}(J)^2=d_2\), and equality of the direct absolute sum with the boundary formula. It reports `VERIFY_OK exact_cases=3481`. Numerical bulk checks are included only as corroboration of the proved limit.

## Relationship to prior work
Scarabotti and Tolli give the finite homogeneous-space isotypic projection framework and identify the Johnson scheme as a basic Gelfand-pair example. Filmus identifies the slice harmonic decomposition with the Johnson primitive idempotents, including the degree-two eigenspace. Krebs and Shaheen derive Johnson spherical functions and Eberlein polynomials representation-theoretically. These sources determine the underlying spectral component, but the inspected texts do not state the endpoint \(\ell^1/\ell^\infty\) norm, the two-boundary telescoping formula above, or its bulk constant. A recent result on hypergeometric mean absolute deviation collapses \(\mathbb E|J-\mathbb EJ|\) to one point mass; that is the degree-one statistic and does not cover the absolute value of the quadratic Johnson spherical kernel here.

## Limitations
The exact formula is proved for the degree-two primitive idempotent only. No claim is made for arbitrary Johnson degrees. The bulk limit assumes the slice density stays away from zero; sparse regimes require different scaling. Classical association-scheme tables may encode the same degree-two kernel under another normalization, so originality is claimed for the endpoint norm reduction and boundary-mass evaluation after statement-level comparison, not for the existence of the Eberlein/Hahn polynomial itself.

## References
1. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533; Proc. London Math. Soc. 100 (2010), 348-376. Primary MSC 43A95.
2. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142.
3. M. Krebs and A. Shaheen, *On the spectra of Johnson graphs*, Electronic Journal of Linear Algebra 17 (2008), 154-167, DOI 10.13001/1081-3810.1256.
4. N. Elezovic, *The mean absolute deviation of the classical discrete distributions: collapse identities, complete asymptotic expansions, and enveloping series*, arXiv:2608.06232, used only for the non-covering degree-one comparison.