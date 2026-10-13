# Sharp urban-residence minimizer and a two-sided invasion window in an Oropouche model

## Finding

**Theorem (complete minimization of the autonomous invasion threshold).** In the positive-parameter autonomous Oropouche sloth–forest-midge–human–city-midge model specified below, let \(p\in[0,1]\) be the proportion of human time spent in the city, and define
\[
 x(p)=\frac{kN_A}{kN_A+(1-p)N_H},\quad x_0=\frac{kN_A}{kN_A+N_H},\qquad
 A=\frac{b^2\pi_{VH}\pi_{HV}N_F}{\mu_V(\mu_A+\gamma_A)N_A},\quad
 B=\frac{b^2\pi_{VH}\pi_{HV}N_F}{\mu_V(\mu_H+\gamma_H)N_H},\quad
 C=\frac{b^2\pi_{VH}\pi_{HV}N_C}{\mu_V(\mu_H+\gamma_H)N_H}.
\]
All three coefficients are strictly positive. The basic reproduction number \(\mathcal R_0(p)\) has **exactly one** global minimizer over \([0,1]\), characterized as follows.

If \(A\le C\), the minimizer is \(p=1\), and \(\min\mathcal R_0^2=C\). If \(A>C\), put \(x_*=(B+C)/(A+B)\). When \(x_0\ge x_*\), the minimizer is \(p=0\). When \(x_0<x_*\), it is the strictly interior point
\[
 p_*=1-\frac{kN_A}{N_H}\frac{A-C}{B+C}\in(0,1),\qquad
 \min_{0\le p\le1}\mathcal R_0(p)^2=\frac{A(B+C)}{A+B}.
\]
For \(A>C\) the function is strictly decreasing up to the stated minimizer and strictly increasing thereafter when the minimizer is interior, and strictly increasing on \((0,1)\) when the minimizer is \(p=0\). For \(A\le C\) it is strictly decreasing on \([0,1)\).

**Exact two-sided threshold witness.** With \(N_A=1\), \(N_H=N_F=N_C=4\), \(k=b=1\), \(\pi_{VH}=3/5\), \(\pi_{HV}=1\), \(\mu_A=\mu_H=\gamma_A=\gamma_H=1/2\), and \(\mu_V=1\), all demographic and transmission parameters are admissible and positive, and
\[
 A=\frac{12}{5},\qquad B=C=\frac35,\qquad
 p_*=\frac58,\qquad \min\mathcal R_0^2=\frac{24}{25}<1.
\]
Nevertheless \(\mathcal R_0(0)>1\) and \(\mathcal R_0(1)=\sqrt{12/5}>1\). The **complete** strict-subcritical interval is
\[
 \mathcal R_0(p)<1\quad\Longleftrightarrow\quad
 \frac12-\frac{\sqrt{30}}{20}<p<\frac12+\frac{\sqrt{30}}{20}.
\]
Hence intermediate urban residence can make the full infection-free state locally invasion-stable although both endpoint residence choices leave some transmission cycle supercritical. At \(p=1\), the supercritical cycle is isolated in wildlife; this does **not** imply urban human infection is supercritical.

## Assumptions and scope

Use the autonomous case of Peterson et al., *A novel mathematical model of seasonality in Oropouche virus transmission in Amazonas, Brazil*, equations (1)–(4), with constant disease-free populations \(N_A,N_F,N_H,N_C>0\), biting rate \(b>0\), forest-vector sloth preference \(k>0\), positive bite-transmission probabilities \(\pi_{VH},\pi_{HV}\le1\), human and sloth removal rates \(\mu_H+\gamma_H>0\) and \(\mu_A+\gamma_A>0\), and vector removal \(\mu_V>0\). Forest midges allocate their bites between sloths and forest-present humans in proportions \(x(p)\) and \(1-x(p)\); city midge–human bites do not depend on \(p\) under the printed model. Fix all other parameters as \(p\) varies. Choose constant vector recruitment so the disease-free values \(N_F,N_C\) are preserved. This theorem concerns the autonomous infection linearization and is not a result for seasonal forcing or fitted outbreak trajectories.

## Proof

At the disease-free equilibrium, source equations (2) and (3.1) yield the two-edge loop strengths \(R_{FA}=Ax^2\), \(R_{FH}=B(1-x)^2\), and \(R_{CH}=C\). The source's exact next-generation expression says that \(y(x)=\mathcal R_0(x)^2\) is the **larger** root of
\[
 P(y,x)=y^2-[Ax^2+B(1-x)^2+C]y+ACx^2=0.
 \tag{1}
\]
For \(0\le x<1\), the coefficient \(B>0\) makes the two roots distinct: the discriminant exceeds or equals \((Ax^2-C)^2\), strictly so for \(x<1\). In particular \(P(C,x)=-BC(1-x)^2<0\), so the smaller root lies below \(C\), the larger root \(y(x)\) lies above \(C\), and \(P_y(y(x),x)>0\). The positive-root formula also proves continuity at \(x=1\), where \(y(1)=\max\{A,C\}\).

