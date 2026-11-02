# Truncated period-lattice spectra classify finite commuting permutations in every variable width

## Finding
Let \(\mathscr A\) be the class of finite structures \((X,\sigma,\tau)\) in a language of **two unary function symbols**, where \(\sigma\) and \(\tau\) are commuting permutations. The empty structure is allowed. For every finite-index subgroup \(H\leq\mathbb Z^2\), let \(m_X(H)\) be the number of orbits of the induced \(\mathbb Z^2\)-action with point stabilizer \(H\). For every integer \(k\geq1\), ordinary first-order logic with at most \(k\) reusable variables and no counting quantifiers satisfies
\[
(X,\sigma,\tau)\equiv_{\mathrm{FO}^k}(Y,\sigma',\tau')
\quad\Longleftrightarrow\quad
\min\{m_X(H),k\}=\min\{m_Y(H),k\}\quad\text{for all finite-index }H\leq\mathbb Z^2.
\]
The quantifier depth is unrestricted. This is a classification **within** the class of finite commuting-permutation structures in the function-symbol signature.

Each equivalence class has a unique, up to isomorphism, smallest representative, obtained by replacing \(m_X(H)\) with \(\min\{m_X(H),k\}\) for each \(H\). Its size is \(\sum_H[\mathbb Z^2:H]\min\{m_X(H),k\}\). If the two structures are nonisomorphic, their minimum distinguishing variable width is
\[
1+\min_{H:m_X(H)\ne m_Y(H)}\min\{m_X(H),m_Y(H)\}.
\]
There are \(\sigma_1(h)=\sum_{d\mid h}d\) subgroups of index \(h\) in \(\mathbb Z^2\). Consequently the number of \(\mathrm{FO}^k\)-classes whose smallest representative has exactly \(n\) elements is the coefficient of \(z^n\) in the formal power series
\[
F_k(z)=\prod_{h\geq1}\left(1+z^h+z^{2h}+\cdots+z^{kh}\right)^{\sigma_1(h)}.
\]
For contrast, one-variable first-order logic **with counting quantifiers** distinguishes all nonisomorphic structures in \(\mathscr A\).

## Assumptions and scope
The domain is finite and may be empty. Both unary operations are bijections and commute. They are *function symbols*, not binary successor relations: hence expressions such as \(\sigma^a\tau^b(x)\) are terms involving only one variable, even for arbitrarily large fixed nonnegative integers \(a,b\). In the group-action notation, \((u,v)\in\mathbb Z^2\) sends \(x\) to \(\sigma^u\tau^v(x)\); inverse powers here describe permutations and need not be formal terms. Every orbit is finite, so each stabilizer is finite-index. Since \(\mathbb Z^2\) is abelian, all points in the same orbit have exactly the same stabilizer subgroup, not merely conjugate ones.

## Proof
**1. Orbit normal forms and one-variable type tests.** Every finite-index subgroup has a unique Hermite presentation \(H=\langle(a,0),(s,b)\rangle\), where \(a,b\geq1\) and \(0\leq s<a\), with index \(ab\). The \(ab\) pairs \((i,j)\) satisfying \(0\leq i<a\), \(0\leq j<b\) form a complete set \(T_H\) of coset representatives. A transitive finite \(\mathbb Z^2\)-set of type \(H\) is canonically \(\mathbb Z^2/H\).

There is an explicit **quantifier-free one-variable** formula \(\theta_H(x)\) characterizing points with stabilizer exactly \(H\): require \(\sigma^a(x)=x\), \(\sigma^s\tau^b(x)=x\), and require the \(ab\) terms \(\sigma^i\tau^j(x)\), with \((i,j)\in T_H\), to be pairwise distinct. The first two equalities imply \(H\subseteq\operatorname{Stab}(x)\), so the orbit has at most \(ab\) points; the inequalities make it have at least \(ab\). Thus equality of stabilizers follows. Conversely, exact stabilizer \(H\) satisfies all these requirements. For points \(x,y\) satisfying \(\theta_H\), belonging to the **same** orbit is equivalent to the quantifier-free formula \(\bigvee_{(i,j)\in T_H}y=\sigma^i\tau^j(x)\).

**2. Lower bound.** If the truncated multiplicities differ, choose a subgroup \(H\) for which the smaller multiplicity is \(r<k\), while the other multiplicity is at least \(r+1\). The sentence asserting the existence of \(r+1\) points of type \(H\) that are pairwise in different orbits uses exactly \(r+1\leq k\) variable symbols, by the explicit formulas of Step 1. It holds precisely when there are at least \(r+1\) such orbits. This proves distinguishability. If \(r=0\), this is just the one-variable existence sentence.

