# Non-free test-map fiber obstruction at the (4,3,2) colorful transversal cell

## Context
The Blagojevic–Matschke–Ziegler (BMZ) colorful Tverberg–Vrecica transversal theorem proves, for prime $r$ (with $r(d-k)$ even or $k=0$), that $k+1$ blocks of $(r-1)(d-k+1)+1$ points in $R^d$ with color classes of size $<r$ admit rainbow $r$-partitions met by a $k$-plane. The prime-to-prime-power extension for the transversal case $k \geq 1$ is open: Jojić–Panina–Živajević extends only type-A ($k=0$) to prime powers, and Kliem's finite verification closes only the affine $(4,2,0)$ cell. The first at-bound prime-power transversal cell is $(r,d,k)=(4,3,2)$: three 7-point blocks in $R^3$ of extremal color type $(3,3,1)$, group $G=(Z/2)^2$ via its regular embedding into $S_4$, coefficients $F_2$.

## Definitions
- $G = (Z/2)^2$ (Klein 4), $H^*(BG;F_2) = F_2[x,y]$, $|x|=|y|=1$.
- $\Delta_{4,m}$: chessboard (rook) complex on a $4 \times m$ board (matchings).
- Per block $K^\ell = \Delta_{4,3} * \Delta_{4,3} * \Delta_{4,1}$, $\dim K^\ell = 6$, 28 vertices.
- $W \subset R^4$: reduced regular representation ($\dim 3$, sum-zero vectors); test-map fiber $F = S(W) \cong S^2$.
- $B = G_{3,1} = RP^2$, $\gamma \to B$ tautological line bundle, $E = \gamma^{\oplus 4}$ with diagonal $\Delta \cong \gamma$ and complement $C$ of rank $n=(r-1)(d-k)=3$.

## Result (headline claim)
At $(r,d,k)=(4,3,2)$ with $G=(Z/2)^2$:
1. Positive machine lemmas. Each $K^\ell$ is 3-acyclic over $F_2$ ($\tilde H_i = 0$ for $i \le 3$; in fact $H_1=H_2=H_3=0$ with Betti $(b_0,\dots,b_6)=(1,0,0,0,12,12,3)$) and $G$-free on all simplices. The labeled rainbow 4-partition count for type $(3,3,1)$ is exactly $2304 = 24\cdot 24\cdot 4$, faithfully encoded as triangles of a 3-partite graph, with block-size census $(2,2,3){:}432$, $(1,2,2,2){:}1008$, $(1,1,2,3){:}864$. The $RP^2$ Euler input holds: $H^*(RP^2;F_2)=F_2[a]/(a^3)$ with $a^2 \ne 0$ (explicit cocycle). The representation Euler class is $w_3(W)=xy(x+y) \ne 0$ with $w_1=0$.
2. Obstruction. The test-map sphere fiber $F = S(W)$ is **not** fixed-point free: every involution $g \ne 1$ is a double transposition (2 cycles), so $\dim W^g = 2-1 = 1$ and $F^g = S^0$ (2 points). Hence the free-fiber transgression step of the BMZ parameterized Borsuk–Ulam argument (free fiber forces a nonzero transgressive class of degree $n$) fails literally for $G=V_4$ at $r=4$. Consistently, $w_3(W)=xy(x+y)$ restricts to $0$ on all three order-2 subgroups (coefficient of $t^3$ is $0$ for $(u,v)\in\{(1,0),(0,1),(1,1)\}$), and each subgroup route drops the transversal intersection input ($e^2 = 0$ in $H^4(RP^2)=0$ for the rank-2 fixed bundle). So the prime-case BMZ proof cannot transfer verbatim to this cell; it stops at an explicitly logged diagram.
3. Consequence for the preset fallback. The monomial $x^3y^3 \in \mathrm{Ind}(Y)$-outside-$\mathrm{Ind}(S(V))$ certificate cannot be completed from acyclicity alone: 3-acyclicity yields only $\mathrm{Ind}(Y) \subseteq H^{*\ge 5}(BV_4)$, while membership needs the actual Borel transgression; moreover a class in $\mathrm{Ind}(Y)\setminus\mathrm{Ind}(S(V))$ is compatible with (does not obstruct) a map $Y \to S(V)$ by functoriality ($\mathrm{Ind}(S(V)) \subseteq \mathrm{Ind}(Y)$ if such a map exists).

## Proof / evidence
Finite computations over $F_2$ (stdlib Python only), all replaying VERIFY_OK:
- `verify_target.py`: $\Delta_{4,3}$ faces $(12,36,24)$, connected, $V_4$-free; $w(W)=(1+x)(1+y)(1+x+y)$, $w_3=xy(x+y)$, $w_1=0$; $2304$ labeled partitions equal brute force over $4^7$ assignments; faithful triangle encoding.
- `verify_target2.py`: full $F_2$ chain complex of $K^\ell$ (chain dims $28,312,1776,5520,9216,7488,2304$; boundary ranks $27,285,1491,4029,5175,2301$) giving Betti $(1,0,0,0,12,12,3)$; $K^\ell$ $V_4$-free on every simplex; 6-vertex $RP^2$ triangulation with $\dim H^1=\dim H^2=1$ and cup square $a^2 \ne 0$.
- `verify_target3.py`: sibling types $(3,2,2)$, $(2,2,2,1)$, $(3,2,1,1)$ all 3-acyclic and $V_4$-free; $\Delta_{4,4}$ $V_4$-free (independent recomputation confirms 0 faces fixed by any single involution).
- `verify_target4.py`: fixed-subspace table ($\dim W^g=1$ per involution; common $V_4$-fixed subspace $0$); Euler restriction coefficients all $0$; subgroup $e^2=0$ log.
- The fixed-dimension formula $\dim W^g = (\text{\#cycles of }g)-1$ and the regular-action permutations $a=(01)(23)$, $b=(02)(13)$, $ab=(03)(12)$ give the obstruction by hand; the scripts certify it. For prime $r$ every $g \ne 1$ is an $r$-cycle with $W^g=0$ — exactly the composite-$r$ phenomenon.

## Limitations
- Not a proof (or disproof) of the full $(4,3,2)$ affine 2-plane transversal; the target stays open.
- Not the preset $x^3y^3$ non-existence certificate (shown uncompletable from these data in the stated direction).
- Gysin/localization or $Z/4$-lift repairs are not attempted.
- BMZ theorem/lemma numbering follows the cited version; structural freeness dependence is version-independent.

## Reproducibility
```
python3 output/artifacts/verify_target.py
python3 output/artifacts/verify_target2.py
python3 output/artifacts/verify_target3.py
python3 output/artifacts/verify_target4.py
```
All stdlib only; each prints VERIFY_OK.

## References
- Blagojević–Matschke–Ziegler, Optimal bounds for a colorful Tverberg–Vrecica type problem, arXiv:0911.2692.
- Jojić–Panina–Živajević, Optimal colored Tverberg theorems for prime powers, arXiv:2005.11913.
- Kliem, A new k-partite graph k-clique iterator and the optimal colored Tverberg problem for ten colored points, arXiv:2112.04268.
