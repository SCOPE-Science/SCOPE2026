# A one-crossing fragmentation law and a universal rescue-gap for fixed-area reserves

## Finding

An exact one-versus-two-reserve benchmark distinguishes mean persistence from persistence at every horizon. Let \(A>0\) be a fixed habitat-area budget, \(k>0\) an extinction-rate scale, and \(\alpha>0\) a patch-area exponent. One undivided, initially occupied reserve of area \(A\) suffers local extinction at rate
\[
m=kA^{-\alpha}>0.
\]
Alternatively, divide the same area equally into two initially occupied reserves. Each half-reserve suffers independent local extinction at rate \(h=k(A/2)^{-\alpha}=2^\alpha m>m\). If exactly one half-reserve remains occupied, it recolonizes the empty half at rate \(c\ge0\); global extinction is absorbing. Denote the two extinction times by \(T_1\) and \(T_2\), respectively, and set \(S_j(t)=\Pr(T_j>t)\).

Define two rescue thresholds
\[
c_{\mathrm{mean}}=\frac{2h^2}{m}-3h,\qquad
c_{\mathrm{tail}}=\frac{(h-m)(2h-m)}{m}=c_{\mathrm{mean}}+m>0.
\]
Then the following assertions hold for every such \(A,k,\alpha\) and \(c\):

1. The split reserve has greater mean persistence exactly when \(c>c_{\mathrm{mean}}\), and equal mean persistence exactly when \(c=c_{\mathrm{mean}}\) (if this latter value is admissible).
2. The split reserve strictly improves survival at **every** positive time horizon, \(S_2(t)>S_1(t)\) for all \(t>0\), **if and only if** \(c\ge c_{\mathrm{tail}}\).
3. If \(0\le c<c_{\mathrm{tail}}\), there is exactly one \(t_*(c)\in(0,\infty)\) such that \(S_2(t)>S_1(t)\) for \(0<t<t_*(c)\), equality holds at \(t=t_*(c)\), and \(S_2(t)<S_1(t)\) for \(t>t_*(c)\). This crossover horizon increases strictly with \(c\).
4. The crossover horizon diverges with a sharp, explicit law:
\[
\lim_{c\uparrow c_{\mathrm{tail}}}(c_{\mathrm{tail}}-c)t_*(c)
=\frac{2h^2-m^2}{m^2}\log\!\left(\frac{2h^2}{2h^2-m^2}\right).
\]
In particular, the gap between the mean-persistence and all-horizon rescue thresholds is **exactly the single-reserve extinction rate** \(m\), independently of the area exponent \(\alpha\). For every \(\alpha>0\), some nonnegative \(c\) makes splitting beneficial in mean but harmful at all sufficiently late horizons.

## Assumptions and scope

The model is a continuous-time Markov occupancy process, not an individual-count or dispersal-mortality model. Each occupied half-reserve loses occupancy at rate \(h\), independently of the other reserve. From the state of exactly one occupied half-reserve, a successful recolonization occurs at rate \(c\), restoring the state with two occupied reserves. Both start occupied; no colonization from outside is possible after both are empty. Recolonization has no additional extinction hazard or budget cost in this conditional comparison. Areas are exactly \(A\) or \(A/2\), not random. The area-power relation is an explicit model assumption, not an empirical universal law.

The one-reserve time is exponential with rate \(m\). For the split reserve, let \(N(t)\in\{2,1,0\}\) count occupied half-reserves, with \(0\) absorbing. Its transitions are
\[
2\xrightarrow{2h}1,\quad 1\xrightarrow{c}2,\quad 1\xrightarrow{h}0.
\]
Thus its transient generator, ordered by occupied counts \(2,1\), is
\[
Q=\begin{pmatrix}-2h&2h\\c&-(h+c)\end{pmatrix}.
\]

## Proof

