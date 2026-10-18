# The 1-limited domination polynomial and exact minima of Möbius ladders

## Finding

Let \(M_n\) be the Möbius ladder on \(2n\) vertices, with \(n\ge3\). For each vertex subset \(D\) which dominates all vertices outside \(D\) and for which every vertex of \(D\) has at most one neighbor outside \(D\), write
\[
P_n(z)=\sum_{D\ \text{1-limited dominating}}z^{|D|},\qquad Q_n(z)=z^{-n}P_n(z).
\]
The following closed generating function determines **every coefficient** of this domination-set polynomial. Set
\[
A(t,z)=1-t^4-z(t+t^2+2t^3+t^4+t^5)-z^2(t^3+t^4),
\qquad B(t,z)=1-t+t^2z.
\]
Then, for all \(n\ge3\),
\[
\boxed{Q_n(z)=[t^n]\left(-t\frac{\partial}{\partial t}\log\frac{(1-t)A(t,z)}{B(t,z)}\right).}
\]
All formal series are expanded at \(t=0\); the coefficients with \(n=1,2\) are formal auxiliary terms, not graph counts. In particular,
\[
\boxed{\gamma^L_1(M_n)=\begin{cases}n,&4\mid n,\\n+1,&4\nmid n,\end{cases}}
\qquad
\boxed{\#\{D:|D|=\gamma^L_1(M_n)\}=\begin{cases}4,&4\mid n,\\2n,&n\equiv2\pmod4,\\3n,&n\ \text{odd}.\end{cases}}
\]
The counts refer to subsets of the fixed labelled graph, not isomorphism classes.

## Assumptions and scope

All graphs are finite, undirected, loopless. For \(n\ge3\), define \(M_n\) on \(\mathbb Z/(2n)\mathbb Z\) with cycle edges \(\{i,i+1\}\) and antipodal edges \(\{i,i+n\}\). Every vertex has degree three. A set \(D\) is 1-limited dominating when every vertex outside \(D\) has a neighbor in \(D\), and every vertex in \(D\) has at most one neighbor outside \(D\). The convention includes \(D=V\); no connectedness of \(D\) is required. This is equivalent to \((1,2)\)-domination on cubic graphs.

## Proof

**1. A uniform cardinality lower bound.** Put \(T=V(M_n)\setminus D\). Every \(v\in T\) has a neighbor in \(D\), whereas every \(v\in D\) has at most one neighbor in \(T\). Hence the number of cut edges obeys
\[
|T|\le e(T,D)\le |D|.
\]
As \(|V|=2n\), every permissible \(D\) has \(|D|\ge n\). Thus \(Q_n(z)\) is a polynomial in nonnegative integral powers of \(z\).

**2. Twisted two-row representation.** Represent consecutive vertices as columns with two positions \(i\) and \(i+n\). For \(0\le i<n\), encode the members of \(T\) by a two-bit state \(b_i\in\{0,1\}^2\). Extend it to all integral column indices using the twist \(b_{i+n}=\sigma(b_i)\), where \(\sigma\) interchanges the two bits. The neighbors of the vertex of row \(r\) in column \(i\) are its counterparts in columns \(i-1\) and \(i+1\), together with the opposite-row vertex in column \(i\). Writing \(a=b_{i-1}\), \(b=b_i\), \(c=b_{i+1}\), its 1-limited dominating condition is exactly
\[
a_r+c_r+b_{1-r}\le1+b_r\qquad(r=0,1).
\]
When \(b_r=0\), this demands at most one neighbor in \(T\); when \(b_r=1\), it demands at most two of the three neighbors in \(T\), equivalently at least one in \(D\). There are no other constraints.

**3. Exact finite-state transfer.** Let the sixteen states be ordered pairs \((a,b)\in\{0,1,2,3\}^2\), with integer bit patterns for the columns. Define the \(16\times16\) matrix \(T(u)\) by
\[
T(u)_{(a,b),(b,c)}=u^{\operatorname{wt}(b)}
\]
when the two displayed inequalities hold, and zero otherwise. Here \(\operatorname{wt}(b)\) is the number of its set bits; repeated endpoints produce only one transition. Let \(S\) be the permutation matrix that simultaneously swaps the two bits in both columns. The matrix \(T(u)\) commutes with \(S\).

A length-\(n\) closed walk with the \(S\)-twisted closing condition chooses precisely one assignment of the \(2n\) graph vertices, with weight \(u^{|T|}\); the initial ordered pair is determined by its first two columns. Consequently the complement-size polynomial is
\[
W_n(u)=\sum_Du^{|V\setminus D|}=\operatorname{tr}(T(u)^nS).
\]
This identity holds for every \(n\ge3\). The automorphism \(S\) has a 10-dimensional \(+1\) eigenspace and a 6-dimensional \(-1\) eigenspace, since four ordered-pair states are fixed by simultaneous row swap. Restrict \(T(u)\) to these two spaces, obtaining matrices \(T_+(u)\), \(T_-(u)\). A finite symbolic determinant computation, fully specified by the accompanying standard-library exact verifier, yields
\[
\det(I-tT_+(u))=(tu-1)\bigl(-1+t+t^2u+t^3(u+2u^2)+t^4(u^2+u^3+u^4)+t^5u^4\bigr),
\]
\[
\det(I-tT_-(u))=1-tu+t^2u.
\]
For reproducibility without numerical diagonalization or a black-box symbolic engine, the verifier constructs each matrix using the preceding bit inequalities, derives the two invariant bases explicitly, and computes every coefficient by exact polynomial-matrix traces and Newton identities. These identities divide integer polynomial coefficients only after confirming divisibility, yielding the displayed factorizations over \(\mathbb Z[u,t]\).

**4. Every coefficient.** The formal matrix identity
\[
\sum_{n\ge1}\operatorname{tr}(T(u)^nS)t^n
=-t\frac{\partial}{\partial t}\log\frac{\det(I-tT_+(u))}{\det(I-tT_-(u))}
\]
follows by applying the usual trace-log formula on the two eigenspaces. Since \(P_n(z)=z^{2n}W_n(z^{-1})\), normalize by \(z^n\) and substitute \(u=z^{-1}\) and \(t\mapsto tz\). After cancellation, the determinant quotient becomes precisely \((1-t)A(t,z)/B(t,z)\). This proves the boxed generating function for every graph \(n\ge3\).

**5. Extremal coefficients.** Direct formal coefficient extraction from the displayed rational expression gives
\[
[z^0]\sum_{n\ge1}\widetilde Q_n(z)t^n=\frac{4t^4}{1-t^4},
\qquad
[z^1]\sum_{n\ge1}\widetilde Q_n(z)t^n=
\frac{t(1+4t+7t^2-2t^4)}{(1-t^2)^2},
\]
where \(\widetilde Q_n\) denotes the formal series coefficient, equal to \(Q_n\) for \(n\ge3\). The first formula says the coefficient of \(z^n\) in \(P_n\) is four when \(4\mid n\), and zero otherwise. In the latter case, the coefficient of \(z^{n+1}\) is \(2n\) for even \(n\) and \(3n\) for odd \(n\); it is positive in every case. Together with Step 1 this proves both the exact minimum and the number of minimizers for all \(n\ge3\).

## Verification

Run `python3 verify.py` in a directory containing the provided standalone script. It verifies the two characteristic determinants as exact polynomial identities over the integers. Independently of the transfer calculation, it exhaustively tests all vertex subsets for each \(3\le n\le9\), verifying every coefficient of \(P_n\); it also compares minimum sizes and multiplicities for \(3\le n\le30\) using transfer dynamic programming. All checks passed. The infinite-family statement follows from the exact transfer determinant and coefficient proof, not extrapolation from the finite tests.

## Relationship to prior work

Radić and Tepeh (2026, initial public posting October 1) study 1-limited and equivalent \((1,2)\)-domination in cubic graphs, prove a hardness theorem, and determine the number for the Goldberg family. Their inspected article does not give this Möbius-ladder polynomial or minimum-set census. Tepeh's 2026 Cartesian-product paper gives product bounds and special cases; the Möbius ladder has an essential twist and is not the usual circular-ladder Cartesian product. Existing general bounds for cubic graphs and ordinary domination-number tables do not imply the exact parameter-dependent polynomial or minimum counts. Search did not establish definitive priority; see the review for remaining literature-coverage limitations.

## Limitations

This classification concerns 1-limited dominating vertex subsets, not ordinary domination, induced matchings, or 1-limited parameters for arbitrary cubic graphs. Full closed coefficients are supplied via a formal generating function rather than a single binomial-sum expression for each degree. The finite determinant computation is exact and reproducible with the included source but has not been independently checked externally. Bibliographic priority is not certified.

## References

1. G. Radić and A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796v1 (first posted 2026-10-01), https://arxiv.org/abs/2610.01796v1.
2. A. Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (2026), https://arxiv.org/abs/2606.22428.
3. *On k-limited domination in graphs*, Mediterranean Journal of Mathematics (2026), https://link.springer.com/article/10.1007/s40314-026-03902-2.
4. *On (1,2)-domination in cubic graphs* (2021), https://www.researchgate.net/publication/354046035_On_12-domination_in_cubic_graphs.
