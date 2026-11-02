# Sharp two-variable quantifier-rank threshold for singly marked directed cycles

## Finding
For each integer \(n\ge3\), define \(C_n^{\bullet}\) on the vertices \(\{0,1,\dots,n-1\}\), with \(S(x,y)\) precisely when \(y\equiv x+1\pmod n\) and the unary predicate \(R(x)\) precisely when \(x=0\). The signature has only \(S,R\) and equality: in particular it contains no global order, constants, function symbols, or counting quantifiers.

For every integer \(q\ge1\),
\[
 C_m^{\bullet}\equiv_q^{\mathrm{FO}^2}C_n^{\bullet}
 \quad\Longleftrightarrow\quad
 (m=n\le2q)\ \text{or}\ (m,n\ge2q+1).
\]
The notation means that all first-order sentences of quantifier rank at most \(q\), using just the two reusable variables \(x,y\), agree. Consequently there are exactly \(2q-1\) different rank-\(q\) theories. Every theory has a representative of size at most \(2q+1\), and this bound is sharp. For every \(3\le m<n\), the least distinguishing rank is exactly \(\lceil m/2\rceil\). At rank zero every structure agrees with every other one.

## Assumptions and scope
All structures are finite singly marked directed simple cycles, with \(n\ge3\). There is exactly one marked vertex. The unique-successor relation is binary and relational rather than a function symbol: allowing nested successor terms would change the result. The family is considered up to isomorphism, so choosing the marked vertex as zero is harmless.

## Proof
**1. Exact two-variable type reduction.** For a finite structure in the displayed signature, let \(U_r(v)\) denote the complete rank-at-most-\(r\) one-free-variable \(\mathrm{FO}^2\) type of \(v\). Its rank-zero datum is whether \(R(v)\) holds. Given \(v,w\), let \(A(v,w)\) record the equality, \(S(v,w)\), and \(S(w,v)\) truth values. Since a quantifier binding either one of the only two variable names leaves a formula with at most one free variable, the complete rank-\(r\) two-variable type of \((v,w)\) is determined by \(A(v,w),U_r(v),U_r(w)\). Conversely each of those data is observable by a formula of rank at most \(r\).

It follows that the following recurrence is *exact*, not merely a sufficient invariant:
\[
 U_{r+1}(v)\ \longleftrightarrow\
 \left(U_r(v),\ \left\{\bigl(A(v,w),U_r(w)\bigr):w\in C_n^{\bullet}\right\}\right).
\]
The set records existence, not multiplicity. For the converse direction, each color has a rank-at-most-\(r\) characteristic formula (only finitely many colors occur at fixed rank in a finite relational signature), so every indicated color/atomic-relation support is expressed by an existential formula of rank at most \(r+1\). A closed formula of rank at most \(q\ge1\) can quantify one of the two variables and then test a rank-at-most-\(q-1\) unary formula. Therefore two such structures agree on all rank-\(q\) sentences *exactly when* their sets of \(U_{q-1}\)-colors agree.

**2. Uniform palette lemma.** For every \(r\ge0\) and every \(n\ge2r+3\), the rank-\(r\) unary colors have exactly \(2r+2\) classes: the red vertex, each of the \(r\) first successors and each of the \(r\) first predecessors of red (each with its own class), and all remaining vertices in one far class. These classes and their complete color data do not depend on \(n\) in this range, except through the number of vertices in the far class.

For \(r=0\), this is simply the red/nonred partition. Assume it for \(r\). The far vertices form one consecutive block of length \(L=n-2r-1\). If \(n\ge2r+5\), then \(L\ge4\). Each far vertex has a nonadjacent, distinct vertex of the same far color. The support recurrence separates the two endpoints of this block, because each is adjacent to a different one of the two distinct near-boundary colors, from the remaining far vertices, and separates the endpoints from each other. All far-block interior vertices have the same support data: they have two far neighbors and at least one far nonneighbor. The old near colors remain distinct, with stable supports to all old colors, because the far block has length at least four and each old near color occupies a fixed position. This proves the asserted palette and cross-length stability for \(r+1\), with new threshold \(n\ge2(r+1)+3\).

