# Projective-subline rigidity and optimal three-helper availability in a rank-four code family

## Finding

Let \(p\) be an odd prime, \(m\ge 2\), \(1\le s<m\), \(q=p^m\), \(r=p^s\), \(\ell=\gcd(m,s)\), and \(h=p^\ell\). On the \(q+1\) coordinates of \(\mathbb P^1(\mathbb F_q)\), let \(\mathcal E\) be the four-dimensional linear code over \(\mathbb F_{q^2}\) with generator columns
\[
v(t)=(1,t,t^r,t^{r+1})^{\mathsf T}\quad(t\in\mathbb F_q),\qquad v(\infty)=(0,0,0,1)^{\mathsf T}.
\]
This is monomially equivalent over \(\mathbb F_{q^2}\) to the length-\(q+1\) four-dimensional unit-circle code of Xiong, Wang, Zheng, and Ji (2026), whose columns are the powers with exponents \(\pm(r-1)/2\) and \(\pm(r+1)/2\).

**Subline rigidity.** Every weight-\(4\) dual support is precisely a four-subset of a projective \(\mathbb F_h\)-subline of \(\mathbb P^1(\mathbb F_q)\), and every such four-subset occurs. Every minimum-weight codeword of \(\mathcal E\) has as its zero set exactly one such subline, and every subline occurs. These are the classical Witt spherical-geometry blocks of the unique projective-subline construction, not merely designs with equal numerical parameters. In particular, the complementary minimum-support design in the cyclic \(\mathbb F_q\)-code of Wang, Tang, and Ding (2022) is isomorphic to the Witt spherical geometry design; this settles the specific isomorphism question posed as their Open Problem 18.

**Exact local repair and availability.** If a target coordinate is mapped to \(\infty\) by a projectivity, its minimal three-helper recovery sets are exactly the distinct triples lying on an affine \(\mathbb F_h\)-line in \(\mathbb F_q\). The number of these sets at every target is
\[
\frac{q(q-1)(h-2)}6.
\]
For \(p=3\), the maximum number of *pairwise disjoint* three-helper recovery sets at every coordinate is exactly
\[
\boxed{q/3}.
\]
There are at least \((q-1)/2\) different explicitly constructible complete disjoint repair schedules, indexed by directions of affine \(\mathbb F_3\)-lines. These are separate schedules, not a claim to classify all optimal schedules.

## Assumptions and scope

The code is linear over \(\mathbb F_{q^2}\); recovery means expression of one coordinate as a linear combination of three distinct other coordinates. Only **minimum-size** recovery sets arising from weight-\(4\) dual words are classified. The affine-line assertion uses coordinates after an allowed projective relabeling and nonzero column scalings; the resulting code has identical dual-support incidence and disjoint repair availability. The stronger exact availability formula requires \(p=3\); no optimal disjoint-availability claim is made here for other odd primes.

A projective \(\mathbb F_h\)-subline means an image of \(\mathbb P^1(\mathbb F_h)\subset\mathbb P^1(\mathbb F_q)\) under \(\operatorname{PGL}_2(\mathbb F_q)\). Every three distinct projective points lie on exactly one such subline, since \(\operatorname{PGL}_2\) acts sharply three-transitively on ordered triples on a projective line. Distinct lines in the affine space \(\mathbb F_q\) over \(\mathbb F_h\) have exactly \(h\) points.

## Proof

**1. Reduction to a projective evaluation representation.** Write the unit-circle generator columns of the 2026 code as
\[
(y^{(r-1)/2},y^{(r+1)/2},y^{-(r-1)/2},y^{-(r+1)/2})^{\mathsf T},\qquad y^{q+1}=1.
\]
Scaling the column by \(y^{(r+1)/2}\) and reordering rows produces \((1,y,y^r,y^{r+1})^{\mathsf T}\). Select \(\omega\in\mathbb F_{q^2}\setminus\mathbb F_q\). The fractional-linear substitution \(y=(t-\omega)/(t-\omega^q)\) bijects \(\mathbb P^1(\mathbb F_q)\) with the unit circle. Clearing denominators by the nonzero scalar \((t-\omega^q)^{r+1}\) changes the four evaluation functions to the four products of \(t-\omega\), \(t-\omega^q\), and their \(r\)-th powers. Their coefficient change-of-basis matrix is the tensor product of two invertible two-by-two matrices (one Frobenius-twisted), hence invertible. This yields \(v(t)\) and, by taking leading coefficients at infinity, \(v(\infty)\).

