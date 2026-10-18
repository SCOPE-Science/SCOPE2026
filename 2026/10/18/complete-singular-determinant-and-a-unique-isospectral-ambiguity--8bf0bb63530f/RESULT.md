# Complete singular determinant and a unique isospectral ambiguity for reflected Volterra integration

## Finding

On complex \(L^2(0,1)\), define the classical integration operator \((Jf)(x)=\int_0^x f(t)\,dt\), the unitary reflection \((Rf)(x)=f(1-x)\), and the reflected-integral pencil \(T_a=(I+aR)J\) for every real \(a\). Let \(s_1(T_a)\ge s_2(T_a)\ge\cdots>0\) denote the **positive** singular values, including multiplicity. Its exact trace-class Fredholm determinant is
\[
\det(I-z^2T_aT_a^*)=D_a(z)=
\begin{cases}
\displaystyle\frac{\cos z-a\cos(az)}{1-a},&a\ne1,\\[5pt]
\cos z-z\sin z,&a=1.
\end{cases}
\]
Every zero of \(D_a\) is real, nonzero, and simple. The positive zeros \(0<t_1<t_2<\cdots\) give the **entire** positive singular spectrum \(s_j(T_a)=1/t_j\). In particular, the two *different* operators \(T_0\) and \(T_{-1}\) have exactly the same singular-value sequence, namely \(s_j=2/((2j-1)\pi)\). This is the **only** nontrivial real-parameter isospectral pair: equality of complete singular-value multisets for \(T_a,T_b\) occurs precisely when \(a=b\) or \(\{a,b\}=\{0,-1\}\).

The singular values also obey the sharp endpoint law
\[
\lim_{j\to\infty}j\,s_j(T_a)=\frac{\max\{1,|a|\}}{\pi}.
\]
Thus \(T_a\in\mathcal S_p\) exactly when \(p>1\), while
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{j=1}^N s_j(T_a)
=\frac{\max\{1,|a|\}}{\pi}.
\]
The weak-Schatten coefficient is therefore **constant on an entire nontrivial parameter interval**, although the exact singular spectra distinguish every parameter there except the pair above.

## Assumptions and scope

All parameter statements refer to **real** \(a\) and complex \(L^2(0,1)\), equipped with Lebesgue measure. Singular values exclude the infinitely repeated zero singular value at \(a=\pm1\) from the nonzero-spectrum enumeration. The Fredholm determinant is well-defined because \(J\) is Hilbert–Schmidt and \(T_aT_a^*\) is positive trace class. Reflection acts on **the output** of integration; \(RJ\) has kernel \(\mathbf1_{x+t\le1}\), not the adjoint \(J^*\) and not a rank-one operator. No statement here extends the determinant to arbitrary complex parameters or arbitrary weights.

## Proof

