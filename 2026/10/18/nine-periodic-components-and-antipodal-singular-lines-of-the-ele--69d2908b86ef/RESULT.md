# Nine-periodic components and antipodal singular lines of the elementary symmetric cubic in characteristic three

## Finding

Let \(k\) be algebraically closed of characteristic \(3\), let \(n\ge3\), and let \(e_3=\sum_{i<j<k}x_ix_jx_k\) in \(k[x_1,\ldots,x_n]\). Write \(\Sigma_n=\operatorname{Proj}(k[x_1,\ldots,x_n]/(e_3,\partial_1e_3,\ldots,\partial_ne_3))\) for the projective singular scheme of the cubic hypersurface.

For a nonempty subset \(S\subseteq[n]\), denote by \(L_S\) the projective point represented by the vector with coordinates \(1\) on \(S\) and \(0\) off \(S\). For a nonempty proper subset \(S\), let \(M_S\) be the point represented by \(1\) on \(S\) and \(-1\) off \(S\), so \(M_S=M_{S^c}\). Let \(P_S\) be the projective line (the projectivization of the two-dimensional vector space) on which all coordinates on \(S\) have a common value \(a\), and all those off \(S\) have a common value \(b\).

**Complete reduced support.** If \(n\equiv2\pmod9\), the reduced support of \(\Sigma_n\) is exactly the union of \(P_S\) for nonempty proper \(S\) satisfying \(|S|\equiv1\pmod9\). Distinct such projective lines occur once up to \(S\leftrightarrow S^c\), and their number, which is the degree of the one-dimensional scheme, is
\[
\frac12\sum_{\substack{1\le m<n\\m\equiv1\ (\mathrm{mod}\ 9)}}\binom nm.
\]
Each such projective line has generic scheme multiplicity \(1\).

If \(n\not\equiv2\pmod9\), the reduced support of \(\Sigma_n\) is finite: it consists precisely of every \(L_S\) with \(|S|\equiv1\pmod9\), together with the following additional points, when applicable:

- for \(n\equiv5\pmod9\), all \(M_S\) with \(|S|\equiv7\pmod9\);
- for \(n\equiv8\pmod9\), all \(M_S\) with \(|S|\equiv4\pmod9\).

There are no other additional points. All listed projective points are distinct except for the prescribed relation \(M_S=M_{S^c}\). Every support point has local scheme length \(3\) if \(n\equiv5,8\pmod9\), and length \(1\) otherwise. Thus the total length (degree) of \(\Sigma_n\) in these cases is
\[
\mu_n\left(\sum_{\substack{1\le m\le n\\m\equiv1\ (\mathrm{mod}\ 9)}}\binom nm+
\frac{\mathbf1_{n\equiv5\ (9)}}2\sum_{\substack{1\le m<n\\m\equiv7\ (9)}}\binom nm+
\frac{\mathbf1_{n\equiv8\ (9)}}2\sum_{\substack{1\le m<n\\m\equiv4\ (9)}}\binom nm\right),
\]
where \(\mu_n=3\) when \(n\equiv5,8\pmod9\) and \(\mu_n=1\) otherwise.

In particular, \(\Sigma_8\) consists of eight coordinate-support points and **35 antipodal-sign points**, every one of local length three, so \(\deg(\Sigma_8)=129\). For \(n=11\), its reduced support is exactly eleven projective lines of generic multiplicity one, and its scheme degree is eleven.

## Assumptions and scope

All assertions concern an algebraically closed base field of characteristic three, the homogeneous elementary symmetric cubic in \(n\ge3\) variables, and the projective singular scheme defined by the polynomial and its first derivatives. The theorem classifies its topological support and the generic multiplicities of all top-dimensional components; in zero dimension it determines every local length. It makes no assertion about embedded or nilpotent structures at intersections of projective lines in the one-dimensional case.

## Proof

**Step 1: at most two coordinate values.** Put \(e_1=\sum_i x_i\) and \(e_2=\sum_{i<j}x_ix_j\). The derivative identity
\[
\partial_i e_3=e_2-x_ie_1+x_i^2
\]
shows that all coordinates at a critical point are roots of the same monic quadratic. Therefore such a point has at most two distinct coordinate values. This reduction is set-theoretic over the algebraically closed field and does not presuppose any scheme-theoretic reducedness.

**Step 2: determine the gradient locus.** Suppose distinct values \(a,b\) occur on blocks \(S,S^c\) of sizes \(m,\ell\), respectively. Subtracting the derivative equations yields \(e_1=a+b\); substituting again yields \(e_2=ab\). Equivalently,
\[
(m-1)a+(\ell-1)b=0,
\qquad (m-1)(\ell-1)(n-2)=0\quad\text{in }k.
\]
When \(m-1\) and \(\ell-1\) are not both zero in \(k\), substitute \(a=-(\ell-1)t\) and \(b=(m-1)t\) into the explicit formula for \(e_2\) to obtain the displayed product condition (the scalar \(t\) is nonzero because \(a\ne b\)). When both integers vanish, the condition holds automatically. The calculation uses that \(2\) is invertible in \(k\). If \(n\not\equiv2\pmod3\), at least one block cardinality is \(1\) modulo three, and the equations force the value on the complementary block to be zero (with the degenerate all-equal case included by allowing full support). Consequently the nonzero critical locus is covered by the affine support lines with \(|S|\equiv1\pmod3\). If \(n\equiv2\pmod3\), the two cardinalities must both be \(1\pmod3\); conversely, their two-block affine planes lie in the critical locus. The all-equal cases are included in the union, by specializing \(a=b\).

