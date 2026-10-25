# Eleven rank-three theories of uniform-matroid flat lattices

## Finding

Let \(1\le r\le n\) be integers and let \(\mathcal L_{n,r}\) be the lattice of flats of the uniform matroid \(U_{r,n}\), in the **one-relation** language \(\{\subseteq\}\) with equality. Then, for all allowed parameter pairs,

\[
\mathcal L_{n,r}\equiv_3\mathcal L_{m,s}
\quad\Longleftrightarrow\quad
\min(r,6)=\min(s,6)\ \text{and}\quad
\bigl(r=1\ \text{or}\ [(n=r)\Longleftrightarrow(m=s)]\bigr).
\]

Thus there are exactly eleven rank-three first-order sentence theories: a single rank-one class, and, for each effective rank \(2,3,4,5,6\), one Boolean class and one genuinely truncated class. Every class has a representative with at most \(121\) elements. This is sharp within this family; the largest minimum representative is \(\mathcal L_{7,6}\), with \(121\) flats. The distinction between \(n=r\) and \(n>r\) remains visible at rank three even after rank stabilization.

## Assumptions and scope

All sets are finite, \(n,r\) are positive integers satisfying \(r\le n\), and the language contains no named ground-set points, lattice operators, rank predicate, or distinguished endpoints. The domain of \(\mathcal L_{n,r}\) is precisely

\[
\{A\subseteq[n]: |A|<r\}\ \cup\ \{[n]\},
\]

ordered by inclusion. Here \(\equiv_3\) means agreement on *every* first-order sentence of quantifier rank at most three, with unbounded formula length and unrestricted reuse of variable names. The rank-one lattice is the two-element chain for every \(n\). When \(n=r\) the domain is the full Boolean inclusion poset.

## Proof

**Logical-type recurrence.** For elements \(X,Y\), encode their atomic ordered relation by \(0\) for equality, \(1\) for \(X\subsetneq Y\), \(2\) for \(Y\subsetneq X\), and \(3\) for incomparability. At a selected pair \((A,B)\), its rank-one extension type consists of its atomic relation \(\rho(A,B)\) together with the sixteen-bit mask

\[
M(A,B)=\bigvee_{C\in\mathcal L_{n,r}} 2^{4\rho(C,A)+\rho(C,B)}.
\]

Here the large disjunction is bitwise OR. The rank-two pointed type of \(A\) is the *set* of all pairs \((\rho(A,B),M(A,B))\) obtained as \(B\) ranges over the lattice. Finally the rank-three sentence type is the set of pointed types of all \(A\). This is the exact Hintikka/Ehrenfeucht–Fraïssé recurrence, with both existential and universal conditions represented by the complete extension sets; no finite bound on formula length is assumed.

**Exact four-cell reduction.** For proper flats \(A,B\) set

\[
u=|A\cap B|,\quad v=|A\setminus B|,\quad w=|B\setminus A|,\quad z=n-u-v-w.
\]

Their feasible parameters satisfy \(u,v,w,z\ge0\), \(u+v=|A|<r\), \(u+w=|B|<r\), and \(u+v+w+z=n\). A third proper flat \(C\) is specified, for purposes of its comparisons with \(A,B\), by integer counts \((x_{11},x_{10},x_{01},x_{00})\) satisfying

\[
0\le(x_{11},x_{10},x_{01},x_{00})\le(u,v,w,z),
\qquad x_{11}+x_{10}+x_{01}+x_{00}<r.
\]

All vector inequalities are coordinatewise. The comparison conditions are **exactly**

\[
\begin{aligned}
C\subseteq A&\iff x_{01}=x_{00}=0,\\
A\subseteq C&\iff x_{11}=u,\ x_{10}=v,\\
C\subseteq B&\iff x_{10}=x_{00}=0,\\
B\subseteq C&\iff x_{11}=u,\ x_{01}=w.
\end{aligned}
\]

The separate choice \(C=[n]\) contributes \(2^{4\alpha+\beta}\), where \(\alpha=0\) if \(A=[n]\) and \(2\) otherwise, and analogously for \(\beta\). For a proper \(C\), each count \(x_i\) can be replaced by its minimum in one of three status classes: zero, full cell, or strictly between them (minimum one, available only when the cell has at least two elements). This preserves the four comparisons and cannot destroy \(\sum_i x_i<r\). Conversely each available status minimum realizes that status. Consequently evaluating at most \(3^4\) status quadruples computes every mask **exactly**, for arbitrary parameters, not merely sampled ground sets.

**Uniform one-point profile lemma.** Let \(T_{n,r}(a)\) denote the complete rank-two pointed type of any proper flat of size \(a\), and let \(T_{n,r}(\top)\) denote that of the top element. Eliminate \(B\) using \(0\le u\le a\), \(0\le w\le n-a\), and \(u+w<r\) in the preceding exact mask expression. The result is the following seven-row table, where \(\mathsf B\) means \(n=r\), \(\mathsf T\) means \(n>r\), and a row entry is the set of \((\rho,\mathrm{mask}_{16})\) labels. The expanded hexadecimal labels in `PROFILES.json` form part of this displayed finite case table.

| Size of the selected flat | \(\mathsf B\): number of pair types | \(\mathsf T\): number of pair types | Row identification |
|---|---:|---:|---|
| \(a=0\) | 4 | 4 | same |
| \(a=1\) | 8 | 8 | different mask for an incomparable pair |
| \(a=2\) | 9 | 9 | same |
| \(3\le a\le r-3\) | 10 | 10 | same |
| \(a=r-2\) | 9 | 9 | same |
| \(a=r-1\) | 8 | 8 | different masks for incomparable pairs |
| \(A=\top\) | 4 | 4 | same |

