# Sharp negative type of the ternary Heisenberg Cayley metric

## Finding

Let \(G=H(\mathbb F_3)\) be the order-27 Heisenberg group and let \(d\) be the graph distance of its canonical four-generator Cayley graph, defined precisely below. There is a unique \(p_*\in(2/3,7/10)\) satisfying
\[
2\cdot 4^{p_*}+2\cdot 2^{p_*}-3\cdot 3^{p_*}-2=0.
\]
Numerically \(p_*=0.677622399811669\ldots\). For every real \(p>0\), the powered-distance matrix \(D_p=[d(g,h)^p]_{g,h\in G}\) is conditionally negative semidefinite if and only if \(p\le p_*\). The inequality is strict on the zero-sum subspace for \(0<p<p_*\); at \(p=p_*\) its nullspace there has dimension exactly four. Consequently the minimum Euclidean dimension realizing \(d^p\) as **squared Euclidean distances** is 26 for \(0<p<p_*\) and 22 at \(p=p_*\).

Equivalently, for every real \(t>0\), the kernel \(K_{t,p}(g,h)=\exp(-t d(g,h)^p)\) is strictly positive definite simultaneously for all \(t>0\) precisely when \(0<p\le p_*\). If \(p>p_*\), it is indefinite for all sufficiently small positive \(t\), while it is strictly positive definite whenever \(t>\log 26\).

## Assumptions and scope

Identify \(G\) with triples \((x,y,z)\in\mathbb F_3^3\), with multiplication
\[
(x,y,z)(a,b,c)=(x+a,y+b,z+c+xb).
\]
The symmetric generating set is \(S=\{(\pm1,0,0),(0,\pm1,0)\}\). Let \(\ell(g)\) be the minimal number of generators in a product equal to \(g\), and set \(d(g,h)=\ell(g^{-1}h)\). This is an undirected connected Cayley graph on 27 distinct vertices. Powers are taken with the convention \(0^p=0\) for \(p>0\). Conditional negative semidefiniteness means \(\sum_{g,h}\overline{c_g}c_h d(g,h)^p\le0\) for every complex coefficient family satisfying \(\sum_g c_g=0\). All Fourier representations and multiplicities below concern the complete complex regular representation; the corresponding real quadratic-form conclusion follows because \(D_p\) is real symmetric.

## Proof

**Distance shells.** Breadth-first multiplication in the four generators gives shell counts \((1,4,8,12,2)\) at distances \(0,1,2,3,4\). These counts can also be verified symbolically by checking the 27 triples; the complete finite enumeration is reproduced by `CHECK.py`.

**Finite-group Fourier decomposition.** Fix \(p>0\), and write \(a=2^p\), \(b=3^p\), \(c=4^p\). Convolution with the function \(g\mapsto\ell(g)^p\) is represented by \(D_p\). The nine one-dimensional irreducible characters \(\chi_{u,v}(x,y,z)=\exp(2\pi i(ux+vy)/3)\) contribute the scalar eigenvalues
\[
\begin{array}{c|c|c}
\text{sector}&\text{eigenvalue}&\text{multiplicity}\\\hline
(u,v)=(0,0)&4+8a+12b+2c&1\\
uv=0,\ (u,v)\ne(0,0)&1-4a+2c&4\\
uv\ne0&-2+2a-3b+2c&4.
\end{array}
\]
The abelian characters have the indicated coefficients because the distance-shell character sums are respectively \((4,8,12,2)\), \((1,-4,0,2)\), and \((-2,2,-3,2)\).

There are two further irreducibles, each of dimension three; they are conjugate. For \(\omega=e^{2\pi i/3}\), one is realized on functions of \(r\in\mathbb F_3\) by
\[
(\rho(x,y,z)f)(r)=\omega^{z+yr}f(r+x).
\]
The Fourier transform \(\sum_{g\in G}\ell(g)^p\rho(g)\), calculated exactly by shell sums, is the real symmetric matrix
\[
M=\begin{pmatrix}
2-2b-c&1+a-2b&1+a-2b\\
1+a-2b&b-c-1&1-2a+b\\
1+a-2b&1-2a+b&b-c-1
\end{pmatrix}.
\]
Its eigenvalues are
\[
2a-c-2,\qquad1-a-c\pm\sqrt3(1+a-2b).
\]
Each of these three values has multiplicity six in \(D_p\), since each three-dimensional irreducible occurs three times in the regular representation and there are two conjugate irreducibles. Thus these six spectral branches exhaust all \(1+4+4+6+6+6=27\) dimensions.

