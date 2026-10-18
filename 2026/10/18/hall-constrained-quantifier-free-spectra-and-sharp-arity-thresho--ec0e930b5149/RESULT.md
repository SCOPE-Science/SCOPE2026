# Hall-constrained quantifier-free spectra and sharp arity thresholds for finite idempotent unary algebras

## Finding

Fix a finite nonempty structure \(A=(A,f)\) in the language of one unary function, subject to \(f^2=f\). The \(r\geq1\) fixed points have, in nonincreasing order, \(c_1\geq\cdots\geq c_r\geq0\) nonfixed preimages each; put \(n=r+\sum_i c_i\), and \(C=c_1\). Let \(T_k(A)\) be the number of distinct complete parameter-free quantifier-free atomic diagrams realized by ordered \(k\)-tuples of \(A\), including \(T_0=1\). Define

\[
B_0(y)=y,\qquad B_b(y)=\frac{y^b(1+y)}{b!}\quad(b\geq1).
\]

For each vector of nonnegative integers \(\nu=(\nu_0,\ldots,\nu_C)\), let \(t=\sum_b\nu_b\). Write its list of demands, with \(b\) repeated \(\nu_b\) times, in nonincreasing order \(d_1\geq\cdots\geq d_t\). Call \(\nu\) feasible when \(t\leq r\) and \(d_j\leq c_j\) for all \(1\leq j\leq t\). Then the finite polynomial

\[
P_{\mathbf c}(y)=\sum_{\nu\text{ feasible}}
\prod_{b=0}^{C}\frac{B_b(y)^{\nu_b}}{\nu_b!}
=\sum_{d=0}^{n}a_dy^d
\]

determines the complete quantifier-free type spectrum:

\[
\boxed{\sum_{k\geq0}T_k(A)\frac{x^k}{k!}=P_{\mathbf c}(e^x-1),\qquad
T_k(A)=\sum_{d=0}^{n}a_d d!\left\{\begin{matrix}k\\d\end{matrix}\right\}.}
\]

Consequently the Boolean algebra of parameter-free quantifier-free definable relations on \(A^k\) contains exactly \(2^{T_k(A)}\) members.

There is also a *sharp arity separation theorem*. For two structures with the same number \(r\) of fixed points and nonincreasing capacity vectors \(\mathbf c\leq\mathbf e\) coordinatewise, with \(\mathbf c\neq\mathbf e\), put

\[
\boxed{k_*=\min_{1\leq j\leq r\,:\,e_j>c_j}j(c_j+1).}
\]

Their realized quantifier-free \(k\)-types coincide as sets for every \(k<k_*\); at each \(k\geq k_*\) the second realizes strictly more types. In particular, the least arity distinguishing the structures by an existential quantifier-free atomic diagram is exactly \(k_*\).

## Assumptions and scope

The carrier is finite and nonempty. The only operation is \(f\), with \(f(f(a))=f(a)\) for every \(a\). Each root is its own preimage, and its capacity counts only *nonfixed* elements mapping to it. The arity theorem compares sorted capacity vectors of equal length under coordinatewise inclusion, but does not assume a particular embedding of carriers. The Stirling number \(\left\{\begin{smallmatrix}k\\d\end{smallmatrix}\right\}\) counts partitions of a \(k\)-element labelled set into \(d\) nonempty blocks, with the usual empty-set conventions.

## Proof

Every term in one variable is equal, under \(f^2=f\), either to that variable or its image under \(f\). Hence a complete quantifier-free atomic diagram for a tuple \((u_1,\ldots,u_k)\) is exactly the equality partition of its \(2k\) labelled terms \((u_1,\ldots,u_k,f(u_1),\ldots,f(u_k))\). All such partitions that occur are individually definable using the finite conjunction of equalities and inequalities asserting the partition.

Partition the distinct tuple-values into *root groups* according to their common image under \(f\). In a group, let \(b\) be the number of distinct nonfixed values and let \(\epsilon\in\{0,1\}\) record whether the fixed root itself occurs as a coordinate. Thus each group consumes \(b+\epsilon\) distinct values, with \(b+\epsilon\geq1\). If \(b=0\), \(\epsilon=1\), giving the labelled-block weight \(B_0(y)=y\). For \(b\geq1\) there are \(b\) unordered leaf blocks and an optional root block, giving \(B_b(y)=y^b(1+y)/b!\). The indeterminate \(y\) marks the number of distinct coordinate-values. There are \(\nu_b\) unordered root groups of each demand \(b\), which contributes an additional divisor \(\nu_b!\).

