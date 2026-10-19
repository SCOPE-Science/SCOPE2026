# Exact enumeration of nonbinary two-shell cut-down de Bruijn cycles

## Finding

For integers \(q\ge3\) and \(n\ge2\), let \(\mathcal U_{q,n}\) be the set of cyclic words on \(\{0,1,\ldots,q-1\}\) whose length-\(n\) cyclic factors are precisely **all** words with exactly one or exactly two nonzero coordinates, each occurring once. Two words are identified precisely when one is a cyclic rotation of the other; alphabet permutations, reversal, and complementation are *not* identifications. Then

\[
\boxed{\left|\mathcal U_{q,n}\right|
=(q-2)!\,\big((q-1)!\big)^{(n-1)(q-1)}
 q^{(n-1)(q-2)+\lfloor(n-1)/2\rfloor}.}
\]

In particular, every word in the set has exact period
\[
L=n(q-1)+\binom n2(q-1)^2.
\]
For example, the counts at \((q,n)=(3,2),(3,3),(3,4),(4,2)\) are respectively \(12,432,5184,6912\).

## Assumptions and scope

The symbols are labelled. Hamming weight means the number of **nonzero coordinates**, not the sum of the coordinate values. Cyclic factors include those wrapping around the end of a displayed period. The graph includes its loops and distinguishes edges by their complete length-\(n\) labels. The result is for the exact two-shell family of weights one and two, and not for an arbitrary choice of permitted weights. The binary specialization is an already-known count and is not claimed as a new theorem.

## Proof

**1. Directed presentation and Euler tours.** Set \(m=n-1\) and \(r=q-1\). Consider the directed graph whose edges are the allowed length-\(n\) words, with an edge \((a_0,\ldots,a_{n-1})\) from \((a_0,\ldots,a_{n-2})\) to \((a_1,\ldots,a_{n-1})\). Its vertices are precisely the length-\(m\) words of weights zero, one, and (when present) two. For each vertex, the legal incoming and outgoing labels depend on the same number of existing nonzero coordinates; hence the graph is balanced. The all-zero vertex \(z\) has outdegree \(r\); every weight-one vertex has outdegree \(q\); and every weight-two vertex has outdegree one.

Each weight-two vertex follows a forced path of zero appends until it reaches a weight-one vertex. From every weight-one vertex, repeated appending of zero reaches \(z\). Thus every vertex has a directed path to \(z\); balance implies that the nonisolated graph is strongly connected. Therefore every cyclic word under consideration is exactly an Euler circuit of this graph, up to cyclic rotation of the edge sequence. Distinct length-\(n\) edge labels ensure no shorter cyclic period. The directed BEST theorem gives the number of such circuits as
\[
t_z\,(r-1)!\,((q-1)!)^{mr},
\]
where \(t_z\) is the number of directed spanning in-arborescences rooted at \(z\). All weight-two vertices contribute the factor \(0!=1\).

**2. Forced paths and the reduced Laplacian.** Write \(e_{i,a}\) for the weight-one vertex with symbol \(a\in\{1,\ldots,r\}\) in position \(i\) counted from the right, where \(0\le i<m\). Every weight-two vertex has exactly one outgoing choice in any in-arborescence, so contracting its forced zero-append path preserves the number of rooted in-arborescences. The choices from \(e_{i,a}\) become:

* Append zero: go to \(e_{i+1,a}\) when \(i<m-1\), or to \(z\) when \(i=m-1\).
* Append a nonzero symbol \(b\): the resulting forced path ends at \(e_{m-1-i,b}\), independently of \(a\). This gives one arc for each of the \(r\) values of \(b\).

The directed reduced Laplacian, with the root row and column deleted, acts on arrays \(f=(f_{i,a})\) as
\[
(\mathscr Lf)_{i,a}=qf_{i,a}
-\mathbf1_{\{i<m-1\}}f_{i+1,a}
-\sum_{b=1}^{r}f_{m-1-i,b}.
\]
This includes self-loops correctly: a loop subtracts from the same diagonal. The directed Matrix-Tree theorem says \(t_z=\det\mathscr L\).

**3. Color decomposition.** Split the array space into the subspace constant in \(a\) at each \(i\), and the subspace whose sum over \(a\) vanishes at each \(i\). Both are invariant under \(\mathscr L\). On the zero-sum subspace, the last term is zero. Relative to a basis of the \(r-1=q-2\) independent color differences, the operator consists of copies of an upper-triangular \(m\)-by-\(m\) matrix with diagonal \(q\). Therefore its determinant is \(q^{m(q-2)}\).

On the constant-color subspace, put \(f_{i,a}=g_i\). The remaining operator is
\[
(\mathscr Hg)_i=qg_i
-\mathbf1_{\{i<m-1\}}g_{i+1}
-rg_{m-1-i}.
\]
It is the root-deleted Laplacian of a *weighted* directed graph on the indices \(0,\ldots,m-1\), together with a root \(z\). Each index \(i\) has an \(A\)-arc of weight one to \(i+1\), or to \(z\) if \(i=m-1\); and a \(B\)-arc of weight \(r\) to \(m-1-i\).

