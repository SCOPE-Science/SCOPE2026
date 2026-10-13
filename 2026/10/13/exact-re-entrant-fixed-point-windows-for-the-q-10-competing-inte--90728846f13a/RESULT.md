# Exact re-entrant fixed-point windows for the q=10 competing-interaction Potts example
## Finding
For the scalar translation-invariant Gibbs-measure fixed-point family studied by Akın and Ulusoy, set \(q=10\), \(a=6/5\), and \(b>0\). Their equation (3.10)
\[
\left(\frac{1+(b+8)u}{b+9u}ight)^2=\frac65u
\]
has a re-entrant, rather than monotone, multiplicity diagram. Define
\[
P_b(u)=(1+(b+8)u)^2-\frac65u(b+9u)^2
\]
and
\[
D(b)=15b^4-458b^3+2190b^2+9840b-58405.
\]
Let \(b_1<b_2<b_3\) be the three positive roots of \(D\). They are isolated by
\[
5.92465054<b_1<5.92465055,
\]
\[
5.93839039<b_2<5.93839040,
\]
and
\[
23.39979284<b_3<23.39979285.
\]
The fixed-point equation has three distinct positive solutions exactly for \(b_1<b<b_2\) and \(b>b_3\), exactly two distinct positive solutions at \(b=b_1,b_2,b_3\), and exactly one positive solution for every other \(b>0\). Hence multiple fixed points in this scalar TISGM family occur exactly on
\[
[b_1,b_2]\cup[b_3,\infty).
\]
In particular, \(b=18\) lies in the uniqueness gap \((b_2,b_3)\), matching the paper's own numerical example and contradicting its Theorem 4.2 claim that all sufficiently large \(b\) are in the phase-transition region.

## Assumptions and scope
The statement concerns only positive solutions of Akın–Ulusoy equation (3.10), which the source uses to describe its scalar translation-invariant Gibbs measures. It does not classify non-translation-invariant Gibbs measures, periodic Gibbs measures, extremality, or thermodynamic stability. The parameter specialization is exactly the source's displayed choice \(a=1.2=6/5\) and its explicit \(q=10\) example.

The earliest exactly dated public full-text event verified for the source is the author upload dated 2022-05-16. The SSRN record is labeled January 2022 and the manuscript itself is dated 2022-01-01, but an exact SSRN posting day was not independently recovered; no earlier exact public-access day is asserted here.

## Proof
For \(q=10\) and \(a=6/5\), clearing the strictly positive denominator \((b+9u)^2\) is reversible for \(b,u>0\). Thus positive fixed points are exactly the positive zeros of
\[
P_b(u)=-\frac{486}5u^3+\left(b^2-\frac{28}5b+64ight)u^2+\left(-\frac65b^2+2b+16ight)u+1.
\]
Its discriminant with respect to \(u\) factors exactly as
\[
\operatorname{Disc}_u(P_b)=\frac{12}{125}(b-1)^2(b+9)^2D(b).
\]
A Sturm count gives exactly three positive simple roots of \(D\) and one negative root. Exact rational endpoint counts isolate the positive roots in the three intervals displayed above. Because \(D(0)<0\) and the leading coefficient of \(D\) is positive, its sign on \(b>0\) is negative on \((0,b_1)\), positive on \((b_1,b_2)\), negative on \((b_2,b_3)\), and positive on \((b_3,\infty)\).

When the cubic discriminant is negative, \(P_b\) has exactly one real zero. Since \(P_b(0)=1\) and its leading coefficient is negative, that zero is positive. The exceptional point \(b=1\) factors as
\[
P_1(u)=-\frac15(6u-5)(9u+1)^2,
\]
so it also has exactly one positive zero.

It remains to show that the three real zeros produced when the discriminant is positive are all positive. On every multiplicity interval one has \(b>b_1>5.924\). There the coefficient of \(u\),
\[
-\frac25(3b^2-5b-40),
\]
is negative, while the coefficient of \(u^2\),
\[
\frac15(5b^2-28b+320),
\]
is positive for every real \(b\). Consequently every coefficient of \(P_b(-u)\) is positive for \(u>0\), so \(P_b\) has no negative zero. Therefore positive discriminant means three distinct positive zeros.

At each \(b_i\), the discriminant vanishes. A triple zero would force the cubic identity \(B^2-3AC=0\), where \(A,B,C\) are the cubic, quadratic, and linear coefficients. The exact resultant of \(D\) with this triple-root condition is nonzero, so none of the \(b_i\) is a triple-root parameter. Thus each endpoint has one positive double zero and one positive simple zero, hence exactly two distinct positive solutions.

## Verification
The accompanying `verify.py` reconstructs the polynomial from the source equation using exact rational arithmetic, checks the discriminant factorization, performs exact Sturm root counts for \(D\), certifies one root in each rational isolating interval, checks the nonzero resultant excluding triple roots, and verifies the \(b=1\) factorization. Its numerical output is used only to display decimal isolations; the root-count theorem is exact.

## Relationship to prior work
Akın and Ulusoy derive equation (3.10) and state in Theorem 4.1 that multiplicity is controlled by the values of \(a\) at the two tangencies. Their Theorem 4.2 then fixes \(a=1.2\) but uses only the discriminant of the tangency equation, concluding a monotone transition threshold in \(b\). For \(q=10\), that argument does not test whether the fixed value \(a=1.2\) lies between the two tangency levels. The same paper later gives \(a=1.2\), \(q=10\), \(b=18\) as a unique-root example, already conflicting with the monotone conclusion. The result above replaces that conflict by the exact complete \(b\)-classification for the displayed \(q=10\) case.

Searches for the exact quartic, its three positive root values, correction/erratum language, the \(q=10,b=18\) example, and equivalent fixed-point formulations did not recover a published statement of these exact windows. The publisher landing page for the final Physica B version was inspectable only at metadata/abstract level, so a version-specific correction hidden in the inaccessible final body remains a residual risk.

## Limitations
The result is a classification of positive solutions to one scalar fixed-point family, not a classification of every Gibbs measure of the Hamiltonian. Multiplicity of these fixed points is reported in the same sense used by the source for its translation-invariant phase discussion. No statement is made about which fixed points are extremal, dynamically stable, or thermodynamically selected.

## References
1. H. Akın and S. Ulusoy, *Limiting Gibbs Measures of The q-State Potts Model with Competing Interactions*, SSRN Electronic Journal, DOI 10.2139/ssrn.4009674. See equation (3.10), Theorems 4.1–4.2, and the \(q=10\), \(a=1.2\), \(b=18\) example.
2. H. Akın and S. Ulusoy, *Limiting Gibbs measures of the q-state Potts model with competing interactions*, Physica B 640 (2022), 413944, DOI 10.1016/j.physb.2022.413944.
