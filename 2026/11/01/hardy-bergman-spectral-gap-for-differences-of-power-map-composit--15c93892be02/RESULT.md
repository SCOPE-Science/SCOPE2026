# Hardy–Bergman spectral gap for differences of power-map composition operators

## Finding

Let \(p,q\) be distinct positive integers. On the normalized analytic weighted Bergman space \(A^2_\alpha(\mathbb D)\), \(\alpha>-1\), write \(C_r f(z)=f(z^r)\) and \(D_{p,q}=C_p-C_q\). Set
\[
 c_r=r^{-(\alpha+1)/2},\qquad
 a_{p,q}=(c_p-c_q)^2,\qquad b_{p,q}=(c_p+c_q)^2.
\]
Then the Fredholm essential spectra of the positive products satisfy
\[
 \sigma_{\mathrm{ess}}(D_{p,q}^*D_{p,q})=[a_{p,q},b_{p,q}],
\]
\[
 \sigma_{\mathrm{ess}}(D_{p,q}D_{p,q}^*)=
 \begin{cases}
 [a_{p,q},b_{p,q}],&\min\{p,q\}=1,\\
 \{0\}\cup[a_{p,q},b_{p,q}],&p,q\ge2.
 \end{cases}
\]
In particular, \(\|D_{p,q}\|_{\mathrm e}=c_p+c_q\), and the lower endpoint \(a_{p,q}\) is strictly positive. The range of \(D_{p,q}\) is closed and its kernel is exactly the constants. If \(\min\{p,q\}=1\), then \(D_{p,q}\) is Fredholm of index zero, with one-dimensional kernel and cokernel. If \(p,q\ge2\), then it has infinite-dimensional cokernel and is left semi-Fredholm but not Fredholm.

The Hardy-space endpoint is qualitatively different. On \(H^2(\mathbb D)\), for the same distinct positive integers and the same composition maps,
\[
 \sigma(D_{p,q}^*D_{p,q})=
 \sigma_{\mathrm{ess}}(D_{p,q}^*D_{p,q})=[0,4],
 \qquad \|D_{p,q}\|=\|D_{p,q}\|_{\mathrm e}=2,
\]
and \(D_{p,q}\) has one-dimensional kernel but **nonclosed range**. Thus the strictly positive essential singular gap, and with it closed range, holds throughout the weighted Bergman range \(\alpha>-1\) but disappears at the Hardy endpoint.

## Assumptions and scope

Here \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and \(A^2_\alpha(\mathbb D)\) is the Hilbert space of analytic functions with squared norm
\[
 \|f\|_\alpha^2=\frac{\alpha+1}{\pi}
 \int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,dx\,dy.
\]
For \(H^2(\mathbb D)\) use the standard boundary-monomial norm. The Fredholm essential spectrum is \(\{\lambda:T-\lambda I\text{ is not Fredholm}\}\), equivalently the spectrum of the image in the Calkin algebra; this meaning is used for the two positive operators above. A semi-Fredholm operator has closed range and at least one finite-dimensional defect space. No claim is made about the full ordinary spectra on the weighted Bergman spaces.

## Proof

**Step 1: a compact perturbation of two multiplicative isometries.** The exact monomial squared norms are
\[
 h_n=\|z^n\|_\alpha^2
 =\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)},
 \qquad n\ge0.
\]
For the orthonormal basis \(e_n=z^n/\sqrt{h_n}\), let \(U_re_n=e_{rn}\); each \(U_r\) is an isometry. Direct substitution gives
\[
 C_re_n=\sqrt{\frac{h_{rn}}{h_n}}\,e_{rn},\qquad
 \lim_{n\to\infty}\sqrt{\frac{h_{rn}}{h_n}}=r^{-(\alpha+1)/2}=c_r.
\]
The limit follows from the gamma-ratio asymptotic, and is valid also for \(r=1\). Since the images of distinct basis elements under \(U_r\) are orthogonal, truncating the diagonal coefficient errors after index \(N\) approximates \(C_r-c_rU_r\) in operator norm. This difference is therefore compact. Accordingly,
\[
 D_{p,q}\equiv B:=c_pU_p-c_qU_q\pmod{\mathcal K},
\]
and \(D_{p,q}^*D_{p,q}\equiv B^*B\pmod{\mathcal K}\), with
\[
 B^*B=(c_p^2+c_q^2)I-c_pc_q(S+S^*),\qquad S=U_p^*U_q.
\]

