# Sharp Euclidean thickness and a cut-balance transition in the standard cyclohedron

## Finding
Let \(n\ge3\), let \(C_n\) be the cycle on vertex set \([n]\), and let \(\mathcal B_n\) be the family of all nonempty vertex subsets inducing connected subgraphs. In the standard coordinate-simplex realization set
\[
W_n=\sum_{B\in\mathcal B_n}\Delta_B,\qquad
\Delta_B=\operatorname{conv}\{e_i:i\in B\}\subset\mathbb R^n.
\]
The affine hull is \(\sum_i x_i=n(n-1)+1\). Widths below are measured in its intrinsic Euclidean metric. Define
\[
A_n=\frac{(n-1)(n-2)}2,\qquad
U_n=\left\lfloor\frac{n^2}{4}\right\rfloor.
\]
Then the exact minimal Euclidean width is
\[
\boxed{\operatorname{width}(W_n)=
\begin{cases}
4\sqrt3,&n=4,\\[2pt]
\sqrt n\,(A_n+U_n)/\sqrt{U_n},&n=3\ \text{or}\ n\ge5.
\end{cases}}
\]
In particular, for even \(n\ge6\) the value is \((3n^2-6n+4)/(2\sqrt n)\), while for odd \(n\ge3\) it is \(3(n-1)^2\sqrt n/(2\sqrt{n^2-1})\). Consequently \(\operatorname{width}(W_n)\sim 3n^{3/2}/2\).

Every minimizing unoriented normal line, and no other one, is represented by
\[
\nu_S=\mathbf1_S-\frac{|S|}{n}\mathbf1,
\]
where \(S\) is a cyclic consecutive block with \(|S|=1\) when \(n=3,4\), and with \(|S|\in\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\) when \(n\ge5\). Complementary blocks give the same unoriented line. The number of distinct minimizing lines is \(n\) for odd \(n\), \(4\) for \(n=4\), and \(n/2\) for even \(n\ge6\). Thus the optimal direction changes sharply from singleton cuts at four vertices to balanced contiguous cuts at five vertices.

The general reduction underlying this result is as follows. For any finite family \(\mathcal H\) of nonempty subsets of \([n]\) with positive real weights \(a_B\), suppose its crossing functional is positive for every nontrivial cut. Then the full-dimensional simplex-sum polytope \(P_{\mathcal H}=\sum_{B\in\mathcal H}a_B\Delta_B\) has minimal intrinsic Euclidean width
\[
\boxed{\min_{\varnothing\ne S\subsetneq[n]}
\sqrt{\frac{n}{|S|(n-|S|)}}
\sum_{B\in\mathcal H}a_B\mathbf1\{B\cap S\ne\varnothing,\ B\setminus S\ne\varnothing\}.}
\]
Every minimizing normal is a centered two-level cut vector. The general reduction is used as a lemma, not advanced as a separately novel result; its layer-cake/coarea mechanism extends the existing graphical-zonotope cut formula.

## Assumptions and scope
All simplices in \(W_n\) have coefficient exactly one; alternative realizations of combinatorially equivalent cyclohedra may have different Euclidean widths. Here \(C_3\) is the ordinary three-vertex cycle. The normal space is \(H=\{u\in\mathbb R^n:\sum_i u_i=0\}\); for nonzero \(u\in H\), directional width is
\[
w_{W_n}(u)/\|u\|_2=\frac{\max_{x\in W_n}u\cdot x-\min_{x\in W_n}u\cdot x}{\|u\|_2}.
\]
The all-cut formula assumes positive crossing weight on every nontrivial cut, ensuring a positive intrinsic width. The theorem is about Euclidean **minimal width**, not the largest inscribed ball, graph diameter, or lattice width.

## Proof
**Step 1: Euclidean width is achieved by a cut.** For the general simplex sum and any \(u\in H\), the directional width is the exactly additive functional
\[
F(u)=\sum_{B\in\mathcal H}a_B(\max_{i\in B}u_i-\min_{i\in B}u_i).
\]
Order the coordinates as \(u_{\sigma(1)}\le\cdots\le u_{\sigma(n)}\). Put \(g_j=u_{\sigma(j+1)}-u_{\sigma(j)}\ge0\), \(S_j=\{\sigma(j+1),\ldots,\sigma(n)\}\), and \(v_S=\mathbf1_S-|S|\mathbf1/n\). Then, exactly,
\[
u=\sum_{j=1}^{n-1}g_jv_{S_j},\qquad
F(u)=\sum_{j=1}^{n-1}g_jF(v_{S_j}),
\quad
\|v_S\|_2^2=\frac{|S|(n-|S|)}n.
\]
The second equality follows because the range of coordinates in each \(B\) equals the sum of precisely the gaps whose cuts separate members of \(B\). If \(\alpha=\min_S F(v_S)/\|v_S\|_2>0\), then
\[
F(u)\ge\alpha\sum_j g_j\|v_{S_j}\|_2\ge\alpha\|u\|_2.
\]
Taking \(u=v_S\) for a minimizing cut gives equality. Equality in the Euclidean triangle inequality for two different positive gaps is impossible: the corresponding centered indicators of two distinct proper nested cuts are nonparallel. Thus every minimizing direction is two-level, and minimizing cuts give all directions. For a simplex, \(F(v_S)\) is exactly its coefficient if \(B\) crosses the cut and zero otherwise. This proves the reduction with its normalization and equality classification.

