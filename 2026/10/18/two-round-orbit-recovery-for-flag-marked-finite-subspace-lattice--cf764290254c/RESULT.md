# Two-round orbit recovery for flag-marked finite subspace lattices

## Finding

Let \(q\) be any prime power, \(V=\mathbb F_q^n\) with \(n\geq1\), and fix a strictly increasing flag
\[
0=U_0\subsetneq U_1\subsetneq\cdots\subsetneq U_s=V.
\]
Consider the finite structure whose elements are **all** linear subspaces of \(V\), whose sole binary relation is strict containment \(X<Y\) meaning \(X\subsetneq Y\), and in which each proper nonzero flag member \(U_1,\ldots,U_{s-1}\) carries its own distinct unary mark. Every other subspace initially has one common colour. At each refinement round a subspace retains its previous colour and separately counts the colours of its strict subspaces and strict superspaces.

**Theorem.** After at most **two** refinement rounds, two subspaces \(W,W'\) have the same colour exactly when
\[
\dim(W\cap U_i)=\dim(W'\cap U_i)\qquad(0\le i\le s).
\]
This is exactly the orbit partition of the automorphism group of the marked strict-inclusion structure. In particular, the stable partition is attained by round two. Equivalently, the pointed one-variable types are separated by formulas of two-variable first-order logic with counting, \(C^2\), of quantifier rank at most two.

Put \(d_i=\dim U_i-\dim U_{i-1}\). The stable colour classes are indexed by every vector \(\mathbf a=(a_1,\ldots,a_s)\) with \(0\le a_i\le d_i\), and there are exactly
\[
\boxed{\prod_{i=1}^{s}(d_i+1)}
\]
such classes, **independently of the field size**. The class indexed by \(\mathbf a\) has cardinality
\[
\boxed{q^{\sum_{1\le i<j\le s}a_j(d_i-a_i)}
\prod_{i=1}^{s}\begin{bmatrix}d_i\\a_i\end{bmatrix}_q},
\]
where the bracket is the Gaussian binomial coefficient. The universal two-round bound is sharp: a single marked two-dimensional subspace of \(\mathbb F_2^4\) does not yield its orbit partition in one round.

## Assumptions and scope

The field is a finite field of order \(q\), not an arbitrary ring. The language contains **strict** containment between all subspaces, not just covers or the point-line incidence relation; both incoming and outgoing relation-colour counts are used. The flag is nested and may have only its trivial endpoints, in which case no individual marks are supplied. The assertions concern the orbit partition of one structure; they **do not** assert identification of the entire marked lattice among all arbitrary finite relational structures.

Define \(e_i(W)=\dim(W\cap U_i)\), with \(e_0(W)=0\), and \(a_i(W)=e_i(W)-e_{i-1}(W)\). Thus \(a_i(W)\in\{0,\ldots,d_i\}\) and \(\dim W=\sum_i a_i(W)\). Every admissible \(\mathbf a\) is realized by taking coordinate subspaces relative to a basis adapted to the flag.

The Gaussian coefficient is
\[
\begin{bmatrix}d\\a\end{bmatrix}_q=\prod_{j=0}^{a-1}\frac{q^{d-j}-1}{q^{a-j}-1},\qquad0\le a\le d,
\]
with an empty product equal to one.

## Proof

**1. Rank appears at round one.** For any subspace \(W\) of dimension \(r\), the number of its strict subspaces is
\[
L_q(r)=\sum_{j=0}^{r-1}\begin{bmatrix}r\\j\end{bmatrix}_q.
\]
For fixed \(q\), this number is strictly increasing with \(r\): an \(r\)-space sits inside an \((r+1)\)-space, and the latter has, among its proper subspaces, every subspace of the former *and* the former itself. Hence its count is strictly greater. The first refinement counts all predecessors, so distinguishes every dimension, in particular all atoms (one-dimensional subspaces).

**2. Membership of atoms in the flag appears at round one.** For an atom \(A\) and a proper marked flag member \(U_i\), if \(A\ne U_i\), the predicate \(A\subsetneq U_i\) is detected by counting the uniquely marked subspace among strict successors of \(A\). If \(A=U_i\), the initial individual mark itself identifies it. Therefore, at round one the colour of every atom determines, for each \(i\), whether \(A\subseteq U_i\). Membership in \(U_0=0\) and \(U_s=V\) is automatic.

**3. Intersection dimensions appear at round two.** Let \(W\) have dimension at least two. Its strict predecessors include all atoms \(A\subseteq W\). Summing the round-one counts over atom colours satisfying \(A\subseteq U_i\), round two recovers precisely
\[
N_i(W)=\#\{A:\dim A=1,\ A\subseteq W\cap U_i\}
=\frac{q^{e_i(W)}-1}{q-1}.
\]
This is strictly increasing in the nonnegative integer \(e_i(W)\). Hence all intersection dimensions \(e_i(W)\) are determined. When \(\dim W\le1\), the intersection dimensions are already known from rank and membership at round one. Thus round-two colours refine the partition by the full \(\mathbf a(W)\) vector.

**4. Such refinement cannot separate a class any further.** For each admissible vector \(\mathbf a\), any two subspaces \(W,W'\) with this vector lie in the same orbit of the subgroup \(\mathrm{GL}(V)\) preserving every \(U_i\). Indeed, build a basis of \(U_1\), then extend it successively to bases of \(U_2,\ldots,V\), at each stage first adding \(a_i\) basis vectors of \((W\cap U_i)/(W\cap U_{i-1})\), then completing with \(d_i-a_i\) other basis vectors. This produces a flag-adapted basis in which \(W\) is spanned by exactly the selected vectors. Perform the same construction for \(W'\), then map one adapted basis to the other. The resulting invertible linear map fixes every \(U_i\) and carries \(W\) to \(W'\). Any automorphism preserving the marks must preserve the intrinsic intersection dimensions, and all refinement colours are automorphism invariant. Consequently, refinement separates exactly the orbits, with no finer splitting; it is stable by round two.

**5. Count classes and their sizes.** The permitted integers \(a_i\) can be chosen independently in \([0,d_i]\), giving the class count. For the size of one class, inductively choose \(W_i=W\cap U_i\). Once \(W_{i-1}\) is fixed, select an \(a_i\)-space in \(U_i/U_{i-1}\) in \(\begin{bmatrix}d_i\\a_i\end{bmatrix}_q\) ways. Its lift to a subspace \(W_i\) with \(W_i\cap U_{i-1}=W_{i-1}\) is the graph of a linear map into \(U_{i-1}/W_{i-1}\); there are \(q^{a_i(\dim U_{i-1}-\dim W_{i-1})}\) such maps. Multiplying gives exactly the displayed size formula.

**6. The depth bound is attained.** In \(V=\mathbb F_2^4\), mark \(U=\langle e_1,e_2\rangle\). Take \(W_0=\langle e_3,e_4\rangle\) and \(W_1=\langle e_1,e_3\rangle\). Both have rank two, are unmarked, and are incomparable with \(U\). Their first-round colours agree because their total lower and upper counts agree and neither sees the uniquely marked \(U\) as a strict neighbour. Yet \(\dim(W_0\cap U)=0\) and \(\dim(W_1\cap U)=1\). Round two separates them, establishing universal sharpness.

## Verification

Two standalone programs are supplied: `check_flag_refinement.py` enumerates linear subspaces via row-reduced echelon matrices and exhaustively compares two-round colours with intersection signatures for many flags; `check_flag_orbits.py` uses an independent spanning-set construction over \(\mathbb F_2\), explicitly enumerates invertible linear maps, checks flag-stabilizer orbits, and verifies the Gaussian size formula. The first also checks the depth-two sharpness witness.

Run `python3 check_flag_refinement.py` and `python3 check_flag_orbits.py` from a directory containing these files. Their exact output is provided in `checks_output.txt`. The checks include \(q\in\{2,3\}\), dimensions through four in the standard run, a binary four-dimensional general-linear group of size \(20{,}160\), and additional selected flags in dimensions five over \(\mathbb F_2\) and four over \(\mathbb F_3\). The all-dimensional claim is supported by the proof, not by extrapolation from enumeration.

For \(q=2\), \(n=4\), and a marked two-space, there are \(\prod_i(d_i+1)=3\cdot3=9\) classes across the 67 subspaces; the class with increments \((1,1)\) contains \(18\) subspaces. For a full flag in \(\mathbb F_2^4\), there are \(16\) classes.

## Relationship to prior work

Kiefer, Schweitzer, and Selman (2015) set out the connection between two-variable counting logic and coarsest equitable partitions for finite relational structures. Arvind, Köbler, Rattan, and Verbitsky (2015) analyze colour refinement, individualization, and orbit-refinability, including graph families such as Johnson graphs. Neither inspected text states the flag-marked full-subspace-lattice result.

Berget and Huang (2011) study finite Grassmannians and partial flag varieties, Schubert decompositions, and Gaussian-counting identities. The intersection-vector orbit parameterization and its \(q\)-counting ingredients belong to that classical geometric setting; they are **not** separately claimed as new. The contribution asserted here is the exact **two-round logical recovery** of all those flag-stabilizer strata in the full strict-inclusion structure, including its sharpness and the resulting uniform stable-colour inventory.

## Limitations

The flag hypothesis is essential to the given transitivity argument; no result is asserted for arbitrary nonnested families of marked subspaces. Using only cover edges rather than full strict containment changes the algorithm and is outside the theorem. The claimed sharpness concerns the **universal** two-round bound, not every flag instance. No characteristic sentence identifying a particular lattice among all finite structures is supplied. Priority against specialized earlier literature remains an open verification risk; a negative search result is not a novelty theorem. No independent mathematical audit has occurred.

## References

1. A. Berget and J. Huang, *Cyclic sieving of finite Grassmannians and flag varieties*, arXiv:1106.1928v1, publicly posted 2011-06-09, https://arxiv.org/abs/1106.1928. The finite flag and Schubert material is in Sections 2–4.
2. S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1, publicly posted 2015-03-30, https://arxiv.org/abs/1503.08792. See Sections 1–2 and the discussion of finite relational structures.
3. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255v1, publicly posted 2015-02-04, https://arxiv.org/abs/1502.01255. See the refinability hierarchy and treatment of individualization.
