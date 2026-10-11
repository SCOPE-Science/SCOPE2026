# Paley half-band concentration: exact character spectrum and complementary spectral pairs

## Finding

For every prime \(p\equiv3\pmod4\), let \(H\) be the multiplicative subgroup of nonzero squares in \(\mathbb F_p\), of order \(m=(p-1)/2\). Write \(\eta\) for the Legendre character, with \(\eta(0)=0\), and \(e_p(u)=\exp(2\pi i u/p)\). With counting-measure unitary Fourier normalization, take the \(H\)-by-\(H\) matrix
\[
A_{x,y}=p^{-1/2}e_p(xy),\qquad x,y\in H,
\]
and the output concentration Gram operator \(K=AA^*\). Every multiplicative character \(\chi:H\to\mathbb T\) is an eigenvector. In terms of the **restricted Jacobi sums**
\[
J_\chi=\sum_{t\in H}\eta(1-t)\chi(t),
\]
the complete spectrum, with one entry per character, is
\[
\boxed{\lambda_1=\frac{p+1}{4p},\qquad
\lambda_\chi=\frac12+\frac{iJ_\chi}{2\sqrt p}\quad(\chi\ne1).}
\]
All numbers \(J_\chi\) are purely imaginary; \(J_1=0\). Consequently \(\lambda_{\overline\chi}=1-\lambda_\chi\) for every nontrivial character, and every eigenvalue lies strictly between zero and one. If numerical eigenvalues coincide, their character multiplicities add. The nonconstant sector satisfies the exact identity
\[
\boxed{\sum_{\chi\ne1}(\lambda_\chi-\tfrac12)^2
=\frac{m(m-1)}{4p}.}
\]
For \(p\ge7\), the sharp achievable fraction of Fourier energy inside \(H\) for a nonzero vector supported on \(H\) is
\[
\boxed{C_p=\frac12+\frac{\max_{\chi\ne1}|J_\chi|}{2\sqrt p}
\ge\frac12+\frac12\sqrt{\frac mp}.}
\]
The lower bound is attained at \(p=7\). The complete nonzero maximizer space is the span of input multiplicative characters \(\chi\) with \(\lambda_{\overline\chi}=C_p\). In addition, if \(m\) is prime, the central value \(1/2\) is absent from the nonconstant spectrum. At \(p=3\) there is only the single eigenvalue \(1/3\).

## Assumptions and scope

The prime \(p\) is always congruent to \(3\) modulo \(4\), and the Fourier transform is \((Uf)(\xi)=p^{-1/2}\sum_{x\in\mathbb F_p}f(x)e_p(x\xi)\). The operator acts on vectors indexed by \(H\) with ordinary counting-measure Euclidean norm, and \(A\) is the restriction \(1_H U1_H\) between copies of \(\ell^2(H)\). A nontrivial character means a character other than the constant character. No claim is made for composite moduli, prime powers of higher degree, or primes congruent to \(1\) modulo \(4\). The safe-prime conclusion has the explicit additional hypothesis that \(m=(p-1)/2\) is prime.

## Proof

**Gauss sum and exact Gram matrix.** For \(d\in\mathbb F_p\), the standard quadratic Gauss sum for \(p\equiv3\pmod4\) yields
\[
\sum_{z\in H}e_p(dz)=\frac{p\mathbf1_{d=0}-1+i\sqrt p\,\eta(d)}2.
\]
Set \(E_{x,y}=\eta(x-y)\) on \(H\times H\), and let \(J\) denote the all-ones matrix of size \(m\). Directly expanding \(K_{x,y}=p^{-1}\sum_{z\in H}e_p((x-y)z)\) gives
\[
\boxed{K=\frac12I-\frac1{2p}J+\frac{i}{2\sqrt p}E.}
\]
Because \(\eta(-1)=-1\), \(E\) is a real skew-symmetric matrix. For \(x\in H\), the substitution \(y=xt\) gives \(\sum_{y\in H}E_{x,y}=\sum_{t\in H}\eta(1-t)\). Pairing \(t\) with \(t^{-1}\), and using \(\eta(1-t^{-1})=-\eta(1-t)\), shows this sum vanishes (the term \(t=1\) is zero). Therefore \(E\mathbf1=0\), and the constant eigenvalue of \(K\) is \(1/2-m/(2p)=(p+1)/(4p)\).

**Simultaneous character diagonalization.** Every multiplicative character \(\chi\) of \(H\), viewed as a vector indexed by \(H\), satisfies
\[
(E\chi)(x)=\sum_{y\in H}\eta(x-y)\chi(y)
=\chi(x)\sum_{t\in H}\eta(1-t)\chi(t)=J_\chi\chi(x).
\]
Distinct characters form an orthogonal basis. The inversion pairing also gives \(J_{\bar\chi}=-J_\chi\), while conjugating the defining sum gives \(J_{\bar\chi}=\overline{J_\chi}\); hence each \(J_\chi\) is purely imaginary. The displayed eigenvalue formulas and pair symmetry follow. Since \(m\) is odd, the nontrivial characters split into conjugate pairs; no assumption of simple eigenvalues is needed.

