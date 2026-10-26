# Reentrant harmonic-sampling obstruction on the \(E_8\) projective root lines

## Finding
Let \(X\) consist of one unit-vector representative from each of the 120 antipodal root lines of the \(E_8\) root system in \(\mathbb R^8\). For every even integer \(\ell\ge0\), let \(\mathcal H_\ell\) denote the real or complex degree-\(\ell\) spherical harmonics on \(S^7\), and let \(E_\ell:\mathcal H_\ell\to\mathbb C^{120}\) be evaluation at \(X\). The evaluation is independent of the representatives because \(\ell\) is even.

For the standard Gegenbauer polynomial \(C_\ell^{(3)}\), write \(u_\ell=C_\ell^{(3)}(1)\), \(v_\ell=C_\ell^{(3)}(0)\), and \(w_\ell=C_\ell^{(3)}(1/2)\). The 120-by-120 matrix \(G_\ell=[C_\ell^{(3)}(x\cdot y)]_{x,y\in X}\) has **exactly three potential eigenvalues**
\[
\begin{aligned}
L_0(\ell)&=u_\ell+63v_\ell+56w_\ell &&\text{(multiplicity 1)},\\
L_3(\ell)&=u_\ell+3v_\ell-4w_\ell &&\text{(multiplicity 84)},\\
L_{-9}(\ell)&=u_\ell-9v_\ell+8w_\ell &&\text{(multiplicity 35)}.
\end{aligned}
\]
When two numerical levels coincide, their multiplicities are added. The rank of \(E_\ell\) is the number of positive eigenvalues counted with these multiplicities.

The resulting complete all-even-degree rank classification is
\[
\operatorname{rank}E_\ell=\begin{cases}
1,&\ell=0,\\35,&\ell=2,\\84,&\ell=4,\\119,&\ell=6,\\120,&\ell=8,\\119,&\ell=10,\\120,&\ell\ge12\text{ even}.
\end{cases}
\]
Thus **degree 8 already interpolates arbitrary values on all 120 lines, degree 10 unexpectedly loses precisely the constant data direction, and every even degree at least 12 again interpolates all data**. At degree 8, the evaluation map has sharp nonzero singular-value condition number \(\sqrt{18/7}\), using probability-normalized spherical \(L^2\) in the domain and counting \(\ell^2\) in the target.

## Assumptions and scope
Use the 240 norm-squared-two roots comprising the 112 vectors \(\pm e_i\pm e_j\), \(1\le i<j\le8\), together with the 128 vectors \(\frac12(\pm1,\ldots,\pm1)\) having an even number of minus signs. Divide them by \(\sqrt2\) and identify antipodes to obtain \(X\). All results concern even harmonic degree. For odd degrees, representative orientation matters, and no odd-degree classification is claimed.

The kernel matrix \(G_\ell\) is not itself the evaluation Gram matrix under probability-sphere normalization: the latter is \(\frac{h_\ell}{u_\ell}G_\ell\), where \(h_\ell=\binom{\ell+7}{7}-\binom{\ell+5}{7}\) and a binomial with an invalid lower index is interpreted as zero. This positive factor changes eigenvalues but not rank.

## Proof
**1. The finite geometry.** Two different projective roots have absolute normalized inner product \(0\) or \(1/2\). The orthogonality graph of the 120 lines is strongly regular with parameters \((120,63,30,36)\); this follows by exhaustive exact enumeration of the two explicit root families, and is also a recorded classical property. If \(A\) is its adjacency matrix, then
\[
A\mathbf1=63\mathbf1,\qquad A^2=27I-6A+36J.
\]
On the perpendicular complement of \(\mathbf1\), the possible adjacency eigenvalues solve \(t^2+6t-27=0\), hence are \(3\) and \(-9\). From the trace and total dimension, their multiplicities are respectively \(84\) and \(35\).

**2. Addition theorem and exact spectrum.** For even \(\ell\), the off-diagonal Gegenbauer values depend only on whether two lines are perpendicular: \(v_\ell\) for adjacent pairs and \(w_\ell\) otherwise. Consequently
\[
G_\ell=(u_\ell-w_\ell)I+(v_\ell-w_\ell)A+w_\ell J.
\]
Diagonalizing simultaneously with \(A\) yields the three claimed scalar formulas and multiplicities. The spherical-harmonic addition theorem identifies \(G_\ell\), up to the specified positive factor, with \(E_\ell E_\ell^*\), so its eigenvalues are nonnegative and its rank is exactly \(\operatorname{rank}E_\ell\).

