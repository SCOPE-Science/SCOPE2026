# Exact cyclic decimation law for de la Vallée Poussin endpoint norms
## Finding
For integers \(n\ge 1\) and \(m\ge 4\), put \(N=nm\). Define the de la Vallée Poussin kernel
\[
V_n(t)=\frac1n\sum_{k=n}^{2n-1}D_k(t),
\qquad
D_k(t)=\sum_{j=-k}^{k}e^{ijt}.
\]
On \(\mathbb Z_N\) with normalized counting measure, let
\[
(\mathcal V_{n,N}f)(x)=\frac1N\sum_{y\in\mathbb Z_N}
V_n\!\left(\frac{2\pi(x-y)}N\right)f(y).
\]
Then
\[
\boxed{
\|\mathcal V_{n,N}\|_{\ell^\infty\to\ell^\infty}
=\|\mathcal V_{n,N}\|_{\ell^1\to\ell^1}
=A_m
}
\]
where
\[
A_m=\frac1m\sum_{s=0}^{m-1}\left|1+2\cos\frac{2\pi s}{m}\right|.
\]
Thus the exact endpoint norm of the sampled \(n\)-th de la Vallée Poussin operator on a grid of size \(nm\) is independent of \(n\): it is exactly the endpoint norm of the three-frequency Fourier projection on \(\mathbb Z_m\).

The finite sum has the closed residue-class form
\[
A_m=
\begin{cases}
\displaystyle \frac13+\frac{2\sqrt3}{m}\cot\frac{\pi}{m},&m\equiv0\pmod3,\\[1mm]
\displaystyle \frac13+\frac{2}{3m}+\frac4m\frac{\sin(\pi/3-\pi/(3m))}{\sin(\pi/m)},&m\equiv1\pmod3,\\[1mm]
\displaystyle \frac13-\frac{2}{3m}+\frac4m\frac{\sin(\pi/3+\pi/(3m))}{\sin(\pi/m)},&m\equiv2\pmod3.
\end{cases}
\]
Consequently
\[
A_m\longrightarrow \frac13+\frac{2\sqrt3}{\pi}.
\]

## Assumptions and scope
The cyclic group is \(\mathbb Z_N\) with normalized measure \(N^{-1}\sum\). The hypothesis \(m\ge4\) makes the sampled frequencies in \(V_n\), which lie between \(-(2n-1)\) and \(2n-1\), nonaliased modulo \(N=nm\). The same kernel identity remains meaningful on smaller grids, but no claim about that aliased interpretation is needed here.

The statement is an endpoint \(\ell^1\) and \(\ell^\infty\) norm identity. It does not determine the interior \(\ell^p\) norms for \(1<p<\infty\).

## Proof
The classical formula for the kernel is
\[
V_n(t)=\frac{\sin^2(nt)-\sin^2(nt/2)}{n\sin^2(t/2)}
      =\frac{\sin(nt/2)\sin(3nt/2)}{n\sin^2(t/2)}.
\]
Fix \(s\in\{0,\ldots,m-1\}\), write \(t_s=2\pi s/(nm)\), and group the \(N=nm\) samples into the coset
\[
t_s+\frac{2\pi q}{n},\qquad 0\le q<n.
\]
The two numerator sine factors each acquire a factor \((-1)^q\), so their product is unchanged. Hence all nonzero members of one coset have the same sign, and
\[
\sum_{q=0}^{n-1}\left|V_n\!\left(t_s+\frac{2\pi q}{n}\right)\right|
=
\frac{|\sin(nt_s/2)\sin(3nt_s/2)|}{n}
\sum_{q=0}^{n-1}\csc^2\!\left(\frac{t_s}{2}+\frac{\pi q}{n}\right).
\]
The standard cotangent identity
\[
\sum_{q=0}^{n-1}\cot\!\left(x+\frac{\pi q}{n}\right)=n\cot(nx)
\]
and differentiation give
\[
\sum_{q=0}^{n-1}\csc^2\!\left(x+\frac{\pi q}{n}\right)=n^2\csc^2(nx).
\]
Therefore, for \(s\ne0\),
\[
\sum_{q=0}^{n-1}\left|V_n\!\left(t_s+\frac{2\pi q}{n}\right)\right|
=n\left|\frac{\sin(3nt_s/2)}{\sin(nt_s/2)}\right|
=n\left|1+2\cos(nt_s)\right|.
\]
For \(s=0\), the same equality follows by continuity: \(V_n(0)=3n\) and the other \(n-1\) members of that coset vanish. Since \(nt_s=2\pi s/m\), averaging over the \(m\) cosets gives
\[
\frac1N\sum_{r=0}^{N-1}\left|V_n\!\left(\frac{2\pi r}{N}\right)\right|
=\frac1m\sum_{s=0}^{m-1}\left|1+2\cos\frac{2\pi s}{m}\right|=A_m.
\]

