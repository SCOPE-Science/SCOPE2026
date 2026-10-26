# A degree-27 bitangent tower and uniform hyperflex boundary for characteristic-three Artin–Schreier quartics

## Finding

For every algebraically closed field \(k\) of characteristic \(3\) and every \(c,d,e,f\in k\), the projective plane quartic
\[
C_{c,d,e,f}:\quad x^3z-xz^3=y^4+cy^3z+dy^2z^2+eyz^3+fz^4
\]
is smooth and has precisely \(28\) geometric bitangent lines, explicitly parameterized below. The fixed line \(z=0\) is a hyperflex. The remaining \(27\) lines form a finite étale tower of degrees \(9\) and \(3\) over the coefficient space. Their contact-root scheme has equation \(r^2=d\); hence \(d=0\) is exactly the contact-coalescence (hyperflex) divisor, independent of the other three coefficients. For \(d\ne0\), there are \(27\) ordinary bitangents and \(55\) distinct geometric contact points including the point at infinity; for \(d=0\), all \(28\) lines are hyperflexes, with \(28\) distinct geometric contact points.

## Assumptions and scope

All geometric counts are over algebraically closed characteristic-three fields. A bitangent means a line whose scheme-theoretic intersection with the smooth plane quartic is twice an effective divisor of degree two; a hyperflex means a tangent line meeting the curve with multiplicity four at one point. Counts concern distinct lines and distinct geometric points, not Frobenius orbits or isomorphism classes. The theorem applies to the one-pole order-four Artin–Schreier genus-three stratum; a separate two-pole stratum is not addressed. The family written here has redundant coefficients before passage to moduli, intentionally permitting a universal formula.

Set
\[
 u=a^3-c,\quad v=u^2-d,\quad
 A(a)=a^9-da^3+a+e+dc-c^3,\quad
 B(a,b)=b^3-b-f+v^2.
\]

## Proof

**Smoothness.** Let \(F=x^3z-xz^3-y^4-cy^3z-dy^2z^2-eyz^3-fz^4\). Then \(\partial F/\partial x=-z^3\). Thus no point with \(z\ne0\) is singular. At \(z=0\) the equation gives \(y=0\), so the unique point is \(P_\infty=[1:0:0]\); there \(\partial F/\partial z=x^3=1\). The plane quartic is smooth and has genus three.

**Every candidate line.** A projective line other than \(z=0\) is either \(x=ay+bz\) or \(y=tz\). The second type meets \(C\) at \(P_\infty\) with multiplicity one: in the local coordinate \(z\) on the chart \(x=1\), its equation begins with the linear term \(z\). Such a line cannot be bitangent. Meanwhile, substituting \(z=0\) in \(F\) gives \(-y^4\), hence it is a hyperflex at \(P_\infty\).

**Coefficient comparison.** On the line \(x=ay+bz\), multiplying \(F\) by \(-1\) yields
\[
 y^4+(c-a^3)y^3z+dy^2z^2+(e+a)yz^3+(f+b-b^3)z^4.
\]
In characteristic three, a monic quartic binary form is the square of a quadratic if and only if it is \((y^2+uyz+vz^2)^2\) for suitable \(u,v\). Comparing the coefficients of \(y^3z\) and \(y^2z^2\) forces \(u=a^3-c\) and \(v=u^2-d\). The two remaining comparisons give \(A(a)=0\) and \(B(a,b)=0\). More precisely the *unconditional polynomial identity* is
\[
 \bigl(-F\bigr)|_{x=ay+bz}-(y^2+uyz+vz^2)^2
   =A(a)\,yz^3-B(a,b)\,z^4.
\]
Therefore the parametrization captures every finite bitangent and gives the factorization exactly.

