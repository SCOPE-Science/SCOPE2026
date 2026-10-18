# Six arithmetic isogeny classes in a natural genus-two code family

## Finding

Work over \(\mathbb F_{19}\). Let \(C_a\) be the smooth projective curve
\[
C_a:\quad y^2=x^6+a x^3+1,
\]
where \(a\) runs through the **entire** set of coefficients for which this family satisfies the separability, no-rational-root and nonempty-affine-evaluation hypotheses of Beshaj--Shaska:
\[
A=\{0,3,4,5,6,7,8,9,10,11,12,13,14,15,16\}.
\]
The Jacobians of these fifteen curves fall into **exactly six** \(\mathbb F_{19}\)-isogeny classes. In fact, for each \(a\in A\) there is an \(\mathbb F_{19}\)-elliptic curve
\[
E_a:\quad w^2=(t+2)(t^3-3t+a)
\]
such that \(\operatorname{Jac}(C_a)\) is \(\mathbb F_{19}\)-isogenous to \(E_a^2\). Write \(\tau_a=20-\#E_a(\mathbb F_{19})\). The complete partition is:

| Parameters \(a\) | \(\tau_a\) | \(\#E_a(\mathbb F_{19})\) | \(\#\operatorname{Jac}(C_a)(\mathbb F_{19})\) |
| --- | ---: | ---: | ---: |
| \(\{7,12\}=\{\pm7\}\) | \(-7\) | \(27\) | \(729\) |
| \(\{5,14\}=\{\pm5\}\) | \(-4\) | \(24\) | \(576\) |
| \(\{9,10\}=\{\pm9\}\) | \(-1\) | \(21\) | \(441\) |
| \(\{4,6,8,11,13,15\}=\{\pm4,\pm6,\pm8\}\) | \(2\) | \(18\) | \(324\) |
| \(\{3,16\}=\{\pm3\}\) | \(5\) | \(15\) | \(225\) |
| \(\{0\}\) | \(8\) | \(12\) | \(144\) |

For each row the entire Hasse--Weil numerator is
\[
L_{C_a}(T)=(1-\tau_a T+19T^2)^2.
\]
In particular, the distinct geometrically non-isomorphic curves with \(a=6\) and \(a=8\) in Beshaj--Shaska's Theorem 10.1 have **isogenous** Jacobians over \(\mathbb F_{19}\), with shared numerator
\[
L(T)=(1-2T+19T^2)^2
=1-4T+42T^2-76T^3+361T^4.
\]
The previously computed hull-profile partition has seven values; this arithmetic isogeny partition has only six. In particular, the single isogeny class \(\{\pm4,\pm6,\pm8\}\) contains curves from two different hull-profile classes.

## Assumptions and scope

The base field is exactly \(\mathbb F_{19}\), and the parameter domain is exactly \(A\) above; this is a classification of *equations in this family*, not a count of isomorphism classes of curves. The affine polynomial is squarefree whenever \(a\ne\pm2\), since its only possible multiple roots away from zero arise from \(u=x^3=-a/2\) and force \(a^2=4\). A direct finite check of the rational-root and nonempty-evaluation conditions, specified below, gives precisely the fifteen values of \(A\). The smooth projective model has genus two, and two rational points lie above infinity because the sextic is monic.

Two genus-two Jacobians over \(\mathbb F_{19}\) are said to be isogenous here if there is an isogeny *defined over \(\mathbb F_{19}\)*. We classify them using equality of their Frobenius polynomials, invoking the isogeny criterion for abelian varieties over finite fields. No claim is made about isomorphism of the principally polarized Jacobians, or isomorphism of the original curves.

## Proof

**1. Elliptic quotient.** The rational automorphism
\[
\beta:(x,y)\longmapsto(1/x,y/x^3)
\]
has order two and preserves the function field of \(C_a\). Its fixed functions
\[
t=x+x^{-1},\qquad w=y(x+1)x^{-2}
\]
satisfy
\[
w^2=(x^3+a+x^{-3})(x+2+x^{-1})
=(t^3-3t+a)(t+2).
\]
Generically, \(x\) has degree two over \(\mathbb F_{19}(t,w)\), because it satisfies \(x^2-tx+1=0\) and the extension has the nontrivial automorphism \(\beta\); then \(y=wx^2/(x+1)\). Thus the displayed quartic is the full quotient function field. For \(a\in A\) its quartic is separable: the cubic \(t^3-3t+a\) has no repeated root when \(a^2\ne4\), and it does not vanish at \(t=-2\) for the same reason. The smooth quotient has genus one and the rational point \((t,w)=(-2,0)\), so it is an elliptic curve \(E_a\).

**2. Two independent quotient maps.** Choose \(\zeta=7\in\mathbb F_{19}\), a primitive cube root of unity. The order-three automorphism \(\alpha:(x,y)\mapsto(\zeta x,y)\) conjugates \(\beta\) to another involution \(\beta'=\alpha\beta\alpha^{-1}\). Its quotient is \(\mathbb F_{19}\)-isomorphic to \(E_a\). On the two-dimensional differential space of \(C_a\), with basis \(\omega_1=dx/y\), \(\omega_2=x\,dx/y\), we have
\[
\alpha^*(\omega_1)=\zeta\omega_1,\quad
\alpha^*(\omega_2)=\zeta^2\omega_2,\quad
\beta^*(\omega_1)=-\omega_2,\quad
\beta^*(\omega_2)=-\omega_1.
\]
The invariant lines of \(\beta^*\) and \(\beta'^*\) differ, because \(\zeta\ne\zeta^2\). Since the characteristic is neither two nor three, they are linearly independent. Hence the sum of the two elliptic quotient pullbacks induces an isomorphism on tangent spaces at the identity, and the resulting map \(E_a\times E_a\to\operatorname{Jac}(C_a)\) is an \(\mathbb F_{19}\)-isogeny. This elementary split-Jacobian mechanism is classical; the exact parameter-to-isogeny-class partition below is the new calculation.

**3. Exhaustive six-class calculation.** The quartic in the formula for \(E_a\) is monic of degree four, so it has two rational points over infinity. Let \(\chi\) be the quadratic character of \(\mathbb F_{19}\), extended by \(\chi(0)=0\). Then
\[
\#E_a(\mathbb F_{19})=21+
\sum_{t=0}^{18}\chi\bigl((t+2)(t^3-3t+a)\bigr),
\qquad
\tau_a=-1-\sum_{t=0}^{18}\chi\bigl((t+2)(t^3-3t+a)\bigr).
\]
These are nineteen-term *exhaustive* finite sums. Exact evaluation for all fifteen admissible parameters yields the six rows in the Finding table. Since elliptic curves over a finite field are isogenous precisely when their traces agree, their squares give exactly those six abelian-surface isogeny classes. The preceding isogeny proves the asserted zeta polynomial for every parameter, not just in enumerated extension degrees.

## Verification

Run `python3 VERIFY.py` using only Python's standard library; `COUNT_CERTIFICATE.txt` records the output. The verifier independently re-derives the complete admissible set, all nineteen-term elliptic character sums, and for every admissible parameter counts \(C_a\) directly over both \(\mathbb F_{19}\) and \(\mathbb F_{19^2}\). It realizes the latter as \(\mathbb F_{19}[v]/(v^2-2)\) and evaluates the quadratic character by the norm to \(\mathbb F_{19}\). These curve point counts agree with the predictions of the squared elliptic Frobenius factor in every case. They are verification of finite calculations, not a substitute for the isogeny argument in step 2.

For \(a=6\) and \(a=8\), the two independent curve counts are \(\#C_a(\mathbb F_{19})=16\) and \(\#C_a(\mathbb F_{19^2})=430\). The rational Jacobian cardinality is \(324\) in each case.

## Relationship to prior work

Beshaj--Shaska, arXiv:2610.04856v1, Section 10 and Theorem 10.1, introduce the complete admissible fifteen-parameter domain, tabulate seven hull profiles, and prove the geometric nonisomorphism of the curves with parameters six and eight. They do not provide the above six Frobenius-trace classes or their complete isogeny-class partition. Their computation of rational affine points already implies the shared *first* trace for that distinguished pair, but not the full zeta numerator without the elliptic splitting argument.

Cardona--Quer, arXiv:math/0203165v1, treat the general geometry and arithmetic of dihedral genus-two curves and elliptic quotients. The existence of elliptic subcovers, their relations and the broad splitting principle are therefore treated here as prior knowledge, not claimed as new. Their general work does not state the particular fifteen-parameter \(\mathbb F_{19}\) trace table in this result. A public abelian-variety isogeny database catalogs many \(\mathbb F_{19}\) classes but the inspected class pages do not supply this source-family-specific partition. General catalogued L-polynomials are not by themselves the map from these specific fifteen equations to classes.

## Limitations

This is a classification of the specified finite family of equations, not a classification of all genus-two curves or all isogenies over \(\mathbb F_{19}\). The split-Jacobian structural lemma has antecedents in dihedral-curve literature; only the full parameter-to-arithmetic-class partition and its relationship to the cited hull-profile example are proposed as new. The catalogue of abelian varieties over \(\mathbb F_{19}\) is extensive and could implicitly subsume isolated polynomial entries; an unindexed table or an unrecognized equivalent normalization is a residual originality risk. No geometric or polarized-Jacobian isomorphism is asserted.

## References

1. L. Beshaj and T. Shaska, *Code Equivalence and Automorphism Groups of Weighted Superelliptic Codes*, arXiv:2610.04856v1 (first public 2026-10-04), especially Section 10 and Theorem 10.1, https://arxiv.org/html/2610.04856v1.
2. G. Cardona and J. Quer, *Curves of genus 2 with group of automorphisms isomorphic to D8 or D12*, arXiv:math/0203165v1 (2002), Sections 2 and 5, https://arxiv.org/html/math/0203165v1.
3. LMFDB, *Abelian varieties over finite fields*, abelian-surface isogeny-class database for \(\mathbb F_{19}\), https://www.lmfdb.org/Variety/Abelian/Fq/2/19/ab_as (a representative class page, not a claimed match to the calculated six classes).
