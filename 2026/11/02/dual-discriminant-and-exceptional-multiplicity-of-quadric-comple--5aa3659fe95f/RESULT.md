# Dual discriminant and exceptional multiplicity of quadric-complete-intersection unprojections

## Finding
Let \(n\ge3\). Let \(S\subset\mathbb P^{n+2}_{\mathbb C}\) be a smooth complete intersection of \(n\) quadrics that contains a line \(E\). Put \(h=c_1(\mathcal O_S(1))\) and \(D=(n-1)h+E\). Nasu's unprojection lemma constructs the complete linear system morphism \(f:S\to Y\subset\mathbb P(H^0(S,D)^\vee)\), which contracts precisely \(E\) to a point \(q\) and is an isomorphism off \(E\). Define \(\Pi_q\subset\mathbb P(H^0(S,D))\) to consist of sections vanishing at \(q\).

Define the *discriminant cycle* \(\mathfrak D_D\) to be the pushforward from the universal first-jet-zero incidence \(\{(x,[s]):j_x^1s=0\}\subset S\times\mathbb P(H^0(S,D))\); multiplicities are those of the incidence, not merely those of its reduced image. Then
\[
\boxed{\mathfrak D_D=[Y^\vee]+(n-1)[\Pi_q]}
\qquad\text{and}\qquad
\boxed{\deg(Y^\vee)=(11n^2-31n+24)2^{n-1}+4n-8.}
\]
The dual \(Y^\vee\) is an irreducible hypersurface, different from \(\Pi_q\). The original smooth embedded surface has \(\deg S^\vee=n(n+1)2^{n-1}\). For \(n=3,4,5\), the new dual degrees are \(124,616,2316\), compared with \(48,160,480\) before unprojection. Their degree ratio tends to \(11\) as \(n\to\infty\).

## Assumptions and scope
All geometry is over \(\mathbb C\), and all line bundles and divisor intersections are taken on the *smooth source* \(S\). The target \(Y\) may be singular at \(q\); it is not assumed smooth. Projective dual means the closure of hyperplanes tangent to the smooth locus of the embedded target, not all hyperplanes through the singular point. By a discriminant cycle we mean the first-jet incidence pushforward, with generic multiplicities. The parameter \(n\) ranges over every integer \(n\ge3\), for every smooth complete intersection of the specified type, not only a very general member.

## Proof
**1. The line and its contraction.** Adjunction gives \(K_S=(n-3)h\), \(h^2=2^n\), \(h\cdot E=1\), and \(E^2=1-n\). Hence \(D\cdot E=0\). Nasu, Lemma 2.3, proves that \(|D|\) is basepoint free and gives a birational morphism \(f\) contracting exactly \(E\), with inverse on \(Y\setminus\{q\}\) obtained by projecting away from \(q\). In particular, \(f\) is an isomorphism on \(S\setminus E\).

The exact sequence
\[
0\to\mathcal O_S((n-1)h)\to\mathcal O_S(D)\to\mathcal O_E\to0
\]
has surjective final map on global sections (Nasu, Proposition 2.2). Its kernel consists of sections whose zero divisors include \(E\). Thus \(\Pi_q\) is precisely the linear subsystem \(E+|(n-1)h|\).

**2. Generic exceptional fibres contribute \(n-1\).** Choose a general pencil in \(|D|\). Exactly one pencil parameter lies in \(\Pi_q\). At that parameter the divisor is \(E+R\), where \(R\in|(n-1)h|\) is general, is smooth and meets \(E\cong\mathbb P^1\) transversely at exactly \((n-1)h\cdot E=n-1\) points. Thus the exceptional member has exactly \(n-1\) ordinary double points on \(S\), with no other singularities.

