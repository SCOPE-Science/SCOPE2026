# Exact edge-erasure sensitivity of gradient projections on rectangular bicliques

## Finding
Let \(a,b\ge2\), let \(G=K_{a,b}\), and remove precisely one edge \(e_0\) to obtain \(G^-\). Orient every edge from the first vertex class to the second, and denote by \(P_G\) and \(P_{G^-}\) the Euclidean orthogonal projectors onto all discrete gradient edge flows. With the coordinatewise supremum norm, the **exact sensitivity identity** is
\[
\boxed{\|P_{G^-}\|_{\infty\to\infty}=\|P_G\|_{\infty\to\infty}-\frac{2}{ab(a-1)(b-1)}}
\]
where
\[
\|P_G\|_{\infty\to\infty}=1+\frac{2(a-1)(b-1)}{ab}.
\]
For \(a,b>2\), precisely the edges disjoint from \(e_0\) attain the maximum row norm. At \(a=2<b\), the rows incident to the first-class endpoint of \(e_0\) also attain the maximum; the analogous statement holds with the classes exchanged. At \(a=b=2\), the surviving graph is a tree and every row norm equals one. For every maximizing row there is an input with all edge entries of modulus one realizing the operator norm.

In particular, the deletion **strictly reduces** the worst possible componentwise amplification, even though one measurement has been removed. In a balanced family with \(a=b=n\), the exact decrement is \(2/[n^2(n-1)^2]\); in an unbalanced family with fixed \(b\) and \(a\to\infty\), it is asymptotic to \(2/[a^2b(b-1)]\).

## Assumptions and scope
The two vertex classes have cardinalities \(a,b\ge2\), and edges have unit conductance. Edge arrays are real or complex, with unweighted Euclidean inner product for defining the projector and \(\ell^\infty\) for measuring it. If \(B\) is the edge-by-vertex signed incidence matrix, the projector is \(B(B^{\mathsf T}B)^\dagger B^{\mathsf T}\). The superscript dagger means the Moore–Penrose inverse. All \(a,b\) are finite integers; no claim is made about weighted edges or deleting more than one edge.

Write vertices as \(i=1,\ldots,a\) and \(j=1,\ldots,b\), so an edge is \((i,j)\); relabel the deleted edge as \(e_0=(1,1)\). Classify retained edges into \(A=(1,j),\ j>1\), \(B=(i,1),\ i>1\), and \(C=(i,j),\ i,j>1\). The lettering here refers only to three edge orbits.

## Proof
**Complete graph projector.** The gradient space on \(K_{a,b}\) is the space of arrays of the form \(u_i-v_j\), or equivalently \(u_i+w_j\). Orthogonal least-squares fitting is two-way additive centering, giving the full projector matrix
\[
P_{(i,j),(k,l)}=\frac{\mathbf1_{i=k}}b+\frac{\mathbf1_{j=l}}a-\frac1{ab}.
\]
Each row sums to one, since the all-one edge array is a gradient. The only negative coefficients of a row are its \((a-1)(b-1)\) entries disjoint from that edge; each equals \(-1/(ab)\). Therefore the absolute row sum is \(1+2(a-1)(b-1)/(ab)\), independent of the row.

**Deletion identity.** Let \(R\) restrict full edge arrays to all edges other than \(e_0\), and let \(e\) be the coordinate vector at \(e_0\). Because \(G^-\) remains connected for all \(a,b\ge2\), restriction is injective on the full gradient subspace. Choose an orthonormal column basis \(U\) for this subspace. The restricted Gram matrix is \(U^{\mathsf T}(I-ee^{\mathsf T})U=I-uu^{\mathsf T}\), where \(u=U^{\mathsf T}e\). Its inverse is \(I+uu^{\mathsf T}/(1-\|u\|_2^2)\). Thus
\[
P_{G^-}=RPR^{\mathsf T}+\frac{(RPe)(RPe)^{\mathsf T}}{1-P_{e,e}},
\qquad 1-P_{e,e}=\frac{(a-1)(b-1)}{ab}>0.
\]
The entries of \(RPe\) are exactly \((a-1)/(ab)\) on orbit \(A\), \((b-1)/(ab)\) on \(B\), and \(-1/(ab)\) on \(C\). Hence all entries of the deleted-edge projector are explicit rational functions of \(a,b\).

