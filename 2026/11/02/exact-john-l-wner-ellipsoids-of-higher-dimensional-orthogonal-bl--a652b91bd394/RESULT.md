# Exact John–Löwner ellipsoids of higher-dimensional orthogonal block bicylinders

## Finding

Let integers \(p,q\ge1\) satisfy \(p+q\ge3\), and let \(a\ge b>0\). For the convex intersection of two orthogonal Euclidean block cylinders
\[
K=K_{p,q}(a,b)=\{(x,y,z)\in\mathbb R^p\times\mathbb R^q\times\mathbb R:\ \|x\|_2^2+z^2\le a^2,\ \|y\|_2^2+z^2\le b^2\},
\]
its unique maximum-volume inscribed ellipsoid (John ellipsoid) is
\[
J=\left\{\frac{\|x\|_2^2}{a^2}+\frac{\|y\|_2^2}{b^2}+\frac{z^2}{b^2}\le1\right\}.
\]
Write \(d=p+q+1\), \(t=b^2/a^2\), \(s=1-t\), \(B=p+q+s(p+1)\), and \(\Delta=B^2-4pds\). The number
\[
u=\frac{2p}{B+\sqrt\Delta}\in(0,1)
\]
is the unique maximizer of \(f(v)=v^p(1-v)^q(1-sv)\) on \(0<v<1\). Its unique minimum-volume enclosing ellipsoid (Löwner ellipsoid) is
\[
L=\left\{\frac{u\|x\|_2^2}{a^2}+\frac{(1-u)\|y\|_2^2}{b^2}+\frac{(1-su)z^2}{b^2}\le1\right\}.
\]
Its *complete* contact set with \(K\) is the common cylinder ridge
\[
\Gamma=\left\{(x,y,z):|z|\le b,\ \|x\|_2^2=a^2-z^2,\ \|y\|_2^2=b^2-z^2\right\}.
\]
The ellipsoid-volume ratio is
\[
\rho_{p,q}(t)=\frac{\operatorname{Vol}_d(L)}{\operatorname{Vol}_d(J)}
=\bigl[u^p(1-u)^q(1-su)\bigr]^{-1/2}.
\]
For fixed \(p,q\), it is strictly decreasing in \(t\in(0,1]\), with sharp bounds
\[
\boxed{\sqrt{\frac{(p+q)^{p+q}}{p^p q^q}}\le\rho_{p,q}(t)
<\sqrt{\frac{d^d}{p^p(q+1)^{q+1}}}.}
\]
Equality on the left holds precisely when \(a=b\); the right endpoint is approached as \(b/a\downarrow0\), and is never attained for positive radii. The conclusions hold without restricting the optimizing ellipsoids to a preselected symmetry class.

## Assumptions and scope

All norms above are **Euclidean block norms**, not coordinatewise maxima. Thus for \(p\ge2\) the first constraint is one single quadratic inequality coupling all \(p\) coordinates. The hypothesis \(p+q\ge3\) excludes the classical three-dimensional two-cylinder case; at least one Euclidean block has dimension at least two. Lebesgue volume is measured in the full dimension \(d\). All four parameters \(p,q,a,b\) may vary as indicated, but the two cylinder axes remain orthogonal in this specified block sense. The normalized radius ratio lies in \(t\in(0,1]\).

## Proof

**1. Symmetry and unrestricted optimality.** The set \(K\) is compact, convex, origin symmetric and has nonempty interior. Uniqueness of its maximum-volume contained ellipsoid and its minimum-volume containing ellipsoid is the standard John–Löwner theorem [1,2,3]. Since \(K\) is invariant under the independent orthogonal actions on \(\mathbb R^p\) and \(\mathbb R^q\), and under \(z\mapsto-z\), each unique extremal ellipsoid is centered at the origin and has a scalar quadratic form on each of these three blocks. This argument derives the symmetry of the optimizer; it does not assume it.

