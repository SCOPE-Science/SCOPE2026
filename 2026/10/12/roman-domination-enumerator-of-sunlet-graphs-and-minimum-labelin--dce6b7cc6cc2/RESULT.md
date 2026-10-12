# Roman-domination enumerator of sunlet graphs and minimum-labeling multiplicities

## Finding
For every integer \(n\ge3\), let \(S_n=C_n\circ K_1\) denote the sunlet graph with a cycle vertex \(v_i\) and its private leaf \(\ell_i\) at each cyclic index \(i\in\mathbb Z/n\mathbb Z\). A Roman dominating function is \(f:V(S_n)\to\{0,1,2\}\) such that every vertex labeled \(0\) is adjacent to a vertex labeled \(2\). Define the Roman-domination polynomial
\[
R_n(z)=\sum_{f\text{ Roman dominating}}z^{\sum_{x\in V(S_n)}f(x)}.
\]
Set
\[
A=z^2(1+z+z^2),\quad B=z(1+z)^2,\quad C=z^2(2+z),
\]
and
\[
D(u,z)=1-(A+C)u-Azu^2-ABzu^3.
\]
Then the complete polynomial at every order is determined by the rational generating function
\[
\boxed{\sum_{n\ge3}R_n(z)u^n=-u\frac{\partial}{\partial u}\log D(u,z)-(A+C)u-(A^2+C^2+2AB)u^2.}
\]
Equivalently, for every \(n\ge4\),
\[
\boxed{R_n(z)=(A+C)R_{n-1}(z)+AzR_{n-2}(z)+ABzR_{n-3}(z),}
\]
where the necessary initial polynomial \(R_3\) and auxiliary traces \(R_1,R_2\) are
\[
R_1=A+C,\qquad R_2=A^2+C^2+2AB,\qquad
R_3=A^3+3A^2B+3AB^2+C^3.
\]
Here \(R_1,R_2\) are *auxiliary matrix traces*, not graph polynomials for nonexistent simple one- and two-cycles.

The minimum weight is \(n+\lceil n/3\rceil\), a value already implied by published Roman-domination results for coronas. The new exact number \(r_n\) of functions attaining that weight is
\[
\boxed{r_n=[z^{n+\lceil n/3\rceil}]R_n(z)=
\begin{cases}
3,&n=3k,\quad k\ge1,\\
\dfrac{(3k+1)(k+6)}2,&n=3k+1,\quad k\ge1,\\
3k+2,&n=3k+2,\quad k\ge1.
\end{cases}}
\]

## Assumptions and scope
Graphs are finite, simple, and labeled at their cyclic vertices; counts are of functions on those labeled vertices, with no quotient by graph automorphisms. The cycle length satisfies \(n\ge3\). A labeled leaf has exactly one neighbor, its corresponding cycle vertex. All polynomials have nonnegative integer coefficients and use total Roman weight, not number of positive vertices or number of label-\(2\) vertices.

## Proof
**1. Fiber reduction.** Fix \(T=\{i:f(v_i)=2\}\) and let \(t=|T|\). If \(i\in T\), the leaf can take any label \(0,1,2\) and its local weight polynomial is \(A\). If \(i\notin T\) but at least one cycle neighbor belongs to \(T\), the allowed pairs \((f(v_i),f(\ell_i))\) are \((0,1),(0,2),(1,1),(1,2)\), giving \(B=z+2z^2+z^3\). If \(i\notin N_{C_n}[T]\), the pair \((0,1)\) is forbidden, while \((0,2),(1,1),(1,2)\) are allowed, giving \(C=2z^2+z^3\). The local conditions are sufficient as well as necessary: each leaf labeled \(0\) sees its cycle vertex labeled \(2\), and each cycle vertex labeled \(0\) either sees a cycle neighbor labeled \(2\) or has a leaf labeled \(2\).

Writing \(d(T)=|N_{C_n}(T)\setminus T|\) and \(q(T)=n-|T|-d(T)\), this gives the independent exact subset formula
\[
\boxed{R_n(z)=\sum_{T\subseteq V(C_n)}A^{|T|}B^{d(T)}C^{q(T)}.}
\]

**2. Cyclic transfer and rational generating function.** Encode \(T\) by a cyclic binary word, with digit \(1\) at its vertices. Use the four ordered states \(00,01,10,11\), where a transition from \((p,q)\) to \((q,r)\) contributes the local weight of the middle digit. The weighted transition matrix is
\[
M=\begin{pmatrix}
C&B&0&0\\
0&0&A&A\\
B&B&0&0\\
0&0&A&A
\end{pmatrix}.
\]
For every \(n\ge3\), closed length-\(n\) walks are in bijection with binary words on the *fixed labeled* cycle, and their products of transition weights equal the terms in the subset formula. Thus \(R_n(z)=\operatorname{tr}(M^n)\). Direct polynomial expansion of the displayed \(4\)-by-\(4\) determinant gives
\[
\det(I-uM)=1-(A+C)u+A(C-B)u^2+AB(C-B)u^3.
\]
Since \(B-C=z\), this is exactly \(D(u,z)\) in the statement. The formal logarithmic-determinant identity
\[
-\,u\frac{\partial}{\partial u}\log\det(I-uM)
=\sum_{j\ge1}\operatorname{tr}(M^j)u^j
\]
requires no convergence assumption. Subtracting the first two auxiliary traces proves the generating function. The characteristic polynomial is \(\lambda(\lambda^3-(A+C)\lambda^2-Az\lambda-ABz)\). Cayley–Hamilton and traces give the displayed third-order recurrence at every \(n\ge4\); direct trace multiplication gives the initial polynomials.

