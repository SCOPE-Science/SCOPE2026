# Minimum identifying codes of crown graphs are balanced one-hole transversals
## Finding
For every integer \(n\ge5\), let
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\},
\]
with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). A set \(C\subseteq V(\operatorname{Cr}_n)\) is a minimum identifying code if and only if there is a unique index \(r\) with \(C\cap\{a_r,b_r\}=\varnothing\), every other pair \(\{a_i,b_i\}\) contributes exactly one vertex, and
\[
|C\cap A|\ge2,\qquad |C\cap B|\ge2.
\]
Thus
\[
\gamma^{\mathrm{ID}}(\operatorname{Cr}_n)=n-1,
\qquad
N_{\min}(\operatorname{Cr}_n)=n\bigl(2^{n-1}-2n\bigr).
\]
The numerical minimum is already covered by prior work on complete bipartite graphs with a maximum matching deleted. The contribution here is the exact classification and count of every minimum code in the balanced crown family.

## Assumptions and scope
An identifying code in a graph \(G\) is a set \(C\subseteq V(G)\) such that all closed-neighborhood traces \(N[v]\cap C\), for \(v\in V(G)\), are nonempty and pairwise distinct. The statement concerns the standard crown graph above and integers \(n\ge5\). Small crowns are deliberately outside the theorem: the balanced two-per-side condition used at equality first becomes feasible at \(n=5\).

## Proof
For each index \(i\), write \(P_i=\{a_i,b_i\}\) and \(c_i=|C\cap P_i|\). For two distinct vertices \(a_i,a_j\),
\[
N[a_i]\triangle N[a_j]=P_i\cup P_j.
\]
Therefore an identifying code must meet \(P_i\cup P_j\) for every \(i\ne j\). In particular, at most one matched pair can have \(c_i=0\). Every other pair then contributes at least one code vertex, so \(|C|\ge n-1\).

Suppose equality holds. Exactly one pair, say \(P_r\), is omitted and every \(P_i\) with \(i\ne r\) contributes exactly one vertex. Put
\[
P=\{i:a_i\in C\},\qquad Q=\{i:b_i\in C\}.
\]
Then \(P\) and \(Q\) partition \([n]\setminus\{r\}\). The closed-neighborhood traces are
\[
N[a_i]\cap C=
\begin{cases}
\{a_i\}\cup\{b_q:q\in Q\},&i\in P,\\
\{b_q:q\in Q\setminus\{i\}\},&i\in Q,\\
\{b_q:q\in Q\},&i=r,
\end{cases}
\]
and symmetrically
\[
N[b_i]\cap C=
\begin{cases}
\{b_i\}\cup\{a_p:p\in P\},&i\in Q,\\
\{a_p:p\in P\setminus\{i\}\},&i\in P,\\
\{a_p:p\in P\},&i=r.
\end{cases}
\]
If \(|P|=1\), the vertex \(b_i\) indexed by the unique member of \(P\) has empty trace; similarly \(|Q|=1\) is impossible. Hence every minimum identifying code must satisfy \(|P|,|Q|\ge2\).

Conversely, assume one pair is omitted, every other pair contributes exactly one vertex, and \(|P|,|Q|\ge2\). The displayed formulas show immediately that every trace is nonempty. Two traces on the same bipartition side are distinct: selected indices carry their own selected vertex, distinct unselected indices delete different selected opposite-side vertices, and the omitted index has the full opposite-side trace. For a cross-side pair, inspect the possible memberships of its indices in \(P\), \(Q\), or \(\{r\}\). A trace from the \(A\)-side has its non-self elements in \(B\), while a trace from the \(B\)-side has its non-self elements in \(A\); equality in the only mixed self-containing case would force simultaneously \(|P|=1\) and \(|Q|=1\). The assumed lower bounds exclude this. Thus all \(2n\) traces are distinct, and the set is identifying.

For \(n\ge5\), such sets exist by choosing the omitted pair and then choosing at least two of the remaining \(n-1\) indices for \(P\), leaving at least two for \(Q\). Therefore the lower bound is attained. For a fixed omitted index, the number of admissible orientations is
\[
\sum_{k=2}^{n-3}\binom{n-1}{k}
=2^{n-1}-2n.
\]
Multiplying by the \(n\) choices of the omitted pair gives the stated count.

## Verification
The proof is symbolic and covers every integer \(n\ge5\). The accompanying `verify.py` independently enumerates every vertex subset of \(\operatorname{Cr}_n\) for \(5\le n\le9\), recomputes all closed-neighborhood traces, confirms the minimum size, checks the structural characterization for every minimum code, and compares the exact count with \(n(2^{n-1}-2n)\). Its replay output is:

`VERIFY_OK n_range=5..9 subset_checks=349184 basis_checks=3538 max_order=18`

The finite computation is corroborative and is not used as a proof for arbitrary \(n\).

## Relationship to prior work
Bousquet, Lagoutte, Li, Parreau and Thomassé give the standard identifying-code formulation in terms of nonempty distinct closed-neighborhood traces and place the problem in the broader theory of identifying codes in hereditary graph classes. Their first public arXiv version appeared on 22 July 2014 and the journal record lists MSC 05C69 first.

Nikandish, Khani Nasab and Dodonge study graphs differing by matchings. Their abstract explicitly says that the identifying-code number of \(K^*_{m,n}\), obtained from \(K_{m,n}\) by deleting a maximum matching, is given. This includes the scalar minimum for crowns. The accessible abstract does not state an all-minimum-code classification or an enumeration. The full text was not openly accessible during this comparison, so this is recorded as a residual literature risk rather than treated as negative evidence. Searches under `crown graph`, `complete bipartite minus perfect matching`, `matching-deleted biclique`, and \(K^*_{n,n}\) did not locate another statement implying the classification and count above.

## Limitations
The theorem is restricted to \(n\ge5\). It does not claim novelty for the scalar value of the identifying-code number. The closest same-object 2020 paper was available only through its abstract and bibliographic metadata in this review; if its inaccessible body contains an all-minimum-code classification or exact count, the originality assessment would need to be revisited. No claim is made for unbalanced \(K^*_{m,n}\).

## References
1. N. Bousquet, A. Lagoutte, Z. Li, A. Parreau, S. Thomassé, *Identifying codes in hereditary classes of graphs and VC-dimension*, arXiv:1407.5833; SIAM J. Discrete Math. 29 (2015), 2047–2064, DOI 10.1137/14097879X.
2. R. Nikandish, O. Khani Nasab, E. Dodonge, *Minimum identifying codes in some graphs differing by matchings*, Discrete Math. Algorithms Appl. 12 (2020), 2050046, DOI 10.1142/S1793830920500469.
