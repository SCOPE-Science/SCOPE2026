# A sharp curvature transition for carbonate-only pH under equal-alkalinity mixing

## Finding

In an ideal carbonate-only equilibrium with positive fixed carbonate alkalinity \(A\), first and second carbonate dissociation constants \(K_1,K_2>0\), and dissolved inorganic carbon \(C>A/2\), let \(r=K_2/K_1\). The curvature of the equilibrium \(\mathrm{pH}(C)\) has a sharp universal transition at \(r_c=1/112\).

When \(r\ge r_c\), \(\mathrm{pH}(C)\) is strictly convex throughout its admissible concentration domain; its second derivative is positive except for one isolated zero when \(r=r_c\). When \(0<r<r_c\), the curvature is positive, then negative, then positive as \(C\) increases, with exactly two distinct inflection points. Therefore, pooling equal-alkalinity waters before calculating pH always produces pH strictly below their volume-weighted mean pH when \(r\ge r_c\), but below-threshold systems admit both signs of this aggregation bias, including strictly positive pooled-minus-mean pH in the negative-curvature interval.

At the threshold the unique zero curvature occurs at \([H^+]/K_1=1/28\), or \(C/A=6/7\). As \(r\uparrow r_c\), the two inflection concentrations satisfy
\[
\frac{C_\pm}{A}=\frac67\pm\frac43\sqrt{r_c-r}+O(r_c-r),
\]
so the intervening concave concentration window has width \(\frac{8A}{3}\sqrt{r_c-r}+O(A(r_c-r))\).

## Assumptions and scope

The aqueous system contains only three ideal equilibrium species \(\mathrm{CO_2^*}\), \(\mathrm{HCO_3^-}\), and \(\mathrm{CO_3^{2-}}\). Concentrations obey \(K_1=[H^+][\mathrm{HCO_3^-}]/[\mathrm{CO_2^*}]\) and \(K_2=[H^+][\mathrm{CO_3^{2-}}]/[\mathrm{HCO_3^-}]\). Carbonate alkalinity is \(A=[\mathrm{HCO_3^-}]+2[\mathrm{CO_3^{2-}}]>0\), and total dissolved inorganic carbon is \(C=[\mathrm{CO_2^*}]+[\mathrm{HCO_3^-}]+[\mathrm{CO_3^{2-}}]\). The constants and temperature are identical across the waters being pooled, as is \(A\) per unit volume; no precipitation, gas exchange, additional protonation reactions, or changes in conserved totals occur during mixing. Water self-ionization, borate, and other alkalinity terms are intentionally excluded; \(A\) here is not full seawater total alkalinity.

For positive species concentrations \(C/A>1/2\), an open interval. Write \(x=[H^+]/K_1\), \(r=K_2/K_1\), and \(y=C/A\). The stated pH refers to \(-\log_{10}[H^+]\) using a consistent concentration reference, so additive unit constants are irrelevant to curvature or mixing differences.

## Proof

The two equilibrium laws give species ratios proportional to \(x^2:x:r\). Hence
\[
y(x)=\frac{x^2+x+r}{x+2r},\qquad
\frac{dy}{dx}=\frac{x^2+4rx+r}{(x+2r)^2}>0.
\]
As \(x\downarrow0\), \(y\downarrow1/2\), while \(y\to\infty\) as \(x\to\infty\). Consequently there is a unique positive \(x\) at every allowed \(C\), explicitly
\[
x(y)=\frac{y-1+\sqrt{(1-y)^2+4r(2y-1)}}2>0.
\]

Differentiating \(\mathrm{pH}=-\log_{10}(K_1x)\) twice with respect to \(C=Ay(x)\), at fixed \(A,K_1,K_2\), gives the exact identity
\[
\frac{d^2\mathrm{pH}}{dC^2}=
\frac{(x+2r)^3}{A^2\ln(10)\,x^2(x^2+4rx+r)^3}
P_r(x),\quad
P_r(x)=x^3+6rx^2+(16r^2-r)x+2r^2.
\]
Every factor outside \(P_r(x)\) is strictly positive. The cubic discriminant factors exactly as
\[
\operatorname{Disc}_x(P_r)=-4r^3(4r-1)^2(112r-1).
\]
For \(r\ge1/16\), every coefficient of \(P_r\) is nonnegative, with positive constant and leading terms, so \(P_r(x)>0\) for \(x>0\). For \(1/112<r<1/16\), the discriminant is negative, so the cubic has one real root; the positive value \(P_r(0)=2r^2\) and its positive leading coefficient imply that root is negative and \(P_r(x)>0\) on the positive axis. At \(r=r_c=1/112\), direct factorization yields
\[
P_{r_c}(x)=\frac{(8x+1)(28x-1)^2}{6272}.
\]
It is positive except at the isolated double zero \(x=1/28\), where substitution in \(y(x)\) gives \(y=6/7\). Since a differentiable function with nonnegative continuous second derivative and no nonempty interval of vanishing curvature is strictly convex, the first assertion includes the borderline parameter.

