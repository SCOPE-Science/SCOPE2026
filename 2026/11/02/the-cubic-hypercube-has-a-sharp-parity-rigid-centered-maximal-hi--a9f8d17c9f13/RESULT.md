# The cubic hypercube has a sharp parity-rigid centered maximal Hilbert norm

## Finding

On the eight-vertex graph \(Q_3\), the centered Hardy–Littlewood graph-ball maximal operator \(M\) has exact, attained strong-type norm
\[
\boxed{\|M\|_{\ell^2\to\ell^2}=\frac{\sqrt{13+3\sqrt{17}}}{4}}.
\]
Every nonzero real norming input, up to a graph automorphism, nonzero scalar magnitude, and independent coordinate signs, has absolute value \(1\) on the four vertices of one bipartition class and \(\sqrt{17}-4\) on the other four vertices. There are precisely two labeled nonnegative norming rays, one for each choice of the larger bipartition class. In particular, neither averaging over radius-two balls nor the radius-three full graph improves the sharp norm over the optimal zero/one-radius pattern. The sharp norm matches the radius-zero/one parity amplification obtainable on the distinct diameter-two graph \(K_{3,3}\), despite \(Q_3\) having diameter three.

## Assumptions and scope

Take \(V=\{0,1\}^3\) with Hamming graph distance and counting measure. For real \(f:V\to\mathbb R\), put
\[
(Mf)(v)=\max_{0\le r\le3}\frac{1}{|B(v,r)|}\sum_{u\in B(v,r)}|f(u)|,
\quad B(v,r)=\{u:d(u,v)\le r\}.
\]
The norm uses the same unnormalized counting \(\ell^2\) measure for input and output. The four ball cardinalities at every vertex are exactly \(1,4,7,8\). The assertion concerns the *centered ball* maximal operator, not maximal spherical means or uncentered balls. All edge lengths and vertex masses in this statement are one.

## Proof

**Reduction to a finite matrix maximum.** For each radius assignment \(\rho:V\to\{0,1,2,3\}\), let \(A_\rho\) have row \(v\) equal to normalized indicator of \(B(v,\rho(v))\). Every entry of every \(A_\rho\) is nonnegative. For \(g=|f|\), coordinatewise maximization gives
\[
\|Mf\|_2^2=\max_\rho\|A_\rho g\|_2^2.
\]
For a nonnegative matrix, replacing any real vector with its coordinatewise absolute value cannot decrease its output norm, so \(\sup_{g\ge0}\|A_\rho g\|_2/\|g\|_2=\|A_\rho\|_{2\to2}\). Since the selection family is finite,
\[
\|M\|_{2\to2}^2=\max_{\rho\in\{0,1,2,3\}^8}\lambda_{\max}(A_\rho^{\mathsf T}A_\rho).
\tag{1}
\]
Thus there are exactly \(4^8=65,536\) cases, not an unbounded search.

**Explicit winning matrix and its spectrum.** Partition the cube by Hamming-weight parity. For the selection \(\rho=0\) on one class and \(\rho=1\) on the other, order the two classes consecutively. Then
\[
A_\rho=\begin{pmatrix}I_4&0\\ C/4&I_4/4\end{pmatrix},
\]
where \(C\) is the \(4\)-by-\(4\) bipartite adjacency matrix of \(Q_3\). Each vertex in one class has exactly one antipode in the other class and is adjacent to all other three vertices. Hence \(C=J_4-P\) for a permutation matrix \(P\), and its singular values are \(3,1,1,1\). The two-dimensional block for singular value \(3\) has Gram matrix
\[
\frac{1}{16}\begin{pmatrix}25&3\\3&1\end{pmatrix}.
\]
Its largest eigenvalue is \(\lambda_*=(13+3\sqrt{17})/16\), simple and greater than every other singular block's largest eigenvalue. A corresponding strictly positive input is constant \(1\) on the radius-zero class and constant \(t=\sqrt{17}-4\) on the radius-one class. Reversing the two classes gives the second winning selection. Since \(4<t+4<5\), one has \(0<t<1\). At a value-one vertex the four radius means are \(1,(1+3t)/4,(4+3t)/7,(1+t)/2\), so radius zero is strictly largest. At a value-\(t\) vertex they are \(t,(3+t)/4,(3+4t)/7,(1+t)/2\); the radius-one mean exceeds radius zero, two and three respectively by \(3(1-t)/4\), \(9(1-t)/28\), and \((1-t)/4\). Therefore the constructed matrix choices are genuinely active, and equality is attained for \(M\).