**Step 2: Count crossing tubes.** The cycle has \(n\) distinct connected subsets of each size \(1,\ldots,n-1\) and one full set: \(|\mathcal B_n|=n(n-1)+1\). Fix nonempty proper \(S\subset[n]\), put \(s=|S|\), and let the cyclic run lengths of the two colors \(S\) and \(S^c\) be respectively \(r_1,\ldots,r_a\) and \(t_1,\ldots,t_a\). A connected subset entirely within a run of length \(r\) is one of its \(r(r+1)/2\) intervals. Therefore the number \(C(S)\) of tubes meeting both colors equals
\[
C(S)=n(n-1)+1-\sum_{j=1}^{a}\frac{r_j(r_j+1)}2
                         -\sum_{j=1}^{a}\frac{t_j(t_j+1)}2.
\]
Because \(T(r)=r(r+1)/2\) is strictly superadditive on positive integers, \(\sum_jT(r_j)\le T(s)\) and \(\sum_jT(t_j)\le T(n-s)\). Both equalities hold precisely when \(a=1\), i.e. \(S\) is a cyclic interval. Consequently
\[
C(S)\ge A_n+s(n-s),
\]
with equality exactly for cyclic intervals.

**Step 3: Optimize cut cardinality.** For a cyclic interval of size \(s\), its width-normalized cut cost is
\[
\sqrt n\,\frac{A_n+z}{\sqrt z},\qquad z=s(n-s).
\]
The real derivative of \((A_n+z)/\sqrt z\) is \((z-A_n)/(2z^{3/2})\). For \(n\ge5\), \(A_n\ge\lfloor n^2/4\rfloor\) (equality at \(n=5\)), so the expression strictly decreases across all admissible \(z\) until its maximum \(U_n\). The maximizing sizes are the two balanced sizes, and the formula follows. For \(n=4\), the two possible \(z\) are \(3\) and \(4\); their widths are respectively \(4\sqrt3\) and \(7\), and \(4\sqrt3<7\). For \(n=3\), only \(z=2\) occurs. Strictness in Steps 1–3 gives all equality cases and counts of normal lines. Elementary simplification gives the parity formulas and the stated asymptotic.

## Verification
The accompanying standalone \(\texttt{checker.py}\) directly builds every cyclic connected subset. It computes every cut cost using integer arithmetic and compares exact squared normalized costs with the asserted minimizing cuts for \(3\le n\le10\); it also evaluates directional widths directly from simplex support functions for 4,800 independently generated mean-zero unit vectors. The observed result is \(\texttt{VERIFY_OK}\). These finite checks corroborate but are not the proof for arbitrary \(n\); Steps 1–3 supply the all-\(n\) argument.

## Relationship to prior work
Padrol, Pilaud and Poullot (2021 preprint) explicitly construct graph associahedra as sums of the coordinate simplices indexed by tubes and identify cycle graph associahedra with cyclohedra; their mathematical focus is deformation cones, not Euclidean thickness. Cardinal, Pournin and Valencia-Pabon (2021) study the **graph-theoretic** diameter of associahedra, not minimal Euclidean support-plane separation. Jochemko and Ravichandran (2019 preprint, 2022 journal) analyze signed simplex sums and Minkowski-linear functionals, not this optimum over Euclidean directions.

The published result *The standard cyclohedron has a unique barycentric incenter* determines the **intrinsic inradius** \((n-1)^{3/2}/\sqrt n\) of exactly this simplex-sum realization; its theorem does not determine minimum width. In particular, the cyclohedron is not assumed centrally symmetric, and the two quantities cannot be identified by doubling the inradius. The published result *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant* proves the analogous graph-edge cut reduction for **centrally symmetric sums of segments**. Its proof shares the coarea idea used in Step 1, which is acknowledged as prior technique; it does not give the all-connected-subsets cycle count or the transition between singleton and balanced cuts.

## Limitations
The metric answer is specific to the standard unit-coefficient simplex-sum embedding. It does not classify optimal widths over all affine or deformed realizations, arbitrary weighted tube sums, or other norms. Previous work on graphical zonotopes supplies a closely related reduction; no novelty is asserted for layer-cake/coarea as an abstract technique. Although searches and inspected primary literature did not reveal the complete width formula for this realization, earlier work under other terminology could exist. Independent mathematical validation is not claimed.

## References
1. Katharina Jochemko and Mohan Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, arXiv:1909.08448 (initial 2019-09-18); *Mathematika* 68 (2022), 217–236, DOI 10.1112/mtk.12122.
2. Arnau Padrol, Vincent Pilaud and Germain Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200 (initial 2021-09-19); *European Journal of Combinatorics* 107 (2023), 103594.
3. Jean Cardinal, Lionel Pournin and Mario Valencia-Pabon, *Diameter estimates for graph associahedra*, arXiv:2106.16130 (initial 2021-06-30), *Annals of Combinatorics* 26 (2022), 873–902.
4. *The standard cyclohedron has a unique barycentric incenter*, public published-finding corpus mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-standard-cyclohedron-has-a-unique-barycentric-incenter--ee5aeb17987e.
5. *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, public published-finding corpus mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab.
