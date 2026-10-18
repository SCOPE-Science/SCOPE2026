# Uniqueness and minimal product length of the closest separable state on the one-zero Dicke edge

## Finding
Let \(n\ge2\) be an integer, let \(0<s<1\), and define
\[
\rho_{n,s}=s|1\rangle^{\otimes n}\!\langle1|^{\otimes n}+(1-s)|D_{n,1}\rangle\!\langle D_{n,1}|,
\quad p=\frac{1-s}{n},\quad q=1-p.
\]
Here \(|D_{n,k}\rangle\) is the normalized symmetric Dicke vector with exactly \(k\) zeros. Set
\[
|\phi_\theta\rangle=\sqrt p\,e^{i\theta}|0\rangle+\sqrt q\,|1\rangle,
\qquad
\sigma_{n,s}=\int_0^{2\pi}|\phi_\theta\rangle^{\otimes n}\!\langle\phi_\theta|^{\otimes n}\,\frac{d\theta}{2\pi}.
\]
Then \(\sigma_{n,s}\) is the **unique** fully separable minimizer of the quantum relative entropy \(D(\rho_{n,s}\Vert\tau)\). Its minimum length as a convex combination of *pure product states* is exactly \(n+1\); the minimum is realized by
\[
\sigma_{n,s}=\frac1{n+1}\sum_{j=0}^{n}
|\phi_{2\pi j/(n+1)}\rangle^{\otimes n}\!\langle\phi_{2\pi j/(n+1)}|^{\otimes n}.
\]
The relative-entropy value and the existence of a phase-averaged optimizer are prior results. The new claims here are the uniqueness of that *density operator* in this rank-two edge family and the exact minimum finite pure-product length; uniqueness of an ensemble is not claimed.

## Assumptions and normalization
The minimization is over all fully separable \(n\)-qubit density matrices, not only symmetric or Dicke-diagonal matrices. The interval \(0<s<1\) is essential. Write \(P_k=|D_{n,k}\rangle\langle D_{n,k}|\) and \(B_k=\binom nk p^kq^{n-k}\). The phase average has Dicke eigenvalues \(B_0,\ldots,B_n>0\), so its rank is \(n+1\). In particular \(B_0=q^n\), \(B_1=(1-s)q^{n-1}\). Logarithms may use any fixed base, with the same base throughout.

## Proof
### 1. A supporting witness and all equality cases
Consider the positive operator
\[
A=\frac{s}{q^n}P_0+\frac1{q^{n-1}}P_1.
\]
We show that \(\operatorname{Tr}(A\tau)\le1\) for every fully separable \(\tau\), with a complete description of the pure product equality cases.