**Exact signed-row calculation.** As the all-one retained-edge array is still a gradient, every row sums to one. Its absolute row sum equals one plus twice the absolute mass of its negative entries. For a row in \(A\), negative entries occur precisely at the \((a-1)(b-2)\) columns in \(C\) having a different second coordinate; each equals \(-1/[a(b-1)]\). For a row in \(B\), negative entries occur precisely at the \((b-1)(a-2)\) columns in \(C\) having a different first coordinate; each equals \(-1/[b(a-1)]\).

For a row \((i,j)\in C\), its negative entries are: the \(b-2\) columns \((1,l)\) with \(l\ne1,j\), each \(-1/[a(b-1)]\); the \(a-2\) columns \((k,1)\) with \(k\ne1,i\), each \(-1/[b(a-1)]\); and the \((a-2)(b-2)\) columns \((k,l)\in C\) with \(k\ne i\) and \(l\ne j\), each \(-(ab-a-b)/[ab(a-1)(b-1)]\). The last coefficient is nonpositive because \(ab-a-b\ge0\) for \(a,b\ge2\). The remaining coefficients are nonnegative: on the two same-coordinate portions of \(C\), their numerators include respectively \(a(a-2)(b-1)+b>0\) and \(b(b-2)(a-1)+a>0\); the diagonal is positive, and the same-coordinate exceptional columns in \(A,B\) equal \((b-2)/[a(b-1)]\) and \((a-2)/[b(a-1)]\).

It follows by summing these negative masses and simplifying that the three absolute row sums are
\[
\begin{aligned}
L_A&=1+\frac{2(a-1)(b-2)}{a(b-1)},\\
L_B&=1+\frac{2(b-1)(a-2)}{b(a-1)},\\
L_C&=1+\frac{2(a-1)(b-1)}{ab}-\frac{2}{ab(a-1)(b-1)}.
\end{aligned}
\]
The final comparisons factor exactly:
\[
L_C-L_A=\frac{2(a-2)}{b(a-1)(b-1)},\qquad
L_C-L_B=\frac{2(b-2)}{a(a-1)(b-1)}.
\]
Both are nonnegative, with the stated equality cases. This proves the sharp formula and the entire maximizing-row classification, including \(a=b=2\).

**Attainment and asymptotics.** For any maximizing row \(r\), choose each input edge entry to be the sign of its real row coefficient (choosing either sign for zeros). Then \(\|(P_{G^-}x)_r\|=\sum_s |(P_{G^-})_{rs}|\) with \(\|x\|_\infty=1\); the same argument works over complex scalars. The exact decrement has the claimed asymptotic forms by elementary division.

## Verification
The standalone file `edge_erasure_checker.py` constructs the projector independently through the grounded incidence Gram matrix, using exact rational arithmetic in SymPy. It checks idempotence, self-adjointness, every row formula, and the sharp value for all pairs \(2\le a,b\le8\). All 49 graph instances and 1,176 row-norm comparisons passed. This finite verification supplements the preceding proof for all integers; it is not an exhaustive proof by enumeration.

Run using `python edge_erasure_checker.py` with Python 3 and SymPy installed.

## Relationship to prior work
Graph Hodge decomposition identifies orthogonal gradient projection with least-squares potential recovery, as discussed by Jiang–Lim–Yao–Ye (2008). The transfer-current framework and its Green-function representation appear in Kassel–Wu (2013). Neither of those inspected treatments provides the sharp deleted-biclique maximum-coordinate stability identity or the maximizing-edge classification. The unrestricted complete-bipartite norm is an elementary baseline. Previously considered balanced deleted-matching instances concern equal part sizes; their statements do not determine the rectangular two-parameter identity without the present off-balance calculation. This comparison does not establish absolute novelty across unindexed literature.

## Limitations
This is an exact special-family theorem, not a universal stability law for arbitrary graphs, multiple deletions, or edge weights. A deletion can change the operator norm in other directions for different graphs. The proof relies on unit conductances, a single omitted edge, and the oriented bipartite incidence convention. The small size of the exact decrement does not imply a similarly small change of every projector entry. No independent external validation is claimed.

## References
1. X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067 (first public 2008-11-07), Sections 2–4.
2. A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946 (first public 2013-12-10), Sections 1–2.