The table is asserted for \(r\ge6\). The second elimination is a finite **integer-interval** calculation, not an observed numerical stabilization: each label asks only for zero/full/interior witnesses in the four cells, strict extension of either selected set, and at most two additional chosen points to violate both subset relations. The necessary proper-flat cardinality bounds are comparisons of \(r\) with \(0,|A|,|B|,|A\cup B|\), possibly plus one or two. Substituting \(|A|=a\), \(|B|=u+w\), \(|A\cup B|=a+w\), with the displayed exact bounds on \(u,w\), the feasible label sets have breakpoints precisely at \(a=0,1,2\) and \(r-a=1,2,3\); extra ground-set points affect only whether \(n-r=0\) or \(n-r\ge1\). For example, in the middle range, the label set is

`0:8421, 1:2322, 1:ad22, 1:af22, 2:4454, 2:c4b4, 2:c4f4, 3:bca8, 3:dca8, 3:fca8`.

The same status criterion gives the other six rows, displayed in full in the embedded table for both regimes. For \(1\le r\le5\), direct substitution into those integer bounds gives exactly the rank-dependent row sets in the canonical pairs \((n,r)=(r,r)\) and \((r+1,r)\), with all \(n>r\) sharing the latter. These deductions are universal identities of integer inequalities; the executable orbit checker is additional reproducibility evidence, not the justification for extending a sampled range to infinity.

**Classification and separation.** If \(r\ge6\), every required row of the table occurs and no other pointed type occurs; hence all Boolean members agree with \(\mathcal L_{6,6}\), and all truncated members agree with \(\mathcal L_{7,6}\). At ranks below six the middle row first becomes available at rank six, and the list of obtainable row labels separates ranks one through five. The Boolean and truncated classes at each rank at least two differ because their atom and coatom pointed types contain different masks. Exact complete-type comparison gives eleven distinct row sets (canonical labels in `verify_types.py` and `PROFILES.json`). Differences produce **actual rank-three separating sentences**: for any rank-one pair-type label \(p\), let \(\theta_p(x,y)\) conjoin the atomic relation with the sixteen existential or negated-existential three-variable atomic diagrams specified by its mask. Then \(\theta_p\) has rank one. A Boolean combination of \(\exists y\,\theta_p(x,y)\) and its negation isolates any complete rank-two pointed type; existentially quantifying \(x\) yields a rank-three separator whenever a pointed type appears in only one structure.

**Sharpness.** The eleven least representatives are \(\mathcal L_{1,1}\) and, for \(r=2,3,4,5,6\), the pairs \(\mathcal L_{r,r}\) and \(\mathcal L_{r+1,r}\). Their sizes are \(1+\sum_{j=0}^{r-1}\binom{n}{j}\), increasing with either parameter. The largest is \(1+\sum_{j=0}^{5}\binom{7}{j}=121\); no other member of its theory has fewer elements, by the classification.

## Verification

Run `python3 verify_types.py` for the exact four-cell recurrence, all eleven representative signatures, every positive pair \(1\le r\le n\le25\), and the complete seven-row mask table. The output is `verify_types_output.txt`. Independently compile and run `verify_direct.cpp` (for example with `g++ -O2 -std=c++17`) to enumerate all actual subsets and all third-flat choices directly for the twelve smallest Boolean-and-truncated comparison models. Its output is `verify_direct_output.txt`; the two methods produce identical complete signature sets. The direct checker does not reuse the Venn-cell status algorithm. Finite checks corroborate the algebraic interval argument and are not used as an unproved infinite-exhaustion step.

## Relationship to prior work

Uniform-matroid flats are standard geometric lattices. The truncated Boolean lattice is studied in Bajnok and Shahriari (2015), which treats cutsets and width/profile extremals, not first-order quantifier-rank equivalence. Faigle's classic discussion of matroid lattices develops structural properties of flats; its available publisher summary does not state this bounded-rank classification. The full Boolean case \(n=r\) is a naturally related, previously considered family, but its classification alone does not imply the distinct truncated class at each rank. The present claim is specifically the full two-parameter classification and optimal representative size, not the standard flat description or the Boolean special case.

## Limitations

The statement is only about uniform matroids of positive rank and the pure inclusion relation at quantifier rank three. It does not imply equivalence in the language with a named ground set, rank, joins/meets as function symbols, or at higher quantifier ranks. Symbolic endpoint elimination is the critical nonstandard step, and its precise case table is supplied for checking; executable parameter sweeps by themselves are not proofs for all integers. The literature search is not exhaustive against inaccessible or unindexed sources, and independent mathematical validation has not been conducted.

## References

1. Béla Bajnok and Shahriar Shahriari, *On Uniform f-vectors of Cutsets in the Truncated Boolean Lattice*, arXiv:1512.02973v1, publicly posted 2015-12-09, https://arxiv.org/abs/1512.02973.
2. Ulrich Faigle, *Lattices*, in *Theory of Matroids*, edited by Neil White, Cambridge University Press (1986), Chapter 3, https://doi.org/10.1017/CBO9780511629563.006. Only the publisher synopsis was accessible for this comparison.
3. Standard first-order Hintikka-type / Ehrenfeucht–Fraïssé characterization of bounded quantifier rank, e.g. the finite-model-theory lecture notes https://www.math.utoronto.ca/rossman/EFgames-lecture.pdf.
