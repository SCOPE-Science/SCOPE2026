# The exact Hilbert norm of centered maximal averaging on the five-cycle

## Finding
Let \(C_5\) have vertices \(0,1,2,3,4\), with adjacency modulo five, and define the centered graph Hardy–Littlewood maximal operator on real data by
\[
(Mf)(i)=\max_{r\in\{0,1,2\}}\frac{1}{|B(i,r)|}\sum_{j\in B(i,r)}|f(j)|.
\]
The sharp strong Hilbert-space inequality is
\[
\boxed{\ \|Mf\|_{\ell^2(C_5)}\le\sqrt{\Lambda}\,\|f\|_{\ell^2(C_5)},\quad
225\Lambda^3-390\Lambda^2+91\Lambda-4=0,\quad
\Lambda\in(1463/1000,1467/1000).\ }
\]
Here \(\Lambda=1.465662645093\ldots\), so the sharp norm is \(1.210645548909\ldots\). The equality moduli, up to positive scaling and cyclic relabeling, are exactly
\[
(|f(0)|,\ldots,|f(4)|)=(1,b,1,c,c),\quad
b=1-\Lambda^{-1},\quad c=\frac{4+2b}{25\Lambda-4}.
\]
Signs are arbitrary since the maximal operator uses \(|f|\). At every such extremizer the uniquely maximizing averaging radii, starting at vertex zero, are \((0,1,0,2,2)\). This includes all three possible radii.

## Assumptions and scope
The graph is precisely the simple unweighted cycle with five vertices. Each ball average uses counting measure, including its center; the input can be any real or complex-valued function, with complex phases arbitrary at equality. The norm is the strong \(\ell^2\)-to-\(\ell^2\) norm, not the edge-variation seminorm, weak-type norm, or uncentered maximal operator. The three ball radii are all possible radii because \(C_5\) has diameter two.

## Proof
**Reduction to finitely many matrices.** For a vector of nonnegative values \(x=|f|\), choose separately at each vertex the radius realizing its maximal average. For \(\rho\in\{0,1,2\}^5\), let \(A_\rho\) be the matrix whose \(i\)-th row is the normalized indicator of \(B(i,\rho_i)\). Since the choices at the five vertices are independent,
\[
\|Mf\|_2^2=\max_{\rho\in\{0,1,2\}^5}\|A_\rho x\|_2^2.
\]
Every \(A_\rho\) has nonnegative entries; hence \(\|A_\rho\|_{2\to2}\) is attained by some nonnegative \(x\) (replace any maximizing vector by its absolute values). It follows, in both directions, that
\[
\|M\|_{2\to2}^2=\max_\rho\lambda_{\max}(A_\rho^{\mathsf T}A_\rho).
\]

**A complete exact separation certificate.** Dihedral rotation and reversal identify the 243 radius patterns into precisely 39 classes. Put \(\rho_*=(0,1,0,2,2)\) and \(q=1463/1000\). Every entry of \(15A_\rho\) is an integer; call this integer matrix \(D_\rho\). For all 38 dihedral classes other than that of \(\rho_*\), the five leading principal minors of
\[
S_\rho=329175I-1000D_\rho^{\mathsf T}D_\rho
=225000\bigl(qI-A_\rho^{\mathsf T}A_\rho\bigr)
\]
are strictly positive. Sylvester's criterion gives \(\|A_\rho\|_{2\to2}^2<q\) for every such class. The accompanying dependency-free integer checker explicitly enumerates all 243 patterns, constructs every dihedral orbit, confirms their 39-class partition and checks all 190 principal determinants by exact Bareiss elimination. Its loops and integer matrices constitute a fully specified exhaustive finite certificate, not a sample of cases.

For \(\rho_*\), take the rational witness \(w=(7,2,7,1,1)\). Direct exact arithmetic gives
\[
\frac{\|A_{\rho_*}w\|_2^2}{\|w\|_2^2}=\frac{17141}{11700}>q.
\]
Thus no other radius pattern can attain the maximal norm, apart from rotations and reversals of \(\rho_*\). The optimal pattern has five distinct translates.

