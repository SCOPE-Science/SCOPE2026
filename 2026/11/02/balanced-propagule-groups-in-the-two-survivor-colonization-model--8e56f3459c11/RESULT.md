# Balanced propagule groups in the two-survivor colonization model

## Finding
Consider a single release of \(N\ge2\) independently surviving founders across any number of identical, isolated, vacant recipient sites. Survival probability is \(p\in(0,1)\); a site counts as founded if at least two allocated individuals survive. The goal is the *expected number of founded sites*, not the probability of at least one founding.

**Balanced-group theorem.** Every globally optimal integer allocation has no singleton group, and the sizes of all its positive groups differ by at most one. Write \(k\) for the number of used sites, \(1\le k\le\lfloor N/2\rfloor\), and \(N=ka+r\) with \(0\le r<k\). Define
\[
 f_p(n)=\Pr\{\operatorname{Bin}(n,p)\ge2\}=1-(1-p)^n-np(1-p)^{n-1},\qquad f_p(0)=f_p(1)=0.
\]
Then the exact unrestricted optimum is
\[
\boxed{V_N(p)=\max_{1\le k\le\lfloor N/2\rfloor}\big[(k-r)f_p(a)+rf_p(a+1)\big].}
\]
For *each* maximizing \(k\), precisely \(k-r\) sites receive \(a\) founders and \(r\) sites receive \(a+1\), up to site relabeling. No other partitions maximize. Thus an unrestricted exponential family of integer partitions reduces to at most \(\lfloor N/2\rfloor\) balanced candidates.

The smallest budget admitting the three qualitatively distinct choices of founding one, two, or three sites is \(N=6\). Put \(p_0=(9-\sqrt{21})/10\). The unique optimum up to relabeling is \((6)\) when \(0<p<p_0\), \((3,3)\) when \(p_0<p<3/4\), and \((2,2,2)\) when \(3/4<p<1\). Exactly two displayed choices tie at each threshold; in particular, the unequal split \((4,2)\) is never optimal.

## Assumptions and scope
All \(N\) founders are indivisible, each assigned exactly once, and each survives independently with the same probability \(p\in(0,1)\). Recipient sites are sufficiently numerous, identical and isolated; one site founded by at least two survivors contributes one unit and additional survivors contribute no further unit. We model no subsequent population dynamics, habitat heterogeneity, spatial dispersal, interaction between release sites, or fixed per-site deployment costs. This is a one-shot conservation or biological-control allocation model with a stylized two-survivor establishment rule.

## Proof
Set \(q=1-p\). The binomial survival law gives the displayed \(f_p\) and strictly positive discrete marginal
\[
 m(j):=f_p(j+1)-f_p(j)=jp^2q^{j-1}>0\quad(j\ge1),\qquad m(0)=0.
\]
In an allocation with a singleton and any other nonempty group, transfer that singleton to the other group: the singleton previously contributed zero, and the recipient gain \(m(j)>0\). Since \(N\ge2\), a maximizing allocation has no singleton; a sole singleton is impossible.

Fix the total \(s\ge4\) in any pair of nonempty groups and define \(H_s(t)=f_p(t)+f_p(s-t)\) on integers \(0\le t\le\lfloor s/2\rfloor\). Its first difference at zero is negative:
\[
H_s(1)-H_s(0)=-m(s-1)<0.
\]
For \(1\le t<\lfloor s/2\rfloor\), write \(u=s-t-1>t\). Then
\[
 H_s(t+1)-H_s(t)=m(t)-m(u),
\]
which is positive, zero or negative as \(q\) is less than, equal to or greater than
\[
Q_s(t)=\left(\frac{t}{u}\right)^{1/(u-t)}.
\]
**Critical pair lemma.** \(Q_s(t)\) is strictly increasing in \(t\). To prove this for real \(0<t<(s-1)/2\), write \(c=(s-1)/2\), \(h=c-t\). Then
\[
\log Q_s(t)=-\frac{1}{h}\operatorname{artanh}(h/c).
\]
For \(0<z<1\), the function \(\operatorname{artanh}(z)/z\) is strictly increasing: differentiating gives \([z/(1-z^2)-\operatorname{artanh}(z)]/z^2\), with numerator zero at zero and positive derivative \(2z^2/(1-z^2)^2\). As \(t\) increases, \(h\) decreases, so \(\log Q_s(t)\) increases strictly.

