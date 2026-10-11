# The sharp square-cell constant for Lipschitz-free \(p\)-interpolation

## Finding
Let \(0<p\leq1\). Put \(Q=[0,1]^2\) with the \(\ell_1\) metric, and let \(V=\{A=(0,0),B=(1,0),C=(0,1),D=(1,1)\}\), pointed at \(A\), with the induced metric. In the real Lipschitz-free \(p\)-space \(\mathcal F_p(V)\), let \(\delta_A=0\) and define the vertex-interpolation retraction
\[
r(x,y)=(1-x)(1-y)\delta_A+x(1-y)\delta_B+(1-x)y\delta_C+xy\delta_D.
\]
Its **exact** Lipschitz constant is
\[
\boxed{\operatorname{Lip}(r)=\frac{(2+2^p)^{1/p}}4.}
\]
In particular, at \(p=1/2\) it is \(3/2+\sqrt2\). For \(0<p<1\), this is strictly larger than the previously known dimensional lower bound \(2^{1/p-1}\).

## Assumptions and scope
All statements concern real scalars, \(0<p\le1\), exactly one unit square with the \(\ell_1\) domain/vertex distances, and the canonical coordinatewise-affine (bilinear) map above. The \(p\)-norm is the standard free \(p\)-space molecular norm; its \(p\)-triangle inequality, not an ordinary triangle inequality, is used when \(p<1\). The formula is for this specified retraction, not the infimum over arbitrary Lipschitz extensions, nor a universal all-dimensional bound. The base point does not affect norms of formal molecules of total coefficient zero.

## Proof
**1. Exact finite transport formula.** For \(m=\sum_{v\in V}m_v\delta_v\) with \(\sum_vm_v=0\), the free \(p\)-norm satisfies
\[
\|m\|_p^p=\min_f\sum_{\{u,v\}\subset V}(d(u,v)|f_{uv}|)^p,
\]
where antisymmetric real edge flows on the complete graph on \(V\) have net divergence \(m\). Indeed, the defining infimum over normalized elementary molecules is equivalent to the displayed flow minimum: on an unordered edge, aggregating coefficients cannot raise \(p\)-cost since \(|a+b|^p\le|a|^p+|b|^p\). The minimum exists, because the cost is coercive on the finite-dimensional affine space of feasible flows. Any minimizing flow has an equally good representative supported on a forest. To see this, take any cycle of nonzero flows and add a signed circulation. Until an edge first reaches zero in either direction, each absolute-value term stays in one sign chamber; its \(p\)th power is concave along this one-dimensional interval. Hence the total cost at an endpoint does not exceed its cost at the original flow. Repeating removes cycles. Extending a forest by zero-flow edges produces a spanning tree. Therefore it suffices to take the minimum over the 16 spanning trees of the complete graph on four vertices, with the unique tree flows determined by vertex masses (each tree-edge flow is the sum of masses on one component after deleting that edge).

**2. Midpoint derivative reduces all secants.** Since \(r\) is affine in each variable separately, its bilinear polarization gives, exactly,
\[
r(z)-r(z')=Dr\bigl((z+z')/2\bigr)[z-z'].
\]
Every derivative at an interior point and in any direction is a limit of admissible short symmetric secants. Continuity extends this equality of suprema to boundary points. Consequently \(\operatorname{Lip}(r)\) is the supremum of the \(p\)-norm of \(Dr(a,b)[s,t]\) over \(a,b\in[0,1]\) and \(|s|+|t|=1\). Reflecting either coordinate of the square permutes vertices and induces an isometry of its free \(p\)-space; we may therefore take \(s,t\ge0\), with \(s+t=1\).

**3. An upper bound from two competing cycle eliminations.** Orient the four unit-length square edges as \(AB,CD,AC,BD\), and write their unnormalized molecules as \(e_{AB}=\delta_B-\delta_A\), \(e_{CD}=\delta_D-\delta_C\), \(e_{AC}=\delta_C-\delta_A\), and \(e_{BD}=\delta_D-\delta_B\). Then
\[
Dr(a,b)[s,t]=\alpha e_{AB}+\beta e_{CD}+\gamma e_{AC}+\eta e_{BD},
\]
where \(\alpha=s(1-b),\ \beta=sb,\ \gamma=t(1-a),\ \eta=ta\); all are nonnegative, and their sum is one. Put \(u=\alpha+\gamma\) and \(v=\beta+\eta\), so \(u+v=1\). The cycle relation \(e_{AB}+e_{BD}=e_{AC}+e_{CD}\) leaves this molecule unchanged when its four coefficients are replaced by \((\alpha+\lambda,\beta-\lambda,\gamma-\lambda,\eta+\lambda)\).

Choosing \(\lambda=-\min\{\alpha,\eta\}\) gives a nonnegative representation with one zero coefficient. Its remaining entries include \(s\) and \(u\) if \(\alpha\le\eta\), or include \(t\) and \(v\) if \(\alpha\ge\eta\). Independently, choosing \(\lambda=\min\{\beta,\gamma\}\) gives another nonnegative three-edge representation: its remaining entries include \(s\) and \(v\) when \(\beta\le\gamma\), or include \(t\) and \(u\) when \(\beta\ge\gamma\). In every case at least one of the two three-edge representations contains a coefficient at least \(1/2\): either they include \(s\) and \(t\) between them, or they both include the same one of \(s,t\) and additionally include \(u,v\) between them. Both pairs sum to one.

