# Two-season endpoint optimality and the first interior dispersal optimum

## Finding

Consider a finite network of habitat patches with positive seasonal reproduction, followed by an unconditional dispersal decision at the same rate each season. For **one** or **two** repeating seasons, under reversible movement with possible migrant mortality, at least one rate from the two extremes—no dispersal or maximal permitted dispersal—maximizes long-run population growth. For two seasons this is the endpoint bound
\[
\sqrt{\rho(M(d)D_2M(d)D_1)}\le
(1-d)\sqrt{\rho(D_2D_1)}+
 d\sqrt{\rho(CD_2CD_1)},\qquad 0\le d\le1.
\]
Here \(D_1,D_2\) are arbitrary strictly positive diagonal matrices and \(M(d)=(1-d)I+dC\). The statement holds for any finite number of patches, without requiring synchronized or oppositely ordered seasonal growth.

The two-season boundary is **sharp in the number of seasons**: for a particular three-season two-patch cycle, no endpoint maximizes growth. With
\[
C=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
D_1=I,\quad D_2=\operatorname{diag}(1,4),\quad
D_3=\operatorname{diag}(4,1),
\]
the three-season monodromy has spectral radius \(4\) at both \(d=0\) and \(d=1\), but \(25/4\) at \(d=1/2\). Consequently every global maximizing rate belongs to \((0,1)\).

An additional exact two-patch cost threshold is available. With \(a>b>0\),
\(D_1=\operatorname{diag}(a,b)\), \(D_2=\operatorname{diag}(b,a)\), and \(C=c\begin{pmatrix}0&1\\1&0\end{pmatrix}\), where \(0<c\le1\), no dispersal is the unique optimum when \(c<\sqrt{b/a}\); maximal dispersal is the unique optimum when \(c>\sqrt{b/a}\); and exactly the two endpoints are optimal at equality. The result concerns asymptotic linear population growth, not evolutionarily stable strategies or finite-population survival probabilities.

## Assumptions and scope

Fix an integer \(n\ge1\). Let each \(D_t\) be an \(n\)-by-\(n\) strictly positive diagonal matrix. Let \(C\) be a nonnegative column-substochastic matrix, i.e. every column sum is at most one; column mass lost corresponds to dispersal mortality. Assume \(C\) is **diagonally symmetrizable**: some positive diagonal matrix \(Q\) makes \(B=QCQ^{-1}\) symmetric. A symmetric movement matrix is a special case. The same movement matrix and dispersal rate \(d\in[0,1]\) are used in every season; the rate denotes the fraction attempting migration. At time \(t\), population abundance is updated by \(x_{t+1}=M(d)D_t x_t\), where \(M(d)=(1-d)I+dC\). Strict positivity of \(D_t\) ensures invertible square-root similarities even if \(C\) is reducible or singular. The cycle growth factor is the spectral radius of its monodromy; its positive root gives growth per season. No density dependence, feedback, or time-varying dispersal rate is assumed.

## Proof

**One season.** For every nonnegative vector \(x\), column substochasticity gives \(\lVert M(d)D_1x\rVert_1\le(\max_i(D_1)_{ii})\lVert x\rVert_1\). Hence \(\rho(M(d)D_1)\le\max_i(D_1)_{ii}=\rho(D_1)\). In particular, \(d=0\) is optimal.

**Two seasons.** Positive diagonal similarity by \(Q\) changes neither the spectrum nor any \(D_t\), so we may replace \(C\) by the symmetric matrix \(B\). Put \(H(d)=(1-d)I+dB\) and \(A(d)=D_2^{1/2}H(d)D_1^{1/2}\). Direct multiplication gives
\[
D_1^{1/2}[H(d)D_2H(d)D_1]D_1^{-1/2}
=D_1^{1/2}H(d)D_2H(d)D_1^{1/2}=A(d)^\mathsf{T}A(d).
\]
Thus \(\sqrt{\rho(M(d)D_2M(d)D_1)}=\lVert A(d)\rVert_2\), where \(\lVert\cdot\rVert_2\) denotes the Euclidean operator norm. Since \(A(d)=(1-d)A(0)+dA(1)\), the triangle inequality yields
\[
\lVert A(d)\rVert_2\le(1-d)\lVert A(0)\rVert_2+d\lVert A(1)\rVert_2
\le\max\{\lVert A(0)\rVert_2,\lVert A(1)\rVert_2\}.
\]
Both sides are nonnegative, so maximizing squared or unsquared growth is equivalent. In particular no interior rate can strictly outperform both endpoints. Equality may occur throughout an interval for degenerate environments, so endpoint *existence*, not universal uniqueness, is the claim.

