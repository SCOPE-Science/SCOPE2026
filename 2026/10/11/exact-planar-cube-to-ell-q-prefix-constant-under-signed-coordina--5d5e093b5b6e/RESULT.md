# Exact planar cube-to-\(\ell_q\) prefix constant under signed coordinate permutations

## Finding
For every \(1\le q\le\infty\), let \(\mathcal P_q\) be the least constant such that every finite sequence \(v_1,\ldots,v_m\in B_\infty^2\) admits signs \(\varepsilon_i\in\{-1,1\}\) and coordinate permutations \(\sigma_i\in S_2\) with
\[
\left\|\sum_{i=1}^k \varepsilon_i\sigma_i(v_i)\right\|_q\le \mathcal P_q
\qquad(1\le k\le m).
\]
Then
\[
\mathcal P_q=2
\qquad\text{for every }1\le q\le\infty.
\]
Moreover, the choices can be made online, using only the current vector and the current partial sum.

## Assumptions and scope
The input vectors lie in the planar cube \(B_\infty^2=[-1,1]^2\). At each step the allowed operation is exactly a common sign followed by one of the two coordinate permutations. The target norm is the usual \(\ell_q^2\) norm for \(1\le q<\infty\), and the max norm for \(q=\infty\). No assumption is made on the sequence length, and no look-ahead is needed.

The recent source arXiv:2610.02127v1 introduces signed-coordinate-permutation prefix balancing and proves, for general dimension and exponents, the explicit bound
\[
R_{n,q}C_{n,p}+n^{1/q-1/p}.
\]
For \(n=2\) and \(p=\infty\), this equals \(2^{1+1/q}\) when \(q<\infty\), while the \(q=\infty\) endpoint equals \(2\). The finding above determines the exact constant simultaneously for all target exponents.

## Proof
Write one input vector as \(v=(a,b)\) and introduce diagonal coordinates
\[
m=\frac{a+b}{2},
\qquad
d=\frac{a-b}{2}.
\]
The elementary identity
\[
|m|+|d|=
\frac{|a+b|+|a-b|}{2}=
\max\{|a|,|b|\}
\]
shows that \(v\in B_\infty^2\) implies \(|m|\le1\) and \(|d|\le1\).

The four possible signed-permutation images of \(v\) are exactly
\[
(\alpha m+\beta d,\alpha m-\beta d),
\qquad \alpha,\beta\in\{-1,1\}.
\]
Indeed, \((\alpha,\beta)=(1,1)\) is \((a,b)\), \((1,-1)\) is \((b,a)\), and the remaining two choices are their negatives. Thus the common sign and the coordinate swap become two independent signs in the \((m,d)\) coordinates.

For the sequence \(v_i\), let
\[
M_k=\sum_{i=1}^k\alpha_i m_i,
\qquad
D_k=\sum_{i=1}^k\beta_i d_i.
\]
Choose \(\alpha_k\) so that \(M_{k-1}\alpha_km_k\le0\), and independently choose \(\beta_k\) so that \(D_{k-1}\beta_kd_k\le0\). Then
\[
|M_k|\le\max\{|M_{k-1}|,|m_k|\},
\qquad
|D_k|\le\max\{|D_{k-1}|,|d_k|\}.
\]
Starting from \(M_0=D_0=0\), induction gives \(|M_k|,|D_k|\le1\) for every prefix.

The corresponding prefix in the original coordinates is
\[
(M_k+D_k,M_k-D_k).
\]
For fixed \(q\), the map
\[
(M,D)\longmapsto\|(M+D,M-D)\|_q
\]
is convex. Every point of \([-1,1]^2\) is a convex combination of its four vertices, and every vertex is sent to one of \((\pm2,0)\) or \((0,\pm2)\), each having \(\ell_q\)-norm \(2\). Hence every prefix has norm at most \(2\). This proves \(\mathcal P_q\le2\), with an online construction.

For sharpness take the two inputs
\[
v_1=(1,1),
\qquad
v_2=(1,-1).
\]
The first signed-permutation orbit is \(\{(1,1),(-1,-1)\}\), while the second is \(\{(1,-1),(-1,1)\}\). Whatever choices are made, the second prefix is one of \((\pm2,0)\) or \((0,\pm2)\), so its \(\ell_q\)-norm is exactly \(2\). Therefore \(\mathcal P_q\ge2\), completing the proof.

## Verification
The group-action step was checked directly: the four pairs \((\alpha,\beta)\in\{-1,1\}^2\) give exactly the four allowed signed-permutation images. The scalar greedy inequality is exact and inductive, not experimental. The target-norm bound follows from convexity on the transformed square, whose four vertices all have image norm \(2\). The lower witness exhausts the two available projective images of each of its two vectors and forces norm \(2\) at the second prefix.

No finite computation is used as a substitute for the universal proof.

## Relationship to prior work
Niles-Weed, Sadovsky, and Shkrob, arXiv:2610.02127v1, introduce this signed-permutation prefix problem. Their Theorem 9 gives the general \(B_p^n\)-to-\(\ell_q\) bound \(R_{n,q}C_{n,p}+n^{1/q-1/p}\). At \(n=2,p=\infty\), their displayed constants give \(2^{1+1/q}\) for finite \(q\) and \(2\) for \(q=\infty\). The present finding supplies the exact value \(2\) for every finite \(q\) as well, by exploiting the special two-dimensional signed-permutation action in diagonal coordinates.

Lund and Magazinov, arXiv:1510.04536v1, prove that the sign-sequence constant of every normed plane is at most \(2\), and note sharpness for the planar max norm. That theorem measures both inputs and partial sums in the same norm. Applied directly to the planar max norm and then compared with \(\ell_q\), it yields only the weaker cross-norm estimate \(2^{1+1/q}\) for finite \(q\); it does not imply the exact cross-norm constant above. Reis and Rothvoss, arXiv:2007.05634, study \(\ell_p\)-to-\(\ell_q\) vector balancing with signs but without the extra coordinate-permutation action and do not give this exact planar prefix constant.

## Limitations
The theorem is specific to dimension two and to cube-bounded inputs \(B_\infty^2\). It does not determine the exact constants for \(B_p^2\) with finite \(p\), nor does it extend the value \(2\) to higher-dimensional cube inputs. The originality comparison cannot exclude an unindexed historical cross-norm formulation, although the checked same-object and alias searches did not locate one.

## References
1. Jonathan Niles-Weed, Shay Sadovsky, Jacob Shkrob, *An optimal constant for vector balancing with permutations*, arXiv:2610.02127v1, first public 2026-10-01.
2. Ben Lund, Alexander Magazinov, *The sign-sequence constant of the plane*, arXiv:1510.04536v1.
3. Victor Reis, Thomas Rothvoss, *Vector Balancing in Lebesgue Spaces*, arXiv:2007.05634.