For every \(\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{GL}_2(\mathbb F_q)\), the transformed column \((ct+d)^{r+1}v((at+b)/(ct+d))\) is obtained from \(v(t)\) by an invertible tensor-product row transformation. The homogeneous version handles any exceptional denominator and infinity. Thus \(\operatorname{PGL}_2(\mathbb F_q)\) preserves the dependence pattern of generator columns.

**2. The exact four-column dependence test.** By projective invariance, fix one of four distinct columns to be \(\infty\) and write the other three as distinct \(a,b,c\in\mathbb F_q\). Four columns are dependent precisely when
\[
\det\begin{pmatrix}1&1&1\\a&b&c\\a^r&b^r&c^r\end{pmatrix}=0
\quad\Longleftrightarrow\quad
\left(\frac{b-a}{c-a}\right)^r=\frac{b-a}{c-a}.
\]
The fixed field of the \(r\)-Frobenius on \(\mathbb F_q\) is exactly \(\mathbb F_h\), since \(\gcd(m,s)=\ell\). Hence the three finite points lie on a common affine \(\mathbb F_h\)-line. Projective covariance shows that four arbitrary distinct coordinates are dependent exactly when they lie on a common projective \(\mathbb F_h\)-subline.

Any three columns are independent. When one is infinity, the first two rows of the finite columns distinguish them and the last row distinguishes infinity. For three finite points, if the determinant of their \((1,t,t^r)\)-rows is nonzero, independence is immediate. If it vanishes, the points have the form \(t=a+v\lambda\) for three distinct \(\lambda\in\mathbb F_h\), with \(v\ne0\). On these points, \(1,t,t^{r+1}\) span the same evaluations as \(1,\lambda,\lambda^2\), because \(t^r=a^r+v^r\lambda\) and the quadratic coefficient in \(t^{r+1}\) equals \(vv^r\ne0\). Their Vandermonde determinant is nonzero. Thus a dependent four-set has a unique dependence relation, all four coefficients nonzero, and yields a weight-\(4\) dual word. Conversely, every weight-\(4\) dual word gives such a four-set.

**3. Minimum-word zero sets and the older open isomorphism problem.** Any three distinct zeros of a nonzero codeword determine a unique \(\mathbb F_h\)-subline; every further zero must belong to that subline by the four-column dependence criterion. Therefore every nonzero codeword has at most \(h+1\) zero coordinates. For any subline, its generator columns span exactly dimension three (three are independent; every fourth is dependent); a nonzero annihilating row exists and has no further zeros. Therefore the minimum Hamming distance is \(q-h\), and the minimum-word zero sets are exactly the projective \(\mathbb F_h\)-sublines.

The \(\mathbb F_q\)-cyclic trace code of Wang, Tang, and Ding uses the same four paired unit-circle monomials, with coefficients constrained to the Frobenius-fixed trace form. Scalar extension of its four-dimensional \(\mathbb F_q\)-coefficient space spans the same four-dimensional \(\mathbb F_{q^2}\)-row space: the maps \(a\mapsto(a,a^q)\) and \(b\mapsto(b,b^q)\) each have full two-dimensional span over \(\mathbb F_{q^2}\), because \(a\mapsto a^q\) is not multiplication by a fixed scalar. Every minimum-zero set of that cyclic code must therefore be one of the projective sublines proved above. Their Theorem 13 independently proves that the cyclic-code minimum-zero sets form a Steiner system with one block through every triple. Since projective sublines also form such a system and every cyclic-code block is among them, the two block families coincide. This supplies the asserted isomorphism, without asserting that the numerical Steiner parameters or the abstract design construction are new.

