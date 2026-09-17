# Exact complex Plücker constants above the Hilbert exponent

## Statement

For an integer $n\ge 1$ and $0<p\le\infty$, let
\[
\mathcal P_n(v_1,\ldots,v_n)
 =\big(\det(v_r(i_s))_{r,s=1}^n\big)_{I=\{i_1<\cdots<i_n\}}
\]
be the Plücker-coordinate map.  For complex sequence spaces define its optimal coordinate-norm constant by
\[
C^{\mathbb C}_{n,p}
 =\sup_{v_1,\ldots,v_n\ne0}
 \frac{\|\mathcal P_n(v_1,\ldots,v_n)\|_{\ell^p(\binom{\mathbb N}{n})}}
 {\prod_{r=1}^n\|v_r\|_{\ell^p}}.
\]
Then
\[
\boxed{
C^{\mathbb C}_{n,p}=
\begin{cases}
1,&0<p\le2,\\[2mm]
n^{\,n(1/2-1/p)},&2\le p<\infty,
\end{cases}}
\]
and the natural endpoint satisfies
\[
\boxed{C^{\mathbb C}_{n,\infty}=n^{n/2}.}
\]
(The two finite-$p$ formulas agree at $p=2$.)

The $0<p\le2$ part is Theorem 2.1(b,c) of Feldman, arXiv:2608.00983.  The new point is that the entire complex supercritical regime $p>2$ is also exact.

## Proof for $p\ge2$

It is enough to work first with finitely supported vectors; the finite-dimensional estimates below are uniform in the support size and pass to $\ell^p$ by truncation.

### 1. The $p=2$ endpoint

Cauchy--Binet gives
\[
\|\mathcal P_n(v_1,\ldots,v_n)\|_2^2
 =\det(\langle v_r,v_s\rangle)_{r,s=1}^n,
\]
and Hadamard's Gram determinant inequality yields
\[
\|\mathcal P_n(v_1,\ldots,v_n)\|_2
 \le \prod_{r=1}^n\|v_r\|_2.
\]
Thus $C^{\mathbb C}_{n,2}=1$.

### 2. The $p=\infty$ endpoint

If $\|v_r\|_\infty\le1$, every $n\times n$ minor $A_I=(v_r(i_s))$ has each row of Euclidean norm at most $\sqrt n$.  Hadamard's determinant inequality therefore gives
\[
|\det A_I|\le n^{n/2},
\]
so $C^{\mathbb C}_{n,\infty}\le n^{n/2}$.

For the reverse inequality, take the $n$ vectors supported on the first $n$ coordinates whose rows form the unnormalised Fourier matrix
\[
F_n=(\omega^{(r-1)(s-1)})_{r,s=1}^n,
\qquad \omega=e^{2\pi i/n}.
\]
Every entry has modulus $1$, while $F_nF_n^*=nI$; hence $|\det F_n|=n^{n/2}$.  Consequently
$C^{\mathbb C}_{n,\infty}=n^{n/2}$.

### 3. Interpolation is sharp

Apply finite multilinear complex interpolation to the same $n$-linear map between the endpoint couples
\[
(\ell^2)^n\to\ell^2\!\binom{\mathbb N}{n},
\qquad
(\ell^\infty)^n\to\ell^\infty\!\binom{\mathbb N}{n}.
\]
For $2<p<\infty$, write
\[
\frac1p=\frac{1-\theta}{2},\qquad \theta=1-\frac2p.
\]
The endpoint norms $1$ and $n^{n/2}$ give
\[
C^{\mathbb C}_{n,p}
 \le (n^{n/2})^\theta
 =n^{n(1/2-1/p)}.
\]

The Fourier frame above has $\|v_r\|_p=n^{1/p}$ for every row and exactly one nonzero $n$-minor, of modulus $n^{n/2}$.  Therefore
\[
C^{\mathbb C}_{n,p}
 \ge \frac{n^{n/2}}{n^{n/p}}
 =n^{n(1/2-1/p)},
\]
which matches the interpolation upper bound.

