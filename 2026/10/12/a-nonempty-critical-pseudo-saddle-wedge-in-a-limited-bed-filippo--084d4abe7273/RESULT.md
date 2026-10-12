# A nonempty critical pseudo-saddle wedge in a limited-bed Filippov epidemic model


## Finding

Wang, Xiao, and Zhu study the Filippov epidemic system
\[
\begin{aligned}
\dot S&=\Lambda-\mu S-\frac{\beta SI}{S+I}+H(I,\epsilon)I,\\
\dot I&=\frac{\beta SI}{S+I}-(\mu+\nu)I-H(I,\epsilon)I,
\end{aligned}
\]
with the switching manifold
\[
I=I_c,
\]
and treatment
\[
H(I,\epsilon)=
\begin{cases}
h_1,&I<I_c,\\
h_0+(h_1-h_0)\dfrac{b}{b+I},&I>I_c.
\end{cases}
\]
Set
\[
q=\mu+\nu,\qquad
\Delta=h_1-h_0>0,
\]
\[
r_0=q+h_0,\qquad r_1=q+h_1=r_0+\Delta.
\]
The source defines
\[
\mathcal R_0=\frac{\beta}{r_1}
\]
and, in its equality case \(\mathcal R_0=1\), states that a pseudo-equilibrium is feasible if
\[
I_c<I_{c0},
\qquad
I_{c0}=\frac{b(r_1-\beta)}{\beta-r_0}.
\]
At \(\mathcal R_0=1\), however,
\[
\beta=r_1,
\]
so
\[
I_{c0}=0.
\]
Thus the printed condition is empty for every positive switching level.

The actual equality-case classification is nonempty. On \(I=I_c>0\), the lower-treatment field has normal component
\[
X_1\sigma
=I_c\left(\frac{\beta S}{S+I_c}-r_1\right)
=-\frac{r_1 I_c^2}{S+I_c}<0.
\]
For the upper-treatment field, the source's tangency formula simplifies at \(\beta=r_1\) to
\[
S_{c2}
=\frac{r_0}{\Delta}I_c+\frac{br_1}{\Delta}.
\]
For \(S>S_{c2}\), the upper field has positive normal component, so the two fields point away from the switching manifold. Hence the equality-case repulsing sliding region is
\[
\Sigma_e
=\left\{(S,I_c):S\ge S_{c2}}\right\}.
\]

The source's sliding dynamics are
\[
\dot S
=-\mu\left[S-\frac{\Lambda-qI_c}{\mu}\right].
\]
Its only stationary point is therefore
\[
E_s=(S_s,I_c),
\qquad
S_s=\frac{\Lambda-qI_c}{\mu}.
\]
Consequently \(E_s\) is a pseudo-equilibrium exactly when \(S_s\ge S_{c2}\). This inequality is equivalent to
\[
\Lambda\Delta-\mu b r_1
\ge
I_c(q\Delta+\mu r_0).
\]
Define
\[
I_c^{\dagger}
=\frac{\Lambda\Delta-\mu b r_1}{q\Delta+\mu r_0}.
\]
For positive \(I_c\), the exact classification is:

\[
\Lambda\Delta\le\mu b r_1
\quad\Longrightarrow\quad
\text{no critical pseudo-equilibrium},
\]
whereas
\[
\Lambda\Delta>\mu b r_1
\quad\Longrightarrow\quad
E_s\text{ is feasible exactly for }0<I_c\le I_c^{\dagger}.
\]
For
\[
0<I_c<I_c^{\dagger},
\]
this point lies strictly inside the repulsing sliding ray. Since the derivative of the one-dimensional sliding field is
\[
F_s'(S)=-\mu<0,
\]
it is a pseudo-saddle in the terminology of the source. At
\[
I_c=I_c^{\dagger},
\]
the pseudo-equilibrium coincides with the upper tangency point.

