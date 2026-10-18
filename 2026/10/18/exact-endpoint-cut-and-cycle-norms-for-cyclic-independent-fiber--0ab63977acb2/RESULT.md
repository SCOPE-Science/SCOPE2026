# Exact endpoint cut and cycle norms for cyclic independent-fiber graph blow-ups

## Finding

For every integer \(n\ge5\) and every integer \(r\ge1\), replace each vertex of the unit-edge cycle \(C_n\) by an independent set of \(r\) vertices, and each cycle edge by all \(r^2\) edges between its two vertex sets. Denote the resulting simple graph by \(G_{n,r}=C_n[\overline{K}_r]\). Equip its real oriented edge-coordinate space with its usual \(\ell_1\) or \(\ell_\infty\) norm. Let \(Q\) be the Euclidean orthogonal projection onto its graph-gradient (cut) space and let \(C=I-Q\) be the complementary Euclidean orthogonal projection onto its circulation (cycle) space.

Then, with no dependence on the parity of \(n\),
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=4-\frac2r-\frac4n+\frac{2}{nr^2},}
\]
\[
\boxed{\|C\|_{1\to1}=\|C\|_{\infty\to\infty}=5-\frac4r-\frac4n+\frac{4}{nr^2}.}
\]
Consequently,
\[
\boxed{\|C\|_{1\to1}-\|Q\|_{1\to1}=1-\frac2r+\frac{2}{nr^2}.}
\]
The unsplit cycle \(r=1\) has strictly larger cut norm, whereas **every independent-fiber blow-up of width \(r\ge2\)** has strictly larger cycle norm. At the minimal width \(r=2\), the positive difference is exactly \(1/(2n)\); thus the threshold is sharp. For fixed \(n\), the limiting norms as \(r\to\infty\) are \(4-4/n\) and \(5-4/n\), respectively. Both global bounds \(\|Q\|<4\) and \(\|C\|<5\) are optimal over the stated family, approached as both parameters grow.

## Assumptions and scope

Vertices are \((x,i)\), with \(x\in\mathbb Z/n\mathbb Z\) and \(i\in\{1,\ldots,r\}\); the only edges join \((x,i)\) to \((x+1,j)\) for arbitrary \(i,j\). Each undirected edge occurs exactly once because \(n\ge5\). Reference orientations point from layer \(x\) to layer \(x+1\). Thus the graph has \(nr\) vertices, \(nr^2\) edges and degree \(2r\). The projections are canonical *Euclidean-orthogonal* ones, not minimizers over all (possibly nonorthogonal) projections. No intermediate \(\ell_p\) operator norm is claimed.

Let \(B\) be the oriented vertex-by-edge incidence matrix with each column equal to the tail indicator minus the head indicator. With the graph Laplacian \(L=BB^{\mathsf T}\) and its Moore--Penrose inverse \(L^+\), the cut projection is \(Q=B^{\mathsf T}L^+B\). As a real symmetric projector, \(Q\) has equal \(\ell_1\) column-sum and \(\ell_\infty\) row-sum operator norms; so does \(C=I-Q\).

## Proof

**Step 1: Laplacian splitting.** Write \(L_n=2I-A_n\) for the Laplacian of the cycle \(C_n\), \(P=J_r/r\) for orthogonal projection onto constant fiber vectors, and \(P^\perp=I-P\). The adjacency matrix of \(G_{n,r}\) is \(A_n\otimes J_r\), hence
\[
L=rL_n\otimes P+2rI_n\otimes P^\perp,
\qquad
L^+=r^{-1}L_n^+\otimes P+(2r)^{-1}I_n\otimes P^\perp.
\]
The two summands act on orthogonal invariant subspaces. The formula for \(L^+\) follows from \(\ker L_n=\operatorname{span}\{\mathbf1\}\) and invertibility of the second summand on every mean-zero fiber.

**Step 2: Every transfer current.** Fix the oriented source edge \(e=((0,a),(1,b))\). Let \(g=L_n^+(\mathbf e_0-\mathbf e_1)\). The base-cycle potential differences satisfy
\[
g_x-g_{x+1}=\begin{cases}(n-1)/n,&x=0,\\-1/n,&x\ne0.\end{cases}\]
Indeed, this is the unique gradient flow with unit source at \(0\), unit sink at \(1\), and total potential difference zero around the cycle. The potential of the blown-up edge, \(\phi=L^+(\mathbf e_{(0,a)}-\mathbf e_{(1,b)})\), has coordinates
\[
\phi_{x,i}=\frac{g_x}{r^2}+
\frac{\mathbf1_{x=0}(\mathbf1_{i=a}-1/r)-\mathbf1_{x=1}(\mathbf1_{i=b}-1/r)}{2r}.
\]
For a row edge \(f=((x,i),(x+1,j))\), the entry \(Q_{f,e}\) equals \(\phi_{x,i}-\phi_{x+1,j}\). The exact signed values and their multiplicities in the source column are:

