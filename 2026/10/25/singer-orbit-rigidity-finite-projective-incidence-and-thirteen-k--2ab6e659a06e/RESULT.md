# Singer-orbit rigidity, finite-projective incidence, and thirteen Klein quartics over \(\mathbb F_3\)

## Finding

Let \(q\) be any prime power of characteristic \(p\), let \(n\geq1\), and let \(d\geq2\) satisfy \(p\nmid d\). Put \(E=\mathbb F_{q^{n+1}}\). Choose a normal basis \(\beta,\beta^q,\ldots,\beta^{q^n}\) of \(E/\mathbb F_q\) and define, for \(\lambda\in E^\times\),
\[
F_\lambda(X_0,\ldots,X_n)=\operatorname{Tr}_{E/\mathbb F_q}\!\left(\lambda\left(\sum_{i=0}^n\beta^{q^i}X_i\right)^d\right).
\]
Write \(H_\lambda\subset\mathbb P^n_{\mathbb F_q}\) for the projective hypersurface \(F_\lambda=0\), and let \(N=(q^{n+1}-1)/(q-1)\).

The following are properties of this particular normal-basis linear system, whose existence and smoothness were established by Asgarli--Ghioca--Reichstein [1].

**Singer orbits.** The \(N\) distinct \(\mathbb F_q\)-rational members are indexed by \(E^\times/\mathbb F_q^\times\). The natural multiplication subgroup of \(\operatorname{PGL}_{n+1}(\mathbb F_q)\) has exactly \(g=\gcd(d,N)\) orbits on them, each of size \(N/g\). In particular, if \(g=1\), all rational members are \(\mathbb F_q\)-projectively isomorphic.

**Finite-projective incidence.** If \(g=1\), there is a bijection of the rational point set \(\mathbb P^n(\mathbb F_q)\) with itself under which the rational-point subsets \(H_\lambda(\mathbb F_q)\) become precisely the point sets of all \(\mathbb F_q\)-hyperplanes, counted once. Thus every rational member has exactly \((q^n-1)/(q-1)\) rational points, and all incidences, including intersections of any collection of these subsets, equal the corresponding ordinary point--hyperplane incidences. In particular, for \(n=2\), any two different rational members share exactly one \(\mathbb F_q\)-point (they can, of course, meet at additional geometric points).

**An infinite family of homogeneous smooth nets.** For \(n=2\) and \(d=q+1\), one has \(\gcd(q+1,q^2+q+1)=1\). Consequently all \(q^2+q+1\) rational curves in this smooth plane net are projectively isomorphic over \(\mathbb F_q\), each has genus \(q(q-1)/2\) and exactly \(q+1\) rational points, and their rational-point blocks are the projective-plane \(2\)-design with parameters \((q^2+q+1,q+1,1)\).

**Exact characteristic-three identification.** Take \(q=3,n=2,d=4\), put \(E=\mathbb F_3[t]/(t^3-t-1)\), and choose \(\beta=t^2\). All thirteen rational curves of the resulting net are \(\mathbb F_3\)-projectively isomorphic to the classical Klein curve
\[
K:\quad X_0^3X_1+X_1^3X_2+X_2^3X_0=0.
\]
They have the common Hasse--Weil zeta function
\[
\boxed{Z(H_\lambda/\mathbb F_3,T)=\frac{1+27T^6}{(1-T)(1-3T)}}.
\]
Their thirteen four-point sets in \(\mathbb P^2(\mathbb F_3)\) form a symmetric \(2\)-\((13,4,1)\) incidence design. For every integer \(m\geq1\), the extension-field count is
\[
\#H_\lambda(\mathbb F_{3^m})=
\begin{cases}
3^m+1,&6\nmid m,\\
3^m+1-6(-27)^{m/6},&6\mid m.
\end{cases}
\]
In particular, each curve is maximal over \(\mathbb F_{3^6}\), with \(892\) points; its reciprocal Frobenius polynomial factors as
\[
1+27T^6=(1+3T^2)(1-3T+3T^2)(1+3T+3T^2).
\]

## Assumptions and scope

The trace in the displayed homogeneous equation is taken **coefficientwise** on the polynomial with coefficients in \(E\); when the variables take values in \(\mathbb F_q\), it equals the usual field trace of the evaluated element. The base field is always a finite field. All assertions about smoothness concern every rational **member** of the linear system and its smoothness over an algebraic closure, not the false statement that every geometrically parametrized member is smooth. Isomorphisms are induced by projective linear transformations defined over the stated finite field. If \(g>1\), the orbit count is for the indicated Singer subgroup; no assertion is made that those orbits remain distinct under the full projective group. The incidence assertion is about rational-point sets, not scheme-theoretic intersections.

