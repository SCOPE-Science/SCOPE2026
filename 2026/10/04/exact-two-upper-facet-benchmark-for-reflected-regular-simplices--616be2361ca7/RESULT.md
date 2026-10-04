# Exact two-upper-facet benchmark for reflected regular simplices

## Finding

Let \(S\subset\mathbb R^n\) be a regular \(n\)-simplex with \(n\ge3\). Let \(H\) be a supporting hyperplane through a vertex \(s_0\), let \(u\) be the inward unit normal of \(H\), and let \(S^H\) be the reflection of \(S\) in \(H\).

Use the upper-side convention of Horváth: a facet is upper if a ray parallel to \(-u\), started sufficiently far in the \(u\)-half-space, first meets \(S\) in that facet. Restrict to supporting hyperplanes for which exactly two facets are upper.

Then
\[
\boxed{
\max_H
\frac{\operatorname{Vol}_n(\operatorname{conv}(S,S^H))}
{\operatorname{Vol}_n(S)}
=
n+\sqrt{\frac{2(n^3-2n^2+2)}{n+1}}
}.
\]

For \(n=5\), this becomes
\[
5+\sqrt{\frac{77}{3}},
\]
which is exactly Horváth's published global optimum.

For every integer \(n\ge5\),
\[
n+\sqrt{\frac{2(n^3-2n^2+2)}{n+1}}>2n.
\]
Thus the two-upper-facet chamber alone beats the height-orthogonal configuration in every dimension in which Horváth showed that the value \(2n\) ceases to be globally optimal.

For \(n\ge6\), where the global supporting-hyperplane problem remains open in the cited primary source, this gives the explicit lower benchmark
\[
\max_H
\frac{\operatorname{Vol}_n(\operatorname{conv}(S,S^H))}
{\operatorname{Vol}_n(S)}
\ge
n+\sqrt{\frac{2(n^3-2n^2+2)}{n+1}}.
\]
Moreover,
\[
\frac1n
\left(
n+\sqrt{\frac{2(n^3-2n^2+2)}{n+1}}
\right)
\longrightarrow
1+\sqrt2.
\]

## Assumptions and scope

The simplex is Euclidean and regular. The reflecting hyperplane supports \(S\) at a vertex. This vertex-intersection reduction is the setting used by Horváth after the earlier main lemma showing that a global maximizing reflected pair may be taken to meet at a common vertex.

The theorem is an exact optimization only in the chamber where the upper side contains exactly two facets. It does not claim that two upper facets are globally optimal for \(n\ge6\).

Normalize the regular simplex so that
\[
s_0=0,\qquad
\lVert s_i\rVert=1,\qquad
\langle s_i,s_j\rangle=\frac12
\quad(i\ne j).
\]
Put
\[
s=\sum_{i=1}^n s_i,\qquad
u_0=\frac{s}{\lVert s\rVert},
\qquad
x=\langle u_0,u\rangle.
\]
If the second upper facet is opposite \(s_i\), put
\[
y=\langle s_i,u\rangle.
\]

## Proof

Horváth's exact prism decomposition gives, when exactly two facets are upper,
\[
\frac{\operatorname{Vol}_n(\operatorname{conv}(S,S^H))}
{\operatorname{Vol}_n(S)}
=
2n f_n(x,y),
\]
where
\[
f_n(x,y)
=
\frac{2}{n}y^2
-
(n+2)\sqrt{\frac{2}{n(n+1)}}\,xy
+
2x^2.
\]

The same primary proof gives the upper-facet constraint
\[
y\le
a_n x,
\qquad
a_n=\sqrt{\frac{n}{2(n+1)}}.
\]
Its spherical-angle estimate specializes, for two upper facets, to
\[
y\ge
b_nx-c_n\sqrt{1-x^2},
\]
where
\[
b_n=\sqrt{\frac{n+1}{2n}},
\qquad
c_n=\sqrt{\frac{n-1}{2n}}.
\]

