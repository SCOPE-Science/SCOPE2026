# The last harmonic interpolation gap on the 31 icosahedral symmetry axes

## Finding
Let \(X\subset S^2\) be the union of all thirty-one antipodal axes of a regular icosahedron: six vertex axes, ten face-center axes and fifteen edge-midpoint axes. For each integer \(k\ge0\), let \(E_k\) evaluate the real spherical harmonics of **exact degree** \(k\) at all sixty-two endpoints of these axes, and put \(r_k=\operatorname{rank}E_k\).

The complete evaluation-rank sequence is as follows. For \(0\le k\le28\), the ranks in increasing order are
\[
(r_0,\ldots,r_{28})=(1,3,5,7,9,11,10,15,14,19,15,18,19,22,19,22,24,25,24,25,29,25,29,28,29,28,29,28,29).
\]
For \(29\le k\le74\), the only degrees where \(r_k<31\) are

| \(r_k\) | Degrees \(k\) |
|---|---|
| \(28\) | \(33\) |
| \(29\) | \(32,34,38,44\) |
| \(30\) | \(30,36,40,42,46,48,50,52,54,56,58,62,64,68,74\) |

At every other degree \(k\ge29\), including **every degree \(k\ge75\)**, the rank is \(31\). Thus
\[
\boxed{\min\{k:r_k=31\}=29,\qquad \min\{K:\forall k\ge K,\ r_k=31\}=75.}
\]
Since the sixty-two endpoints form thirty-one antipodal pairs, maximal exact-degree rank is \(31\): arbitrary data can be interpolated only when they satisfy the forced parity \(f(-x)=(-1)^kf(x)\). The degree-\(74\) deficiency is exactly one-dimensional, and degree \(75\) begins permanent parity-compatible interpolation.

## Assumptions and scope
Set \(\varphi=(1+\sqrt5)/2\). Take the twelve (unnormalized) icosahedral vertices
\[
I_0=\{(0,a,b\varphi),(b\varphi,0,a),(a,b\varphi,0):a,b\in\{-1,1\}\}.
\]
Take the twenty dodecahedral face-axis directions
\[
D_0=\{(a,b,c):a,b,c\in\{-1,1\}\}\ \cup\
\{(0,a\varphi,b/\varphi),(b/\varphi,0,a\varphi),(a\varphi,b/\varphi,0):a,b\in\{-1,1\}\}.
\]
Let \(M_0\) comprise the thirty vectors \((u+v)/(2\varphi)\), for unordered pairs \(\{u,v\}\subset I_0\) satisfying \(\|u-v\|^2=4\). Every element of \(M_0\) is a unit vector. The set \(X\) is the union of \(I_0/\sqrt{\varphi+2}\), \(D_0/\sqrt3\), and \(M_0\). The three orbits have \(12,20,30\) members and comprise \(31\) antipodal pairs. Orientation and overall scale do not affect the result. All ranks are over \(\mathbb R\).

## Proof
Choose one vector \(x_i\) from each antipodal pair. By the spherical harmonic addition theorem, the Gram matrix of degree-\(k\) evaluation is a positive multiple of the Legendre matrix
\[
G_k=\big(P_k(\langle x_i,x_j\rangle)\big)_{i,j=1}^{31},\qquad P_k(1)=1.
\]
Therefore \(r_k=\operatorname{rank}G_k\). The antipodal relation gives the same evaluation rank on all sixty-two nodes.

All Gram ranks are computable in \(F=\mathbb Q(\sqrt5)\) without approximating square roots. Write a representative in raw coordinates \(v_i\) with squared norm \(n_i\in F\), and put \(d_{ij}=v_i\cdot v_j\in F\) and \(z_{ij}=d_{ij}^2/(n_in_j)\in F\). Define polynomials \(A_h,B_h\) by
\[
P_{2h}(t)=A_h(t^2),\qquad P_{2h+1}(t)=tB_h(t^2),\qquad A_0=B_0=1.
\]
The Legendre recurrence yields
\[
A_{h+1}(z)=\frac{(4h+3)zB_h(z)-(2h+1)A_h(z)}{2h+2},
\qquad
B_{h+1}(z)=\frac{(4h+5)A_{h+1}(z)-(2h+2)B_h(z)}{2h+3}.
\]
For even \(k=2h\), the entries of \(G_k\) are \(A_h(z_{ij})\in F\). For odd \(k=2h+1\), congruence by the positive diagonal matrix with entries \(\sqrt{n_i}\) transforms \(G_k\) into the matrix with entries \(d_{ij}B_h(z_{ij})\in F\), preserving rank.