## Consequences for the recent sharp-constant problem

Feldman (arXiv:2608.00983, Theorem 2.1(d), Remark 2.2, Problem P1) gives a real $\{\pm1\}$-matrix lower bound and states that the $p>2$ sharp-constant problem contains the classical Hadamard maximal-determinant problem.  For **complex** $\ell^p$, that obstruction disappears: a complex Hadamard matrix exists in every order, with the Fourier matrix providing one explicitly.  Thus the complex version of Problem P1 has a closed form for every $n$ and $p$.

In particular,
\[
\lim_{p\downarrow2}C^{\mathbb C}_{n,p}=1,
\qquad
\lim_{p\to\infty}C^{\mathbb C}_{n,p}=n^{n/2}.
\]
So the continuity question at $2^+$ and the fixed-$n$ large-$p$ asymptotics are completely determined in the complex setting.

There is also a useful scalar-field boundary.  Let $C^{\mathbb R}_{n,p}$ be the corresponding real constant and let $h_n$ be the maximal determinant of an $n\times n$ $\{\pm1\}$ matrix.  Then, for $p>2$,
\[
\max\{1,h_n n^{-n/p}\}
 \le C^{\mathbb R}_{n,p}
 \le C^{\mathbb C}_{n,p}
 =n^{n(1/2-1/p)}.
\]
If a real Hadamard matrix of order $n$ exists, $h_n=n^{n/2}$ and both bounds coincide, so the same exact formula holds over $\mathbb R$ for that order.  Without a real Hadamard matrix, the real problem can remain genuinely different.  Regardless of real Hadamard existence, the displayed complex upper bound and the trivial lower bound $C^{\mathbb R}_{n,p}\ge1$ imply
\[
\lim_{p\downarrow2} C^{\mathbb R}_{n,p}=1.
\]
Thus the $2^+$ continuity part of Problem P1 is settled even for the real scalar interpretation.

## Context and originality

The source preprint explicitly presents the exact $p>2$ constants and continuity at $2^+$ as open.  Its own proof already uses multilinear complex interpolation on $1\le p\le2$, and its Grassmannian is projectivized by $\mathbb C^\times$, so the complex scalar case is naturally within the stated framework.  Tadej--Życzkowski record the standard Fourier construction of a complex Hadamard matrix in every order.

Searches for equivalent statements under the terminology Plücker-coordinate norms, exterior powers, compound matrices, $\ell^p$ norms of minors, and complex Hadamard/Fourier extremizers did not locate this exact supercritical formula.  The ingredients themselves are classical; the contribution is the sharp interpolation synthesis and the resulting scalar-field correction/resolution of the recent open regime.

A residual originality risk remains in older tensor-norm and compound-matrix literature, where an equivalent inequality may be expressed without Plücker terminology.  In particular, the full texts of Defant--Floret, *Tensor Norms and Operator Ideals* (1993), and Ryan, *Introduction to Tensor Products of Banach Spaces* (2002), were not exhaustively inspected.  The source preprint itself cites those works for neighboring tensor-norm facts but states that it had not located the sharp constant in print.

## References

1. D. V. Feldman, *Plücker coordinates of finite-dimensional subspaces of $\ell^p$ and its direct sums: summability, reconstruction, stratification*, arXiv:2608.00983 (2026). https://arxiv.org/abs/2608.00983
2. J. Bergh and J. Löfström, *Interpolation Spaces: An Introduction*, Grundlehren 223, Springer (1976), especially the multilinear complex interpolation theorem cited by Feldman. https://doi.org/10.1007/978-3-642-66451-9
3. W. Tadej and K. Życzkowski, *A concise guide to complex Hadamard matrices*, Open Systems & Information Dynamics 13 (2006), 133--177. https://arxiv.org/abs/quant-ph/0512154 ; https://doi.org/10.1007/s11080-006-8220-2

**Same-model review: passed. Cross-model review: not yet performed.**
