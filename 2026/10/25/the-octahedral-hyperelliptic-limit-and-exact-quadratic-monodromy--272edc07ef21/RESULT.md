# The octahedral hyperelliptic limit and exact quadratic monodromy at the double-conic Ciani boundary

## Finding

For an algebraically closed field \(k\) of characteristic distinct from \(2,3\), the symmetric Ciani family
\[
C_q: x^4+y^4+z^4+(2+q)(x^2y^2+y^2z^2+z^2x^2)=0
\]
over \(K=k((q))\) acquires good reduction after \(s^2=q\). Its smooth special fiber is the octahedral hyperelliptic genus-three curve
\[
H:W^2=U^8+14U^4V^4+V^8.
\]
The nontrivial element of \(\mathrm{Gal}(k((s))/k((q)))\) specializes to the hyperelliptic involution; thus tame inertia acts by \(-1\) on every six-dimensional auxiliary-adic first cohomology. The minimal ramification index for good reduction is \(2\), not \(1\).

## Assumptions and scope

The residue field \(k\) is algebraically closed, \(\operatorname{char}k\notin\{2,3\}\). The parameters \(q\) and \(s\) are formal uniformizers, \(K=k((q))\), \(K'=k((s))\) with \(q=s^2\). Good reduction means a smooth, proper, geometrically connected relative curve over the corresponding complete discrete valuation ring. The statement concerns this specific one-parameter degeneration; it neither identifies every Ciani boundary nor extends to residue characteristic two or three. No assertion is made that the abstract hyperelliptic octahedral curve or the general existence of stable reduction is new.

## Proof

Put
\[
Q=x^2+y^2+z^2,\qquad R=x^2y^2+y^2z^2+z^2x^2.
\]
The family is \(Q^2+qR=0\). Over \(k[[q]]\) it specializes to a double smooth conic \(Q^2=0\); the generic fiber is smooth. Indeed, for the quartic with parameter \(t\), differentiation gives \(2x(2x^2+t(y^2+z^2))\) and its cyclic companions. If all three coordinates are nonzero and \(t\ne2\), subtracting the normalized derivatives forces their squares to agree, and the curve equation gives \(t=-1\). If exactly two coordinates are nonzero, the derivative equations force \(t^2=4\). A one-coordinate point never lies on the quartic. Thus singular fibers can occur only for \(t\in\{-2,-1,2\}\). Since \(t=2+q\) is transcendental over \(k\), the generic curve is a smooth plane quartic of genus three.

Base change \(q=s^2\) and blow up the ambient \(\mathbb P^2_{k[[s]]}\) along \((s,Q)\), retaining the strict transform of \(Q^2+s^2R=0\). On the chart \(Q=sw\) its defining equations are
\[
Q=sw,\qquad w^2+R=0.
\]
On the complementary chart \(s=Qv\), the strict-transform equation is \(1+v^2R=0\). That chart contains no additional component in the special fiber: if \(s=0\) and \(Q\ne0\), then \(v=0\) and the equation reads \(1=0\). The two charts therefore glue to the double cover of \(Q=0\) cut out by \(w^2=-R\). The blow-up is projective, and these equations show the resulting special fiber is the asserted double cover with no exceptional extra components.

Choose \(i\in k\) with \(i^2=-1\). A parametrization of the conic is
\[
[x:y:z]=[2UV:U^2-V^2:i(U^2+V^2)].
\]
Substitution gives the exact homogeneous identity
\[
R|_{Q=0}=-(U^8+14U^4V^4+V^8),
\]
so the special curve is \(H\) as displayed. Its branch divisor has eight distinct points, because
\[
\operatorname{Disc}_U(U^8+14U^4+1)=2^{40}3^4,
\]
which is invertible in \(k\). The double cover of \(\mathbb P^1_k\) is smooth of genus \((8-2)/2=3\). Since its special fiber is smooth and its generic fiber is smooth, the strict transform is a smooth proper family over \(k[[s]]\): in a neighborhood of the special fiber, smoothness follows directly from the Jacobian criterion in the displayed blow-up charts, and properness implies these neighborhoods cover the entire special fiber; the generic fiber is the original smooth quartic. Thus this is a good-reduction model (and therefore a stable model).

The deck involution \(\tau:s\mapsto-s\) leaves the original coordinates \(x,y,z\) fixed and sends \(w=Q/s\) to \(-w\). On \(H\) it is exactly the hyperelliptic involution. Since \(H/\langle\tau\rangle\cong\mathbb P^1_k\), for any auxiliary prime \(\ell\ne\operatorname{char}(k),2\) the invariant part of \(H^1_{\mathrm{\acute et}}(H_{\bar k},\mathbb Q_\ell)\) vanishes. As \(\tau^2=1\) and characteristic of the coefficients is zero, \(\tau\) acts as \(-\mathrm{Id}\) on the full six-dimensional space. Smooth-proper base change transfers this to the generic fiber after adjoining \(s\). The tame inertia image is therefore precisely the nontrivial group of order two. If there were good reduction over the original \(K\), inertia would act trivially on \(H^1\), a contradiction. Over any finite extension of odd ramification index the action remains nontrivial, while \(K'/K\) has index two and provides good reduction. The minimal ramification index is exactly two.

## Verification

The attached standalone `check_stable_limit.py` is reproducible with Python 3 and SymPy. It checks the exact homogeneous conic parametrization, the eight-degree branch identity and discriminant factorization; reconstructs the quartic square-completion and the strict-transform substitution; verifies generic singular-parameter alternatives symbolically. These finite symbolic checks certify algebraic equalities. The properness and smoothness of the blow-up, the Galois action, and the inertia argument are mathematical deductions detailed above, not inferred from experiment.

## Relationship to prior work

Lercier–Ritzenthaler–Rovetta–Sijsling explicitly give the same one-parameter symmetric \(S_4\)-quartic family and identify \(t=2\) as a singular boundary parameter. Bouw et al. (2021) classify stable-reduction *types* for the larger Ciani stratum and give invariants of positive-genus components; their complete 48-page source was not accessible for a decisive statement-level comparison. The abstract of Bouw et al. (2025) discusses potentially good reduction and conductor exponents of non-special Ciani quartics, but does not state this explicit quadratic monodromy computation. The octahedral hyperelliptic genus-three curve itself has historical antecedents and is not claimed new. The present finding isolates the explicit degeneration and establishes its exact quadratic inertia mechanism.

## Limitations

This result is over algebraically closed residue fields of characteristic not two or three. The stable isomorphism class is not presented as a newly classified abstract curve. The full 2021 Ciani-reduction monograph and complete 2025 conductor paper could not be examined, so equivalent prior explicit computations cannot be excluded; no absolute priority claim is made. The result does not compute conductors over arbitrary arithmetic bases. There has been no independent mathematical audit.

## References

1. Lercier, Ritzenthaler, Rovetta, Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, LMS J. Comput. Math. 17 (2014), 128–147; arXiv:1403.0562; https://doi.org/10.1112/S146115701400031X.
2. Bouw, Coppola, Kılıçer, Kunzweiler, Lorenzo García, Somoza, *Reduction Types of Genus-3 Curves in a Special Stratum of their Moduli Space*, Women in Numbers Europe III (2021), 115–162; arXiv:2003.07633; https://doi.org/10.1007/978-3-030-77700-5_4.
3. Bouw, Coppola, Lorenzo García, Somoza, *On the Conductor of Ciani Plane Quartics*, La Matematica 4 (2025), 643–673; arXiv:2310.10416; https://doi.org/10.1007/s44007-025-00156-y.
4. Rodríguez and González-Aguilera, *Fermat's quartic curve, Klein's curve and the tetrahedron*, Extremal Riemann Surfaces, Contemporary Mathematics 201 (1997), 43–62. (Historical octahedral-curve antecedent; full text not inspected.)
