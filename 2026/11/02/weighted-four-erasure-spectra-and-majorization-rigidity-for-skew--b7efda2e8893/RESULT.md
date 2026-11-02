# Weighted four-erasure spectra and majorization rigidity for skew-conference frames

## Finding

For any existing real skew-symmetric conference matrix of order \(n\ge8\), the associated half-dimensional complex Parseval equiangular tight frame has **exactly two spectra for four arbitrary positive erasure weights**, independent of both the choice and assignment of these weights to coordinates. A four-site spectrum is the spectrum of the weighted erased-coefficient operator, not of a reconstruction using a newly optimized dual frame.

More precisely, write \(q=n-1\) and let \(C\) be an \(n\)-by-\(n\) real matrix satisfying \(C^\mathsf T=-C\), \(C_{ii}=0\), \(C_{ij}\in\{-1,1\}\) for \(i\ne j\), and \(CC^\mathsf T=qI\). Set \(P=(I+iC/\sqrt q)/2\), and take any \(n\)-by-\(n/2\) matrix \(V\) with \(VV^*=P\) and \(V^*V=I\). For a four-subset \(S=\{s_1,s_2,s_3,s_4\}\) and positive weights \(w=(w_1,w_2,w_3,w_4)\), let \(D_{S,w}\) be diagonal with entries \(w_j\) at \(s_j\) and zero elsewhere. Define the positive weighted erasure operator \(T_{S,w}=V^*D_{S,w}V\).

The four positive eigenvalues of \(2T_{S,w}\) are exactly the roots of
\[
\chi_{\tau,w}(x)=x^4-e_1(w)x^3+(1-q^{-1})e_2(w)x^2-(1-3q^{-1})e_3(w)x+(1-6q^{-1}+\tau q^{-2})e_4(w),
\]
where \(e_j(w)\) is the elementary symmetric polynomial of degree \(j\) in the four weights and
\[
\tau=\operatorname{Pf}(C_S)^2\in\{1,9\}.
\]
For \(n>8\), the other \(n/2-4\) eigenvalues of \(2T_{S,w}\) are zero. Both types occur. Their respective numbers among the \(\binom n4\) subsets are
\[
N_1=\frac{n(n-1)(n-2)(n-4)}{32},\qquad
N_9=\frac{n^2(n-1)(n-2)}{96}.
\]
The unweighted four-subset count is a standard consequence of skew-conference spectral identities and is included to make the weighted classification quantitative, not presented as a separate new result.

Let \(L_\tau(w)\) denote the largest real zero of \(\chi_{\tau,w}\). For every strictly positive weight vector,
\[
L_1(w)>L_9(w).
\]
Thus the **exact adversarial weighted four-erasure norm**, over all supports and placements of the same weights, is \(\frac12L_1(w)\). It is symmetric and Schur-convex in \(w\): for positive vectors of the same sum, \(w\succcurlyeq v\) (majorization) implies \(L_1(w)\ge L_1(v)\), and likewise for the favorable class \(L_9\). In particular, for every \(W>0\),
\[
\boxed{\displaystyle\min_{w_j>0,\ \sum_jw_j=W}\ \max_{|S|=4}\|T_{S,w}\|=\frac W8\left(1+\frac{1+\sqrt2}{\sqrt{n-1}}\right),}
\]
attained by the equal allocation \(w_1=w_2=w_3=w_4=W/4\). The maximum ranges over supports and any assignment of these four weights. For a uniformly chosen four-subset, the norm has the two-point distribution
\[
\mathbb P\!\left(\|T_{S,w}\|=L_1(w)/2\right)=\frac{3(n-4)}{4(n-3)},\quad
\mathbb P\!\left(\|T_{S,w}\|=L_9(w)/2\right)=\frac n{4(n-3)}.
\]
The conclusion remains valid with the physically attenuating weights \(0<w_j\le1\); arbitrary positive weights simply extend the operator statement.

## Assumptions and scope

