# Congruence-profile polynomial and generic simplicity for finite chain-product weak Heyting–Brouwer algebras

## Finding

Fix integers \(k\geq 2\) and \(n_1,\ldots,n_k\geq 1\). Let \(C_r\) mean the bounded chain with exactly \(r\) elements and put
\[
L_{\mathbf n}=\prod_{i=1}^{k}C_{n_i+1}.
\]
Count **distinct named operations** \((\to,\leftarrow)\) on this fixed lattice reduct that make it a weak Heyting–Brouwer (WHB) algebra, with no quotient by lattice automorphisms. Define the congruence-profile polynomial
\[
Q_{\mathbf n}(z)=\sum_{(\to,\leftarrow)}z^{c(\to,\leftarrow)},
\]
where the congruence lattice of each expansion is isomorphic to the Boolean lattice on \(c(\to,\leftarrow)\) points.

The following finite weighted endpoint formula determines the **entire** polynomial. For each ordered pair \((i,j)\), choose either \((u_{ij},v_{ij})=(0,0)\) of weight \(1\), or integers
\[
1\leq u_{ij}\leq n_i,\qquad 1\leq v_{ij}\leq n_j
\]
of weight
\[
w_{ij}(u_{ij},v_{ij})=\binom{u_{ij}+v_{ij}-2}{u_{ij}-1}.
\]
Set \(U_i=\max_j u_{ij}\), \(V_i=\max_j v_{ji}\), and
\[
I=\sum_{i=1}^{k}\max(0,n_i-U_i-V_i).
\]
In the disjoint union \(X=\bigsqcup_i X_i\) of chains \(X_i=\{x_{i,1}<\cdots<x_{i,n_i}\}\), let \(P_i(u)\) be the first \(u\) points of \(X_i\) and \(T_i(v)\) its last \(v\) points; both are empty at parameter zero. For each nonzero pair \((u_{ij},v_{ij})\), form the support set
\[
S_{ij}=P_i(u_{ij})\cup T_j(v_{ij}).
\]
Let \(H\) be the undirected graph whose vertices are these nonzero ordered pairs and whose distinct vertices \((i,j)\) and \((r,s)\) are adjacent exactly when \(S_{ij}\cap S_{rs}\ne\varnothing\). Write \(\kappa(H)\) for the number of connected components, with \(\kappa(\varnothing)=0\). Then
\[
\boxed{Q_{\mathbf n}(z)=\sum_{\mathbf u,\mathbf v}\left(\prod_{i,j}w_{ij}(u_{ij},v_{ij})\right)z^{I+\kappa(H)}.}
\]
The formula has precisely \(\prod_{i,j}(1+n_i n_j)\) endpoint configurations; for fixed \(k\) it computes every coefficient in polynomial time in \(\sum_i n_i\). The total number of expansions is
\[
\boxed{Q_{\mathbf n}(1)=\prod_{i,j}\binom{n_i+n_j}{n_i}.}
\]
In particular, the coefficient of \(z\) is the exact number of **simple** WHB expansions. The polynomial records all congruence-lattice ranks, not merely simplicity.

There is also a uniform asymptotic theorem. Choose a WHB expansion uniformly from all those on \(L_{\mathbf n}\) and set \(m=\min_i n_i\). Then
\[
\boxed{\Pr(\text{the expansion is simple})\geq 1-2k^2e^{-m/4}.}
\]
Hence, for fixed \(k\geq2\), a uniformly chosen expansion is simple with probability tending to \(1\) as all factor lengths tend to infinity; the same holds when \(k^2e^{-m/4}\to0\).

For two factors, illustrative exact profiles are
\[
Q_{(2,2)}(z)=1213z+70z^2+12z^3+z^4
\]
and
\[
Q_{(2,3)}(z)=11632z+309z^2+50z^3+8z^4+z^5.
\]
The underlying lattices here have respectively \(9\) and \(12\) elements. These are counts of named expansions, not isomorphism classes.

## Assumptions and scope

A WHB-algebra is a bounded distributive lattice with two binary operations satisfying the weak-Heyting, weak-difference, and two interaction axioms as in Celani–Nagy–Zuluaga Botero (2023), Definitions 2.1, 3.1, and 4.3. No reflexivity or transitivity of the additional relation is imposed. The known finite Priestley duality (their Theorem 5.7) identifies expansions on \(L_{\mathbf n}\) with relations \(R\subseteq X^2\) satisfying
\[
x'\leq x\ R\ y\leq y'\quad\Longrightarrow\quad x'R y'.
\]
The second dual relation is \(R^{-1}\). The congruence correspondence (their Theorem 5.10) identifies congruences with subsets closed under both \(R\) and \(R^{-1}\). Those two theorems are prior work, not new assertions here.

All chain factors, their positions, and the operations are named; if factor sizes coincide, swapping factors does not identify two expansions. The endpoint formula is an exact identity for every allowed \(k\) and factor-size vector. Its asymptotic bound is uniform in the vector.

## Proof

**1. Reduction to independent Ferrers blocks.** The Priestley dual of \(L_{\mathbf n}\) is the disjoint union of chains \(X_i\). Restrict \(R\) to the rectangular block \(X_i\times X_j\). The frame implication above forces rows to be final intervals of the target chain, nested by reverse inclusion as the source index increases. Conversely, any such choice of a Ferrers matrix independently in each block gives an admissible relation. Therefore the block matrices are independent choices, and the total number in a block of dimensions \(s\) by \(t\) is the number of nondecreasing row thresholds in \(\{1,\ldots,t+1\}\), namely \(\binom{s+t}{s}\). This proves the total count.