A family of root groups is realizable if and only if it can be injected into the \(r\) distinct fixed-point fibers with each group's demand not exceeding the assigned fiber capacity. Sorting both lists decreasingly makes this matching condition equivalent to \(t\leq r\) and \(d_j\leq c_j\) for every \(j\leq t\): necessity follows from counting the first \(j\) groups above each capacity threshold; sufficiency is immediate by assigning group \(j\) to fiber \(j\). Thus the displayed polynomial is precisely the exponential generating polynomial for feasible *injective-coordinate* atomic diagrams (nonempty distinct value blocks). A diagram having \(d\) distinct values can be inflated to a \(k\)-tuple by a surjection of its labelled coordinates onto these \(d\) blocks. Its coefficient is therefore multiplied by \(d!\left\{\begin{smallmatrix}k\\d\end{smallmatrix}\right\}\), and the exponential substitution \(y=e^x-1\) proves both generating formulas.

Different equality partitions are logically inequivalent, and every union of finitely many atomic-diagram classes is definable by a disjunction; therefore the number of definable \(k\)-ary relations is \(2^{T_k(A)}\).

For the sharp threshold, a diagram realizable under \(\mathbf e\) but not \(\mathbf c\) must have sorted leaf demands \(d_j>c_j\) for some \(j\) with \(e_j>c_j\). The first \(j\) root groups then contain at least \(j(c_j+1)\) *distinct nonfixed coordinate values*, so no tuple of arity less than \(k_*\) can witness a difference. Conversely, choose an index \(j\) attaining the minimum and a diagram with exactly \(j\) distinct root groups, each containing exactly \(c_j+1\) distinct nonfixed-coordinate blocks, with no root coordinates. This diagram is feasible under \(\mathbf e\), since \(e_i\geq e_j\geq c_j+1\) for \(i\leq j\), but infeasible under \(\mathbf c\). Its arity is \(j(c_j+1)=k_*\). Repeating a coordinate extends it to every larger arity while preserving the obstruction, proving the sharp assertion.

## Verification

The companion Python program `verify_qf_types.py` uses exact rational arithmetic to compute \(P_{\mathbf c}\) and independently enumerates all \(k\)-tuples and their canonical equality partitions. It agrees on 197 capacity/arity instances (21,570 enumerated ordered tuple assignments), including unequal fibers. A second exact-arithmetic check compares spectra for 2,249 coordinatewise comparable pairs of capacity vectors and verifies the stated first separating arity. The program prints `VERIFY_OK` and `SHARP_THRESHOLD_OK` on success. These bounded checks are reproducibility evidence, not the proof for arbitrary finite algebras.

For example, the vectors \((2,1,0)\) and \((3,1,0)\) agree through arity two but differ at arity three: their profiles \((T_0,\ldots,T_5)\) are respectively \((1,2,9,51,321,2097)\) and \((1,2,9,52,339,2332)\). The sharper example \((3,1)\leq(3,2)\) is first distinguished at arity four.

## Relationship to prior work

Campercholi--Tellechea--Ventura (2023) prove a general semantic criterion and decision algorithms for quantifier-free definability in finite structures, in terms of subisomorphisms between generated substructures. Their decision theorem motivates the finite equality-diagram problem but does not state the present Hall-constrained all-arity enumerator or exact separation threshold. Areces--Campercholi--Penazzi--Ventura (2019) study complexity of open-formula definability rather than these fiber-capacity profiles. Quinn-Gregson (2026) classifies model-theoretic homogeneity phenomena in monounary structures, not the finite structure-specific distribution of realized quantifier-free diagrams claimed here. Finite Stirling transforms and labelled-set partition techniques are classical; only their precise combination with capacity feasibility and sharp separating arity is assessed as an additional result here.

## Limitations

The argument concerns quantifier-free formulas without parameters over *finite idempotent unary* structures. It does not count definability with parameters or quantifiers and does not assert the same formulas for general unary maps, non-idempotent maps, or infinite structures. The separation threshold assumes the same fixed-point count and coordinatewise nested sorted capacities. Older specialized enumeration results under different terminology might already contain an equivalent statement; no claim of exhaustive publication priority or independent external validation is made.

## References

1. M. Campercholi, M. Tellechea, P. Ventura, *Two algorithms to decide Quantifier-free Definability in Finite Algebraic Structures*, arXiv:2303.17017, first posted 2023-03-29, https://arxiv.org/abs/2303.17017.
2. C. Areces, M. Campercholi, D. Penazzi, P. Ventura, *The Complexity of Definability by Open First-Order Formulas*, arXiv:1904.04637, first posted 2019-04-09, https://arxiv.org/abs/1904.04637.
3. T. Quinn-Gregson, *Ultrahomogeneity and omega-categoricity of monounary algebras*, arXiv:2603.26616, first posted 2026-03-27, https://arxiv.org/abs/2603.26616.
