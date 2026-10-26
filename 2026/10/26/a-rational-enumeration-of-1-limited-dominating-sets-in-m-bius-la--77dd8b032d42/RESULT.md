# A rational enumeration of 1-limited dominating sets in Möbius ladders

## Finding

For every integer \(n\ge3\), let \(M_{2n}\) be the cubic Möbius ladder with vertex set \(\mathbb Z/(2n)\mathbb Z\), rim edges between consecutive residues, and opposite chords joining residues at difference \(n\). A set \(D\) is **1-limited dominating** when every vertex outside \(D\) has a neighbor in \(D\), while every vertex in \(D\) has at most one neighbor outside \(D\). Define the full complement-cardinality enumerator
\[
F_n(z)=\sum_{D\,\text{1-limited dominating in }M_{2n}} z^{2n-|D|}.
\]
Set
\[
Q(t,z)=t+t^2z+t^3(z+2z^2)+t^4(z^2+z^3+z^4)+t^5z^4.
\]
The **complete enumerator for every cardinality** is determined by the single rational logarithmic-derivative identity
\[
\boxed{\sum_{n\ge1}F_n(z)t^n=-t\frac{\partial}{\partial t}
\log\!\left(\frac{(1-tz)(1-Q(t,z))}{1-tz+t^2z}\right).}
\]
The coefficients with \(n\ge3\) count the indicated simple graphs; those with \(n=1,2\) are auxiliary formal coefficients of the transfer construction, not graph claims. Equivalently, for every \(n\ge3\),
\[
F_n(z)=z^n+n[t^n]\sum_{k\ge1}\frac{Q(t,z)^k-[tz(1-t)]^k}{k}.
\]
In particular, if \(N_n\) denotes the number of minimum-cardinality 1-limited dominating sets, then
\[
\boxed{\gamma_1^{\mathrm L}(M_{2n})=\begin{cases}n,&4\mid n,\\n+1,&4\nmid n,\end{cases}\quad
N_n=\begin{cases}4,&n\equiv0\pmod4,\\2n,&n\equiv2\pmod4,\\3n,&n\text{ odd}.\end{cases}}
\]
The minimum-size formula and the four optima when \(4\mid n\) were already recorded in an earlier comparison; the full cardinality enumerator and the optimal multiplicities when \(4\nmid n\) are the new claims.

## Assumptions and scope

Graphs are finite, simple, with fixed labeled rim vertices. Distinct vertex sets are counted separately even if related by graph automorphisms. The result is for all integers \(n\ge3\), without an asymptotic qualification. The exponent of \(z\) counts excluded (white) vertices, so the largest degree of \(F_n\) corresponds to the *smallest* size of a dominating set. Because the graph is cubic, 1-limited domination is also called \((1,2)\)-domination: selected vertices have at least two selected neighbors.

## Proof

**1. Local encoding.** Divide the rim into \(n\) two-vertex columns, with vertices \(i\) and \(i+n\) in column \(i\). Let \(c_i=(c_{i,0},c_{i,1})\in\{0,1\}^2\), where a bit is \(1\) exactly when its vertex is *outside* \(D\). If \(\sigma\) swaps the two coordinates, twisted closure of the rim means \(c_{i+n}=\sigma c_i\), and in particular \(c_{-1}=\sigma c_{n-1}\) and \(c_n=\sigma c_0\). For each row \(r\in\{0,1\}\), the three neighbors of the vertex at column \(i\) consist of its other-row partner and its same-row neighbors in columns \(i-1\) and \(i+1\). Both defining domination conditions are therefore exactly the inequality
\[
c_{i-1,r}+c_{i+1,r}+c_{i,1-r}\ \le\ 1+c_{i,r}.
\]
Indeed, at a selected vertex the left side may not exceed one, while at an excluded vertex the left side may not equal three, which is precisely the requirement for a selected neighbor.