**4. Exact weighted tree count.** A rooted in-arborescence of this index graph must choose one outgoing arc per index. If it chooses \(B\) at an index \(i\ge\lfloor m/2\rfloor\), the nonempty interval of indices \([m-1-i,i]\) is closed under all chosen arcs: at \(i\) its \(B\)-arc remains in the interval; below \(i\), an \(A\)-arc moves at most to \(i\), and a \(B\)-arc reflects an index to another point of the interval. No vertex of this interval can reach \(z\), which is impossible. Conversely, if every \(B\)-choice lies at an index \(i<\lfloor m/2\rfloor\), each such choice jumps strictly forward to an index in the upper half, from which all steps follow the forward \(A\)-arcs to \(z\). Thus precisely those choices produce in-arborescences.

There are \(\lfloor m/2\rfloor\) eligible low indices, each offering either weight one for \(A\) or weight \(r\) for \(B\). The weighted Matrix-Tree theorem therefore yields
\[
\det\mathscr H=(1+r)^{\lfloor m/2\rfloor}
=q^{\lfloor m/2\rfloor}.
\]
Together with the color-difference determinant,
\[
t_z=q^{m(q-2)+\lfloor m/2\rfloor}.
\]
Substituting this into the BEST formula and taking \(m=n-1\) proves the displayed enumeration. \(\square\)

## Verification

The accompanying standalone standard-library program `verify.py` independently constructs the **full**, uncontracted directed graph and computes its rooted Matrix-Tree determinant by exact fraction-free Bareiss elimination. It checks all stated counts for \(2\le q\le5\) over recorded ranges, including \(2\le n\le6\) for \(q=3\). A separate procedure exhaustively enumerates local outgoing-edge orderings and counts the valid root-fixed Euler tours at \(2\le n\le10\) for \(q=2\), \(2\le n\le4\) for \(q=3\), and \(n=2\) for \(q=4\). Every checked count matches the theorem, and the literal output is in `verification_output.txt`. These finite tests are independent consistency checks; the preceding proof supplies all-parameter correctness.

## Relationship to prior work

Ruskey, Sawada and Williams (2012) proved existence of universal cycles over binary adjacent Hamming-weight layers. Mitchell and Wild (arXiv:2607.22350, first submitted July 24, 2026) establish the analogous existence for nonbinary Hamming weight, but their investigated theorem is about existence, not enumeration. Fredricksen (1993) explicitly calculated the analogous **binary** two-low-weight count using pure-cycling-register joins; that case is prior work and is not part of the claimed nonbinary novelty. Li, Jiang and Lin (2022/2023) examine cycles whose binary windows have weight at most two and report counts for some small cases; their accessible abstract and appendix do not assert the nonbinary enumeration. Chee and collaborators (2020) enumerate a different notion of constrained de Bruijn code, defined through the nonrepetition of windows at positions within a chosen distance, rather than the requirement to use precisely the Hamming-weight-one/two window set. The present claim gives an all-parameter formula over alphabets of at least three symbols, using a color-space decomposition absent from these inspected statements.

## Limitations

The formula does not count orbits under reversal, nonzero-symbol permutation, or other alphabet symmetries; only cyclic rotation is factored out. It applies to exactly Hamming-weight-one and Hamming-weight-two windows, not to an arbitrary weight band or digit-sum restriction. The body of the Li–Jiang–Lin subscription article was not accessible, although its abstract and accessible appendix were checked; differently phrased or unindexed earlier nonbinary enumerations remain a literature risk.

## References

1. C. J. Mitchell and P. R. Wild, *Weight-constrained cut-down de Bruijn sequences*, arXiv:2607.22350, first submitted 2026-07-24. https://arxiv.org/abs/2607.22350
2. F. Ruskey, J. Sawada and A. Williams, *De Bruijn Sequences for Fixed-Weight Binary Strings*, SIAM Journal on Discrete Mathematics 26(2) (2012), 605–617, DOI: 10.1137/100808782.
3. H. Fredricksen, *The Number of Nonlinear Shift Registers That Produce All Vectors of Weight ≤ t*, IEEE Transactions on Information Theory 39(6) (1993), 1989–1990.
4. M. Li, Y. Jiang and D. Lin, *Properties of the cycles that contain all vectors of weight ≤ k*, Designs, Codes and Cryptography 91 (2023), 221–239; online 2022-09-06, DOI: 10.1007/s10623-022-01100-9.
5. Y. M. Chee, T. Etzion, H. M. Kiah, A. Vardy, V. K. Vu and E. Yaakobi, *Constrained de Bruijn Codes: Properties, Enumeration, Constructions, and Applications*, arXiv:2005.03102, first submitted 2020-05-06.
6. N. G. de Bruijn, T. van Aardenne-Ehrenfest, and standard directed BEST and Matrix-Tree counting identities, as used in references 2–4.