**Step 2: the arithmetic Jacobi decomposition.** Put \(g=\gcd(p,q)\), \(a=p/g\), and \(b=q/g\). Then \(\gcd(a,b)=1\), \(a\ne b\), and
\[
 S=U_bU_a^*,\qquad
 Se_n=\begin{cases}e_{bn/a},&a\mid n,\\0,&a\nmid n.\end{cases}
\]
The vacuum \(e_0\) is a one-dimensional reducing sector, irrelevant for essential spectra.

If \(a=1\) and \(b>1\), then \(S=U_b\). Each positive integer is uniquely \(b^kr\), with \(k\ge0\) and \(b\nmid r\); for each \(r\), the sector spanned by \(\{e_{b^kr}:k\ge0\}\) is a one-sided infinite Jacobi path. There are infinitely many such sectors. The operator \(S+S^*\) on each sector has spectrum \([-2,2]\), seen from the bound \(\|S+S^*\|\le2\) and approximate eigenvectors formed by long trigonometric waves of frequency \(\theta\in[0,\pi]\), with energy \(2\cos\theta\). Selecting orthogonal sectors produces a Weyl sequence for every point of \([-2,2]\). The case \(b=1\), \(a>1\), is the adjoint case and is identical for \(S+S^*\).

If \(a,b>1\), every positive integer has a unique representation \(a^ub^vr\) where \(u,v\ge0\), \(a\nmid r\) and \(b\nmid r\). Coprimality ensures uniqueness and independence of the two maximal exponents. For each such \(r\) and each fixed \(L=u+v\), the subspace
\[
 \operatorname{span}\{e_{a^ub^{L-u}r}:u=0,1,\ldots,L\}
\]
reduces \(S+S^*\) and carries the adjacency matrix of a path with \(L+1\) vertices. Its eigenvalues are
\[
 2\cos\frac{j\pi}{L+2},\qquad 1\le j\le L+1.
\]
For every fixed \(L\) there are infinitely many admissible \(r\), so each displayed value has infinite multiplicity. As \(L\) ranges over the nonnegative integers, these values are dense in \([-2,2]\). Because \(\|S+S^*\|\le2\), this proves in all cases
\[
 \sigma_{\mathrm{ess}}(S+S^*)=[-2,2].
\]
The finite-path versus infinite-ray distinction is a property of this Calkin representative; it does not assert spectral-type stability under arbitrary compact perturbations.

**Step 3: the essential spectra.** Spectral mapping in the Calkin \(C^*\)-algebra gives
\[
 \sigma_{\mathrm{ess}}(D_{p,q}^*D_{p,q})
 =\big[(c_p-c_q)^2,(c_p+c_q)^2\big].
\]
For any element \(x\) of a unital algebra, \(x^*x\) and \(xx^*\) have the same nonzero spectral values; apply this to the Calkin image of \(D_{p,q}\). If \(p,q\ge2\), each \(e_n\) with positive \(n\) divisible by neither \(p\) nor \(q\) is orthogonal to the entire range of \(D_{p,q}\). There are infinitely many such integers, hence the adjoint has infinite-dimensional kernel and zero is in \(\sigma_{\mathrm{ess}}(D_{p,q}D_{p,q}^*)\). If \(\min\{p,q\}=1\), say \(p=1\), then \(D_{p,q}=I-C_q\) differs compactly from \(I-c_qU_q\). Since \(0<c_q<1\), the latter is invertible by a norm-convergent Neumann series. Therefore \(D_{p,q}\) is Fredholm and zero is absent from the essential spectrum of its right positive product. This proves the second displayed formula. The essential norm is the square root of the maximum essential spectral value of \(D_{p,q}^*D_{p,q}\).

**Step 4: closed range and defects.** Because \(p\ne q\) and \(\alpha+1>0\), \(c_p\ne c_q\). Therefore zero is outside the essential spectrum of \(D_{p,q}^*D_{p,q}\); its spectral projection near zero is finite-dimensional, and it is bounded below outside that projection. This implies closed range. If \(f(z)=\sum_{n\ge0}a_nz^n\) is nonconstant and \(n_0\ge1\) is its lowest nonzero positive index, the lowest positive degrees in \(f(z^p)\) and \(f(z^q)\) are the distinct degrees \(pn_0\) and \(qn_0\), so \(D_{p,q}f\ne0\). Constants are killed, hence \(\ker D_{p,q}=\mathbb C1\). The Fredholm index is zero in the \(p=1\) or \(q=1\) case because compact perturbations preserve the index of an invertible operator; in the other case the cokernel is infinite-dimensional by Step 3.

