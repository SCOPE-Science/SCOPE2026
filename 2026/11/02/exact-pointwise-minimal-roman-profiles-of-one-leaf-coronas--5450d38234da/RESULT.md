# Exact pointwise-minimal Roman profiles of one-leaf coronas

## Finding
For any finite simple base graph \(G=(V,E)\) with \(n=|V|\ge 1\), form its **one-leaf corona** \(G\odot K_1\) by adjoining a separate pendant vertex \(v'\) adjacent only to each \(v\in V\). A Roman dominating function takes labels in \(\{0,1,2\}\), and every zero-labeled vertex must have a neighbor labeled \(2\). Such a function is **pointwise-minimal** if no different coordinatewise smaller feasible function exists.

Let \(M_{G\odot K_1}(z)\) sum \(z^{\omega(f)}\) over all pointwise-minimal Roman dominating functions \(f\), where \(\omega(f)=\sum_x f(x)\). For \(A\subseteq V\), let \(B(A)=N_G(A)\setminus A\) and \(U(A)=V\setminus (A\cup N_G(A))\), using the open neighborhood of a set. Then the **entire weight polynomial** is
\[
\boxed{M_{G\odot K_1}(z)=\sum_{A\subseteq V}2^{|U(A)|}\,z^{2n-|B(A)|}.}
\]
All minimal functions are uniquely described by choosing \(A\) and, independently, one of two permitted leaf-base states for every vertex in \(U(A)\); the complete description is in the proof.

For the total number \(m(G)=M_{G\odot K_1}(1)\), one has the **sharp all-graph bounds**
\[
\boxed{2^{n+1}-1\le m(G)\le3^n.}
\]
For \(n\ge2\), equality on the left holds exactly for \(G=K_n\), and equality on the right exactly for the edgeless graph. Adding any missing base edge strictly decreases \(m(G)\).

For the *sunlet* \(C_n\odot K_1\), \(n\ge3\), its entire weight polynomial is the trace of the \(n\)-th power of the following explicitly weighted transfer matrix:
\[
\boxed{M_{C_n\odot K_1}(z)=\operatorname{tr}(T(z)^n),\quad
T(z)=\begin{pmatrix}
2z^2&z&0&0\\
0&0&z^2&z^2\\
z&z&0&0\\
0&0&z^2&z^2
\end{pmatrix}.}
\]
In particular, the number of pointwise-minimal Roman dominating functions on the sunlet is
\[
\boxed{M_{C_n\odot K_1}(1)=1+(1+\sqrt2)^n+(1-\sqrt2)^n\qquad (n\ge3).}
\]

## Assumptions and scope
Graphs are finite, undirected, and simple, and the corona has precisely one private leaf per original vertex. Vertex labels are compared in the pointwise order \(0<1<2\). The total-weight enumerator counts distinct functions on the original labeled vertex set, not automorphism orbits. No connectedness hypothesis is needed. The explicit transfer formula is for a single cycle with \(n\ge3\), not for a path or arbitrary product.

## Proof
**Local structure.** Fix a pointwise-minimal Roman dominating function \(f\), and define \(A=\{v\in V:f(v)=2\}\). For any original vertex \(v\), its private leaf \(v'\) has no neighbor other than \(v\). If \(v\in A\), the leaf must have label \(0\): positive leaf labels could be decreased, since \(v\) already carries \(2\). The original vertex cannot have its label \(2\) decreased, because the leaf of label \(0\) would immediately lose its unique possible defender. Hence the pair is \((f(v),f(v'))=(2,0)\).

If \(v\notin A\) has a neighbor in \(A\), the pair must be \((0,1)\). Indeed, \(f(v)=1\) could be decreased to \(0\) while the base neighbor still defends it, and \(f(v)=0\) forces the leaf to be positive. The leaf label \(2\) could be lowered to \(1\) without losing feasibility, so only leaf label \(1\) is minimal. This is exactly the case \(v\in B(A)\).

Finally, if \(v\in U(A)\), no original neighbor of \(v\) has label \(2\). There are precisely two possible pairs: \((0,2)\) and \((1,1)\). The first uses the private leaf as the defender of the zero-labeled base vertex; the second has two ones and no zero that needs defense. Every decrease of a positive entry in either pair breaks feasibility: decreasing the leaf from \(2\) leaves the base \(0\) undefended, while changing either \(1\) of \((1,1)\) to \(0\) creates a zero with no adjacent \(2\). Thus these are exactly the two minimal possibilities and may be chosen independently at vertices of \(U(A)\).

Conversely, every labeling constructed according to these three local cases is a Roman dominating function: each base zero in \(B(A)\) has a base defender, each base zero in \(U(A)\) has its leaf defender, and each leaf zero is next to its own base \(2\). Every positive entry is nondecreasable by the arguments above. Since feasible Roman functions are upward closed in the coordinatewise order, one-step nondecreasability is equivalent to pointwise minimality. Hence the classification is necessary and sufficient.

