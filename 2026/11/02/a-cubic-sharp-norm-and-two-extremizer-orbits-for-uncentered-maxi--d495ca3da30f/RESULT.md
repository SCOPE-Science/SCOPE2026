# A cubic sharp norm and two extremizer orbits for uncentered maximal averages on the triangular prism

## Finding

Let \(G=C_3\square K_2\) be the simple unweighted triangular-prism graph, with counting measure and the shortest-path metric. For a real function \(f\) on its six vertices, define the uncentered Hardy–Littlewood maximal operator by
\[
\widetilde M f(v)=\max_{\substack{c\in V(G),\ r\in\{0,1,2\}\\v\in B(c,r)}}\frac{1}{|B(c,r)|}\sum_{u\in B(c,r)}|f(u)|.
\]
The exact, attained strong Hilbert-space norm is
\[
\boxed{\|\widetilde M\|_{\ell^2\to\ell^2}=\sqrt{\lambda_*}=1.278110667051124\ldots,}
\]
where \(\lambda_*=1.633566877229869\ldots\) is the unique real root in \((1.63356,1.63357)\) of
\[
\boxed{64\lambda^3-124\lambda^2+33\lambda-2=0.}
\]
Put
\[
a=\frac{\lambda_*-1}{\lambda_*},\quad
b=\frac{3\lambda_*-1}{\lambda_*(8\lambda_*-1)},\quad
c=\frac{3\lambda_*-1}{\lambda_*(16\lambda_*-1)}.
\]
Then \(0<c<b<a<1\), with respective approximate values \(a=0.3878426320104\), \(b=0.1978568756258\), and \(c=0.0949928781923\). Every nonzero real extremizer is obtained by independent coordinate sign changes and positive scaling from one of **exactly eighteen labeled nonnegative rays**: choose either triangle layer, choose two vertices of that layer to have value \(1\), give the third vertex value \(a\), and give one arbitrarily chosen vertex of the opposite layer value \(b\) and its other two vertices value \(c\). Conversely, all eighteen rays attain the norm.

The automorphism group has exactly two orbits on these rays. There are six rays where the vertex carrying \(b\) is vertically matched to the vertex carrying \(a\), and twelve rays where it is matched to a vertex carrying \(1\).

Moreover, the centered operator \(M\), defined with \(c=v\) fixed in each ball, is strictly weaker in strong \(\ell^2\) norm:
\[
\boxed{\|M\|_{\ell^2\to\ell^2}^{\,2}<\frac32<\frac{81}{50}<\|\widetilde M\|_{\ell^2\to\ell^2}^{\,2}.}
\]
The strict centered estimate is checked independently, without relying on a previously recorded exact centered constant.

## Assumptions and scope

Label the two triangle layers \(0,1,2\) and \(3,4,5\). Vertices within each layer are mutually adjacent; the three remaining edges join \(j\) to \(j+3\) for \(j=0,1,2\). All edges have unit length. A ball is closed in the shortest-path metric, and averages are with respect to unweighted counting measure. The norm is taken on the six-dimensional **real** \(\ell^2\) space; because the maximal operator uses absolute input values, arbitrary independent coordinate sign changes do not affect it.

The graph has diameter two. Its distinct ball sizes are \(1\), \(4\), and \(6\). For each evaluation vertex \(v\), exactly six distinct balls contain \(v\): its singleton; the four radius-one balls centered at \(v\) and its three neighbors; and the whole vertex set. Repeated descriptions of the same ball are identified. The parameter \(r\) may equivalently range over all nonnegative real radii.

## Proof

**1. Exact finite linearization.** For each vertex choose one of its six containing balls, independently. A six-tuple of choices \(s\) determines a nonnegative \(6\)-by-\(6\) averaging matrix \(A_s\), whose \(v\)-th row is the normalized indicator of the chosen ball. For every nonnegative input \(x\),
\[
\|\widetilde Mx\|_2^2=\max_s\|A_sx\|_2^2.
\]
There are exactly \(6^6=46656\) matrices. Since each \(A_s\) is entrywise nonnegative, replacing a maximizing singular vector by its componentwise absolute value cannot decrease \(\|A_sx\|_2\). Interchanging two finite or compact maxima therefore gives
\[
\|\widetilde M\|_{2\to2}^{\,2}=\max_s\lambda_{\max}(A_s^{\mathsf T}A_s).
\]
This identity is exact; there is no assumption that a maximizing selection is known in advance.

