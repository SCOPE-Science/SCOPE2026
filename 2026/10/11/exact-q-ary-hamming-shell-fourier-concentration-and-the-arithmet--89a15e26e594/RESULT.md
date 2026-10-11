# Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion

## Finding
Let \(q\ge3\) and \(n\ge2\) be integers. On the finite group \(G=(\mathbb Z/q\mathbb Z)^n\), let the shell \(S_k\) consist of vectors with exactly \(k\) nonzero coordinates, where \(1\le k\le n-1\). Let \(P\) be the orthogonal projection onto the first Fourier band, consisting of the constant and the nontrivial one-coordinate characters. The concentration operator \(C=PM_{\mathbf1_{S_k}}P\) has a completely explicit spectrum.

Set
\[
p=\frac{q-1}{q},\qquad a=\frac{k}{n},\qquad
w=\frac{\binom nk(q-1)^k}{q^n},
\]
and define
\[
R=1+\frac{n(a-p)^2}{p(1-p)},\qquad
U=\frac{na(1-a)}{(n-1)p(1-p)},\qquad
T=\frac ap.
\]
The eigenvalues, listed with their multiplicities (merge coincident levels), are
\[
\boxed{wR\;(1),\quad wU\;(n-1),\quad wT\;(n(q-2)),\quad 0\;(1).}
\]
Every displayed positive eigenvalue is strictly positive in the stated interior-shell range. Consequently,
\[
\operatorname{rank}C=n(q-1),\qquad \dim\ker C=1.
\]
The complete nullspace is spanned by
\[
F(x)=\sum_{i=1}^n\mathbf1_{\{x_i\ne0\}}-k,
\]
which is a nonzero degree-one Fourier function vanishing precisely on the shell.

The restriction map, after quotienting by this unavoidable null direction, has identical positive singular values **if and only if**
\[
\boxed{n\equiv1\pmod q,\qquad k=\frac{(q-1)n+1}{q}.}
\]
This gives an infinite arithmetic family: \(n=q\ell+1\), \(k=(q-1)\ell+1\) for all \(\ell\ge1\). In these cases the nonzero eigenvalue equals \(w(1+1/[n(q-1)])\). Outside the tight family the exact stable-reconstruction condition number is
\[
\kappa=\sqrt{\frac{\max\{R,U,T\}}{\min\{R,U,T\}}}>1.
\]

## Assumptions and scope
The symbol count \(q\) is an arbitrary integer at least three; it need not be a prime power. Every Fourier character has the form \(\chi_{h}(x)=\exp(2\pi i\langle h,x\rangle/q)\). The first band is
\[
\mathcal H=\operatorname{span}\{1,\chi_{a e_i}:1\le i\le n,\ 1\le a\le q-1\},
\quad \dim\mathcal H=1+n(q-1).
\]
The ambient inner product is \(\langle f,g\rangle=q^{-n}\sum_{x\in G}f(x)\overline{g(x)}\). The concentration operator is a positive operator on \(\mathcal H\); eigenvalue multiplicities refer to this finite-dimensional complex Hilbert space. The shell has \(\binom nk(q-1)^k\) points. The quotient-frame statement means that the singular values of \(f\mapsto\mathbf1_{S_k}f\) restricted to the orthogonal complement of \(\ker C\), with ambient normalization, all coincide. No claim is made that restriction is injective on all of \(\mathcal H\): it never is.

## Proof
Write \(Y_i(x)=\mathbf1_{\{x_i\ne0\}}\), so its ambient mean is \(p=(q-1)/q\). Define the normalized radial coordinate
\[
u_i(x)=\frac{Y_i(x)-p}{\sqrt{p(1-p)}}.
\]
The one-coordinate character space decomposes orthogonally in ambient counting measure into \(\mathbb C u_i\) and a \((q-2)\)-dimensional transverse subspace \(V_i\). An element of \(V_i\) is a mean-zero function of \(x_i\) that vanishes at zero and whose sum over the \(q-1\) nonzero symbols is zero. Therefore
\[
\mathcal H=\operatorname{span}\{1,u_1,\ldots,u_n\}\oplus \bigoplus_{i=1}^n V_i.
\]

Condition on \(x\in S_k\) uniformly. The active-coordinate indicators form a uniform \(k\)-subset of \(\{1,\ldots,n\}\), whence
\[
\mathbb E(Y_i\mid S_k)=a,\quad
\operatorname{Var}(Y_i\mid S_k)=a(1-a),\quad
\operatorname{Cov}(Y_i,Y_j\mid S_k)=-\frac{a(1-a)}{n-1}\;(i\ne j).
\]
Conditional on the active indices, nonzero symbols are independent and uniform. Hence all transverse modes have conditional mean zero, distinct-coordinate transverse modes and radial modes are orthogonal, and the conditional Gram operator is the scalar \(T=a/p\) on \(\bigoplus_iV_i\). Indeed a transverse function vanishes on the zero symbol, so its conditional squared norm is \(a/p\) times its ambient squared norm. The multiplicity here is \(n(q-2)\).

