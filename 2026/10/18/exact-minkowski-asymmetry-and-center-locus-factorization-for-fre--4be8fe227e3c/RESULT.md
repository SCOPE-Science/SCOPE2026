# Exact Minkowski asymmetry and center-locus factorization for free joins

## Finding

For any integer \(k\ge 2\) and full-dimensional compact convex bodies \(A_i\subset\mathbb R^{d_i}\), where every \(d_i\ge1\), let \(J=J(A_1,\ldots,A_k)\) be their **free join**: the convex hull of copies of the factors in affinely independent, mutually skew subspaces. Its dimension is \(\sum_i d_i+k-1\). Denote by \(s(A)\) the Minkowski asymmetry and by \(M(A)\) the complete set of its Minkowski centers.

Then

\[
s(J)=\sum_{i=1}^{k}s(A_i)+k-1.
\]

More strongly, let \(S=\sum_{i=1}^{k}(s(A_i)+1)\) and \(\lambda_i=(s(A_i)+1)/S\). In the canonical free-join coordinates described below, **all** Minkowski centers are exactly

\[
M(J)=\left\{(\lambda_1a_1,\ldots,\lambda_ka_k;\lambda_1,\ldots,\lambda_{k-1}):a_i\in M(A_i)\ \text{for every }i\right\}.
\]

Consequently the center locus is affinely isomorphic to \(\prod_i M(A_i)\), and

\[
\dim\operatorname{aff}M(J)=\sum_{i=1}^{k}\dim\operatorname{aff}M(A_i).
\]

In particular, the free join of \(k\) arbitrary centrally symmetric convex bodies, regardless of their dimensions or shapes, always has asymmetry \(2k-1\).

## Assumptions and scope

For every compact full-dimensional convex body \(A\), define its Minkowski asymmetry by

\[
s(A)=\min_{h\ge1}\bigl\{h:\exists c\in\mathbb R^d,\ A-c\subset h(c-A)\bigr\}
\]

and its center set by \(M(A)=\{c:A-c\subset s(A)(c-A)\}\). Equivalently, \(c\) is an admissible center at factor \(h\) exactly when \((h+1)c-A\subset hA\). The minimum is attained, \(1\le s(A)\le d\), and every admissible center belongs to \(A\).

Use block coordinates \((x_1,\ldots,x_k;t_1,\ldots,t_{k-1})\in\mathbb R^{\sum_i d_i+k-1}\). Let \(t_k=1-\sum_{i<k}t_i\). Explicitly,

\[
J=\left\{(t_1a_1,\ldots,t_ka_k;t_1,\ldots,t_{k-1}):t_i\ge0,\ \sum_i t_i=1,\ a_i\in A_i\right\}.
\]

The condition is independent of the choice of affine coordinates for the original free join. No smoothness, symmetry, integrality, or polyhedral assumption is imposed on any factor. Zero-dimensional factors are excluded from the stated theorem; the normalized point-factor case follows separately with the natural asymmetry convention \(s(\{x\})=0\).

## Proof

**1. Every admissible center admits positive barycentric weights.** Suppose for some \(h\ge1\), \(c\) obeys \((h+1)c-J\subset hJ\). For any \(x\in J\), the point \(y=((h+1)c-x)/h\) belongs to \(J\), and \(c=(x+hy)/(h+1)\in J\). Thus write \(c=(t_1a_1,\ldots,t_ka_k;t_1,\ldots,t_{k-1})\), with \(t_i\ge0\), \(\sum_i t_i=1\), \(a_i\in A_i\). Applying the containment to a point on the \(i\)-th factor face shows that the \(i\)-th barycentric coordinate of its reflected image, divided by \(h\), is \(((h+1)t_i-1)/h\ge0\). If equality held, the varying \(i\)-th spatial block would have to be identically zero for all \(x_i\in A_i\), impossible since \(d_i\ge1\). Hence \((h+1)t_i-1>0\), so in particular every \(t_i>0\).

**2. Factorwise lower bound.** For fixed \(i\), apply \((h+1)c-J\subset hJ\) to the complete face consisting of points with \(x_i\in A_i\) and zero in every other spatial block. Barycentric-coordinate uniqueness in the ambient affine direct sum forces

\[
(h+1)t_i a_i-A_i\subset\bigl((h+1)t_i-1\bigr)A_i.
\]

By the defining optimality of the Minkowski asymmetry of \(A_i\), this implies \((h+1)t_i-1\ge s(A_i)\). Summation over every \(i\) gives

\[
h+1-k=\sum_i\bigl((h+1)t_i-1\bigr)\ge\sum_i s(A_i),
\]

so \(h\ge S-1=\sum_i s(A_i)+k-1\).

**3. Matching containment.** For each \(i\) choose any \(a_i\in M(A_i)\), put \(t_i=\lambda_i=(s(A_i)+1)/S\), and let \(c\in J\) be the displayed weighted embedding. We prove \(Sc-J\subset(S-1)J\). It suffices to check each generating factor face, because both the map \(x\mapsto Sc-x\) and the target \((S-1)J\) respect convex combinations. For \(x\) on the \(i\)-th face, the image \(Sc-x\) has barycentric block weights