**3. Minimum weights and multiplicities.** For fixed \(T\), the lowest exponent of its term in the subset formula is \(n+|T|+q(T)\); its coefficient is \(2^{q(T)}\), because the minimum terms of \(A,B,C\) have respective coefficients \(1,1,2\). The set \(T\cup(V(C_n)\setminus N_{C_n}[T])\) dominates \(C_n\), hence \(|T|+q(T)\ge\gamma(C_n)=\lceil n/3\rceil\); equality is attained by a minimum dominating set as \(T\), so the minimum Roman weight is \(n+\lceil n/3\rceil\).

To count equality cases, write \(n=3k+s\), with \(s\in\{0,1,2\}\). Since a vertex of \(T\) dominates at most three cycle vertices, equality and \(n\le3|T|+q(T)\) restrict \((|T|,q(T))\) to \((k,0)\) for \(s=0\), \((k+1,0)\) or \((k,1)\) for \(s=1\), and \((k+1,0)\) for \(s=2\). For nonempty \(T\), list the cyclic positive gaps between its successive positions, summing to \(n\). The number of undominated vertices in a gap of length \(g\) is \(\max(g-3,0)\). In the zero-undominated cases, all gaps belong to \(\{1,2,3\}\). If \(n=3k\), they are all \(3\), giving exactly three subsets. If \(n=3k+2\), exactly one gap is \(2\), giving \(n\) subsets. If \(n=3k+1\) with \(k+1\) selected vertices, the total deficit from gaps of length \(3\) is two: either one gap \(1\) or two gaps \(2\), for
\[
\frac{n}{k+1}\left((k+1)+\binom{k+1}{2}\right)=\frac{n(k+2)}2
\]
subsets. Finally, if \(n=3k+1\) and \(|T|=k,q(T)=1\), exactly one gap has length \(4\) and all others have length \(3\), giving \(n\) subsets, each weighted \(2\) because of its one undominated vertex. The total \(n(k+2)/2+2n=n(k+6)/2\) completes the proof.

## Verification
The standalone standard-library checker `verify.py` independently constructs the Roman-domination polynomials by exhaustive ternary labelings for \(n=3,4,5,6\); by enumeration of all subsets \(T\) for \(3\le n\le12\); and by exact polynomial traces of the transfer matrix for \(1\le n\le14\). It checks the recurrence for \(4\le n\le14\) and the minimum weights and multiplicities for \(3\le n\le14\). Its expected concluding line is:

`VERIFY_OK brute_orders=3..6 assignments=597780 subset_orders=3..12 trace_orders=3..14 polynomial_recurrence_orders=4..14 minimum_counts=3..14`

As a small independent coefficient example,
\[
R_3(z)=3z^4+18z^5+54z^6+81z^7+75z^8+47z^9+21z^{10}+6z^{11}+z^{12}.
\]
These are finite corroborations; the proof of the formulas for arbitrary \(n\) is the fiber reduction, transfer identity, and gap enumeration above.

## Relationship to prior work
Roman domination and Roman-domination numbers are established notions. Eullaran and Baldado (2011) treat the Roman-domination number of arbitrary graph coronas. That result already controls the minimum *weight* here and is explicitly not claimed as new. Gangabylaiah, Indiramma, Soner, and Alwardi (2021) define the Roman-domination polynomial and derive, among other results, a polynomial for \(K_n\circ K_1\) (their Theorem 3.7); for \(n\ge4\), the graph \(C_n\circ K_1\) is not of that complete-base form. The subsequent cycle-polynomial study treats \(C_n\) itself, not its pendant corona. The present result adds an evaluated all-weight enumeration on the sunlet family and exact residue-dependent counts of minimum functions. The known coronas' minimum-weight formula and the preexisting cycle-only or complete-base polynomial do not, on their stated domains, give these formulas without a new local-pair analysis.

## Limitations
No claim is made to a new Roman-domination number, a theorem for arbitrary attachment graphs, or a fully automated uniqueness certification. The 2011 corona-number paper's public abstract and date were checked but its linked full-text download was unavailable; that access limitation and the possibility of an earlier differently indexed sunlet enumeration remain priority risks. An indexed cycle-polynomial paper was examined through available theorem excerpts, but its full PDF endpoint denied access, so the absence of a concealed equivalent formula there is not asserted from snippets. The finite verification checks only the stated orders and is not a substitute for the symbolic proof.

## References
1. E. J. Cockayne, P. A. Dreyer, S. M. Hedetniemi, and S. T. Hedetniemi, *Roman domination in graphs*, Discrete Mathematics 278 (2004), 11–22.
2. L. Eullaran and M. Baldado Jr., *Roman domination number of the join and corona of graphs*, The Mindanawan Journal of Mathematics 2 (2011), 66–69; publication page dated 2011-10-01: https://journals.msuiit.edu.ph/tmjm/article/view/20 .
3. D. Gangabylaiah, I. M. H., N. D. Soner, and A. Alwardi, *On the Roman domination polynomial of graphs*, Bulletin of the International Mathematical Virtual Institute 11 (2021), 355–365. DOI: https://doi.org/10.7251/BIMVI2102355G .
4. D. G., A. Alwardi, and I. M. H., *Roman Domination Polynomial of Cycles*, International Journal of Mathematical Combinatorics 3 (2021), 86–97. Indexed copy: https://fs.unm.edu/IJMC/Roman_Domination_Polynomial_of_Cycles.pdf .
5. F. N. Abu-Khzam, H. Fernau, and K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, arXiv:2208.05261 (2022); this studies enumeration of *minimal* Roman functions, a different all-weight question.