**2. Twisted transfer.** Use the four possible column words as an alphabet \(\mathcal A\) and index a \(16\)-state matrix \(T(z)\) by ordered pairs \((p,c)\in\mathcal A^2\). Its entry from \((p,c)\) to \((c,q)\) is \(z^{|c|}\) if both inequalities from Step 1 hold with neighbors \(p,q\), and is zero otherwise. No other entries are nonzero. Let \(J\) be the permutation matrix taking \((p,c)\) to \((\sigma p,\sigma c)\). The transfer commutes with \(J\). A closed length-\(n\) path with this twist corresponds bijectively to the labeled admissible configuration \((c_0,\ldots,c_{n-1})\); each column contributes its white-vertex weight exactly once. Thus
\[
F_n(z)=\operatorname{tr}(T(z)^n J)
=\operatorname{tr}(T_+(z)^n)-\operatorname{tr}(T_-(z)^n),
\]
where \(T_+\) and \(T_-\) are the restrictions to the symmetric and antisymmetric eigenspaces of \(J\).

**3. Finite determinant identity.** In the orbit-sum and orbit-difference bases of these eigenspaces, omit states outside directed cycles (their matrices are strictly triangular after permutation and contribute only zero eigenvalues). The remaining matrices are the following explicit matrices, with the row/column order as displayed:
\[
A_+(z)=\begin{pmatrix}
1&2&1&0&0&0&0\\
0&0&0&z&z&0&0\\
0&0&0&0&0&z^2&z^2\\
1&1&0&0&0&0&0\\
0&0&0&z&z&0&0\\
1&0&0&0&0&0&0\\
0&0&0&0&0&z^2&0
\end{pmatrix},\qquad
A_-(z)=\begin{pmatrix}
0&z&z\\-1&0&0\\0&z&z
\end{pmatrix}.
\]
To make this reduction independently checkable, encode a column by the integer \(c_{i,0}+2c_{i,1}\). The ordered-pair indices in lexicographic order are \(0,\ldots,15\). For \(A_+\), take (respectively) the symmetric orbit vectors supported at indices \(\{0\},\{1,2\},\{3\},\{4,8\},\{5,10\},\{12\},\{15\}\); for \(A_-\), take the differences at \(\{1,2\},\{4,8\},\{5,10\}\), with the lower index having coefficient \(+1\). The remaining orbit vectors are transient: they lie on no directed cycle. Direct expansion along rows of the two displayed matrices gives
\[
\det(I-tA_+(z))=(1-tz)(1-Q(t,z)),\qquad
\det(I-tA_-(z))=1-tz+t^2z.
\]
These are finite polynomial equalities in \(\mathbb Z[t,z]\). The independent pure-integer determinant computation in `verify.py` evaluates both determinants by the Leibniz formula, with the same displayed entries, and confirms the identities coefficientwise. The omitted acyclic states cannot change a trace of a positive matrix power or either determinant.

**4. Extracting all sizes.** The formal identity \(-t\partial_t\log\det(I-tA)=\sum_{n\ge1}\operatorname{tr}(A^n)t^n\), valid over formal power series with polynomial coefficients, applied to the two determinants in Step 3 proves the stated rational logarithmic-derivative formula. Expanding the three logarithms gives the alternative finite coefficient formula in the Finding section.

**5. Optimal sizes and multiplicities.** Every monomial \(t^a z^b\) in \(Q\) has deficit \(a-b\ge0\); zero deficit occurs only for \(t^4z^4\). In the alternative formula, the \(z^n\) term cancels exactly with the corresponding \(k=n\) term from \([tz(1-t)]^k\). Thus the degree of \(F_n\) is at most \(n\). If \(4\mid n\), the only way a product of terms from \(Q\) has total length \(n\) and total deficit zero is to take \(n/4\) copies of \(t^4z^4\). Its coefficient after the logarithmic factor \(n/k\) is \(4\); therefore \([z^n]F_n(z)=4\).