**1. Fold the Green operator.** Write \(K=JJ^*\); its integral kernel is \(\min(x,t)\). It is positive, injective and compact. Its unbounded inverse is \(-d^2/dx^2\) with conditions \(w(0)=0\) and \(w'(1)=0\). Let \(L=1/2\) and identify reflection-even and reflection-odd functions on \((0,1)\) with two copies of \(L^2(0,L)\), using normalized restrictions. In these coordinates \(R=\operatorname{diag}(1,-1)\), so \(A_a=I+aR=\operatorname{diag}(c_+,c_-)\) with \(c_+=1+a\), \(c_-=1-a\). Directly folding the kernel gives
\[
K=\begin{pmatrix}K_+&B\\ B^*&K_-\end{pmatrix},\quad
K_+(x,t)=L+\min(x,t),\quad K_-(x,t)=L-\max(x,t),\quad B(x,t)=t-L.
\]
In particular \(B\) has rank one. The nonzero squared singular values of \(T_a=A_aJ\) are precisely the positive eigenvalues of \(A_aKA_a\).

**2. Exact secular equation for \(a\ne\pm1\).** Since \(A_a\) is invertible, \(A_aKA_a y=\mu y\) with \(\mu>0\) is equivalent to
\[
A_a^{-1}K^{-1}A_a^{-1}y=\mu^{-1}y.
\]
For \(t=\mu^{-1/2}\), the even/odd folded pieces \(u,v\) of \(y\) solve
\[
u''+c_+^2t^2u=0,\quad v''+c_-^2t^2v=0;
\qquad u'(L)=0,\quad v(L)=0.
\]
The endpoint conditions for \(A_a^{-1}y\) are
\[
\frac{u(0)}{c_+}+\frac{v(0)}{c_-}=0,\qquad
-\frac{u'(0)}{c_+}+\frac{v'(0)}{c_-}=0.
\]
Using \(u(x)=U\cos(c_+t(L-x))\) and \(v(x)=V\sin(c_-t(L-x))\), a nonzero solution exists precisely when
\[
c_-\cos(c_+tL)\cos(c_-tL)-c_+\sin(c_+tL)\sin(c_-tL)=0.
\]
The cosine addition formulas simplify this expression to \(\cos t-a\cos(at)\). Thus the positive eigenvalue condition is exactly \(D_a(t)=0\).

**3. All zeros are real and simple, including singular parameter limits.** For real \(a\ne\pm1\), the numerator is the derivative of
\[
\sin z-\sin(az)=2\cos\left(\frac{(1+a)z}{2}\right)
\sin\left(\frac{(1-a)z}{2}\right).
\]
The right-hand side is a real entire function in the Laguerre–Pólya class, since both factors have only real zeros. Differentiation preserves that class, so \(\cos z-a\cos(az)\) has only real zeros. They are simple: if it and its derivative vanished at a real \(t\), then \(\cos t=a\cos(at)\) and \(\sin t=a^2\sin(at)\). Squaring and adding gives \(1=a^2\cos^2(at)+a^4\sin^2(at)\), impossible when \(|a|<1\) or \(|a|>1\). For \(a=-1\), the normalized determinant equals \(\cos z\). For \(a=1\), the locally uniform limit \(D_a(z)\to\cos z-z\sin z\) remains real-rooted, and its positive roots are simple: a simultaneous root of it and its derivative would give \((2+t^2)\sin t=0\), impossible for real \(t\). All determinants have value one at the origin; their real zeros therefore occur in nonzero symmetric pairs.

For completeness the exceptional operators can also be checked directly: at \(a=-1\) only the odd folded block survives, namely \(4K_-\), with Neumann–Dirichlet eigenfrequencies \((2j-1)\pi\) and hence singular values \(2/((2j-1)\pi)\). At \(a=1\) only \(4K_+\) survives; the boundary equations for \(K_+\) reduce to \(u'(0)=2u(0)\), \(u'(L)=0\), giving \(t\tan t=1\), or \(D_1(t)=0\). The claimed spectral correspondence therefore holds for all real parameters.

**4. Identify the Fredholm determinant, not merely its zeros.** For every real \(a\), \(D_a\) is an even entire function of exponential type and order at most one, normalized by \(D_a(0)=1\). Hadamard factorization, paired over the real symmetric zeros and without a quadratic exponential factor (order at most one), gives \(D_a(z)=\prod_{j\ge1}(1-z^2/t_j^2)\). Since \(T_aT_a^*\) is trace class, this convergent canonical product is exactly \(\det(I-z^2T_aT_a^*)\). Coefficient comparison additionally yields
\[
\operatorname{tr}(T_aT_a^*)=\frac{1+a+a^2}{2},\qquad
\operatorname{tr}((T_aT_a^*)^2)=
\frac{(1+a+a^2)^2}{4}-\frac{1+a+a^2+a^3+a^4}{12}.
\]

**5. Classify all isospectral real parameters.** Expand the normalized entire determinant:
\[
D_a(z)=\sum_{n\ge0}\frac{(-1)^n}{(2n)!}
\left(\sum_{j=0}^{2n}a^j\right)z^{2n},
\]
with the value at \(a=1\) understood by continuity. If two positive singular spectra agree, their Fredholm determinants agree. Comparison of the quadratic coefficients gives
\((a-b)(a+b+1)=0\). If \(a\ne b\), necessarily \(b=-1-a\). Comparison of the quartic coefficients then gives \(-a(a+1)(2a+1)=0\). The root \(a=-1/2\) yields \(b=a\), so the only distinct choices are \((a,b)=(0,-1)\) and \((-1,0)\). Conversely \(D_0=D_{-1}=\cos z\), proving complete equivalence for that pair.

**6. Sharp singular-value asymptotics.** The folded expression in Step 1 shows that \(A_aKA_a\) differs by finite rank (at most two) from
\[\operatorname{diag}(c_+^2K_+,c_-^2K_-).\]
Both scalar kernels are Green kernels of a regular second-order problem on \((0,L)\). For \(K_+\) the boundary conditions are \(u'(0)=u(0)/L\), \(u'(L)=0\); for \(K_-\) they are \(u'(0)=0\), \(u(L)=0\). Their positive eigenfrequencies have counting law \(N(k)=Lk/\pi+O(1)\). Finite-rank perturbations alter the spectral counting function by at most their rank. Consequently the number of singular values of \(T_a\) exceeding \(\varepsilon>0\) satisfies
\[
\#\{j:s_j(T_a)>\varepsilon\}=
\frac{L(|1+a|+|1-a|)}{\pi\varepsilon}+O(1)
=\frac{\max\{1,|a|\}}{\pi\varepsilon}+O(1),
\quad\varepsilon\downarrow0.
\]
Inversion proves the asserted sharp \(j\,s_j\) limit and all Schatten thresholds. Summing a sequence asymptotic to a positive multiple of \(1/j\) proves the logarithmic limit. The endpoint \(p=1\) diverges, while \(p>1\) converges; for \(0<p<1\) it also diverges.

## Verification

Run `python verify_reflection.py` with NumPy installed as specified in `requirements.txt`. The checker performs 472 assertions, including exact rational identities for the determinant's quadratic and quartic coefficients, independent finite-section singular-value comparisons, Hilbert–Schmidt traces and Fredholm products at several parameters, direct bisection of the scalar secular equation, and convergence to the exceptional parameter. The explicit calculations and tests verify representative cases; the all-parameter determinant, real-rootedness, isospectral classification and high-index asymptotics are established analytically above.

## Relationship to prior work

The classical exact singular values of \(J\) were obtained by Halmos and appear in Eveson's 2003 and Lyubich–Tsedenbayar's 2010 work. Lyubich and Tsedenbayar, *The norms and singular numbers of polynomials of the classical Volterra operator in* \(L^2(0,1)\), specifically study \(\phi(J)\), including \(I+aJ\), not \(J+aRJ\); their full paper was inspected. Eveson's 2004 preprint addresses iterates of Volterra convolution operators and uses reflection in a different norm-estimation argument; it does not supply this determinant. Tuan and Gorenflo analyze singular-value rates for triangular Volterra kernels, not the reflected triangular-plus-Hankel pencil here. General work on reflection-symmetric **rank-one-corrected** weighted integration has a different operator, \(J_w-\alpha Q_w\), where \(Q_w\) has rank one; it does not imply the present two-dimensional folded Green-kernel classification. The known individual value \(s_j(J)=2/((2j-1)\pi)\) is not claimed as new. The claimed contribution is the full real-parameter determinant, its unique nontrivial isospectral ambiguity, and the flat weak-Schatten plateau.

## Limitations

The parameter is real and reflection is unweighted. The result does not determine singular vectors or treat complex parameters or nonsymmetric weights. The Fredholm formula depends on exact interval-reflection symmetry; there is no claim of a general determinant for arbitrary mixed Volterra–Hankel kernels. Published Volterra spectral literature is extensive, and an unindexed equivalent formulation could exist; bibliographic priority requires independent scrutiny. Finite-section checks do not certify infinite-dimensional conclusions independently.

## References

- S. P. Eveson, *Norms of iterates of Volterra operators on* \(L^2\), J. Operator Theory 50 (2003), 369–386, https://jot.theta.ro/jot/archive/2003-050-002/2003-050-002-010.pdf.
- S. P. Eveson, *Asymptotic behaviour of iterates of Volterra operators on* \(L^p(0,1)\), arXiv:math/0409516v1, first posted 27 September 2004, https://arxiv.org/abs/math/0409516.
- Y. Lyubich and D. Tsedenbayar, *The norms and singular numbers of polynomials of the classical Volterra operator in* \(L^2(0,1)\), Studia Math. 199 (2010), 171–184, DOI:10.4064/sm199-2-3; https://www.impan.pl/shop/en/publication/transaction/download/product/90183.
- V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numer. Funct. Anal. Optim. 17 (1996), 453–461, DOI:10.1080/01630569608816704.