A finite convolution matrix has every row and every column equal, up to cyclic permutation, to the sampled kernel. Thus its \(\ell^\infty\) and \(\ell^1\) operator norms are exactly the normalized absolute row sum above. Equality for \(\ell^\infty\) is attained by a phase choice matching one row; equality for \(\ell^1\) follows from the corresponding column sum.

It remains to evaluate \(A_m\). The factor \(1+2\cos(2\pi s/m)\) is negative exactly for integer indices strictly between \(m/3\) and \(2m/3\). Since its unsigned average is obtained from its mean \(1\) by subtracting twice the negative contribution, a finite cosine-progression sum gives the three displayed formulas according to \(m\bmod3\). Expanding \(\sin(\pi/m)\) and \(\cot(\pi/m)\) at zero yields the stated limit.

## Verification
The accompanying `artifacts/verify.py` checks the decimation identity in \(4680\) pairs with \(1\le n\le40\) and \(4\le m\le120\), checks the three residue formulas, and independently checks the differentiated cotangent identity away from its poles. Its maximum numerical errors are below \(4.1\times10^{-14}\) for decimation, \(4.5\times10^{-16}\) for the residue formulas, and \(2.0\times10^{-15}\) relative error for the cosecant-square identity.

These computations are regression checks only. The proof above is exact for every stated \(n\) and \(m\).

## Relationship to prior work
Mehta studies the continuous delayed de la Vallée Poussin kernels and proves that their continuous \(L^1\) norms are constant along dilation families. In the classical \((1,2)\) family, the continuous norm is \(\frac13+\frac{2\sqrt3}{\pi}\). Deregowska and Lewandowska give the same kernel in the operator form used here and study minimality of the continuous operator. Neither inspected paper treats uniform cyclic sampling or the exact coset-by-coset collapse above.

Themistoclakis and Van Barel study discrete generalized de la Vallée Poussin approximation on algebraic grids, including Lebesgue constants and numerical behavior. Their discrete nodes and kernels are Jacobi-based; the inspected report does not state a uniform-cyclic exact norm or a reduction to a three-frequency Fourier projection.

A published exact result determines endpoint norms of the three-frequency Fourier projection on cyclic groups. That result supplies the natural comparison value \(A_m\), but it does not imply that every sampled de la Vallée Poussin kernel on \(\mathbb Z_{nm}\) has exactly that norm. The new content is the all-\(n\) coset decimation identity that establishes this equivalence.

## Limitations
The theorem concerns cyclic grids whose size is an integer multiple of the de la Vallée Poussin scale and, as stated, uses \(m\ge4\) to avoid frequency aliasing. It gives endpoint norms only. It does not claim an analogous exact reduction for arbitrary grid sizes or for interior \(\ell^p\) norms.

## References
1. H. Mehta, *The L1 norm of the generalized de la Vallée Poussin kernel*, arXiv:1311.1407v1, first public 5 November 2013.
2. B. Deregowska and B. Lewandowska, *On the minimal property of de la Vallée Poussin's operator*, Bull. Aust. Math. Soc. 91 (2015), 129–133, DOI:10.1017/S0004972714000744; first published online 8 October 2014.
3. W. Themistoclakis and M. Van Barel, *Generalized de la Vallée Poussin approximations on [-1,1]*, KU Leuven Report TW 666, April 2016.
