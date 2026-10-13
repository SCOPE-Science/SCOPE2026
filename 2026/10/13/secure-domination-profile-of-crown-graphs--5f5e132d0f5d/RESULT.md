# Secure-domination profile of crown graphs
## Finding
For every integer \(n\ge3\), write the crown graph as
\[
\operatorname{Cr}_n=K_{n,n}-M_n,
\]
with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted matching \(M_n=\{a_i b_i:1\le i\le n\}\). For a set \(S\subseteq V(\operatorname{Cr}_n)\), classify each matched pair by the two-bit state indicating membership of \(a_i,b_i\) in \(S\). Let \(a,b,c,d\) be the numbers of states \(00,10,01,11\), so that \(a+b+c+d=n\), and put
\[
p=b+d=|S\cap A|,\qquad q=c+d=|S\cap B|.
\]
Then \(S\) is secure dominating if and only if both
\[
\Phi_A:\quad (a+c=0)\ \vee\ (q\ge3)\ \vee\ \bigl(q=2\ \wedge\ (d\ge1\ \vee\ a=0)\bigr)\ \vee\ \bigl(q=1\ \wedge\ (a,c,d)=(1,0,1)\bigr)
\]
and
\[
\Phi_B:\quad (a+b=0)\ \vee\ (p\ge3)\ \vee\ \bigl(p=2\ \wedge\ (d\ge1\ \vee\ a=0)\bigr)\ \vee\ \bigl(p=1\ \wedge\ (a,b,d)=(1,0,1)\bigr)
\]
hold. Hence the exact bivariate enumerator by the two bipartition-side cardinalities is
\[
\mathcal S_n(u,v)=\sum_{\substack{a,b,c,d\ge0\\a+b+c+d=n\\\Phi_A\wedge\Phi_B}}
\frac{n!}{a!b!c!d!}\,u^{b+d}v^{c+d}.
\]
The ordinary secure-domination polynomial is \(\mathcal S_n(x,x)\).

For \(n\ge5\), the minimum secure dominating sets have size \(4\) and exactly two possible state profiles:
\[
(n-2,0,0,2)\qquad\text{or}\qquad(n-3,1,1,1).
\]
Thus their number is
\[
\binom n2+n(n-1)(n-2)=\frac{n(n-1)(2n-3)}2.
\]
At the small boundaries, \(\gamma_s(\operatorname{Cr}_3)=3\) with \(14\) minimum sets, while \(\gamma_s(\operatorname{Cr}_4)=4\) with \(62\) minimum sets.

## Assumptions and scope
Graphs are finite, simple, and undirected. A dominating set \(S\) is secure if every vertex \(z\notin S\) has a neighbor \(y\in S\) such that \((S\setminus\{y\})\cup\{z\}\) is again dominating. The theorem classifies every secure dominating set of every crown graph \(\operatorname{Cr}_n\) for \(n\ge3\). The scalar minimum values are included for completeness but are not part of the originality claim; the retained contribution is the all-set classification and enumerator.

## Proof
First note a domination criterion for a crown graph. If \(q\) vertices of \(B\) are selected, then all unselected vertices of \(A\) are dominated automatically when \(q\ge2\). If \(q=1\), with unique selected vertex \(b_j\), domination of \(A\) holds exactly when \(a_j\in S\); in the state notation this is exactly the case \(d=1\) and \(c=0\). If \(q=0\), domination of \(A\) requires every vertex of \(A\) to be selected. The symmetric statement holds with \(A\) and \(B\) exchanged.

Consider now an unselected vertex \(a_i\). Any defender must be some selected \(b_j\) with \(j\ne i\). After the swap \(b_j\mapsto a_i\), the number of selected \(B\)-vertices falls from \(q\) to \(q-1\), while the number of selected \(A\)-vertices rises from \(p\) to \(p+1\). The \(B\)-side domination condition is automatic after such a legal swap: if \(p\ge1\), then at least two \(A\)-vertices are selected afterward; if \(p=0\), the new unique selected \(a_i\) has its matched vertex \(b_i\) still selected because the defender has index \(j\ne i\). Thus only domination of the \(A\)-side can fail.

There are four possibilities. If no \(A\)-vertex is outside \(S\), equivalently \(a+c=0\), there is no attack to defend. If \(q\ge3\), removing any admissible defender leaves at least two selected \(B\)-vertices, so domination remains. If \(q=2\), then after a swap only one \(B\)-vertex remains. When \(a=0\), every unselected \(A\)-vertex is itself paired with one of the two selected \(B\)-vertices, so choosing the other selected \(B\)-vertex as defender leaves its matched partner selected after the swap. When \(a>0\), an attack at a \(00\)-pair can be defended exactly when at least one of the two selected \(B\)-vertices belongs to a \(11\)-pair, that is, exactly when \(d\ge1\). Finally, if \(q=1\), removal of the only selected \(B\)-vertex leaves none; the swap can therefore dominate \(A\) only when the attacked \(a_i\) was the sole unselected \(A\)-vertex, and the unique selected \(B\)-vertex must have a different index. This is exactly \((a,c,d)=(1,0,1)\). These cases are precisely \(\Phi_A\). Exchanging the two bipartition classes gives \(\Phi_B\). Hence \(S\) is secure if and only if \(\Phi_A\wedge\Phi_B\).