\[
w_j=s(A_j)+1-\mathbf1_{\{i=j\}},\qquad\sum_jw_j=S-1.
\]

For every \(j\ne i\), the spatial block is \((s(A_j)+1)a_j\in w_jA_j\), since \(a_j\in A_j\). For \(j=i\), it is \((s(A_i)+1)a_i-x_i\in s(A_i)A_i=w_iA_i\), precisely because \(a_i\in M(A_i)\). Thus the image belongs to \((S-1)J\) for every generating point and hence for all \(J\). This attains the lower bound.

**4. All centers and their dimension.** At the optimal factor \(h=S-1\), the \(k\) inequalities \(St_i-1\ge s(A_i)\) have sums equal on both sides. Every inequality is therefore an equality: \(t_i=(s(A_i)+1)/S\). The facewise containment in Step 2 now reads \((s(A_i)+1)a_i-A_i\subset s(A_i)A_i\), which says exactly \(a_i\in M(A_i)\). Step 3 proves the converse for every choice of these centers. Since all \(t_i>0\), the resulting affine product embedding is injective and preserves sums of affine dimensions.

## Verification

The proof is analytic and valid for all integer \(k\ge2\) and all positive finite factor dimensions. The accompanying `checker.py` separately constructs facet descriptions of finite polytope examples and solves the defining linear containment problem directly by linear programming, without imposing the predicted factorization. Cases include two squares (computed asymmetry \(3\)), triangle plus square (\(4\)), trapezoid plus square (\(7/2\)), triangular prism plus square (\(4\)), a three-factor mixture (\(6\)), and three segments (\(5\)). All numerically recovered factors agree with the theorem. Those finite experiments are corroborative only and do not certify the general statement.

For a geometric example of the center-locus statement, the triangular prism \(\Delta_2\times[0,1]\) has asymmetry \(2\), with a one-dimensional interval of centers in the segment coordinate. Its free join with any centrally symmetric positive-dimensional body has asymmetry \(4\) and a one-dimensional center locus, even though its dimension depends on the symmetric factor. This follows directly from the theorem and the elementary prism calculation.

Reproduce the finite checks with `python checker.py` after installing the declared `requirements.txt` dependencies. Numerical optimization tolerance is \(2\times10^{-7}\).

## Relationship to prior work

Minkowski asymmetry and Minkowski centers are classical. Brandenberg and König (2014, arXiv:1310.4368, especially Section 3.1) describe the asymmetry and its basic bounds. Brandenberg, von Dichter, and González Merino (first arXiv release June 20, 2023, arXiv:2306.11460) study symmetrization inequalities and relationships with asymmetry. Den Hertog, Pauphilet, and Soali (first public Optimization Online posting January 19, 2022) characterize centers by robust optimization, including exact polyhedral formulations. These foundations neither state nor, without an additional reduction, directly imply the asserted free-join identity together with the complete factorization of the center locus.

An earlier observation that pyramiding a convex body increases its asymmetry by one is the zero-dimensional singleton-factor boundary of the present construction; it does not give the independent positive-dimensional factor case or its center-locus product. Similarly, statements about Minkowski sums, Cartesian products, or joins of **simplices** do not give this general asymmetry law: the factors here may be nonsymmetric smooth bodies or have nonunique Minkowski centers. A prior theorem for arbitrary free joins under different terminology remains a bibliographic possibility.

## Limitations

The equality is restricted to **free joins**, meaning the factor affine hulls are independent. It is not asserted for arbitrary convex hulls of overlapping bodies, Minkowski sums, or Cartesian products. The statement concerns Minkowski asymmetry and minimizing-center sets, not Euclidean inradii or canonical ellipsoids. The optional point-factor convention is outside the positive-dimensional theorem. The proof is self-contained once the elementary definition and existence of Minkowski centers are granted, but no independent mathematical audit has been performed. Bibliographic novelty is a best-knowledge assessment, not a proof of uniqueness in the literature.

## References

1. R. Brandenberg and S. König, *Sharpening Geometric Inequalities using Computable Symmetry Measures*, arXiv:1310.4368 (first release 2013; later revised). https://arxiv.org/abs/1310.4368
2. R. Brandenberg, K. von Dichter, and B. González Merino, *From inequalities relating symmetrizations of convex bodies to the diameter-width ratio for complete and pseudo-complete convex sets*, arXiv:2306.11460 (first release June 20, 2023). https://arxiv.org/abs/2306.11460
3. D. den Hertog, J. Pauphilet, and M. Y. Soali, *Minkowski Centers via Robust Optimization: Computation and Applications*, Optimization Online (January 19, 2022), subsequently *Operations Research*, 72 (2024), 2135–2152. https://optimization-online.org/2022/01/8768/