For \(0<r<1/112\), the discriminant is positive, so \(P_r\) has three distinct real roots. The polynomial \(P_r(-z)=-z^3+6rz^2+(r-16r^2)z+2r^2\) has exactly one sign change for positive \(z\), so Descartes' rule and the cubic root count imply exactly one negative and two positive roots. The sign pattern on \(x>0\) is thus \(+,-,+\), giving the precisely two inflections and the described concavity band.

For onset, Taylor-expand \(P_r(x)\) at \((x,r)=(1/28,1/112)\). There \(P=P_x=0\), \(P_{xx}=9/28\) and \(P_r=1/56\); therefore for \(r=r_c-\epsilon\), the two positive roots obey \(x_\pm=1/28\pm\sqrt\epsilon/3+O(\epsilon)\). As \(y_x=4\) there, their mapped concentration ratios are \(y_\pm=6/7\pm4\sqrt\epsilon/3+O(\epsilon)\).

For pooling, conservation and common \(A,K_1,K_2\) give \(\bar C=\sum_iw_iC_i\) and \(\mathrm{pH}_{\mathrm{pool}}=\mathrm{pH}(\bar C)\). Jensen's inequality establishes the strict global convex-case comparison for nonidentical concentrations. Within either local convex band the same inequality holds for concentrations staying inside that band; within the open concave band it reverses strictly. Because both types of open intervals exist when \(r<r_c\), two-component mixtures with arbitrarily small positive concentration contrast realize both bias signs. This says nothing universal about mixtures spanning several curvature bands.

## Verification

Run \(\texttt{python3 check_carbonate.py}\) with Python 3 standard library. The accompanying checker recomputes the cubic discriminant directly from its coefficients at ten exact rational parameters, checks the critical factorization and curvature signs at three exact rational configurations, compares finite-difference curvatures against the derived analytic second derivative at 3,000 independent random configurations, and tests the critical square-root onset numerically. The exact symbolic identities above, not the finite tests, establish the universal theorem.

For \(r=1/10000\), at \(x=1/10000,1/1000,1/50\), respectively, \(C/A=6667/10000,367/400,205/202\), and \(P_r(x)\) has signs \(+,-,+\). Equal-volume pools of concentrations \(C/A=y\pm0.0005\) exhibit pooled-minus-mean pH of approximately \(-1.46692\times10^{-6}\), \(+7.03979\times10^{-6}\), and \(-5.34375\times10^{-5}\), respectively. This checks both sign directions without relying on field data.

## Relationship to prior work

Deffeyes (1965) derives the carbonate equilibrium and conserved-carbon/alkalinity geometry foundational to this calculation. Schulz and collaborators (2009) treat DIC changes at fixed alkalinity; their openly circulated manuscript dates to 23 April 2009. Egleston, Sabine, and Morel (2010) derive ocean carbonate buffering derivatives, including a carbonate-dominant approximation. These facts and first derivatives are prior work, not new claims. The present narrowly defined contribution is the complete sharp parameter classification of the second derivative, its double-inflection onset, and the sign of equal-alkalinity pH pooling error.

Wigley and Plummer (1976) specifically study carbonate-water mixing and are especially relevant historically. Available abstract-level material does not resolve whether their full argument, or subsequent work on diprotic-buffer curvature, contains an equivalent theorem. The complete article was not inspected, so historical priority remains provisional; this is not an assertion that all potentially stronger literature has been excluded.

## Limitations

Only ideal carbonate alkalinity is conserved here; true seawater generally includes borate, hydroxide, proton, and other terms, and mixing waters with different alkalinities or equilibrium constants has no such one-variable Jensen law. The classification is exact for this restricted model but is not an empirical statement about open-ocean pH, mixing kinetics, biogeochemical feedbacks, or carbonate precipitation. Finite computational checks do not substitute for the exact proof. Broader historical derivations could subsume the curvature classification; no external independent audit has been performed.

## References

1. K. S. Deffeyes, *Carbonate Equilibria: A Graphic and Algebraic Approach*, Limnology and Oceanography 10 (1965), 412–426. DOI: 10.4319/lo.1965.10.3.0412.
2. K. G. Schulz, J. Barcelos e Ramos, R. E. Zeebe, and U. Riebesell, *CO2 perturbation experiments: similarities and differences between dissolved inorganic carbon and total alkalinity manipulations*, Biogeosciences 6 (2009), 2145–2153. DOI: 10.5194/bg-6-2145-2009. Public discussion version: 23 April 2009.
3. E. S. Egleston, C. L. Sabine, and F. M. M. Morel, *Revelle revisited: Buffer factors that quantify the response of ocean chemistry to changes in DIC and alkalinity*, Global Biogeochemical Cycles 24 (2010). DOI: 10.1029/2008GB003407.
4. T. M. L. Wigley and L. N. Plummer, *Mixing of carbonate waters*, Geochimica et Cosmochimica Acta 40 (1976), 989–995. DOI: 10.1016/0016-7037(76)90041-7 (full text not inspected).