For fixed \(x\), \(f_n(x,y)\) is a convex quadratic in \(y\). Hence its maximum over the admissible interval occurs at one of the two endpoints.

At the upper endpoint \(y=a_nx\), direct substitution gives
\[
f_n(x,a_nx)=x^2.
\]
The interval is nonempty only if
\[
(b_n-a_n)x\le c_n\sqrt{1-x^2}.
\]
Since
\[
\frac{b_n}{a_n}=\frac{n+1}{n},
\]
this implies
\[
x^2\le1-\frac1{n^2}.
\]
Thus the upper endpoint contributes at most
\[
1-\frac1{n^2}.
\]

Now consider the lower endpoint. Write
\[
y=\sin\phi.
\]
The equality
\[
\sin\phi=b_nx-c_n\sqrt{1-x^2}
\]
is inverted by
\[
x=b_n\sin\phi+c_n\cos\phi.
\]
Substitution into \(f_n\) simplifies exactly to
\[
g_n(\phi)
=
\frac1n\sin^2\phi
+
\frac{n-1}{n}\cos^2\phi
+
\sqrt{\frac{n-1}{n+1}}\sin\phi\cos\phi.
\]

Therefore \(g_n\) is the Rayleigh quotient of
\[
M_n=
\begin{pmatrix}
\frac1n &
\frac12\sqrt{\frac{n-1}{n+1}}\\[1mm]
\frac12\sqrt{\frac{n-1}{n+1}} &
\frac{n-1}{n}
\end{pmatrix}.
\]
Its largest eigenvalue is
\[
\lambda_n
=
\frac12+
\frac1{2n}
\sqrt{\frac{2(n^3-2n^2+2)}{n+1}}.
\]

This eigenvalue is strictly larger than the best upper-endpoint value. Indeed,
\[
(2\lambda_n-1)^2
-
\left(1-\frac{2}{n^2}\right)^2
=
\frac{(n-1)(n^2-2n-2)^2}{n^4(n+1)}
>0
\]
for \(n\ge3\). Since both compared quantities are positive,
\[
\lambda_n>1-\frac1{n^2}.
\]

It remains to verify that the positive eigenvector realizing \(\lambda_n\) corresponds to a genuine two-upper-facet configuration rather than merely to the relaxed endpoint.

Let
\[
q_n=\sqrt{\frac{n-1}{n+1}},
\qquad
m_n=\frac{q_n}{2}.
\]
For the positive unit eigenvector \((\sin\phi,\cos\phi)\),
\[
\frac{\sin\phi}{\cos\phi}
=
\frac{m_n}{\lambda_n-1/n}.
\]
For \(n\ge3\),
\[
\lambda_n>\frac12+\frac1n,
\]
because
\[
\frac{2(n^3-2n^2+2)}{n^2(n+1)}
-
\frac4{n^2}
=
\frac{2(n^2-2n-2)}{n(n+1)}>0.
\]
Hence
\[
\frac{\sin\phi}{\cos\phi}<q_n.
\]
But
\[
a_nb_n=\frac12,
\qquad
a_nc_n=\frac{q_n}{2},
\]
so this inequality is exactly
\[
\sin\phi
<
a_n(b_n\sin\phi+c_n\cos\phi)
=
a_nx.
\]
Thus the second facet is strictly upper.

To see realizability directly, decompose
\[
s_i=b_nu_0+w_i,
\qquad
\lVert w_i\rVert=c_n.
\]
Take
\[
u=xu_0-\sqrt{1-x^2}\frac{w_i}{c_n}.
\]
Then
\[
\langle s_i,u\rangle
=
b_nx-c_n\sqrt{1-x^2}
=
\sin\phi.
\]
For every \(j\ne i\),
\[
\langle s_j,w_i\rangle=-\frac1{2n},
\]
and therefore
\[
\langle s_j,u\rangle
=
b_nx+
\frac{\sqrt{1-x^2}}{\sqrt{2n(n-1)}}
>
b_nx
>
a_nx.
\]
Thus no other facet joins the upper side. The maximizing lower-endpoint configuration is a genuine two-upper-facet supporting configuration.