**3. Finite exceptional degrees.** The generating function \(\sum_{\ell\ge0}C_\ell^{(3)}(t)z^\ell=(1-2tz+z^2)^{-3}\) gives \(u_\ell=\binom{\ell+5}{5}\) and permits exact substitution at \(0\) and \(1/2\). For \(\ell=0,2,4,6,8,10\), the three eigenvalue triples in the order \((L_0,L_3,L_{-9})\) are respectively
\[
(120,0,0),\quad (0,0,72),\quad (0,180,0),\quad (0,420,576),\quad (3240,1260,1296),\quad (0,3060,2952).
\]
The multiplicities yield the stated ranks. In particular, at degree 10 the zero vector is exactly the constant adjacency sector; the two other sectors are strictly positive.

**4. No further rank defects.** For any even \(\ell\), the generating functions \((1+z^2)^{-3}\) and \((1-z+z^2)^{-3}=(1+z)^3/(1+z^3)^3\) imply
\[
|v_\ell|=\frac12\left(\frac\ell2+1\right)\left(\frac\ell2+2\right),\qquad
|w_\ell|\le\frac32\left(\frac\ell3+1\right)\left(\frac\ell3+2\right).
\]
Hence strict diagonal dominance of \(G_\ell\) follows from positivity of
\[
P(\ell)=\binom{\ell+5}{5}-\frac{63}{2}\left(\frac\ell2+1\right)\left(\frac\ell2+2\right)-84\left(\frac\ell3+1\right)\left(\frac\ell3+2\right).
\]
For \(\ell=12+s\), \(s\ge0\), exact expansion gives
\[
P(12+s)=1904+\frac{46111}{30}s+\frac{1573}{6}s^2+\frac{449}{24}s^3+\frac58s^4+\frac1{120}s^5>0.
\]
Thus all eigenvalues of \(G_\ell\) are positive whenever \(\ell\ge12\) is even, proving the infinite-degree conclusion without extrapolating from finite tests.

**5. Sharp degree-eight conditioning.** With probability-normalized sphere measure, \(h_8=4719\), \(u_8=1287\), and \(h_8/u_8=11/3\). The squared singular values of \(E_8\), omitting source-side null modes, are \((11/3)(3240,1260,1296)\), with multiplicities \((1,84,35)\). Therefore \(\kappa(E_8)^2=3240/1260=18/7\). Equality is attained on the constant and adjacency-eigenvalue-three sectors, so the condition number is sharp.

## Verification
The standalone standard-library script `check_e8.py` enumerates all 240 integer-scaled roots, identifies precisely 120 antipodal lines, exhaustively checks all 7,140 distinct line pairs and their common-neighbor counts, computes the exact adjacency intersection statistics, and recomputes the above Gegenbauer eigenvalue triples with rational recurrence. It confirms the exceptional-degree table and representative later even degrees. The infinite tail relies on the displayed positive-coefficient polynomial proof, not on the finite script.

## Relationship to prior work
Delsarte, Goethals and Seidel (1977), Theorems 3.3 and 3.6 and Example 8.4, supply the general spherical-harmonic addition/characteristic-matrix theory and describe the \(E_8\) root configuration as a tight spherical 7-design. Coulangeon (2006) discusses the design structure of the \(E_8\) lattice. Schmidt (arXiv:2209.14906, Section 3.1) states the \((120,63,30,36)\) orthogonality graph parameters. None of those inspected texts gives the all-even-degree rank table, proves the rank-stabilization cutoff, or identifies the degree-eight/ten reentrant loss. The spectral formula here uses their established facts and a new explicit cutoff argument; it is not a new addition theorem, root system, or strongly regular graph.

## Limitations
Only the 120 antipodal projective lines and even degrees are classified. The claim does not concern odd-degree evaluations at an oriented choice of representatives or simultaneous mixed-degree evaluation. Previously unindexed equivalent classifications remain a priority risk. The all-degree proof is analytic, with the finite graph counts independently reproducible by exhaustive integer enumeration.

## References
1. P. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata **6** (1977), 363–388. https://www.math.unipd.it/~alvise/PHD_2024/LEZIONI/SPHERE/PDF/DELSARTE%20Spherical%20codes%20and%20designs.pdf
2. R. Coulangeon, *Spherical designs and zeta functions of lattices*, arXiv:math/0611735 (first posted 2006-11-23), https://arxiv.org/abs/math/0611735.
3. S. Schmidt, *Quantum isomorphic strongly regular graphs from the \(E_8\) root system*, arXiv:2209.14906 (first posted 2022-09-29), Section 3.1, https://arxiv.org/abs/2209.14906.
