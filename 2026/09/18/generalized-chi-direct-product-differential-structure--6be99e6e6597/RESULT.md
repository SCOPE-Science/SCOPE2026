# Generalized chi permutations split into independent odd chi blocks

## Result

Let
\[
\chi_{n,v}(x)_i=x_i+x_{i+v}x_{i+2v}+x_{i+2v},\qquad i\in\mathbb Z/n\mathbb Z,
\]
and put
\[
d=\gcd(n,v),\qquad \ell=n/d.
\]
Define the coordinate relabeling
\[
T_v(x)_{r,t}=x_{r+tv},\qquad 0\le r<d,\quad 0\le t<\ell.
\]
Then, for every `n` and every nonzero `v mod n`, one has the exact conjugacy
\[
T_v\circ\chi_{n,v}\circ T_v^{-1}=\chi_\ell^{\times d}.
\]
Thus the generalized map is not an indecomposable `n`-bit nonlinear layer: it is exactly `d` parallel copies of the ordinary odd-length chi map whenever it is a permutation.

The second family introduced together with it,
\[
\chi_{n,-2v}(x)_i=x_i+x_{i-2v}x_{i-v}+x_{i-v},
\]
has the same block decomposition. On one length-`ell` block it is
\[
\psi_\ell(z)_t=z_t+z_{t-2}z_{t-1}+z_{t-1}.
\]
If
\[
A(z)_t=z_{-t}+1,
\]
then `A` is an affine involution and
\[
\psi_\ell=A\circ\chi_\ell\circ A.
\]
Consequently
\[
T_v\circ\chi_{n,-2v}\circ T_v^{-1}
=(A\circ\chi_\ell\circ A)^{\times d}.
\]
In particular, the two explicit generalized families have identical cycle-order and differential-uniformity invariants inherited from `chi_ell`.

## Consequences in the permutation case

Write `n=2^k n_0` with `n_0` odd. Feng, Wang, Yu and Zhang proved in arXiv:2609.19548 that `chi_{n,v}` is a permutation exactly when `2^k | v`. The decomposition above gives an equivalent one-line criterion:
\[
\chi_{n,v}\text{ is a permutation}
\iff \ell=\frac{n}{\gcd(n,v)}\text{ is odd}
\iff 2^k\mid v.
\]
The same criterion holds for `chi_{n,-2v}`. Since `v` is nonzero modulo `n`, an odd `ell` here satisfies `ell>=3`.

For every such permutation:

1. **Exact order.** The known order formula for ordinary chi gives
   \[
   \operatorname{ord}(\chi_{n,v})=
   \operatorname{ord}(\chi_{n,-2v})=
   2^{\left\lceil\log_2((\ell+1)/2)\right\rceil}.
   \]
   Hence the permutation order depends on the smaller odd block length `ell`, not on the ambient dimension `n`.

2. **Inverse algebraic degree.** Since affine conjugation and coordinate relabeling preserve algebraic degree,
   \[
   \deg(\chi_{n,v}^{-1})=
   \deg(\chi_{n,-2v}^{-1})=\frac{\ell+1}{2}.
   \]
   For `chi_{n,v}` itself, coordinate relabeling also preserves the exact monomial count in each inverse coordinate. Using the known formula for `chi_ell^{-1}`, the number of degree-`m` monomials in each inverse coordinate is
   \[
   \binom{(\ell+1)/2}{m},\qquad 1\le m\le(\ell+1)/2,
   \]
   and the total is `2^((ell+1)/2)-1`.

3. **Complete differential factorization.** Let
   \[
   N_F(a,b)=|\{x:F(x+a)+F(x)=b\}|.
   \]
   Under the block coordinates supplied by `T_v`, if
   `a=(a^(0),...,a^(d-1))` and `b=(b^(0),...,b^(d-1))`, then
   \[
   N_{\chi_{n,v}}(a,b)
   =\prod_{r=0}^{d-1}N_{\chi_\ell}(a^{(r)},b^{(r)}).
   \]
   Equivalently, after row and column reindexing, the DDT is the `d`-fold Kronecker product of the DDT of `chi_ell`. The second family has an affinely equivalent DDT.

4. **Exact differential uniformity.** For odd `ell>1`, the known differential formula for ordinary chi says that every compatible differential has probability `2^{-w(a)}`, where the minimum of `w(a)` over nonzero input differences is `2`. Hence `chi_ell` has maximum differential probability `1/4`, or differential uniformity `2^(ell-2)`. The product formula therefore gives
   \[
   \boxed{\delta(\chi_{n,v})=\delta(\chi_{n,-2v})=2^{n-2}},
   \]
   equivalently a maximum differential probability exactly `1/4`, for every permutation in these two families.

5. **No cross-block diffusion under iteration.** Every iterate of either explicit family preserves the partition into the `d` coordinate cycles
   \[
   C_r=\{r+tv\pmod n:0\le t<\ell\}.
   \]
   If `n` is even, the permutation condition forces `d` to be divisible by the full power of two dividing `n`, so `d>=2`. Thus every even-dimensional permutation in these two explicit families has a nontrivial invariant block decomposition for all iteration counts.

