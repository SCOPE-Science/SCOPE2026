# Generalized shift-invariant chi permutations are composite chi layers

## Result

Let
\[
F_{n,v}(x)_i=x_i+x_{i+v}x_{i+2v}+x_{i+2v}
\]
and
\[
G_{n,v}(x)_i=x_i+x_{i-2v}x_{i-v}+x_{i-v},
\]
with all indices in \(\mathbb Z/n\mathbb Z\). These are the two permutation families denoted \(\chi_{n,v}\) and \(\chi_{n,-2v}\) in Feng--Wang--Yu--Zhang (2026).

Write
\[
n=2^k n_0,\qquad n_0\text{ odd},
\]
and suppose \(2^k\mid v\), which is exactly the permutation condition for these two families. Put
\[
d=\gcd(n,v),\qquad \ell=n/d.
\]
Then \(\ell\) is odd and at least 3.

**Theorem.** There is a coordinate permutation
\[
\Pi_v:\mathbb F_2^n\longrightarrow (\mathbb F_2^\ell)^d
\]
such that
\[
\Pi_v F_{n,v}\Pi_v^{-1}=\chi_\ell^{\times d}.
\]
Moreover, if \(T:\mathbb F_2^\ell\to\mathbb F_2^\ell\) is the affine involution
\[
(Tz)_t=z_{-t}+1,
\]
then
\[
\Pi_v G_{n,v}\Pi_v^{-1}
=T^{\times d}\,\chi_\ell^{\times d}\,T^{\times d}.
\]
Hence both new permutation families are affine-conjugate to the same composite-\(\chi\) layer consisting of \(d\) parallel copies of the ordinary odd-dimensional \(\chi_\ell\).

For even \(n\), one has \(d\ge 2^k\ge2\). Thus every permutation in either named family is necessarily imprimitive: its coordinates split into at least two noninteracting nonlinear circles, and no iterate of the nonlinear layer alone can transfer information between these circles.

Feng--Wang--Yu--Zhang also prove that every permutation in their full quadratic shift-invariant class
\[
y_i=x_{i+u}+x_{i+v}(x_{i+w}+a_i)
\]
is shift-equivalent to one of the two named families. Consequently, every permutation in that characterized class is extended-affine equivalent to a composite \(\chi\) layer.

## Proof

The map \(t\mapsto tv\) on \(\mathbb Z/n\mathbb Z\) decomposes the coordinate set into exactly \(d=\gcd(n,v)\) cycles, each of length \(\ell=n/d\). Choose one representative \(c_j\) from each cycle and define
\[
(\Pi_v x)_{j,t}=x_{c_j+tv},
\qquad 0\le j<d,\quad t\in\mathbb Z/\ell\mathbb Z.
\]
For \(F_{n,v}\), on one such cycle we obtain
\[
(\Pi_vF_{n,v}x)_{j,t}
=(\Pi_vx)_{j,t}
 +(\Pi_vx)_{j,t+1}(\Pi_vx)_{j,t+2}
 +(\Pi_vx)_{j,t+2},
\]
which is exactly the standard \(\chi_\ell\) rule. Different cycles use disjoint variables, proving
\[
\Pi_vF_{n,v}\Pi_v^{-1}=\chi_\ell^{\times d}.
\]

For \(G_{n,v}\), the local rule on a cycle is
\[
B(z)_t=z_t+z_{t-2}z_{t-1}+z_{t-1}.
\]
Let \(T(z)_t=z_{-t}+1\). Since \(T^2=\mathrm{id}\), direct expansion over \(\mathbb F_2\) gives
\[
(T\chi_\ell T)(z)_t
=z_t+z_{t-2}z_{t-1}+z_{t-1}=B(z)_t.
\]
Thus each block is affine-conjugate to \(\chi_\ell\), proving the second identity.

The divisibility \(2^k\mid v\) implies \(2^k\mid d\), so
\[
\ell=\frac{n}{d}
\]
is odd. Since \(v\not\equiv0\pmod n\), \(d<n\) and therefore \(\ell>1\), hence \(\ell\ge3\).

## Cryptographic consequences

### Exact inverse algebraic degree

For odd \(\ell\), the known inverse of \(\chi_\ell\) has algebraic degree
\[
\deg(\chi_\ell^{-1})=\frac{\ell+1}{2}.
\]
A direct product has the maximum of the coordinate degrees of its factors, and invertible affine conjugacy preserves algebraic degree. Therefore
\[
\boxed{
\deg(F_{n,v}^{-1})
=
\deg(G_{n,v}^{-1})
=
\frac{\ell+1}{2}
=
\frac{n/\gcd(n,v)+1}{2}.
}
\]
Thus the inverse degree is governed by the nonlinear circle length \(\ell\), not by the ambient state size \(n\). In particular, families with fixed \(\ell\) have bounded inverse degree even as \(n\) grows.

### Differential uniformity and complete spectra

Mella--Mehrdad--Daemen (2023) give the differential and extended Walsh spectra of composite \(\chi\) through convolution of the corresponding single-circle spectra. The theorem identifies the new families exactly with that previously studied object, so those formulas apply without new spectral enumeration.

For a nonzero input difference to \(\chi_\ell\), the minimum restriction weight is 2. Indeed, the all-one difference has weight \(\ell-1\ge2\); otherwise the restriction weight is \(h+r\), where \(h\) is Hamming weight and \(r\) is the number of circular 001 substrings. A one-bit difference has \(h=r=1\), while \(h\ge2\) already gives weight at least 2. Hence the maximum differential probability of \(\chi_\ell\) is exactly \(1/4\).