When \(4\nmid n\), degree \(n\) is impossible. To reach degree \(n-1\) from \(Q\), exactly one monomial must have deficit one, and all others must be copies of \(t^4z^4\). The available deficit-one monomials are
\[
t,\quad t^2z,\quad 2t^3z^2,\quad t^4z^3,\quad t^5z^4.
\]
Their total-length residues modulo four give coefficients \(2n\) when \(n\equiv1\pmod4\) (the length-one and length-five choices), \(n\) when \(n\equiv2\pmod4\), and \(2n\) when \(n\equiv3\pmod4\). This covers \(n\ge3\): in the residue-one case the first relevant order is \(n=5\), where both choices exist. The subtracted \([tz(1-t)]^k\) contribution adds exactly \(n\) to \([z^{n-1}]F_n\), because only \(k=n-1\) contributes and \([t^n]t^{n-1}(1-t)^{n-1}=-(n-1)\). The resulting positive counts are \(3n,2n,3n\) in residues one, two, three. Since \(|D|=2n-|V\setminus D|\), the asserted minimum sizes and numbers of minima follow. \(\square\)

## Verification

The enclosed standalone `verify.py` uses only the Python standard library. It (i) independently computes both displayed determinants by exact subset-form Leibniz expansion; (ii) obtains the coefficient polynomials via Newton identities and compares them against the unreduced sixteen-state twisted transfer for all \(3\le n\le50\); and (iii) independently enumerates every vertex subset and checks the graph-theoretic definition directly for all \(3\le n\le10\). The final line is `VERIFY_OK`. These finite checks corroborate, but do not replace, the unrestricted combinatorial and determinant proof above.

For illustration, \(F_3(z)=1+6z+9z^2\) and \(F_4(z)=1+8z+12z^2+8z^3+4z^4\); every coefficient counts *excluded* vertices.

## Relationship to prior work

Tepeh's 2026 study of limited domination in Cartesian products established general bounds and exact numbers for several structured graph families, providing the current enumeration's impetus. Radić and Tepeh's October 2026 study proves complexity results and evaluates the invariant for Goldberg snarks, not the complete set distribution of Möbius ladders. The earlier general cubic-graph study by Fakharan and coauthors treats \((1,2)\)-domination bounds. A pre-existing directly related record, identified by the opaque claim ID `667abaa2-f0fd-48af-af32-0526b89aa687`, already gives the minimum size and the four minimum sets when \(4\mid n\). Those statements are expressly **not** claimed here as new. The full all-cardinality generating function and the additional multiplicity formulas are not consequences of merely knowing this extremal value, and no equivalent all-size formula was found in the searched primary literature or research index.

The equivalent formulation in terms of white/blue partitions and perfect matching cuts covers the lower-bound equality case but does not provide the full polynomial or the non-equality optimal multiplicities. Ordinary domination polynomials and homology of ladder matching complexes concern distinct objects.

## Limitations

The graph family is the opposite-chord Möbius ladder, not the ordinary circular ladder, and only \(n\ge3\) represents the specified simple cubic graph. The enumeration is for labeled vertex sets and does not quotient by automorphisms. The rational transfer expression is an all-order proof, while direct subset enumeration ends at \(n=10\). The cited primary texts and indexed results were compared, but literature searches cannot rule out unindexed prior equivalent enumerators. This has received a self-review; no independent audit or external mathematical validation has been performed.

## References

1. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428, first publicly submitted June 21, 2026. https://arxiv.org/abs/2606.22428
2. G. Radić and A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796v1, first publicly submitted October 1, 2026. https://arxiv.org/abs/2610.01796
3. M. H. Fakharan, A. A. Gorzin, M. A. Henning, A. Jafari and R. Touserkani, *On (1,2)-domination in cubic graphs*, Discrete Mathematics 344 (2021), 112546. https://doi.org/10.1016/j.disc.2021.112546
4. D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On \(k\)-limited domination in graphs*, Computational and Applied Mathematics (online September 11, 2026). https://doi.org/10.1007/s40314-026-03902-2
