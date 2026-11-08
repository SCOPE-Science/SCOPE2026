# A hypergeometric singular-spectrum limit for second-order point-mass Cesàro operators

## Finding

For each real \(0<r<1\), let \(W_r\) act on the classical Hardy Hilbert space \(H^2(\mathbb D)\) by
\[
(W_rf)(z)=\frac{f(rz)}{(1-rz)^2}.
\]
This is the second-order generalized Cesàro operator induced by the unit point mass at \(r\). Put \(h=-\log r\), let \(H_0=0\) and \(H_n=\sum_{j=1}^n j^{-1}\), and define the entire functions
\[
F(w)=\sum_{n=0}^\infty\frac{w^n}{(n!)^4},\qquad
G(w)=2\sum_{n=1}^\infty\frac{H_nw^n}{(n!)^4},\qquad
\Delta(w)=F(w)^2-2w\bigl(F(w)G'(w)-F'(w)G(w)\bigr).
\]
The zeros of \(\Delta\) form an infinite strictly increasing sequence of positive real numbers \(0<w_1<w_2<\cdots\), with no finite accumulation point. Every positive zero corresponds to exactly one singular-value rank. For the singular values \(s_j\), in nonincreasing order and repeated by multiplicity,
\[
\boxed{\ \sum_{j=1}^\infty\left|h^2s_j(W_r)-\frac1{4\sqrt{w_j}}\right|^2=O(h^2)\quad(r\uparrow1).\ }
\]
In particular, for each fixed \(j\ge1\), \(h^2s_j(W_r)=1/(4\sqrt{w_j})+O(h)\). The first positive zero obeys \(0.5568<w_1<0.5569\), giving \(\lim_{r\uparrow1}h^2\|W_r\|=0.335032128638\ldots\).

There are exact global moment checks, valid for every \(0<r<1\). With \(q=r^2\),
\[
\operatorname{Tr}(W_r^*W_r)=\frac{1+q}{(1-q)^4},\qquad
\operatorname{Tr}\bigl((W_r^*W_r)^2\bigr)
=\frac{q^6+4q^5+13q^4+16q^3+13q^2+4q+1}{(1-q)^8(1+q)^4}.
\]
Thus the rescaled second and fourth singular-value moments tend respectively to \(1/8\) and \(13/1024\). These assertions form one spectral-limit theorem, with finite-parameter identities furnishing independent normalizations.

## Assumptions and scope

The monomials \(e_n(z)=z^n\), indexed from \(n=0\), are orthonormal in \(H^2(\mathbb D)\). The parameter \(r\) is real and strictly between zero and one. On coefficients, the operator is
\[
(W_ra)_n=r^n\sum_{j=0}^n(n-j+1)a_j.
\]
The singular values are those of the compact Hilbert-space operator \(W_r\). Neither the unbounded endpoint map at \(r=1\) nor a statement about its ordinary eigenvalues is included. The limiting space is \(L^2(0,\infty)\), with Lebesgue measure; its singular values are numbered starting at one.

## Proof

**1. Exact discrete Gram kernel and trace normalization.** The coefficient matrix is lower triangular with entries \(r^n(n-j+1)\) for \(j\le n\). Each of its rows has finite support and decays geometrically, so \(W_r\) is Hilbert–Schmidt. Its positive Gram matrix has the exact entries
\[
(W_r^*W_r)_{jk}=q^{\max(j,k)}\left[A+B|j-k|\right],\quad
A=\frac{1+q}{(1-q)^3},\quad B=\frac1{(1-q)^2}.
\]
Indeed, for \(j\le k\), set \(n=k+t\) in the defining sum and use
\(\sum_{t\ge0}(t+1)^2q^t=(1+q)/(1-q)^3\) and
\(\sum_{t\ge0}(t+1)q^t=(1-q)^{-2}\). Summing the diagonal gives the displayed Hilbert–Schmidt trace. Squaring the Gram matrix and grouping off-diagonal pairs by their positive distance gives
\[
\operatorname{Tr}\bigl((W_r^*W_r)^2\bigr)
=\frac1{1-q^2}\left[
\frac{1+q^2}{1-q^2}A^2
+\frac{4q^2}{(1-q^2)^2}AB
+\frac{2q^2(1+q^2)}{(1-q^2)^3}B^2\right].
\]
Simplification gives the rational expression in the finding. The moments are finite because the Gram operator is trace class.

