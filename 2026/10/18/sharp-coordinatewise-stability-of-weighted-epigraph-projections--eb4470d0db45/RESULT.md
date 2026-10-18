# Sharp coordinatewise stability of weighted epigraph projections and their polar cones

## Finding
Fix an integer \(n\ge1\) and any positive numbers \(w_1,\ldots,w_n\). Put \(a_i=1/w_i\) and consider the weighted maximum-norm epigraph
\[
 C_w=\{(t,x)\in\mathbb R^{n+1}:t\ge\max_{1\le i\le n}w_i|x_i|\}.
\]
Write \(P_w\) for the **Euclidean nearest-point projection** onto \(C_w\), but measure the perturbations of its input and output in the coordinatewise \(\ell^\infty\) norm on \(\mathbb R^{n+1}\). For \(S\subseteq\{1,\ldots,n\}\), set
\[
 R(S)=\frac{1+\sum_{j\in S}a_j}{1+\sum_{j\in S}a_j^2},\qquad R(\varnothing)=1.
\]
Its exact global coordinatewise Lipschitz constant is
\[
 \boxed{\operatorname{Lip}_\infty(P_w)=\max\left\{1,\max_{\varnothing\ne S\subseteq[n]}R(S)\max\left(1,\max_{i\in S}a_i\right)\right\}.} \tag{1}
\]
The maximum can be evaluated using only \(O(n^2)\) candidate subsets, rather than all \(2^n\): include each subset comprising the \(k\) smallest \(a_i\), and, for each specified coordinate \(i\), include \(\{i\}\) together with the \(k\) smallest \(a_j\) among \(j\ne i\), for every allowed \(k\). In particular,
\[
 \boxed{\operatorname{Lip}_\infty(P_w)=1\quad\Longleftrightarrow\quad w_1=\cdots=w_n=1.} \tag{2}
\]
The sharp **unconstrained weight-design maximum** and its complete equality cases are
\[
 \boxed{\max_{w_1,\ldots,w_n>0}\operatorname{Lip}_\infty(P_w)=\frac{1+\sqrt{n+1}}2.} \tag{3}
\]
Writing \(s=\sqrt{n+1}\), equality in (3) holds **exactly** for the following \(n+1\) vectors of reciprocal weights: either \(a_i=1/(s+1)\) for every \(i\), or, for some one coordinate \(h\), \(a_h=s+1\) and \(a_j=1\) for all \(j\ne h\). The former extremizes the height output row, the latter a clipped spatial output row. Thus the worst design amplification grows like \(\sqrt n/2\) despite the calibrated unweighted cone being nonexpansive.

For comparison, its polar partner is the \(\ell^1\) epigraph \(C_1=\{(t,x):t\ge\sum_i|x_i|\}\). At equal, unit weights,
\[
 \boxed{\operatorname{Lip}_\infty(\Pi_{C_1})=\frac{2n}{n+1},\qquad \operatorname{Lip}_\infty(P_{(1,\ldots,1)})=1.} \tag{4}
\]
The unweighted contrast is included to interpret the weight-design theorem; earlier work already gives the underlying unweighted projector and its directional derivatives, so (4) is not presented as a separately novel result.

## Assumptions and scope
All spaces and coordinates are real and finite-dimensional. The ambient nearest-point projection is defined with the standard **Euclidean \(\ell^2\) distance**; only the Lipschitz sensitivity is measured in \(\ell^\infty\). The epigraph parameter \(t\) is one of the coordinates used in both norms. All weights are strictly positive and no normalization on the weights is imposed. The quantity \(\operatorname{Lip}_\infty(P)\) denotes \(\sup_{u\ne v}\|P(u)-P(v)\|_\infty/\|u-v\|_\infty\). The exact formula (1) holds for every weight vector. Equality classifications (2) and (3) are global, not infinitesimal-only.