The accompanying standard-library-only `verify.py` constructs every raw direction and performs **exact Gaussian elimination in \(F\)** for the seventy-five degrees \(0\le k\le74\). This gives the complete finite rank table above. It independently constructs the fifteen distinct squared inner-product levels from the stated coordinates and tests the exact maximum
\[
\max_{i\ne j}|\langle x_i,x_j\rangle|^2=\frac12+\frac{\sqrt5}{6}<\frac78.
\]

For every \(75\le k\le1699\), the same checker evaluates the corresponding exact algebraic entries modulo the prime \(10009\) under \(\sqrt5\mapsto4070\), for which \(4070^2\equiv5\pmod{10009}\). Each of the \(1625\) resulting matrices has rank \(31\) modulo the prime. Denominators are invertible, since the Legendre recurrence only divides by positive integers less than \(1702\), and the geometric coordinates have denominators prime to \(10009\). Thus every modular nonzero determinant proves characteristic-zero invertibility.

For \(k\ge1700\), the exact distance bound gives \(\sin\theta_{ij}>7/20\) at every distinct pair. The classical Bernstein inequality
\[
|P_k(\cos\theta)|\le\sqrt{\frac2{\pi k\sin\theta}}
\]
implies, using \(\pi>157/50\), that every off-diagonal absolute row sum of \(G_k\) is strictly less than
\[
30\sqrt{\frac2{(157/50)\,1700\,(7/20)}}<1.
\]
Since the diagonal is identically one, \(G_k\) is strictly diagonally dominant and positive definite. The exact elimination, modular certificates and analytic tail together prove the rank statement for **all** nonnegative integers \(k\).

## Verification
Execute `python3 verify.py` with Python 3 and no third-party dependencies. The script regenerates the 31 nodes, checks coordinate norms and squared separation, calculates all seventy-five exact low-degree ranks, verifies \(10009\) is prime, checks the required finite-field root and tests the invertibility of every degree from \(75\) through \(1699\). It then checks the rational inequality used for the analytic tail. The output marker is `ICOSAHEDRAL_31_AXES_ALL_DEGREE_CERTIFICATE_OK`.

The low-rank elimination is exact arithmetic, not a floating-point threshold. The modular calculation establishes only the specified finite nonvanishing; the Bernstein argument separately covers the infinite tail. The exact-degree result is distinct from cumulative-degree interpolation.

## Relationship to prior work
Bannai, Okuda and Tagami [1] develop harmonic-index spherical designs, Gegenbauer addition kernels and symmetry-induced cancellations. Hughes and Waldron [2] work with the **six plus ten** lines associated with the icosahedral and dodecahedral axes, giving a weighted high-order half-design. Calvo [3] identifies the same **thirty-one** projective axes as the intersections of the fifteen icosahedral mirror lines and studies their invariant plane curves and Waldschmidt constants. These results supply geometry and methods but do not state the present full exact-degree harmonic interpolation sequence or its sharp final gap. Known results about the separate rotational-axis orbits do not determine whether their restrictions are jointly independent at any fixed harmonic degree.

## Limitations
The claim concerns the fixed standard icosahedral axis configuration and single-degree real spherical harmonics, not arbitrary deformations, optimal conditioning, or interpolation without antipodal parity. The result has an exact, reproducible proof package, but no independent mathematical audit. Equivalent older calculations in icosahedral representation theory or cubature could affect originality; in particular, complete texts of some historical symmetrized-harmonics sources were not available for comparison. This remains a historical-coverage uncertainty, not a step used in the proof.

## References
[1] E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1 (first public 2013-08-23), https://arxiv.org/abs/1308.5101.

[2] D. Hughes and S. Waldron, *Spherical half-designs of high order*, available full text, https://www.math.auckland.ac.nz/~waldron/Preprints/Half-designs/half-designs.pdf.

[3] S. Calvo, *The icosahedral line configuration and Waldschmidt constants*, arXiv:2209.01499v1 (first public 2022-09-03), https://arxiv.org/abs/2209.01499.

[4] G. Szegő, *Orthogonal Polynomials*, 4th ed., American Mathematical Society, 1975, §7.3 (Bernstein-type Legendre inequality).
