# Affine product decomposition of the generalized chi permutations

## Statement

Let
\[
n=2^k n_0,\qquad n_0\ \text{odd},
\]
and work over \(\mathbb F_2^n\) with subscripts in \(\mathbb Z/n\mathbb Z\). For a nonzero \(\delta\in\mathbb Z/n\mathbb Z\) satisfying \(2^k\mid\delta\), put
\[
d=\gcd(n,\delta),\qquad \ell=\frac nd.
\]
Then \(\ell>1\) is odd. Define the two quadratic permutations introduced by Feng--Wang--Yu--Zhang [1]
\[
(A_\delta(x))_i=x_i+x_{i+\delta}x_{i+2\delta}+x_{i+2\delta},
\]
and
\[
(B_\delta(x))_i=x_i+x_{i-2\delta}x_{i-\delta}+x_{i-\delta}.
\]
Let \(\chi_\ell\) be the ordinary odd-dimensional chi map
\[
(\chi_\ell(z))_t=z_t+z_{t+1}z_{t+2}+z_{t+2}.
\]

**Theorem.**

1. \(A_\delta\) is linearly conjugate to the Cartesian product of \(d\) independent copies of \(\chi_\ell\):
   \[
   A_\delta\sim \chi_\ell^{\times d}.
   \]
2. \(B_\delta\) is affinely conjugate to the same product. Hence \(A_\delta\) and \(B_\delta\) are affinely conjugate.
3. Every nondegenerate permutation in the full family classified in [1],
   \[
   P_{u,v,w}(x)_i=x_{i+u}+x_{i+v}(x_{i+w}+1),
   \]
   is affine-equivalent to \(\chi_\ell^{\times d}\), where
   \[
   \delta=v-w,\qquad d=\gcd(n,\delta),\qquad \ell=n/d.
   \]
4. For fixed \(n=2^k n_0\), the nondegenerate permutations in [1] have exactly
   \[
   \boxed{\tau(n_0)-1}
   \]
   affine-equivalence classes, indexed by the divisors \(\ell>1\) of \(n_0\).

Thus the apparent \(n\)-dimensional family has an exact effective nonlinear block length \(\ell\): after affine coordinate changes it is just \(d=n/\ell\) parallel copies of the ordinary odd chi map.

## Context

Feng--Wang--Yu--Zhang completely classify their quadratic shift-invariant family [1]. Their theorem says that, after putting \(\delta=v-w\), a map of the displayed form is a permutation exactly when
\[
2^k\mid\delta,
\qquad
\nu:=u-w\equiv 2\delta\ \text{or}\ -\delta\pmod n,
\qquad
(a_i)_i=\mathbf 1.
\]
They state that the resulting maps are shift-equivalent to the two canonical families \(A_\delta\) and \(B_\delta\), and remark that the behavior of their iterates is similar. They do not give a product decomposition, an affine-equivalence classification, or transferred inverse/differential/linear parameters.

For ordinary odd \(\chi_m\), the exact permutation order is known [2], and the inverse formula and inverse algebraic degree are known [1,3]. The result here reduces the new family exactly to those ordinary odd maps.

A related but distinct precedent is CHICHI: Lyu et al. note that CHICHI is extended-affine equivalent to a concatenation of two ordinary chi maps of different odd sizes [4]. The family studied here is different; the decomposition below is uniform across the complete new classification of [1].

## Proof of the product decomposition

The additive step \(\delta\) partitions \(\mathbb Z/n\mathbb Z\) into the \(d\) cycles
\[
C_r=\{r+t\delta\pmod n:0\le t<\ell\},
\qquad 0\le r<d.
\]
Define the coordinate permutation
\[
\Pi_\delta(x)=\bigl(z^{(0)},\ldots,z^{(d-1)}\bigr),
\qquad
z^{(r)}_t=x_{r+t\delta}.
\]
On the \(r\)-th cycle,
\[
(A_\delta(x))_{r+t\delta}
=z^{(r)}_t+z^{(r)}_{t+1}z^{(r)}_{t+2}+z^{(r)}_{t+2}.
\]
Therefore
\[
\boxed{
\Pi_\delta A_\delta\Pi_\delta^{-1}
=
\chi_\ell^{\times d}.
}
\]
This proves the first claim.

For \(B_\delta\), the induced block map is
\[
(b(z))_t=z_t+z_{t-2}z_{t-1}+z_{t-1}.
\]
Let
\[
(Rz)_t=z_{-t},\qquad Cz=z+\mathbf 1,
\]
and put \(T=CR=RC\). Then \(T\) is an affine involution and a direct calculation gives
\[
(RbR(z))_t
=z_t+z_{t+1}z_{t+2}+z_{t+1}
=(C\chi_\ell C(z))_t.
\]
Consequently
\[
\boxed{TbT=\chi_\ell.}
\]
Applying \(T\) independently on all \(d\) blocks proves that \(B_\delta\) is affinely conjugate to \(\chi_\ell^{\times d}\).

## Reduction of the full classified family