Implicit differentiation gives
\[
 P_x(y,x)=2\big[By(1-x)-Ax(y-C)\big],\qquad
 y'(x)=-\frac{P_x(y(x),x)}{P_y(y(x),x)}.
 \tag{2}
\]
At \(x=0\), the larger root is \(B+C\) and \(y'(0)=-2B<0\). For any interior stationary point, \(By(1-x)=Ax(y-C)\). Factor (1) as \((y-Ax^2)(y-C)=By(1-x)^2\). Substitution into this identity and division by \(y-C>0\) give \(y=Ax\). Putting this in the stationary equation and dividing by \(Ax>0\) yields \(B(1-x)=Ax-C\). Therefore every interior stationary point must equal
\[
 x=x_*:=\frac{B+C}{A+B},\qquad y=\frac{A(B+C)}{A+B}.
 \tag{3}
\]
If \(A\le C\), the candidate \(x_*\ge1\), so no interior stationary point exists; continuity of the derivative and its negative sign at zero show strict decrease. If \(A>C\), \(x_*\in(0,1)\) and the value in (3) exceeds \(C\). Direct substitution in (1) verifies the candidate lies on the larger-root branch, hence is an actual stationary point. There can be no other one. Near \(x=1\) the larger root tends to \(A\), and (2) gives \(y'(1^-)=2A>0\). Thus (3) is the unique strict global minimum on \([0,1]\). Since \(x(p)\) strictly increases from \(x_0\) to \(1\), restricting to the physical interval gives precisely the three cases in the theorem; solving \(x(p_*)=x_*\) gives the displayed \(p_*\).

For the exact example, (1) becomes \(P(1,x)=[-39x^2+30x-5]/25\), and \(x(p)=1/(5-4p)\). Therefore
\[
 P(1,x(p))=\frac{6-80(p-1/2)^2}{25(5-4p)^2}.
 \tag{4}
\]
The smaller root stays below \(C=3/5<1\) for \(p<1\), so \(\mathcal R_0(p)<1\) holds exactly when \(P(1,x(p))>0\). Formula (4) proves the two exact endpoints. At \(p=0\), \(P(1,x_0)=-14/625<0\), while at \(p=1\), \(y(1)=A=12/5>1\). At \(x_*=2/5\), equation (3) gives \(y=24/25\), proving the minimum and the asserted strict-subcritical interval. These arguments cover all boundaries, including the reducible \(p=1\) endpoint.

## Verification

Run `python3 verify.py` from this package directory. The checker uses Python standard-library exact rational arithmetic to verify the chosen model's loop coefficients, the defining quadratic, the exact optimizer and threshold identity (4), and the signs at the two endpoint configurations. It also performs deterministic random-parameter finite stress tests of the sharp minimization formula; these tests are checks, not proofs of the quantified theorem. The complete proof is the implicit-differentiation argument above.

## Relationship to prior work

Peterson et al. (2026), Sect. 3.1, derives (1), its three loop strengths and bounds on the baseline reproduction number, and subsequently concentrates on seasonality and parameter fits. Their equations do not give the sharp optimizer over human urban-residence fraction or the exact subcritical window in (4). Shetgaonkar and Sharma (2026), Sect. 4.1, already obtain a minimizer of the reproduction number against *vector feeding preference* for a different **two-host, one-vector** network; therefore the generic fact that host-choice curves can be U-shaped is not claimed here. Althouse (2026) examines weighted versus unweighted force-of-infection definitions in multi-host, multi-vector systems but does not imply (3) for the Oropouche path with a fixed urban loop. The earlier host-competition/vector-preference work of Zhu et al. (2022) characterizes dilution/amplification, not the exact Oropouche optimizer. Related published multi-patch SEIR spectral comparisons address different coupling structures.

## Limitations

The result is an exact **baseline local invasion-threshold** classification, not a theorem on global elimination, nonlinear endemic attractors, forced reproduction numbers, or the effect of changing \(p\) on recruitment or midge ecology. The rational example is synthetic and is not calibrated to Amazonas field values. At \(p=1\), the forest wildlife infection can grow although the forest-to-human pathway is severed; interpreting \(\mathcal R_0(1)>1\) as evidence of urban human invasion would be incorrect. Prior analytic work already establishes other U-shaped host-choice reproduction thresholds, and unindexed source material could contain a directly overlapping four-node optimization.

## References

1. C. Peterson, D. Gandhi, E. Slack, E. Rubio, A. Claxton and C. M. Kribs, *A novel mathematical model of seasonality in Oropouche virus transmission in Amazonas, Brazil*, Journal of Mathematical Biology **93**, article 21 (published 24 July 2026), DOI: https://doi.org/10.1007/s00285-026-02422-1. Full-text Sections 2.2, 3.1, 4 and Appendix A read.
2. D. Gandhi et al., *A Novel Mathematical Model of Oropouche Virus Transmission Dynamics*, BEER 2025 oral presentation, repository: https://ir.library.illinoisstate.edu/beer/2025/parallel_session_3/19/ (public presentation listed as 9 November 2025; attached historical abstract could not be read).
3. S. Shetgaonkar and A. Sharma, *Modeling the impact of host diversity on the evolution of vector feeding preferences and implications for disease control*, arXiv:2604.27113 (29 April 2026), https://arxiv.org/abs/2604.27113. Public full-text reproduction and Section 4.1 read at https://www.researchgate.net/publication/404333449_Modeling_the_impact_of_host_diversity_on_the_evolution_of_vector_feeding_preferences_and_implications_for_disease_control.
4. B. M. Althouse, *Ecological specialization in vectors alters transmission thresholds and endemic dynamics in multi-host, multi-vector systems*, PLOS Computational Biology **22** e1014754 (11 September 2026), https://doi.org/10.1371/journal.pcbi.1014754. Full-text Sections 2.1–2.3 and discussion read.
5. *Host competence, interspecific competition and vector preference interact to determine the vector-borne infection ecology*, Frontiers in Ecology and Evolution (2022), https://doi.org/10.3389/fevo.2022.993844. Methods and comparison section read.