**Exact eigenvalue.** For \(\rho_*\), the averaging matrix is
\[
A_*=
\begin{pmatrix}
1&0&0&0&0\\
1/3&1/3&1/3&0&0\\
0&0&1&0&0\\
1/5&1/5&1/5&1/5&1/5\\
1/5&1/5&1/5&1/5&1/5
\end{pmatrix}.
\]
Reflection exchanging \(0\leftrightarrow2\) and \(3\leftrightarrow4\) splits the space into a three-dimensional even subspace, a one-dimensional antisymmetric mode of singular value one, and a one-dimensional kernel. In the orthonormal even basis
\(\bigl((e_0+e_2)/\sqrt2,e_1,(e_3+e_4)/\sqrt2\bigr)\), the averaging matrix restricts to
\[
B=\begin{pmatrix}
1&0&0\\
\sqrt2/3&1/3&0\\
2/5&\sqrt2/5&2/5
\end{pmatrix}.
\]
A direct determinant calculation gives
\[
\det(zI-B^{\mathsf T}B)=z^3-\frac{390}{225}z^2+\frac{91}{225}z-\frac4{225}.
\]
The cubic is negative at \(q\) and positive at \(1467/1000\), while its derivative and second derivative are positive for \(z\ge q\); hence it has exactly one root above \(q\), which is \(\Lambda\). The remaining eigenvalues are smaller than \(q\) or equal to one or zero. This proves the exact norm.

**Every extremizer.** All entries of \(A_*^{\mathsf T}A_*\) are strictly positive (the final two rows of \(A_*\) are uniform), so Perron–Frobenius makes its top eigenvector unique up to positive scaling and strictly positive. Reflection forces it to be \((a,b',a,c',c')\). Writing \(s=(2a+b')/3\) and \(t=(2a+b'+2c')/5\), the eigenvalue equations yield \(\Lambda(a-b')=a\), \(\Lambda(b'-c')=s/3\), and \((25\Lambda-4)c'=4a+2b'\). Therefore \(a>b'>c'>0\), and the displayed formula follows after normalization \(a=1\). These strict inequalities show that the selected radii are uniquely optimal: radius zero at \(0,2\), radius one at \(1\), and radius two at \(3,4\). The other four extremizer families are obtained by dihedral relabeling (which here reduces to cyclic translation). Arbitrary coordinate phases are allowed because the input is replaced by its absolute value.

## Verification
Run `python3 check_C5.py` using only Python's standard library. The code enumerates all radius assignments; verifies the orbit count and partition; verifies exact positive definiteness for every competing class; checks the rational witness; and reconstructs the optimal characteristic coefficients by Newton's trace identities. The run completed with the printed status `PASS: 243 patterns; 39 dihedral classes; 1 top class of size 5;` and exact integer certificates. The proof explains why those finite checks exhaust all possible radius choices; floating-point eigenvalues serve only as descriptive approximations.

## Relationship to prior work
Soria and Tradacete (arXiv:1410.6204, public 2014-10-22) developed the finite-graph centered maximal-operator framework and gave general bounds and exact results for complete/star graphs in specified regimes. González-Riquelme and Madrid (arXiv:2005.03146, public 2020-05-06) determined sharp strong Hilbert norms for complete graphs and stars, but their stated graph families do not include the five-cycle. González-Riquelme, Kovač and Madrid (arXiv:2603.12462, public 2026-03-12) analyze edge-variation inequalities, including a census on five-vertex graphs; their optimization functional is different from the strong Hilbert norm determined here. The distinct published five-cycle Lipschitz-free numerical-index result does not imply a centered-averaging norm. The finite matrix/spectral reduction is elementary and is not itself asserted novel. The new mathematical assertion is the explicit cubic, its strict global radius-mask comparison, and the full extremizer classification on the natural first nontrivial odd cycle.

## Limitations
This statement determines exactly one graph's sharp constant and does not yield closed formulas for longer odd cycles or for other \(\ell^p\) exponents. Exact finite arithmetic proves the five-vertex case, not any infinite-family claim. Priority remains provisional because the literature search cannot exclude an equivalent result under different terminology. Independent mathematical and bibliographic assessment has not been performed.

## References
1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (first public version 2014-10-22), https://arxiv.org/abs/1410.6204.
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (first public version 2020-05-06), https://arxiv.org/abs/2005.03146.
3. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462 (first public version 2026-03-12), https://arxiv.org/abs/2603.12462.
