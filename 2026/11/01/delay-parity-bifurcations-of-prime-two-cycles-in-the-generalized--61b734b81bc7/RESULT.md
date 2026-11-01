# Delay-parity bifurcations of prime-two cycles in the generalized Lozi recurrence

## Finding
For every pair of integers \(1\le k<d\), every \(0<\nu<2\), and every \(a>0\), consider the Bilal–Ramaswamy delayed Lozi recurrence
\[
x_n=1-a|x_{n-k}|-(1-\nu)x_{n-d}.
\]
The following is a **complete classification of least-period-two solutions**, rather than a stability claim. A two-cycle means a bi-infinite alternating real sequence \(\ldots,u,v,u,v,\ldots\) with \(u\ne v\), or equivalently the associated orbit of the \(d\)-coordinate delay map. Cycles differing only by interchange of \(u\) and \(v\) are counted once.

Put
\[
s=2-\nu>0,\qquad
h=\begin{cases}s,&d\text{ even},\\ \nu,&d\text{ odd}.\end{cases}
\]
The answer depends **only on the parities** of the two delays, not on their magnitudes.

**Odd nonlinear delay \(k\).** If \(a>h\), exactly one prime-two cycle exists, with phase values
\[
(u,v)=\left(\frac{a+h}{a^2+sh},\frac{h-a}{a^2+sh}\right),\qquad u>0>v.
\]
At \(a=h\), infinitely many such cycles exist: precisely the pairs \(u,v\ge0\), \(u\ne v\), satisfying
\[
u+v=\frac{2}{s+h}.
\]
For \(a<h\), there is no prime-two cycle.

**Even nonlinear delay \(k\).** If
\[
a>\max\{h,\sqrt{sh}\},
\]
there is exactly one prime-two cycle, given by
\[
(u,v)=\left(\frac{a-h}{a^2-sh},-\frac{a+h}{a^2-sh}\right),\qquad u>0>v.
\]
There is a continuum of prime-two cycles **only** when \(d\) is odd, \(\nu>1\), and \(a=\nu\): all the pairs \(u,v\le0\), \(u\ne v\), with
\[
u+v=\frac{1}{1-\nu}.
\]
At every other parameter not covered by the unique-cycle case there is no prime-two cycle.

Every isolated cycle has negative and positive phase values. Its average \((u+v)/2\) is **positive for odd \(k\)** and **negative for even \(k\)**. In particular, for \(k\) even and \(d\) odd, the creation of the isolated cycle has three qualitatively distinct regimes:

* If \(0<\nu<1\), set \(a_0=\sqrt{\nu(2-\nu)}\). Cycles exist precisely for \(a>a_0\); both phase values diverge at the boundary, with
\[
u\sim\frac{a_0-\nu}{2a_0(a-a_0)},\qquad
v\sim-\frac{a_0+\nu}{2a_0(a-a_0)}
\quad(a\downarrow a_0).
\]
* If \(\nu=1\), cycles exist for \(a>1\), with the **exact** simplification
\[
u=\frac{1}{a+1},\qquad v=-\frac{1}{a-1}.
\]
One phase stays bounded while the other diverges.
* If \(1<\nu<2\), a continuum of negative-phase cycles occurs at \(a=\nu\); a unique mixed-sign cycle appears for \(a>\nu\) and tends to the finite endpoint \((0,-1/(\nu-1))\) as \(a\downarrow\nu\).

For example, \(k=2\), \(d=3\), \(\nu=1/2\), \(a=1\) has the exact prime-two cycle \(\{2,-6\}\), despite having only one fixed point. The negative fixed point does not exist until \(a>3/2\).

## Assumptions and scope
All states and time indices are real and integer, respectively. The delay map acts on \(\mathbb R^d\); no restriction to a compact trapping set or to attracting cycles is imposed. The parameter interval \(0<\nu<2\) is the dissipative interior used in the defining family, and \(a>0\) fixes the modulus-feedback orientation. Critical lines and zero-valued phases are included. The endpoints \(\nu=0,2\), negative \(a\), and minimal periods other than two are not classified here.

For orientation, fixed points are constant sequences with the always-existing positive value \(1/(s+a)\), together with a negative fixed point \(1/(s-a)\) exactly when \(a>s\). This elementary fixed-point criterion is not part of the novelty claim.

## Proof
Write \(x_{2m}=u\) and \(x_{2m+1}=v\). Conversely, any pair satisfying both phase equations gives a full bi-infinite solution and a genuine two-cycle whenever \(u\ne v\). Delays preserve or interchange parity according to their parity. Adding the two phase equations eliminates delay parity and yields the **universal sum identity**
\[
s(u+v)+a(|u|+|v|)=2. \tag{1}
\]
Subtracting gives the **parity-sensitive difference identity**
\[
h(u-v)+a(-1)^k(|u|-|v|)=0, \tag{2}
\]
where \(h=1+(1-\nu)(-1)^d>0\), precisely the stated definition. Conversely, adding and subtracting the two original phase equations is an invertible operation, so (1) and (2) are jointly sufficient.

If \(u,v>0\), then \(|u|-|v|=u-v\). For \(u\ne v\), (2) requires odd \(k\) and \(a=h\). Equation (1) then gives \(u+v=2/(s+h)\), and the nonnegative endpoints with one phase zero also solve both equations. If \(u,v<0\), then \(|u|-|v|=-(u-v)\), so (2) requires even \(k\) and \(a=h\). Equation (1) gives \(u+v=2/(s-h)\); its required negativity holds exactly if \(h>s\). Because \(h=s\) for even \(d\), this is possible exactly for odd \(d\) and \(\nu>1\). Again the zero endpoints are valid. There are no other same-sign nonconstant solutions.

