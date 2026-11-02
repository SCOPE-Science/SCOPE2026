# Distinct sharp cut and cycle projections for complete split graphs

## Finding
Let \(a,b\ge 2\) be integers, and let \(G_{a,b}=K_a\vee\overline{K_b}\), the unweighted complete split graph formed by joining every vertex of a clique of size \(a\) to every vertex of an independent set of size \(b\). Its oriented real edge space \(E_{a,b}\) carries the coordinate \(\ell_1\) norm. Write \(C_{a,b}\) for the cut (gradient) space and \(Z_{a,b}\) for the circulation (divergence-zero) space. Define
\[
 n=a+b,\qquad
 d_C=2b(n-1)+(a-1)(a+2b-2),\qquad
 d_Z=2b(n-3)+(a-1)(a+2b-4),
\]
\[
 B_C=\frac{a+2b-2}{d_C},\quad A_C=\frac{1-bB_C}{a},\qquad
 B_Z=\frac{a+2b-4}{d_Z},\quad A_Z=\frac{1-bB_Z}{a}.
\]
Then the unrestricted relative projection constants are exactly
\[
 \boxed{\lambda(C_{a,b},E_{a,b})=2(n-1)A_C},\qquad
 \boxed{\lambda(Z_{a,b},E_{a,b})=1+2(n-3)A_Z}.
\]
The first minimum is attained by the explicitly defined projection \(P_{A_C,B_C}\) below, and the second by \(I-P_{A_Z,B_Z}\). Both minimizers are unique among projections invariant under permutations of the clique and independent-set vertices. They are different: **no projection onto the cut space simultaneously minimizes its own norm and the norm of its complementary cycle-space projection**. Moreover, the Euclidean orthogonal cut projection minimizes the \(\ell_1\) norm exactly when \(a=2\); its complementary orthogonal circulation projection minimizes that norm exactly when \(a=4\). All conclusions hold for every \(b\ge2\).

## Assumptions and scope
Orient clique edges from their smaller to their larger label and each cross edge from the clique to the independent set. Represent an edge flow by an antisymmetric clique matrix \(X\) and a rectangular matrix \(Y\). Set
\[
 k_i=\sum_{j=1}^a X_{ij},\quad h_i=\sum_{u=1}^bY_{iu},\quad
 g_u=\sum_{i=1}^aY_{iu},\quad s=\sum_{i,u}Y_{iu}.
\]
The cut space consists of gradients \(\nabla(\phi,\psi)\) with clique coordinates \(\phi_i-\phi_j\) and cross coordinates \(\phi_i-\psi_u\). The circulation space is its Euclidean orthogonal complement. For real \(A,B\) satisfying \(aA+bB=1\), set
\[
 \phi_i=A k_i+B(h_i-s/a),\qquad \psi_u=-g_u/a,
 \qquad P_{A,B}(X,Y)=\nabla(\phi,\psi).
\]
This is a projection onto \(C_{a,b}\). The parameter restrictions \(a,b\ge2\) are essential to the formulas and to the sharp separation statement.

## Proof
**1. Projection identity and invariant normal form.** For a gradient of vertex potentials \((v_i,w_u)\), direct summation gives \(k_i=a(v_i-\bar v)\), \(h_i-s/a=b(v_i-\bar v)\), and \(g_u=a(\bar v-w_u)\). Since \(aA+bB=1\), the above map returns clique potentials \(v_i-\bar v\) and outer potentials \(w_u-\bar v\). Thus \(P_{A,B}\) fixes every gradient and has range in the cut space, proving \(P_{A,B}^2=P_{A,B}\).

Every projection can be averaged over \(S_a\times S_b\), acting by signed coordinate permutations on edges. Averaging preserves the projection property and cannot increase either \(\|P\|_1\) or \(\|I-P\|_1\). Every invariant projection onto the cut space has the displayed form: fix the mean clique potential to be zero. Equivariance forces its clique potential to be a linear combination \(A k_i+B(h_i-s/a)\), because antisymmetric clique edges contribute only the signed incidence sum and cross edges contribute only the centered row sum. Its outer potential is a linear combination of \(g_u-s/b\) and \(s\), since the outer-coordinate stabilizers have only a distinguished-column and a common coefficient. Requiring that all gradients be fixed forces the outer potential to equal \(-g_u/a\) and \(aA+bB=1\). This also proves the uniqueness of the parameter pair for an invariant projection.

**2. Exact edge-column norms.** The \(\ell_1\) operator norm is the largest absolute column sum. The group has two edge orbits: a clique edge and a cross edge. Counting their coefficients in the displayed potential formula gives
\[
 \begin{aligned}
 F_{CC}(A)&=2(n-1)|A|,\\
 F_{CP}(B)&=\frac{|1+(a-1)B|+(a-1)|1-B|}{a}
       +\frac{(a-1)(a+2b-2)}{a}|B|,\\
 H_{CC}(A)&=|1-2A|+2(n-2)|A|,\\
 H_{CP}(B)&=\frac{a-1}{a}\bigl(2|1-B|+(a+2b-2)|B|\bigr).
 \end{aligned}
\]
Here \(\|P_{A,B}\|_1=\max\{F_{CC}(A),F_{CP}(B)\}\) and \(\|I-P_{A,B}\|_1=\max\{H_{CC}(A),H_{CP}(B)\}\). To reproduce the counts: a clique-edge column has two nonzero clique potentials \(\pm A\), producing one \(2A\) clique entry, \(2(a-2)\) further clique entries of magnitude \(|A|\), and \(2b\) cross entries of magnitude \(|A|\). A cross-edge column has clique potentials \((a-1)B/a\) at its initial vertex and \(-B/a\) elsewhere, and outer potential \(-1/a\) at its final vertex and zero elsewhere. The four rectangular blocks have respective multiplicities \(1,b-1,a-1,(a-1)(b-1)\); clique contributions are \((a-1)|B|\). Subtracting these columns from the identity yields the two \(H\) formulas.