For the characteristic-three case, the polynomial \(t^3-t-1\) is irreducible over \(\mathbb F_3\), the element \(t\) has multiplicative order \(13\), and \(t^2,(t^2)^3,(t^2)^9\) form a normal basis of \(E/\mathbb F_3\).

## Proof

**1. The smooth system and its parameters.** Let \(Y_j=\sum_{i=0}^n\beta^{q^{i+j}}X_i\), where exponents of \(\beta\) are read modulo \(n+1\) in the Frobenius cycle. The Moore matrix transforming \((X_i)\) into \((Y_j)\) is invertible over \(E\) because the conjugates of \(\beta\) form a normal basis. Expanding the field trace as a polynomial gives
\[
F_\lambda=\sum_{j=0}^{n}\lambda^{q^j}Y_j^d.
\]
All diagonal coefficients are nonzero when \(\lambda\ne0\); since \(p\nmid d\), the Jacobian criterion proves geometric smoothness. The diagonal forms \(Y_j^d\) are linearly independent, so the map \(\lambda\mapsto F_\lambda\) is an injective \(\mathbb F_q\)-linear map from \(E\) to degree-\(d\) forms. Its projectivization is an \(n\)-plane with exactly \(N\) distinct rational members. These geometric ingredients and the normal-basis construction are prior work [1], not a novelty assertion here.

**2. Singer orbits and the incidence formula.** Identify \(\mathbb F_q^{n+1}\) with \(E\) by the normal-basis linear map \((x_i)\mapsto y=\sum_i\beta^{q^i}x_i\). Multiplication by any \(\nu\in E^\times\) is then an \(\mathbb F_q\)-linear invertible substitution \(M_\nu\) of the \(X_i\), and direct substitution gives
\[
F_\lambda(M_\nu X)=F_{\lambda\nu^d}(X).
\]
Scalar multiplication by \(\mathbb F_q^\times\) has no effect on the projective substitution, so the Singer group \(G=E^\times/\mathbb F_q^\times\) is cyclic of order \(N\). Its action on the \(N\) member labels is multiplication by the subgroup \(G^d\), which has index \(g=\gcd(d,N)\). This proves the exact orbit statement.

A rational point corresponds to \([y]\in G\). The incidence \([y]\in H_\lambda(\mathbb F_q)\) holds precisely when \(\operatorname{Tr}(\lambda y^d)=0\). When \(g=1\), the map \([y]\mapsto[y^d]\) is a permutation of \(G\), and the nondegenerate trace pairing \((\lambda,z)\mapsto\operatorname{Tr}(\lambda z)\) identifies projective parameter labels \([\lambda]\) with every hyperplane in \(\mathbb P(E)\). Thus the incidence is exactly the ordinary point--hyperplane design transported by this point permutation. A hyperplane in \(\mathbb P^n(\mathbb F_q)\) has \((q^n-1)/(q-1)\) points. In the plane case two different trace hyperplanes intersect in one projective point, and every pair of points lies on exactly one trace hyperplane. Finally \(q^2+q+1\equiv1\pmod{q+1}\), proving the claimed infinite family.

**3. Identification with the characteristic-three Klein curve.** In \(E=\mathbb F_3[t]/(t^3-t-1)\), take \(\beta=t^2\) and \(\lambda=1\). The exact trace expansion is
\[
\begin{aligned}
P(X_0,X_1,X_2)={}&X_0^4+2X_0^3X_1+X_0^3X_2+X_0X_1^3+2X_0X_2^3\\
&+X_1^4+2X_1^3X_2+X_1X_2^3+X_2^4.
\end{aligned}
\]
With
\[
A=\begin{pmatrix}1&1&2\\2&1&1\\1&2&1\end{pmatrix}\in\operatorname{GL}_3(\mathbb F_3),\qquad\det A=1,
\]
one checks, by expansion in \(\mathbb F_3[X_0,X_1,X_2]\), that \(P(A X)=X_0^3X_1+X_1^3X_2+X_2^3X_0\). The standalone checker verifies this complete polynomial identity coefficient by coefficient. Since \(N=13\) and \(\gcd(4,13)=1\), Step 2 sends every rational parameter to \(\lambda=1\) by an \(\mathbb F_3\)-projective change of coordinates. All thirteen curves therefore are Klein quartics over \(\mathbb F_3\), and the preceding incidence theorem gives their complete \(2\)-\((13,4,1)\) rational-point design without relying on finite sampling.

**4. Exact zeta function.** A nonsingular plane quartic has genus \(3\). For \(k=1,2,3\), use the exact field presentations
\[
\mathbb F_3,\quad \mathbb F_3[u]/(u^2+1),\quad\mathbb F_3[t]/(t^3-t-1).
\]
Every rational projective point is uniquely represented by one of \([1:y:z]\), \([0:1:z]\), and \([0:0:1]\). Exhaustive exact field evaluation of the displayed Klein equation gives the following numbers of zeros in these three disjoint charts:

