# A sharp directed-rescue allocation law for two habitat patches

## Finding
Let \(e_1,e_2,C>0\). A species occupies either, both, or neither of two habitat patches. Local extinctions occur at rate \(e_i\) whenever patch \(i\) is occupied. Colonization from occupied patch 1 into empty patch 2 occurs at rate \(u\); colonization in the opposite direction occurs at rate \(v\). The state \(00\) is absorbing. Budget equality means \(u+v=C\), with \(u,v\ge0\).

Let the initial state be \(10\), \(01\), or \(11\) with respective probabilities \(\alpha,\beta,\gamma\ge0\), \(\alpha+\beta+\gamma=1\), independent of subsequent transitions. Put \(S=e_1+e_2\) and let \(\mathcal T(u)\) be the expected time to absorption. For a feasible range \(\ell\le u\le C-r\), where \(\ell,r\ge0\) and \(\ell+r\le C\), its **unique maximizer** is

\[
\boxed{u_* = \operatorname{proj}_{[\ell,C-r]}\!\left(\frac{C+\alpha e_1-\beta e_2}{2}\right),\qquad v_*=C-u_*.}
\]

If the interval is a singleton, that feasible choice is necessarily optimal; otherwise the objective is strictly concave. In particular, without lower bounds, the optimal policy is strictly interior exactly when \(-C<\alpha e_1-\beta e_2<C\), all directed from patch 1 when \(\alpha e_1-\beta e_2\ge C\), and all directed from patch 2 when \(\alpha e_1-\beta e_2\le-C\). The boundary equalities still give unique endpoint optima.

The result also gives an exact mean-persistence loss under any other allocation. With \(u_0=(C+\alpha e_1-\beta e_2)/2\),

\[
\mathcal T(u_*)-\mathcal T(u)
=\frac{(u-u_0)^2-(u_*-u_0)^2}{e_1e_2(C+e_1+e_2)}\quad(\ell\le u\le C-r).
\]

## Assumptions and scope
This is a four-state, homogeneous, continuous-time Markov chain. There is no immigration from outside the two patches and no recolonization of the globally empty state. Each local extinction clock runs at the same rate regardless of occupation of the other patch, and the two directional colonization rates are independently controllable but have a fixed sum. All inputs are known constants, with no demographic variation within an occupied patch. The target is the **unconditional expected time to total extinction from the specified initial distribution**, not the probability of survival at any fixed time or the quasi-stationary mean lifetime.

## Proof
Write \(t_{10},t_{01},t_{11}\) for the mean time to hit \(00\) from each nonempty state. The only transitions are \(10\to00\) at rate \(e_1\), \(10\to11\) at rate \(u\), \(01\to00\) at rate \(e_2\), \(01\to11\) at rate \(v\), \(11\to01\) at rate \(e_1\), and \(11\to10\) at rate \(e_2\). The backward equations, with \(S=e_1+e_2\), are

\[
(e_1+u)t_{10}-ut_{11}=1,\quad
(e_2+v)t_{01}-vt_{11}=1,\quad
St_{11}-e_2t_{10}-e_1t_{01}=1.
\]

The coefficient determinant is \(e_1e_2(S+u+v)>0\). Hence the unique finite solution is

\[
 t_{10}=\frac{(u+e_2)(v+S)}{e_1e_2(S+u+v)},\quad
 t_{01}=\frac{(v+e_1)(u+S)}{e_1e_2(S+u+v)},
\]
\[
 t_{11}=\frac{uv+(u+v)S+e_1^2+e_1e_2+e_2^2}{e_1e_2(S+u+v)}.
\]

(Each formula may also be checked directly in the backward equations.) The chain reaches \(00\) almost surely: there is a positive-probability finite sequence of consecutive extinctions from each nonempty state, and the finite transient class has no closed communicating component. Substituting \(v=C-u\), then weighting the expressions by \(\alpha,\beta,\gamma\), gives

\[
 \mathcal T'(u)=\frac{C+\alpha e_1-\beta e_2-2u}{e_1e_2(C+S)},\qquad
 \mathcal T''(u)=-\frac{2}{e_1e_2(C+S)}<0.
\]

