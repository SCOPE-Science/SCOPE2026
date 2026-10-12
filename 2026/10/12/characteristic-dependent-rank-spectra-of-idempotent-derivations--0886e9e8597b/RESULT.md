# Characteristic-dependent rank spectra of idempotent derivations of triangular matrix algebras

## Finding
Let \(K\) be a field, \(n\ge 2\), and \(T_n(K)\) the unital associative algebra of upper triangular \(n\times n\) matrices. A derivation is a \(K\)-linear map \(D:T_n(K)\to T_n(K)\) satisfying \(D(XY)=D(X)Y+XD(Y)\). An idempotent derivation satisfies \(D^2=D\), with the square taken under composition.

Every idempotent derivation is \(D=\operatorname{ad}_{U H U^{-1}}\), where \(U\) is upper unitriangular, \(\operatorname{ad}_{H}(X)=HX-XH\), and \(H=\operatorname{diag}(\lambda_1,\dots,\lambda_n)\) has \(\lambda_1=0\). The normalized diagonal labels are exactly:

* If \(\operatorname{char}K\ne 2\), the zero string or \((0,\dots,0,-1,\dots,-1)\), with a unique cut after position \(k\) for \(1\le k<n\).
* If \(\operatorname{char}K=2\), any binary string \((0,\epsilon_2,\dots,\epsilon_n)\), \(\epsilon_i\in\{0,1\}\).

Different normalized label strings yield disjoint unitriangular orbits of derivations. If \(K=\mathbf F_q\), a nonconstant string with \(k\) entries equal to one label and \(n-k\) to the other determines \(q^{k(n-k)}\) distinct derivations, each of rank \(k(n-k)\). The complete rank enumerator is therefore

\[
\mathcal P_{n,q}(t)=\sum_{D^2=D}t^{\operatorname{rank}D}=
\begin{cases}
1+\displaystyle\sum_{k=1}^{n-1}q^{k(n-k)}t^{k(n-k)}, &\text{if }q\text{ is odd},\\[2mm]
1+\displaystyle\sum_{k=1}^{n-1}\binom{n-1}{k}q^{k(n-k)}t^{k(n-k)}, &\text{if }q\text{ is even}.
\end{cases}
\]

In particular, \(\mathcal P_{3,q}(t)=1+2q^2t^2\) for odd \(q\), versus \(1+3q^2t^2\) for even \(q\). Evaluation at \(t=1\) counts all idempotent derivations. The zero derivation contributes the initial \(1\).

## Assumptions and scope
Every field is allowed in the structural classification, without a hypothesis of algebraic closedness or perfectness. Counting requires a finite field of cardinality \(q\), an arbitrary prime power. The rank is the rank of \(D\) acting on the \(n(n+1)/2\)-dimensional \(K\)-vector space \(T_n(K)\), not the matrix rank of its inner generator. Automorphisms used for normal forms are inner conjugations by upper unitriangular matrices. The result concerns associative-algebra derivations; it is not a classification of general linear idempotents or of idempotent elements of \(T_n(K)\).