| Field | \([1:y:z]\) | \([0:1:z]\) | \([0:0:1]\) | Total |
|:--|--:|--:|--:|--:|
| \(\mathbb F_3\) | 2 | 1 | 1 | 4 |
| \(\mathbb F_9\) | 8 | 1 | 1 | 10 |
| \(\mathbb F_{27}\) | 26 | 1 | 1 | 28 |

The accompanying portable exact-arithmetic program independently enumerates both the Klein polynomial and the expanded trace polynomial and agrees in all three fields. Write \(s_k=3^k+1-\#K(\mathbb F_{3^k})\). The table yields \(s_1=s_2=s_3=0\). Newton identities therefore force the first three nonconstant coefficients of the degree-six numerator to vanish; the genus-three Weil functional equation forces coefficients four and five to vanish and the final coefficient to be \(3^3=27\). This proves \(L_K(T)=1+27T^6\). Its reciprocal eigenvalues have sixth powers equal to \(-27\), so their power sums vanish unless \(6\mid m\), when the power sum is \(6(-27)^{m/6}\). This proves the count for **every** positive \(m\), beyond the three exact finite computations. The Weil bound at \(m=6\) is attained because \(3^6+1+6\sqrt{3^6}=892\).

## Verification

Run `python3 verify.py` using only the Python standard library. It checks the irreducible-field arithmetic, order and normality conditions, the complete trace expansion, the invertible change of coordinates to the Klein quartic, independent exhaustive point counts over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), the thirteen four-point blocks and every block/point incidence, and the Newton-identity coefficients. Its final marker is `VERIFY_OK`. Structural statements for all \(q,n,d\) are supported by the proofs of Steps 1 and 2, **not** inferred from those finite checks.

## Relationship to prior work

Asgarli--Ghioca--Reichstein [1], Section 3, construct the normal-basis \(\mathbb F_q\)-smooth system and prove its parameter dimension and geometric smoothness. Those assertions are imported, not claimed as new. The Singer subgroup orbit count, its rational point--hyperplane incidence interpretation, the resulting full family of \(q+1\)-degree isotrivial smooth nets, and the identification of the thirteen characteristic-three rational members with Klein quartics are the present contributions.

Meagher--Top [2] already explain the exceptional characteristic-three geometry of Klein and Fermat quartics, which is not new here; their displayed twist classifications in Section 7 explicitly assume characteristic at least five. Lercier--Ritzenthaler--Rovetta--Sijsling [3] address plane-quartic moduli and twist enumeration but not this net; their general theory assumes characteristic above seven, and their enumerated trace distributions concern primes at least eleven. Dolgachev [5, Section 4.2] also establishes the exceptional characteristic-three equivalence between Klein and Fermat quartics over the algebraic closure, without identifying the trace-net members or their finite-field incidence. The classical Klein polynomial and its own arithmetic are pre-existing objects. The zeta calculation above is supplied as an exact arithmetic consequence for the **entire explicitly embedded net**, not as a claim that a new genus-three isogeny class was discovered.

## Limitations

No uniqueness is claimed among all \(\mathbb F_q\)-smooth linear systems, and no classification of the full \(\operatorname{PGL}_{n+1}(\mathbb F_q)\)-orbits is given when \(g>1\). The rational-point incidence design does not imply that the hypersurfaces are hyperplanes as schemes. The displayed zeta function applies only to the specified characteristic-three quartic net; the arbitrary-\(q\) result supplies exact base-field incidence, not complete extension-field zeta functions. Some older finite-geometry or characteristic-three Klein computations could contain equivalent subclaims; the net-specific combination was not identified in the inspected literature. Independent validation has not been performed.

## References

1. S. Asgarli, D. Ghioca, Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918, first public 2 July 2022, Section 3, especially the normal-basis construction and Lemma 3. https://arxiv.org/abs/2207.00918
2. S. Meagher, J. Top, *Twists of genus three curves over finite fields*, Finite Fields Appl. 16 (2010), 347--368, Sections 4, 7, 8. https://doi.org/10.1016/j.ffa.2010.06.001
3. R. Lercier, C. Ritzenthaler, F. Rovetta, J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, LMS J. Comput. Math. 17 (2014), 128--147, arXiv:1403.0562. https://arxiv.org/abs/1403.0562
4. S. Asgarli, D. Ghioca, Z. Reichstein, *Linear system of hypersurfaces passing through a Galois orbit*, arXiv:2310.10361 (2023); related finite-field linear-system setting, but different irreducibility rather than the present trace-net arithmetic. https://arxiv.org/abs/2310.10361
5. I. Dolgachev, *Automorphisms of del Pezzo surfaces in odd characteristic*, J. Lond. Math. Soc. 109 (2024), Section 4.2, including Corollary 4.6. https://doi.org/10.1112/jlms.12905
