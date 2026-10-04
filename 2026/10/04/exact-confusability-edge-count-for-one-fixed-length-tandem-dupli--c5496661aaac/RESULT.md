# Exact confusability edge count for one fixed-length tandem duplication

## Finding
For integers \(q\ge 2\), \(\ell\ge 1\), and \(n\ge \ell\), let \(D_\ell(x)\) be the set of distinct words obtained from \(x\in\mathbb Z_q^n\) by exactly one tandem duplication of a contiguous block of length \(\ell\). Let \(G_{q,\ell,n}\) be the simple graph on \(\mathbb Z_q^n\) in which distinct \(x,y\) are adjacent precisely when \(D_\ell(x)\cap D_\ell(y)\ne\varnothing\).

If \(n\le 2\ell\), then \(G_{q,\ell,n}\) has no edges. If \(n\ge 2\ell+1\), then
\[
|E(G_{q,\ell,n})|=
\frac{(n-2\ell)(q-1)q^{n-\ell-2}}{2}
\bigl((q-1)(n-2\ell-1)+2q\bigr).
\]
Every adjacent pair has exactly one common one-duplication output. Hence the average degree is
\[
\overline d(G_{q,\ell,n})=
\frac{(n-2\ell)(q-1)\bigl((q-1)(n-2\ell-1)+2q\bigr)}{q^{\ell+2}}.
\]
For example, in the binary length-two duplication channel,
\[
|E(G_{2,2,n})|=2^{n-5}(n-4)(n-1)\qquad(n\ge5).
\]

## Assumptions and scope
The alphabet is the additive group \(\mathbb Z_q\). A tandem duplication of length \(\ell\) at position \(p\), where \(0\le p\le n-\ell\), sends a decomposition \(x=uvw\) with \(|u|=p\) and \(|v|=\ell\) to \(uvvw\). The error set \(D_\ell(x)\) is a set, so different duplication positions producing the same output are identified. The theorem counts unordered pairs of distinct length-\(n\) source words whose exact-one-error sets intersect. It does not assert an optimal code size.

## Proof
Use the standard \(\ell\)-step derivative. For \(x=(x_1,\ldots,x_n)\), write
\[
\phi_\ell(x)=(a,b),\qquad
a=(x_1,\ldots,x_\ell),\qquad
b_j=x_{j+\ell}-x_j\pmod q
\]
for \(1\le j\le n-\ell\). This map is a bijection between \(\mathbb Z_q^n\) and \(\mathbb Z_q^\ell\times\mathbb Z_q^{n-\ell}\). Under \(\phi_\ell\), a tandem duplication at position \(p\) leaves \(a\) unchanged and inserts a block \(0^\ell\) into \(b\) at the corresponding gap.

Fix \(a\), and put \(m=n-\ell\). Every derivative tail \(b\in\mathbb Z_q^m\) has a unique decomposition
\[
b=0^{r_0}w_1 0^{r_1}w_2\cdots w_s0^{r_s},
\]
where every \(w_i\ne0\), every \(r_i\ge0\), and \(r_0+\cdots+r_s=m-s\). Call \((w_1,\ldots,w_s)\) the nonzero skeleton and \(r=(r_0,\ldots,r_s)\) the zero-run vector. Inserting \(0^\ell\) into the \(i\)-th zero run replaces \(r\) by \(r+\ell e_i\). Thus the distinct one-duplication outputs are indexed by the \(s+1\) zero runs.

Two distinct derivative tails with a common one-duplication output must have the same nonzero skeleton. If their zero-run vectors are \(r\ne t\), then a common output means
\[
r+\ell e_i=t+\ell e_j
\]
for some \(i\ne j\). Equivalently,
\[
t=r+\ell e_i-\ell e_j,
\]
with \(r_j\ge\ell\). The ordered pair \((i,j)\) is uniquely determined by \(t-r\), so two distinct source words have at most one common one-duplication output. Conversely every such legal transfer gives one common output.

Fix a skeleton of length \(s\). To count oriented legal transfers, choose the donor zero run in \(s+1\) ways and the distinct recipient in \(s\) ways. After subtracting \(\ell\) from the donor, the remaining zero mass is \(n-2\ell-s\). The number of weak compositions into \(s+1\) zero runs is
\[
\binom{n-2\ell}{s}.
\]
Every unordered adjacent pair is counted in both orientations. Therefore one fixed skeleton contributes
\[
\frac{s(s+1)}2\binom{n-2\ell}{s}
\]
edges. There are \((q-1)^s\) nonzero skeletons of length \(s\) and \(q^\ell\) possible prefixes \(a\). With \(N=n-2\ell\), this gives
\[
|E|=\frac{q^\ell}{2}
\sum_{s=0}^{N}s(s+1)\binom Ns(q-1)^s.
\]
If \(N\le0\), no legal transfer exists. For \(N\ge1\), differentiating the binomial theorem twice yields
\[
\sum_{s=0}^{N}s(s+1)\binom Ns z^s
=N(N-1)z^2(1+z)^{N-2}+2Nz(1+z)^{N-1}.
\]
Substituting \(z=q-1\) gives the stated edge formula. Dividing twice the edge count by \(q^n\) gives the average degree.

## Verification
The bundled `verify.py` uses only the Python standard library. It reconstructs every tandem-duplication output directly, independently computes the derivative, checks for every tested word and position that duplication is exactly zero-block insertion in derivative coordinates, forms every pairwise error-ball intersection, verifies that each nonempty intersection has cardinality one, and compares the direct edge count with the closed formula.

The finite replay covers multiple values of \(q\), \(\ell\), and \(n\), including all tested boundary cases with \(n\le2\ell\). It also checks the binary \(\ell=2\) specialization through \(n=10\). The replay ends with `VERIFY_OK`. These finite checks corroborate the proof; they are not used as a substitute for the general argument.

## Relationship to prior work
Lenz, Wachter-Zeh, and Yaakobi define tandem-duplication spheres and the same derivative transformation, and use it to derive code-cardinality bounds. Yehezkeally and Schwartz use zero-run signatures and a Manhattan-metric representation to analyze intersections of descendant cones in reconstruction coding. Lenz, Jünger, and Wachter-Zeh likewise exploit the reduction from tandem duplication to zero-block insertion for code bounds and constructions.

The present statement aggregates the one-error intersection relation over all length-\(n\) source words. Its new content is the exact number of conflicting source pairs for every \(q,\ell,n\), together with the fact that every conflict has exactly one common one-error descendant. The count follows by summing legal transfers of \(\ell\) zeros between zero runs over all nonzero skeletons.

## Limitations
The theorem concerns exactly one tandem duplication of one fixed length. It does not count conflicts for two or more duplications, mixed duplication lengths, palindromic or reverse-complement duplications, or source words of unequal length. It gives the total edge count and common-descendant multiplicity, not the degree sequence, independence number, or an optimal correcting-code cardinality. Literature searches cannot exclude an unindexed or unpublished prior computation of the same aggregate invariant.

## References
1. Andreas Lenz, Antonia Wachter-Zeh, and Eitan Yaakobi, “Duplication-Correcting Codes,” arXiv:1712.09345v1, 2017.
2. Yonatan Yehezkeally and Moshe Schwartz, “Reconstruction Codes for DNA Sequences with Uniform Tandem-Duplication Errors,” arXiv:1801.06022v1, 2018.
3. Andreas Lenz, Niklas Jünger, and Antonia Wachter-Zeh, “Bounds and Constructions for Multi-Symbol Duplication Error Correcting Codes,” arXiv:1807.02874v1, 2018.