More intrinsically, near any \(t\in E\) use local parameters \((t,z)\), where \(E=(z=0)\), and trivialize \(D\) by the nowhere-zero exceptional section. A variable global section has a local expansion \(s=a+z\,g(t)+O(z^2)\), with \(a=s|_E\in\mathbb C\) constant and with \(g\) the restriction of a member of \(|(n-1)h|\), a polynomial of degree \(n-1\) on \(E\). The critical-point equations over \(E\) are \(a=g(t)=0\). At a simple root \(t_i\), the quadratic term in the local section is \(z\,g'(t_i)(t-t_i)+c z^2\); its Hessian has nonzero determinant. Consequently, \(n-1\) distinct reduced critical-point branches dominate \(\Pi_q\) generically, each of mapping degree one. Hence its coefficient in \(\mathfrak D_D\) is exactly \(n-1\), not merely one.

**3. The other discriminant component is the ordinary projective dual.** Away from \(E\), sections of \(|D|\) contain the image of \(H^0(S,(n-1)h)\). Since \(n-1\ge2\), these sections separate second-order jets at any fixed point of \(S\setminus E\): degree-\((n-1)\) polynomials on the ambient projective space separate two-jets on the embedded smooth surface. The first-jet incidence is therefore regular over \(S\setminus E\), and a general singular section there has a nondegenerate quadratic term (an ordinary node). The closure of this incidence is the irreducible conormal variety of \(Y\), so its image is \(Y^\vee\), and generic characteristic-zero conormal reflexivity makes its degree over the dual image equal to one. The existence of ordinary tangencies follows also from the positive count in Step 4 after removing the exceptional contribution. In particular \(Y^\vee\) is a hypersurface; choosing general jets with \(s|_E\ne0\) shows that it differs from \(\Pi_q\).

**4. Total discriminant count.** For a generic pencil in the complete system, its base scheme consists of \(D^2\) transverse points, none on \(E\). Blowing them up produces a fibration over \(\mathbb P^1\), with Euler characteristic \(e(S)+D^2\). A smooth member has genus determined by \(2g-2=D(D+K_S)\), hence Euler characteristic \(e(C)=-D(D+K_S)\). By Step 2 and by second-jet separation away from \(E\), each singular fibre has only ordinary nodes, all outside \(E\) except for the one special parameter. Comparing Euler characteristics of the fibration and smooth fibres yields the total nodal count
\[
N_D=e(S)+3D^2+2K_S\cdot D
=\int_S c_2(J^1\mathcal O_S(D)).
\]
The jet-bundle equality follows independently from the exact sequence \(0\to\Omega_S^1\otimes\mathcal O_S(D)\to J^1\mathcal O_S(D)\to\mathcal O_S(D)\to0\). For the smooth complete intersection,
\[
c(T_S)=\frac{(1+h)^{n+3}}{(1+2h)^n},\qquad
e(S)=(n^2-3n+6)2^{n-1}.
\]
The intersections are
\[
D^2=(n-1)^2 2^n+n-1,\qquad
K_S\cdot D=(n-3)((n-1)2^n+1).
\]
Thus
\[
N_D=(11n^2-31n+24)2^{n-1}+5n-9.
\]
The exceptional fibre contributes exactly \(n-1\) ordinary nodes, while each generic node away from \(E\) corresponds to one hyperplane tangent to \(Y\) at a smooth point. Therefore
\[
\deg Y^\vee=N_D-(n-1)=(11n^2-31n+24)2^{n-1}+4n-8,
\]
and the asserted discriminant cycle decomposition follows.

**5. Comparison with the original embedding.** For the very ample class \(h\), the same jet Chern calculation yields
\[
\deg(S^\vee)=e(S)+2K_S\cdot h+3h^2
=n(n+1)2^{n-1}.
\]
The ratio of the two displayed degrees is \(11+O(1/n)\), proving the asymptotic statement.

## Verification
The supplied standalone script `verify_dual_unprojection.py` uses exact integer arithmetic to extract the coefficient of \(h^2\) in \((1+h)^{n+3}(1+2h)^{-n}\), independently reconstruct all intersection numbers and the Euler-pencil count, and compare them with the closed forms for \(2\le n\le100\). It checks genus parity, the exceptional nodal subtraction and four small cases. It emits `VERIFY_OK`. The script is a finite consistency check; the proof for every \(n\ge3\) is the geometric argument and symbolic identities above.

## Relationship to prior work
Nasu, *Obstructions to deforming space curves lying on a complete intersection of quadrics* (2026), §2.1, Proposition 2.2 and Lemma 2.3, constructs the unprojection and describes the contraction, but does not state a projective-dual degree or exceptional discriminant multiplicity. The current finding uses those established geometric facts, not a claim of priority for the unprojection. General first-jet and polar-class formulas underlie the total discriminant calculation, and the classical smooth quintic del Pezzo case \(n=2\) supplies a boundary consistency check; neither is claimed as new. The combination here gives the exceptional multiplicity and a closed degree formula for the higher-codimension unprojection series. Classical polar formulas might imply this result with additional local analysis; independent historical-priority verification remains open.

## Limitations
The statement requires smooth complex complete intersections containing a line, and the complete \(|(n-1)h+E|\) model. It does not compute higher polar degrees, the full singularity stratification of \(Y\), or analogue formulas for other contracted curves. The multiplicity \(n-1\) belongs to the incidence discriminant cycle on \(|D|\), not to the reduced hypersurface \(Y^\vee\). The finite checks do not certify the infinite statement independently.

## References
- Hirokazu Nasu, *Obstructions to deforming space curves lying on a complete intersection of quadrics*, arXiv:2610.30962v1, first submitted 2026-10-22, particularly §2.1, Proposition 2.2 and Lemma 2.3; https://arxiv.org/html/2610.30962v1.
- Hirokazu Nasu, *Obstructions to deforming space curves lying on a del Pezzo surface*, *Manuscripta Mathematica* 177 (2026), article 33, doi:10.1007/s00229-026-01714-6 (the degree-four/del Pezzo boundary geometry).
- Ingrid Bauer and Fabrizio Catanese, *Equivariant syzygies for the Del Pezzo surface of degree 5*, *Rendiconti del Circolo Matematico di Palermo* 70 (2021), 97–120, doi:10.1007/s12215-020-00483-9 (classical fifth-degree surface model).