**Étale bitangent tower and total count.** On the affine parameter base \(S=\operatorname{Spec}\mathbb F_3[c,d,e,f]\), the algebra \(\mathcal O_S[a]/(A)\) is free of rank nine, because \(A\) is monic degree nine in \(a\). Since \(\partial A/\partial a=1\), it is finite étale. Adjoining \(b\) via the monic cubic \(B\) is again finite étale, since \(\partial B/\partial b=-1\). The composite is finite étale of degree \(27\). Each geometric fiber therefore supplies \(27\) distinct lines \(x=ay+bz\); with \(z=0\), exactly \(28\) lines occur, and the exhaustive line classification above precludes any others.

**Contact scheme.** The binary quadratic is \(Q=(y-uz)^2-dz^2\), since \(2=-1\) in characteristic three. On the chart \(z=1\) its contact roots are \(y=u+r\), with \(r^2=d\), and the corresponding points on the bitangent are
\[
 [x:y:z]=[a(u+r)+b:u+r:1].
\]
The finite-contact parameter scheme is precisely the rank-two extension of the finite étale degree-27 bitangent tower by \(r^2=d\). Since the characteristic is not two, it is étale when \(d\ne0\) and simply ramified along the divisor \(d=0\) (the derivative in \(r\) is \(2r\)). For \(d\ne0\), each of the 27 lines touches at two distinct points, yielding 54 finite distinct contact points; two *different* bitangents cannot share a tangent point on a smooth curve, because a smooth point has a unique tangent line. Adding \(P_\infty\) gives \(55\) points. When \(d=0\), \(Q=(y-uz)^2\), and all 27 finite lines have a single order-four point, distinct between the lines; with \(P_\infty\), exactly 28 points occur. This also proves that no further special coefficient loci yield extra hyperflexes.

## Verification

The standalone file `verify.py` performs arithmetic in an eight-variable sparse polynomial ring over \(\mathbb F_3\), proves the unconditional displayed coefficient identity by exact zero reduction, and checks three rational-fiber specializations. Run `python3 verify.py`, which prints `VERIFY_OK`. The proof independently establishes smoothness, line completeness, separability, and contact distinctness; the finite checks are not substituted for those universal arguments.

## Relationship to prior work

Li's 2009 study of small-field degree-two del Pezzo surfaces supplies exceptional historical branch quartics. Oyono and Ritzenthaler's 2010 full paper recalls the general \(28\)-bitangent theorem in odd characteristic and studies rational intersection points, not the displayed coefficient-space degree-27 cover. Duque-Rosero–Goodson–Lorenzo García–Malmskog–Scheidler (2024, revised 2025) classify the characteristic-three genus-three Artin–Schreier strata and exhibit the standard one-pole family \(Y^3-Y=X^4+\lambda X^2\); they do not give a bitangent/contact-cover classification. The exceptional all-hyperflex subcase, including a model equivalent to \(\lambda=0\), is already known and is not asserted to be novel. The new mathematical assertion is the uniform explicit étale/branched bitangent-contact tower on the whole one-pole stratum, with exact hyperflex wall and contact incidence. A previous isolated computation on an exceptional quartic does not by itself establish these relative formulas for arbitrary coefficients.

## Limitations

The finite-field Frobenius orbit decomposition of the degree-27 tower is not determined. The formulas do not classify the other two-pole Artin–Schreier genus-three stratum. An equivalent family-wide formula might exist in specialized theta-characteristic, Hasse–Witt, or classical quartic literature not identified by the searches. The result supplies equations and a relative algebraic cover; it does not claim uniqueness of these presentation coordinates or characterize every plane quartic with the same hyperflex profile.

## References

1. S. Li, *Rational Points on Del Pezzo Surface of degree 1 and 2*, arXiv:0904.3555 (first public 2009-04-22), https://arxiv.org/abs/0904.3555.
2. R. Oyono and C. Ritzenthaler, *On rationality of the intersection points of a line with a plane quartic*, arXiv:1006.0873 (first public 2010-06-04), https://arxiv.org/pdf/1006.0873.
3. J. Duque-Rosero, H. Goodson, E. Lorenzo García, B. Malmskog and R. Scheidler, *On invariants of Artin-Schreier curves*, arXiv:2401.08843 (first public 2024; used only for modern stratification context), https://arxiv.org/pdf/2401.08843.