**2. John ellipsoid.** A centered block ellipsoid with positive semiaxes \(A,C,T\) is given by \(\|x\|_2^2/A^2+\|y\|_2^2/C^2+z^2/T^2\le1\). It lies in the first cylinder exactly when \(\max(A,T)\le a\), and in the second exactly when \(\max(C,T)\le b\); this follows by maximizing each defining quadratic over the ellipsoid, or simply by comparing the two relevant axis endpoints. Therefore the admissible semiaxes obey \(A\le a\), \(C\le b\), and \(T\le b\) (as \(b\le a\)). Their volume is proportional to \(A^p C^q T\), so the unique maximizer has \((A,C,T)=(a,b,b)\). A John contact certificate consists of the positive equal weights on the \(2d\) endpoints of the \(d\) corresponding principal axes; under the affine map sending \(J\) to the unit ball these are the coordinate unit vectors, with zero mean and identity covariance divided by \(d\).

**3. Enclosing ellipsoid reduction.** Write a candidate containing ellipsoid as \(\|x\|_2^2/A^2+\|y\|_2^2/C^2+z^2/T^2\le1\). For any \(z\) with \(0\le z^2\le b^2\), the maximum of its defining quadratic over the section \(K\cap\{z=\mathrm{const}\}\) equals
\[
\frac{a^2-z^2}{A^2}+\frac{b^2-z^2}{C^2}+\frac{z^2}{T^2}.
\]
This expression is affine in \(z^2\). Containment is therefore **equivalent** to its two endpoint inequalities
\[
\frac{a^2}{A^2}+\frac{b^2}{C^2}\le1,\qquad
\frac{a^2-b^2}{A^2}+\frac{b^2}{T^2}\le1.
\]
Set \(v=a^2/A^2\), \(w=b^2/C^2\), \(h=b^2/T^2\). The conditions are \(v+w\le1\), \(sv+h\le1\), with positive coefficients. Since \(\operatorname{Vol}(L)\) is proportional to \((v^p w^q h)^{-1/2}\), minimizing volume is maximizing that product. For fixed \(v\in(0,1)\), the unique optimal choices are \(w=1-v\), \(h=1-sv\). Thus the remaining optimization is
\[
\max_{0<v<1} f(v),\qquad f(v)=v^p(1-v)^q(1-sv).
\]
The logarithm has strictly negative second derivative,
\[
(\log f)''(v)=-\frac p{v^2}-\frac q{(1-v)^2}-\frac{s^2}{(1-sv)^2}<0.
\]
Its derivative ranges from positive infinity to negative infinity at the interval's endpoints. Hence there is a unique maximizer \(u\). Its first-order equation, after multiplying by the positive quantity \(v(1-v)(1-sv)\), is
\[
p-\bigl[p+q+s(p+1)\bigr]u+d s u^2=0.
\]
The unique root in \((0,1)\) is the stated rationalized radical; this remains valid at \(s=0\), where it reduces to \(p/(p+q)\). Positivity of \(\Delta\) also follows from the strict existence of this unique interior root; explicitly \(B>0\) and the discriminant of the quadratic is nonnegative, with no repeated root at the strictly concave maximum. The optimization yields the displayed \(L\).

**4. Exact contact locus and a finite optimality certificate.** At the maximizing coefficients, both endpoint inequalities are equalities. Therefore the sectionwise maximum of the Löwner quadratic is *identically one for all* \(|z|\le b\). Equality within a section requires \(\|x\|_2^2=a^2-z^2\) and \(\|y\|_2^2=b^2-z^2\), since the coefficients of both blocks are strictly positive. This proves precisely \(K\cap\partial L=\Gamma\).

For an explicit Löwner contact certificate set \(\alpha=q/[d(1-u)]\), \(\beta=1/[d(1-su)]\). The stationary equation is equivalent to \(\alpha+\beta=1\). Give total probability \(\alpha\), uniformly distributed, to the \(4pq\) contacts with \(z=0\), \(x=\pm a e_i\), \(y=\pm b e_j\). Give total probability \(\beta\), uniformly distributed, to the \(4p\) contacts with \(z=\pm b\), \(x=\pm\sqrt{a^2-b^2}e_i\), and \(y=0\). Under the diagonal affine map taking \(L\) to the unit ball, both measures are centrally symmetric, and their mixture has scalar covariance components
\[
\frac{\alpha u+\beta su}{p}=\frac1d,
\quad\frac{\alpha(1-u)}q=\frac1d,
\quad\beta(1-su)=\frac1d.
\]
Thus the contact barycenter is zero and its covariance is \(I_d/d\), an independent normal-form contact certificate for the unrestricted Löwner optimum [2,3]. This proves all dimensions including cases of coincident contact coordinates at \(a=b\).