Take a normalized pure product vector
\[
|\Psi\rangle=\bigotimes_{j=1}^n
\bigl(\sqrt{r_j}e^{i\theta_j}|0\rangle+\sqrt{1-r_j}|1\rangle\bigr),
\qquad 0\le r_j\le1,
\]
and write \(u=n^{-1}\sum_j r_j\). Arithmetic-geometric mean yields
\[
|\langle D_{n,0}|\Psi\rangle|^2=\prod_{j=1}^n(1-r_j)\le(1-u)^n.\tag{1}
\]
For the one-zero Dicke overlap, the triangle inequality and Cauchy--Schwarz give
\[
\begin{split}
|\langle D_{n,1}|\Psi\rangle|^2
&\le\frac1n\left(\sum_j\sqrt{r_j}\prod_{\ell\ne j}\sqrt{1-r_\ell}\right)^2\\
&\le\frac1n\left(\sum_j r_j\right)
\left(\sum_j\prod_{\ell\ne j}(1-r_\ell)\right).
\end{split}
\]
The normalized elementary symmetric mean of degree \(n-1\) in the nonnegative variables \(1-r_1,\ldots,1-r_n\) is at most their arithmetic mean to the \((n-1)\)-st power (Maclaurin's inequality); hence
\[
\frac1n\sum_j\prod_{\ell\ne j}(1-r_\ell)\le(1-u)^{n-1},
\]
and therefore
\[
|\langle D_{n,1}|\Psi\rangle|^2\le n u(1-u)^{n-1}.\tag{2}
\]
The inequalities include all boundary cases \(r_j=0,1\) by continuity. Notice that (1) uses the **correct direction** of arithmetic-geometric mean, applied to \(1-r_j\), not to the reciprocal product.

Combining (1) and (2) gives
\[
\langle\Psi|A|\Psi\rangle\le
q^{-n}(1-u)^{n-1}\left[s(1-u)+nqu\right]=:f(u).
\]
Put \(t=u/(1-u)\) for \(0\le u<1\). Then
\[
f(u)=\frac{s+nqt}{q^n(1+t)^n},\qquad
\operatorname{sgn}\left(\frac{df}{dt}\right)
=\operatorname{sgn}\left(q-s-(n-1)qt\right).
\]
Since \(q-s=(n-1)p\), the only maximum occurs at \(t=p/q\), equivalently \(u=p\), where \(f(p)=1\). At \(u=1\) the witness expectation is zero, so this is the global maximum.

If equality \(\langle\Psi|A|\Psi\rangle=1\) holds, then \(u=p\in(0,1)\), and because \(s>0\) equation (1) must be an equality. Strict arithmetic-geometric-mean equality forces \(r_1=\cdots=r_n=p\). The triangle inequality in the Dicke-one overlap (with all amplitudes nonzero) then forces every \(e^{i\theta_j}\) to have the same phase. Conversely every \(|\phi_\theta\rangle^{\otimes n}\) saturates. Consequently the pure product saturation set is **exactly** that common-phase one-parameter orbit, and linearity extends \(\operatorname{Tr}(A\tau)\le1\) to all separable \(\tau\).

### 2. Optimality among all separable density matrices
Let \(\tau\) be fully separable and suppose \(D(\rho_{n,s}\Vert\tau)<\infty\) (otherwise it cannot improve on \(\sigma_{n,s}\)). Write \(a_j=\langle D_{n,j}|\tau|D_{n,j}\rangle\), \(j=0,1\). Jensen's inequality for the strictly concave logarithm gives
\[
\operatorname{Tr}(\rho_{n,s}\log\tau)
\le s\log a_0+(1-s)\log a_1.
\]
With \(B_0=q^n\) and \(B_1=(1-s)q^{n-1}\), weighted arithmetic-geometric mean and the supporting witness imply
\[
\left(\frac{a_0}{B_0}\right)^s
\left(\frac{a_1}{B_1}\right)^{1-s}
\le s\frac{a_0}{B_0}+(1-s)\frac{a_1}{B_1}
=\operatorname{Tr}(A\tau)\le1.
\]
Thus \(\operatorname{Tr}(\rho_{n,s}\log\tau)
\le s\log B_0+(1-s)\log B_1
=\operatorname{Tr}(\rho_{n,s}\log\sigma_{n,s})\), proving optimality of \(\sigma_{n,s}\) and reproducing the previously known relative-entropy value.

### 3. Rigidity of the minimizing density operator
If \(\tau\) is any minimizer, equality holds throughout the preceding chain, in particular \(\operatorname{Tr}(A\tau)=1\). Every pure product component of any separable decomposition must therefore saturate the witness. Section 1 forces
\[
\tau=\int |\phi_\theta\rangle^{\otimes n}\!\langle\phi_\theta|^{\otimes n}\,d\mu(\theta)
\]
for a probability measure on the circle (a finite mixture is included). Equality in logarithmic vector-state Jensen for \(P_0\), whose weight \(s\) is positive, forces \(|D_{n,0}\rangle\) to be an eigenvector of \(\tau\).

In the Dicke basis,
\[
\langle D_{n,k}|\tau|D_{n,\ell}\rangle
=\sqrt{B_kB_\ell}\int e^{i(k-\ell)\theta}\,d\mu(\theta),
\]
with all \(B_k>0\). The eigenvector condition at \(k=0\) forces \(\int e^{im\theta}\,d\mu(\theta)=0\) for \(m=1,\ldots,n\). Every nonzero Dicke-basis index difference has magnitude at most \(n\), so *all* off-diagonal entries of \(\tau\) vanish. Its diagonal entries equal \(B_k\). Hence \(\tau=\sigma_{n,s}\); the closest fully separable state is unique even without restricting the competitor to symmetric states.

### 4. Minimum number of pure product terms
The Dicke eigenvalues \(B_0,\ldots,B_n\) are all positive, so \(\operatorname{rank}\sigma_{n,s}=n+1\). A convex mixture of \(L\) rank-one projectors has rank at most \(L\), giving \(L\ge n+1\) for any pure-product decomposition. For the \((n+1)\)-st roots of unity, the average \(\frac1{n+1}\sum_{j=0}^ne^{2\pi i jm/(n+1)}\) is zero for each \(1\le|m|\le n\), so the claimed \((n+1)\)-term pure product ensemble reproduces \(\sigma_{n,s}\) exactly. It attains the lower bound.

## Verification and limitations
The new proof uses the correct-direction Maclaurin--Cauchy bound (1)--(2). The original displayed product inequality in the earlier proof had the wrong direction and is **not** used. The argument holds for every integer \(n\ge2\) and every real \(0<s<1\), with no extrapolation from finite numerical samples. It does not address the two endpoints or larger Dicke mixtures. Neither uniqueness of a phase measure nor uniqueness of a finite minimizing ensemble is asserted. The existing numerical verifier checks parameter identities and phase quadrature but is supplementary to this analytic proof.

## Comparison to previous results
Wei, Ericsson, Goldbart and Munro introduced the symmetric Dicke mixtures and phase-averaged relative-entropy candidate (2004). Wei's 2008 treatment proves optimality for the broader symmetric family and uses the triangle/Cauchy/Maclaurin bounds for the overlaps with symmetric Dicke states; that *known mathematical ingredient* is explicitly reused here. The further equality-case classification of the witness, Jensen equality and Fourier-moment rigidity prove uniqueness of the density operator and exact minimal finite pure-product length on the interior one-zero edge. Friedland and Gour give a general uniqueness theorem in a full-rank regime, inapplicable to the present rank-two state; that is not a claim that every rank-deficient state is nonunique.

## References
1. T.-C. Wei, M. Ericsson, P. M. Goldbart, and W. J. Munro, *Connections between relative entropy of entanglement and geometric measure of entanglement*, Quantum Information and Computation **4** (2004), arXiv:quant-ph/0405002.
2. T.-C. Wei, *Relative entropy of entanglement for multipartite mixed states: Permutation-invariant states and Dür states*, Physical Review A **78** (2008), 012327, arXiv:0805.1090; especially the Dicke overlap bound in the proof of the symmetric-state result.
3. S. Friedland and G. Gour, *Closed formula for the relative entropy of entanglement in all dimensions*, Physical Review Letters **106** (2011), 130401, arXiv:1007.4544.
