# Exact genus-four closed-point threshold over \(\mathbf F_4\)

## Finding

**Theorem.** Let \(\rho(q,g)\) be the least integer \(r_0\) such that every smooth projective geometrically integral curve of genus \(g\) over \(\mathbf F_q\) has a closed point of every degree \(r\ge r_0\). Then

\[
\rho(4,4)=4.
\]

The upper bound is the published general estimate of Aubry–Herbaut–Monaldi. The matching lower bound is witnessed by the smooth projective model of

\[
C:\quad y^2+y=x^9+\omega,\qquad
\mathbf F_4=\mathbf F_2[\omega]/(\omega^2+\omega+1).
\]

This genus-four curve has exactly one point over each of \(\mathbf F_4\) and \(\mathbf F_{64}\), namely its point above infinity, so it has no closed point of degree three.

## Assumptions and scope

All curves are smooth, projective, and geometrically integral. A closed point of degree \(r\) on a curve over \(\mathbf F_q\) means a closed point whose residue field has degree exactly \(r\) over \(\mathbf F_q\). Write \(N_r=\#C(\mathbf F_{q^r})\) and \(B_r\) for the number of degree-\(r\) closed points. Then \(N_r=\sum_{d\mid r}dB_d\). The claim concerns only the single threshold pair \((q,g)=(4,4)\); it does not classify curves of genus four or determine \(\rho(q,g)\) for other pairs.

## Proof

**Upper bound.** Proposition 2.2 of Aubry–Herbaut–Monaldi gives, for \(g\ge1\),

\[
\rho(q,g)\le \max\!\left(2,\left\lceil4\log_q(1+\sqrt{2g})\right\rceil\right).
\]

For \((q,g)=(4,4)\), we have \(4^{3/4}=2\sqrt2<1+\sqrt8<4\). Hence \(3<4\log_4(1+\sqrt8)<4\), so the ceiling is four and \(\rho(4,4)\le4\).

**Lower bound.** Let \(C\) be the smooth projective model of the displayed Artin–Schreier equation. The right-hand side has a unique pole, at infinity, of odd order nine. The Artin–Schreier genus formula therefore gives \(g(C)=(9-1)/2=4\); the pole is totally ramified, so there is exactly one point of \(C\) above infinity.

For any finite extension of \(\mathbf F_2\), the equation \(y^2+y=a\) has solutions precisely when the absolute trace of \(a\) to \(\mathbf F_2\) is zero; in that case it has two solutions. Over \(\mathbf F_4\), every nonzero \(x\) satisfies \(x^9=1\), while \(0^9=0\). Since \(\operatorname{Tr}_{\mathbf F_4/\mathbf F_2}(\omega)=\operatorname{Tr}(\omega^2)=1\), both \(x^9+\omega\) at \(x=0\) and at nonzero \(x\) have trace one. Thus there are no affine \(\mathbf F_4\)-points and \(N_1=1\).

Now work over \(\mathbf F_{64}\). For every \(x\in\mathbf F_{64}\), the element \(x^9\) lies in \(\mathbf F_8\): for nonzero \(x\), its multiplicative order divides \(63/\gcd(63,9)=7\), and the case \(x=0\) is immediate. Because \([\mathbf F_{64}:\mathbf F_8]=2\), every element of \(\mathbf F_8\) has absolute trace zero from \(\mathbf F_{64}\) to \(\mathbf F_2\). On the other hand, \(\operatorname{Tr}_{\mathbf F_{64}/\mathbf F_2}(\omega)=\operatorname{Tr}_{\mathbf F_4/\mathbf F_2}(\omega)=1\), since \([\mathbf F_{64}:\mathbf F_4]=3\). Consequently \(\operatorname{Tr}_{\mathbf F_{64}/\mathbf F_2}(x^9+\omega)=1\) for every \(x\), so there are no affine \(\mathbf F_{64}\)-points either and \(N_3=1\).

The point-count identity gives \(N_3=B_1+3B_3\) and \(N_1=B_1\). Since \(N_1=N_3=1\), it follows that \(B_3=(N_3-N_1)/3=0\). This curve has no degree-three closed point, so \(\rho(4,4)>3\). Combining the lower and upper bounds proves \(\rho(4,4)=4\).

## Verification

The included dependency-free script `verify.py` implements arithmetic in \(\mathbf F_{64}=\mathbf F_2[t]/(t^6+t+1)\), verifies the embedded \(\mathbf F_4\) and absolute-trace identities, and checks \(N_1=N_3=1\) and \(B_3=0\). Its output is `N1=1; N3=1; B3=0; VERIFY_OK`. This finite computation corroborates the explicit point counts; the proof of the trace identities and the general upper bound are mathematical arguments, not inferences from a finite search.

## Relationship to prior work

Aubry, Herbaut, and Monaldi define \(\rho(q,g)\), give the general upper bound used above, and tabulate exact values for genera one, two, and three. The inspected paper does not state the genus-four value at \(q=4\) or this explicit degree-three obstruction. Lario's DS-curve resource notes that for genus four and base fields other than \(\mathbf F_2\), it lists candidate Weil polynomials rather than a complete list of explicit curve models; it is relevant adjacent evidence but does not, in the inspected overview, identify this equation. Searches of published-finding corpus and accessible prior research ledgers found no matching claim. This is a literature-search conclusion, not a uniqueness certification.

## Limitations

The result determines one value of \(\rho(q,g)\) and gives one explicit curve with no degree-three closed point. It does not classify genus-four curves over \(\mathbf F_4\), determine their zeta functions in general, or settle \(\rho(q,g)\) for any other pair. A prior explicit model with the same trace property in an unindexed source remains a residual originality risk; the exact proof and upper-bound implication are independently reproducible here.

## References

1. Y. Aubry, F. Herbaut, and J. Monaldi, “Closed points on curves over finite fields,” arXiv:2310.11218v1, first publicly posted 17 October 2023, especially the definition of \(\rho(q,g)\), Proposition 2.2, and the table of exact values for genera one through three. https://arxiv.org/abs/2310.11218
2. J.-C. Lario, “Curves over Finite Fields with Diophantine Stability,” DS-curves resource, genus-four table overview. https://web.mat.upc.edu/joan.carles.lario/DS.html
