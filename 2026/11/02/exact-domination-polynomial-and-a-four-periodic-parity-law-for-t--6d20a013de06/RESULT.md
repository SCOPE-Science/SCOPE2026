# Exact domination polynomial and a four-periodic parity law for three-row cylindrical king graphs

## Finding

Let \(H_n=P_3\boxtimes C_n\), the strong product of a three-vertex path with an \(n\)-cycle, for an integer \(n\ge3\). Let \(D_n(z)=\sum_{S\subseteq V(H_n),\ S\text{ dominates }H_n}z^{|S|}\) be the ordinary domination polynomial. Put
\[
u=z,\qquad v=z+3z^2+z^3,
\]
and define the monic polynomials
\[
A(X)=X^3+uX^2+u^2X-u^2,
\]
\[
B(X)=X^6-(u+v)X^5-(u^2+uv+v)X^4
 -(u^2v+u^2+3uv+v)X^3+uvX^2+u^2v.
\]
For every integer \(n\ge3\), the complete domination polynomial has the algebraic power-sum form
\[
\boxed{D_n(z)=\sum_{A(\alpha)=0}\alpha^n+\sum_{B(\beta)=0}\beta^n.}
\]
Roots are taken over an algebraic closure of \(\mathbb Q(z)\), with algebraic multiplicity. Thus every cardinality count of dominating sets is determined by two fixed polynomials of degrees three and six, independently of the circumference. In particular, the signed domination count satisfies the exact four-periodic law
\[
\boxed{D_n(-1)=\begin{cases}9,&4\mid n,\\1,&4\nmid n.\end{cases}}
\]
Equivalently, the number of even-cardinality dominating sets exceeds the number of odd-cardinality dominating sets by nine precisely when the circumference is divisible by four, and by one otherwise.

## Assumptions and scope

All graphs are simple and undirected. Write \(V(H_n)=\{(r,j):r\in\{1,2,3\},\ j\in\mathbb Z/n\mathbb Z\}\). Two *distinct* vertices are adjacent if their path coordinates differ by at most one and their cycle coordinates differ by at most one modulo \(n\). Thus the closed neighborhood of \((r,j)\) is exactly
\[
N[(r,j)]=\bigl(\{r-1,r,r+1\}\cap\{1,2,3\}\bigr)\times\{j-1,j,j+1\}.
\]
The three columns indexed by \(j-1,j,j+1\) are distinct for every \(n\ge3\). A dominating set meets every closed neighborhood. The polynomial includes the coefficient of every possible set size, including a zero constant term.

## Proof

**Column compression.** For any selected subset of a column, record which rows are covered by its selected vertices within that column and either adjacent column. There are only four possible row-coverage types: \(0=\varnothing\), \(L=\{1,2\}\), \(R=\{2,3\}\), and \(F=\{1,2,3\}\). The weight, namely the sum of \(z^{\lvert S_j\rvert}\) over actual subsets having a given type, is respectively
\[
 w_0=1,\quad w_L=u=z,\quad w_R=u=z,\quad w_F=v=z+3z^2+z^3.
\]
Indeed, the full-coverage subsets are the middle singleton, the three two-element subsets, and the entire column. Compression does not lose multiplicity because the choices in different columns are independent once their coverage types have been specified.

**Local condition and transfer.** A cyclic word \((a_0,\ldots,a_{n-1})\) on \(\{0,L,R,F\}\) represents a dominating set if and only if, for every \(j\), the union of the row-coverage types \(a_{j-1}\cup a_j\cup a_{j+1}\) equals \(F\). This is equivalent to saying that each consecutive triple contains \(F\), or contains both \(L\) and \(R\). It follows directly from the displayed closed-neighborhood description.

Order the symbols as \((0,L,R,F)\) and let \(T\) be a \(16\times16\) matrix indexed by ordered symbol pairs. Its entry from \((a,b)\) to \((b,c)\) equals \(w_b\) if \(a\cup b\cup c=F\), and is zero otherwise; every entry not of this specified form is zero. A closed walk of length \(n\) in this pair-state graph uniquely specifies a cyclic word with labeled columns. It contributes \(\prod_{j=0}^{n-1}w_{a_j}\). Therefore the exact polynomial, for every \(n\ge3\), is
\[
D_n(z)=\operatorname{tr}(T^n).
\]
No limiting or asymptotic argument is involved.

