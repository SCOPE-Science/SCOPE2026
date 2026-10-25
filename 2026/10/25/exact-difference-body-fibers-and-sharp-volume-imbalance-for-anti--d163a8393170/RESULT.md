# Exact difference-body fibers and sharp volume imbalance for antipodally clipped cubes

## Finding

For every integer \(d\ge 3\) and real parameters \(0\le a,b\le1\), put \(s=a+b\) and define the full-dimensional convex polytope
\[
K_{a,b}^{(d)}=\{x\in[0,1]^d:a\le\sum_{i=1}^d x_i\le d-b\}.
\]
Its **entire difference body**, not merely its volume, satisfies the exact identity
\[
\boxed{K_{a,b}^{(d)}-K_{a,b}^{(d)}=[-1,1]^d\cap\{w:|\sum_{i=1}^d w_i|\le d-s\}.}
\]
In particular, at fixed \(s\), the difference body is independent of how the two opposite corners are truncated. Both volumes and their quotient are
\[
\operatorname{vol}_d(K_{a,b}^{(d)})=1-\frac{a^d+b^d}{d!},\qquad
\operatorname{vol}_d(K_{a,b}^{(d)}-K_{a,b}^{(d)})=2^d-\frac{2s^d}{d!},
\]
\[
\boxed{\mathcal R_d(a,b)=\frac{2^dd!-2s^d}{d!-(a^d+b^d)}.}
\]
For each \(0<s<2\), with \(0\le a,b\le1\) and \(a+b=s\), this quotient increases strictly with \(|a-b|\). Its unique minimum occurs at \(a=b=s/2\) and equals \(2^d\). The unique maximum up to exchanging the two parameters occurs at \(\{a,b\}=\{\min(s,1),\max(s-1,0)\}\), and equals
\[
\frac{2^dd!-2s^d}{d!-[\min(s,1)^d+\max(s-1,0)^d]}.
\]
Consequently, for every \(s\in(0,2)\), the fixed difference body has a continuous family of clipped-cube preimages with distinct volumes, and the exact sharp volume range within this family is determined by the displayed formulas. The identities and ratio remain valid under every invertible affine image of the construction.

## Assumptions and scope

Here \(d\) is an integer at least three; \(a,b\) are real numbers between zero and one inclusive. The difference body of a set \(K\) is \(K-K=\{x-y:x,y\in K\}\). Lebesgue volume is the ambient \(d\)-dimensional volume. A zero parameter means that corresponding corner is not clipped. The constraints define nonempty full-dimensional polytopes throughout the stated parameter range. The strict inequality assertion concerns \(0<s<2\); at either endpoint there is only one admissible parameter allocation.

## Proof

**1. Exact difference body: necessity.** For \(x,y\in K_{a,b}^{(d)}\), write \(w=x-y\) and \(S=\sum_i w_i\). Coordinate bounds imply \(w\in[-1,1]^d\); the two sum bounds imply \(|S|\le(d-b)-a=d-s\). This proves inclusion in the asserted intersection.

**2. Exact difference body: sufficiency.** Fix \(w\in[-1,1]^d\) with \(|S|\le d-s\). Put \(p=\sum_i\max(w_i,0)\), \(q=\sum_i\max(-w_i,0)\); then \(S=p-q\). To construct \(x=y+w\), each coordinate of \(y\) may be chosen independently in
\[
\max(0,-w_i)\le y_i\le 1-\max(w_i,0).
\]
Every possible value of \(Y=\sum_i y_i\) in the entire interval \([q,d-p]\) is attainable, by continuity of a sum of independent intervals. The two sum constraints on \(y\) and \(y+w\) require
\[
Y\in[q,d-p]\cap[a,d-b]\cap[a-S,d-b-S].
\]
These three closed intervals have a common point precisely when each lower endpoint is at most each upper endpoint. After eliminating inequalities already implied by \(|w_i|\le1\) and \(a+b\le d\), the remaining conditions are
\[
|S|\le d-s,\qquad p\le d-\max(a,b),\qquad q\le d-\max(a,b).
\]
To verify the latter two, if \(w\) has both a positive and a negative coordinate, at most \(d-1\) coordinates contribute to each of \(p\) and \(q\), so \(p,q\le d-1\le d-\max(a,b)\). Otherwise one of \(p,q\) is zero and the other equals \(|S|\le d-s\le d-\max(a,b)\). Thus all interval intersections are nonempty. Choosing \(Y\) in that intersection and suitable coordinates \(y_i\) yields \(x,y\in K_{a,b}^{(d)}\) with \(w=x-y\). The set identity follows.

