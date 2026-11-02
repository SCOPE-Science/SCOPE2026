# Five three-round theories of lattices of flats of uniform matroids

## Finding
For integers \(2\le r<n\), let \(U_{r,n}\) be the uniform matroid of rank \(r\) on an \(n\)-element set, and let \(\mathcal F_{r,n}\) denote its lattice of flats in the signature \(\{\subseteq,=\}\). For all \(2\le r<n\) and \(2\le s<m\),
\[
\boxed{\mathcal F_{r,n}\equiv_3\mathcal F_{s,m}\quad\Longleftrightarrow\quad\min(r,6)=\min(s,6).}
\]
Here \(\equiv_3\) is agreement on all first-order sentences of quantifier rank at most three. In particular, ground-set size is invisible at this depth once it exceeds matroid rank; exactly five theories occur, represented by ranks \(2,3,4,5,6\). Their smallest within-family representatives have respectively \(5,12,27,58,121\) flats. The bound of \(121\) flats for representatives of every theory is sharp.

## Assumptions and scope
Every rank is an integer at least two, every ground-set size is strictly greater than rank, and the sole nonlogical relation is inclusion of flats. The parameters do not name individual ground-set elements, cardinalities, rank predicates, or matroid operations. The lattice of flats is the concrete poset
\[
\mathcal F_{r,n}=\{X\subseteq[n]:|X|\le r-1\}\cup\{[n]\}.
\]
All quantifier-rank comparisons refer to the three-round Ehrenfeucht--Fraisse game on these posets, with equality included.

## Proof
**1. Exact three-round type reduction.** Write \(h=r-1\). If two elements \(X,Y\) have been selected, partition the ground set into the four cells
\[
A=X\cap Y,\quad B=X\setminus Y,\quad C=Y\setminus X,\quad D=[n]\setminus(X\cup Y),
\]
with cell sizes \((a,b,c,d)\). For any proper flat \(Z\), write its four intersection sizes as \((u_A,u_B,u_C,u_D)\). Such a quadruple represents a permitted third selection precisely when \(0\le u_i\le |i|\) and \(\sum u_i\le h\). The third selection may alternatively be \([n]\), which is always allowed. Comparability of \(Z\) with \(X,Y\) is determined by these four counts: for example \(Z\subseteq X\) iff \(u_C=u_D=0\), and \(X\subseteq Z\) iff \(u_A=a,u_B=b\). The corresponding two criteria for \(Y\) interchange \(B,C\). This supplies an exact formula for the one-round extension signature \(\Sigma_h(a,b,c,d)\): it consists of all triples of relations in \(\{=,<,>,\parallel\}\) attainable with \(Z\), including \(Z=[n]\).

In this formula each coordinate of \(Z\) needs only three choices: empty, full, or nonempty and not full. For the last choice, selecting one element minimizes total size. Thus a table of at most \(3^4=81\) choices determines the exact signature, with no approximation and for arbitrary cell sizes. This is implemented literally by the standalone `check.py`. Equality and strict/non-strict inclusion are explicitly treated; the selected vertices may be repeated.

**2. A pointed two-round compression lemma.** Fix a *proper* flat \(X\), put \(s=|X|\), \(t=h-s\), and put \(e=n-h\ge2\). The set of one-round signatures after all possible second choices \(Y\) depends exactly on
\[
(\min(s,3),\min(t,2)). \tag{1}
\]
A direct verification of this finite combinatorial lemma proceeds as follows. For a proper \(Y\), write \(a=|X\cap Y|\), \(b=s-a\), \(c=|Y\setminus X|\), and \(d=e+t-c\). Its admissibility is
\[
0\le a\le s,\quad b=s-a,\quad 0\le c\le\min(b+t,e+t),\quad d=e+t-c.
\]
A useful explicit form of the case calculation is that, for two proper flats with the above parameters, the complete third-extension signature is determined by the six capped data
\[
\bigl(\min(a,2),\min(b,2),\min(c,2),\min(t,2),\min(b+t-c,2),\max(-1,\min(t-c,2))\bigr).\tag{2}
\]
To obtain (2), write down the four exact subset tests \(Z\subseteq X\), \(X\subseteq Z\), \(Z\subseteq Y\), \(Y\subseteq Z\) using empty/full statuses of the four cells, then minimize \(|Z|\) among statuses producing each of the sixteen possible pairs of order relations. The only full-region cardinality costs that can control the rank limit are \(a+b\), \(a+c\), and \(a+b+c\), so their spare capacities are exactly \(t\), \(b+t-c\), and \(t-c\). At most two further chosen elements matter. A full outside cell is never required by any subset test; the possible lack of an outside element is compensated by the two opposite difference cells whenever the union exceeds the rank bound, because \(n\ge h+2\). This supplies a finite, exhaustive derivation of (2) directly from the 81 statuses.