**3. Sharpness and absence of hidden identifications.** Let \(\mathcal P_r(n)\) be the set of rank-\(r\) unary colors present in \(C_n^{\bullet}\). We inductively prove that these sets distinguish every length \(n=3,\dots,2r+2\), while all lengths \(n\ge2r+3\) have one common palette. The base \(r=0\) is immediate: all \(n\ge3\) share the red/nonred palette.

For the induction step, any previously distinguished short lengths remain distinguished because \(U_{r+1}\) retains \(U_r\). The only new lengths to separate are \(2r+3\) and \(2r+4\) from the stable range \(n\ge2r+5\). The old far block has respectively \(L=2\), \(L=3\), and \(L\ge4\) vertices. Examine the rank-\(r+1\) test, for a vertex in the old far class, that there exists a distinct *nonadjacent* vertex of that same old far class. When \(L=2\) the test is false at both far vertices, when \(L=3\) it is true at both endpoints but false at the middle, and when \(L\ge4\) it is true at every far vertex. Thus the new palettes contain, respectively, only the false, both true and false, or only the true *extensions of the old far color*. These three support sets are different, and each is distinguishable from earlier short lengths because forgetting one rank recovers the old palette. This completes the induction.

**4. Finish.** A rank-\(q\) sentence sees exactly the palette \(\mathcal P_{q-1}(n)\), by step 1. Step 3 shows that lengths \(3\le n\le2q\) are pairwise distinct, and all lengths \(n\ge2q+1\) agree. There are \((2q-2)+1=2q-1\) types, the stable class first appears at length \(2q+1\), and for \(m<n\) the first separating rank is the smallest \(q\) with \(m\le2q\), namely \(\lceil m/2\rceil\).

## Verification
The standalone standard-library program `verify_marked_cycles.py` implements two independent procedures: (i) the exact unary support refinement in step 1 and (ii) full logical-type recursion on assignments of zero, one, or two variables. For all lengths \(3\le n\le24\) and ranks \(1\le q\le8\), both procedures reproduce the theorem's predicted equality classes, comprising 3,872 ordered parameter-pair/rank comparisons in each method. Run `python3 verify_marked_cycles.py`; the expected output is embedded in `verification_output.txt`. This finite check corroborates the exact recurrences but the induction above proves the unbounded statement.

## Relationship to prior work
Weis and Immerman (2007, 2009) prove structure theorems for two-variable logic on *linear words with an available order relation*, including successor. Their results provide background but are not the claimed exact threshold in *cyclic successor-only* structures with one unary marker. Kufleitner and Lauser (2012) study alternation hierarchies over ordered words, not these pointed cycles. Related exact rank-depth results for directed paths and one-marked linear orders address different signatures and families; the present cutoff is linear in quantifier rank, and the proof does not assume either of those statements. No claim of exhaustive historical priority is made.

## Limitations
The theorem is restricted to singly marked directed cycles with at least three vertices, in the *binary relational* successor language and ordinary two-variable first-order logic. It does not cover named global order, two or more marked vertices, unmarked disjoint unions of cycles, function-symbol terms, counting quantifiers, or three-variable logic. No independent mathematical audit has been carried out.

## References
1. P. Weis and N. Immerman, *Structure Theorem and Strict Alternation Hierarchy for FO2 on Words*, Electronic Colloquium on Computational Complexity report TR07-008, public 18 January 2007, https://eccc.weizmann.ac.il/report/2007/008/ ; extended text https://arxiv.org/abs/0907.0616 (2009).
2. M. Kufleitner and A. Lauser, *Quantifier Alternation in Two-Variable First-Order Logic with Successor Is Decidable*, 2012, https://arxiv.org/abs/1212.6500.