**Step 5: the Hardy boundary.** On \(H^2\), \(\|z^n\|=1\) and \(C_r=U_r\) exactly. Thus \(D_{p,q}=U_p-U_q\), so the same Jacobi calculation, now with \(c_p=c_q=1\), gives \(\sigma_{\mathrm{ess}}(D_{p,q}^*D_{p,q})=[0,4]\). The operator norm is at most \(2\) by the triangle inequality and at least \(2\) by this essential spectrum; therefore it equals \(2\). Since the positive operator is bounded between \(0\) and \(4I\), its ordinary spectrum is also exactly \([0,4]\). Its kernel is still the constants. Were the range of \(D_{p,q}\) closed, its restriction to the orthogonal complement of this one-dimensional kernel would be bounded below, so zero could not be in the essential spectrum of \(D_{p,q}^*D_{p,q}\). This contradiction proves nonclosed range.

## Verification

A standalone standard-library script `verify.py` checks the exact finite monomial Gram identities for integer weights, the coprime arithmetic path action and its Chebyshev eigenvalues, the infinite-ray formula in divisible cases, and convergence of the basis coefficients to \(c_r\). Running the embedded script yielded **27,276 passing finite assertions**. The essential-spectrum theorem relies on the analytical decomposition and Calkin argument above; finite checks alone cannot establish it.

As concrete parameters, for \(\alpha=0\), \(p=2\), \(q=3\), the essential singular interval is \([|2^{-1/2}-3^{-1/2}|,2^{-1/2}+3^{-1/2}]\). This operator has closed range and infinite-dimensional cokernel. For \(p=1\), \(q=3\), the same formula with \(c_1=1\) gives a Fredholm operator of index zero.

## Relationship to prior work

The motivating Li–Wang–Zhao study treats the compactness of finite linear combinations of composition operators on Bergman–Orlicz spaces. Its two main theorems are compactness equivalences, not complete essential singular spectra. Kriete–Moorhouse give conditions for compact linear relations in the Calkin algebra and essential-norm bounds; Hu–Yang derive essential-norm estimates and Schatten criteria for differences. These results do not state the present exact two-sided essential spectral gap or its Hardy-versus-Bergman closed-range consequence. Leng–Zhao address Schatten class membership for cross-adjoint products, rather than the difference's essential positive spectrum.

The graph decomposition of multiplicative composition is a classical idea, and previously investigated cross-products and single monomial self-commutators provide related inputs. The finding does not claim those methods or the algebraic cross-product identity as independently novel. The new assertion is the full positive essential-spectrum and Fredholm/closed-range classification for a pair of power maps across the analytic weighted Bergman/Hardy boundary. The 2015 Abdollahi–Mehrangiz–Roientan article on one-symbol self-commutators was located, but its full text was unavailable for line-by-line comparison, leaving a residual originality risk.

## Limitations

No formula is claimed for the entire ordinary singular spectrum on \(A^2_\alpha\), nor for general nonmonomial symbols, nonlinear sums with three or more symbols, or non-Hilbert Bergman spaces. Independent validation and definitive publication priority have not been established. Literature coverage does not prove uniqueness. The 2015 single-symbol paper remains a full-text comparison risk; stronger reformulations under other terminology may also exist.

## References

1. Y. Li, Z. Wang, L. Zhao, *Compact linear combination of composition operators on Bergman–Orlicz spaces*, arXiv:2609.28111 (first posted 2026-09-23), https://arxiv.org/abs/2609.28111.
2. T. Kriete, J. Moorhouse, *Linear relations in the Calkin algebra for composition operators*, arXiv:math/0608466 (2006), https://arxiv.org/abs/math/0608466.
3. X. Hu, Z. Yang, *Essential norm and Schatten class difference of weighted composition operators over the ball*, arXiv:2507.19745 (2025), https://arxiv.org/abs/2507.19745.
4. Q. Leng, X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472 (2026), https://arxiv.org/abs/2610.15472.
5. A. Abdollahi, S. Mehrangiz, T. Roientan, *Self-commutators of composition operators with monomial symbols on the Bergman space*, Bulletin of the Iranian Mathematical Society 41 (2015), 65–76 (abstract available; complete text not inspected).