The 81-choice formula and (2) give the following exact elementary *pumping identities* for the collection of attainable signatures. In the few cases where one of the six caps changes, the unchanged signature follows by evaluating the empty/full/partly-selected states; no numerical convergence argument is used:

(a) Once \(e\ge2\), increasing the outside-cell capacity does not create a new signature. Indeed, if \(c>t+2\), set \(\delta=c-t-2\). Then \(b\ge\delta+2\), and the proper pair signature is unchanged by replacing \((a,b,c)\) with \((a+\delta,b-\delta,t+2)\). The replacement fits in \(n=h+2\); if \(c\le t+2\), the original pair already fits. The case \(Y=[n]\) has the same signature for all \(e\ge2\). Thus \(e\) can be reduced to \(2\).

(b) At \(e=2\), when \(t\ge3\), decreasing \(t\) by one preserves the set of proper-pair signatures. For the forward implication keep \(a,b\) and replace \(c\) by \(c-1\) if \(c\ge3\), otherwise leave \(c\) fixed. For the inverse implication increase \(c\) by one if \(c\ge2\), otherwise leave it fixed. Here \(h\) and \(n\) change together. When \(c\ge3\), the clipped cell statuses and relevant rank slacks are unchanged; when \(c\le2\), the only exceptional threshold patterns are the finitely many possibilities \(c\in\{0,1,2\}\), checked directly by the same 81-choice formula.

(c) At \(e=2\), when \(s\ge6\), decreasing \(s\) by one preserves the signatures: if \(a\ge3\), decrease \(a\) by one; otherwise decrease \(b\) by one. In the reverse direction increase \(a\) when \(a\ge2\), otherwise increase \(b\). The cell-size cutoffs are unchanged, except the boundary \(b=4,c=t+2\), which gives the same signature by direct inspection of the 81 possibilities. These moves preserve admissibility and all non-exceptional rank slacks. Finally, the finite cases \(s=3,4,5\) with \(t=0,1,2\) give identical signature sets for each fixed \(t\). They are fully enumerated by the formula in step 1. Combining (a)--(c) proves that the pointed profile depends only on the two truncations in (1). In particular this is an *all-parameter* case reduction, not an induction from experimentally sampled dimensions.

For transparency, the canonical table of numbers of pair signatures in the proper pointed profile, with rows \(\min(s,3)=0,1,2,3\) and columns \(\min(t,2)=0,1,2\), is
\[
\begin{array}{c|ccc} &0&1&2\\\hline 0&\text{not admissible}&3&4\\1&4&6&8\\2&6&8&9\\3&8&9&10\end{array}.
\]
These eleven canonical pointed signatures are pairwise distinct as *sets* of full pair signatures (equal cardinalities in the table are not identification criteria). Their actual contents, rather than just their sizes, are compared in the verification program. If \(X=[n]\), its two-round pointed profile has a separate type for \(r=2\) and one common type for every \(r\ge3\), by the same four-cell test.

