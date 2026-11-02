# Sharp universal Fourier sampling stability on proper colourings of cycles

## Finding

Let \(n\ge3\) and \(q\ge3\) be integers. Let \(\mathcal C_{n,q}\) be the nonempty set of proper colourings \(x\in(\mathbb Z/q\mathbb Z)^n\) of the cyclic graph \(C_n\), so \(x_i\ne x_{i+1}\) with indices modulo \(n\). Equip \(\mathcal C_{n,q}\) with uniform probability. Restrict to this set the constant \(1\) and the \(n(q-1)\) first-coordinate additive characters \(\chi_{i,t}(x)=\exp(2\pi\mathrm i t x_i/q)\), where \(1\le i\le n\) and \(1\le t<q\). Write \(G_{n,q}\) for their probability-normalized Hermitian Gram matrix.

Put \(a=q-1\), \(s=(-1)^n\), \(Z=a^n+as\), and \(H=(a^n-s)/Z\). For \(0\le k<n\), define
\[
\lambda_0=H\frac{a-1}{a+1}+\frac{n(a-1)s}{Z},\qquad
\lambda_k=H\frac{a^2-1}{a^2+1+2a\cos(2\pi k/n)}\quad(1\le k<n).
\]
Then the **complete eigenvalue multiset** of \(G_{n,q}\) consists of \(1\) once and each \(\lambda_k\) repeated \(q-1\) times; coincident values have added multiplicities. The frame is injective except when \((n,q)=(3,3)\), when its Gram nullity is exactly \(2\).

In every nonsingular case, its sharp squared coefficient-to-sample condition number is \(\kappa_{n,q}^2=\max_k\lambda_k/\min_k\lambda_k\). The extra constant Gram eigenvalue \(1\) lies between these extrema, because the spatial block has trace \(n\). Its optimal universal bound is
\[
\boxed{\sup_{q\ge3,\ n\ge3,\ (n,q)\ne(3,3)}\kappa_{n,q}^2=\frac32(4+\sqrt5),}
\]
with equality **only** at \((n,q)=(5,3)\). For every \(q\ge4\), \(\kappa_{n,q}^2\le(q/(q-2))^2\le4\); the second inequality is an equality only for \(q=4\), and the first is attained among finite \(n\) exactly for \((n,q)=(3,4)\). For fixed \(q\ge3\), \(\lim_{n\to\infty}\kappa_{n,q}^2=(q/(q-2))^2\).

There is also an exact locality statement: if \(R\) is the \(n\times n\) spatial covariance block on any nontrivial colour-frequency character, \(S\) cyclically shifts \(\mathbb C^n\), \(P=\mathbf1\mathbf1^{*}/n\), and \(G_{n,q}\) is nonsingular, then
\[
R^{-1}=\frac{Z}{(a^n-s)(a^2-1)}\bigl((a^2+1)I+a(S+S^{-1})\bigr)
+\left(\lambda_0^{-1}-\frac{Z(a+1)^2}{(a^n-s)(a^2-1)}\right)P.
\]
Thus the precision matrix is exactly nearest-neighbour cyclic plus one constant-mode correction.

## Assumptions and scope

The cycle has distinct vertices and \(n\ge3\); the colour alphabet is the additive cyclic group of size \(q\), not necessarily prime. The colouring constraint uses inequality, so it is invariant under all colour permutations. The sampling measure assigns equal probability \(1/Z\) to each proper colouring, with \(Z=(q-1)^n+(q-1)(-1)^n\). All Gram norms use this probability normalization; the condition number refers to the full restriction operator; adding its orthogonal constant column does not change the extremal Gram eigenvalues. The isolated binary case \(q=2\) is excluded: only even cycles admit proper binary colourings, with two alternating colourings and a highly singular first band.

## Proof

