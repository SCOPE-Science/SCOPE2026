# Exact forced-colouring functions at maximum degree two

## Status and provenance

The formulas and proofs in this record are correct, but an independent audit on 29 September 2026 found that the original novelty framing was incomplete. The earlier SCOPE record

`2026/09/17/forced-three-colouring-max-degree-two--2226d8f07ffd`

was committed at 2026-09-17 23:56:20 UTC and already contains the exact three-colour path and cycle coefficient formulas and the resulting maximum-degree-two classification. This record was committed later. It is therefore retained as an alternate derivation and refinement package rather than as the first SCOPE discovery of those core formulas.

The additional content retained here is the two-channel root-of-unity/transfer-matrix presentation for cycles, the all-colour packaging, the isolated-vertex correction in the two-colour product formula, and the exact minimum-domain consequences.

## Three-colour formulas

Let F_n(p)=FC_3(P_n;p). Then
\[
F_1=3p,\qquad F_2=6p^2,
\]
and for n>=3,
\[
\boxed{F_n=2pF_{n-1}+2p(1-3p)F_{n-2}.}
\]
Equivalently,
\[
FC_3(P_n;p)=\sum_{j=0}^{\lfloor(n-1)/2\rfloor}
3\,2^{n-j-1}\binom{n-1-j}{j}p^{n-j}(1-3p)^j.
\]

For cycles define
\[
A_0=2,\ A_1=2p,\quad A_n=2pA_{n-1}+2p(1-3p)A_{n-2},
\]
\[
B_0=2,\ B_1=-p,\quad B_n=-pB_{n-1}-p(1-3p)B_{n-2}.
\]
Then for n>=3,
\[
\boxed{FC_3(C_n;p)=A_n+2B_n.}
\]
This is equivalent to the earlier closed coefficient formula
\[
FC_3(C_n;p)=\sum_{j=0}^{\lfloor n/2\rfloor}
\frac{n}{n-j}\binom{n-j}{j}
\bigl(2^{n-j}+2(-1)^{n-j}\bigr)p^{n-j}(1-3p)^j.
\]

The path proof uses the fact that successful initially uncoloured vertices form an independent set of internal vertices. Writing proper 3-colourings in edge-difference signs in Z_3 makes an omitted vertex eligible exactly when two consecutive signs agree. The cycle formula follows either from the earlier suppression count or from the four-state transfer matrix and a cubic root-of-unity closure filter.

## All numbers of colours when Delta<=2

For a graph whose components have orders n_1,...,n_k:

- lambda=1: FC_1(G;p)=1 exactly when G is edgeless, and 0 otherwise.
- lambda=2: if G is non-bipartite the value is 0; if it is bipartite,
\[
\boxed{FC_2(G;p)=2^k\prod_i\bigl((1-p)^{n_i}-(1-2p)^{n_i}\bigr).}
\]
This includes isolated vertices, each contributing 2p.
- lambda=3: multiply the path and cycle factors above over components.
- lambda>=4: no initially uncoloured vertex can be forced, so
\[
FC_\lambda(G;p)=P(G;\lambda)p^{|V(G)|}.
\]

## Minimum forcing domains

For successful partial 3-assignments the minimum initial domain size is
\[
\left\lfloor\frac n2\right\rfloor+1\quad\text{on }P_n,
\qquad
\left\lceil\frac n2\right\rceil\quad\text{on }C_n.
\]
These minima add over components.

## Source-paper consistency corrections

The current Farr preprint prints FC_3(P_3;p)=6p^2(1-2p). Direct counting and the formulas above give
\[
\boxed{FC_3(P_3;p)=6p^2(1-p),}
\]
which also agrees with the earlier Farr--Morgan work and with the chromatic specialization at p=1/3. The two-colour product formula likewise extends over isolated vertices by multiplicativity.

## Verification

Independent definition-level enumeration during the 29 September audit reproduced the path coefficients through n=6 and the cycle coefficients through n=7. The previously committed verifier gives additional finite checks. These computations support, but do not replace, the general proof.

## Literature context and limitations

Farr's 2026 paper develops the forced-colouring function, basic examples, the bipartite two-colour theorem and the general hardness result. Farr--Morgan introduced the polynomial framework. The core three-colour path/cycle family formulas in this record are not claimed as separately original because they already appeared in the earlier SCOPE record named above.

The record remains restricted to maximum degree two. Its scientific contribution after provenance repair is an alternate derivation and a set of refinements/corollaries, not an independent first discovery of the central formulas.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108 (2026).
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746; Springer (2025).
3. SCOPE record `2026/09/17/forced-three-colouring-max-degree-two--2226d8f07ffd`, committed 2026-09-17 23:56:20 UTC.