## Proof
**1. All derivations are inner.** Write \(e_i=E_{ii}\), and let \(\delta\) be any \(K\)-linear derivation. Put \(A=\sum_i\delta(e_i)e_i\). Differentiating \(e_i^2=e_i\) gives \(e_i\delta(e_i)e_i=0\). For \(i\ne j\), differentiating \(e_je_i=0\) and multiplying by \(e_i\) shows \(e_j\delta(e_i)e_i=-\delta(e_j)e_i\). Consequently \(Ae_j=\delta(e_j)e_j\) and \(e_jA=-\delta(e_j)(1-e_j)\), so \([A,e_j]=\delta(e_j)\) for every \(j\). Thus \(\delta'=\delta-\operatorname{ad}_A\) kills every \(e_j\).

For \(i\le j\), the one-dimensional Peirce component \(e_iT_n(K)e_j=K E_{ij}\) is preserved by \(\delta'\); hence \(\delta'(E_{ij})=c_{ij}E_{ij}\), where \(c_{ii}=0\). From \(E_{ij}E_{j\ell}=E_{i\ell}\), we obtain \(c_{ij}+c_{j\ell}=c_{i\ell}\). Taking \(a_i=c_{in}\) for \(i<n\) and \(a_n=0\), one has \(c_{ij}=a_i-a_j\), proving \(\delta'=\operatorname{ad}_{\operatorname{diag}(a_i)}\). An inner generator is unique modulo \(K I\): commuting with all \(e_i\) makes it diagonal, and commuting with all \(E_{i,i+1}\) makes its diagonal constant.

**2. Idempotence forces a diagonalizable generator.** Let \(D=\operatorname{ad}_H\), with \(H\) upper triangular. Its characteristic polynomial splits over \(K\); the polynomial primary decomposition of \(H\) yields commuting \(H=S+N\), where \(S\) is diagonalizable over \(K\), \(N\) is nilpotent, and both are upper triangular. Then \(\operatorname{ad}_S\) is diagonalizable (matrix units between eigenvectors give eigenvalues equal to differences of eigenvalues of \(S\)); \(\operatorname{ad}_N\) is nilpotent because it is the difference of the commuting nilpotent operators of left- and right-multiplication by \(N\). These operators commute. If \(D^2=D\), then \(D\) is diagonalizable with eigenvalues among \(0,1\), because \(X(X-1)\) is square-free over every field. In a commuting semisimple-plus-nilpotent decomposition, the nilpotent term must be zero: on each eigenspace of \(\operatorname{ad}_S\), \(D\) would otherwise have a nontrivial nilpotent Jordan part. Thus \(\operatorname{ad}_N=0\). By the center calculation in step 1, \(N\) is scalar, and nilpotence forces \(N=0\). Hence \(H=S\) is diagonalizable.

**3. Triangular normal form and the label restriction.** The spectral projectors of upper triangular diagonalizable \(H\) preserve the standard flag. For each standard vector \(e_j\), applying the projector for its diagonal entry \(\lambda_j\) produces an eigenvector congruent to \(e_j\) modulo the first \(j-1\) basis vectors. These eigenvectors form an upper unitriangular eigenbasis \(U\), so \(H=U\operatorname{diag}(\lambda_i)U^{-1}\). Conjugation by \(U\) acts by an automorphism of \(T_n(K)\) and transports \(\operatorname{ad}_H\) to the diagonal adjoint.

On the basis units \(E_{ij}\), \(i\le j\), the diagonal adjoint is multiplication by \(\lambda_i-\lambda_j\). It is idempotent if and only if
\[
\lambda_i-\lambda_j\in\{0,1\}\quad\text{for every }i<j.
\]
Adding a common scalar does not change the derivation; normalize \(\lambda_1=0\). Then every \(\lambda_j\) belongs to \(\{0,-1\}\). When the characteristic differs from two, \(-1\notin\{0,1\}\), so an occurrence of \(-1\) cannot precede a later \(0\); this produces exactly one cut. When the characteristic is two, \(-1=1\), and arbitrary binary strings satisfy all pairwise conditions. Two different normalized diagonal strings cannot become conjugate modulo a scalar, because upper triangular conjugation preserves each diagonal entry.

**4. Finite-field orbits and ranks.** For a fixed normalized diagonal \(H\) with two distinct labels, put \(c=\#\{(i,j):i<j,\lambda_i\ne\lambda_j\}\). The upper unitriangular group has \(q^{n(n-1)/2}\) elements; its stabilizer of \(H\) consists of matrices whose \((i,j)\) entry is zero whenever \(\lambda_i\ne\lambda_j\), and has \(q^{n(n-1)/2-c}\) elements. Its orbit therefore has \(q^c\) members, and these correspond to different derivations since the generator is unique modulo scalars and all generators in the orbit have the same diagonal. The image of \(\operatorname{ad}_H\) is spanned by precisely the \(E_{ij}\) with unequal labels, so \(\operatorname{rank}D=c\). With \(k\) labels of one kind, \(c=k(n-k)\), independent of their positions.

In odd characteristic there is one nonzero normalized label string for every cut \(k=1,\dots,n-1\). In characteristic two, the first label is fixed to zero and choosing the remaining \(k\) nonzero labels contributes \(\binom{n-1}{k}\) strings. Adding the zero derivation gives the two asserted enumerators. These steps are valid over all finite prime powers; no field-size assumptions were introduced.

## Verification
The attached standalone Python program `verify.py` independently lists all inner generators modulo scalars over selected prime fields, constructs the full derivation matrix on the matrix-unit basis, tests \(D^2=D\) entrywise, computes ranks by modular row reduction, and compares with the formulas. Its exact test cases are \((n,p)=(2,2),(2,3),(2,5),(3,2),(3,3),(3,5),(4,2),(4,3),(5,2)\); execution returns `VERIFY_OK`. The test exhausts those finite instances, not arbitrary dimensions or extension fields. The preceding algebraic argument proves the general claims without invoking these tests.

## Relationship to prior work
Cheraghpour--Jafari, arXiv:2402.12611v1 (first posted February 20, 2024; primary MSC 16S50), develops structural results about Jordan superderivations of triangular matrix rings, not composition-idempotent rank spectra. The conventional description of derivations as inner for upper triangular matrix algebras is older (e.g. Jøndrup, 1995); it is used and proved again here, not claimed as novel. Vladeva (2022) describes derivations of triangular matrix rings, while Vladeva's earlier semiring work treats derivations over additively idempotent semirings, a different base algebra. Hou (2019) and Wright (2020) study idempotent triangular **matrices**, distinct from idempotent **derivations**; their results provide an important comparison, especially for the characteristic-two reduction to binary diagonal matrices. The contribution here is the all-characteristic classification of derivation projections together with exact complete rank multiplicities and their characteristic-two change.

## Limitations
The classification is for unital associative upper triangular matrix algebras with scalar entries over a field, not arbitrary triangular rings over noncommutative bases. A previously established equivalent formulation might exist in literature on projection derivations, multiplicative splittings, or idempotent triangular matrices; comparison with certain restricted-access publisher articles could not be completed from full text. Finite computations do not establish the formulas beyond their enumerated cases. This is a mathematical derivation and reproducibility record, not a claim of independent assessment.

## References
1. H. Cheraghpour and M. Jafari, *On Jordan superderivations and Jordan super-biderivations of trivial extensions and triangular matrix rings*, arXiv:2402.12611v1 (2024), https://arxiv.org/abs/2402.12611.
2. D. I. Vladeva, *Derivations of triangular matrix rings*, Linear and Multilinear Algebra 71 (2023), 1450–1461, DOI:10.1080/03081087.2022.2063786 (first published online April 18, 2022).
3. D. I. Vladeva, *Derivatives of triangular, Toeplitz, circulant matrices and of matrices of other forms over semirings*, arXiv:1707.04716v1 (2017), https://arxiv.org/abs/1707.04716.
4. X. Hou, *Idempotents in triangular matrix rings*, Linear and Multilinear Algebra, DOI:10.1080/03081087.2019.1596223 (2019).
5. S. Wright, *Triangular idempotent matrices over a general ring*, Linear and Multilinear Algebra, DOI:10.1080/03081087.2020.1773377 (2020).
6. S. Jøndrup, *Automorphisms and derivations of upper triangular matrix rings*, Linear Algebra Appl. 221 (1995), 205–218.