The order \(n\) is an integer at least eight **for which such a real skew-conference matrix actually exists**. No existence assertion for other orders is made. The base field is complex; \(V\) is a Parseval analysis matrix, so its columns are orthonormal and its rows form the frame vectors. The operator \(T_{S,w}\) acts on \(\mathbb C^{n/2}\); its norm is the canonical-dual reconstruction-error norm of a weighted four-coordinate loss if weights model loss fractions. All four weights must be positive for the strict two-type inequality. At zero weights the formulas extend continuously, but the two spectra may coalesce. Majorization is with equal total weight.

The claim concerns a **fixed four-site weight multiset** allowed to vary in placement. It does not assert optimality across all frames, across choice of dual frame, or across loss patterns with more than four sites. Unweighted partial spectral information and the underlying frame construction are not new.

## Proof

**1. Projection and reduction.** Since \(C^\mathsf T=-C\) and \(CC^\mathsf T=qI\), one has \(C^2=-qI\), so \((iC/\sqrt q)^2=I\). Its trace is zero, hence its eigenvalues \(+1,-1\) occur equally often. This proves \(P^2=P=P^*\) and \(\operatorname{rank}P=n/2\). The nonzero eigenvalues of \(2V^*D_{S,w}V\) are those of the positive four-by-four matrix
\[
H_{S,w}=D_w^{1/2}(I_4+iC_S/\sqrt q)D_w^{1/2},\quad D_w=\operatorname{diag}(w_1,w_2,w_3,w_4).
\]
They are all strictly positive: for any four-subset, the Hermitian matrix \(iC_S\) has characteristic polynomial \(t^4-6t^2+\tau\) with \(\tau=1\) or \(9\). Its largest possible eigenvalue magnitude is \(1+\sqrt2<\sqrt7\le\sqrt q\), so \(I_4+iC_S/\sqrt q\) is positive definite.

**2. Principal minors give the complete weighted spectrum.** Any one-by-one principal minor of \(I+iC_S/\sqrt q\) is \(1\). Any two-by-two principal minor is \(1-1/q\). Every three-by-three principal minor is \(1-3/q\), since an order-three real skew-sign matrix has eigenvalues \(0,\pm i\sqrt3\). The four-by-four determinant is \(1-6/q+\tau/q^2\), because \(iC_S\) has eigenvalues in opposite pairs and its determinant is \(\operatorname{Pf}(C_S)^2\). Multiplying the principal minors of order \(j\) by the corresponding products of \(w_i\) and summing yields the elementary characteristic coefficients of \(H_{S,w}\). This proves the displayed quartic, including its complete symmetry under permutations of the weights. The Pfaffian is \(C_{12}C_{34}-C_{13}C_{24}+C_{14}C_{23}\), a sum of three signs, so \(\tau\in\{1,9\}\).

**3. Both types and their exact counts.** The global characteristic polynomial of \(C\) is \((t^2+q)^{n/2}\). Its coefficient of \(t^{n-4}\) equals the sum of determinants of all its order-four principal submatrices, hence
\[
N_1+9N_9=\binom{n/2}{2}q^2,\qquad N_1+N_9=\binom n4.
\]
Solving gives the displayed integer formulas. Both are positive for every allowed \(n\ge8\).

**4. Strict hierarchy of the weighted types.** The two quartics differ only in their constant terms:
\[\chi_{1,w}(x)=\chi_{9,w}(x)-8e_4(w)/q^2.\]
Since \(e_4(w)>0\), the first polynomial is strictly negative at the largest eigenvalue \(x=L_9(w)\) of the second. It tends to positive infinity as \(x\to+\infty\), so it has a strictly larger real zero. This proves \(L_1(w)>L_9(w)\) and the exact worst-case class, with no numerical root search.