In a direct product, differential probabilities multiply across active blocks; choosing a difference active in exactly one block shows that the same maximum \(1/4\) is attained globally. Therefore both generalized families have exact differential uniformity
\[
\boxed{\Delta(F_{n,v})=\Delta(G_{n,v})=2^{n-2}.}
\]
Their entire differential and extended Walsh spectra are the \(d\)-fold composite spectra of \(\chi_\ell\).

### Iterates and order

For every integer \(r\ge1\),
\[
\Pi_vF_{n,v}^r\Pi_v^{-1}=(\chi_\ell^r)^{\times d},
\]
and
\[
\Pi_vG_{n,v}^r\Pi_v^{-1}
=T^{\times d}(\chi_\ell^r)^{\times d}T^{\times d}.
\]
Thus neither family ever creates cross-block diffusion under repeated application. Also, using the known order formula for odd-dimensional \(\chi\),
\[
\boxed{
\operatorname{ord}(F_{n,v})
=
\operatorname{ord}(G_{n,v})
=
\operatorname{ord}(\chi_\ell)
=2^{\left\lceil\log_2((\ell+1)/2)\right\rceil}.
}
\]
This gives a precise explanation of the recent paper's remark that the iterates of the two generalized families behave similarly.

For fixed \(n\), two maps \(F_{n,v}\) with the same \(\gcd(n,v)\) are coordinate-conjugate. Since valid \(\ell=n/\gcd(n,v)\) are nontrivial odd divisors of \(n_0\), the family collapses to at most \(\tau(n_0)-1\) affine-conjugacy types, even though the defining formulas admit many values of \(v\).

## Verification

`artifacts/verify_composite_chi.py` exhaustively checks the two conjugacies for the valid examples
\[
(n,v)=(6,2),(10,2),(12,4),
\]
checks inverse algebraic degrees for \((6,2)\) and \((10,2)\) by explicit inversion followed by Möbius-transform ANF extraction, and checks exact differential uniformity for \((6,2)\) and \((10,2)\). The recorded output is in `artifacts/verification.txt` and ends in `PASS`.

These finite checks are sanity checks; the theorem is proved algebraically above.

## Relation to prior work

Feng--Wang--Yu--Zhang (2026) introduce the two generalized families, prove the exact permutation condition \(2^k\mid v\), and completely characterize their larger quadratic shift-invariant class. Their proof already organizes coordinates into cycles \(C_i=\{i+tv\}\) when analyzing the derivative equations, but the paper does not identify the permutations themselves as parallel copies of ordinary \(\chi\), does not state the affine conjugacy between the two named families, and does not transfer the composite-\(\chi\) spectra or the inverse-degree formula.

Mella--Mehrdad--Daemen (2023) study ordinary and composite \(\chi\) in detail and give convolution formulas for differential and linear spectra, but their work predates the 2026 generalized family. Kriepke--Kyureghyan and Andreoli--Leander--Piccione--Stennes study other even-dimensional \(\chi\)-like constructions; those constructions are different from the skip-step family considered here.

The novelty claimed here is therefore the structural identification and its consequences for the newly introduced 2026 family, not the known theory of ordinary or composite \(\chi\).

## Limitations

The result concerns the quadratic shift-invariant family characterized by Feng--Wang--Yu--Zhang and, most sharply, its two named permutation families. It does not classify unrelated \(\chi\)-like permutations such as ChiChi or the higher-degree generalized \(\chi_{n,m}\) family. Block decomposition of a nonlinear layer alone does not imply insecurity of a full primitive that interleaves the layer with a mixing linear transformation. The originality assessment is to the best of our knowledge; because the decomposition is short once the coordinate cycles are noticed and the motivating preprint is very recent, folklore and near-simultaneous priority risk remain material.

## References

1. Xiutao Feng, Qiang Wang, Jingyi Yu, Anpeng Zhang, *A generalization of the map chi*, arXiv:2609.19548 (2026). https://arxiv.org/abs/2609.19548
2. Silvia Mella, Alireza Mehrdad, Joan Daemen, *Differential and Linear properties of vectorial boolean functions based on chi*, Cryptography and Communications 15 (2023), 1087--1116. https://doi.org/10.1007/s12095-023-00639-1
3. J. Schoone, J. Daemen, *Algebraic properties of the maps chi_n*, Designs, Codes and Cryptography 92 (2024). https://doi.org/10.1007/s10623-024-01395-w
4. F. Liu, S. Sarkar, W. Meier, T. Isobe, *The inverse of chi and its applications to Rasta-like ciphers*, Journal of Cryptology 35 (2022), Article 28.
5. Bjorn Kriepke, Gohar Kyureghyan, *There are siblings of chi which are permutations for n even*, Designs, Codes and Cryptography 94 (2026), Article 125. https://doi.org/10.1007/s10623-026-01830-0
6. Samuele Andreoli, Gregor Leander, Enrico Piccione, Lukas Stennes, *Generalizations of ChiChi: Families of Low-Latency Permutations in Any Even Dimension*, IACR Transactions on Symmetric Cryptology 2025(3), 800--826. https://doi.org/10.46586/tosc.v2025.i3.800-826
