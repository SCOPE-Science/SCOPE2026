# Sharp centered \(\ell^2\) maximal norm and twelve extremizer rays on the six-cycle

## Finding

Let \(C_6\) be the unweighted six-cycle with vertices \(0,1,\ldots,5\), read modulo six, and counting measure. For the centered graph-ball Hardy–Littlewood maximal operator \(M\), the sharp, attained strong norm is
\[
\boxed{\|M\|_{\ell^2(C_6)\to\ell^2(C_6)}=\sqrt{\lambda_*}=1.233045384931315\ldots,}
\]
where \(\lambda_*=1.520400921300415\ldots\) is the unique real root above \(1517/1000\) of
\[
P(z)=24300z^5-73710z^4+68847z^3-20992z^2+2011z-48.
\]
There are precisely **twelve distinct labeled nonnegative extremizing rays**, a single orbit under the dihedral automorphism group of \(C_6\). All nonzero real extremizers arise from these rays by arbitrary independent coordinate signs and positive scaling.

A representative nonnegative extremizer \(v\), normalized by \(v_0=1\), has coordinates
\[
(v_0,v_1,v_2,v_3,v_4,v_5)\approx
(1,0.204881134027,0.204881134027,0.101855511106,
0.699000817265,0.181094290052).
\]
In particular, its two adjacent coordinates \(v_1=v_2\) coincide, while its unique maximum is at vertex \(0\). The exact coordinates are supplied below by rational polynomials evaluated at \(\lambda_*\).

## Assumptions and scope

Distances are shortest-path distances on the simple cycle; balls are **closed** balls \(B(i,r)=\{j:\operatorname{dist}(i,j)\le r\}\). For every real function \(f\) on the six vertices,
\[
M f(i)=\max_{r\in\{0,1,2,3\}}\frac1{|B(i,r)|}\sum_{j\in B(i,r)}|f(j)|,
\qquad \|f\|_2^2=\sum_{i=0}^5|f(i)|^2.
\]
The four ball sizes at every vertex are \(1,3,5,6\). No weights or degree-normalized averages are used. The theorem makes no assertion about other cycle lengths or \(\ell^p\) exponents.

## Proof

**Finite linearization.** For each choice \(r=(r_0,\ldots,r_5)\in\{0,1,2,3\}^6\), let \(A_r\) have row \(i\) equal to the uniform average on \(B(i,r_i)\). All entries are nonnegative. Every nonnegative \(x\) satisfies \(\|Mx\|_2^2=\max_r\|A_rx\|_2^2\). Conversely, a nonnegative top singular vector exists for every \(A_r\), since \(A_r^{\mathsf T}A_r\) is entrywise nonnegative. Consequently,
\[
\|M\|_{2\to2}^2=\max_{r\in\{0,1,2,3\}^6}
\lambda_{\max}(A_r^{\mathsf T}A_r).
\]
This identity is an exact reduction, with no sampling assumption.

**Exhaustive strict bound.** Put \(B_r=30A_r\), an integer matrix, and \(Q_r=B_r^{\mathsf T}B_r\). With \(q=1517/1000\), the integer symmetric matrix
\[
T_r=13653I_6-10Q_r=9000\bigl(qI_6-A_r^{\mathsf T}A_r\bigr)
\]
is positive definite for exactly **4084** of the \(4^6=4096\) radius selections. The exact verification computes all six leading principal minors by fraction-free Sylvester elimination; for every reported positive-definite selection, all pivots are strictly positive. The remaining **12** selections are exactly the dihedral images of
\[
r_*=(0,1,2,3,0,1).
\]
The executable complete certificate is `verify_c6.py` (standard Python 3, no dependencies). In particular, every nonexceptional selection has squared singular norm strictly less than \(1517/1000\).

**Exceptional spectrum.** For \(r_*\), the six rows of \(B_{r_*}\) are
\[
\begin{pmatrix}
30&0&0&0&0&0\\
10&10&10&0&0&0\\
6&6&6&6&6&0\\
5&5&5&5&5&5\\
0&0&0&0&30&0\\
10&0&0&0&10&10
\end{pmatrix}.
\]
The exact characteristic polynomial is
\[
\det(zI_6-Q_{r_*}/900)=\frac{zP(z)}{24300}.
\]
The shifted polynomial \(P(y+1517/1000)\) has a strictly negative constant coefficient and strictly positive coefficients at every higher degree. Descartes' rule of signs therefore gives exactly one real root above \(1517/1000\). Direct exact-rational substitution proves
\[
\frac{15204009213}{10^{10}}<\lambda_*<\frac{15204009214}{10^{10}}.
\]
Since the exceptional Gram matrix is entrywise positive, the top eigenvalue is simple and its eigenvector has strictly positive entries.