**3. Global cut minimum.** Put \(h=(a-1)(a+2b-2)/a>0\). The triangle inequality implies \(|1+(a-1)B|+(a-1)|1-B|\ge a\), so for every real feasible pair,
\[
 \|P_{A,B}\|_1\ge\max\{2(n-1)|A|,\ 1+h|B|\}.
\]
If this norm is at most \(L\), then
\[
 1=|aA+bB|\le a|A|+b|B|
 \le\frac{aL}{2(n-1)}+\frac{b(L-1)}h.
\]
Consequently \(L\ge 2(n-1)(h+b)/(ah+2b(n-1))\). The two bounds intersect, with \(A,B>0\), at \((A_C,B_C)\) displayed above. More explicitly, at \(B=0\) the first affine bound exceeds the second, whereas at \(B=1/b\) it is zero and the second is strictly positive. Their intersection lies in \(0<B<1/b\), and then \(0<A<1/a\). At that intersection the earlier triangle inequality is an equality, so both column types have norm \(L\). This proves the first exact formula and, through saturation of both strict affine bounds, uniqueness of the invariant minimizer.

**4. Global circulation minimum.** Put \(c=2(a-1)/a\) and \(j=(a-1)(a+2b-4)/a>0\). The elementary inequalities \(|1-2A|\ge1-2|A|\) and \(|1-B|+|B|\ge1\) show that
\[
 \|I-P_{A,B}\|_1\ge
 \max\{1+2(n-3)|A|,\ c+j|B|\}.
\]
If its norm is at most \(L\), then
\[
 1\le\frac{a(L-1)}{2(n-3)}+\frac{b(L-c)}j.
\]
The sharp intersection of these two affine bounds occurs at \((A_Z,B_Z)\). It again lies in \(0<B<1/b\), \(0<A<1/a\le1/2\): at \(B=0\) the first bound is larger, and at \(B=1/b\) the second is larger. In this interval both preceding elementary inequalities are equalities. Thus the second exact formula holds and its invariant minimizing parameter is unique. Complementation exchanges projections onto cut and cycle, so this minimum is the unrestricted circulation-space projection constant.

**5. Incompatibility and orthogonal thresholds.** Direct cross multiplication yields
\[
 B_Z-B_C=\frac{4b(b-1)}{d_Cd_Z}>0.
\]
If a single projection optimized both costs, its group average would also optimize both, contradicting uniqueness and this strict inequality. The Euclidean orthogonal cut projection is \(P_{1/n,1/n}\), as follows either from the graph-Laplacian inverse or from symmetry of the matrix coefficients between the two edge orbits. Direct expansion gives \(n(a+2b-2)-d_C=-(a-2)(b-1)\) and \(n(a+2b-4)-d_Z=-(a-4)(b-1)\). Since \(b\ge2\), the orthogonal projection is cut-optimal exactly at \(a=2\) and its complementary projection is cycle-optimal exactly at \(a=4\). This completes the proof.

## Verification
The accompanying `CHECKER.py` uses Python's exact rational arithmetic and reconstructs all edge columns for every \(2\le a,b\le8\). It checks gradient fixing, projection properties, every formula, the strict parameter separation, and the orthogonal thresholds, for 49 parameter pairs and 1813 edge columns. Separately, direct unrestricted linear programs for \((a,b)=(2,2),(3,2),(3,3),(4,2)\) agreed with the exact constants to numerical tolerance; these checks are supplementary, not the infinite proof. For instance, the two minima are \(3/2\) and \(4/3\) for \((2,2)\), and \(115/66\) and \(27/14\) for \((3,3)\). Reproduce the exact checker with `python3 CHECKER.py`.

## Relationship to prior work
The invariant-projection method for graph cycle spaces is developed in Dilworth–Kutzarova–Ostrovskii (2018, 2023), with specific applications to diamond and Laakso graphs, discrete tori, and Hamming graphs. The present complete-split-graph family has two non-equivalent edge orbits and a one-parameter family of invariant projections; neither the two sharp split-graph formulas nor their incompatible minimizers follow from the inspected specialized formulas in those works. The 2020 Laakso analysis concerns recursive graphs with different operator structure. Complete bipartite graphs and balanced complete multipartite graphs have different edge-orbit and part-size hypotheses; their sharp constants do not imply these asymmetric split-graph constants. No priority claim beyond the described comparisons is warranted.

## Limitations
The theorem concerns **real, finite, unweighted** complete split graphs and the coordinate \(\ell_1\) edge norm. It does not classify arbitrary nonsymmetric minimizers, nonuniform edge weights, arbitrary complete multipartite graphs, or norms \(\ell_p\) with \(p\ne1\). Literature under alternate electrical-network or operator-projection terminology might contain equivalent results and has not been exhaustively ruled out. Independent mathematical audit has not been performed.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first public version 2018-07-10), https://arxiv.org/abs/1807.03814.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, arXiv:2007.07949 (first public version 2020-07-15), https://arxiv.org/abs/2007.07949.
3. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public version 2023-05-21), https://arxiv.org/abs/2305.12582.