An exact witness is
\[
\Lambda=8,\quad
\mu=\frac1{10},\quad
\nu=\frac35,
\]
\[
h_0=\frac15,\quad h_1=2,\quad
b=\frac1{10},\quad
\beta=\frac{27}{10},\quad
I_c=5.
\]
Then
\[
q=\frac7{10},\quad
\Delta=\frac95,\quad
r_0=\frac9{10},\quad
r_1=\frac{27}{10},
\]
and therefore
\[
\mathcal R_0=1,
\qquad
I_{c0}=0.
\]
But the corrected cutoff is
\[
I_c^{\dagger}=\frac{1597}{150}>5,
\]
while
\[
S_{c2}=\frac{53}{20},
\qquad
S_s=45.
\]
Thus \((45,5)\) is strictly inside the repulsing sliding ray. Moreover,
\[
S_s+I_c=50<\frac{\Lambda}{\mu}=80,
\]
so the point lies in the source's positively invariant region.

## Assumptions and scope

The parameters satisfy the source's biological assumptions
\[
\Lambda>0,\quad \mu>0,\quad \nu\ge0,\quad b>0,
\]
\[
h_1>h_0\ge0,
\qquad I_c>0.
\]
The result is restricted to the critical surface
\[
\mathcal R_0=1.
\]
It does not alter the source's classifications for \(\mathcal R_0\ne1\), nor does it claim that all global bifurcation diagrams must change.

The endpoint \(I_c=I_c^{\dagger}\) is included as a pseudo-equilibrium under the source's definition because the repulsing sliding region is written with its tangency endpoint included. The strict inequality \(I_c<I_c^{\dagger}\) is the genuine interior pseudo-saddle regime.

## Proof

At \(\mathcal R_0=1\), one has \(\beta=r_1\). The source's auxiliary quantity is therefore
\[
I_{c0}=\frac{b(r_1-r_1)}{r_1-r_0}=0,
\]
since
\[
r_1-r_0=\Delta>0.
\]
This proves that the printed equality criterion \(I_c<I_{c0}\) is impossible for positive \(I_c\).

For the actual Filippov geometry, let
\[
\sigma(S,I,I_c)=I-I_c.
\]
On the switching manifold, the normal component of the lower field is
\[
X_1\sigma
=I_c\left(\frac{\beta S}{S+I_c}-r_1\right).
\]
Substitution of \(\beta=r_1\) gives
\[
X_1\sigma=-\frac{r_1I_c^2}{S+I_c}<0.
\]

The source gives the upper tangency coordinate
\[
S_{c2}
=\frac{[(b+I_c)r_0+b\Delta]I_c}
{(b+I_c)(\beta-r_0)-b\Delta}.
\]
At \(\beta=r_1=r_0+\Delta\), its denominator is
\[
(b+I_c)\Delta-b\Delta=\Delta I_c,
\]
so
\[
S_{c2}
=\frac{(b+I_c)r_0+b\Delta}{\Delta}
=\frac{r_0}{\Delta}I_c+\frac{br_1}{\Delta}.
\]
The source itself identifies the equality-case sliding region as the same ray \(S\ge S_{c2}\). The sign computation above shows explicitly that the lower field points downward there, while the upper field changes to the opposite sign after its tangency; hence the ray is repulsing.

The sliding equation is
\[
\dot S=-\mu(S-S_s),
\qquad
S_s=\frac{\Lambda-qI_c}{\mu}.
\]
Its unique fixed point is feasible precisely when
\[
S_s\ge S_{c2}.
\]
Multiplying by the positive quantity \(\mu\Delta\) gives
\[
\Delta(\Lambda-qI_c)
\ge
\mu r_0 I_c+\mu b r_1,
\]
or equivalently
\[
\Lambda\Delta-\mu b r_1
\ge
I_c(q\Delta+\mu r_0).
\]
The coefficient of \(I_c\) on the right is positive. Therefore positive feasible switching levels exist if and only if
\[
\Lambda\Delta>\mu b r_1,
\]
and, in that case, are exactly
\[
0<I_c\le
\frac{\Lambda\Delta-\mu b r_1}{q\Delta+\mu r_0}.
\]
The sliding derivative is \(-\mu<0\), proving the pseudo-saddle classification for interior points of the repulsing ray. Equality in the feasibility inequality gives \(S_s=S_{c2}\), hence collision with the tangency point.

