# Gaussian-moment deficits obstruct universal fixed-margin correlation compatibility

## Statement

Let \(F\) be a standardised probability law on \(\mathbb R\): if \(X\sim F\), then
\(\mathbb E X=0\) and \(\mathbb E X^2=1\).  Write \(P_d\) for the elliptope of
\(d\times d\) correlation matrices, and \(S_d^F\subseteq P_d\) for the correlation
matrices of random vectors whose \(d\) marginal laws are all \(F\).

For an integer \(q\ge 2\), put
\[
g_q=(2q-1)!!,\qquad
\mu_{2q}(F)=\mathbb E|X|^{2q}.
\]

### Theorem 1: finite obstruction from a Gaussian even-moment deficit

Assume \(\mu_{2q}(F)<g_q\) for some \(q\ge2\).  Then there is a finite \(m\) for
which
\[
S_m^F\ne P_m.
\]
More quantitatively, for every integer \(k\ge1\) satisfying
\[
\mu_{2q}(F)
<
g_q\prod_{r=0}^{q-1}\frac{k}{k+2r},
\tag{1}
\]
there is an \(m\times m\) correlation matrix in \(P_m\setminus S_m^F\) with
\[
m\le {k+2q-1\choose 2q}
\quad\text{and rank }k.
\tag{2}
\]
Consequently, \(S_d^F\ne P_d\) for every \(d\ge m\).

Since the product in (1) increases to \(1\) as \(k\to\infty\), every strict
deficit below the Gaussian \(2q\)-th moment eventually gives a finite
correlation obstruction.

### Corollary 2: every platykurtic margin fails in finite dimension

If \(F\) has finite fourth moment
\[
\kappa=\mathbb E X^4<3,
\]
then universal fixed-margin correlation compatibility fails in finite dimension.
Indeed, any integer
\[
k>\frac{2\kappa}{3-\kappa}
\tag{3}
\]
admits an obstruction with
\[
m\le {k+3\choose4}.
\tag{4}
\]

### Corollary 3: a sharp six-dimensional kurtosis-only obstruction

Let \(\rho=1/\sqrt5\), and define
\[
M=
\begin{pmatrix}
1&\rho&\rho&-\rho&\rho&\rho\\
\rho&1&\rho&-\rho&-\rho&-\rho\\
\rho&\rho&1&\rho&\rho&-\rho\\
-\rho&-\rho&\rho&1&\rho&-\rho\\
\rho&-\rho&\rho&\rho&1&\rho\\
\rho&-\rho&-\rho&-\rho&\rho&1
\end{pmatrix}.
\tag{5}
\]
Then \(M\in P_6\), \(\operatorname{rank}M=3\), and for every standardised law
\(F\) with
\[
\mathbb E X^4<\frac95
\tag{6}
\]
one has \(M\notin S_6^F\).

The constant \(9/5\) is sharp as a universal condition based only on the fourth
moment: the standardised uniform law has fourth moment \(9/5\), while every
\(6\times6\) correlation matrix is attainable with uniform margins (in fact,
the exact uniform threshold is dimension \(9\)).

### Corollary 4: exact threshold for a continuum of symmetric Beta margins

Let \(F_a\) be the standardisation of \(\mathrm{Beta}(a,a)\), with
\[
\frac12\le a<1.
\]
Then
\[
S_d^{F_a}=P_d
\quad\Longleftrightarrow\quad
d\le5.
\tag{7}
\]
Thus throughout the whole interval \(1/2\le a<1\), the exact universal
correlation-compatibility threshold is five.  At the boundary \(a=1\), the law
is uniform and the exact threshold jumps to nine.

For every finite \(a>1\), the same family is still platykurtic:
\[
\mathbb E F_a^4
=
3-\frac{6}{2a+3}
=
\frac{3(2a+1)}{2a+3}<3.
\tag{8}
\]
Hence it also fails universal compatibility in some finite dimension.  In
Theorem 1 with \(q=2\), any integer \(k>2a+1\) gives an obstruction with
\(m\le {k+3\choose4}\).

## Proof

### 1. A finite positive cubature for one spherical moment tensor