**3. Equivalence.** In a three-round Ehrenfeucht--Fraisse game, the first move leaves precisely two rounds. The previous lemma therefore gives the complete types of first-move positions. For \(r\ge6\), every admissible clipped pair in the preceding table occurs: \(s=0,1,2\), an interior \(3\le s\le r-3\), and the top-near values \(s=r-2,r-1\); their sets of two-round types do not depend on \(r\) or \(n\). The top type is also common. Hence every two such lattices are three-round equivalent. For fixed ranks \(2\le r\le5\), the same lemma and \(n\)-compression give equivalence for all \(n>r\).

**4. Sharp separation.** In the poset signature write \(x<y\) for \(x\subseteq y\) and \(x\ne y\). With \(x\) a proper flat, define formulas of quantifier rank at most two after \(x\):
\[
\begin{aligned}
L_1(x)&:=\exists y\ (y<x),\\
L_2(x)&:=\exists y\exists z\ (z<y<x),\\
L_3(x)&:=\exists y\bigl(y<x\land\exists z(z<y)\land\exists z(y<z<x)\bigr),\\
U_1(x)&:=\exists y\exists z\ (x<y<z),\\
U_2(x)&:=\exists y\bigl(x<y\land\exists z(y<z)\land\exists z(x<z<y)\bigr).
\end{aligned}
\]
For proper \(x\), these express respectively \(|x|\ge1\), \(|x|\ge2\), \(|x|\ge3\), \(t\ge1\), and \(t\ge2\). Consequently each of
\[
\exists x\,(L_1(x)\land U_1(x)),\quad
\exists x\,(L_2(x)\land U_1(x)),\quad
\exists x\,(L_3(x)\land U_1(x)),\quad
\exists x\,(L_3(x)\land U_2(x))
\]
has quantifier rank at most three and is true exactly for ranks at least \(3,4,5,6\), respectively. Therefore none of the five classes can merge.

Finally \(|\mathcal F_{r,n}|=1+\sum_{i=0}^{r-1}\binom ni\). This is minimized within a class at the least permitted rank and at \(n=r+1\). The stable class begins at \((r,n)=(6,7)\), where the count is \(121\); the other minimum counts are \(5,12,27,58\).

## Verification
`check.py` computes exact one-round pair extensions by a four-cell state table, assembles complete two-round pointed types and three-round root types, and independently compares these against direct three-round enumeration of actual subset posets on small ground sets. It checks the boundary identities in step 2 for tens of thousands of finite configurations and recovers five classes for \(2\le r<n\le16\). The test log is in `check_output.txt`. The arbitrary-parameter part rests on the explicit cell-state argument and the pumping reductions above, not on those finite test bounds.

## Relationship to prior work
The foundational treatment of flats and geometric lattices in Margolis--Rhodes--Silva, arXiv:1510.05485, concerns representation and structure, rather than quantifier-rank equivalence. Bonin--de Mier, arXiv:math/0505689, studies *cyclic* flats; its main results do not classify pure inclusion theories of the ordinary flat lattices used here. Related three-round classifications of full Boolean inclusion lattices and of vector-subspace lattices do not imply the present claim: uniform-matroid flat lattices have a distinct, rank-truncated family with a collapsed top, and neither of those earlier statements supplies a first-order rank-three transfer to it.

## Limitations
This theorem concerns nontrivial uniform matroids and rank-three first-order logic of pure inclusion. It makes no assertion about all matroids, larger quantifier ranks, signatures with named rank functions, counting logic, or logical equivalence when matroid rank equals ground-set size. The calculations in the included program are finite corroborations. Historical-priority checking was non-exhaustive and independent mathematical validation has not been performed.

## References
1. S. Margolis, J. Rhodes, and P. V. Silva, *On the lattice of flats of a boolean representable simplicial complex*, arXiv:1510.05485, first public 2015-10-19; https://arxiv.org/abs/1510.05485.
2. J. E. Bonin and A. de Mier, *The Lattice of Cyclic Flats of a Matroid*, arXiv:math/0505689, first public 2005-05-31; https://arxiv.org/abs/math/0505689.
