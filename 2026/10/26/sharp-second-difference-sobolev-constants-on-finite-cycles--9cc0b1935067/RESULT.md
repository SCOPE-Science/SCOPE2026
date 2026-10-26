# Sharp second-difference Sobolev constants on finite cycles

## Finding
For every integer \(N\ge3\), let \(\mathbb K=\mathbb R\) or \(\mathbb C\) and let \(x=(x_j)_{j\in\mathbb Z/N\mathbb Z}\in\mathbb K^N\) satisfy \(\sum_jx_j=0\). Define the cyclic forward difference by \((Dx)_j=x_{j+1}-x_j\); all norms below are unnormalized counting-measure norms. The optimal constant in
\[
\sum_j|x_j|\le C_{\mathbb K,N}\left(\sum_j|(D^2x)_j|^2\right)^{1/2}
\]
is, with \(m=\lfloor N/2\rfloor\) and \(h=m(N-m)\),
\[
\boxed{C_{\mathbb R,N}^2=\frac{h\,[2h^2+(N^2+15)h+24]}{180N},\qquad
 C_{\mathbb C,N}^2=\frac{N}{16\sin^4(\pi/N)}.}
\]
The constants coincide exactly at \(N=4\), and \(C_{\mathbb R,N}<C_{\mathbb C,N}\) at every other \(N\ge3\). In the real case a maximizing vector is obtained from the cyclic bi-Laplacian Green operator applied to a sign vector whose positive coordinates are \(m\) consecutive vertices. In the complex case every nonzero first Fourier character is maximizing. In particular,
\[
\lim_{N\to\infty}\frac{C_{\mathbb R,N}}{C_{\mathbb C,N}}=\frac{\pi^2}{\sqrt{120}}.
\]

## Assumptions and scope
The ambient space consists of all real or complex sequences indexed by the finite cycle, with zero arithmetic mean; the difference is cyclic, rather than the zero-extended Dirichlet difference. The right-hand side is the ordinary counting-measure \(\ell^2\) norm of the second forward difference, and the left-hand side is the counting-measure \(\ell^1\) norm. The convention matters: neither probability-normalized norms nor endpoint zero-extension may be substituted without rescaling or changing the theorem. All \(N\ge3\) are included. The result gives an attaining family, not a classification of all real equality cases.

## Proof
Let \(L=D^*D\) be the cycle Laplacian. On the zero-mean subspace, \(L\) is positive and invertible, and the energy operator of \(D^2\) equals \((D^2)^*D^2=L^2\). Write \(G=(L^2)^\dagger\) for the Moore--Penrose inverse on the full coordinate space (zero on constants). The entries of this real circulant operator are \(G_{jk}=g(j-k)\), where, for the representative \(0\le r<N\),
\[
H(r)=r(N-r),\qquad
 g(r)=\frac{N^4+10N^2-11}{720N}-\frac{H(r)}{12N}-\frac{H(r)^2}{24N}.
\]
This formula is verified algebraically: its sum over a period vanishes, and applying the cyclic second-neighbor Laplacian twice gives \(L^2g=\delta_0-N^{-1}\mathbf1\). One can first check \(Lg(r)=(N^2-1)/(12N)-H(r)/(2N)\), then check the cyclic boundary index separately. Thus \(G\) is precisely the required pseudoinverse; no limiting or asymptotic argument is used here.

For real vectors, \(\|x\|_1=\max_{\sigma\in\{-1,1\}^N}\langle\sigma,x\rangle\). Hilbert-space duality with the energy inner product on the zero-mean space gives
\[
 C_{\mathbb R,N}^2=\max_{\sigma\in\{-1,1\}^N}\langle\sigma,G\sigma\rangle.
\]
Given \(\sigma=2\mathbf1_A-\mathbf1\) for a subset \(A\) of \(m_A\) vertices and using \(G\mathbf1=0\), its value is \(4\langle\mathbf1_A,G\mathbf1_A\rangle\).

Put \(K=\lfloor N/2\rfloor\), and let \(d(j,k)\) be the shortest cyclic distance. Because \(H(r)\) strictly increases with \(r\) for \(0\le r\le K\), \(g\) is strictly decreasing with cyclic distance on these indices. Its layer-cake decomposition is
\[
 g(d)=g(K)+\sum_{r=0}^{K-1}[g(r)-g(r+1)]\,\mathbf1_{\{d\le r\}}.
\]
For each integer \(r\), the number of pairs of points in \(A\) with cyclic distance at most \(r\) is maximized, at prescribed \(|A|\), by an interval of consecutive cyclic vertices. This is the published cycle-power edge-isoperimetric theorem of Vasilev [2, Theorem 1], with the radius-zero term constant for fixed cardinality. Since every coefficient \(g(r)-g(r+1)\) is positive, a consecutive set maximizes \(\langle\mathbf1_A,G\mathbf1_A\rangle\) for every prescribed \(m_A\).