The three pair types contribute total weights \(2\), \(1\), and \(2\), respectively, so the weight is \(2|A|+|B(A)|+2|U(A)|=2n-|B(A)|\). The first two types are forced, and each of the \(|U(A)|\) vertices has exactly two possibilities, proving the polynomial formula.

**Extremal counts.** If an edge is added to \(G\), the size of \(U(A)\) cannot increase for any \(A\); it strictly decreases at least for \(A\) equal to one of the edge's endpoints (the other endpoint was a nonneighbor before insertion). Consequently \(m(G)=\sum_A2^{|U(A)|}\) decreases strictly. The smallest possible value is therefore attained exactly at the complete graph and the largest exactly at the empty graph when \(n\ge2\). For the empty graph, \(|U(A)|=n-|A|\), so the sum is \(3^n\). For the complete graph, the empty set contributes \(2^n\), and each of the \(2^n-1\) nonempty sets contributes \(1\). This establishes both bounds and equality cases. At \(n=1\) both bounds equal \(3\).

**Cyclic transfer.** On \(C_n\), encode a subset \(A\) by a cyclic binary word \(a_1\ldots a_n\) with \(a_i=1\) if \(i\in A\). The contribution of the middle bit \(b\) in a triple \((a,b,c)\) is \(z^2\) when \(b=1\), \(z\) when \(b=0\) and at least one neighboring bit is \(1\), and \(2z^2\) when all three bits are \(0\). Using states \(00,01,10,11\) and transitions \(ab\longrightarrow bc\) gives the displayed matrix \(T(z)\). Closed length-\(n\) walks correspond bijectively to indexed cyclic binary words, including the constant words, yielding the trace identity for every \(n\ge3\).

Direct determinant expansion gives
\[
\det(\lambda I-T(z))=\lambda\bigl(\lambda^3-3z^2\lambda^2+(2z^4-z^3)\lambda+2z^5-z^4\bigr).
\]
At \(z=1\) this factors as \(\lambda(\lambda-1)(\lambda^2-2\lambda-1)\). Taking the sum of the \(n\)-th powers of the four eigenvalues, with algebraic multiplicity, proves the Pell–Lucas expression for \(n\ge3\).

## Verification
The included standard-library-only program `verify.py` independently constructs corona adjacency and tests the original Roman domination and pointwise-minimal conditions, rather than relying on the structural criterion. It exhaustively checks all \(75\) simple base graphs of orders \(1\) through \(4\), comparing full weight polynomials with the sum formula. For cycles of orders \(3\) through \(6\), it compares direct exhaustive function counts, the subset formula and the transfer-matrix formula. It verifies the exact Pell–Lucas numerical identity for cycle orders \(3\) through \(18\). Executing the program prints `VERIFY_OK` after all assertions pass. The complete proof above, rather than finite enumeration, establishes the infinite statements.

## Relationship to prior work
Abu-Khzam, Fernau and Mann (2022; arXiv:2204.04765) study extension and polynomial-delay enumeration of **pointwise-minimal** Roman dominating functions on arbitrary graphs; their general private-neighbor framework is prior art. Their subsequent 2022 preprint (arXiv:2208.05261) treats enumeration bounds for several graph classes and exact counts for paths. The present result is a special-graph-product structural identity and **complete weight-count formula** for every one-leaf corona, with sharp total-count extremals and an explicit sunlet transfer/spectrum. The general enumeration algorithms do not directly supply the displayed formula, bounds, or cycle trace in the inspected material. Earlier Roman-domination work on coronas studies minimum weights and specific configurations rather than this complete pointwise-minimal weight distribution. The familiar optimization identity \(\gamma_R(G\odot K_1)=n+\gamma(G)\) also follows from the weight formula, but is *not* the new claim and is not asserted to have been first discovered here.

## Limitations
No independent mathematical audit has been performed. The result does not claim to characterize the zeros, asymptotic coefficient distribution, or automorphism orbits of the full polynomial for arbitrary base graphs. The full enumeration uses a sum over all subsets of \(V(G)\) and is not a polynomial-time algorithm for arbitrary input graphs. The originality assessment covers inspected sources and accessible mathematical-record searches but cannot exclude an unindexed equivalent formula or a previously unpublished consequence of an earlier general theorem.

## References
- F. N. Abu-Khzam, H. Fernau and K. Mann, *Minimal Roman Dominating Functions: Extensions and Enumeration*, arXiv:2204.04765, first public 2022-04-10, https://arxiv.org/abs/2204.04765.
- F. N. Abu-Khzam, H. Fernau and K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, arXiv:2208.05261, first public 2022-08-10, https://arxiv.org/abs/2208.05261.
- M. Siva Parvathi and B. Maheswari, *Roman Dominating and Total Dominating Functions of Corona Product Graph of a Path with a Star*, International Journal of Computer Engineering and Technology 5(1), 21–27 (2014), https://iaeme.com/Home/article_id/IJCET_05_01_003.