Finally,
\[
2n\lambda_n
=
n+\sqrt{\frac{2(n^3-2n^2+2)}{n+1}},
\]
proving the formula.

The comparison with \(2n\) follows from
\[
(2\lambda_n-1)^2-1
=
\frac{(n-1)(n^2-4n-4)}{n^2(n+1)},
\]
so \(\lambda_n>1\) exactly for integer \(n\ge5\). The large-\(n\) limit follows by dividing the closed form by \(n\).

## Verification

The accompanying `verify.py` reconstructs the largest eigenvalue, the positive eigenvector, the endpoint equality, strict visibility of exactly the second upper facet, exclusion of all remaining facets, and the published two-facet volume bracket for every integer dimension from \(3\) through \(400\).

It separately checks the \(n=5\) specialization
\[
5+\sqrt{\frac{77}{3}},
\]
the threshold \(n\ge5\) for beating \(2n\), and the asymptotic normalized value \(1+\sqrt2\).

The replay output is:

`VERIFY_OK reflected simplex two-upper-facet benchmark`

The finite checks are consistency checks only. The proof of the all-dimensional formula is the analytic endpoint and eigenvalue argument above.

## Relationship to prior work

Horváth's 2019 paper is the direct primary source. It defines the upper-side decomposition and derives the exact volume expression in terms of the number of upper facets. It proves that the height-orthogonal value \(2n\) is globally optimal for \(n\le4\), proves that it fails in higher dimensions, and solves the global \(n=5\) case with value
\[
5+\sqrt{\frac{77}{3}}.
\]
The paper explicitly leaves the higher-dimensional supporting-hyperplane problem open.

In the \(n=5\), two-upper-facet case, Horváth reduces the lower endpoint to
\[
\frac15\sin^2\phi
+
\frac45\cos^2\phi
+
\sqrt{\frac23}\sin\phi\cos\phi
\]
and optimizes it. The present result identifies the all-dimensional matrix behind that calculation and proves that its positive eigenvector is feasible in the two-upper-facet chamber for every \(n\ge3\).

Horváth's earlier 2013/2014 paper and the 2015 survey stated the value \(2n\) in all dimensions. The 2019 primary source explicitly corrects that statement. Those earlier claims therefore do not cover the formula above.

Targeted searches for the exact higher-dimensional two-upper-facet maximum, its closed radical form, the equivalent Rayleigh-quotient matrix, and follow-up work on the 2019 problem did not locate an equivalent result.

## Limitations

The theorem does not settle the global problem for \(n\ge6\): configurations with three or more upper facets may give a larger volume.

The exact prism-volume formula and the upper-facet inequalities are used as published premises from Horváth's paper. They are not re-proved from first principles here.

The literature search found no later equivalent result, but unindexed or differently phrased work remains a residual originality risk.

## References

Á. G. Horváth, “An extremal problem of regular simplices: the five-dimensional case,” Journal of Geometry 110 (2019), article 17, DOI 10.1007/s00022-019-0472-4; preprint arXiv:1811.12399, first submitted 2018-11-29.

Á. G. Horváth, “On an extremal problem connected with simplices,” Beiträge zur Algebra und Geometrie 55 (2014), 415–428, DOI 10.1007/s13366-013-0151-9; preprint arXiv:1303.3454.

Á. G. Horváth, “Volume of convex hull of two bodies and related problems,” in Discrete Geometry and Symmetry, Springer Proceedings in Mathematics & Statistics 234 (2018), 201–224, DOI 10.1007/978-3-319-78434-2_11; preprint arXiv:1509.08859.