| Layer boundary | Clone condition | Value | Multiplicity |
| --- | --- | --- | ---: |
| \(0\to1\) | \(i=a,\ j=b\) | \((r-1/n)/r^2\) | \(1\) |
| \(0\to1\) | exactly one of \(i=a,\ j=b\) | \((r/2-1/n)/r^2\) | \(2(r-1)\) |
| \(0\to1\) | neither equality | \(-1/(nr^2)\) | \((r-1)^2\) |
| \(1\to2\) | \(i=b\) | \(-((r-1)/2+1/n)/r^2\) | \(r\) |
| \(1\to2\) | \(i\ne b\) | \((1/2-1/n)/r^2\) | \(r(r-1)\) |
| \((n-1)\to0\) | \(j=a\) | \(-((r-1)/2+1/n)/r^2\) | \(r\) |
| \((n-1)\to0\) | \(j\ne a\) | \((1/2-1/n)/r^2\) | \(r(r-1)\) |
| other \(n-3\) boundaries | any clones | \(-1/(nr^2)\) | \((n-3)r^2\) |

All signs are as displayed for \(n\ge5\), \(r\ge1\) whenever the corresponding multiplicity is nonzero. This is a full determination of the rooted electrical-current column, not just its aggregate norm.

**Step 3: Absolute sums and complementary projector.** Summing absolute values in the table gives
\[
\begin{aligned}
\|Q\mathbf e_e\|_1
&=1+\frac{r^2-4r+2}{nr^2}
 +\frac{2(r-1)}r+\frac{2(2-r)}{nr}+\frac{n-3}{n}\\
&=4-\frac2r-\frac4n+\frac{2}{nr^2}.
\end{aligned}
\]
The graph is edge-transitive by cyclic rotations and independent permutations of clones in each fiber. Conjugation of the orthogonal projector by the induced signed coordinate permutations therefore makes every column absolute sum equal to this value. The source diagonal entry is the effective resistance \(Q_{e,e}=r^{-1}-(nr^2)^{-1}\), strictly between zero and one. Consequently
\[
\|C\mathbf e_e\|_1=1+\|Q\mathbf e_e\|_1-2Q_{e,e}
=5-\frac4r-\frac4n+\frac{4}{nr^2}.
\]
Symmetry of both projectors gives the corresponding \(\ell_\infty\) identities.

**Step 4: Sharp sign change and limits.** For \(r=1\) the difference is \(-1+2/n<0\). For any integer \(r\ge2\) it is \(1-2/r+2/(nr^2)>0\), with \(r=2\) yielding \(1/(2n)\). Both norms remain below \(4\) and \(5\), respectively, and converge to them along \(n,r\to\infty\), proving optimality of these global bounds.

## Verification

The self-contained Python 3 standard-library program `check_cycle_blowup.py` independently constructs and inverts a grounded integer graph Laplacian using exact fractions. It reconstructs *every* canonical-projector column for nine parameter pairs, covering \(259\) edge columns in total, and checks all diagonal entries, absolute column sums, symmetry, and the original incidence divergences. Execute `python check_cycle_blowup.py` beside this file. This finite test is corroboration; the proof above establishes the infinite-parameter result.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii [1] supply the Banach-space motivation and cycle-space projection framework, treating discrete tori and Hamming graphs in depth. The present graph uses independent vertex fibers connected by complete bipartite links, which is neither a Cartesian Hamming graph nor, for \(n\ge5\), a complete multipartite graph. The known complete multipartite cases at base cycle sizes three and four, and ordinary cycles at fiber size one, are boundaries rather than new cases of the claim. Polettini [2] develops general cycle/cocycle oblique projection algebra, but does not supply these canonical orthogonal endpoint norms. The exact fiber-splitting transfer-current computation and absolute-norm formula for \(n\ge5\) distinguish the present result. The *difference* of the two canonical norms, once the common off-diagonal sum is known, is \(1-2Q_{e,e}\); for an edge-transitive graph the diagonal itself also follows from the classical effective-resistance sum (Foster identity). Thus the scalar dominance threshold by itself is not asserted to be a new general principle; the new content is the complete signed current profile and resulting absolute endpoint norms.

## Limitations

The claim is restricted to integer uniform independent-fiber widths and unweighted graph edges. It does not determine minimum norms among all projections, nonlinear analogues, arbitrary unbalanced fiber sizes, or intermediate \(\ell_p\) norms. Similar formulas under an alternative electrical-network presentation may exist in less readily indexed literature; no uniqueness assertion is made.

## References

[1] S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first version posted 2023-05-21; especially Sections 1.1, 2.1, 2.6, 2.7. https://arxiv.org/abs/2305.12582

[2] M. Polettini, *Cycle/cocycle oblique projections on oriented graphs*, arXiv:1405.0899, 2014; especially Sections 2 and 3. https://arxiv.org/abs/1405.0899