**1. Exact moments and colour separation.** Put \(T=J-I\), the \(q\times q\) matrix whose entries indicate distinct colours. Its eigenvalues are \(a=q-1\) on constants and \(-1\) on the \((q-1)\)-dimensional orthogonal complement. Thus \(\operatorname{tr}(T^n)=Z\), and
\[(T^d)_{uu}=\frac{a^d+(q-1)(-1)^d}{q}.\]
For vertices at cyclic separation \(d\), the probability of equal colours is
\[
P_d=\frac{q(T^d)_{uu}(T^{n-d})_{uu}}{Z}.
\]
Every single colour is uniform, and the joint colour law is invariant under the full colour-permutation group. Consequently different nontrivial additive colour characters are orthogonal, and the common covariance of the same character at separation \(d\) is \(r_d=(qP_d-1)/(q-1)\), namely
\[
r_d=\frac{(-1)^d a^{n-d}+(-1)^{n-d}a^d+(q-2)(-1)^n}{Z}.
\]
The constant character is orthogonal to all the others. The remaining Gram matrix splits as \(q-1\) identical real circulants \(R=(r_{j-i\bmod n})\).

**2. Spatial Fourier spectrum.** A spatial mode \(v_k(j)=\exp(2\pi\mathrm i kj/n)\) has eigenvalue \(\sum_{d=0}^{n-1}r_d\exp(-2\pi\mathrm i kd/n)\). For \(k\ne0\), the final constant term of \(r_d\) vanishes on summing. The two remaining geometric sums, with \(z=\exp(-2\pi\mathrm i k/n)\) and \(D=a^n-s\), combine as
\[
\frac{D}{Z}\left(\frac a{a+z}-\frac1{1+az}\right)
=\frac{D(a^2-1)}{Z(a^2+1+a(z+z^{-1}))}.
\]
For \(k=0\), add the surviving constant-term contribution \(n(q-2)s/Z\). This yields all displayed eigenvalues, multiplicities and the precision identity: invert each nonconstant spatial frequency and correct the constant frequency by a rank-one projector.

**3. Positivity and its only exception.** For \(q\ge3\), \(a\ge2\), so \(H>0\), the denominators of \(\lambda_k\) for \(k\ne0\) are at least \((a-1)^2>0\), and all these modes are positive. For even \(n\), \(\lambda_0>0\). For odd \(n\), writing \(B=(a-1)/(a+1)\) gives
\[\lambda_0=HB\left(1-\frac{n(a+1)}{a^n+1}\right).\]
The parenthesis vanishes for \((a,n)=(2,3)\), and is strictly positive for every other odd \(n\ge3\): at \(n=3\) use \(a\ge3\), and at \(n\ge5\) use \(a\ge2\) and \(a^n+1>n(a+1)\). Hence the nullity is exactly \(q-1=2\) at the sole exception.

**4. Global upper bound.** Let \(B=(a-1)/(a+1)\). The nonconstant spatial modes lie in \([HB,H/B]\). If \(n\) is even, \(\lambda_0\ge HB\), and also \(\lambda_0\le H/B\): after clearing positive denominators the latter follows from \(n(a-1)^2(a+1)\le4a(a^n-1)\), itself a consequence of \(a^n-1=(a-1)\sum_{j=0}^{n-1}a^j\ge n a(a-1)\) for \(n\ge3\). Thus \(\kappa_{n,q}^2\le B^{-2}\), strictly for finite even \(n\).

For odd \(n\), the smallest mode is \(\lambda_0\) and the largest occurs at spatial frequencies \(k=(n\pm1)/2\). Set \(\Delta_n=1-\cos(\pi/n)\), \(r=n(a+1)/(a^n+1)\). Direct division yields
\[
\kappa_{n,q}^2=\frac{(a+1)^2}{\bigl((a-1)^2+2a\Delta_n\bigr)(1-r)}.
\]
For \(n=3\), \(a\ge3\), the exact eigenvalues are \(\lambda_0=(a-2)/a\) and \(\lambda_1=\lambda_2=(a+1)/a\), so \(\kappa^2=(a+1)/(a-2)\le B^{-2}\), with equality only at \(a=3\).

For odd \(n=5\), \(a\ge3\), use \(\Delta_5=(3-\sqrt5)/4>1/6\). Then
\[
\frac{2a\Delta_5}{(a-1)^2+2a\Delta_5}>\frac{a}{3a^2-5a+3}\ge\frac{5(a+1)}{a^5+1}=r.
\]
The second inequality follows from \(a^6-15a^3+10a^2+11a-15>0\) for \(a\ge3\). For every odd \(n\ge7\), \(1-\cos(\pi/n)\ge2/n^2\) and \((a-1)^2+2a\Delta_n\le(a+1)^2\). For \(a\ge3\), the inequality \(n^3(a+1)^3\le4a^{n+1}\) holds: its ratio comparison is strongest at \((a,n)=(3,7)\), where \(343\cdot64<4\cdot3^8\); increasing either parameter improves it. Hence \(r\le 4a/[n^2(a+1)^2]\le2a\Delta_n/((a-1)^2+2a\Delta_n)\). All odd cases with \(a\ge3\) therefore have \(\kappa^2\le B^{-2}\le4\).

