# Complete two-point tightness profile in finite abelian groups
## Finding
Let \(G\) be a finite abelian group and let
\[
E=\{x,y\}\subset G,\qquad d=y-x,\qquad m=\operatorname{ord}(d)\ge2.
\]
For the tightness quantities introduced by Ferguson--Mayeli--Sothanaphan, define
\[
c_m=
\begin{cases}
0,&m\text{ even},\\
\sin(\pi/(2m)),&m\text{ odd}.
\end{cases}
\]
Then
\[
L(E)=2(1-c_m),\qquad
U(E)=2(1+c_m),
\]
\[
\rho(E)=\frac{1+c_m}{1-c_m},\qquad
D(E)=2\sqrt{1-c_m^2}.
\]
Equivalently,
\[
\rho(E)=
\begin{cases}
1,&m\text{ even},\\
\tan^2\!\left(\pi/4+\pi/(4m)\right),&m\text{ odd}.
\end{cases}
\]
Hence a two-point subset of a finite abelian group is spectral if and only if the order of its difference is even. For odd \(m\), the same formula gives the exact quantitative failure of spectrality.

## Assumptions and scope
The definitions are those of Ferguson--Mayeli--Sothanaphan. If \(B\subset\widehat G\) has two characters, \(L_E(B)\) and \(U_E(B)\) are the optimal squared Riesz bounds of the \(2\times2\) Fourier restriction matrix, \(\rho_E(B)=U_E(B)/L_E(B)\), and \(D_E(B)\) is its absolute determinant. The set-level quantities are
\[
L(E)=\max_B L_E(B),\quad
U(E)=\min_B U_E(B),\quad
\rho(E)=\min_B\rho_E(B),\quad
D(E)=\max_BD_E(B).
\]
Only two-point subsets are classified here.

## Proof
Translation of \(E\) does not change any of the four set-level quantities, so take
\[
E=\{0,d\}.
\]
Likewise, multiplying both characters in a candidate partner \(B=\{\chi_0,\chi_1\}\) by \(\chi_0^{-1}\) changes the Fourier matrix only by unitary diagonal factors. Thus it suffices to write
\[
B=\{1,\psi\}.
\]
Set
\[
\zeta=\psi(d).
\]
Because \(d\) has order \(m\), \(\zeta\) is an \(m\)-th root of unity. Conversely every \(m\)-th root occurs. Indeed, the evaluation map
\[
\operatorname{ev}_d:\widehat G\to\mathbb C^\times,\qquad
\psi\mapsto\psi(d)
\]
has kernel consisting of the characters that are trivial on \(\langle d\rangle\). Those characters are exactly the characters of \(G/\langle d\rangle\), so the kernel has size \(|G|/m\). Since \(|\widehat G|=|G|\), the image has size \(m\), and therefore equals the full group of \(m\)-th roots of unity.

After the above unitary normalizations, the Fourier matrix is
\[
T_\zeta=
\begin{pmatrix}
1&1\\
1&\zeta
\end{pmatrix}.
\]
Its Gram matrix is
\[
T_\zeta^*T_\zeta=
\begin{pmatrix}
2&1+\zeta\\
1+\overline\zeta&2
\end{pmatrix},
\]
so the squared singular values are
\[
2-|1+\zeta|\quad\text{and}\quad 2+|1+\zeta|.
\]
Thus
\[
L_E(B)=2-|1+\zeta|,\qquad
U_E(B)=2+|1+\zeta|,
\]
\[
\rho_E(B)=\frac{2+|1+\zeta|}{2-|1+\zeta|},
\qquad
D_E(B)=|1-\zeta|.
\]
Write \(\zeta=e^{2\pi i k/m}\). Then
\[
|1+\zeta|=2|\cos(\pi k/m)|,\qquad
|1-\zeta|=2|\sin(\pi k/m)|.
\]
All four set-level optimizations therefore reduce to choosing an \(m\)-th root closest to \(-1\). If \(m\) is even, \(-1\) itself is available and the minimum of \(|\cos(\pi k/m)|\) is \(0\). If \(m\) is odd, the two closest exponents are
\[
k=(m-1)/2,\qquad k=(m+1)/2,
\]
and the minimum is
\[
\sin(\pi/(2m)).
\]
The displayed formulas for \(L(E)\), \(U(E)\), and \(\rho(E)\) follow immediately. At the same optimizing exponents,
\[
|1-\zeta|=2\sqrt{1-c_m^2},
\]
which gives the formula for \(D(E)\).

Finally, for odd \(m\), the elementary identity
\[
\frac{1+\sin a}{1-\sin a}
=
\tan^2(\pi/4+a/2)
\]
with \(a=\pi/(2m)\) gives the stated tangent form.

## Verification
The accompanying `verify.py` exhaustively checks every two-point subset and every two-character partner in a collection of cyclic and product groups, including all cyclic groups of orders \(2\) through \(16\), \(\mathbb Z_2^2\), \(\mathbb Z_2\times\mathbb Z_4\), \(\mathbb Z_2\times\mathbb Z_6\), and \(\mathbb Z_3^2\). For each set it recomputes \(L(E)\), \(U(E)\), \(\rho(E)\), and \(D(E)\) from the Fourier restriction matrices and compares them with the closed formulas above. It prints `VERIFY_OK`.

The finite computation is a sanity check only. The proof is analytic and covers every finite abelian group.

## Relationship to prior work
Ferguson--Mayeli--Sothanaphan introduced the tightness quantities and asked for nontrivial lower bounds for \(\rho(E)\) in terms of information about \(E\). Their Proposition 5.1 proves only the asymptotic statement
\[
\rho(E_p)\to1
\]
for two-point subsets of \(\mathbb Z_p^{d_p}\) as the prime \(p\to\infty\). Their Example 5.2 shows that the analogous convergence can fail for composite moduli, using sets whose difference has order \(3\), but it does not give the complete all-group formula. The theorem above replaces both statements, in cardinality two, by an exact invariant depending only on the order of the difference. In particular, Example 5.2 has the exact constant
\[
\rho(E)=3.
\]

Targeted searches for the exact formula, its tangent form, and an order-of-difference classification did not locate a covering statement in the checked literature or in the semantic findings database.

## Limitations
This theorem does not classify three-point or larger sets. It also does not provide a lower bound for \(\rho(E)\) from coarse geometric information that applies uniformly across all cardinalities. The originality check was targeted rather than exhaustive; differently phrased or non-indexed literature remains a residual risk.

## References
1. S. Ferguson, A. Mayeli, and N. Sothanaphan, "Riesz bases of exponentials and multi-tiling in finite abelian groups," arXiv:1904.04487, first posted 9 April 2019.