**Exact extinction-time transform.** Absorption from state \(1\) occurs at rate \(h\). Inverting the transient resolvent gives, for every \(s\ge0\),
\[
\mathbb E[e^{-sT_2}]
=(1,0)(sI-Q)^{-1}\binom{0}{h}
=\frac{2h^2}{s^2+(3h+c)s+2h^2}.
\]
Define the distinct positive rates
\[
\lambda_- =\frac{3h+c-\sqrt{(3h+c)^2-8h^2}}2,
\qquad
\lambda_+ =\frac{3h+c+\sqrt{(3h+c)^2-8h^2}}2.
\]
The discriminant is positive for \(h>0,c\ge0\); \(\lambda_-\lambda_+=2h^2\), \(\lambda_-+\lambda_+=3h+c\), and \(0<\lambda_-<\lambda_+\). Uniqueness of Laplace transforms identifies \(T_2\) in distribution with the sum of two independent exponentials of rates \(\lambda_-\) and \(\lambda_+\). Hence
\[
S_2(t)=\frac{\lambda_+e^{-\lambda_-t}-\lambda_-e^{-\lambda_+t}}{\lambda_+-\lambda_-},
\quad S_1(t)=e^{-mt},
\quad \mathbb E[T_2]=\frac{3h+c}{2h^2},\quad \mathbb E[T_1]=\frac1m.
\]
The assertion about means is immediate, including equality and boundary cases.