It remains to treat \(a=2\), equivalently \(q=3\). Even \(n\) have \(\kappa^2<9\); \(n=3\) is singular. At \(n=5\), \(\lambda_0=1/5\), and the maximum mode has \(\lambda_{2}=\lambda_3=33/[10(4-\sqrt5)]\), giving \(\kappa^2=\frac32(4+\sqrt5)>9\). For \(n=7\), \(r=7/43\) and \(\Delta_7>1/20\), so the denominator in the odd-case formula exceeds \((6/5)(36/43)>1\), hence \(\kappa^2<9\). For \(n=9\), \(r=1/19\) and \(\Delta_9>1/100\), giving \(\kappa^2<9\cdot475/468<\frac32(4+\sqrt5)\). For all odd \(n\ge11\), \(r\le33/2049<1/50\); the denominator is greater than \(1-r\), yielding \(\kappa^2<450/49<\frac32(4+\sqrt5)\). The elementary bounds on \(\Delta_7,\Delta_9\) follow from \(1-\cos t\ge t^2/3\) for \(0\le t\le1\) and \(\pi>3\). This proves the unique global extremizer. Finally, as \(n\to\infty\) at fixed \(q\), the smallest eigenvalue approaches \(B\) and the largest approaches \(B^{-1}\), proving the asserted limit.

## Verification

The accompanying `checker.py` enumerates all proper colourings for twelve \((q,n)\)-pairs with \(3\le q\le5\), \(3\le n\le6\), checks exact rational two-point moments against the transfer-matrix expressions and checks every DFT eigenvalue numerically. It also spot-checks positivity and the sharp universal bound over a larger finite grid. Run `python3 checker.py` with Python 3.10 or later; it uses only the standard library. These finite tests corroborate but do not establish the universal inequalities, which are proved above.

## Relationship to prior work

The elementary transfer matrix of the zero-temperature antiferromagnetic Potts model is standard. Borgs and Chayes's 1994 analysis identifies Potts colour-space covariance sectors in infinite-volume models; it does not state the finite-cycle spatial Fourier eigenvalues or their extremal uniform condition-number optimization. Salas and Sokal's 2000 transfer-matrix study develops powerful chromatic-polynomial methods for lattice strips; it does not give the condition-number classification on the one-dimensional proper-colouring cycle. The novel target here is the simultaneous exact finite-size Fourier-frame statement, inverse-covariance locality, and especially the **globally sharp** extremizer \((q,n)=(3,5)\). Standard two-point correlation calculations alone do not establish this global inequality; the odd-size comparisons in Step 4 are essential.

## Limitations

The result concerns only coordinate Fourier characters (degree at most one), not higher harmonic degrees, and only proper colourings of single cycles. The constant mode is a separate orthogonal one-dimensional summand, but its eigenvalue is between the two extremal values of the colour-character block. The sharpness argument is exact but does not provide optimal noisy reconstruction algorithms beyond the spectral inverse already stated. A historical treatment of finite cyclic Potts covariance conditioning under different terminology might be equivalent and remains a literature risk. No independent mathematical audit has been performed.

## References

1. C. Borgs and J. T. Chayes, *The covariance matrix of the Potts model: A random cluster analysis*, arXiv:adap-org/9411001v1, first publicly submitted 1994-11-14, https://arxiv.org/html/adap-org/9411001v1.
2. J. Salas and A. D. Sokal, *Transfer Matrices and Partition-Function Zeros for Antiferromagnetic Potts Models I. General Theory and Square-Lattice Chromatic Polynomial*, arXiv:cond-mat/0004330v1, first publicly submitted 2000-04-19, https://arxiv.org/html/cond-mat/0004330v2.
3. S.-C. Chang and R. Shrock, *Transfer matrices for the zero-temperature Potts antiferromagnet on cyclic and Möbius lattice strips*, Physica A 347 (2005), 400–450, doi:10.1016/j.physa.2004.08.010. (Bibliographic and abstract inspection only.)
