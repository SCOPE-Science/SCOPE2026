# Exact facial-distance spectrum and a quarter-density transition for hypersimplices

## Finding

For integers \(n\ge3\) and \(1\le k<n\), let the Euclidean hypersimplex be
\[
\Delta_{n,k}=\{x\in[0,1]^n:\textstyle\sum_{i=1}^n x_i=k\}.
\]
Its vertices are the indicator vectors of all \(k\)-subsets of \([n]\). For a nonempty proper face \(F\), set
\[
\delta(F)=\operatorname{dist}\left(F,\operatorname{conv}(\operatorname{vert}(\Delta_{n,k})\setminus F)\right),
\qquad \Phi(\Delta_{n,k})=\min_{F\text{ proper, nonempty}}\delta(F).
\]
Here all distances use the ambient Euclidean norm, which is the intrinsic Euclidean metric on the affine hyperplane of \(\Delta_{n,k}\).

Every nonvertex proper face is uniquely described by disjoint coordinate subsets \(I,J\) fixed respectively to one and zero, with \(a=|I|\), \(b=|J|\), \(m=n-a-b\), and \(0<k-a<m\). Then its **exact squared facial distance** is
\[
\boxed{\delta(F)^2=\frac{n}{m(a+b)+4ab}=\frac{n}{n(a+b)-(a-b)^2}.}
\]
For a vertex face, \(\delta(F)^2=n/[k(n-k)]\).

Put \(q=\min\{k,n-k\}\), and for \(n\ge3\) define
\[
D_{n,k}=\begin{cases}
4q(n-q)-2n,&2q\le n<4q-1,\\[1mm]
\lfloor n^2/4\rfloor+2n(q-1),&n\ge4q-1.
\end{cases}
\]
Then the **sharp global facial distance**, equivalently the pyramidal width, is
\[
\boxed{\Phi(\Delta_{n,k})=\sqrt{\frac{n}{D_{n,k}}}.}
\]
For the degenerate one-dimensional exception \(\Delta_{2,1}\), \(\Phi(\Delta_{2,1})=\sqrt2\).

The minimizing face types are explicit. Under the coordinate-complement isometry, assume \(k=q\le n/2\). Every minimum-producing nonvertex face fixes exactly \(a=q-1\) ones and \(b\) zeros, where \(b\) is an integer in \([0,n-q-1]\) nearest to \(n/2+q-1\); when this target is greater than the upper bound, take \(b=n-q-1\). In particular, at \(n<4q-1\) the minimizing nonvertex faces have exactly two free coordinates, while for large \(n/q\) their free dimension grows. When \(n=3\), vertex faces also attain the minimum; for \(n\ge4\), no vertex does. At the half-integer target, two distinct zero-fixation counts may minimize if both fit the interval.

## Assumptions and scope

The hypersimplex is given in its usual \(0\)-\(1\) embedding, not an arbitrarily affinely distorted realization. A proper face means a nonempty face other than the entire body. Fixing coordinates as above describes all its faces, even for the simplex endpoints \(k=1\) and \(k=n-1\). The absolute value of \(\Phi\) changes under rescaling. The theorem concerns arbitrary positive integers \(n\ge3\) and \(1\le k<n\), plus the stated special case \(n=2\); it uses no asymptotic limit or enumeration bound.

## Proof

**1. Coordinate faces and symmetrization.** Each face is obtained by imposing some coordinate equalities \(x_i=1\) and \(x_j=0\). Write the disjoint fixed sets as \(I,J\), their complement as \(M\), and \(a=|I|\), \(b=|J|\), \(m=|M|\), \(r=k-a\). The face is positive dimensional exactly when \(0<r<m\). Its stabilizer \(S_I\times S_J\times S_M\) acts by orthogonal coordinate permutations and preserves both \(F\) and the convex hull of vertices outside \(F\). Averaging a closest pair over this finite stabilizer does not increase the Euclidean distance. Thus a closest point on \(F\) may be taken to have coordinates \(1\) on \(I\), \(0\) on \(J\), and \(r/m\) on \(M\).

**2. A two-parameter exact distance problem.** For a symmetrized point \(y\) in the outside-vertex hull, let \(s\) be its total missing mass on \(I\), and let \(v\) be its total added mass on \(J\). These are nonnegative. Every outside vertex violates at least one fixed coordinate, and, because the vertices are integral, has \(s+v\ge1\); the same inequality holds for their convex combinations. The constant coordinate values of \(y\) are \(1-s/a\) on \(I\), \(v/b\) on \(J\), and \((r+s-v)/m\) on \(M\), omitting any empty group. Therefore
\[
\|x-y\|^2=\frac{s^2}{a}+\frac{v^2}{b}+\frac{(s-v)^2}{m},
\qquad s,v\ge0,\quad s+v\ge1.
\]
When \(a=0\) one must set \(s=0\); when \(b=0\) one must set \(v=0\). Since the displayed quadratic form is positive homogeneous of degree two, its minimum over this cone lies on \(s+v=1\). When both groups are nonempty, the minimizing parameters are
\[
s_* = \frac{a(m+2b)}{m(a+b)+4ab},\qquad
v_* = \frac{b(m+2a)}{m(a+b)+4ab}.
\]
They belong to \([0,1]\) and sum to one. Direct substitution gives \(\min\|x-y\|^2=n/[m(a+b)+4ab]\), including the limiting cases \(a=0\) and \(b=0\).

