# Exact two-step-domination polynomial of rectangular rook graphs

## Finding
For integers \(m,n\ge 2\), let \(R_{m,n}=K_m\square K_n\) be the rook graph on the ordered grid \([m]\times[n]\). A **two-step dominating set** is a subset \(S\) such that **every** vertex (including the selected ones) has a member of \(S\) at graph distance exactly two. Define the labelled-cardinality polynomial
\[
T_{m,n}(z)=\sum_{S\text{ two-step dominating in }R_{m,n}}z^{|S|}.
\]
Then
\[
\boxed{\begin{aligned}
T_{m,n}(z)={}&(1+z)^{mn}-mn(1+z)^{m+n-1}\\
&+m(n-1)(1+z)^n+n(m-1)(1+z)^m\\
&-(m-1)(n-1)+\frac{m(m-1)n(n-1)}2z^2.
\end{aligned}}
\]
For \(\min(m,n)=1\), the two-step-domination polynomial is identically zero, since no distance-two neighbors exist. The complete minimum-set census for \(m,n\ge2\) is
\[
\boxed{\begin{array}{c|c|c}
\text{case}&\text{minimum cardinality}&\text{number of minimum sets}\\\hline
\min(m,n)=2&4&\binom{\max(m,n)}{2}^{2}\\
\min(m,n)\ge3&3&6\binom m3\binom n3.
\end{array}}
\]
In the first case, each of the two short-side fibers contains exactly two selected cells; in the second case the three selected cells occupy three distinct rows and three distinct columns. The minimum cardinalities were previously known; the complete polynomial and the count of all minimizing labelled subsets are the contributions asserted here.

## Assumptions and scope
Graphs are finite, undirected, loopless and simple. The Cartesian product \(R_{m,n}\) has vertices \((i,j)\), adjacent when they differ in exactly one coordinate. For \(m,n\ge2\), two vertices of \(R_{m,n}\) have distance two exactly when **both** coordinates differ. Thus the distance-two adjacency graph is the direct (categorical, tensor, Kronecker) product \(K_m\times K_n\); a two-step dominating set in the rook graph is exactly a **total** dominating set of that direct product. This is **not** hop domination (which requires a distance-two witness only for vertices outside the set), nor ordinary domination of the product (which permits the vertex itself to cover itself).

The polynomial counts subsets of the individual labelled vertices, without dividing by graph automorphisms. All formulas are exact identities in \(\mathbb Z[z]\), with no asymptotic or random-model assumptions.

## Proof
Fix \(m,n\ge2\) and view \(S\) as the selected cells of an \(m\)-row, \(n\)-column binary array. For each row \(i\), define \(c_i\) to be the number of occupied columns containing **only** the selected cell in row \(i\). A column is called **strong** if it has at least two selected cells. A column is **singleton** if it has exactly one; others are empty.

Every vertex \((i,j)\) must see some selected \((i',j')\) with \(i'\ne i\) and \(j'\ne j\). Consequently the following condition is necessary and sufficient:

\[
\tag{1}\text{For each row }i,\text{ there are at least two distinct columns containing a selected cell outside row }i.
\]
Indeed, if at least two such columns exist, after excluding any one column \(j\) at least one remains; conversely, if at most one exists, the vertex in that column has no distance-two witness. Condition (1) applies to selected and unselected vertices alike.

Write \(w=(1+z)^m-1-mz\), the weighted enumerator of nonempty strong columns. Partition arrays by the number \(h\) of strong columns; these classes are disjoint.

If \(h\ge2\), condition (1) holds automatically because every strong column contains a selected cell outside every fixed row. Every column is otherwise an empty or singleton column with enumerator \(1+mz\). The contribution, by subtracting the cases with at most one strong column, is
\[
A=(1+z)^{mn}-(1+mz)^n-nw(1+mz)^{n-1}.
\]
If \(h=1\), its strong column already supplies one suitable column for every row. The remaining singleton columns must use at least two **different** row labels; otherwise the common label has no second external column. The contribution is therefore
\[
B=nw\big((1+mz)^{n-1}-m(1+z)^{n-1}+m-1\big).
\]
For \(h=0\), let \(t\) be the number of occupied singleton columns. Condition (1) becomes \(t-c_i\ge2\) for every row \(i\). Necessarily \(t\ge3\). Among \(m^t\) assignments of the \(t\) distinct columns to rows, the prohibited assignments are the \(m\) constant functions and the \(tm(m-1)\) functions with exactly one value different from the common value on the other \(t-1\) columns. For \(t\ge3\) these families are pairwise disjoint. Hence
\[
C=\sum_{t=3}^n\binom nt\big(m^t-m-tm(m-1)\big)z^t.
\]
Thus \(T_{m,n}=A+B+C\). Substituting \(w=(1+z)^m-1-mz\), using
\[
\begin{aligned}
\sum_{t=3}^n\binom nt z^t&=(1+z)^n-1-nz-\binom n2 z^2,\\
\sum_{t=3}^n t\binom nt z^t&=nz(1+z)^{n-1}-nz-n(n-1)z^2,
\end{aligned}
\]
and collecting powers yields exactly the boxed symmetric closed formula. This is an identity of finite polynomials, so it also covers the boundary cases \(m=n=2\) and \(n=2\).