**2. Hilbert–Schmidt convergence of the entire spectral problem.** Define \(U_h:\ell^2(\mathbb N_0)\to L^2(0,\infty)\) by
\[
U_he_n=h^{-1/2}\mathbf1_{[nh,(n+1)h)}.
\]
It is an isometry. On the whole target space, the zero extension \(U_h(h^2W_{e^{-h}})U_h^*\) is the integral operator with step kernel
\[
K_h(x,y)=h\,e^{-nh}(n-j+1)\mathbf1_{\{j\le n\}},\quad
x\in[nh,(n+1)h),\quad y\in[jh,(j+1)h).
\]
Define the second-order exponentially weighted Volterra operator
\[
(Tf)(x)=e^{-x}\int_0^x(x-y)f(y)\,dy,\quad
K(x,y)=e^{-x}(x-y)\mathbf1_{\{0\le y<x\}}.
\]
If \(j\le n\), the differences between \((n-j+1)h\) and \((x-y)_+\), and between \(e^{-nh}\) and \(e^{-x}\), imply for \(0<h\le1\)
\[
|K_h(x,y)-K(x,y)|\le h e^{-nh}\bigl(2+(n+1)h\bigr).
\]
For \(j>n\), both kernels vanish. Integrating over all cells therefore bounds the squared kernel difference by
\[
h^4\sum_{n=0}^\infty (n+1)e^{-2nh}\bigl(2+(n+1)h\bigr)^2=O(h^2).
\]
Consequently \(\|U_h(h^2W_{e^{-h}})U_h^*-T\|_{\mathcal S_2}=O(h)\). The infinite-dimensional Hilbert–Schmidt singular-value perturbation inequality, obtained by finite-rank approximation from the finite-dimensional Mirsky inequality, now yields
\[
\sum_{j\ge1}|h^2s_j(W_{e^{-h}})-s_j(T)|^2=O(h^2).
\]
In particular no spectral mass disappears at the boundary; this is a whole-sequence result rather than just fixed-rank convergence.

**3. A positive integral kernel and its eigenproblem.** The positive trace-class operator \(Q=T^*T\) has the symmetric continuous kernel
\[
Q(y,z)=\int_{\max(y,z)}^\infty e^{-2x}(x-y)(x-z)\,dx
=\frac{1+|y-z|}{4}e^{-2\max(y,z)}.
\]
It is injective, since \(Tf=0\) implies that the second distributional derivative of \(e^xTf(x)=\int_0^x(x-y)f(y)\,dy\) is \(f=0\). Hence \(Q\) has infinitely many positive eigenvalues tending to zero. Let \(Qf=\lambda f\) with \(\lambda>0\), and put \(u(x)=\int_0^x(x-y)f(y)\,dy\). Then
\[
u(0)=u'(0)=0,\quad u''=f,\quad u''''=\lambda^{-1}e^{-2x}u.
\]
The kernel formula gives \(|f(x)|\le C_\lambda(1+x^{3/2})e^{-2x}\|f\|_2\) for large \(x\), so \(u(x)=a+bx+o(1)\) and \(u''(x),u'''(x)\to0\). Conversely, any nonzero solution of this differential equation with the two conditions at zero, at most linear growth, and exponentially decaying second derivative yields the eigenfunction \(f=u''\): both \(\lambda f\) and \(T^*(e^{-x}u)\) have the same second derivative and vanish with their first derivatives at infinity. This proves the converse, with no appeal to numerical boundary shooting.