Let
\[
\delta=v-w,
\qquad z_i=x_{i+w}.
\]
The classification theorem of [1] leaves two cases.

If \(u-w=-\delta\), then
\[
P_{u,v,w}(x)_i
=z_{i-\delta}+z_{i+\delta}(z_i+1)
=(A_\delta(z))_{i-\delta}.
\]
If \(u-w=2\delta\), then
\[
P_{u,v,w}(x)_i
=z_{i+2\delta}+z_{i+\delta}(z_i+1)
=(B_\delta(z))_{i+2\delta}.
\]
Thus every nondegenerate map in the classified family differs from one of the two canonical maps only by invertible coordinate shifts on the input and output. Combining this with the preceding conjugacies yields the claimed affine equivalence to \(\chi_\ell^{\times d}\).

The excluded case \(\delta=0\) is degenerate: the quadratic term collapses and the map is affine rather than a genuinely quadratic member of the family.

## Exact affine-equivalence classification

Write
\[
\delta=2^k a\pmod n,
\qquad 1\le a<n_0.
\]
Then
\[
\ell
=\frac{n}{\gcd(n,\delta)}
=\frac{n_0}{\gcd(n_0,a)}.
\]
Hence every nondegenerate map has \(\ell>1\) dividing \(n_0\), and every divisor \(\ell>1\) of \(n_0\) occurs by taking \(a=n_0/\ell\).

All maps with the same \(\ell\) are affine-equivalent to the same product \(\chi_\ell^{\times n/\ell}\). To see that two different \(\ell\)'s cannot collapse to one affine class, use inverse algebraic degree. For odd \(\ell\), the ordinary chi inverse has degree [3]
\[
\deg(\chi_\ell^{-1})=\frac{\ell+1}{2}.
\]
A Cartesian product has the same inverse degree as one block, and invertible affine maps on either side preserve vectorial algebraic degree. Therefore every nondegenerate classified permutation has
\[
\boxed{
\deg(P^{-1})=\frac{\ell+1}{2}.
}
\]
Distinct \(\ell\)'s give distinct inverse degrees. This proves the exact count \(\tau(n_0)-1\).

In particular, if \(n_0=p\) is an odd prime, every nondegenerate member of the new family belongs to a single affine class:
\[
\boxed{
P\sim \chi_p^{\times 2^k}.
}
\]
For \(p=3\), all these permutations have quadratic inverses.

## Canonical dynamics

Affine equivalence by unrelated input and output maps does not preserve iteration, so the following dynamical statements are asserted for the canonical maps \(A_\delta,B_\delta\), for which actual conjugacies were proved.

Schoone--Daemen proved that, for odd \(m\),
\[
\operatorname{ord}(\chi_m)
=2^{\lceil\log_2((m+1)/2)\rceil}.
\]
A direct product of identical copies has the same order. Hence
\[
\boxed{
\operatorname{ord}(A_\delta)
=
\operatorname{ord}(B_\delta)
=2^{\lceil\log_2((\ell+1)/2)\rceil}.
}
\]

The ordinary \(\chi_\ell\) has exactly two fixed points. Indeed, \(\chi_\ell(z)=z\) is equivalent to
\[
(z_{t+1}+1)z_{t+2}=0\qquad\text{for every }t.
\]
If one coordinate equals \(1\), the preceding coordinate must equal \(1\); cyclicity then forces the all-one state. Otherwise the state is all zero. Consequently
\[
\boxed{
|\operatorname{Fix}(A_\delta)|
=|\operatorname{Fix}(B_\delta)|
=2^d.
}
\]
More generally, for every positive integer \(r\),
\[
|\operatorname{Fix}(A_\delta^r)|
=|\operatorname{Fix}(B_\delta^r)|
=|\operatorname{Fix}(\chi_\ell^r)|^d.
\]
Thus the number of cycles of exact length \(r\) is
\[
\frac1r\sum_{s\mid r}\mu(r/s)
|\operatorname{Fix}(\chi_\ell^s)|^d.
\]
The complete state-diagram information for ordinary \(\chi_\ell\) therefore lifts multiplicatively to the canonical generalized maps.

## Explicit inverse

The standard inverse formula [1,3] transfers blockwise. For \(A_\delta\), if \(y=A_\delta(x)\), then
\[
\boxed{
(A_\delta^{-1}(y))_i
=
y_i+
\sum_{j=1}^{(\ell-1)/2}
 y_{i-(2j-1)\delta}
 \prod_{r=j}^{(\ell-1)/2}
 (y_{i-2r\delta}+1).
}
\]
All indices are modulo \(n\). The inverse of \(B_\delta\) is obtained by applying the blockwise reverse-complement involution before and after this ordinary-chi inverse.

## Differential and linear tables factor exactly