Let \(U\) be uniform on the unit sphere \(S^{k-1}\subset\mathbb R^k\).  The
symmetric tensor
\[
T=\mathbb E\,U^{\otimes 2q}
\]
belongs to the convex hull of
\(\{u^{\otimes2q}:u\in S^{k-1}\}\).  The vector space of symmetric
\(2q\)-tensors on \(\mathbb R^k\) has dimension
\[
D={k+2q-1\choose2q}.
\]
All tensors \(u^{\otimes2q}\) with \(|u|=1\) lie in the affine hyperplane on
which contraction against the symmetrised \(q\)-fold identity tensor equals
\(|u|^{2q}=1\).  Carathéodory's theorem therefore yields unit vectors
\(a_1,\ldots,a_m\) and positive weights \(w_1,\ldots,w_m\), with
\[
m\le D,\qquad \sum_{j=1}^m w_j=1,
\]
such that
\[
T=\sum_{j=1}^m w_j a_j^{\otimes2q}.
\tag{9}
\]

Contracting (9) against \(x^{\otimes2q}\) gives, for every \(x\in\mathbb R^k\),
\[
\sum_{j=1}^m w_j\langle a_j,x\rangle^{2q}
=
c_{k,q}|x|^{2q},
\tag{10}
\]
where rotational invariance of \(U\) and the standard spherical moment formula
give
\[
c_{k,q}
=
\mathbb E U_1^{2q}
=
\frac{(2q-1)!!}{k(k+2)\cdots(k+2q-2)}.
\tag{11}
\]
The vectors \(a_j\) span \(\mathbb R^k\): otherwise a nonzero vector orthogonal
to all of them would make the left side of (10) zero while the right side is
positive.

### 2. From cubature to a forbidden correlation matrix

Let \(A\) be the \(m\times k\) matrix whose \(j\)-th row is \(a_j^\top\), and
let
\[
M=AA^\top.
\]
Then \(M\in P_m\) and \(\operatorname{rank}M=k\).

A standard rank-decomposition characterisation of fixed-margin correlation
compatibility says that \(M\in S_m^F\) exactly when there exists a random vector
\(V\in\mathbb R^k\) such that
\[
\mathbb EV=0,\qquad \operatorname{Cov}(V)=I_k,\qquad
\langle a_j,V\rangle\sim F\quad(j=1,\ldots,m).
\tag{12}
\]
This characterisation appears for uniform margins in Wang, Wang and Wang
(2019) and in the standardised fixed-margin form in Phillips (2026).

Suppose such a \(V\) exists.  Apply (10) pointwise to \(V\), take expectations,
and use the common marginal law:
\[
\mu_{2q}(F)
=
\sum_{j=1}^m w_j\,\mathbb E\langle a_j,V\rangle^{2q}
=
c_{k,q}\,\mathbb E|V|^{2q}.
\tag{13}
\]
Because \(\operatorname{Cov}(V)=I_k\),
\[
\mathbb E|V|^2=k.
\]
Jensen's inequality applied to \((|V|^2)^q\) yields
\[
\mathbb E|V|^{2q}\ge k^q.
\tag{14}
\]
Combining (11)--(14),
\[
\mu_{2q}(F)
\ge
(2q-1)!!
\prod_{r=0}^{q-1}\frac{k}{k+2r},
\]
contradicting (1).  This proves Theorem 1.  If an \(m\times m\) matrix is
incompatible, adjoining an identity block preserves incompatibility, which
gives all higher dimensions.

For \(q=2\), the lower bound becomes \(3k/(k+2)\); rearranging
\(\kappa<3k/(k+2)\) gives (3), proving Corollary 2.

### 3. The six icosahedral directions

Let \(\varphi=(1+\sqrt5)/2\), and take one representative from each antipodal
pair of vertices of a regular icosahedron:
\[
(0,1,\varphi),\ (0,-1,\varphi),\
(\varphi,0,1),\ (\varphi,0,-1),\
(1,\varphi,0),\ (-1,\varphi,0),
\]
normalised to unit length.  Call the resulting unit vectors
\(a_1,\ldots,a_6\).  Their Gram matrix is exactly (5); its eigenvalues are
\(2,2,2,0,0,0\), so it lies in \(P_6\) and has rank three.