**4. Entire characteristic function.** For a complex spectral parameter \(w\), set \(\zeta=we^{-2x}\). The two solutions
\[
u_1(x;w)=F(\zeta),\qquad u_2(x;w)=xF(\zeta)+G(\zeta)
\]
solve \(u''''=16we^{-2x}u\). Termwise differentiation is justified locally uniformly, using \(n^4/(n!)^4=1/((n-1)!)^4\) and \(H_n-H_{n-1}=1/n\). They have respective asymptotics \(u_1\to1\) and \(u_2=x+o(1)\) as \(x\to\infty\). They span all at-most-linear-growth solutions: for any such solution, exponential decay of the forcing implies \(u(x)=a+bx+o(1)\); subtracting \(a u_1+b u_2\) gives a solution vanishing at infinity together with its first three derivatives. Four integrations from infinity produce a Volterra equation whose sup-norm kernel is a contraction on every sufficiently far tail. Thus the difference vanishes on a tail and, by ODE uniqueness, everywhere.

At \(x=0\), the constraints \(u=u'=0\) admit a nonzero combination of \(u_1,u_2\) exactly when
\[
\det\begin{pmatrix}
F(w)&G(w)\\[-1mm]
-2wF'(w)&F(w)-2wG'(w)
\end{pmatrix}
=\Delta(w)=0.
\]
The case \(w=0\) is excluded by \(\Delta(0)=1\). For each nonzero complex zero, the resulting solution has an exponentially decaying second derivative, giving a nonzero eigenfunction of \(Q\) with eigenvalue \(\lambda=(16w)^{-1}\); hence every zero is positive real. Conversely every positive eigenvalue gives a zero. At a positive zero \(F(w)>0\), so the boundary matrix has nullity exactly one, making every positive eigenvalue simple. Thus its singular values are precisely \(s_j(T)=1/(4\sqrt{w_j})\), once per increasing positive root. The growth and injectivity of \(T\) imply infinitely many such roots. Combining with Step 2 proves the main assertion.

**5. Independent moment check and first-root bracket.** Direct integration yields
\[
\operatorname{Tr}(Q)=\int_0^\infty\int_0^x e^{-2x}(x-y)^2\,dy\,dx=\frac18,
\]
\[
\operatorname{Tr}(Q^2)=\frac18\int_0^\infty e^{-4x}\int_0^x(1+x-y)^2\,dy\,dx=\frac{13}{1024}.
\]
Both agree with Step 1 after multiplying by \(h^4\) and \(h^8\), respectively, and taking \(r=e^{-h}\uparrow1\). The entire characteristic has the exact initial expansion
\[
\Delta(w)=1-2w+\frac38w^2-\frac5{324}w^3+\frac{35}{165888}w^4-\cdots.
\]
Exact rational evaluation with bounded tails (see `verification.py`) gives opposite signs at \(w=0.5568\) and \(w=0.5569\). Its derivative is negative throughout \([0,1]\), as follows by the same coefficient-tail estimates, so the enclosed root is the first positive one.

## Verification

Run `python verification.py` with Python's standard library. It independently checks finite-dimensional lower-triangular products, the exact rational Gram formula at several rational parameters, the first characteristic coefficients, the two moment normalizations, and a rigorous rational sign bracket for the first root. Finite checks do not establish the infinite-dimensional convergence, root characterization, or spectral uniqueness; these follow from Steps 2–4. The root decimal is a numerical approximation, not a certified full sequence of zeros.

## Relationship to prior work

Tang and Xie, arXiv:2609.19725v1 (first submitted 2026-09-17), treat mapping, boundedness and compactness of generalized Cesàro operators between Hardy spaces for general measures and exponents; their definition specializes exactly to this point-mass order-two operator. Those mapping statements do not specify its singular-value spectrum or the boundary-layer characteristic function. The accessible introduction was inspected, but complete later sections were not recoverable at this reading and are an explicit priority risk.

An earlier published result on the order-one geometric Rhaly operator identifies the complete singular spectrum at a fixed interior parameter through Hahn–Exton basic Bessel zeros. Its matrix is \(r^n\mathbf1_{\{j\le n\}}\), not the present \(r^n(n-j+1)\mathbf1_{\{j\le n\}}\). Neither an unbounded formal factor \((I-S)^{-1}\) nor the order-one spectral formula supplies the second-order, renormalized spectrum without further analysis. Another published result on the Hardy–Volterra commutator uses the interval kernel \((x-y)/x\) on \([0,1]\), producing a different fourth-order differential equation with coefficient \(x^{-2}\).

Ramlau, Koutschan and Hofmann (arXiv:1811.11642) give transcendental boundary equations for **unweighted** \(n\)-fold integration on \([0,1]\). Their \(n=2\) equation has constant coefficients and finite-interval boundary conditions, whereas the present equation has coefficient \(e^{-2x}\) on the half-line and an explicit confluent hypergeometric determinant. Putinar and Tener (arXiv:1612.03970) obtain singular-value estimates and multiplicity information for geometric square-root-derivative weighted compositions; their operator class and normalization do not imply this entire profile. No direct covering statement was found in the checked sources; this negative search is not a proof of global novelty.

## Limitations

The result concerns only order two, unit point-mass measures, and the classical Hardy Hilbert space. The root equation is exact but implicit; no elementary closed form, uniform higher-root numerical intervals, or sharp large-rank asymptotic is claimed. The \(O(h)\) bound is a norm estimate, not a sharp coefficient. The proof establishes one-dimensional singular eigenspaces but does not separately equate complex analytic zero order with eigenspace dimension. The inaccessible portions of relevant 2026 manuscripts and possible general weighted fourth-order spectral theorems remain publication-priority risks. Independent mathematical verification has not been performed.

## References

1. P. Tang and H. Xie, *Complete mapping criteria for generalized Cesàro operators between Hardy spaces*, arXiv:2609.19725v1 (2026-09-17). https://arxiv.org/abs/2609.19725
2. O. Blasco and A. Pennanen, *Cesàro operator induced by a Bergman kernel*, arXiv:2609.21657v1 (2026-09-18). https://arxiv.org/abs/2609.21657
3. R. Ramlau, C. Koutschan and B. Hofmann, *On the singular value decomposition of n-fold integration operators*, arXiv:1811.11642v1 (2018-11-28). https://arxiv.org/abs/1811.11642
4. M. Putinar and J. E. Tener, *Singular values of weighted composition operators and second quantization*, arXiv:1612.03970v1 (2016-12-12). https://arxiv.org/abs/1612.03970
5. *Hahn–Exton zeros determine every singular value of a geometric Rhaly operator*, published published-finding corpus research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-hahn-exton-zeros-determine-every-singular-value-of-a-geometric-r--43fc115e6443
6. *An entire characteristic determinant for the singular spectrum of the Hardy–Volterra commutator*, published published-finding corpus research record, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-entire-characteristic-determinant-for-the-singular-spectrum-o--2a37cf33f373
