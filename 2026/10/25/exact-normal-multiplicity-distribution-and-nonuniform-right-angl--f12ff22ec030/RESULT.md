# Exact normal-multiplicity distribution and nonuniform right-angle transition in triangles

## Finding

Let \(Y\) be uniform in a nondegenerate Euclidean triangle \(T\). Following the polygonal boundary convention in Nasonov--Panina--Siersma [1], count the distinct perpendicular normals from \(Y\) to boundary critical points of the squared-distance function. This count is defined away from the zero-area bifurcation set. It is either four or six. For a nonobtuse triangle it is six almost surely.

For an obtuse triangle write \(A\in(\pi/2,\pi)\) for its unique obtuse angle and \(b,c>0\) for the lengths of its incident sides. Put \(k=-\cos A\in(0,1)\), \(q=b/c\), and

\[
F(A,q)=\frac{1-k^2}{1+k^2+k(q+q^{-1})}
=\frac{bc\sin^2 A}{(c-b\cos A)(b-c\cos A)}.
\]

The full normal-multiplicity law is

\[
\Pr[N_T(Y)=6]=F(A,q),\qquad \Pr[N_T(Y)=4]=1-F(A,q).
\]

In particular \(\mathbb E[N_T(Y)]=4+2F(A,q)\) and \(\operatorname{Var}[N_T(Y)]=4F(A,q)(1-F(A,q))\).

At every fixed obtuse angle \(A\), the exact sharp bound and rigidity statement are

\[
0<F(A,q)\le F_*(A)=\frac{1-k}{1+k}=\cot^2\!\left(\frac A2\right),
\]

with equality if and only if \(b=c\), and

\[
\frac{F_*(A)}{F(A,q)}-1
=\frac{4k}{(1+k)^2}\sinh^2\!\left(\frac12\log q\right).
\]

The lower endpoint zero is an unattained infimum, approached as \(q\to0\) or \(q\to\infty\). Thus the sharp range of mean multiplicity at fixed obtuse angle is \(4<\mathbb EN_T\le 4+2\cot^2(A/2)\).

There is a nonuniform right-angle transition: for \(k\to0^+\) and \(s=k(q+q^{-1})\to\lambda\in[0,\infty]\),

\[
\mathbb E[N_T]\longrightarrow 4+\frac2{1+\lambda},
\]

where \(\lambda=\infty\) gives the limit four. All limits in \([4,6]\) occur along nondegenerate obtuse triangles with obtuse angles approaching \(\pi/2\). In particular the convergence to six is not uniform over degenerating adjacent-side ratios.

## Assumptions and scope

Triangles are nondegenerate and Euclidean, and the probability measure is normalized planar area. A boundary normal means a generic critical point of the squared-distance function restricted to the polygonal boundary, counted without multiplicity. Points on projection-boundary lines, vertices of the triangle, and nongeneric transitions form a planar null set and do not affect the asserted distribution. The fixed-angle bounds concern all positive adjacent side lengths, up to similarity. The boundary-layer statement concerns sequences of proper triangles, although their limiting shapes may degenerate.

## Proof

**1. Critical-point count.** By [1, Section 3.1], for a generic interior \(Y\) every local minimum of the squared-distance function on a triangle's boundary is a perpendicular foot on the relative interior of an edge. Local extrema alternate along the closed boundary and therefore the number of local maxima equals the number of local minima. Every triangle has either two or three such feet; hence \(N_T(Y)\) equals four or six, and six occurs precisely when all three edge projections are interior. This fact is used as stated in [1]; the remaining area and extremal calculations are supplied below.

**2. Area of the three-foot chamber.** Place the obtuse vertex at \(A_0=(0,0)\) and the others at \(B=(c,0)\) and \(C=(b\cos A,b\sin A)\). The other two vertex angles are acute; consequently every interior point projects into the opposite side \(BC\). Write a point of the triangle as \(Y=\beta B+\gamma C\) with \(\beta,\gamma>0\) and \(\beta+\gamma<1\). Orthogonal projection into \(AB\) is equivalent to \(\beta c+\gamma b\cos A>0\), while projection into \(AC\) is equivalent to \(\beta c\cos A+\gamma b>0\). The upper endpoint inequalities are automatic: the linear projection coordinates of the triangle's three vertices attain their maximum at \(B\), respectively \(C\).

