# Zero forcing sets of complete bipartite graphs with a deleted matching

## Finding

Let \(m,n\geq3\) and \(0\leq t\leq\min(m,n)\) be integers. Delete \(t\) pairwise disjoint edges from the complete bipartite graph \(K_{m,n}\), obtaining \(G_{m,n,t}\). Put
\[
P_m=\binom m2-\binom{m-t}2,\qquad
P_n=\binom n2-\binom{n-t}2,\qquad
E=t(m-t)(n-t)+\binom t2.
\]
For the ordinary zero forcing polynomial \(\mathcal Z(G;z)=\sum_{S\text{ zero forcing}}z^{|S|}\), the exact identity is
\[
\boxed{\mathcal Z(G_{m,n,t};z)=z^{m+n}+(m+n)z^{m+n-1}
 +(mn+P_m+P_n)z^{m+n-2}
 +(nP_m+mP_n)z^{m+n-3}
 +(P_mP_n-E)z^{m+n-4}.}
\]
All lower coefficients vanish. In particular,
\[
Z(G_{m,n,t})=
\begin{cases}
m+n-2,&t=0,\\
m+n-3,&t=1,\\
m+n-4,&2\leq t\leq\min(m,n).
\end{cases}
\]
For a crown graph \(\mathrm{Cr}_q=K_{q,q}\) with a perfect matching deleted, \(q\geq3\), the specialization is
\[
\mathcal Z(\mathrm{Cr}_q;z)
=z^{2q-4}\left[\left(z^2+qz+\binom q2\right)^2-\binom q2\right].
\]
Thus the number of minimum zero forcing sets in \(\mathrm{Cr}_q\) is
\(\binom q2\bigl(\binom q2-1\bigr)\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Fix bipartition classes \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\). Edges \(a_ib_i\) are absent precisely for \(1\leq i\leq t\), and every other cross-part pair is an edge. The ordinary color-change rule permits a *blue* vertex with exactly one white neighbor to force that neighbor blue; forcing proceeds until no further color change is possible. A zero forcing set is an initial blue set that turns all vertices blue. The cases \(m=2\) or \(n=2\) are not asserted.

For an arbitrary initial blue set \(S\), let \(I=\{i:a_i\notin S\}\), \(J=\{j:b_j\notin S\}\), \(I_*=I\cap[t]\), and \(J_*=J\cap[t]\), with \([t]=\{1,\ldots,t\}\). The underlying structural characterization is that \(S\) is zero forcing **if and only if** all four conditions hold:

1. \(|I|\leq2\) and \(|J|\leq2\).
2. If \(|I|=2\), then \(I_*\neq\varnothing\).
3. If \(|J|=2\), then \(J_*\neq\varnothing\).
4. If \(|I|=|J|=2\), then \(I_*\neq J_*\).

## Proof

**Necessary restrictions.** If there are at least three white vertices in \(A\), every blue vertex in \(B\) has at least two white neighbors in \(A\): it can miss at most one edge to \(A\). Therefore no force into \(A\) is ever possible while those three white vertices remain, even if forces into \(B\) are performed. Such a state cannot finish. The same argument applies with the bipartition classes reversed.

If exactly two vertices \(a_i,a_j\) are white and neither index belongs to \([t]\), every vertex in \(B\) is adjacent to both, and neither can ever be forced. Consequently \(|I|=2\) requires \(I_*\neq\varnothing\), and symmetrically \(|J|=2\) requires \(J_*\neq\varnothing\).

Suppose both sides contain two whites, and \(I_*=J_*\). A blue vertex in \(B\) cannot have its exceptional missing edge directed to a white vertex in \(A\): such an exception would require an index in \(I_*\) not present in \(J_*\), and that index set is empty. Hence every blue vertex of \(B\) is adjacent to both white vertices of \(A\). The same reasoning applies in the other direction. No first force exists. Thus the fourth restriction is necessary.

**Sufficiency.** If each side has at most one white vertex, all whites can be forced: each white vertex has at least two neighbors in the opposite class, since each part has size at least three and only one cross-edge incident to a vertex could have been removed. With at most one white on that opposite side, at least one of those neighbors is blue. These forces can be applied successively.

If \(|I|=2\), \(J=\varnothing\), and \(i\in I_*\), then blue \(b_i\) is adjacent to exactly one of the two white vertices in \(A\), so it forces that vertex. What remains has at most one white on either side and finishes. The case with sides interchanged is identical.

If \(|I|=2\), \(|J|=1\), and \(I_*\neq\varnothing\), choose \(i\in I_*\). If \(i\notin J\), blue \(b_i\) immediately forces one of the two white vertices in \(A\), and the state reduces to at most one white on either side. If \(i\in J\), then \(J=\{i\}\). There exists a blue vertex in \(A\), because \(m\geq3\) and only two vertices in \(A\) are white; this blue vertex is adjacent to \(b_i\), because the only vertex of \(A\) nonadjacent to \(b_i\) is the white vertex \(a_i\). Hence it forces \(b_i\), giving the already solved case \((|I|,|J|)=(2,0)\). Again the opposite orientation is symmetric.