**3. Upper bound for arbitrary quantifier depth.** Assume all truncated multiplicities agree. In the ordinary \(k\)-pebble back-and-forth game, maintain a matching of the distinct orbits currently occupied by the pebbles. Each matched orbit has the same stabilizer subgroup, and all selected points within it have matching displacements relative to a chosen selected anchor. Thus all equalities between unary-function terms of selected points are preserved, not just the atomic equalities of the underlying points. When a pebble is lifted, at most \(k-1\) orbits remain occupied. If the next point lies in an already occupied orbit, use the unique matching displacement. If it lies in a new orbit of type \(H\), choose an unoccupied orbit of the same type in the other structure. Such an orbit exists: for multiplicity below \(k\), the two total multiplicities are equal, while for multiplicity at least \(k\), at most \(k-1\) orbits are occupied. An arbitrary orbit isomorphism matches the moved point. The invariant is restored regardless of the direction of the move. Hence Duplicator wins every finite number of rounds, proving \(\mathrm{FO}^k\)-equivalence.

**4. Exact minimum widths and sizes.** The lower-bound sentence at \(r+1\) variables and the upper bound through \(r\) variables prove the minimum width formula. The orbit multiplicities after truncation are the smallest componentwise integers in the equivalence class; the orbit types determine an action up to isomorphism. Therefore the minimum representative is unique up to isomorphism and has the displayed size.

**5. Enumerative formula.** The Hermite normal form with determinant \(h\) has \(ab=h\), and for each divisor \(a\mid h\) there are \(a\) allowed values of \(s\). Thus the number of orbit types of size \(h\) is \(\sigma_1(h)\). For each type, the minimum-representative multiplicity can be any integer from \(0\) through \(k\); its size contribution is a multiple of \(h\). Multiplying these independent finite choices in the ring of formal power series yields \(F_k(z)\). Each coefficient is finite, since only indices at most its degree contribute.

**6. Counting contrast.** For any \(H\), the formula \(\theta_H(x)\) holds at exactly \([\mathbb Z^2:H]m_X(H)\) elements. A one-variable counting quantifier distinguishes two different such cardinalities. Thus the family is identified up to isomorphism by one-variable logic with counting.

## Verification
Three fully standalone Python programs are included. `check_pebbles.py` constructs small commuting actions, computes the complete bounded-displacement atomic diagram of their selected variables, and independently refines all \(k\)-tuple logical types to a fixed point for \(k=1,2,3\). Across 348 comparisons, observed equivalence exactly matched subgroup-multiplicity truncation. `check_orbits.py` directly enumerates every commuting pair of permutations on sets of size one through six, classifies its orbits up to simultaneous conjugacy, and checks the \(\sigma_1(h)\) count and the independent Euler-product isomorphism counts; it also calculates the first thirteen coefficients of \(F_k\) for \(k=1,2,3\). `check_terms.py` independently evaluates the explicit one-variable stabilizer test for 87 Hermite types of index at most ten, with 54,114 cross-type point tests. These are finite checks, not an infinite proof; the proof is Steps 1–6 above. Run each script with ordinary Python 3 from its own directory; no external dependencies are needed.

## Relationship to prior work
The classical group-action description by stabilizer subgroups supplies the orbit normal form. Grohe and Otto's work develops finite-variable pebble equivalence and corresponding counting/noncounting distinctions; it does not state this exact commuting-action classification or its Euler product. Albert, Bouvel, and Féray analyze first-order logics of permutations as order-pairs or as the graph of a single bijection, using a **relational** signature; their theories and quantifier-depth arguments do not provide the function-symbol \(\mathrm{FO}^k\) orbit-spectrum theorem here. Kiefer, Schweitzer, and Selman classify finite relational structures identified by two-variable **counting** logic, not the exact plain \(\mathrm{FO}^k\) equivalence classes of two commuting unary functions. The distinction of signatures and quantifier resources is essential; this theorem is not asserted as a consequence of any one of those papers.

## Limitations
The finite-domain and commuting-bijection hypotheses are essential to the stated orbit and stabilizer descriptions. The result does not cover two **binary relational successor symbols**, arbitrary noninvertible unary maps, arbitrary noncommuting permutations, extra constants, or infinite actions. The canonical-size enumeration concerns the size of the **smallest** representative of an equivalence class, not the number of classes represented at a fixed size. No finite bound on distinguishing quantifier rank, shortest formula length, or asymptotic coefficient growth is claimed. Historical priority beyond the inspected literature remains a limitation; independent mathematical audit has not been performed.

## References
1. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, first public arXiv posting 2012-04-09, arXiv:1204.1990; CSL 2012, doi:10.4230/LIPIcs.CSL.2012.289.
2. M. Albert, M. Bouvel and V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459, first posted 2018-08-16; Journal of Combinatorial Theory Series A 171 (2020), 105158.
3. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first posted 2015-03-30.