**2. Exhaustive spectral separation with integer arithmetic.** Let \(R_s=12A_s\); this is an integer matrix, because all ball sizes divide twelve. For each of the \(46656\) selections form the integer symmetric matrix
\[
Q_s=11664I-50R_s^{\mathsf T}R_s.
\]
By Sylvester's criterion, \(Q_s\) is positive definite precisely when every leading principal minor is strictly positive. Positive definiteness implies
\[
\lambda_{\max}(A_s^{\mathsf T}A_s)<\frac{81}{50}.
\]
The attached fully standalone integer-arithmetic verifier constructs all six balls at every vertex, enumerates all \(46656\) choices, and checks those principal minors by fraction-free elimination, with exact-division assertions at every step. Exactly **46638** matrices satisfy strict positive definiteness; the remaining **18** are exhaustively enumerated. These 18 are precisely the following combinatorial selections: choose a distinguished triangle layer, retain singleton averages at two of its vertices, choose one of the three radius-one balls centered in that layer for the remaining vertex, and at each vertex in the opposite layer choose the radius-one ball centered at its vertically matched vertex of the distinguished layer. Thus the count is \(2\cdot3\cdot3=18\). No untested cases are hidden in this step.

**3. The exceptional spectrum.** One representative exceptional matrix, with its entries multiplied by four, is
\[
4A_*=\begin{pmatrix}
4&0&0&0&0&0\\
0&4&0&0&0&0\\
1&1&1&1&0&0\\
1&1&1&1&0&0\\
1&1&1&0&1&0\\
1&1&1&0&0&1
\end{pmatrix}.
\]
An exact determinant calculation yields
\[
\det(zI-(4A_*)^{\mathsf T}(4A_*))
=z(z-16)(z-1)(z^3-31z^2+132z-128).
\]
All 18 exceptional Gram matrices have this polynomial and, more strongly, are obtained from the displayed Gram matrix by simultaneous permutations of rows and columns. The verifier establishes the polynomial via the integer Faddeev–LeVerrier recurrence and checks the coordinate permutations. These *matrix* permutations need not be graph automorphisms; this is why two different graph-automorphism orbits can share one exact singular value.

For \(z=16\lambda\), the cubic factor becomes the displayed equation \(64\lambda^3-124\lambda^2+33\lambda-2=0\). That cubic has three real roots, one in \((0,1/10)\), one in \((1/5,1/4)\), and one in \((1.63356,1.63357)\), by opposite exact rational signs at each interval's endpoints. Its derivative is strictly positive for \(\lambda\ge81/50\), as is verified directly. Consequently the last root is the largest eigenvalue after the scale change, and it exceeds \(81/50\). All nonexceptional choices are strictly below this threshold, so the displayed value is the global norm.

**4. Explicit Perron vector and strict activity.** With \(\lambda=\lambda_*\) and \(a,b,c\) as stated, let \(x=(1,1,a,b,c,c)^{\mathsf T}\). Put
\[
d=\frac{2+a+b}{4}=\frac{2(3\lambda-1)}{8\lambda-1},\qquad
e=\frac{2+a+c}{4}=\frac{4(3\lambda-1)}{16\lambda-1}.
\]
Direct multiplication gives \(A_*x=(1,1,d,d,e,e)^{\mathsf T}\), and
\[
A_*^{\mathsf T}A_*x
=\bigl(1+(d+e)/2,\ 1+(d+e)/2,\ (d+e)/2,\ d/2,\ e/4,\ e/4\bigr)^{\mathsf T}.
\]
The identities \(d=2\lambda b\), \(e=4\lambda c\), and
\[
\frac{d+e}{2}-(\lambda-1)
=-\frac{2(64\lambda^3-124\lambda^2+33\lambda-2)}{(8\lambda-1)(16\lambda-1)}=0
\]
therefore establish \(A_*^{\mathsf T}A_*x=\lambda x\). Every coordinate is strictly positive, so the Perron eigenvalue is simple and the nonnegative maximizing ray is unique for this matrix. The other 17 matrices inherit this eigenvector statement by the verified coordinate permutations.