**5. Majorization and sharp equal-weight minimax.** Fix any four-subset of a given type. For fixed frame vectors \(f_{s_j}\), the map
\[
w\longmapsto\lambda_{\max}\!\left(2\sum_{j=1}^4w_j f_{s_j}f_{s_j}^*\right)
\]
is convex because it is a largest eigenvalue of a Hermitian matrix affine in \(w\). Step 2 proves this map is invariant under **all permutations** of \(w\), even though the frame vectors themselves are not generally permutable by a frame symmetry. A symmetric convex function is Schur-convex: if \(v\) lies in the convex hull of permutations of \(w\), then \(L_\tau(v)\le L_\tau(w)\). Every positive vector of sum \(W\) majorizes \((W/4,W/4,W/4,W/4)\). For equal weights, the larger eigenvalue of \(iC_S\) in the \(\tau=1\) type is \(1+\sqrt2\), since its squared eigenvalues are \(3\pm2\sqrt2\). Hence \(L_1(W/4,\ldots,W/4)=(W/4)(1+(1+\sqrt2)/\sqrt q)\), and multiplying by \(1/2\) proves the sharp minimax formula. Divide the counts in Step 3 by \(\binom n4\) to obtain the probability law. This completes the proof for every existing order and all strictly positive real weights.

## Verification

The accompanying `check_weighted_skew.py` constructs Paley skew-conference matrices of orders \(8,12,20\) directly from quadratic characters. For every four-subset, it checks \(\tau\in\{1,9\}\) and the exact type counts; for a representative of each type, it computes the characteristic polynomial symbolically with nonuniform weights \((1,2,3,5)\), compares it to the theorem's quartic exactly using SymPy, and checks numerical eigenvalue positivity and strict norm ordering. The executed checker prints `WEIGHTED_SKEW_CONFERENCE_FOUR_ERASURE_OK`. These finite checks independently test the formulas but do not establish the all-order assertion; Steps 1–5 supply the proof for arbitrary existing matrices.

## Relationship to prior work

Bodmann and Paulsen's *Frames, Graphs and Erasures* (first public 2004-06-08) establishes frame-erasure error operators and the unweighted uniform-frame perspective. Hoffman and Solazzo's *Complex Equiangular Tight Frames and Erasures* (2011-07-08) identifies the complex three-erasure-uniform skew-conference class and studies unweighted erasures; this class is the starting geometric object, not a new construction. Cheng, Lv, and Sun's *Frames of uniform subframe bounds with applications to erasures* treats cardinality-uniform subframe properties and unweighted erasure bounds. Fickus and coauthors study erasure-robust frames and numerical conditioning. The unweighted four-site class counts likewise follow from classical principal-minor identities. The specific addition here is **the entire positive four-weight spectrum**, its assignment invariance, the strict worst-class order at *all* weights, and the consequent sharp Schur-convex minimax with explicit two-point sampling law. The inspected material was not found to state this joint weighted theorem; absence from the inspected sources is not a proof of global novelty.

## Limitations

This is a mathematical statement about arbitrary existing real skew-conference matrices, not an existence theorem. No guarantee is asserted for noncanonical duals, noncommuting losses, correlated attenuation, five or more erasures, or weights with negative entries. The erasure norm is a deterministic operator norm, not a stochastic noise-performance model. Historical coverage by a differently stated general principal-minor theorem remains possible. Independent mathematical validation has not been performed.

## References

1. B. G. Bodmann and V. I. Paulsen, *Frames, Graphs and Erasures*, first posted 2004-06-08, arXiv:math/0406134, https://arxiv.org/abs/math/0406134.
2. T. Hoffman and J. Solazzo, *Complex Equiangular Tight Frames and Erasures*, first posted 2011-07-08, arXiv:1107.2267, https://arxiv.org/abs/1107.2267.
3. M. Fickus, J. Jasper, D. G. Mixon, and J. D. Peterson, *Group-theoretic constructions of erasure-robust frames*, arXiv:1210.0139, https://arxiv.org/abs/1210.0139.
4. Q. Cheng, F. Lv, and W. Sun, *Frames of uniform subframe bounds with applications to erasures*, Linear Algebra Appl. 555 (2018), 186–200, DOI:10.1016/j.laa.2018.05.025.
