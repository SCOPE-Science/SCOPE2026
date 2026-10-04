# Restrained-dominating-set profile of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\},
\]
with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). For \(D\subseteq V(\operatorname{Cr}_n)\), put
\[
I=\{i:a_i\notin D\},\qquad J=\{j:b_j\notin D\},\qquad \alpha=|I|,\qquad \beta=|J|.
\]
Then \(D\) is a restrained dominating set if and only if either \(I=J=\varnothing\), or \(1\le\alpha,\beta\le n-1\) and all applicable boundary conditions below hold:

- if \(\alpha=1\), the unique index in \(I\) is not in \(J\);
- if \(\alpha=n-1\), the unique index outside \(I\) is not in \(J\);
- if \(\beta=1\), the unique index in \(J\) is not in \(I\);
- if \(\beta=n-1\), the unique index outside \(J\) is not in \(I\).

Define
\[
A_n(z)=\sum_{k=2}^{n-2}\binom{n}{k}z^k,\qquad
B_n(z)=\sum_{k=2}^{n-2}\binom{n-1}{k}z^k,
\]
where an empty sum is zero. The exact complement-profile enumerator over all restrained dominating sets is
\[
Q_n(u,v)=1+A_n(u)A_n(v)+n(u+u^{n-1})B_n(v)+n(v+v^{n-1})B_n(u)+n(n-1)uv+n u^{n-1}v^{n-1}.
\]
Hence the ordinary cardinality polynomial is
\[
P_n(x)=x^{2n}Q_n(x^{-1},x^{-1}).
\]
In particular,
\[
\gamma_r(\operatorname{Cr}_n)=2,
\]
and the minimum restrained dominating sets are exactly the \(n\) deleted-matching pairs \(\{a_i,b_i\}\).

## Assumptions and scope
Graphs are finite and simple. A restrained dominating set \(D\) is a dominating set such that every vertex outside \(D\) also has a neighbor outside \(D\). The crown graph is taken for \(n\ge3\), so it is connected. The theorem classifies all restrained dominating sets, not only those of minimum size.

## Proof
Write \(C=V(\operatorname{Cr}_n)\setminus D\), with \(C\cap A=\{a_i:i\in I\}\) and \(C\cap B=\{b_j:j\in J\}\). If \(C=\varnothing\), then \(D=V(\operatorname{Cr}_n)\) is restrained dominating.

Assume \(C\ne\varnothing\). Since every vertex of \(C\) must have a neighbor in \(C\), both \(I\) and \(J\) are nonempty. Since every vertex of \(C\) must also have a neighbor in \(D\), neither \(I\) nor \(J\) can have size \(n\). Thus \(1\le\alpha,\beta\le n-1\).

If \(\alpha=1\), say \(I=\{i\}\), then \(b_i\in C\) would have no neighbor in \(C\), so \(i\notin J\). If \(\alpha=n-1\), say \([n]\setminus I=\{i\}\), then \(a_i\) is the only vertex of \(A\cap D\); if \(b_i\in C\), that vertex would have no neighbor in \(D\), so again \(i\notin J\). The two conditions involving \(\beta\) follow symmetrically.

Conversely, assume the displayed size and boundary conditions. For \(a_i\in C\), if \(\beta\ge2\), it has a neighbor in \(C\cap B\) unless \(\beta=1\) and the sole vertex is \(b_i\); the latter is excluded by the \(\beta=1\) boundary condition. Likewise, if \(n-\beta\ge2\), it has a neighbor in \(B\cap D\); the only delicate case is \(\beta=n-1\), and that obstruction is exactly excluded by the \(\beta=n-1\) condition. The same argument with the sides interchanged handles every \(b_j\in C\). Therefore every vertex outside \(D\) has both a neighbor in \(D\) and a neighbor outside \(D\), proving the characterization.

For the enumerator, if \(2\le\alpha,\beta\le n-2\), every choice of \(I,J\) is allowed, giving \(\binom n\alpha\binom n\beta\). If \(\alpha\in\{1,n-1\}\) and \(2\le\beta\le n-2\), the special index determined by \(I\) must be avoided by \(J\), giving \(n\binom{n-1}\beta\); the transposed case is symmetric. On the four boundary corners, the counts are \(n(n-1)\) for \((\alpha,\beta)=(1,1)\), zero for the two mixed corners, and \(n\) for \((\alpha,\beta)=(n-1,n-1)\). Summing these cases gives \(Q_n(u,v)\). The substitution for \(P_n(x)\) follows because \(|D|=2n-\alpha-\beta\).

The maximum possible value of \(\alpha+\beta\) among admissible profiles is \(2n-2\), attained only at \((n-1,n-1)\). Its \(n\) admissible choices have the same omitted index, so their complements in \(V(\operatorname{Cr}_n)\) are exactly \(\{a_i,b_i\}\). Hence the minimum size is two and these are precisely the minimum sets.

## Verification
The accompanying verifier exhaustively checks every vertex subset for \(3\le n\le9\). It independently implements the restrained-domination definition, compares it with the profile criterion, checks every profile coefficient against the closed counting formula, and confirms the minimum-size classification. This finite computation is a consistency check; the proof above establishes the theorem for every \(n\ge3\).

## Relationship to prior work
Henning and Kazemi's work on \(k\)-tuple restrained domination supplies a broad framework in which ordinary restrained domination is the \(k=1\) case and treats general bipartite bounds for the higher-tuple setting. Its searchable full text contains no occurrence of “crown,” and its bipartite section does not state an all-set crown-graph classification or the profile enumerator above. The foundational restrained-domination literature studies general bounds and complexity, including bipartite graphs, rather than this exact deleted-perfect-matching family. Searches using the aliases “crown graph,” “biclique crown,” and “\(K_{n,n}\) minus a perfect matching” found no statement implying the profile theorem or enumerator.

## Limitations
The theorem concerns ordinary restrained domination on the standard crown graphs \(\operatorname{Cr}_n\) for \(n\ge3\). It does not claim an analogous profile formula for arbitrary matching-deleted bicliques, unequal bipartition sizes, or higher \(k\)-tuple restrained domination. The exhaustive verifier stops at \(n=9\) and is not used as an infinite proof. A residual literature risk is a non-indexed crown-specific treatment not surfaced by the focused searches.

## References
1. M. A. Henning and A. P. Kazemi, “k-Tuple Restrained Domination in Graphs,” arXiv:1603.02433, first public version 8 March 2016; later published in Quaestiones Mathematicae, DOI 10.2989/16073606.2020.1762137.
2. G. S. Domke, J. H. Hattingh, S. T. Hedetniemi, R. C. Laskar, and L. R. Markus, “Restrained domination in graphs,” Discrete Mathematics 203 (1999), 61–69, DOI 10.1016/S0012-365X(99)00016-3.