Strict concavity on the feasible interval proves the projected unique optimizer and both sharp endpoint thresholds. Completing the square gives the exact regret identity displayed above. If initially both patches are occupied (\(\gamma=1\)), the optimizer is \(u=v=C/2\) even for unequal \(e_1,e_2\). If initially only patch 1 is occupied (\(\alpha=1\)), the optimizer is \(u_*=\min\{C,(C+e_1)/2}\); therefore the one-way to split transition occurs exactly at \(C=e_1\). The analogous formula for initially only patch 2 is obtained by relabeling. All boundary cases are included.

## Verification
The standalone `two_patch_verification.py` uses a separately implemented Gaussian-elimination solution of the three nonabsorbing-state backward equations, and compares it with the closed forms. It checks 5,000 seeded random admissible sets of rates, initial-state probabilities and allocations, verifies the exact quadratic regret formula, compares feasible constrained policies, and tests rational examples. Run `python3 two_patch_verification.py`; it uses only the Python standard library.

For \(e_1=1\), \(e_2=4\), and \(C=2\), an initially fully occupied pair has optimum \(u=v=1\) and expected lifetime \(8/7\). Either one-way policy instead yields \(31/28\). From state \(10\), the unique optimum shifts to \(u=3/2\), \(v=1/2\), where the mean lifetime is \(121/112\); a policy incapable of colonization from patch 1 has mean lifetime \(1\). These numbers follow exactly from the equations, independent of floating-point calculations.

## Relationship to prior work
Day and Possingham (1995) give general stochastic patch-occupancy transition-matrix construction, including directed colonization and a two-patch example, in a **discrete annual-step model**. The present continuous-time mean-persistence optimization concerns a different transition mechanism and a fixed directional-rate sum; their general matrix framework alone does not state the sharp initial-condition-dependent optimizer.

Etienne and Heesterbeek (2001) study interventions changing local extinction or colonization probabilities and report qualitative prioritization rules. Their full text was not accessible in this inspection; their work is a material possible prior for a more specialized allocation theorem, not evidence of its absence.

Ross and Pollett (2009, conference version) analyze budget tradeoffs between **homogeneous** colonization and extinction rates, and explicitly identify targeted versus uniform patch interventions as a direction for further work. Frank and Wissel (2002) propose an approximation for heterogeneous landscapes' mean persistence, rather than an exact initial-state-dependent two-directional-rate allocation for a minimal continuous-time chain.

## Limitations
The statement applies only to two habitat patches and fixed directed rescue-rate budgets; it is not asserted for larger networks, nonlinear ecological costs, density-dependent local populations, external recolonization, finite-horizon survival probabilities or all alternative stochastic updating conventions. Its ecological applicability requires independent empirical justification of exponential clocks and of a budget linear in colonization rates. The complete 2001 Etienne–Heesterbeek article remains inaccessible and a more general existing Markov conservation optimization theorem might imply the formula. Historical priority has not been independently established. The executable tests are finite checks, not a substitute for the algebraic proof.

## References
- Day, J. R., and H. P. Possingham (1995), *A stochastic metapopulation model with variability in patch size and position*, Theoretical Population Biology 48, 333–360. DOI: 10.1006/tpbi.1995.1034. Author-uploaded full-text transcription: https://www.researchgate.net/publication/256906366_A_Stochastic_Metapopulation_Model_with_Variability_in_Patch_Size_and_Position
- Etienne, R. S., and J. A. P. Heesterbeek (2001), *Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model*, The American Naturalist 158, 389–407. DOI: 10.1086/321986. Abstract: https://www.journals.uchicago.edu/doi/10.1086/321986
- Ross, J. V., and P. K. Pollett (2009), *Rules of thumb for metapopulation management*, MODSIM09, 1795–1801. Author-uploaded complete-text transcription: https://www.researchgate.net/publication/43511313_Rules_of_thumb_for_metapopulation_management
- Frank, K., and C. Wissel (2002), *A formula for the mean lifetime of metapopulations in heterogeneous landscapes*, The American Naturalist 159, 530–552. DOI: 10.1086/338991.