Finally,
\[
S_s+I_c
=\frac{\Lambda}{\mu}-\frac{\nu}{\mu}I_c
\le\frac{\Lambda}{\mu},
\]
so every positive feasible pseudo-equilibrium also satisfies the source's population bound whenever \(S_s\ge0\), which is automatic from \(S_s\ge S_{c2}>0\).

## Verification

The bundled exact-arithmetic checker verifies the symbolic substitutions
\[
I_{c0}=0,
\qquad
S_{c2}=\frac{r_0}{\Delta}I_c+\frac{br_1}{\Delta},
\]
and the equivalence between \(S_s\ge S_{c2}\) and the corrected cutoff.

For the explicit witness it verifies exactly
\[
I_c^{\dagger}=\frac{1597}{150},
\qquad
S_{c2}=\frac{53}{20},
\qquad
S_s=45,
\]
as well as the strict normal-field signs at \((45,5)\), the zero sliding velocity, and the invariant-region inequality.

The finite arithmetic replay is not used to prove the general classification. The classification follows from the exact vector-field and inequality calculations above.

## Relationship to prior work

The motivating article explicitly states that at \(\mathcal R_0=1\) the sliding region is the repulsing ray \(\Sigma_{e2}\), derives the scalar sliding dynamics, and then lists the pseudo-equilibrium feasibility condition \(I_c<I_{c0}\). The same page defines \(I_{c0}=b(r_1-\beta)/(\beta-r_0)\). Combining those printed formulas exposes the empty condition at equality, but the article does not replace it with the direct equality-case calculation given here.

Qin, Tang, Xiang, and Yang study a closely related Filippov infectious-disease model with limited medical resources and selection pressure. Their full text develops sliding segments, pseudo-equilibria, boundary equilibria, and sliding bifurcations for a different treatment law. Its pseudo-equilibrium is obtained from a different scalar sliding equation and does not imply the equality-surface formula above.

Shan and Zhu analyze a smooth SIR model in which recovery depends on hospital-bed availability. That work motivates hospital-capacity nonlinearities but has no discontinuous switching manifold and therefore does not imply this Filippov equality classification.

Targeted searches by DOI, exact title, the symbols \(I_{c0}\) and \(S_{c2}\), equality-threshold language, pseudo-equilibrium terminology, and correction/erratum terminology did not locate a published correction of this boundary case.

## Limitations

The correction is confined to the critical surface \(\mathcal R_0=1\). It does not reclassify the source's \(\mathcal R_0>1\) or \(\mathcal R_0<1\) regimes.

At the endpoint \(I_c=I_c^{\dagger}\), the pseudo-equilibrium coincides with the tangency point; the strict interior pseudo-saddle statement is therefore for \(0<I_c<I_c^{\dagger}\).

The publisher records the article as published online in December 2017 without an exact day. The day-resolved bibliographic record used for the machine-readable first-public-date field is 2018-01-01; the earlier month-only publisher evidence is retained here rather than converted into an invented calendar day.

An unindexed author note or correction could contain the same equality calculation.

## References

1. A. Wang, Y. Xiao, H. Zhu, “Dynamics of a Filippov epidemic model with limited hospital beds,” Mathematical Biosciences and Engineering 15 (2018), 739–764. DOI: 10.3934/mbe.2018033.
2. W. Qin, S. Tang, C. Xiang, Y. Yang, “Effects of limited medical resource on a Filippov infectious disease model induced by selection pressure,” Applied Mathematics and Computation 283 (2016), 339–354. DOI: 10.1016/j.amc.2016.02.042.
3. C. Shan, H. Zhu, “Bifurcations and complex dynamics of an SIR model with the impact of the number of hospital beds,” Journal of Differential Equations 257 (2014), 1662–1688. DOI: 10.1016/j.jde.2014.05.030.
