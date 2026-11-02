# Exact uncentered Hilbert maximal norm on the five-cycle

## Finding

On the unweighted cycle \(C_5\), with five vertices, counting measure, and shortest-path metric balls, the uncentered Hardy–Littlewood maximal operator has the sharp attained strong Hilbert norm

\[
\|\widetilde M\|_{\ell^2\to\ell^2}=\sqrt{\lambda_*}=1.292531070898058\ldots,
\]

where \(\lambda_*\) is the **unique** real root in \((1670/1000,1671/1000)\) of

\[
81z^3-171z^2+62z-4=0.
\]

Write

\[
D_*=81\lambda_*^2-54\lambda_*+4,\qquad
 a_*=(27\lambda_*-2)/D_*,\qquad c_*=(9\lambda_*-2)/D_*.
\]

Every nonzero real extremizer has, up to cyclic rotation, positive scaling and arbitrary independent coordinate signs, the coordinatewise absolute-value pattern

\[
(a_*,1,a_*,c_*,c_*).
\]

Numerically \(a_*=0.308219396369\ldots\) and \(c_*=0.093206372458\ldots\). There are exactly five labeled nonnegative extremizing rays (one for each vertex at which the largest value occurs).

## Assumptions and scope

Identify vertices with \(\mathbb Z/5\mathbb Z\), edges joining residues differing by one. For \(f:V\to\mathbb R\), define

\[
\widetilde M f(v)=\max_{c\in V,\ r\in\{0,1,2\},\ v\in B(c,r)}
\frac{1}{|B(c,r)|}\sum_{w\in B(c,r)}|f(w)|.
\]

Here \(B(c,r)=\{w:d(w,c)\le r\}\), the radius-two ball is the whole vertex set, and no averaging over arbitrary connected arcs or arbitrary subsets is allowed. The strong norm is the supremum of \(\|\widetilde M f\|_2/\|f\|_2\) over nonzero real signals. Input signs are irrelevant to the operator.

For each evaluation vertex \(v\), its five **distinct eligible balls**, in the fixed order used by the checker, are: the singleton \(\{v\}\); the three radius-one balls centered respectively at \(v-1,v,v+1\); and the full five-vertex ball. Thus the independent row selections number exactly \(5^5=3125\).

## Proof

**Linearization.** For every nonnegative input vector \(x\), select independently at each vertex one of its five legal balls and place its average row into a matrix \(A_\sigma\). As all averages are nonnegative,

\[
\|\widetilde M x\|_2^2
=\max_{\sigma\in\{0,1,2,3,4\}^5}\|A_\sigma x\|_2^2.
\]

Consequently, \(\|\widetilde M\|_{2\to2}^2=\max_\sigma\lambda_{\max}(A_\sigma^{\mathsf T}A_\sigma)\). For the reverse inequality implicit in this equality, a nonnegative top singular vector exists for each nonnegative matrix \(A_\sigma\): take absolute values of any maximizing vector, which cannot decrease the output norm.

**Complete exact upper certificate.** Put \(B_\sigma=15A_\sigma\), an integer matrix because every eligible ball has size one, three or five. For any selection, the rational squared-norm bound

\[
\lambda_{\max}(A_\sigma^{\mathsf T}A_\sigma)<5/3
\]

is equivalent to positive definiteness of the integer matrix \(375I-B_\sigma^{\mathsf T}B_\sigma\). By Sylvester's criterion, it suffices to verify all five leading principal determinants are positive. The attached standalone program `check_c5_uncentered.py` constructs the legal balls from the cycle and computes those determinants using **exact integer fraction-free elimination**. Among all 3125 selections exactly 3120 pass. The five failing selections, in vertex order \((0,1,2,3,4)\) and with option indices as specified above, are

\[
(3,0,1,1,3),\quad(1,1,3,3,0),\quad(3,3,0,1,1),\quad
(1,3,3,0,1),\quad(0,1,1,3,3).
\]

These are precisely the rotations of one selection. The program proves this as an exhaustive finite assertion, not by floating-point comparison. No conjecture about longer cycles is needed.

**Exceptional eigenvalue.** The first exceptional matrix is

\[
A=\begin{pmatrix}
1/3&1/3&1/3&0&0\\
0&1&0&0&0\\
1/3&1/3&1/3&0&0\\
0&1/3&1/3&1/3&0\\
1/3&1/3&0&0&1/3
\end{pmatrix}.
\]

