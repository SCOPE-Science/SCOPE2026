# A complete translation-distance phase diagram for hypercube covariograms

## Finding

For every integer \(d\ge2\), let \(Q=[-1,1]^d\). Its covariogram is \(g_Q(h)=\operatorname{Vol}_d(Q\cap(Q+h))\). Fix a Euclidean translation length \(\|h\|_2=2s\), with \(0<s<\sqrt d\). Then

\[
\boxed{\max_{\|h\|_2=2s}\frac{g_Q(h)}{2^d}=\max_{1\le k\le d,\;s<\sqrt k}\left(1-\frac{s}{\sqrt k}\right)^k.}
\]

Every maximizing translation has exactly \(k\) nonzero coordinates, each of absolute value \(2s/\sqrt k\), for one of the maximizing integers \(k\). Thus the optimizing direction changes discretely from a coordinate-axis direction for small \(s\) to a full-diagonal direction near \(\sqrt d\).

More precisely, a unique number \(\rho\in(1/2,1)\) satisfies
\[
H(\rho)=0,\qquad H(u)=\log(1-u)+\frac{u}{2(1-u)}.
\]
For each integer \(k\ge1\), the adjacent functions \(F_k(s)=(1-s/\sqrt k)^k\) and \(F_{k+1}(s)\) have exactly one positive equality point \(c_k\) with \(0<c_k<\sqrt k\); moreover
\[
\rho\sqrt k<c_k<\rho\sqrt{k+1},\qquad c_1=2(\sqrt2-1).
\]
In dimension \(d\), exactly the \(d-1\) thresholds \(c_1<\cdots<c_{d-1}\) occur. Set \(c_0=0\), and use \(c_d=\sqrt d\) only as the endpoint of the stated domain. For \(c_{k-1}<s<c_k\), the maximizing support size is uniquely \(k\); at \(s=c_k\), exactly \(k\) and \(k+1\) are optimal. The thresholds satisfy \(c_k/\sqrt k\to\rho\).

## Assumptions and scope

The cube is axis aligned, has side length \(2\), and the Euclidean translation length—not any coordinate-wise or maximum norm—is fixed. The dimension \(d\) is an arbitrary integer at least \(2\), and \(0<s<\sqrt d\). The statement concerns translations of one fixed cube, not rotations, arbitrary orthotopes, or a general convex body. A maximizing translation is classified up to sign choices and coordinate permutations. The normalization by \(2^d\) is by the cube's volume.

## Proof

**1. Product reduction.** For \(h=(h_1,\ldots,h_d)\), the intersection consists of independent coordinate overlaps, hence
\[
\frac{g_Q(h)}{2^d}=\prod_{i=1}^d(1-x_i)_+,\qquad x_i=\frac{|h_i|}{2},\qquad\sum_i x_i^2=s^2.
\]
Since \(s<\sqrt d\), the equal-coordinate choice \(x_i=s/\sqrt d<1\) has positive product. Consequently, any global maximizer has positive product and every coordinate is strictly smaller than \(1\).

