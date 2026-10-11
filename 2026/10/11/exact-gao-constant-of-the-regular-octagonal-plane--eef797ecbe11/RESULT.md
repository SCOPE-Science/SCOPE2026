# Exact Gao constant of the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\) be the real regular octagonal Banach plane, where
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For Gao's lower von Neumann--Jordan constant
\[
c'_{\mathrm{NJ}}(X_8)=\inf_{x,y\in S_{X_8}}\frac{N(x+y)^2+N(x-y)^2}{4},
\]
the exact value is
\[
c'_{\mathrm{NJ}}(X_8)=\frac{2+\sqrt2}{4}.
\]
Thus the regular octagon supplies an exact equality case for the Euclidean-comparison lower bound in the absolute-normalized-norm framework, although the sufficient maximizer-matching condition used in the published equality theorem does not hold here.

## Assumptions and scope
All scalars are real. The result concerns the two-dimensional norm \(N\) displayed above and the lower Gao constant, i.e. the infimum over two unit vectors. It does not concern the upper generalized von Neumann--Jordan constant or the distinct supremal generalized Gao constants appearing elsewhere in the literature.

Write
\[
a=\sqrt2-1,\qquad d=\sqrt{1+a^2}=\sqrt{4-2\sqrt2}.
\]
The unit ball of \(N\) is the regular octagon cut out by
\[
|s|\le1,\qquad |t|\le1,\qquad |s|+|t|\le\sqrt2,
\]
whose eight vertices are obtained from \((1,a)\) and \((a,1)\) by signs and coordinate interchange.

## Proof
For every \(z=(s,t)\in\mathbb R^2\),
\[
N(z)\le \|z\|_2.
\]
Indeed, each of \(|s|\), \(|t|\), and \((|s|+|t|)/\sqrt2\) is at most \(\sqrt{s^2+t^2}\).

Conversely,
\[
\|z\|_2\le d\,N(z).
\]
By homogeneity it is enough to take \(N(z)\le1\). Every such \(z\) is a convex combination of the eight octagon vertices, and every vertex has Euclidean norm
\[
\sqrt{1+a^2}=d.
\]
Convexity of the Euclidean norm therefore gives \(\|z\|_2\le d\). Hence
\[
\frac{\|z\|_2}{d}\le N(z)\le\|z\|_2.
\]

Now let \(x,y\in S_{X_8}\). Since \(N\le\|\cdot\|_2\), one has \(\|x\|_2\ge1\) and \(\|y\|_2\ge1\). Applying the lower Euclidean comparison to \(x+y\) and \(x-y\), then using the parallelogram identity, yields
\[
\begin{aligned}
N(x+y)^2+N(x-y)^2
&\ge \frac{\|x+y\|_2^2+\|x-y\|_2^2}{d^2}\\
&=\frac{2\|x\|_2^2+2\|y\|_2^2}{d^2}\\
&\ge\frac4{d^2}.
\end{aligned}
\]
Therefore
\[
c'_{\mathrm{NJ}}(X_8)\ge\frac1{d^2}=\frac1{4-2\sqrt2}=\frac{2+\sqrt2}{4}.
\]

For equality, take
\[
x=(1,0),\qquad y=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right).
\]
Both vectors are \(N\)-unit. Directly,
\[
N(x+y)=1+\frac1{\sqrt2},\qquad N(x-y)=\frac1{\sqrt2}.
\]
Consequently
\[
\frac{N(x+y)^2+N(x-y)^2}{4}
=\frac{2+\sqrt2}{4},
\]
which matches the lower bound.

## Verification
The proof uses only the explicit octagon, the sharp two-sided comparison with the Euclidean norm, and the Euclidean parallelogram identity. The bundled `verify.py` checks the algebraic identities for \(d^2\), the candidate value, the equality witness, and the locations of the comparison-ratio extrema in exact arithmetic over \(\mathbb Q(\sqrt2)\). Its successful output is `VERIFY_OK`.

## Relationship to prior work
Zuo, Huang, Huang, and Wang define the lower Gao-type constants for absolute normalized norms and note that the case \(p=2\) is Gao's constant. Their Euclidean comparison gives a general lower bound in terms of two norm-comparison extrema. Their Theorem 7 supplies a sufficient condition for equality in the case \(p=2\): the two comparison extrema must occur at parameters satisfying a specific product relation.

For the regular-octagonal profile
\[
\phi(t)=\max\left\{1-t,t,\frac1{\sqrt2}\right\},
\]
the ratio \(\phi/\phi_2\) has maximum \(1\) only at \(t=0,1/2,1\), while \(\phi_2/\phi\) is maximized at \(t=1-1/\sqrt2\) and its reflection. None of the maximizing choices in \([0,1/2]\) satisfy the product condition in Theorem 7. The theorem therefore does not imply equality for this octagon. The explicit orthogonal pair above supplies the missing attainment argument.

Targeted searches for the lower Gao constant of the regular octagonal plane found related exact constants for the same norm and Gao constants for other norm families, but no statement implying this exact infimum. The later paper on the “generalized Gao's constant” studies a different supremal invariant and therefore does not cover the present lower constant.

## Limitations
The result is specific to the regular octagonal plane and to the quadratic lower Gao constant. It does not determine the full \(p\)-parameter lower Gao-type profile. The originality assessment is based on inspected primary literature and targeted semantic and exact-phrase searches; noncoverage by a search index is not a proof that no equivalent statement exists in unindexed literature.

## References
1. Z. Zuo, Y. Huang, H. Huang, and J. Wang, “The Gao-Type Constant of Absolute Normalized Norms on \(\mathbb R^2\),” *Mathematics* 10 (2022), 4591. DOI: 10.3390/math10234591.
2. Z.-F. Zuo, Y.-M. Huang, and J. Wang, “The generalized Gao's constant of absolute normalized norms in \(\mathbb R^2\),” *Mathematical Inequalities & Applications* 26 (2023), 109–129. DOI: 10.7153/mia-2023-26-09.