Let \(F:\mathbb F_2^\ell\to\mathbb F_2^\ell\) be a permutation and let
\[
G=F^{\times d}:\mathbb F_2^{d\ell}\to\mathbb F_2^{d\ell}.
\]
For its difference distribution table write
\[
D_F(a,b)=|\{x:F(x+a)+F(x)=b\}|.
\]
Block independence gives the exact identity
\[
\boxed{
D_G((a_j)_j,(b_j)_j)=\prod_{j=1}^d D_F(a_j,b_j).
}
\]
If \(\Delta(F)=\max_{a\ne0,b}D_F(a,b)\) is differential uniformity, then
\[
\boxed{
\Delta(G)=2^{\ell(d-1)}\Delta(F).
}
\]
Indeed, if the input difference is nonzero on \(r\) blocks, its best possible count is at most
\[
\Delta(F)^r2^{\ell(d-r)}
\le
\Delta(F)2^{\ell(d-1)},
\]
and equality is attained by activating only one block.

For the vectorial Walsh transform
\[
W_F(\alpha,\beta)
=
\sum_x(-1)^{\alpha\cdot x+\beta\cdot F(x)},
\]
block independence likewise gives
\[
\boxed{
W_G((\alpha_j)_j,(\beta_j)_j)
=
\prod_{j=1}^dW_F(\alpha_j,\beta_j).
}
\]
Let
\[
\Lambda(F)=\max_{\beta\ne0,\alpha}|W_F(\alpha,\beta)|.
\]
Then
\[
\boxed{
\Lambda(G)=2^{\ell(d-1)}\Lambda(F).
}
\]
Therefore every nondegenerate permutation \(P\) in [1] satisfies
\[
\boxed{
\Delta(P)=2^{n-\ell}\Delta(\chi_\ell),
\qquad
\Lambda(P)=2^{n-\ell}\Lambda(\chi_\ell).
}
\]
Equivalently, the normalized worst-case differential probability and normalized maximum linear correlation are exactly those of the smaller odd map:
\[
\frac{\Delta(P)}{2^n}
=
\frac{\Delta(\chi_\ell)}{2^\ell},
\qquad
\frac{\Lambda(P)}{2^n}
=
\frac{\Lambda(\chi_\ell)}{2^\ell}.
\]
The usual vectorial nonlinearity consequently scales by \(2^{n-\ell}\).

For even \(n\), every nondegenerate map in the family has \(d\ge2\), so this direct-product structure is unavoidable. This does not by itself imply weakness of a full cryptographic design: a surrounding linear layer may deliberately mix the parallel blocks. It does show that the nonlinear layer alone gains no normalized differential or linear advantage merely from the larger ambient dimension.

## Reproducibility

`artifacts/verify.py` is a standalone Python 3 script using only the standard library. It exhaustively checks representative cases \((n,\delta)=(6,2),(10,2),(12,4)\) for the product decomposition, reverse-complement conjugacy, fixed-point count, order, inverse formula, and inverse degree where feasible. It also checks all classified nondegenerate parameter triples for \(n=6\), and verifies the predicted DDT and Walsh scaling for \(\chi_{6,2}\) against \(\chi_3\). The recorded output is in `artifacts/verify_output.txt`.

The finite computations are sanity checks. The general theorem follows from the explicit conjugacies and product identities above.

## Originality boundary and limitations

The classification of the quadratic shift-invariant permutations, the two canonical generalized families, the ordinary chi inverse formula, the ordinary chi inverse degree, and the ordinary chi state diagram/order are prior results [1--3]. Direct-product factorization of DDT and Walsh tables is standard once a product decomposition is known. CHICHI was also already known to admit a different concatenation-type affine decomposition [4].

The new claim is the exact affine product decomposition of the family introduced in [1], the resulting \(\tau(n_0)-1\) affine-class classification, and the systematic transfer of inverse degree, canonical dynamics, and differential/linear parameters through the effective odd block length \(\ell\).

Originality is asserted only to the best of our knowledge. The source preprint [1] is very recent, and its closing remark already notes similar iterate behavior between its two canonical families. The direct-product observation is elementary once the coordinate cycles are isolated, so a near-simultaneous observation or a later revision of [1] is a material residual priority risk.

The result is structural rather than a cryptanalytic break. It does not analyze a complete cipher, does not account for diffusion supplied by surrounding linear layers, and does not claim that the standard chi properties transferred here are themselves new.

## References

1. X. Feng, Q. Wang, J. Yu, A. Zhang, *A generalization of the map chi*, arXiv:2609.19548v1 (2026). https://arxiv.org/abs/2609.19548
2. J. Schoone, J. Daemen, *The state diagram of chi*, Designs, Codes and Cryptography 92 (2024), 1393--1421. https://doi.org/10.1007/s10623-023-01349-8
3. J. Schoone, J. Daemen, *Algebraic properties of the maps chi_n*, Designs, Codes and Cryptography 92 (2024), 2341--2365. https://doi.org/10.1007/s10623-024-01395-w
4. C. Lyu, M. Yuan, D. Zheng, S. Sun, S. Li, *A Generalized chi_n-Function*, IEEE Transactions on Information Theory 72 (2026), 2543--2556; arXiv:2509.20880. https://arxiv.org/abs/2509.20880