For opposite signs choose the phase ordering \(u>0>v\) (the other ordering is its time shift). Set \(S=u+v\) and \(\Delta=u-v>0\). Then \(|u|+|v|=\Delta\) and \(|u|-|v|=S\). Equations (1)–(2) become
\[
sS+a\Delta=2,\qquad h\Delta+a(-1)^k S=0. \tag{3}
\]
If \(k\) is odd, the unique algebraic solution is
\[
\Delta=\frac{2a}{a^2+sh},\qquad S=\frac{2h}{a^2+sh};
\]
this has \(u=(S+\Delta)/2>0\) and \(v=(S-\Delta)/2<0\) **if and only if** \(a>h\). If \(k\) is even, (3) instead gives
\[
\Delta=\frac{2a}{a^2-sh},\qquad S=-\frac{2h}{a^2-sh}.
\]
Because \(\Delta>0\), one must have \(a^2>sh\), and because \(u=(S+\Delta)/2>0\), one must also have \(a>h\). These conditions are both necessary and sufficient and yield the advertised formulas. At the singular value \(a^2=sh\), (3) would give \(0=2\), so no opposite-sign solution was discarded by division. Likewise, a zero-valued phase at \(a=h\) is already included in the appropriate same-sign continuum and does not supply a separate orbit. This exhausts all sign cases and proves the complete classification and uniqueness assertions.

The mean-sign statement follows directly from \(S=\pm 2h/(a^2\pm sh)\). The three asymptotic regimes in the even-\(k\), odd-\(d\) case use \(h=\nu\), \(sh=\nu(2-\nu)\). When \(0<\nu<1\), \(a_0>\nu\) and \(a^2-a_0^2=(a-a_0)(a+a_0)\), giving the two displayed simple poles. At \(\nu=1\) the factorizations \((a-1)/(a^2-1)=1/(a+1)\) and \(-(a+1)/(a^2-1)=-1/(a-1)\) are exact. When \(1<\nu<2\), the denominator at \(a=\nu\) is \(2\nu(\nu-1)>0\), and the stated finite limit follows.

## Verification
`verify.py` uses only exact rational arithmetic and the Python standard library. It independently constructs all four sign-chamber linear systems, solves nonsingular cases, and compares their complete prime-two lists with the theorem for **18,150** noncritical combinations of delays and parameters. It separately checks examples from each of the three continuum resonance types, the exact cycle \(\{2,-6\}\), fixed-point identities, and full recurrence identities for negative and positive time indices. Run `python3 verify.py` from the directory containing this document. The analytical proof above, not this finite test set, establishes the universal quantifiers.

## Relationship to prior work
Bilal and Ramaswamy (2020, arXiv:2005.01849, their Section II and equation (3)) introduced the delayed higher-dimensional Lozi recurrence, its greatest-common-divisor delay reduction, and fixed-point stability boundaries. Those results are taken as the starting point; the present classification is **not** claimed to introduce the map or its fixed-point equations. Their inspected full text does not provide a uniform prime-two census by both delay parities or the three-way infinity/finite bifurcation of the even-nonlinear, odd-linear delay case.

Botella-Soler, Castelo, Oteo and Ros (2011, arXiv:1102.0034, Section 3.1) explicitly calculate isolated two-cycles and bisecting continua for the **classical planar Lozi map**. In particular, the \(k=1,d=2\) specialization of the present result is covered by that earlier paper and is **not an independent novelty**. The new scope lies in simultaneous unrestricted delay classification, the even-\(k\), odd-\(d\) pole threshold, and its three-regime creation law; the preceding planar theorem does not imply those cases merely by renaming parameters.

Ou (2022, arXiv:2203.02326, Sections 1 and 3) proves symbolic and analytic existence statements for periodic points of an orientation-preserving **planar** Lozi family in a restricted parameter region. That work's itinerary continuation machinery is not a statement about the Bilal–Ramaswamy family with arbitrary two delays, and its planar uniqueness assertion cannot yield the parity/singularity classification here without additional analysis.

## Limitations
No stability, attraction, entropy, invariant-measure or hyperchaos conclusion is drawn. In particular, a cycle that exists algebraically may be repelling or irrelevant to a bounded attractor. The singular periodic continua need not be normally attracting. The result does not cover endpoint damping parameters or higher periods. The planar two-cycle formula and the general phenomenon of bisecting continua are previously known. Relevant works outside the inspected indexed and source literature could contain an equivalent delay-parity treatment; a second independent audit has not been conducted.

## References
1. S. Bilal and R. Ramaswamy, *A higher-dimensional generalization of the Lozi map: Bifurcations and dynamics*, first public arXiv version 2020-05-04, arXiv:2005.01849. https://arxiv.org/abs/2005.01849
2. V. Botella-Soler, J. M. Castelo, J. A. Oteo and J. Ros, *Bifurcations in the Lozi map*, 2011, arXiv:1102.0034. https://arxiv.org/abs/1102.0034
3. D.-S. Ou, *Critical points in higher dimensions, I: Reverse order of periodic orbit creations in the Lozi family*, first version 2022-03-04, arXiv:2203.02326. https://arxiv.org/abs/2203.02326