**3. Exact volumes.** In \([0,1]^d\), the omitted region \(\sum_i x_i<a\) is a coordinate simplex of volume \(a^d/d!\) because \(a\le1\); the region \(\sum_i x_i>d-b\) is its opposite analogue of volume \(b^d/d!\). They have disjoint interiors because \(s\le2<d\), so subtracting their volumes gives the first formula. Similarly, \([-1,1]^d\) loses two opposite corner simplices where \(\sum_i w_i>d-s\) or \(\sum_i w_i<-(d-s)\), each of volume \(s^d/d!\) since \(s\le2\) and each coordinate can extend distance two from a corner. These caps are interior-disjoint because \(2s\le4<2d\). This gives the difference-body volume and ratio formulas.

**4. Sharp fixed-sum extremizers.** For fixed \(s\), the numerator of \(\mathcal R_d\) is constant and strictly positive. The positive denominator is \(d!-[a^d+(s-a)^d]\). The map \(a\mapsto a^d+(s-a)^d\) is strictly convex on its admissible interval \([\max(0,s-1),\min(1,s)]\), symmetric around \(s/2\), and strictly increasing with \(|a-s/2|\). Hence \(\mathcal R_d\) is strictly increasing with \(|a-b|\). The center \(a=b=s/2\) is the unique minimum; the interval endpoints are the only two maxima. The minimum equals \(2^d\), either by direct substitution or because \(K_{s/2,s/2}^{(d)}\) is centrally symmetric. This proves the announced exact extremal values.

**5. Affine images.** For an invertible linear map \(T\) and vector \(z\), \((TK+z)-(TK+z)=T(K-K)\), and both numerator and denominator of \(\mathcal R_d\) scale by \(|\det T|\). The theorem therefore carries over to every affine parallelotope carrying these opposite parallel-facet corner cuts.

## Verification

A standalone checker `verify.py` tests the exact interval-feasibility criterion over rational parameter grids and coordinate difference grids in several dimensions, checks the analytic volume and ratio formulas by exact rational arithmetic, and verifies the strict fixed-sum comparison on rational samples. It may be run with Python 3 using `python verify.py`; no third-party packages are required. These finite checks are consistency evidence, not a proof for all real parameters and dimensions. The five proof steps above establish the general theorem.

## Relationship to prior work

The classical Rogers–Shephard inequalities constrain the volume ratio of a convex body and its difference body, and the Brunn–Minkowski inequality gives the general lower bound \(\operatorname{vol}(K-K)\ge2^d\operatorname{vol}(K)\), with equality for centrally symmetric bodies. Here the lower bound is an exact equality at balanced cuts, but neither general inequality identifies a whole fixed-difference-body family of asymmetric parallelotope truncations or its sharp volume range. Recent higher-order Godbersen work studies mixed volumes of \(K\) and \(-K\), a related but different global problem. This finding concerns explicit set equality between difference bodies of distinct shapes, rather than only a volume inequality. Unlike one-vertex truncations of simplices, the present construction performs two opposing truncations of a parallelotope and varies their relative allocation.

## Limitations

This is a complete theorem for the stated two-corner-cut parallelotope family, **not** a classification of all convex bodies sharing a given difference body. The sharp extrema apply only within this family. The mathematical proof is self-contained; external-source overlap searches do not establish historical priority. In particular, full text of one recent potentially related Godbersen paper and of some classical sources was not accessible for comprehensive comparison; independent historical verification may reveal an earlier equivalent formulation. No independent scientific audit has been performed.

## References

1. C. A. Rogers and G. C. Shephard, *Convex bodies associated with a given convex body*, Journal of the London Mathematical Society (1958), DOI: 10.1112/jlms/s1-33.3.270.
2. J. Abardia and E. Saorín Gómez, *The role of the Rogers–Shephard inequality in the characterization of the difference body*, arXiv:1602.00967 (2016).
3. *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806 (first publicly available 2026-10-05).