On the \((n-1)\)-dimensional radial contrast space \(\{\sum_i c_i u_i:\sum_i c_i=0\}\), the above covariance matrix has eigenvalue
\[
\frac{a(1-a)}{p(1-p)}\left(1+\frac1{n-1}\right)
=\frac{na(1-a)}{(n-1)p(1-p)}=U.
\]
For the remaining span of \(1\) and the normalized radial sum \(n^{-1/2}\sum_i u_i\), the conditional Gram matrix is
\[
\begin{pmatrix}1&b\\b&b^2\end{pmatrix},\qquad
b=\frac{\sqrt n(a-p)}{\sqrt{p(1-p)}}.
\]
It has eigenvalues \(1+b^2=R\) and \(0\). Its null vector corresponds exactly to \(\sum_iY_i-k\). The unconditional concentration inner product equals \(w\) times the conditional inner product, so all the positive eigenvalues acquire the common factor \(w\), whereas the null eigenvalue remains zero. Strict positivity of \(R,U,T\) follows from \(0<a<1\). This proves the spectrum, rank, and one-dimensional kernel.

For the arithmetic classification set \(z=qk-(q-1)n\), an integer. Direct reduction of the three rational expressions gives
\[
R-T=\frac{z(z-1)}{n(q-1)},\qquad
R-U=\frac{(z-1)(z+q-1)}{(n-1)(q-1)},
\]
\[
T-U=\frac{qk(z-1)}{n(n-1)(q-1)}.
\]
Since \(qk>0\), equality of all three positive levels is equivalent to \(z=1\). The integer equation \(qk-(q-1)n=1\) is exactly the boxed congruence and formula for \(k\). In particular \(n=q\ell+1\) gives \(k=(q-1)\ell+1\). Substituting \(z=1\) yields \(R=U=T=1+1/[n(q-1)]\). The singular values of restriction are the square roots of the positive concentration eigenvalues; their ratio gives the stated condition number. The calculation also identifies every pairwise collision: \(R=T\) occurs exactly for \(z\in\{0,1\}\), \(R=U\) for \(z\in\{1,1-q\}\), and \(T=U\) only for \(z=1\). No numerical enumeration is used in this deduction.

## Verification
A standalone checker in `artifacts/verify.py` independently constructs the actual complex Fourier character matrix on each tested \(G\), restricts to \(S_k\), and compares its Hermitian Gram-matrix eigenvalues with the exact formulas. It runs examples for \(q\in\{3,4,5\}\), \(2\le n\le4\), and all interior shells of feasible sizes. Separately it uses Python rational arithmetic, rather than floating-point approximations, to test the arithmetic tightness equivalence over \(3\le q\le15\), \(2\le n\le79\), and all interior shells. Execute from the package root with `python artifacts/verify.py` (requires Python 3 with NumPy). Expected success marker: `VERIFY_OK`. The finite computation does not establish the all-parameter result; the proof above does.

## Relationship to prior work
Multivariate Krawtchouk polynomial theory and harmonic analysis of Hamming schemes provide the natural context. Diaconis–Griffiths develop polynomials on multinomial occupancy spaces. Xu constructs tight polynomial frames on composition spaces; these do not directly state the spectrum of spatial restriction of the **unsymmetrized** coordinate-character band on an individual \(q\)-ary Hamming shell. Bannai–Bannai–Bannai study relative designs on binary Hamming shells, with 'tightness' referring to extremal design cardinalities rather than equality of the nonzero singular values of the present Fourier restriction. The complete \(q\)-ary spectral formula and exact congruence criterion concern this particular concentration operator. The standard covariance formulas used in the proof are not themselves claimed as new.

## Limitations
The theorem concerns only the first Fourier band and one full Hamming shell; it does not treat higher Fourier degrees, unions of shells, arbitrary weighted sampling, or combinatorial subsampling. The degenerate shells \(k=0\) and \(k=n\) are excluded because additional spectral zeros occur there. A general representation-theoretic or association-scheme identity could imply the formulas implicitly; no exhaustive priority guarantee is asserted. Exact calculations for finite parameters verify implementation but are not infinite proofs.

## References
1. E. Bannai, E. Bannai, H. Bannai, *On the existence of tight relative 2-designs on binary Hamming association schemes*, arXiv:1304.5760, first posted 2013-04-21. https://arxiv.org/abs/1304.5760
2. P. Diaconis and R. Griffiths, *An introduction to multivariate Krawtchouk polynomials and their applications*, arXiv:1309.0112, first posted 2013-08-31. https://arxiv.org/abs/1309.0112
3. Y. Xu, *Tight Frame with Hahn and Krawtchouk Polynomials of Several Variables*, arXiv:1309.7526, first posted 2013-09-29. https://arxiv.org/abs/1309.7526