**Exact extremizer and active balls.** Define \(p_j(z)\) by
\[
\begin{aligned}
p_0(z)&=72900z^4-127089z^3+51336z^2-5617z+142,\\
p_1(z)=p_2(z)&=13041z^3-16569z^2+2255z-71,\\
p_3(z)&=4941z^3-5346z^2+233z+52,\\
p_4(z)&=13041z^3-3852z^2+149z-2,\\
p_5(z)&=10125z^3-13572z^2+3641z-122.
\end{aligned}
\]
Then \(v_j=p_j(\lambda_*)/p_0(\lambda_*)\). Polynomial division modulo \(P\) verifies exactly that \(Q_{r_*}v=900\lambda_*v\). Exact rational interval bounds on the displayed isolating interval establish both \(p_j(\lambda_*)>0\) for every \(j\) and all **18** strict inequalities
\[
\frac1{|B(i,r_{*,i})|}\sum_{j\in B(i,r_{*,i})}v_j
>
\frac1{|B(i,s)|}\sum_{j\in B(i,s)}v_j,
\qquad i=0,\ldots,5,\quad s\ne r_{*,i}.
\]
Thus \(Mv=A_{r_*}v\) and \(\|Mv\|_2^2=\lambda_*\|v\|_2^2\). Because \(\lambda_*>q\), this one selection beats every nonexceptional one; dihedral symmetry treats the other eleven.

Finally, every extremizer must maximize a singular Rayleigh quotient for an exceptional \(A_r\), hence must lie on that selection's unique nonnegative Perron ray (after taking coordinatewise absolute values). The twelve rays are distinct: \(v_0\) is the unique maximum, and its two neighboring values \(v_1\) and \(v_5\) are unequal. Therefore no nonidentity dihedral symmetry fixes this ray. Independent input signs do not change \(Mf\). This proves the complete equality classification.

## Verification

Execute `python verify_c6.py` with Python 3. The checker constructs every ball from the graph distance, tests all 4096 selection matrices by exact integer arithmetic, identifies the twelve-element exceptional orbit, computes the exact characteristic polynomial, isolates the unique relevant quintic root, verifies the polynomial eigenvector identity, and certifies the 18 strict active-ball inequalities using rational derivative bounds. Its success marker is

`CERTIFICATE_OK selections=4096 strict=4084 exceptional=12 characteristic_quintic=exact root_isolation=exact eigenvector=exact active_selection_tests=18`

The listed finite exhaustion is complete because each vertex has exactly four different closed balls, giving exactly \(4^6\) choices; it is not statistical evidence. The infinite mathematical assertion here is only universal quantification over real input vectors of this fixed six-dimensional space, discharged by the spectral reduction and exhaustive certificate.

## Relationship to prior work

Soria and Tradacete introduced systematic graph-ball maximal-operator estimates, including sharp results in ranges at most \(\ell^1\) and on special graph families [1]. González-Riquelme and Madrid established strong \(\ell^2\) norm formulas for complete graphs and stars [2]. González-Riquelme, Kovač and Madrid examined sharp **variation** bounds, including finite graphs of at most five vertices [3]. These statements do not imply the six-cycle strong \(\ell^2\) norm: variation controls graph gradients rather than the full counting-measure Hilbert norm, while complete graphs and stars have different ball families. Existing exact results for centered strong \(\ell^2\) norms on the four- and five-cycles do not cover the first diameter-three cycle, whose four local ball radii create a different selection geometry.

The value here is an exact natural invariant and equality classification for the smallest diameter-three cycle. It is not a general formula for all cycles. Undiscovered or unindexed equivalent computations remain a possible priority risk.

## Limitations

The graph is precisely the unit-edge six-cycle with counting measure; only centered, unweighted graph-ball averages and real \(\ell^2\) are treated. The proof does not yield exact norms for longer even cycles, weighted graphs, uncentered maximal operators or other exponents. Computational evidence is an **exhaustive exact certificate** for this particular finite operator family, not an independent external validation. Publication priority is not established absolutely.

## References

[1] J. Soria and P. Tradacete, *Best constants for the Hardy-Littlewood maximal operator on finite graphs*, first public 2014-10-22, arXiv:1410.6204, https://arxiv.org/abs/1410.6204.

[2] C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, first public 2020-05-06, arXiv:2005.03146, https://arxiv.org/abs/2005.03146.

[3] C. González-Riquelme, V. Kovač, and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, first public 2026-03-12, arXiv:2603.12462, https://arxiv.org/abs/2603.12462.