There is also a consequence for the complete degree-two family classified in Theorem 1 / Corollary 3 of Feng et al. For the nondegenerate nonlinear cases, put `s=v-w (mod n)`, `s!=0`. Their two permitted offset relations make the resulting map an input/output cyclic-shift equivalent of either `chi_{n,s}` or `chi_{n,-2s}`. Cyclic shifts are linear coordinate permutations. Therefore every such nonlinear permutation has differential uniformity `2^(n-2)` and inverse algebraic degree `(ell+1)/2`, where `ell=n/gcd(n,s)`.

## Proof of the block decomposition

The sets
\[
C_r=\{r+tv\pmod n:0\le t<\ell\},\qquad 0\le r<d,
\]
are exactly the cycles of addition by `v` on `Z/nZ`. They partition all coordinates because `d=gcd(n,v)` and each cycle has length `ell=n/d`.

Write `z_t=x_{r+tv}` on one fixed cycle. Then
\[
\begin{aligned}
\chi_{n,v}(x)_{r+tv}
&=x_{r+tv}+x_{r+(t+1)v}x_{r+(t+2)v}+x_{r+(t+2)v}\\
&=z_t+z_{t+1}z_{t+2}+z_{t+2}\\
&=\chi_\ell(z)_t,
\end{aligned}
\]
with `t` modulo `ell`. Different cycles use disjoint variables, proving the direct-product identity.

For the second family the same relabeling gives
\[
\chi_{n,-2v}(x)_{r+tv}
=z_t+z_{t-2}z_{t-1}+z_{t-1}=\psi_\ell(z)_t.
\]
Let `C(z)=z+1` and `R(z)_t=z_{-t}`. Direct substitution gives
\[
C\circ\chi_\ell\circ C:
 z_t\mapsto z_t+z_{t+1}z_{t+2}+z_{t+1},
\]
and conjugating by `R` yields `psi_ell`. Since `A=RC=CR`, one has `psi_ell=A chi_ell A`.

The order and inverse-degree statements now follow from conjugacy and the known corresponding formulas for ordinary chi. The differential factorization follows because for a Cartesian product `F^{x d}`, the derivative equation separates independently in every block. For the differential-uniformity statement, the ordinary-chi differential formula gives maximum probability `1/4`; choosing a nonzero difference in exactly one block attains `1/4`, while every nonzero difference involving more blocks can only multiply additional probabilities at most `1/4`.

## Relation to prior literature

Feng, Wang, Yu and Zhang introduced `chi_{n,v}` and `chi_{n,-2v}` and proved the exact permutation criterion in *A generalization of the map chi*, submitted 17 September 2026 (arXiv:2609.19548). Their proof partitions a derivative system according to the same arithmetic cycles and reduces a key argument to an odd cycle, but the paper does not state the map-level direct-product conjugacy, the affine conjugacy between the two block maps, the inherited order/inverse-degree formulas for these families, or the DDT factorization and exact differential uniformity derived here.

For ordinary odd-length chi, the order/cycle structure is known from Schoone and Daemen's *The state diagram of chi* (2024). Schoone and Daemen's *Algebraic properties of the maps chi_n* (2024) records the inverse-degree and inverse-monomial formulas and gives the differential-probability formula used above. Those ordinary-chi results are not claimed as new here.

Related even-dimensional chi-like constructions by Kriepke and Kyureghyan, Lyu et al., and the ChiChi line use different maps and do not by themselves imply the stated decomposition of the newly introduced `chi_{n,v}` family.

## Reproducibility

`artifacts/verify_structure.py` exhaustively checks the two block identities for `(n,v)=(6,2),(10,2),(12,4)`, and computes differential uniformities for representative base and generalized maps. Its recorded output is in `artifacts/verification.txt`. These finite checks are sanity checks only; the general result is proved above.

## Limitations

- Originality is asserted only to the best of our knowledge. The motivating preprint appeared on 17 September 2026, so near-simultaneous or not-yet-indexed observations are a material residual risk.
- The direct-product theorem concerns the `chi_{n,v}` and `chi_{n,-2v}` families defined above. The differential-uniformity corollary extends to the nondegenerate nonlinear permutations in Feng et al.'s classified degree-two family via their shift equivalence; the exact order statement is only asserted for the two explicitly conjugated families.
- The result identifies a structural and differential limitation of these nonlinear layers; it is not, by itself, a cryptanalytic break of any full cipher using them together with separate diffusion layers.
- No independent validation or formal verification is asserted.

## References

1. Xiutao Feng, Qiang Wang, Jingyi Yu, Anpeng Zhang, *A generalization of the map chi*, arXiv:2609.19548, submitted 17 September 2026. https://arxiv.org/abs/2609.19548
2. Jan Schoone, Joan Daemen, *The state diagram of chi*, Designs, Codes and Cryptography 92 (2024), 1393-1421. https://doi.org/10.1007/s10623-023-01349-8
3. Jan Schoone, Joan Daemen, *Algebraic properties of the maps chi_n*, Designs, Codes and Cryptography 92 (2024), 2341-2365. https://doi.org/10.1007/s10623-024-01395-w
4. Bjorn Kriepke, Gohar Kyureghyan, *There are siblings of chi which are permutations for n even*, Designs, Codes and Cryptography 94 (2026), Article 125. https://doi.org/10.1007/s10623-026-01830-0
5. Samuele Andreoli, Gregor Leander, Enrico Piccione, Lukas Stennes, *Generalizations of ChiChi: Families of Low-Latency Permutations in Any Even Dimension*, IACR Transactions on Symmetric Cryptology 2025(3), 800-826. https://doi.org/10.46586/tosc.v2025.i3.800-826