**Exclusion of all other selections.** Let \(T_\rho=56A_\rho\); its entries are integers, because the possible row denominators are \(1,4,7,8\). Set \(\tau=317/200\) and form the integer symmetric matrix
\[
D_\rho=317\cdot56^2 I_8-200 T_\rho^{\mathsf T}T_\rho
=200\cdot56^2(\tau I_8-A_\rho^{\mathsf T}A_\rho).
\]
The accompanying standard-library-only verifier exhausts every radius assignment. For each of the \(65,534\) assignments other than the two alternating-parity selections, it applies exact integer fraction-free symmetric elimination and checks the positivity of all eight successive leading principal minors of \(D_\rho\). No approximate eigenvalue, sampling, or external numeric oracle is used. Positivity of all these minors is equivalent by Sylvester's criterion to \(D_\rho\) being positive definite. Consequently, for all other assignments,
\[
\lambda_{\max}(A_\rho^{\mathsf T}A_\rho)<317/200.
\]
Meanwhile \(\lambda_*>317/200\), because \(\sqrt{17}>103/25\), which follows from \(17>(103/25)^2\). Combined with (1), this proves the exact sharp norm and shows that precisely the two parity assignments maximize the matrix spectral norm.

**All equality cases.** The winning Gram matrix is nonnegative and irreducible: the adjacency relation through its positive entries connects all eight vertices. Perron–Frobenius gives a unique positive top eigenvector up to scaling. The block calculation identifies this vector as the two-level profile \((1,t)\) across the parity classes. Since every real extremizer of the nonlinear maximal operator must also maximize at least one selected matrix, the strict separation above leaves only these two rays for \(|f|\). Signs may be chosen independently because \(M\) depends only on \(|f|\). Cube automorphisms interchange the classes, completing the classification.

## Verification

Run `python3 verify.py` with the file in this package. It builds the cube from independent bit-flip edges, reconstructs all-pairs graph distances by breadth-first search, checks the \(1,4,7,8\) ball sizes, enumerates every \(4^8\) radius assignment and performs integer-only Sylvester checks for all \(65,534\) nonexceptional matrices. It additionally checks the structural bipartite adjacency identities of both exceptional selections and the exact strict threshold separation. Its deterministic success output is:

`CERTIFICATE_OK selections=65536 strict=65534 exceptional=2`

The finite part of the proof is an exhaustive certificate for this **fixed** finite graph, not evidence extrapolated to other cube dimensions. The analytic parts identify the norming eigenvalue and all extremizers.

## Relationship to prior work

Soria and Tradacete (arXiv:1410.6204, first available 2014-10-22) develop centered finite-graph maximal operators and general sharp \(\ell^p\) results principally for \(p\le1\), including four-vertex \(\ell^1\) examples. González-Riquelme and Madrid (arXiv:2005.03146) give sharp strong \(\ell^2\) constants for complete graphs and stars; their main strong-norm statements do not cover \(Q_3\). Harrow–Kolla–Schulman (arXiv:1209.4148) and Krause (arXiv:1309.4466) prove dimension-free maximal inequalities for *spherical* averages on Boolean cubes, rather than the precise eight-vertex graph-ball constant or norming profile here. Those spherical estimates cannot identify this exact ball norm: the ball operator is pointwise dominated by the spherical maximal operator but has different averaging candidates.

The elementary radius-zero/one parity matrix on \(K_{3,3}\) has the same controlling \(2\)-by-\(2\) Gram block and therefore attains the same numerical lower bound. That observation does not imply the sharp upper bound on \(Q_3\), whose radius-two and radius-three balls create additional row-selection matrices. The exclusion of all those additional configurations is the distinctive assertion.

## Limitations

This proof is specific to the unweighted eight-vertex cube and real centered ball averages. It does not determine sharp norms on higher cubes, weighted cubes, general cubic bipartite graphs, other \(\ell^p\) exponents, spherical maximal means, or uncentered maximal operators. The rigorous finite certificate establishes correctness of the stated computation when its integer arithmetic and matrix reduction are inspected; no independent external scientific audit is implied. A literature search cannot exclude every unpublished or unindexed equivalent computation.

## References

- A. W. Harrow, A. Kolla, L. J. Schulman, *Dimension-Free \(L_2\) Maximal Inequality for Spherical Means in the Hypercube*, arXiv:1209.4148, submitted 2012-09-19, https://arxiv.org/abs/1209.4148.
- B. Krause, *Dimension-Free \(L^p\)-Maximal Inequalities for Spherical Means in the Hypercube*, arXiv:1309.4466, submitted 2013-09-17, https://arxiv.org/abs/1309.4466.
- J. Soria, P. Tradacete, *Best constants for the Hardy-Littlewood maximal operator on finite graphs*, arXiv:1410.6204, submitted 2014-10-22, https://arxiv.org/abs/1410.6204.
- C. González-Riquelme, J. Madrid, *Sharp Inequalities for Maximal Operators on Finite Graphs*, arXiv:2005.03146, submitted 2020-05-06, https://arxiv.org/abs/2005.03146.
