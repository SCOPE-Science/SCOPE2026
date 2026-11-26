# Exact re-entrant fixed-point windows for the q=10 competing-interaction Potts example

## Finding

For the scalar fixed-point equation at \(q=10\) and \(a=6/5\), consider \(b>0\) and count only solutions \(u>0\) of
\[
 \left(\frac{1+(b+8)u}{b+9u}\right)^2=\frac65 u.
\]
Let \(b_1<b_2<b_3\) be the positive roots of
\[
D(b)=15b^4-458b^3+2190b^2+9840b-58405.
\]
They lie in \((5.92465054,5.92465055)\), \((5.93839039,5.93839040)\), and \((23.39979284,23.39979285)\), respectively, with the displayed decimals interpreted as exact rationals. There are exactly three distinct positive solutions for \(b\in(b_1,b_2)\cup(b_3,\infty)\), exactly two at each of the three endpoints, and exactly one at every other \(b>0\). Thus the set with multiple positive fixed points is
\[
[b_1,b_2]\cup[b_3,\infty).
\]
In particular \(b=18\) is in the gap, even though at \(b=18\) the graph of \(u\mapsto u^{-1}((1+(b+8)u)/(b+9u))^2\) has two distinct positive stationary points. Existence of two stationary points does not give multiplicity at the prescribed level \(a=6/5\). The diagram is not a single threshold, but **does** have multiplicity for all sufficiently large \(b\).

## Assumptions and scope

This is the positive-solution count of one scalar translation-invariant fixed-point equation in the competing-interaction Potts setting, not a classification of all Gibbs measures. It asserts nothing about periodic or non-translation-invariant solutions, extremality, stability, or thermodynamic phase selection.

## Proof

The denominator is strictly positive on the specified domain, so the equation is equivalent to \(F_b(u)=0\), where
\[
 F_b(u)=5(1+(b+8)u)^2-6u(b+9u)^2
       =-486u^3+(5b^2-28b+320)u^2+(-6b^2+10b+80)u+5.
\]
The cubic discriminant formula gives the identity
\[
 \operatorname{Disc}_u F_b=60(b-1)^2(b+9)^2D(b).
\]
Exact rational substitution gives the following signs, which also provide an elementary isolation certificate:

| Argument or endpoint pair | Signs of \(D\) |
|---|---|
| \(-10,0\) | \(+,-\) |
| \(5.92465054,5.92465055\) | \(-,+\) |
| \(5.93839039,5.93839040\) | \(+,-\) |
| \(23.39979284,23.39979285\) | \(-,+\) |

The four disjoint intervals each contain a real root; degree four forces exactly one simple root in every interval and no others. In particular the positive set of \(D\) on \(b>0\) is \((b_1,b_2)\cup(b_3,\infty)\).

For negative discriminant a real cubic has just one real root, which here is positive because \(F_b(0)=5\) and the leading coefficient is negative. At \(b=1\) its factorization is \(-(6u-5)(9u+1)^2\), with one positive root. For every \(b\ge b_1>59/10\), the quadratic coefficient \(5b^2-28b+320\) is positive (its discriminant in \(b\) is negative), and the linear coefficient \(-6b^2+10b+80\) is negative (already negative at \(59/10\) and decreasing thereafter). Hence \(F_b(-v)>0\) for every \(v>0\) in the whole range \(b\ge b_1\). At positive discriminant all three real roots are therefore positive.

At each \(b_i\) the discriminant vanishes simply as a function of \(b\). To exclude a triple root, divide by the constant leading coefficient and shift \(u\) to remove the quadratic term, obtaining a depressed monic cubic with coefficients \(p(b),r(b)\). A triple root requires \(p=r=0\), which would force both the discriminant \(-4p^3-27r^2\) and its parameter derivative to vanish. Thus at each \(b_i\) the cubic has a double root and a simple root. They are real (a nonreal repeated root would need its conjugate with the same multiplicity), and both are positive by the coefficient argument. This proves all counts.

For the stationary-point comparison, set \(T_b(u)=u^{-1}((1+(b+8)u)/(b+9u))^2\). Differentiating, or taking its logarithmic derivative for \(u>0\), shows that the positive stationary points satisfy
\[
 9(b+8)u^2+(27-b(b+8))u+b=0.
\]
Its discriminant is \((b(b+8)-9)(b(b+8)-81)\). Both roots are distinct and positive exactly for \(b(b+8)>81\), since the product is positive and their sum has the sign of \(b(b+8)-27\). This corresponds to \(b>\sqrt{97}-4\). That threshold gives the existence of turning points, not the position of the horizontal line at \(6/5\) relative to the turning values. For example, at \(b=18\) the turning-point inequality holds, but \(D(18)=-268141\), so the fixed point is unique.

## Relationship to prior work

Akın and Ulusoy study the competing-interaction Potts model and its scalar translation-invariant fixed-point analysis. The exact classification above concerns the displayed scalar equation and isolates its genuine fixed-level discriminant. A stationary-point-only criterion would wrongly include strictly more parameters at this level. This comparison is with the mathematical criterion itself, not a claim that eventual large-\(b\) multiplicity is false.

## Verification

The cubic discriminant, the rational sign table and the exceptional factorization are directly checkable in exact polynomial arithmetic. The accompanying `verify.py` checks the equivalent discriminant for \(P_b=F_b/5\), confirms the root counts and isolations by exact Sturm counts, and independently excludes a triple root by a nonzero resultant. Those exact certificates do not depend on the displayed decimal approximations to the roots. The stationary-point comparison follows by the differentiation above.

## References

1. H. Akın and S. Ulusoy, *Limiting Gibbs Measures of The q-State Potts Model with Competing Interactions*, DOI 10.2139/ssrn.4009674.
2. H. Akın and S. Ulusoy, *Limiting Gibbs measures of the q-state Potts model with competing interactions*, Physica B 640 (2022), 413944, DOI 10.1016/j.physb.2022.413944.