**4. Exact repair set census.** Fix a target and send it to infinity. A weight-\(4\) dual relation through infinity yields three helpers precisely when the helpers belong to one affine \(\mathbb F_h\)-line. There are \(q(q-1)/(h(h-1))\) distinct affine \(\mathbb F_h\)-lines and each contributes \(\binom h3\) distinct triples. Every three noncollinear helpers cannot be a recovery triple by the dependence criterion. This proves the exact count \(q(q-1)(h-2)/6\).

For \(p=3\), regard \(\mathbb F_q\) as an \(m\)-dimensional vector space over \(\mathbb F_3\). For each one-dimensional \(\mathbb F_3\)-direction \(\langle v\rangle\), the affine lines \(a+\{0,v,-v\}\) partition \(\mathbb F_q\) into exactly \(q/3\) disjoint triples. Since \(\mathbb F_3\subseteq\mathbb F_h\), each triple is a valid local recovery set. There are \((q-1)/2\) directions, furnishing that many different full schedules. Every recovery set consumes exactly three helpers from the available \(q\) coordinates, so more than \(q/3\) disjoint sets are impossible. Equality follows.

## Verification

The embedded standalone file `verify.py` implements finite-field arithmetic using irreducible-polynomial residue fields, exact Gaussian elimination, projective normalization, and exhaustive four-coordinate tests. For \((p,m,s)=(3,2,1),(5,2,1),(3,3,1),(3,3,2)\), it checks all \(56{,}110\) four-subsets, their predicted subline criterion, per-coordinate repair counts, and direction-based line partitions. The recorded execution in `verification_output.txt` ends with `SUBLINE_REPAIR_CENSUS_OK`. These finite checks corroborate but do not replace the all-parameter proof above.

For reference the number of projective sublines equals \(q(q^2-1)/(h(h^2-1))\), and the number of distinct dual weight-\(4\) supports equals \(q(q^2-1)(h-2)/24\); both follow from unique subline containment of every three projective points. These incidence counts are derivable from the previously known design parameters; their novelty is **not** claimed separately.

## Relationship to prior work

Xiong, Wang, Zheng, and Ji (2026) constructed the unit-circle code, proved several weight-support three-design statements, and established all-symbol locality three. This result identifies the *actual* weight-four support hypergraph, not merely its design parameters or existence of repair alternatives. Wang, Tang, and Ding (2022), Theorem 13, had already obtained the corresponding cyclic-code Steiner system and dual weight-four design parameters and explicitly posed the Witt spherical-design isomorphism question as Open Problem 18. The subline model answers that question and supplies the exact coordinatewise, pairwise-disjoint repair availability in characteristic three.

The finite-projective-line subline system and affine line parallelisms are classical structures. The claimed contribution is their explicit identification with the given coding families and the consequent exact repair incidence/availability theorem, not the discovery of the classical designs themselves.

## Limitations

The 2022 code is over \(\mathbb F_q\), while the 2026 extension is over \(\mathbb F_{q^2}\); the subline identification applies to both through the trace-span argument, whereas the explicit storage-recovery interpretation is stated for the latter. No generalized higher-size recovery-set enumeration, robustness under failures, or decoding-complexity guarantee is established. The number of complete directional schedules is a constructive lower bound, not an exhaustive classification. Equivalent implicit identification in earlier geometric coding literature remains a priority risk; independent verification has not occurred.

## References

1. Shiyan Xiong, Xiaoqiang Wang, Dabin Zheng, Qinqin Ji, *Infinite families of 3-designs from linear and nonlinear codes*, arXiv:2609.15525 (first public submission 2026-09-14), https://arxiv.org/abs/2609.15525.
2. Xiaoqiang Wang, Chunming Tang, Cunsheng Ding, *Infinite families of cyclic and negacyclic codes supporting 3-designs*, arXiv:2207.07262 (2022), especially Theorem 13, Remark 17 and Open Problem 18, https://arxiv.org/abs/2207.07262.