Its positive eigenvector necessarily has reflection-symmetric shape \(x=(a,b,a,c,c)\). In these coordinates the restriction of \(A^{\mathsf T}A\) is

\[
R=\frac19\begin{pmatrix}
5&3&1\\6&13&2\\1&1&1
\end{pmatrix}.
\]

The full characteristic polynomial, written for \(H=(3A)^{\mathsf T}(3A)\), is

\[
\det(uI-H)=u(u-2)(u^3-19u^2+62u-36).
\]

The checker verifies this monic degree-five identity by exact determinant evaluation at six distinct integer arguments. The displayed cubic for \(\lambda_*\) follows by \(u=9\lambda_*\). Direct rational sign checks give a root in \((1670/1000,1671/1000)\); its cubic derivative is strictly positive from \(5/3\) onward, so this is the only root above \(5/3\).

Normalize \(b=1\). The first and third eigenvalue equations yield \(a=a_*\) and \(c=c_*\). The second equation is exactly the displayed cubic. Both coordinates are positive in the stated rational interval. The matrix \(A^{\mathsf T}A\) is nonnegative and irreducible, so Perron–Frobenius shows that \(\lambda_*\) is its **simple spectral radius** and \(x=(a_*,1,a_*,c_*,c_*)\) its unique nonnegative top eigenvector up to scale. Each of the four other exceptional matrices is a rotation and has the same eigenvalue.

**Sharpness and all equality cases.** The program performs rigorous rational interval arithmetic in \(\lambda_*\in(1670/1000,1671/1000)\) and verifies, for each vertex, that the row of the displayed exceptional matrix is the **unique** largest permitted average on \(x\). Therefore \(\widetilde M x=Ax\), proving attainment. Any maximizing input must saturate one of the five exceptional spectral bounds: all other row selections lie strictly below \(5/3<\lambda_*\). The top eigenvalue of each exceptional matrix is simple; hence all equality cases are precisely the five rotations of \(x\), with independent signs and positive scale. This proves the stated classification.

## Verification

Run `python3 check_c5_uncentered.py` with Python's standard library; no external package or stored numerical result is used. The expected output is

`CERTIFICATE_OK selections=3125 strict=3120 exceptional=5 characteristic=exact active=20`

The certificate covers every possible row choice, checks all strict upper bounds with integer Sylvester determinants, verifies the exceptional characteristic polynomial, and checks twenty strict average-activity inequalities using rational enclosing intervals. An independent numerical eigenspectrum pass over all 3125 matrices reproduced the same five maximizers, with winning squared norm \(1.670636569236880\ldots\) and next-highest squared norm approximately \(1.642657130281066\); that numerical pass is supplementary and is not used as proof.

## Relationship to prior work

Soria–Tradacete established the finite-graph maximal-operator framework and exact general results at small exponents [1]. González-Riquelme–Madrid [2] computed strong \(\ell^2\) norms for **centered** operators on complete graphs and stars; their paper defines uncentered versions but does not give this five-cycle strong norm. The later González-Riquelme–Kovač–Madrid five-vertex census [3] concerns **centered edge variation**, not uncentered strong \(\ell^2\) norms. The present calculation is a distinct sharp norm and complete extremizer classification for the smallest noncomplete odd cycle. No general theorem or interval bound from these sources implies the exact algebraic constant. Unindexed equivalent calculations remain possible.

## Limitations

This is a five-vertex, unit-edge, counting-measure theorem for graph-metric balls and real \(\ell^2\). It does not determine longer odd-cycle norms, arbitrary metric intervals, weights, exponents other than two, or graph families. The computation is a **finite exhaustive proof for this fixed graph**, not an infinite-family claim. Publication priority remains subject to unindexed work and external expert examination; independent validation has not been performed.

## References

[1] J. Soria and P. Tradacete, *Best constants for the Hardy-Littlewood maximal operator on finite graphs*, initial public arXiv version dated 22 October 2014, arXiv:1410.6204, https://arxiv.org/abs/1410.6204.

[2] C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146, https://arxiv.org/abs/2005.03146.

[3] C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy-Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462, https://arxiv.org/abs/2603.12462.
