# Gaussian-binomial enumeration of rank-one Rota–Baxter operators on triangular matrix algebras

## Finding
Let \(k=\mathbb F_q\), where \(q\) is any prime power, and let \(T_n(k)\) denote the associative algebra of upper-triangular \(n\times n\) matrices. A weight-zero Rota–Baxter operator is a \(k\)-linear map \(R:T_n(k)\to T_n(k)\) satisfying
\[
R(x)R(y)=R(R(x)y+xR(y))\quad(x,y\in T_n(k)).
\]
The rank of an operator below is its rank as a linear transformation on the entire algebra, not the matrix rank of any image element.

**Theorem.** For every \(n\ge 1\), the number of nonzero, vector-space-rank-one weight-zero Rota–Baxter operators whose one-dimensional image is spanned by an idempotent is
\[
B_n(q)=2\sum_{k=1}^{n-1}q^{k(n-k)}\left({n\brack k}_q-\binom nk\right),
\]
where \({n\brack k}_q\) is the Gaussian binomial coefficient. This is exactly the number of rank-one Rota–Baxter operators with image spanned by an element of nonzero square.

In the first triangular matrix algebra whose Jacobson radical has nonzero square, \(T_3(\mathbb F_q)\), the **complete** count of nonzero rank-one weight-zero Rota–Baxter operators is
\[
\boxed{\mathcal R_3(q)=3q^5+4q^4+4q^3-8q^2-2q-1.}
\]
Of these,
\[
\boxed{A_3(q)=3q^5-2q-1}
\]
have square-zero image generators and
\[
\boxed{B_3(q)=4q^2(q^2+q-2)}
\]
have idempotent image generators. Both formulas hold in characteristic two and for nonprime finite fields. In particular the totals for \(q=2,3,4,5\) are \(155,1082,4215,12164\).

## Assumptions and scope
All fields in the theorem are finite, with no restriction on characteristic. The algebra \(T_n(k)\) has identity; \(n\ge1\) and \(q\) is a prime power. The counting is of distinct **labeled linear operators**, without division by algebra automorphisms or nonzero scalar multiples. Zero operators and maps of rank greater than one are excluded. The two image-generator types are disjoint and exhaustive for rank-one weight-zero operators over any field.

An idempotent \(e\) means \(e^2=e\) and \(e\ne0\). A square-zero generator \(u\) satisfies \(u\ne0\), \(u^2=0\). Every line spanned by a nonsquare-zero image generator contains a unique nonzero idempotent; a square-zero image line contains none.

## Proof
### 1. The rank-one reduction, used as background
On an arbitrary unital associative algebra \(A\) over a field, write a nonzero rank-one map as \(R(x)=f(x)u\), where \(u\ne0\) and \(f\ne0\). Substituting in the Rota–Baxter identity gives
\[
f(x)f(y)u^2=(f(x)f(uy)+f(y)f(xu))u.\]
Choosing \(x,y\) with nonzero functional values forces \(u^2\in ku\). Writing \(u^2=\lambda u\), insert \(x\in\ker f\), then \(y\in\ker f\), to see that there exist scalars \(a,b\) for which
\[
f(uy)=af(y),\qquad f(xu)=bf(x),\qquad a+b=\lambda.
\]
Since left and right multiplication by \(u\) have squares equal to multiplication by \(\lambda u\), their induced eigenvalues satisfy \(a^2=\lambda a\) and \(b^2=\lambda b\). If \(\lambda=0\), then \(a=b=0\) over a field, and precisely the nonzero functionals annihilating \(uA+Au\) are allowed. If \(\lambda\ne0\), scale \(u\) uniquely to the idempotent \(e=u/\lambda\) and absorb the scale into the functional. The possible pairs of eigenvalues of multiplication by \(e\) are exactly \((1,0)\) and \((0,1)\). Thus the admissible nonzero functionals for the normalized image generator \(e\) are precisely the nonzero duals of the Peirce corners \(eA(1-e)\) and \((1-e)Ae\); there are
\[
(q^{\dim eA(1-e)}-1)+(q^{\dim(1-e)Ae}-1)
\]
choices. The two classes do not intersect because a functional simultaneously satisfying both pairs would be zero. Conversely each described pair satisfies the displayed identity directly. This reduction is not asserted to be a new classification in general algebras.

### 2. Idempotent-image enumeration for every \(n\)
An idempotent \(e\in T_n(k)\) has diagonal entries \(\epsilon_i\in\{0,1\}\). Let \(D=\operatorname{diag}(\epsilon_1,\ldots,\epsilon_n)\), and put \(J\) for the strictly upper-triangular ideal. The matrix
\[
w=eD+(1-e)(1-D)\]
satisfies \(w\equiv1\pmod J\) and \(ew=wD\). It is therefore invertible and gives \(e=wDw^{-1}\), with \(w\in1+J\). For a fixed zero-one diagonal word containing \(k\) ones and \(n-k\) zeros, the group \(1+J\) acts transitively by conjugation. Its stabilizer at \(D\) consists precisely of upper-unitriangular entries supported at pairs \(i<j\) with \(\epsilon_i=\epsilon_j\). There are exactly \(k(n-k)\) pairs with unequal entries, so the number of idempotents with that diagonal is \(q^{k(n-k)}\).