These directions satisfy the exact quartic identity
\[
\sum_{j=1}^6\langle a_j,x\rangle^4
=
\frac65|x|^4.
\tag{15}
\]
If (5) were in \(S_6^F\), the characterisation (12) would give a
three-dimensional \(V\) with identity covariance and all six projected laws
equal to \(F\).  Averaging (15) and taking expectations gives
\[
\mathbb E X^4=\frac15\mathbb E|V|^4
\ge \frac15(\mathbb E|V|^2)^2
=\frac95.
\]
This proves Corollary 3.  Phillips (2026) used the same icosahedral identity for
the arcsine law; the observation here is that the argument depends only on the
common fourth moment.

### 4. Symmetric Beta margins

For the standardisation \(F_a\) of \(\mathrm{Beta}(a,a)\), the Pearson
kurtosis is (8).  Hence \(a<1\) is equivalent to
\(\mathbb E F_a^4<9/5\).  Corollary 3 therefore gives failure in dimension six,
and hence in every larger dimension.

Devroye and Letac (2015, Section 4) proved that for every \(a\ge1/2\), every
correlation matrix of dimension at most five is attainable with
\(\mathrm{Beta}(a,a)\) margins.  Combining their positive result with the
six-dimensional obstruction proves (7).  For \(a=1\), the margin is uniform;
Wang and Zhang (2026) proved that the exact threshold there is dimension nine.

## Relation to prior literature

Devroye and Letac established universal compatibility for symmetric
\(\mathrm{Beta}(a,a)\) margins through dimension five and for uniform margins
through dimension nine.  Wang, Wang and Wang developed the rank-decomposition
viewpoint and gave the first high-dimensional incompatibility result for
uniform margins.  Wang and Zhang recently completed the uniform classification
with exact threshold nine.  Phillips recently used quartic identities to give
short incompatibility proofs for uniform margins and, separately, the arcsine
law; the latter settled the \(a=1/2\) endpoint of (7).

Theorem 1 isolates a more general mechanism: a deficit in any even moment
relative to the corresponding Gaussian moment can be converted, by a finite
positive spherical cubature, into a finite fixed-margin correlation
obstruction.  Corollaries 2--4 give a quantitative platykurtic criterion, a
six-dimensional fourth-moment boundary, and an exact continuum of symmetric
Beta thresholds.

## Limitations

The moment condition is sufficient, not necessary.  The result does not
classify margins whose relevant even moments equal or exceed the Gaussian
moments.  The Carathéodory bound in (2) is a general existence bound and is not
claimed to be the smallest possible obstruction dimension.  The six-dimensional
matrix (5) is much sharper when the fourth moment is below \(9/5\).

For symmetric \(\mathrm{Beta}(a,a)\) with \(a>1\), the finite-dimensional
obstruction supplied here is not an exact dimensional threshold.  Apart from
the uniform point \(a=1\), no exact classification for that range is claimed.

Originality is asserted only to the best of our knowledge.  The fixed-margin
correlation literature, copula-compatibility literature, and
Carathéodory/Tchakaloff cubature literature contain closely related ingredients;
the literature review described in `REVIEW.md` did not locate the combined
moment-deficit theorem or the Beta-family consequence (7).

## References

1. L. Devroye and G. Letac, *Copulas with prescribed correlation matrix*,
   Séminaire de Probabilités XLVII, Lecture Notes in Mathematics 2137,
   585--601 (2015). DOI: 10.1007/978-3-319-18585-9_25.
2. B. Wang, R. Wang and Y. Wang, *Compatible matrices of Spearman's rank
   correlation*, Statistics & Probability Letters 151, 67--72 (2019).
   DOI: 10.1016/j.spl.2019.03.015.
3. R. Wang and Z. Zhang, *The exact dimensional threshold for Spearman
   rank-correlation compatibility*, arXiv:2609.16278 (2026).
4. C. Phillips, *Two short proofs of incompatibility for correlation matrices*,
   arXiv:2609.14610 (2026).
5. W. Hürlimann, *A closed-form universal trivariate pair-copula*, Journal of
   Statistical Distributions and Applications 1, 7 (2014).
   DOI: 10.1186/2195-5832-1-7.