Consequently the signs of \(H_s(t+1)-H_s(t)\), for \(t\ge1\), can only pass from negative through at most one zero to positive. Together with the strictly negative first difference, \(H_s\) is initially decreasing and then increasing. Hence every interior \(t\in\{1,\ldots,\lfloor s/2\rfloor-1\}\) satisfies the **strict** inequality
\[
H_s(t)<\max\{H_s(0),H_s(\lfloor s/2\rfloor)\}.
\]
If two positive groups of a purported global optimum differed in size by at least two, their smaller size would be interior in this display. Replacing those two groups by either one merged group or by the balanced pair would strictly increase the expected number of founded sites while preserving \(N\), a contradiction. Thus all positive group sizes differ by at most one. For each possible count \(k\), the unique multiset of balanced sizes is specified by Euclidean division \(N=ka+r\). Computing its objective gives the formula, and its strict pair lemma exhausts every optimum.

For \(N=6\), only the three balanced multisets \((6)\), \((3,3)\), \((2,2,2)\) need comparison. Direct expansion gives
\[
f_p(6)-2f_p(3)=p^2(p^2-3p+3)(5p^2-9p+3),
\]
\[
2f_p(3)-3f_p(2)=p^2(3-4p).
\]
The quadratic \(p^2-3p+3\) is positive; \(5p^2-9p+3\) has the unique zero \(p_0=(9-\sqrt{21})/10\) in \((0,1)\). Its sign switches from positive to negative there. The second difference switches sign at \(p=3/4\), proving all strict regimes and ties. \(N<6\) cannot found three distinct sites with at least two survivors each, so six is the first budget exhibiting the three-way choice.

## Verification
Run `python3 checker.py` using only the Python standard library. It reproduces both polynomial factorizations by integer coefficient arithmetic, compares the unrestricted partition maximum with the balanced-candidate formula by exact rational arithmetic for \(2\le N\le18\) and forty survival fractions, and tests the strict pair lemma at further exact rational parameters. In this package it returned `PASS: 7049 exact-rational assertions; max checked N=18`. The analytic pair lemma, not the finite checks, proves the all-\(N\), all-\(p\) result.

## Relationship to prior work
Shea and Possingham (2000 issue; first-published online stamp 2001-12-25) directly optimize biological-control release number and sizes, with a multi-year stochastic dynamic program and a prescribed sigmoid establishment curve. They compare a restricted family of large, small and mixed releases, and do not state the present all-partitions theorem for the specific independent two-survivor rule. Fernandez, Hance and Deneubourg (2012) model collective movement with Allee effects; Duncan et al. (2014) model establishment probability against founder number; Goodsman and Lewis (2016) study spatial minimum founding populations. Koontz et al. (2018) study introductions at one recipient site at multiple times. None of the inspected material supplies this exact one-shot multisite integer-allocation formula, though broader optimization results for S-shaped returns could subsume it. Historical priority is therefore provisional.

## Limitations
This statement is exact only for the independent identical-survival, at-least-two-survivors founding rule and an unrestricted count of identical sites. It does not assert that two founders suffice for long-term ecological establishment, nor prescribe ecological releases when survival is correlated, thresholds exceed two, sites differ, site numbers are capped, or later reproduction and extinction matter. The literature comparison does not establish absolute novelty or independent certification.

## References
1. Shea, K. and Possingham, H. P., *Optimal release strategies for biological control agents: an application of stochastic dynamic programming to population management*, Journal of Applied Ecology 37 (2000 issue), 77–86. DOI: https://doi.org/10.1046/j.1365-2664.2000.00467.x (publisher first-online date 2001-12-25).
2. Fernandez, A. A., Hance, T. and Deneubourg, J. L., *Interplay between Allee effects and collective movement in metapopulations*, Oikos 121 (2012), 813–822. DOI: https://doi.org/10.1111/j.1600-0706.2011.20181.x (first online 2012-01-23).
3. Duncan, R. P., Blackburn, T. M., Rossinelli, S. and Bacher, S., *Quantifying invasion risk: the relationship between establishment probability and founding population size*, Methods in Ecology and Evolution 5 (2014), 1255–1263. DOI: https://doi.org/10.1111/2041-210X.12288.
4. Goodsman, D. W. and Lewis, M. A., *The minimum founding population in dispersing organisms subject to strong Allee effects*, Methods in Ecology and Evolution 7 (2016), 1100–1109. DOI: https://doi.org/10.1111/2041-210X.12573.
5. Koontz, M. J. et al., *Parsing propagule pressure: Number, not size, of introductions drives colonization success in a novel environment*, Ecology and Evolution 8 (2018), 8043–8054. DOI: https://doi.org/10.1002/ece3.4226.