**All-horizon ordering and unique crossover.** Put \(d=\lambda_+-\lambda_->0\) and \(u=e^{-dt}\). The split extinction-time hazard is
\[
H_2(t)=-\frac{d}{dt}\log S_2(t)
=\frac{\lambda_-\lambda_+(1-u)}{\lambda_+-\lambda_-u}.
\]
It starts at \(0\), increases strictly for \(t>0\), and approaches \(\lambda_-\):
\[
H_2'(t)=\frac{\lambda_-\lambda_+d^2u}{(\lambda_+-\lambda_-u)^2}>0.
\]
For \(R(t)=S_2(t)/S_1(t)\), we have \(R(0)=1\) and \((\log R)'=m-H_2(t)\). Therefore, if \(\lambda_-\le m\), \(R\) is strictly increasing for finite \(t\) and the split option is always better. If \(\lambda_->m\), \(R\) first rises, later decreases, and tends to \(0\). It consequently crosses \(1\) at exactly one strictly positive time.

Because \(\lambda_+\ge 2h>m\), the condition \(\lambda_-\le m\) is equivalent to the characteristic polynomial being nonpositive at \(m\):
\[
m^2-(3h+c)m+2h^2\le0
\quad\Longleftrightarrow\quad
c\ge\frac{(h-m)(2h-m)}m=c_{\mathrm{tail}}.
\]
This proves the sharp universal horizon threshold and the unique-crossover alternative, including \(c=0\) and \(c=c_{\mathrm{tail}}\).

**Crossover monotonicity in rescue.** Couple the processes at rates \(0\le c_1<c_2\) by using the same local-extinction clocks and the same recolonization opportunities of rate \(c_1\), with independent additional recolonization opportunities of rate \(c_2-c_1\) only for the second process. The occupied set of the first process remains a subset of that of the second, so \(S_2(t;c_2)\ge S_2(t;c_1)\). The inequality is strict for all \(t>0\): with positive probability in any positive time interval, one reserve first empties, the extra recolonization event restores it only in the higher-rescue process, and the other reserve then empties while the restored reserve persists. On \([0,c_{\mathrm{tail}})\), a larger \(c\) therefore makes the survival difference strictly positive at the smaller \(c\)'s unique crossover, so its own unique crossover occurs strictly later.

**Critical divergence.** At \(c=c_{\mathrm{tail}}\), \(\lambda_-=m\) and \(\lambda_+=2h^2/m\). The slow eigenrate obeys
\[
\frac{d\lambda_-}{dc}=-\frac{\lambda_-}{\lambda_+-\lambda_-},
\quad
\lambda_-(c)-m\sim \frac{m^2}{2h^2-m^2}(c_{\mathrm{tail}}-c).
\]
The unique crossover tends to infinity as \(c\uparrow c_{\mathrm{tail}}\) by strict survival ordering and continuity. At that crossover, rearrange \(R(t_*)=1\) to obtain
\[
(\lambda_--m)t_*=\log\!\left(\frac{\lambda_+}{\lambda_+-\lambda_-}\right)
+\log\!\left(1-\frac{\lambda_-}{\lambda_+}e^{-(\lambda_+-\lambda_-)t_*}\right).
\]
The second logarithm tends to zero and the first tends to \(\log(2h^2/(2h^2-m^2))\), proving the claimed limit. Finally, subtracting the two thresholds gives \(c_{\mathrm{tail}}-c_{\mathrm{mean}}=m\). Since \(c_{\mathrm{tail}}>\max(0,c_{\mathrm{mean}})\), there always exists an admissible rescue rate for which the mean and sufficiently late horizon preferences disagree. All statements follow.

## Verification

For \(\alpha=1\), \(m=1\), \(h=2\), one obtains \(c_{\mathrm{mean}}=2\) and \(c_{\mathrm{tail}}=3\). At \(c=5/2\),
\[
\mathbb E[T_2]=\frac{17}{16}>1=\mathbb E[T_1],
\quad \lambda_-=\frac{17-\sqrt{161}}4>1,
\]
so the split option has the larger mean despite a smaller survival probability at all sufficiently late horizons. Its unique horizon crossover is approximately \(2.0154308463\) time units. For this area scaling, the crossover divergence constant is \(7\log(8/7)\).

The accompanying `check.py` uses exact symbolic inversion to reproduce the Laplace transform, mean and threshold identities, then independently solves the transient-generator equations for 256 rational parameter choices. It also verifies the illustrative crossover numerically. These finite checks do not establish the universal statements, which are proved above.

## Relationship to prior work

Quinn and Hastings (1987) discuss extinction in subdivided habitats and the short-horizon advantage of subdivision. Etienne and Heesterbeek (2000) study the optimal number and size of reserves using mean extinction time and a patch reproductive measure. Nicol and Possingham (2010) examine whether restoration should expand patch area or increase patch count with stochastic dynamic programming. These studies motivate the fixed-area comparison, but the accessible material does not provide the present exact one-crossing classification under positive recolonization or the constant-width separation between mean and all-horizon thresholds.

Hartig and Drechsler (2008, arXiv:0807.4040) establish horizon-independent rankings for a single species **within their exponential, quasi-stationary survival model**. The two-patch process here starts with full occupancy and has a strictly increasing extinction-time hazard rather than an exponential survival law; thus its time-horizon reversal does not contradict that paper's theorem. Niebuhr and collaborators (2015) investigate habitat fragmentation and animal search movement by spatial simulations, not this finite-state extinction/recolonization comparison.

The compound-exponential transform and increasing-hazard property are standard phase-type facts; no novelty is claimed for them in isolation. The proposed contribution is their exact application to this area-constrained conservation comparison, including its necessary-and-sufficient crossing criterion, the unchanging \(m\)-width gap, and the critical divergence law.

## Limitations

The two equally sized patches are assumed to start occupied, and their extinction clocks are independent; a common catastrophe mechanism, unsplit-patch rescue, colonization costs, edge effects and individual demographic dynamics are not included. The parameter \(c\) is a freely specified successful recolonization rate rather than a derived geometry-dependent dispersal rate. Results therefore do not determine an empirically optimal reserve design without calibration.

Relevant early papers by Quinn and Hastings (1987), Etienne and Heesterbeek (2000), and Nicol and Possingham (2010) could be evaluated from published abstracts and references, but their complete texts were not accessible here. An equivalent specialized theorem in those full texts or in reliability theory cannot be categorically excluded. The mathematical proof is exact for the explicit model; neither general ecological validity nor literature exhaustiveness is asserted.

## References

1. Quinn, J. F., and Hastings, A. (1987). “Extinction in Subdivided Habitats.” *Conservation Biology* 1, 198–209. DOI: 10.1111/j.1523-1739.1987.tb00033.x.
2. Etienne, R. S., and Heesterbeek, J. A. P. (2000). “On Optimal Size and Number of Reserves for Metapopulation Persistence.” *Journal of Theoretical Biology* 203, 33–50. DOI: 10.1006/jtbi.1999.1060.
3. Hartig, F., and Drechsler, M. (2008). “The time horizon and its role in multiple species conservation planning.” *Biological Conservation* 141, 2625–2631. arXiv:0807.4040; DOI: 10.1016/j.biocon.2008.07.028.
4. Nicol, S. C., and Possingham, H. P. (2010). “Should metapopulation restoration strategies increase patch area or number of patches?” *Ecological Applications* 20, 566–581. DOI: 10.1890/08-2216.1. First published online 2010-03-01.
5. Niebuhr, B. B. S., and coauthors (2015). “Survival in patchy landscapes: the interplay between dispersal, habitat loss and fragmentation.” *Scientific Reports* 5, 11898. DOI: 10.1038/srep11898.