## Proof
**1. Weighted epigraph charts.** Let \((b,y)\in\mathbb R\times\mathbb R^n\) be the input, and write \((\theta,z)=P_w(b,y)\). For fixed \(\theta\ge0\), the uniquely minimizing spatial output is
\[
 z_i=\operatorname{clip}(y_i,-a_i\theta,a_i\theta).
\]
Consequently \(\theta\) uniquely minimizes the strictly convex scalar function
\[
 (\theta-b)^2+\sum_{i=1}^n(|y_i|-a_i\theta)_+^2
\]
over \(\theta\ge0\). On any open chart with \(\theta>0\), fixed signs \(\sigma_i\), and a prescribed set \(S=\{i:|y_i|>a_i\theta\}\) of clipped coordinates, differentiation gives
\[
 \theta=\frac{b+\sum_{j\in S}a_j\sigma_jy_j}{D_S},\qquad D_S=1+\sum_{j\in S}a_j^2.
\]
Thus the absolute row sum of the height derivative is \(R(S)\); the absolute row sum of a clipped spatial derivative row \(i\in S\) is \(a_iR(S)\), and each unclipped coordinate has derivative row norm \(1\). Charts in the interior of the cone have identity derivative; the open polar-interior chart has zero derivative. In boundary charts the projector remains continuous and piecewise affine. Any finite line segment can be partitioned into affine pieces, so the largest chart derivative norm bounds the global Lipschitz modulus.

Every chart \(S\ne\varnothing\) is attained **with strict inequalities**: choose \(\theta=1\), input \(b=1-|S|\), input \(y_i=a_i+a_i^{-1}\) for \(i\in S\), and \(y_j=0\) otherwise. Its projection is \((1,z)\) with \(z_i=a_i\) on \(S\) and zero off \(S\). Arbitrarily small perturbations in the signed row-maximizing direction realize the derivative norm as a limit of actual Lipschitz ratios. This proves (1), including its sharpness.

**2. Sorted-prefix reduction.** Consider the fraction \(R(S)=N_S/D_S\). For an index \(j\notin S\), adjoining \(j\) strictly increases it exactly when \(a_j<1/R(S)\); for \(j\in S\), removing \(j\) strictly increases it exactly when \(a_j>1/R(S)\). Therefore at any maximizing subset, all unforced included \(a_j\) are no larger than all excluded \(a_j\), except possibly equal values at the common threshold. Sorting these values yields a prefix maximizer. Apply this once to the height row, and once for every spatial row with its index \(i\) forced into the set. This gives the stated \(O(n^2)\) candidate family (after sorting), with the same exact maximum.

**3. Rigidity.** When every \(a_i=1\), \(R(S)=1\) for every nonempty \(S\), so (1) gives nonexpansivity. Conversely, if some \(a_i\ne1\), choose \(S=\{i\}\). When \(a_i<1\), \((1+a_i)/(1+a_i^2)>1\); when \(a_i>1\), \(a_i(1+a_i)/(1+a_i^2)>1\). The corresponding chart is attainable, proving the strict necessity in (2).

**4. Optimal weight design and all equality cases.** Fix a chart \(S\) with \(k=|S|\ge1\), and let \(v=(1,(a_j)_{j\in S})\in\mathbb R^{k+1}\). Its height and clipped-output row norms are exactly
\[
 \frac{v_h\sum_{j=0}^kv_j}{\sum_{j=0}^kv_j^2},\qquad h=0\text{ or }h\in S,
\]
where \(v_0=1\). This is the Rayleigh quotient of
\[
 B_h=\tfrac12(e_h\mathbf1^\mathsf T+\mathbf1 e_h^\mathsf T).
\]
The matrix has nonzero eigenvalues \((1\pm\sqrt{k+1})/2\), so its largest Rayleigh quotient is \((1+\sqrt{k+1})/2\), attained uniquely up to positive scaling at \(e_h+(k+1)^{-1/2}\mathbf1\). Every chart row is therefore bounded by \((1+\sqrt{n+1})/2\), with strict inequality when \(k<n\). To attain equality one must have \(S=[n]\). If \(h=0\), normalize the height coordinate of the top eigenvector to \(1\): this gives \(a_j=1/(1+s)\) for all \(j\). If \(h\ge1\), the same normalization gives \(a_h=1+s\) and \(a_j=1\) for \(j\ne h\). Both designs have nonempty strict chart neighborhoods by Step 1, proving (3) and the exhaustive equality classification.