**Exact two-patch mortality switch.** At \(d=0\), the two-season monodromy has spectral radius \(ab\). At \(d=1\), it has spectral radius \(c^2a^2\). Hence the endpoint maximizing rates exchange exactly when \(c=\sqrt{b/a}\). If endpoint radii are unequal, the displayed convex inequality is strictly below their maximum for every interior \(d\), proving uniqueness. At equality, \(A(0)=\sqrt{ab}\,I\), while \(A(1)=c\begin{pmatrix}0&b\\a&0\end{pmatrix}\). Because \(a>b\), the unique maximizing right singular direction for \(A(1)\) is the first coordinate axis; its image under \(A(1)\) is orthogonal to its image under \(A(0)\). Equality in the operator-norm triangle inequality would require both images to be positively collinear for a common unit maximizing direction, which is impossible. Therefore every interior rate is strictly suboptimal even at the endpoint tie. The condition \(c\le1\) ensures column substochasticity.

**Three-season sharpness.** Let \(F\) be the two-site swap matrix, so \(M(0)=I\), \(M(1)=F\), and \(M(1/2)=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\). With the stated three seasonal reproduction matrices, the monodromies \(M(d)D_3M(d)D_2M(d)D_1\) are respectively
\[
P_0=\begin{pmatrix}4&0\\0&4\end{pmatrix},\quad
P_{1/2}=\begin{pmatrix}25/8&25/8\\25/8&25/8\end{pmatrix},\quad
P_1=\begin{pmatrix}0&1\\16&0\end{pmatrix}.
\]
Their spectral radii are respectively \(4,25/4,4\). Spectral radius varies continuously with \(d\) for finite matrices; hence a global maximum exists on \([0,1]\), and neither endpoint can attain it. One season was already shown endpoint-optimal; therefore three seasons are the shortest possible periodic cycle permitting strict interior superiority in this model class.

## Verification

`checker.py` is a standalone SymPy program. Running `python checker.py` writes `verification_certificate.json` deterministically in the same directory. It checks 28 exact rational similarity identities in dimensions two, three, and four; verifies the two-patch tied-endpoint example at five rates; and verifies all three exact three-season monodromies and their eigenvalues. The certificate is included in this package. Finite checks establish neither the arbitrary-dimensional statement nor uniqueness; those follow from the preceding operator-norm and equality arguments.

## Relationship to prior work

Schreiber and Li (2010 preprint; 2011 journal article) investigate unconditional dispersal in time-periodic ecological environments, especially evolutionarily stable strategies and coalitions. Their reversible-migration two-period analysis proves selection and source–sink results in a density-dependent evolutionary model. It does **not state** the present general column-substochastic, arbitrary-two-diagonal endpoint-maximization bound or the minimal three-season counterexample. The shared reversible matrix hypothesis means this comparison is essential.

Altenberg (2013) establishes spectral-radius ordering and monotonicity for symmetrizable matrices under particular commuting and spectral-sign conditions; its principal comparisons involve products of the forms \(A^2D\), \(AD\), and related expressions. These are not an all-parameter operator-norm convexity identity for two arbitrary seasonal diagonal matrices under a single reversible movement operator. The underlying norm convexity itself is classical; the claimed contribution is the precise ecological growth optimization and its sharp temporal boundary, **not a new matrix-norm theorem**.

Earlier dispersal-strategy studies and later continuous-time models establish that temporal variation changes dispersal incentives, but they generally ask different model/optimization questions. No exhaustive uniqueness or independent priority certificate is asserted.

## Limitations

The equal-rate assumption is essential: a different rate each season does not produce the stated affine matrix norm. Reversibility (diagonal symmetrizability) is also essential to the argument; the theorem makes no claim for nonreversible matrices. For three or more seasons, only existence of an explicit strict interior advantage is proved, not a classification for every network. The result optimizes deterministic linear asymptotic growth, not ecological persistence under demographic stochasticity. The literature comparison cannot exclude every equivalent unpublished or differently named formulation.

## References

1. S. J. Schreiber and C.-K. Li, *Evolution of unconditional dispersal in periodic environments*, arXiv:1007.5267, first posted 2010-07-29; Journal of Biological Dynamics (2011), DOI 10.1080/17513758.2010.525667. https://arxiv.org/abs/1007.5267
2. L. Altenberg, *On the Ordering of Spectral Radius Product r(A)r(AD) Versus r(A²D) and Related Applications*, arXiv:1301.4969 (2013), DOI 10.1137/130906179. https://arxiv.org/abs/1301.4969
3. D. P. Hardin, P. Takáč and G. F. Webb, *A Comparison of Dispersal Strategies for Survival of Spatially Heterogeneous Populations* (1988), DOI 10.1137/0148086. https://doi.org/10.1137/0148086
4. G. Katriel, *Dispersal-induced growth in a time-periodic environment*, arXiv:2104.01589 (2021). https://arxiv.org/abs/2104.01589