Finally, suppose \(|I|=|J|=2\), \(I_*\neq\varnothing\), \(J_*\neq\varnothing\), and \(I_*\neq J_*\). If \(i\in I_*\setminus J_*\), then \(b_i\) is blue and is adjacent to exactly one of the two whites in \(A\); it forces that white and reduces the state to \((1,2)\), with nonempty \(J_*\), which is settled above. If no such \(i\) exists, since \(I_*\neq J_*\) there must be \(j\in J_*\setminus I_*\). Then blue \(a_j\) forces one of the whites in \(B\) and reduces to the symmetric case \((2,1)\). This proves the four-condition characterization.

**Counting.** Define \(P_m\) to be the number of 2-element subsets of \([m]\) meeting \([t]\), and define \(P_n\) analogously; the displayed binomial formulas follow by complementation. For zero, one, two, three, or four initial white vertices, the admissible patterns have respective counts
\[
1,\qquad m+n,\qquad mn+P_m+P_n,\qquad nP_m+mP_n,\qquad P_mP_n-E.
\]
The sole subtraction in the last coefficient removes pairs \((I,J)\) of 2-element white index sets for which \(I_*=J_*\neq\varnothing\). Their common intersection with \([t]\) has either one or two indices. In the one-index case there are \(t(m-t)(n-t)\) choices, as the remaining index in each set must lie outside \([t]\). In the two-index case there are \(\binom t2\) choices. This gives \(E\), and multiplication by the appropriate powers of \(z\) proves the polynomial.

For \(t=0\), \(P_m=P_n=0\), so the first nonzero coefficient below full degree is \(mn\) at degree \(m+n-2\). For \(t=1\), \(P_m,P_n>0\), the degree \(m+n-3\) coefficient is positive, while the degree \(m+n-4\) coefficient is zero. When \(t\geq2\), take \(I=\{1,i\}\) and \(J=\{2,j\}\), with \(i\in[m]\setminus\{1,2\}\) and \(j\in[n]\setminus\{1,2\}\). The matched supports are nonempty and unequal, giving a valid four-white state. Hence its coefficient is positive, proving the three forcing-number cases. Substitution \(m=n=t=q\) proves the crown formula.

## Verification

The standalone `verify.py` computes the ordinary color-change closure directly, checks the four-condition characterization for every initial blue set, and independently matches the coefficient formula. Running `python verify.py` with Python 3 and only the standard library gave:

```
VERIFY_OK cases=130 initial_colourings=407040 (3<=a,b<=7, a+b<=14, all t)
```

The exhaustive finite check tests the formula only in the stated finite range; the preceding case proof is what establishes the unrestricted claim.

## Relationship to prior work

Barioli and collaborators established foundations for zero forcing and its minimum-rank connections (arXiv:1003.2028, first available March 10, 2010; primary MSC 05C50). Boyer and collaborators introduced and analyzed the size-enumerating zero forcing polynomial (arXiv:1801.08910, first available January 26, 2018). In particular, their Proposition 4 gives \(\mathcal Z(K_{m,n};z)=z^{m+n}+(m+n)z^{m+n-1}+mnz^{m+n-2}\), the \(t=0\) boundary of the present formula. That proposition does not describe graphs from which a matching has been deleted: its hypotheses require a complete multipartite graph. The present result classifies all initial sets throughout the deleted-matching family, rather than only its number of minimum forcing vertices.

Targeted searches for the same graph family, its crown specialization, and the zero forcing polynomial did not identify the claimed classification or closed form in the checked literature. Those searches are not a completeness proof for the literature. Indexed findings about geodesic subpaths and CIS pairs of these same graphs concern different invariants and imply neither the forcing characterization nor the enumerator.

## Limitations

The assertion is restricted to \(m,n\geq3\); it does not address general deletions that share endpoints or positive-semidefinite, skew, connected, or power zero forcing variants. The exact polynomial can be deduced from the proved characterization, but no independent formal proof assistant or external audit has been used. Unindexed sources, including a relevant 2013 thesis whose full text could not be inspected, may contain prior results not detected by the literature comparison.

## References

1. F. Barioli, W. Barrett, S. M. Fallat, H. T. Hall, L. Hogben, B. Shader, P. van den Driessche, H. van der Holst, *Zero forcing parameters and minimum rank problems*, arXiv:1003.2028 (first version March 10, 2010), https://arxiv.org/abs/1003.2028.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910 (first version January 26, 2018), https://arxiv.org/abs/1801.08910, especially Section 4, Proposition 4.
3. M. A. Taklimi, *Zero Forcing Sets for Graphs*, arXiv:1311.7672 (2013), https://arxiv.org/abs/1311.7672. Full text was not obtainable during the comparison; cited as an outstanding inspection risk, not as evidence of noncoverage.