Thus a feasible representation has three nonnegative coefficients \(q_1,q_2,q_3\), totaling one, with \(\max q_i\ge1/2\). Its decreasing rearrangement majorizes \((1/2,1/4,1/4)\): the largest is at least \(1/2\), while the smallest is at most \(1/4\). Concavity of \(x\mapsto x^p\), together with the free \(p\)-norm's molecular upper bound and the fact that all four square-edge lengths are one, yields
\[
\|Dr(a,b)[s,t]\|_p^p\le\sum_{i=1}^3q_i^p\le(1/2)^p+2(1/4)^p.
\]
The middle inequality is Karamata's inequality; it remains an equality when \(p=1\). This proves the required global upper bound.

**4. Sharpness, using an exact 16-tree calculation.** Take the interior point \((a,b)=(1/4,1/4)\) and normalized direction \((s,t)=(1/2,1/2)\). The four vertex masses of its derivative, in the order \(A,B,C,D\), are
\[
(-3/4,1/4,1/4,1/4).
\]
For every spanning tree, cut-summing these masses determines its three flow magnitudes. Multiplying by the corresponding \(\ell_1\) edge lengths (one for a side, two for a diagonal) gives exactly the following sorted triples, with multiplicities:

| Sorted length-times-flow magnitudes | Number of trees |
| --- | ---: |
| \((1/4,1/4,1/2)\) | 3 |
| \((1/4,1/4,1)\) | 2 |
| \((1/4,1/2,3/4)\) | 4 |
| \((1/4,1/4,3/2)\) | 1 |
| \((1/2,1/2,1/2)\) | 2 |
| \((1/4,3/4,1)\) | 2 |
| \((1/2,1/2,3/2)\) | 2 |

The counts total 16 (the 4 stars and 12 paths on four labelled vertices). Each sorted triple is componentwise at least \((1/4,1/4,1/2)\), and the first triple occurs. Therefore the transport formula gives, **for every real \(0<p\le1\)**,
\[
\|Dr(1/4,1/4)[1/2,1/2]\|_p^p=2(1/4)^p+(1/2)^p.
\]
Short symmetric secants about that interior point attain this ratio in the limit. Taking \(p\)th roots gives \((2+2^p)^{1/p}/4\), completing the proof.

For comparison, when \(0<p<1\), the inequality \(1+2^{p-1}>2^p\) implies \((2+2^p)^{1/p}/4>2^{1/p-1}\), while at \(p=1\) both values equal one.

## Verification
The standalone `verify_square.py` performs exact-rational enumeration of all 16 labelled spanning trees; reproduces the seven flow-magnitude triples and their multiplicities; checks componentwise minimality of the sharp triple; checks 775 rational cycle-elimination coefficient configurations and their divergence equality; and compares the sharp tree formula at four exponent values. Execute `python3 verify_square.py` with Python 3 standard library only. The analytic derivation above, not this finite sample, proves the continuum upper bound for all real parameters and exponents. The finite tree enumeration is exhaustive, and all quantities in that enumeration are exact fractions.

## Relationship to prior work
Albiac–Ansorena–Cúth–Doucha (arXiv:2006.08018v1, 2020), Theorem 3.5 and its coordinatewise-affine construction, introduce this canonical family and establish a dimension-dependent Lipschitz bound, without the stated sharp square-cell value. Bíma (arXiv:2303.03265v1, 2023), Theorem 3.2, supplies improved upper and lower bounds for general cube unions: at dimension two its lower bound is \(2^{1/p-1}\), strictly below this one-cell exact value when \(p<1\). Albiac–Ansorena (arXiv:2603.28193v1, 2026) develop a different general Lipschitz-extension and embedding theorem; their inspected main statements do not provide this exact coordinatewise-bilinear square constant. The contribution is the first nontrivial dimensional sharp instance for the specified canonical cell interpolation, not a claim about the universal best extension constant.

## Limitations
The proof is restricted to a single square and the real free \(p\)-space over its four vertices with the \(\ell_1\) metric. It does not establish optimality among all possible extensions or retractions, a sharp constant for unions of cells, or sharp constants for higher-dimensional cubes. While the cited primary results and directly relevant searchable literature have been compared, unindexed equivalent formulations are possible.

## References
1. F. Albiac, J. L. Ansorena, M. Cúth and M. Doucha, *Structure of the Lipschitz free \(p\)-spaces \(\mathcal F_p(\mathbb Z^d)\) and \(\mathcal F_p(\mathbb R^d)\) for \(0<p\le1\)*, arXiv:2006.08018v1 (first posted 2020-06-14), especially Theorem 3.5 and Section 3. https://arxiv.org/html/2006.08018v1
2. J. Bíma, *Lipschitz Free Spaces and Subsets of Finite-Dimensional Spaces*, arXiv:2303.03265v1 (first posted 2023-03-06), especially Theorem 3.2 and its proof. https://arxiv.org/abs/2303.03265
3. F. Albiac and J. L. Ansorena, *Lipschitz extensions into \(p\)-Banach spaces, and canonical embeddings of Lipschitz-free \(p\)-spaces for \(0<p<1\)*, arXiv:2603.28193v1 (first posted 2026-03-30). https://arxiv.org/html/2603.28193v1
