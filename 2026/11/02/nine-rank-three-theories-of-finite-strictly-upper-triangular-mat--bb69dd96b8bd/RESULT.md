# Nine rank-three theories of finite strictly upper-triangular matrix-unit semigroups

## Finding
For every \(n\ge1\), let
\[
U_n=\{0\}\cup\{e_{ij}:1\le i<j\le n\},\qquad
 e_{ij}e_{k\ell}=\begin{cases}e_{i\ell},&j=k,\\0,&j\ne k,\end{cases}
\]
with absorbing \(0\). In the one-sorted first-order language consisting of equality, a constant \(0\), and a ternary relation \(M(x,y,z)\) for \(xy=z\), the precise rank-three equivalence classification is
\[
U_m\equiv_3 U_n\quad\Longleftrightarrow\quad
(m=n<9)\ \lor\ (m,n\ge9),\quad m,n\ge1.
\]
Thus there are exactly nine rank-three theories in this family, represented by \(U_1,\ldots,U_9\). The largest smallest representative has \(1+\binom92=37\) elements. Equivalently, these are the strictly positive-length paths of an oriented line quiver, together with zero for noncomposable pairs; no stationary length-zero paths are included. The semigroups are nilpotent and their nilpotency indices grow without bound, although their rank-three theories stabilize at nine matrix indices.

## Assumptions and scope
All ranks refer to ordinary first-order quantifier nesting depth in the stated *relational*, not functional, multiplication signature. Each \(U_n\) consists only of the zero matrix and individual strictly upper-triangular matrix units, not arbitrary sums of matrix units. For \(n=1\) this is the one-element zero semigroup. Products associate because nonzero multiplication is concatenation of directed intervals on the chain \(1<\dots<n\).

## Proof
**Step 1: exact finite-type recursion.** For each finite \(U_n\), fix \(k\in\{0,1,2,3\}\). The complete atomic diagram of a selected tuple \((a_1,\ldots,a_k)\) records all equalities and all instances of \(M\) whose three arguments belong to the selected tuple together with the named zero. At length three there are \(4^2=16\) ordered equality tests and \(4^3=64\) multiplication tests, with symbols \((0,x,y,z)\). Write \(A_n(x,y,z)\) for this exact bit pattern. Define types recursively as *sets*, ignoring repetition:
\[
P_n(x,y)=\{A_n(x,y,z):z\in U_n\},\quad
Q_n(x)=\{P_n(x,y):y\in U_n\},\quad
R_n=\{Q_n(x):x\in U_n\}.
\]
These are the complete rank-one types of pointed pairs, rank-two types of pointed singles, and rank-three types of the unpointed structures. Indeed, Ehrenfeucht--Fraïssé backward induction says that equality of the corresponding sets of possible next-step types is equivalent to a Duplicator response to every move. Their atomic base diagram is recoverable by restricting any nonempty child diagram to the older variables; these semigroups have nonempty domains. Hence no atomic information was discarded in the set recursion. Integer type identifiers in the C++ implementation intern *complete exact bit patterns and sorted sets* with equality, not random fingerprints.

The standalone `tri_types.cpp` computes \(R_n\) exactly for every \(1\le n\le26\) and reports the respective identifiers
\[
0,1,2,3,4,5,6,7,8,8,\ldots,8.
\]
The corresponding pointed single-type counts are \(1,2,4,7,11,16,22,25,26\), then \(26\) through \(n=26\). The output in `tri_results26.txt` provides each bound and identifier. Thus \(U_1,\ldots,U_8\) are pairwise inequivalent and inequivalent to \(U_9\), and all \(U_9,\ldots,U_{26}\) have identical rank-three theories. The independently written `tri_independent.py` uses immutable nested sets of raw truth tuples rather than type interning and reproduces the same boundary for \(1\le n\le12\).