**3. Attainment (essential, not just a relaxation).** When \(a>0\), select a face vertex with a zero in the free group, replace one fixed-one coordinate by zero and that free zero by one. Uniformly averaging all such one-swap outside vertices under \(S_I\times S_J\times S_M\) gives the symmetric parameters \((s,v)=(1,0)\). When \(b>0\), similarly replace one free one by zero and one fixed zero by one, obtaining \((s,v)=(0,1)\). Both swaps are possible since \(0<r<m\). The convex combination with coefficients \(s_*\) and \(v_*\) gives an actual point in the outside-vertex hull realizing the minimizing quadratic value. Hence the face-distance formula is an equality.

**4. Vertex faces.** A vertex has a support of size \(k\). Any other vertex replaces exactly \(h\ge1\) entries of that support by \(h\) entries of its complement. Symmetrization under \(S_k\times S_{n-k}\) gives a squared distance of \(h^2(1/k+1/(n-k))\), minimized at \(h=1\), and the uniform average of single-swap vertices realizes it. Thus \(\delta(\{v\})^2=n/[k(n-k)]\).

**5. Maximizing the face denominator.** For nonvertex proper faces the inverse squared distance, multiplied by \(n\), equals
\[
D(a,b)=n(a+b)-(a-b)^2,
\quad 0\le a\le k-1,\quad0\le b\le n-k-1,\quad a+b>0.
\]
Coordinate complementation exchanges \(k\) with \(n-k\) and \(a\) with \(b\). Assume \(k=q\le n/2\). For every allowed fixed \(b\), the discrete increment
\[
D(a+1,b)-D(a,b)=n-2(a-b)-1>0
\]
for \(0\le a<q-1\), so necessarily \(a=q-1\). The remaining expression
\[
D(q-1,b)=n(q-1+b)-(b-q+1)^2
\]
is a concave integer quadratic with real vertex \(b_0=n/2+q-1\). If \(n<4q-1\), its allowed upper endpoint \(b=n-q-1\) is its unique maximizing integer, giving \(D=4q(n-q)-2n\). Otherwise its nearest admissible integer or integers to \(b_0\) maximize it, giving \(D=\lfloor n^2/4\rfloor+2n(q-1)\). The boundary \(n=4q-1\) agrees from both formulas.

The face with \(a=k-1\), \(b=n-k-1\), and \(m=2\) exists for every \(n\ge3\) and yields denominator \(4k(n-k)-2n\). This is at least the vertex denominator \(k(n-k)\) because \(k(n-k)\ge n-1\) and \(3(n-1)-2n=n-3\ge0\). Thus vertices cannot decrease the final minimum. Equality with the vertex bound occurs only at \(n=3\), and for \(n=2\) only vertex faces exist. This completes both the global formula and the minimizing-face characterization.

## Verification

Running `python3 verify_hypersimplex.py` performs exact rational algebra comparisons for every positive-dimensional face type for \(3\le n\le30\), checks the all-parameter integer optimizer against exhaustive face-type maximization, constructs actual outside-vertex one-swap barycenters for small dimensions, and evaluates phase-boundary examples. In the run used to prepare these results it reported **49,100 successful exact comparisons/checks**. Separately, an independently formulated SciPy constrained convex-hull distance minimization matched the formulas on 41 selected face types, including an eight-dimensional balanced hypersimplex. These finite computations are cross-checks, not the proof for unrestricted \(n\), which is the five-step argument above.

## Relationship to prior work

Peña and Wirth, *Calculus of the Facial Distance* (arXiv:2608.28971, initially posted August 29, 2026), derive general calculus rules and lower bounds for simplex-like \(0\)-\(1\) polytopes, including the Birkhoff polytope; their examples do not identify the exact facewise distance or \(n/q\) transition for hypersimplices. Deza, Martínez-Rubio, Peña, and Wirth, *Facial distance and diameter* (arXiv:2609.32440, first posted September 26, 2026), prove a sharp universal upper ratio and obtain an exact Birkhoff value; the universal inequality does not imply the present hypersimplex equality or optimizing face types. Standard simplex endpoints of the new formula agree with the classical regular-simplex value. The distinction is the facewise exact formula, all-rank uniform-matroid base-polytope specialization, and explicit transition in its minimizing coordinate-face dimensions.

## Limitations

This result does not describe general matroid base polytopes, weighted hypersimplices, arbitrary norms, or general affine images. It is a geometric invariant, not a new Frank-Wolfe convergence theorem or a bound on a specific algorithm run. The historical-priority comparison covers the accessible main facial-distance sources and targeted mathematical-record searches but cannot exclude unindexed equivalent expressions in older uniform-matroid optimization literature. Independent mathematical validation has not been performed.

## References

1. J. Peña and E. Wirth, *Calculus of the Facial Distance*, arXiv:2608.28971, version first public August 29, 2026. https://arxiv.org/abs/2608.28971
2. A. Deza, D. Martínez-Rubio, J. Peña, and E. Wirth, *Facial distance and diameter*, arXiv:2609.32440, first public September 26, 2026. https://arxiv.org/html/2609.32440
3. J. Zhao, *Pyramidal Width Can Increase Under Vertex Insertion*, arXiv:2607.29555, July 31, 2026. https://arxiv.org/abs/2607.29555