**2. Exact endpoint multiplicity.** A nonzero Ferrers block has precisely \(u\geq1\) nonempty initial source rows and \(v\geq1\) nonempty final target columns. After deleting all-zero rows and columns, every row and column is nonempty. Index its active target columns from left to right and write the first occupied column of each active row as \(t_1,\ldots,t_u\). The nested-row condition and column nonemptiness are exactly
\[
1=t_1\leq t_2\leq\cdots\leq t_u\leq v.
\]
There are \(\binom{u+v-2}{u-1}\) such sequences. The empty block has unique parameters \((0,0)\) and weight \(1\). Thus a complete choice of endpoint parameters has multiplicity equal to the displayed product of weights.

**3. Components from endpoint supports.** Regard \(R\) as an undirected graph after forgetting arrow orientations, including isolated vertices. Every nonzero block is connected on its active vertices: its least source point is joined to every active target point, and its greatest target point is joined to every active source point. Its vertex set is exactly \(S_{ij}\), even when \(i=j\) and the source and target portions overlap. The union of nonzero block graphs consequently has one component per component of their support-intersection graph \(H\). The remaining isolated vertices in \(X_i\) are precisely those lying strictly between the union of the outgoing active prefixes (length \(U_i\)) and the union of incoming active suffixes (length \(V_i\)); their number is \(\max(0,n_i-U_i-V_i)\). Thus the number of undirected \(R\)-components is exactly \(I+\kappa(H)\).

**4. Congruences and weighted polynomial.** Since the second dual relation is \(R^{-1}\), a subset of \(X\) is closed under both relations exactly when it is a union of the undirected \(R\)-components. The cited congruence correspondence therefore gives a Boolean congruence lattice with precisely \(I+\kappa(H)\) atoms. Summing the multiplicities from Step 2 according to that number proves the polynomial. A nontrivial algebra is simple exactly when its congruence lattice has two elements, equivalently when the component number is \(1\).

**5. Uniform generic simplicity.** In a uniformly random block of size \(s\) by \(t\), the probability that its active source prefix has length at most \(\lfloor s/2\rfloor\) is the ratio of the number of Ferrers matrices with at least \(r=\lceil s/2\rceil\) trailing zero rows to all matrices. By direct counting and \(1-x\leq e^{-x}\),
\[
\frac{\binom{s-r+t}{s-r}}{\binom{s+t}{s}}
=\prod_{h=0}^{r-1}\frac{s-h}{s+t-h}
\leq \exp\!\left(-\frac{rt}{s+t}\right)
\leq e^{-\min(s,t)/4}.
\]
The analogous bound holds for an active target suffix of length at most \(\lfloor t/2\rfloor\), by transposing and reversing the block. A union bound over the two endpoint events in each of the \(k^2\) blocks shows that, outside an event of probability at most \(2k^2e^{-m/4}\), every block has an active source prefix longer than half of its source chain and an active target suffix longer than half its target chain.

On this event no chain point is isolated, because an outgoing prefix and an incoming suffix each longer than half the same chain cover it. Every block is nonempty. The support-intersection graph \(H\) is connected: blocks with the same source intersect at that chain's first point, and blocks with the same target intersect at that chain's last point; any two ordered-pair blocks are linked by a path through their common-source/common-target intermediate block. Therefore \(I=0\) and \(\kappa(H)=1\), proving the probability inequality and limits.

## Verification

Run `python verify_congruence.py` with Python 3 and no external dependencies. The checker evaluates the endpoint formula and independently enumerates actual monotone Ferrers matrices for sizes \((1,1)\), \((1,2)\), \((2,2)\), \((2,3)\), and \((3,3)\). It also brute-forces **all** binary relations on the dual posets of sizes \((1,1)\), \((1,2)\), \((2,2)\), filtering directly by the frame axioms. Finally, it checks all WHB algebra equations over the induced upset lattices for \((1,1)\) and \((1,2)\). These tests returned `VERIFY_OK` and the displayed polynomial coefficients. The proof of the all-size formula and asymptotic probability bound is deductive; finite computations alone cannot certify these infinite statements.

## Relationship to prior work

Celani, Nagy, and Zuluaga Botero introduced WHB-algebras and proved relational Priestley duality and the doubly closed-set congruence representation (Theorems 5.7 and 5.10) in their 2023 preprint. The reduction from congruences to undirected relation components is an immediate finite consequence and is **not** asserted to be independently new. The result here is the all-factor-size **weighted endpoint-support formula** for the full congruence-rank distribution on products of chains, its exact simple-algebra counts, and a uniform asymptotic simplicity bound. The binomial count of an individual Ferrers block is classical; it is likewise not claimed as novel. Related literature on bounded distributive lattices with strict implication provides background but does not, in the material inspected, state this joint congruence-profile enumeration and uniform random-expansion theorem.

## Limitations

The polynomial enumerates named expansions of a fixed lattice reduct, **not** isomorphism types. The algebraic congruence characterization and dual equivalence are cited inputs, not proved from axioms here. For variable \(k\), the endpoint sum can be large; the polynomial-time assertion holds only for fixed \(k\). The probability bound is a sufficient-event bound, not a sharp asymptotic expansion. Equivalent results under Ferrers matrix, tense algebra, or distributive-lattice terminology cannot be ruled out absolutely by literature searches. There has been no independent external audit.

## References

1. S. Celani, A. Nagy, and W. Zuluaga Botero, *Bounded distributive lattices with strict implication and weak difference*, arXiv:2312.10873 (first public version 2023-12-18), especially Sections 2–5, Theorems 5.7 and 5.10. https://arxiv.org/abs/2312.10873
2. R. Jansana and S. A. Celani, *Bounded distributive lattices with strict implication*, Mathematical Logic Quarterly 51 (2005), DOI:10.1002/malq.200410022. Cited for predecessor duality; only bibliographic-level material was available for the present comparison.