**Step 2: the infinite tail.** Consider the ordered index sets \(([n],<)\) and \(([m],<)\), with one *paired* move selecting at most two indices, repeated for three rounds. A standard gap strategy gives Duplicator an order- and equality-preserving response whenever both initial index sets have at least \(26\) points. For completeness set \(t_0=0\) and \(t_{r+1}=3t_r+2\), hence \(t_1=2\), \(t_2=8\), \(t_3=26\). With \(r\) moves remaining, keep a partial order isomorphism on selected indices and require each corresponding open gap to have equal cardinality when smaller than \(t_r\), and otherwise both cardinalities at least \(t_r\). In the next move, at most two *new* points enter a given gap, dividing it into at most three subgaps. When the old gap sizes are both at least \(3t_{r-1}+2\), the new points can be placed so that each small subgap is matched exactly and all larger subgaps remain at least \(t_{r-1}\): if all three subgaps were small, their total together with the two selected points would be smaller than \(3t_{r-1}+2\), a contradiction; allocate the surplus to a large subgap. Gaps not played in retain the weakened invariant. This proves the induction, including one-point moves and points already selected.

A zero semigroup move is answered by zero. A nonzero selection \(e_{ij}\), \(i<j\), is answered by \(e_{i'j'}\), where \(i',j'\) are the corresponding index-pair responses in the order game. After three moves, equality between any selected units and every product atom \(M(a,b,c)\) is determined by equality of the six index coordinates of the selected nonzero units: \(e_{ij}e_{k\ell}\) is nonzero exactly when \(j=k\), and then equals \(e_{i\ell}\). This is preserved by the order-game partial isomorphism. Therefore \(U_n\equiv_3U_m\) for all \(n,m\ge26\).

**Step 3: gluing.** Exact finite recursion yields \(U_9\equiv_3U_{26}\); the infinite paired-index strategy yields \(U_{26}\equiv_3U_n\) for all \(n\ge26\). Transitivity gives equivalence throughout \(n\ge9\). The distinct computed types at \(n<9\) prove optimality. No finite experiment was extrapolated to the infinite tail.

## Verification
Reproduce with a C++17 compiler and Python 3 by running `sh verify.sh` from the unpacked package directory. The script compiles the C++ implementation, runs its complete exact type recursion for \(1\le n\le26\), runs the independent Python recursion for \(1\le n\le12\), and byte-compares both outputs against `tri_results26.txt` and `tri_py12.txt`. C++ maps use exact equality for all atomic signatures and all sorted type-ID vectors. The paired-gap lemma and transitivity are separate mathematical arguments and are not certified by the finite programs.

## Relationship to prior work
Distler's 2010 thesis studies enumeration and classification of finite nilpotent semigroups, with an enumeration library for orders at most eight; that library cannot tabulate the \(37\)-element representative or establish the uniform infinite claim. Huschenbett and Kufleitner (arXiv:1310.3195v1, 2013) develop Ehrenfeucht--Fraïssé methods for order-based representations of semigroup language identities; their theorem concerns identities of omega-terms and logical fragments of words, not rank-three theories of this specific family. Gould and Quinn-Gregson (2019) study countable categoricity and important semigroup constructions, including Brandt semigroups, but not this exact bounded-depth finite classification. A separate prior classification for full Brandt matrix units allows idempotents \(e_{ii}\) and all off-diagonal units; these semigroups contain no nonzero idempotent and are not a parameter substitution of that result. No cited work currently establishes the nine-class assertion as a corollary. Priority outside the inspected corpus remains uncertain.

## Limitations
The theorem is restricted to single matrix units on strictly increasing ordered pairs, named absorbing zero, and *relational* multiplication at quantifier rank three. It does not assert stabilization in the functional multiplication language, higher ranks, arbitrary nilpotent semigroups, or all strict upper-triangular matrices. The independently reproduced finite experiment covers a smaller range than the C++ enumerator; the infinite upper bound rests on the proved paired-index game. The full text of Distler's thesis could not be retrieved during source inspection; only its repository metadata and abstract were accessible. Independent human validation and exhaustive historical priority are not claimed.

## References
1. Andreas Distler, *Classification and enumeration of finite semigroups*, PhD thesis, University of St Andrews, repository record dated 2010-06-23, https://research-repository.st-andrews.ac.uk/handle/10023/945 .
2. Martin Huschenbett and Manfred Kufleitner, *Ehrenfeucht-Fraïssé Games on Omega-Terms*, arXiv:1310.3195v1, first posted 2013-10-11, https://arxiv.org/abs/1310.3195 .
3. Victoria Gould and Thomas Quinn-Gregson, *\(\aleph_0\)-categoricity of semigroups*, *Semigroup Forum* 99 (2019), 260–292, https://doi.org/10.1007/s00233-019-10002-7 .