**5. Sharp ratio and strict monotonicity.** The semiaxes of \(L\) are \(a/\sqrt{u}\), \(b/\sqrt{1-u}\), \(b/\sqrt{1-su}\), yielding the ratio in the statement. For any fixed \(v\in(0,1)\), the function \(v^p(1-v)^q[1-(1-t)v]\) is strictly increasing in \(t\). Its maximal value is also strictly increasing: evaluate the larger-\(t\) function at the smaller-\(t\) unique maximizer. Therefore \(\rho_{p,q}(t)\) is strictly decreasing. At \(t=1\), \(u=p/(p+q)\), giving the lower bound and its equality case. As \(t\downarrow0\), \(u\to p/d\), yielding the strict limiting upper endpoint. All quantifiers and endpoint claims follow.

## Verification

The accompanying executable `verify_bicylinder_general.py` performs exact symbolic stationary and contact-weight identities, an independent numerical one-variable optimization, checks the two active containment constraints, samples interior sections and points on the entire contact ridge, and tests the sharp ratio bounds and monotonicity across many dimensions and radius ratios. On the documented environment it completed with `VERIFY_OK 4791 checks; exact identities, independent optimization, contacts and containment`. Execute `python verify_bicylinder_general.py` with Python 3, SymPy, SciPy and NumPy installed. Finite testing checks consistency; it does not replace the proof of the all-parameter statements.

## Relationship to prior work

The Steinmetz bicylinder and its volume are classical geometric objects [4]. The statements of the John and Löwner theorems and their contact characterizations are established results [1,2,3]. Earlier analyses of the **three-dimensional bicylinder** concern the excluded case \(p=q=1\); separate families defined by one cylinder inequality **per coordinate** use a fundamentally different intersection, with coordinatewise rather than Euclidean block constraints. The present claim is restricted to genuine higher-dimensional blocks (\(p+q\ge3\)) and supplies exact radical formulas, full contact locus, an explicit two-layer design, and all-parameter sharp ratio extrema for these bodies. General results do not themselves state the explicit block-cylinder formulas. Searches and comparisons found no direct equivalent, but this is not proof of historical novelty.

## Limitations

The two axes are orthogonal; both cylinders are centered and their defining forms have Euclidean block symmetry. The theorem does not cover translated, tilted or noncircular cross-section cylinders, or the three-dimensional case. Its ellipsoid ratios are affine volume ratios, not Euclidean Hausdorff distances. Earlier uncatalogued or differently formulated results could cover the same theorem, and no independent audit or historical-priority certification has been completed. Verification assumes the stated numerical Python dependencies.

## References

[1] M. J. Todd, *Minimum-Volume Ellipsoids: Applications, Duality, and Algorithms*, presentation dated July 6, 2007, https://people.orie.cornell.edu/~miketodd/ublndetz.pdf. The presentation discusses optimal design and containing ellipsoids for other shapes; it does not furnish the block-bicylinder formula used here.

[2] P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246, publicly submitted July 31, 2012, https://arxiv.org/abs/1207.7246.

[3] J.-B. Lasserre, *A generalization of Löwner-John's ellipsoid theorem*, arXiv:1302.1056, publicly submitted February 5, 2013, https://arxiv.org/abs/1302.1056.

[4] E. W. Weisstein, *Steinmetz Solid*, MathWorld, https://mathworld.wolfram.com/SteinmetzSolid.html (accessed October 31, 2026 UTC). Contains the classical three-dimensional intersection geometry, not the higher-dimensional ellipsoid classification claimed here.