**2. No unequal positive coordinates at a maximizer.** Fix the nonempty support \(I=\{i:x_i>0\}\), and restrict the objective to its relative interior. Write \(y_i=x_i^2\) for \(i\in I\) and \(f(y)=\log(1-\sqrt y)\). The objective's logarithm is \(\sum_{i\in I}f(y_i)\) subject to \(\sum y_i=s^2\). Direct differentiation gives
\[
f'(y)=-\frac{1}{2\sqrt y(1-\sqrt y)},\qquad f''(y)=\frac{1-2\sqrt y}{4y^{3/2}(1-\sqrt y)^2}.
\]
At a relative-interior stationary point all derivatives \(f'(y_i)\) agree. Therefore all positive \(x_i\) solve the same quadratic equation \(x_i(1-x_i)=a\). There are at most two distinct values, and if two occur they are \(u\) and \(1-u\), with \(0<u<1/2\). Varying their squared coordinates by \(y_i\mapsto y_i+\varepsilon\), \(y_j\mapsto y_j-\varepsilon\) preserves the constraint and stays in the relative interior for sufficiently small positive or negative \(\varepsilon\). The second derivative of the objective logarithm along this line at \(\varepsilon=0\) is
\[
 f''(u^2)+f''((1-u)^2)=\frac{(1-2u)^2}{4u^3(1-u)^3}>0.
\]
Such a point cannot be a local maximum. Every global maximizing support therefore has all its \(k=|I|\) nonzero coordinates equal to \(s/\sqrt k\), requiring \(s<\sqrt k\). Conversely each such vector is admissible. This proves the maximum formula and the complete equal-coordinate shape classification, leaving only comparison of \(k\).

**3. Strictly unimodal continuation in support size.** For fixed \(s>0\) extend the candidate to real \(z>s^2\):
\[
 F_z(s)=\left(1-\frac{s}{\sqrt z}\right)^z.
\]
With \(u=s/\sqrt z\), differentiation yields
\[
\partial_z\log F_z(s)=H(u)=\log(1-u)+\frac{u}{2(1-u)},\qquad H'(u)=\frac{2u-1}{2(1-u)^2}.
\]
Here \(H(0)=0\) by continuity, \(H(1/2)=1/2-\log2<0\), and \(H(u)\to+\infty\) as \(u\uparrow1\). Thus there is exactly one root \(\rho\in(1/2,1)\). As \(z\) grows, \(u\) decreases, so \(F_z(s)\) rises strictly up to \(z=(s/\rho)^2\), then falls strictly. Hence no nonadjacent support sizes can tie for the global maximum.

**4. Exactly one crossing of each adjacent pair.** For integer \(k\ge1\) and \(0<s<\sqrt k\), put
\[
 D_k(s)=\log F_k(s)-\log F_{k+1}(s).
\]
Then \(D_k(0)=0\) and
\[
 D_k'(s)=-\frac{\sqrt k}{1-s/\sqrt k}+\frac{\sqrt{k+1}}{1-s/\sqrt{k+1}}.
\]
This derivative is positive at \(s=0\), vanishes exactly once at \(s=(k+1)\sqrt k-k\sqrt{k+1}\), and is negative thereafter; meanwhile \(D_k(s)\to-\infty\) as \(s\uparrow\sqrt k\). Thus a unique nonzero zero \(c_k\) exists and its crossing is strict. The continuous unimodality in Step 3 implies \(F_k>F_{k+1}\) at \(s=\rho\sqrt k\) and \(F_{k+1}>F_k\) at \(s=\rho\sqrt{k+1}\) (if the latter exceeds \(\sqrt k\), the \(k\)-candidate already vanishes). Therefore \(\rho\sqrt k<c_k<\rho\sqrt{k+1}\), and in particular \(c_k<c_{k+1}\). Between successive thresholds the unique optimizing integer is \(k\); at \(c_k\), strict unimodality excludes every other integer. For \(k=1\), expanding \(1-s=(1-s/\sqrt2)^2\) gives \(c_1=2(\sqrt2-1)\). Dividing the two bounds on \(c_k\) by \(\sqrt k\) proves the asymptotic ratio. This completes the proof.

## Verification

All proof steps above are analytic and apply to arbitrary finite dimension. An accompanying standard-library script checks independent exact cube-intersection products, the equal-support candidates, the ordered strict switching of adjacent branches, numerical derivatives, and randomized spherical competitors for several dimensions. Its finite checks do not constitute a proof of the general theorem. Reproduce using `python3 verify.py`.

## Relationship to prior work

Bianchi's work introduces and studies the covariogram as the intersection volume with a translate and addresses determination of convex bodies from the full covariogram. Bianchi–Gardner–Kiderlen develop reconstruction algorithms based on covariogram data, including bounds involving the cube's brightness function. Schymura studies sharp general symmetric-difference/overlap bounds under translations and matching; these do not classify the fixed-Euclidean-length maximizing direction for an already specified cube. The present result evaluates a different, directional extremal functional of the cube's known covariogram and locates all changes of optimizer. It does not assert any new covariogram uniqueness theorem.

## Limitations

The formula does not extend without further analysis to a rotated copy, to arbitrary boxes under Euclidean-distance constraints, or to the minimum of the covariogram on a Euclidean sphere. The interpretation at \(s=0\) is simply full overlap; at and beyond \(s=\sqrt d\) the maximal intersection volume is zero. Earlier formulations of the elementary constrained-product optimization may exist under different terminology; the novelty comparison is not a proof of exhaustive historical priority.

## References

1. G. Bianchi, *The covariogram and Fourier–Laplace transform in* \(\mathbb C^n\), arXiv:1312.7816, first submitted 2013-12-30, published in Proc. Lond. Math. Soc. 113 (2016), 1–23.
2. G. Bianchi, R. J. Gardner and M. Kiderlen, *Phase retrieval for characteristic functions of convex bodies and reconstruction from covariograms*, arXiv:1003.4486, first submitted 2010-03-23, J. Amer. Math. Soc. 24 (2011), 293–343.
3. D. Schymura, *An upper bound on the volume of the symmetric difference of a body and a congruent copy*, arXiv:1010.2446, first submitted 2010-10-12.