For each admissible quadruple \((a,b,c,d)\), the labeled matched pairs can be assigned those four states in exactly \(n!/(a!b!c!d!)\) ways, and the side sizes are \(p=b+d\) and \(q=c+d\). Summing these multinomial counts gives the displayed bivariate enumerator.

For \(n\ge5\), a secure set of size \(4\) cannot have \(p=0\) or \(q=0\), and the cases \((p,q)=(1,3)\) or \((3,1)\) would force only four matched-pair indices to account for all vertices outside the relevant side, contradicting \(n\ge5\). Hence \(p=q=2\). Because a size-four set cannot meet all \(n\ge5\) matched pairs, one has \(a>0\), so the \(q=2\) and \(p=2\) clauses force \(d\ge1\). Thus either \(d=2\), giving profile \((n-2,0,0,2)\), or \(d=1\), giving \((n-3,1,1,1)\). Their counts are \(\binom n2\) and \(n(n-1)(n-2)\), respectively. The exhaustive formula gives the stated small boundary values.

## Verification
The accompanying `verify_secure_crown.py` independently constructs each crown graph, enumerates every vertex subset for \(3\le n\le8\), checks secure domination directly from the definition, and compares it with the state criterion. It also independently aggregates the bivariate coefficients from the multinomial formula and checks the minimum-size counts. The finite computation checks the implementation and boundary cases; the infinite theorem rests on the proof above rather than on enumeration.

## Relationship to prior work
Secure domination is an established protection parameter; a 2004 bibliographic record for the foundational paper lists MSC 05C69. A 2016 paper on secure restrained domination explicitly treats secure and secure-restrained domination and states that it determines specific values for graph classes including crown graphs in its surrounding indexed literature. Because that source is directly relevant to the scalar crown-graph parameter, no scalar value \(\gamma_s(\operatorname{Cr}_n)\) is claimed as original here.

The closest broader structural result located in the current search gives the secure-domination polynomial of complete multipartite graphs. A crown graph is obtained from \(K_{n,n}\) by deleting a perfect matching, and the missing matched adjacencies are exactly what creates the index-sensitive \(00,10,01,11\) conditions above, so the complete-multipartite formula does not imply this classification. A 2020 paper develops secure-domination polynomials for paths, and a 2026 paper studies the connected-secure domination polynomial for paths, cycles, complete graphs, stars, and coronas; neither provides the crown-graph all-set profile.

A comprehensive 2014 dissertation on secure graph domination was also searched in full searchable text. It contains extensive material on complete bipartite graphs and edge-removal effects, but a direct full-text search returned no occurrence of “crown.” This does not by itself establish novelty, but it lowers the risk of an obvious same-object predecessor.

## Limitations
The 2016 secure-restrained paper is a plausible same-object source. Its abstract and indexed metadata were inspectable, but full text could not be obtained in this run without an unavailable interactive institutional step. Therefore the originality assessment explicitly retains residual risk that the paper may classify more crown-graph secure dominating sets than its public metadata indicates. The theorem does not claim priority for the scalar secure-domination number. Exhaustive verification was performed only through \(n=8\); it is a check, not the proof of the general result.

## References
1. E. J. Cockayne, O. Favaron, and C. M. Mynhardt, “Secure domination, weak Roman domination and forbidden subgraphs,” Bulletin of the Institute of Combinatorics and its Applications 39 (2003), 87–100. Exact bibliographic day and MSC evidence used here: zbMATH-linked record dated 23 August 2004, MSC 05C69.
2. P. Roushini Leely Pushpam and C. Suseendran, “Further results on secure restrained domination in graphs,” Journal of Discrete Mathematical Sciences and Cryptography 19 (2016), 277–291, DOI 10.1080/09720529.2014.1001590; published online 14 June 2016.
3. A. P. de Villiers, “Edge Criticality in Secure Graph Domination,” PhD dissertation, Stellenbosch University, 2014.
4. K. Lal Gipson and T. Subha, “Secure Domination Polynomials of Paths,” International Journal of Scientific & Technology Research 9 (2020).
5. J. D. Andoyo and R. F. Rulete, “On Connected Secure Domination Polynomial of Some Graphs,” Annals of Communications in Mathematics 9 (2026), article 9, DOI 10.62072/acm.2026.09025.