**Step 3: impose the cubic equation.** On a constant support line of cardinality \(m\), the cubic restricts to \(\binom m3 a^3\). Lucas's binomial congruence in characteristic three says that, for \(m\equiv1\pmod3\), the coefficient is the residue of \(\lfloor m/3\rfloor\) modulo three. Hence precisely \(m\equiv1\pmod9\) survive.

For the two-block plane with \(m=3u+1\), \(\ell=3v+1\), freshman's dream gives
\[
(1+az)^m(1+bz)^\ell\equiv
(1+az)(1+bz)(1+a^3z^3)^u(1+b^3z^3)^v\pmod{z^4}.
\]
Thus \(e_3\) restricts to \(u a^3+v b^3=(ua+vb)^3\), where the integers \(u,v\) are reduced modulo three. Since \(u+v=(n-2)/3\), there are only three cases:

- \(n\equiv2\pmod9\): \(u+v=0\) in \(k\). If \(u=v=0\), the entire two-block plane lies in the singular scheme; otherwise the cubic vanishes only at \(a=b\), the diagonal, which belongs to every qualifying whole plane.
- \(n\equiv5\pmod9\): \(u+v=1\). If \((u,v)=(0,1)\) or \((1,0)\), a support line remains, with nonzero block size \(1\pmod9\). The residual possibility \((u,v)=(2,2)\) gives \(a=-b\), and both block sizes are \(7\pmod9\).
- \(n\equiv8\pmod9\): \(u+v=2\). The pairs \((0,2)\) and \((2,0)\) give support lines, while \((1,1)\) gives \(a=-b\) with both sizes \(4\pmod9\).

This proves the exhaustive set-theoretic classification and shows that different points in the finite cases do not coincide. In the plane case the only repetitions are complementary partitions; all projective lines contain the diagonal projective point but are otherwise distinct.

**Step 4: generic multiplicity and local length.** For a critical two-block point \((a^m,b^\ell)\), with \(a\ne b\) and \(m,\ell\equiv1\pmod3\), the Hessian has cross-block entries zero and diagonal blocks proportional to \(J_m-I_m\) and \(J_\ell-I_\ell\), where \(J\) is an all-ones matrix. Each block has rank one less than its size, so the Hessian has rank \(n-2\). Because the corresponding affine two-block plane is contained in the gradient zero scheme, the Jacobian criterion and equality of tangent and component dimension show that the gradient scheme is smooth of dimension two at such points. Its local ring is that of the plane. The cubic restricts there to \((ua+vb)^3\). On a proper surviving affine line in this plane this cuts a smooth reduced line raised to the third power, yielding length exactly three after projectivization. On an entire surviving affine plane the cubic vanishes identically, giving generic multiplicity one.

In the remaining residue classes, along a nonzero support line of size \(m\equiv1\pmod3\), the same Hessian calculation gives rank \(n-1\): the support block has rank \(m-1\) and the complementary block has rank \(n-m\), since \(n-2\not\equiv0\pmod3\). Thus the gradient scheme is a smooth affine line near such a point. If its support cardinality is \(1\pmod9\), the cubic vanishes on that line, so the projective singular scheme has local length one.

These calculations also show that in the finite cases there is no hidden local length beyond the stated one. Counting each complementary sign or plane partition twice gives the displayed formulas; summing generic degrees and multiplicities gives the projective scheme degree.

## Verification

The accompanying standard-library program `check.py` exhausts all \(3^n\) points over \(\mathbb F_3\) for \(3\le n\le9\), testing the original cubic and all derivatives against the announced reduced support. It checks the two-block generating-polynomial identity for \(3\le n\le150\), exact Hessian ranks in representative cases, and predicted degrees at \(n=5,8,11,14\). It prints `CHECK_OK` on success. The infinite assertions follow from the symbolic argument above; finite enumerations alone would not prove them.

## Relationship to prior work

Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic* (arXiv:2610.00259v1, September 24, 2026), establishes the dimensions of these loci, the extremal components, and local multiplicities along coordinate components. Its Theorems 1.3–1.4 and Section 7 explicitly do not give a classification of all smaller-dimensional components. The present cubic characteristic-three specialization supplies that missing entire support classification, exact projective degrees, and the previously unaccounted antipodal-sign components (for example, 35 additional points for eight variables). Xie's local coordinate-axis multiplicity theorem agrees with the corresponding part of this result and is not represented as new.

Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics* (arXiv:2509.05009), investigates dimension bounds and their complexity motivation, not these complete projective schemes. Cafure, Matera and Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed–Solomon codes* (arXiv:1109.2265), provide a partition-space method and dimension bounds, rather than these nine-periodic component and degree formulas. Related singular cubic varieties do not contain the given elementary-symmetric cubic family as a stated consequence.

## Limitations

The classification is specific to characteristic three and degree three; it does not classify general elementary symmetric hypersurfaces or all higher-order multiplicity loci. In the case \(n\equiv2\pmod9\), the degree counts the one-dimensional top cycle and does not describe potential embedded components or infinitesimal intersections at the common diagonal point. Publication and indexing searches cannot exclude an unindexed equivalent result, and no independent assessment has been performed.

## References

1. Ying Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (first posted September 24, 2026), https://arxiv.org/html/2610.00259v1 .
2. Ian Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009, https://arxiv.org/abs/2509.05009 .
3. A. Cafure, G. Matera and M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed–Solomon codes*, arXiv:1109.2265, https://arxiv.org/abs/1109.2265 .