**The unique controlling crossing.** Set \(u=2^p\) and \(\beta=\log_2 3\), so \(3/2<\beta<5/3\). The potentially vanishing fourfold sector is
\[
F(u)=2u^2+2u-2-3u^\beta.
\]
For \(u\ge1\), \(F(1)=-1\), \(F(2)=1\), \(F'(1)=6-3\beta>1\), and
\[
F''(u)=4-3\beta(\beta-1)u^{\beta-2}\ge4-10/3>0.
\]
Therefore \(F\) increases strictly from its negative initial value to infinity, and has exactly one zero \(u_*>1\), equivalent to the stated unique \(p_*\). Rational-power certificates in `CHECK.py` prove \(F(2^{2/3})<0<F(2^{7/10})\); thus \(2/3<p_*<7/10\).

At \(p=p_*\), the other fourfold scalar sector is strictly negative: \(1-4u+2u^2\) is increasing for \(u>1\) and is less than \(-0.2199\) at \(u=2^{7/10}\). The antisymmetric three-dimensional-block eigenvalue satisfies
\[
2a-c-2=-1-(a-1)^2<0.
\]
For \(p\in[2/3,7/10]\) we have \(2b-1-a>0\), so the larger of the remaining block eigenvalues is \(1-a-c+\sqrt3(2b-1-a)\). From the exact integer-power-verified rational bounds
\[
\begin{gathered}
2^{2/3}>1.58740,\quad4^{2/3}>2.51984,\\
3^{7/10}<2.15768,\quad\sqrt3<1.73206,
\end{gathered}
\]
we obtain the rigorous uniform upper bound
\[
1-a-c+\sqrt3(2b-1-a)
<1-1.58740-2.51984+1.73206(2\cdot2.15768-1-1.58740)
<-0.1143.
\]
The other eigenvalue of this pair is smaller. Thus exactly the four \(uv\ne0\) characters vanish at \(p_*\); every other eigenvalue on the zero-sum subspace is strictly negative. The constant-character eigenvalue is positive.

**All exponents and embeddings.** The interval property of negative type implies that \(D_p\) is conditionally negative semidefinite for \(0<p<p_*\); the strictness theorem for finite metric spaces, or the Bernstein integral for fractional powers, makes it strictly negative on the zero-sum subspace. For \(p>p_*\), \(F(2^p)>0\), so the fourfold character sector immediately violates the defining inequality. With \(J=I-\mathbf1\mathbf1^T/27\), the centered squared-distance Gram matrix is \(-JD_pJ/2\), with rank 26 below the threshold and rank 22 at the threshold. These are precisely the smallest possible Euclidean embedding dimensions.

Finally, Schoenberg's correspondence between conditionally negative definite distances and exponential positive definite kernels gives the all-\(t\) criterion. Distinctness of the embedded points makes the Gaussian kernel strictly positive definite for every \(t>0\) in the admissible exponent range. Beyond the threshold, the positive fourfold Fourier eigenvalue of \(D_p\) makes the corresponding eigenvalue of \(K_{t,p}\) negative for all sufficiently small \(t>0\). Since every off-diagonal distance is at least one, \(t>\log26\) gives strict diagonal dominance and hence positive definiteness for **every** \(p>0\).

## Verification

`CHECK.py` constructs all 27 group elements, determines distances by an exhaustive breadth-first search, checks the shell counts, verifies every scalar character sum, reconstructs the two conjugate three-dimensional Fourier blocks symbolically and factors their characteristic polynomial. It also certifies the signs at the rational exponents \(2/3\) and \(7/10\) by comparing integer powers of rational intervals, checks the independent Fourier bounds, and independently tests the 27-by-27 endpoint matrix numerically. Its output is reproduced in `VERIFICATION.md`. The finite numerical checks corroborate but do **not** substitute for the analytic uniqueness, interval and strictness arguments above.

## Relationship to prior work

Sánchez's finite-metric negative-type results provide a general determinant criterion, and Murugan proves general vertex-transitive equality criteria. Those abstract statements apply to many finite graphs but do not give the displayed Heisenberg threshold, its controlling Fourier sector, the four-dimensional degeneracy or the Gaussian bandwidth dichotomy. DeDeo, Martínez, Medrano, Minei, Stark and Terras study this exact degree-four Heisenberg Cayley graph family, using its adjacency spectrum and group representations; their treatment is about adjacency eigenvalues, not fractional powered-distance matrices or negative-type exponents. The present statement refines this context by calculating a different nonlinear spectral family at the smallest odd Heisenberg parameter. Equivalence with an unindexed earlier specialization remains a residual originality risk.

## Limitations

The exact numerical invariant is established for \(H(\mathbb F_3)\) with the canonical four-element generating set, not for all finite Heisenberg groups. The theorem specifies simultaneous positivity for every bandwidth and the small- and large-bandwidth supercritical behavior, but does not classify each intermediate bandwidth at supercritical exponents. The originality comparison is bounded to the inspected primary literature and accessible published records; unindexed equivalent calculations may exist. No independent mathematical audit has been performed.

## References

- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, publicly posted 2011-08-02, https://arxiv.org/abs/1108.0451.
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657v1, publicly posted 2011-12-23, https://arxiv.org/abs/1112.5657.
- M. DeDeo, M. Martínez, A. Medrano, M. Minei, H. Stark and A. Terras, *Spectra of Heisenberg graphs over finite rings*, Conference Publications (2003), pp. 213–222, DOI 10.3934/proc.2003.2003.213; https://doi.org/10.3934/proc.2003.2003.213.
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Trans. Amer. Math. Soc. 44 (1938), 522–536.