Conjugation preserves Peirce dimensions. For \(D\),
\[
\dim DA(1-D)=N_{10}(\epsilon):=\#\{(i,j):i<j,\ \epsilon_i=1,\ \epsilon_j=0\},
\]
\[
\dim (1-D)AD=N_{01}(\epsilon):=\#\{(i,j):i<j,\ \epsilon_i=0,\ \epsilon_j=1\}.
\]
Summing the rank-one functional counts over all words of fixed Hamming weight \(k\), the inversion enumerator identity yields
\[
\sum_{|\epsilon|=k}q^{N_{10}(\epsilon)}=
\sum_{|\epsilon|=k}q^{N_{01}(\epsilon)}={n\brack k}_q.
\]
Since there are \(\binom nk\) words, their total contribution is
\(2q^{k(n-k)}({n\brack k}_q-\binom nk)\). Summation for \(1\le k<n\) proves \(B_n(q)\); the two constant diagonal words give no admissible functionals.

### 3. Complete square-zero-image count for \(T_3(k)\)
Write a strictly upper-triangular matrix as
\[
u=aE_{12}+bE_{23}+cE_{13}.
\]
Every square-zero element of \(T_3(k)\) has zero diagonal, and \(u^2=abE_{13}\), so \(u^2=0\) exactly when \(ab=0\). The projective lines of nonzero square-zero elements fall into three disjoint families: \(a\ne0,b=0\), consisting of \(q\) lines; \(a=0,b\ne0\), consisting of another \(q\) lines; and the unique central line \(a=b=0,c\ne0\). In the first two families \(\dim(uA+Au)=2\), while on the central line this dimension is \(1\). For a given projective image generator of either first type, \(f\) has \(q^{6-2}-1=q^4-1\) choices; on the central line, \(q^{6-1}-1=q^5-1\) choices. Each operator is counted exactly once by choosing a normalized representative of its image line, hence
\[
A_3(q)=2q(q^4-1)+(q^5-1)=3q^5-2q-1.
\]
The all-dimension formula at \(n=3\) gives
\[
B_3(q)=2\sum_{k=1}^{2}q^2({3\brack k}_q-3)=4q^2(q^2+q-2).
\]
Their sum proves the displayed complete census. No divisibility assumptions on \(q\) were used.

## Verification
Two standalone verifiers are included. Compile \(rb_triangular_verify.cpp\) with a C++17 compiler and execute it to exhaust all projective rank-one maps over \(\mathbb F_2\) and \(\mathbb F_3\). Unlike the symbolic proof, this checker tests the defining Rota–Baxter identity on all ordered pairs of the six matrix-unit basis elements. The observed totals are \(155\) and \(1082\), partitioned as \((91,64)\) and \((722,360)\) by image type.

Run \(rb_peirce_verify.py\) with Python 3 to enumerate all binary idempotents of \(T_n(\mathbb F_2)\) for \(n=2,3,4\), calculate Peirce-corner dimensions by independent binary row reduction, and compare with the Gaussian-binomial formula; the nonzero idempotent-image operator counts are \(4,64,1280\). The arithmetic values for other \(q\) in the statement follow algebraically from the proved polynomial, not from a claimed exhaustive computational check. Finite computations are illustrative tests, not proofs of the universal statements.

## Relationship to prior work
Guo–Rosenkranz–Zheng (first arXiv submission 2014-02-15) classify weight-zero Rota–Baxter operators on two- and three-element semigroup algebras over characteristic-zero fields. These algebras have vector-space dimensions at most three and do not include the six-dimensional triangular algebra in the present census.

Gubarev (first arXiv submission 2024-03-30) gives a classification, up to suitable symmetries and scalar multiplication, of **all** weight-zero Rota–Baxter operators on \(T_3(F)\) over characteristic-zero fields. His stronger structural classification covers the rank-one solutions in that characteristic; the present contribution is not a new characteristic-zero operator classification. The explicit finite-field labeled count in every characteristic, together with the independent all-\(n\) Gaussian-binomial formula for the idempotent-image stratum, is not stated by that classification. A future derivation from its normal forms could recover portions of the count in suitable characteristics.

Previous enumerations for radical-square-zero path algebras concern a different associative algebra: \(T_3(k)\) has \(J^2=kE_{13}\ne0\), whereas the corresponding radical-square-zero quotient kills that product. Consequently, their numerical operator counts do not transfer to the present algebra. The general rank-one reduction in the proof is background, not a new contribution.

## Limitations
The complete count is given only for \(n=3\); for arbitrary \(n\) the theorem counts just the idempotent-image part, not the entire rank-one locus. Nothing here classifies higher-rank Rota–Baxter operators or orbit counts under conjugation. The formulas count rational points over finite fields and make no claim about the scheme structure of parameter spaces. Originality is assessed against the stated relevant sources and searches, not independently certified or claimed as absolute priority.

## References
1. L. Guo, M. Rosenkranz, S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702 (initial submission 2014-02-15), https://arxiv.org/abs/1402.3702.
2. V. Gubarev, *Rota–Baxter operators of weight zero on upper-triangular matrices of order three*, arXiv:2404.00289 (initial submission 2024-03-30), https://arxiv.org/abs/2404.00289.