For the minimum-set classification, a selected set with at most two cells fails (1): if the cells are in distinct rows, consider one of those rows; if they are in a common row, that row has no external selected cell. With three cells, condition (1) precludes a strong column, since only one further selected column could exist; it also forces all three occupied columns to have different row labels. Thus three-cell solutions exist precisely when \(m,n\ge3\), and consist of an injective correspondence between three chosen rows and three chosen columns. Their number is \(\binom m3\binom n3 3!\).

When \(m=2\), (1) requires at least two selected columns in row \(1\) and at least two selected columns in row \(2\), so four cells are necessary and sufficient. Every minimum set is a choice of two distinct columns independently in each row, giving \(\binom n2^2\) possibilities. Interchanging rows and columns handles \(n=2\). These arguments classify every minimizer and prove the minimum-count assertions.

If \(\min(m,n)=1\), the rook graph is complete or a singleton and has no pair of vertices at distance two. Consequently no two-step dominating subset exists.

## Verification
The accompanying standalone script `verify.py` computes the closed formula with exact integer binomial coefficients. Independently, it enumerates all labelled vertex subsets and checks the **definition** of distance-two domination with bit-mask neighborhoods, without using the row/column characterization in the enumerator. It exhaustively checks 13 dimension pairs up to 18 vertices (714,576 subsets) and obtains exact coefficient-by-coefficient agreement. It also checks symmetry, nonnegative coefficients, and the minimum-size/multiplicity formulas for 841 further parameter pairs \((m,n)\) with \(2\le m,n\le30\). The exhaustive checks are finite consistency tests, not substitutes for the polynomial proof above.

For example, \(T_{2,2}(z)=z^4\), \(T_{2,3}(z)=9z^4+6z^5+z^6\), and the first nonzero coefficient of \(T_{3,3}(z)\) is \(6z^3\). To reproduce: `python3 verify.py` using Python 3.8 or later; the verifier has no nonstandard dependencies.

## Relationship to prior work
Das, Das and Islam (2026) distinguish hop domination from two-step domination and investigate complexity on regular and claw-free graph classes. The present theorem is a precise enumeration in the regular rook-graph family, rather than a complexity result. Zhao, Shan and Ahangar (2013, Theorem 3) had already determined the minimum total domination number of the direct product \(K_m\times K_n\) to be \(4\) if the shorter factor has order \(2\), and \(3\) otherwise. Those minimum cardinalities are not claimed as new. The present polynomial resolves the entire cardinality distribution and classifies/counts every minimum set.

Burcroff and O'Brien (2021, Section 5) analyze the **ordinary domination polynomial** of direct products of complete graphs and the rook graph; that notion admits self-coverage and is not the total domination enumerator computed here. Dod's 2016 work on trivariate total-domination polynomials of graph products may contain further related identities, but its full text could not be inspected here. Therefore final priority with respect to that paper, and to unlocated literature, is not established; the formula is a best-knowledge candidate, not an independently certified publication-priority claim.

## Limitations
The theorem applies to the complete two-factor rook grid, not arbitrary Cartesian products or higher-dimensional Hamming graphs. For \(\min(m,n)=1\) there are no admissible subsets. The exhaustive verifier covers only its stated finite ranges. A relevant 2016 graph-products paper could not be compared at theorem level, and independent mathematical review and comprehensive bibliographic priority verification have not occurred.

## References
1. S. Das, S. Das and S. S. Islam, *On the Complexity of Hop Domination and 2-Step Domination in Graph Classes*, arXiv:2605.20970, first posted 20 May 2026. https://arxiv.org/abs/2605.20970
2. Y. Zhao, E. Shan and H. A. Ahangar, *Signed total domination on Kronecker products of two complete graphs*, Australasian Journal of Combinatorics **56** (2013), 95–102, especially Theorem 3. https://ajc.maths.uq.edu.au/pdf/56/ajc_v56_p095.pdf
3. A. Burcroff and G. O'Brien, *Unimodality and monotonic portions of certain domination polynomials*, arXiv:2110.00709, Section 5. https://arxiv.org/abs/2110.00709
4. M. Dod, *Graph products of the trivariate total domination polynomial and related polynomials*, Discrete Applied Mathematics **209** (2016), 92–101. DOI:10.1016/j.dam.2015.10.008 (abstract inspected; complete manuscript not inspected).