The two strict inequalities define a wedge whose intersection with \(BC\), parametrized by \(X(t)=(1-t)B+tC\), is exactly

\[
\frac{-c\cos A}{b-c\cos A}<t<\frac{c}{c-b\cos A}.
\]

The three-foot region is the triangle with apex \(A_0\) and this subsegment of \(BC\) as base. Its area divided by \(|T|\) equals the difference between the two endpoint parameters, namely

\[
\frac{c}{c-b\cos A}+\frac{c\cos A}{b-c\cos A}
=\frac{bc(1-\cos^2 A)}{(c-b\cos A)(b-c\cos A)}.
\]

This is \(F(A,q)\). For nonobtuse triangles, every vertex projects into each opposite edge's closed slab; the convexity of each such slab implies every interior point projects into all three edges, apart from an irrelevant null set. The claimed two-point distribution, expectation, and variance now follow.

**3. Fixed-angle optimum and exact stability.** Since \(q+q^{-1}\ge2\), with equality exactly at \(q=1\), the probability \(F(A,q)\) is maximized uniquely at \(b=c\). Simplifying at \(q=1\) gives \(F_*=(1-k)/(1+k)=\cot^2(A/2)\). The identity

\[
1+k^2+k(q+q^{-1})=(1+k)^2+4k\sinh^2\!\left(\tfrac12\log q\right)
\]

proves the stated exact stability law. The denominator diverges precisely when \(q\) tends to zero or infinity, proving both sharpness and nonattainment of the fixed-angle infimum.

**4. Right-angle boundary layer.** Let \(k\to0^+\) and write \(s=k(q+q^{-1})\). The exact formula becomes \(F=(1-k^2)/(1+k^2+s)\), so \(F\to1/(1+\lambda)\) for any limit \(s\to\lambda\in[0,\infty]\). Every finite positive \(\lambda\) is realized by \(q=\lambda/k\), the case \(\lambda=0\) by \(q=1\), and \(\lambda=\infty\) by \(q=k^{-2}\). Multiplying by two and adding four gives the claimed complete accumulation interval. Notice that the uniformly controlled approach to six requires \(k(q+q^{-1})\to0\); a small angular excess alone does not suffice for degenerating triangles.

## Verification

The self-contained `verification.py` independently clips the original triangle by the two perpendicular-projection half-planes, checks 24 pairs of obtuse-angle/side-ratio parameters, verifies a rational exact case \(F=32/133\), checks the hyperbolic-sine stability identity, and tests 72,000 independently sampled triangle interior points against direct edge-projection counts. It also exercises nine finite representatives of the nonuniform right-angle transition. The script completed without assertions. All finite tests supplement rather than replace the analytic argument above.

## Relationship to prior work

Nasonov, Panina and Siersma [1, Sections 3.1 and 6, especially Proposition 9] established that the count on any triangle takes values four and six, that nonobtuse triangles always have six almost surely, and that the mean for obtuse triangles lies strictly between four and six. Their text does not supply the exact area fraction, the adjacent-side-ratio dependence, fixed-angle rigidity and stability, or the nonuniform joint right-angle/shape limit. A published calculation of average normal multiplicity for **regular odd polygons** gives six in its equilateral triangular instance but does not address arbitrary obtuse triangles. The present calculation is an exact quantitative refinement of the earlier qualitative planar statement, not a new proof of its general polygonal normal-count theory.

## Limitations

The result only concerns Euclidean planar triangles, generic boundary squared-distance critical points and area-uniform interior sampling. It does not generalize to all polygons or higher-dimensional simplices. The near-right-angle limits allow degenerating shape ratios and should not be confused with a fixed side-ratio perturbation. The comparative source inspection was targeted rather than exhaustive; an algebraically equivalent earlier formula may exist in older geometric-probability literature. No independent review or certification has been performed.

## References

[1] I. Nasonov, G. Panina, and D. Siersma, Concurrent normals problem for convex polytopes and Euclidean distance degree, arXiv:2406.01773 (first posted 2024-06-03; consulted arXiv full-text version 2, sections 3.1 and 6). https://arxiv.org/abs/2406.01773 ; full text: https://arxiv.org/html/2406.01773v2 .

[2] Published research record, "Exact average-normal deficit of regular odd polygons" (2026), public identifier ending in `6b1be049a38f`; only its indexed abstract was inspected, not its full text. Its regular-polygon restriction differs from the obtuse-triangle family considered here.