**Centered second moment and energy extremizers.** The function \(t\mapsto\eta(1-t)\) on \(H\) has squared norm \(m-1\). Character Parseval therefore gives \(\sum_\chi|J_\chi|^2=m(m-1)\); the constant term vanishes. Substituting the eigenvalue formula gives the centered identity. For \(p\ge7\), there is at least one nontrivial character, and the average value of \(|J_\chi|^2\) over nontrivial characters is exactly \(m\). By conjugate pairing, the largest nonconstant eigenvalue is \(1/2+\max_{\chi\ne1}|J_\chi|/(2\sqrt p)\), at least the stated lower bound. The constant eigenvalue is strictly below \(1/2\), so cannot maximize. Since \(A\) is symmetric, its input Gram operator is \(A^*A=\overline K\). Therefore an input character \(\chi\) has energy ratio \(\lambda_{\bar\chi}\), and the complete equality space is the span of the listed characters. At \(p=7\), \(H\) has three elements and the two nontrivial restricted Jacobi sums have moduli \(\sqrt3\), proving equality in the lower bound.

**Strict boundaries.** Tao's prime-cyclic support uncertainty theorem says every nonzero \(f\) satisfies \(|\operatorname{supp} f|+|\operatorname{supp} Uf|\ge p+1\). If \(A\) had a nontrivial kernel, some nonzero input supported on \(H\) would have its full Fourier transform supported on \(\mathbb F_p\setminus H\), giving support-sum at most \(m+(p-m)=p\), a contradiction. If \(\|A\|=1\), a nonzero vector would have both support and Fourier support contained in \(H\), giving at most \(2m=p-1\), again impossible. Since \(K=AA^*\) is a positive contraction, all its eigenvalues lie strictly in \((0,1)\).

**Prime-order resonance exclusion.** Suppose additionally that \(m\) is prime. Fix a generator \(g\) of \(H\) and put \(c_j=\eta(1-g^j)\) for \(0\le j<m\). Then \(c_0=0\), whereas all other \(c_j\) are \(\pm1\). For any nontrivial \(\chi\), the number \(J_\chi\) is a value \(\sum_{j=0}^{m-1}c_j\zeta^{kj}\) at a primitive \(m\)-th root \(\zeta^k\). If it vanished, the rational polynomial \(\sum_jc_jz^j\) would be divisible by the irreducible polynomial \(1+z+\cdots+z^{m-1}\). Their degrees force all coefficients \(c_j\) to be equal, contradicting \(c_0=0\) and \(c_1\ne0\). Thus \(J_\chi\ne0\) and no nonconstant eigenvalue is \(1/2\).

## Verification

The standalone `VERIFY.py` recomputes the normalized Fourier submatrix, Legendre Gram identity, multiplicative-character eigenbasis, complementary pairs, centered moment, and prime-order exclusion for primes up to \(101\) that are congruent to \(3\) modulo \(4\). Invoke `python VERIFY.py` with Python, NumPy, and a standard Python interpreter. These finite numerical checks corroborate the formulas but is not a proof for unrestricted primes. The proof above is uniform, and its strict spectral endpoints depend on the stated prime-cyclic uncertainty theorem.

## Relationship to prior work

Renes's 2004 Paley tournament frames provide the standard Gauss-sum/Paley Gram setting, without in their stated results solving the particular quadratic-residue-by-quadratic-residue Fourier compression through the multiplicative character spectrum. Tao's 2003 prime-cyclic uncertainty theorem supplies the already-known strict nonvanishing of all prime Fourier minors; no novelty is claimed for this input. Gregory and Kirkland's 1999 general tournament-matrix estimates concern different singular-value objects and offer general extremal bounds, not this explicit chosen Fourier concentration spectrum. The present assessed contribution is the combined character-by-character concentration spectrum, complementary-pair structure, centered moment, sharp localization eigenspaces, and prime-order center exclusion. Those statements could have an older equivalent in the theory of induced Paley tournaments or Jacobi sums; priority remains subject to specialist comparison.

## Limitations

No elementary closed form for the largest restricted Jacobi sum is claimed for arbitrary prime \(p\); the sharp constant is an exact finite-character-sum maximum. The safe-prime gap is qualitative rather than a uniform numerical separation from \(1/2\). Numerical eigenvalues can approach zero or one closely, but finite-precision computations do not prove equality or non-equality.

## References

- T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first public preprint 2003-08-29, https://arxiv.org/html/math/0308286v6.
- J. M. Renes, *Equiangular Tight Frames From Paley Tournaments*, arXiv:math/0408287, first public preprint 2004-08-20, https://arxiv.org/html/math/0408287v2.
- D. A. Gregory and S. J. Kirkland, *Singular values of tournament matrices*, Electronic Journal of Linear Algebra 5 (1999), 39–52, https://journals.uwyo.edu/index.php/ela/article/view/61.