**Finite exact determinant.** With the above explicit entry rule, direct determinant expansion over \(\mathbb Z[u,v,X]\) yields
\[
\det(XI_{16}-T)=X^7 A(X)B(X).
\]
This is a finite polynomial identity, not a numerical fit. Its left side is completely specified by the preceding entry rule and its right side by the displayed cubic and sextic. The accompanying standalone checker constructs all 256 matrix entries and recomputes the characteristic polynomial symbolically to verify the identity over \(\mathbb Z[z,X]\). In particular, the seven zero eigenvalues contribute nothing to traces of positive powers. For every positive \(n\), the trace of \(T^n\) equals the sum of the \(n\)th powers of the nine nonzero algebraic eigenvalues with multiplicity, proving the stated exact formula for \(n\ge3\).

**Specialization at \(z=-1\).** Here \(u=-1\), \(v=1\), and the two factors reduce to
\[
A(X)=(X-1)(X^2+1),\qquad
B(X)=(X-1)^2(X+1)^2(X^2+1).
\]
Thus the nine roots, with multiplicities, are \(1\) three times, \(-1\) twice, and each of \(i\) and \(-i\) twice. Consequently,
\[
D_n(-1)=3+2(-1)^n+2i^n+2(-i)^n.
\]
For odd \(n\), this is \(1\). For \(n\equiv2\pmod4\), it is also \(1\), and for \(n\equiv0\pmod4\), it is \(9\). This completes the proof.

## Verification

The file `verify.py` is a standalone Python 3/SymPy implementation of the stated definitions, not a source of an unproved infinite extrapolation. It verifies the characteristic polynomial identity symbolically, compares the entire polynomial against independently enumerated graph dominating sets for every \(n\in\{3,4,5,6\}\), and evaluates the integer signed transfer for all \(1\le n\le64\). All checks returned `VERIFY_OK` in the recorded execution. The computation for \(n=1,2\) tests only the formal transfer trace, not simple-cycle graph boundary cases; the theorem starts at \(n=3\). The proof of the infinite statement is the transfer bijection and exact characteristic polynomial identity.

## Relationship to prior work

Moore and Mertens established the alternating-sum identity \(D_{P_m\boxtimes P_n}(-1)=(-1)^{\lceil m/2\rceil\lceil n/2\rceil}\) for king graphs on ordinary rectangular boards and explicitly observed that cyclic boundary conditions change the behavior [1, Section 3]. Their finite cylinder table uses a cyclic **first** coordinate, namely \(C_m\boxtimes P_n\), whereas the present graph has a three-vertex **noncyclic first** coordinate and a cyclic second coordinate, \(P_3\boxtimes C_n\); their displayed row \(m=3\) therefore does not tabulate this family. No all-circumference ordinary domination-polynomial factorization for the present family appears there. Small cases here are verified directly from adjacency.

Mertens gave transfer-matrix algorithms for domination polynomials of Cartesian grids, Cartesian cylinders and tori, as well as rectangular *noncyclic* king graphs [2, Sections 1–3 and 6]. That general methodology motivates using finite states, but its stated graph families and conclusions do not give the present nine-root factorization or four-periodic signed law. Klobučar studied independent sets and independent dominating sets of strong products of paths and cycles [3]; independent domination is a different counting invariant from all ordinary dominating sets.

## Limitations

The theorem covers precisely \(P_3\boxtimes C_n\) with \(n\ge3\), not general king-cylinder widths or the toroidal strong product \(C_m\boxtimes C_n\). The algebraic root-sum is an exact coefficient prescription rather than a coefficientwise elementary binomial formula. The characteristic polynomial factorization is finite algebra explicitly replayable by the checker. Publication-priority searches cannot rule out unindexed or differently formulated results. Independent external mathematical audit has not been performed. The published small-cylinder table makes the first coordinate cyclic, unlike the family treated here; it has not been treated as a certificate for this graph definition.

## References

[1] C. Moore and S. Mertens, *Domination by kings is oddly even*, arXiv:2407.19344v1, submitted July 27, 2024. https://arxiv.org/abs/2407.19344

[2] S. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, arXiv:2408.08053v1, submitted August 15, 2024. https://arxiv.org/abs/2408.08053

[3] A. Klobučar, *Independent sets and independent dominating sets in the strong product of paths and cycles*, Mathematical Communications 10 (2005), 23–30. https://hrcak.srce.hr/en/657