For a consecutive block of \(m_A\) vertices, counting pair separations gives
\[
4\langle\mathbf1_A,G\mathbf1_A\rangle
=4\left(m_Ag(0)+2\sum_{r=1}^{m_A-1}(m_A-r)g(r)\right)
=\frac{u\,[2u^2+(N^2+15)u+24]}{180N},\quad u=m_A(N-m_A).
\]
The last identity follows by substituting the displayed quartic Green polynomial and summing elementary powers. The displayed expression is strictly increasing in \(u\ge0\). Consequently \(m_A\in\{\lfloor N/2\rfloor,\lceil N/2\rceil\}\) is optimal, yielding the stated real constant. For such an interval take \(\sigma=2\mathbf1_A-\mathbf1\) and \(x=G\sigma\). Since \(\langle\sigma,x\rangle=C_{\mathbb R,N}^2=\|D^2x\|_2^2\), dual optimality forces \(\|x\|_1=\langle\sigma,x\rangle\), so this is indeed a real extremizer (after arbitrary nonzero scaling).

For complex sequences, Cauchy--Schwarz and the sharp Fourier spectral gap of the cycle Laplacian give
\[
\|x\|_1\le\sqrt N\|x\|_2
\le\frac{\sqrt N}{4\sin^2(\pi/N)}\|D^2x\|_2.
\]
Equality is attained by \(x_j=e^{2\pi i j/N}\), proving the complex constant. Equality for a nonzero *real* vector in this chain would require constant \(|x_j|\) and membership in the first Fourier eigenspace. For even \(N\), constant modulus implies \(x_j\in\{\pm a\}\), while an eigenvector there satisfies \(x_{j-1}+x_{j+1}=2\cos(2\pi/N)x_j\); this forces \(\cos(2\pi/N)\in\{-1,0,1\}\), and for \(N\ge4\) only \(N=4\) is possible. For odd \(N\), constant-modulus nonzero real coordinates cannot have zero sum. At \(N=4\), \((1,1,-1,-1)\) attains both constants. This proves the strict separation. Finally \(m(N-m)=N^2/4+O(1)\), and \(\sin(\pi/N)\sim\pi/N\), giving the stated ratio limit.

## Verification
The standalone standard-library script `verification/check_cycles.py` independently constructs the rational Green formula, checks \(L^2g=\delta_0-N^{-1}\mathbf1\) and zero mean for \(3\le N\le60\), verifies monotonicity and the closed block formula, and exhaustively checks all sign subsets for \(3\le N\le13\). It passed 2,853 exact-rational assertions. The finite checks are diagnostic and do not replace the all-order proof, whose nontrivial universal rearrangement step is explicitly based on [2].

## Relationship to prior work
Hindov, Nitzan, Olsen and Rydhe [1, Theorem 1] find sharp \(\ell^1\)-to-\(\ell^2\) higher-difference constants with *zero extension outside a finite interval*, where their polynomial extremizers differ from the cyclic mean-zero extremizers here. Vasilev [2, Theorem 1] proves the cycle-power edge-isoperimetric theorem, which supplies an important already-known combinatorial ingredient; it does not state an inverse bi-Laplacian Sobolev norm or a real--complex contrast. Earlier periodic first-difference sharp bounds address the energy \(\|Dx\|_2\), not \(\|D^2x\|_2\). The present statement combines an exact biharmonic Green identity with [2] and an independent Fourier extremality argument to solve the natural second-order periodic endpoint problem. No new graph-isoperimetric theorem is claimed.

## Limitations
The optimal sign sets are shown to include balanced consecutive blocks; uniqueness or a complete equality classification for arbitrary sign sets is not claimed. The proof treats the second cyclic difference, not all orders. The novelty comparison cannot exclude an older equivalent formulation in periodic spline, Green-kernel or discrete Sobolev literature; independent historical-priority assessment remains appropriate. No infinite-dimensional norm inequality is inferred from the finite-cycle formulas.

## References
[1] R. Hindov, S. Nitzan, J.-F. Olsen and E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1, first submitted 2026-10-13. Theorem 1 and Sections 1--4.

[2] K. Vasilev, *The edge-isoperimetric inequality for powers of cycles*, arXiv:2601.06912v1, first submitted 2026-01-11. Theorem 1 and its proof in Section 3; also *Mathematics and Education in Mathematics* 55 (2026), 78--84.