**5. Polar comparison.** For \(C_1\), on a strict active chart with \(k\) nonzero spatial outputs, the Euclidean projection has
\[
 \lambda=\frac{\sum_{i\in S}|y_i|-b}{k+1},\quad
 \theta=b+\lambda,\quad z_i=\operatorname{sgn}(y_i)(|y_i|-\lambda)_+.
\]
For every nonempty active set, both the height and the nonzero spatial derivative rows have absolute sum \(2k/(k+1)\), while other rows are zero. The cone-interior derivative is identity and the polar-interior derivative is zero. The full active chart is attained, for example, by input \((n-1,2,\ldots,2)\), whose projection is \((n,1,\ldots,1)\). Maximizing over \(k\) proves (4). The positive dual \(C_\infty^*\) equals \(C_1\) for the unweighted maximum-norm epigraph, but polar duality does not equate their \(\ell^\infty\) projector moduli.

## Verification
The accompanying `verify.py` requires Python 3.10 or newer and only its standard library. Running `python verify.py` produces a `VERIFY_OK` line after exact-fraction comparison of exhaustive active subsets with the sorted-prefix candidates, 181,224 exact-rational and numerical active-chart, Moreau-polar and weight-design checks. The code recomputes selected Euclidean projectors from one-dimensional stationarity and soft thresholding, rather than reading an externally produced norm table. These finite checks are falsification tests, **not** proofs of the all-parameter statements; Steps 1–5 give the proof.

## Relationship to prior work
Ding, Sun, and Toh (public technical report dated 2010-09-26) give the exact Euclidean projector onto **unweighted** \(\ell^\infty\) and \(\ell^1\) epigraphs and directional derivatives, including uniform scalar rescaling. Their formulas underpin the unweighted comparison in (4); they do not include heterogeneous coordinate weights, the sorted-prefix exact stability invariant, or the complete optimal-weight classification (3). Chierchia, Pustelnik, Pesquet, and Pesquet-Popescu (initially public 2012-10-22), Proposition 3.6, give the clipped **weighted** \(\ell^\infty\)-epigraph projection itself. This provides the correct starting point but does not determine its sharp coordinatewise Lipschitz norm or weight-design extrema. Later general epigraphical projection work studies variational continuity and differentiation rather than these quantitative global maxima. The novelty assessment is limited to the stated stability and design results, not the underlying projection algorithms or general derivative theory.

## Limitations
All coordinates are real, the dimension is finite, and weights are strictly positive. The exact formula is for unweighted maximum-error sensitivity of a **Euclidean** projector; it is not the norm of a nearest-point map defined using \(\ell^\infty\) distance. The global design optimizer treats weights as unrestricted positive parameters; constraints fixing a product, sum, or condition number could change the answer. The polar comparison is a supporting consequence of known unweighted projection formulas, not an independently novel claim. Although the closest inspected papers do not state the heterogeneous exact stability invariant and its optimizer classification, undiscovered older equivalent formulations remain a bibliographic risk. Independent review has not been performed.

## References
1. C. Ding, D. Sun, K.-C. Toh, *An Introduction to a Class of Matrix Cone Programming*, Optimization Online, first posted 2010-09-26, https://optimization-online.org/2010/09/2746/ ; open full text https://optimization-online.org/wp-content/uploads/2010/09/2746.pdf . See §3, especially Proposition 3.2.
2. G. Chierchia, N. Pustelnik, J.-C. Pesquet, B. Pesquet-Popescu, *Epigraphical splitting for solving constrained convex formulations of inverse problems with proximal tools*, arXiv:1210.5844, initially submitted 2012-10-22, https://arxiv.org/html/1210.5844v3 . See §3.3, Proposition 3.6.
3. M. P. Friedlander, A. Goodwin, T. Hoheisel, *From perspective maps to epigraphical projections*, arXiv:2102.06809, https://arxiv.org/abs/2102.06809 . General variational context only.
