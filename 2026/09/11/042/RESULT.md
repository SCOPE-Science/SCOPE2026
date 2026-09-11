# H_2 of unordered configuration spaces of the theta graph is torsion-free

## Context

Rational (edge-)stability for unordered configuration spaces of graphs
$B_k(\Gamma)$ is established (Church–Farb / Randal-Williams philosophy;
An–Drummond-Cole–Knudsen edge stabilization), but the integral boundary is
open. The admitted target asked whether $H_2(B_5(\Theta_{(2,3,4)});\mathbb Z)$
carries a persistent $\mathbb Z/2$ summand past the rational stable range.
The submitted result resolves this negatively, uniformly in $k$.

## Definitions

- $\Theta$ denotes the theta graph: two vertices joined by three internally
  disjoint paths. $\Theta_{(2,3,4)}$ is a subdivision (path lengths 2,3,4),
  hence homeomorphic to the minimal model with vertices $A,B$ and edges
  $e_0,e_1,e_2$.
- $B_k(\Gamma)=\{(x_1,\dots,x_k)\in\Gamma^k:x_i\ne x_j\}/\Sigma_k$ is the
  $k$th unordered configuration space; $B(\Gamma)=\bigsqcup_k B_k(\Gamma)$.
- Świątkowski complex (An–Drummond-Cole–Knudsen, arXiv:1806.05585,
  Definition 2.7): for a commutative ring $R$,
  $S(\Gamma;R)=R[E]\otimes\bigotimes_{v}S(v)$,
  $S(v)=\mathbb Z\langle\emptyset,v,h\in H(v)\rangle$,
  $|\emptyset|=(0,0)$, $|v|=|e|=(0,1)$, $|h|=(1,1)$,
  $\partial(h)=e(h)-v(h)$. Degree counts half-edge factors; weight counts
  particles; differentials preserve weight.

## Result

For the theta graph (in particular $\Theta_{(2,3,4)}$), $H_2(B_k(\Theta);
\mathbb Z)$ is free abelian for every $k$. In particular
$H_2(B_5(\Theta_{(2,3,4)});\mathbb Z)$ has no $\mathbb Z/2$ direct summand,
and no 2-cycle $z$ with $2z$ a boundary but $z$ not a boundary exists.
The target claim is false.

## Proof / evidence

By Theorem 2.10 of arXiv:1806.05585,
$H_*(B(\Gamma);R)\cong H_*(S(\Gamma;R))$ naturally (case $R=\mathbb Z$
included). Since $\Theta_{(2,3,4)}$ is homeomorphic to the minimal theta
model, its $B_k$-homology equals that of the minimal model. At $A$ the
complex contributes $\emptyset_A,v_A$ (degree 0) and $a_0,a_1,a_2$
(degree 1); similarly at $B$. Each vertex factor contributes at most one
half-edge generator, so with two vertices every basis element has degree
$\le 2$. Hence in every weight $C_3=0$, $D_3=0$, and
$H_2(B_k)=\ker(D_2:C_2\to C_1)$. In fixed weight $C_2$ is free abelian
(free on $m\cdot a_i b_j$, $m$ of edge-degree $k-2$); a subgroup of a free
abelian group is free. Hence no torsion exists, uniformly in $k$.
Computed certificate (consistency only; vanishing needs no SNF):
unreduced complex at $k=4$: $C=(41,96,54)$, ranks $(40,53)$,
$H=(1,3,1)$; at $k=5$: $C=(61,150,90)$, ranks $(60,87)$, $H=(1,3,3)$,
entries in $\{-1,0,1\}$, $D_1D_2=0$ exactly. $H_2$ ranks agree with the
paper's Example 3.5 $\Theta_3$ field formula (1 at $k=4$, 3 at $k=5$).

## Limitations

Falsification is for integral $H_2$ of unordered configurations of the
theta graph at every weight. No claim about $H_1$ torsion (known for other
graphs), graphs with $\ge 3$ essential vertices, ordered configurations,
or coefficients beyond the $\mathbb Z$-freeness argument. Diagnosis: any
repair must change the graph (e.g. $K_4$, where $C_3\ne 0$) or the degree;
lobe-length subdivision does not alter the homeomorphism type or argument.

## Reproducibility

Run `python3 output/artifacts/compute_theta.py` (stdlib + sympy); log in
`output/artifacts/verify.log`. Independent replay confirmed identical
dimensions, ranks, $D_1D_2=0$, $H_0=1$, and Example 3.5 rank match.

## References

- B. H. An, G. C. Drummond-Cole, B. Knudsen, Edge stabilization in the
  homology of graph braid groups, arXiv:1806.05585 (v3), Def 2.7, Thm 2.10,
  Sec 3 Ex 3.5. https://arxiv.org/abs/1806.05585
- B. H. An, B. Knudsen, On the second homology of planar graph braid
  groups, arXiv:2008.10371. https://arxiv.org/abs/2008.10371