For all 18 exceptional matrices, each chosen averaging ball uniquely maximizes its output coordinate at the corresponding positive eigenvector. This can also be seen from \(0<c<b<a<1\) and the explicit averages above. For complete independent coverage, the verifier bounds \(\lambda\) in the exact rational isolating interval, propagates rational intervals for \(a,b,c\), and checks **540 strict comparisons**: five competing balls at each of six vertices in each of eighteen configurations. Thus all eighteen positive eigenvectors are actual nonlinear maximal-operator extremizers, not merely singular vectors of inactive selections.

Conversely, any nonzero input attaining the nonlinear norm must select one of those eighteen spectral-maximizing matrices. The absolute-value input then lies on its unique nonnegative top singular ray, so the described eighteen rays exhaust equality. The graph automorphisms independently permute the three vertical pairs and interchange the two layers; they preserve whether the \(b\)-vertex is vertically paired with the \(a\)-vertex, giving the asserted two orbit sizes \(6\) and \(12\).

**5. Centered versus uncentered.** Fixing a ball's center at its evaluation vertex leaves only three choices per row, hence \(3^6=729\) centered matrices. Applying the same exact integer Sylvester test to the positive-definiteness of \(432I-2R_s^{\mathsf T}R_s\) for all 729 centered selections proves \(\|M\|_{2\to2}^{\,2}<3/2\). Since \(3/2<81/50<\lambda_*\), the strict separation follows without invoking any prior centered computation.

## Verification

The complete reproducible certificate is `verify_uncentered_prism.py`. It uses Python's standard library only, constructs the graph and ball family from first principles, and uses exact integers and rational fractions. Run `python verify_uncentered_prism.py` from the directory containing that script. Expected output is:

```text
CERTIFICATE_OK selections=46656 strict=46638 exceptional=18
CERTIFICATE_OK characteristic=[1,-48,675,-2868,4288,-2048,0]
CERTIFICATE_OK active_competitor_inequalities=540 rays=18 orbit_types=6+12
CERTIFICATE_OK centered_strict_lt_3/2=729 uncentered_gt_81/50
```

The exhaustive finite certificate is a proof here because the domain is exactly the finite set of all permitted averaging selections, not a sample from a larger or infinite family. All arithmetic in the spectral exclusion and root isolation is exact; no floating-point threshold is used. The analytic reduction, positivity argument, and eigenvector identities explain why the finite certificate establishes the claimed nonlinear norm and complete equality classification.

## Relationship to prior work

Soria and Tradacete (arXiv:1410.6204, first public October 22, 2014) introduce finite-graph centered maximal norms, establish general \(\ell^p\) comparisons and calculate special graph classes; their exact general extremal bound concerns \(0<p\le1\) and does not imply the uncentered strong \(\ell^2\) constant here. González-Riquelme and Madrid (arXiv:2005.03146) explicitly define uncentered graph-ball operators but obtain sharp strong \(\ell^2\) values for complete graphs and stars in the centered setting, not this graph. González-Riquelme, Kovač and Madrid (arXiv:2603.12462) investigate graph maximal *variation* and enumerate up to five vertices; their different seminorm and graph domain do not cover this six-vertex uncentered Hilbert calculation.

The exact centered triangular-prism problem is distinct and does not imply the uncentered constant or the two-orbit equality classification; the present proof independently establishes a strict centered–uncentered separation. Some broader finite-graph computations might encode this special case without an indexed title, which remains a publication-priority risk. No complete claim of priority over all unpublished or unindexed work is made.

## Limitations

The theorem concerns precisely the unweighted triangular prism with counting measure, real \(\ell^2\), and graph-distance balls. It does not imply corresponding exact norms for larger prisms, other graph products, weighted measures, other exponents, or the uncentered variation seminorm. The numerical decimals are illustrative; the defining cubic, the rational isolation interval, and the exhaustive integer certificate supply the exact content. The mathematical statement has not undergone independent scientific validation.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204, initially public October 22, 2014. https://arxiv.org/abs/1410.6204
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146, May 6, 2020. https://arxiv.org/abs/2005.03146
3. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462, March 12, 2026. https://arxiv.org/abs/2603.12462
