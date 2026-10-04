# Fixed-window incidence has exactly the same structural parameter ambiguity as cumulative incidence in the closed SEIR model

## Finding

Consider the closed SEIR system
\[
\dot S=-\beta SI,\qquad
\dot E=\beta SI-\gamma E,\qquad
\dot I=\gamma E-\alpha I,\qquad
\dot R=\alpha I,\qquad
\dot C=\beta SI,
\]
with nonnegative initial states and positive parameters. The auxiliary state \(C\) is cumulative incidence.

Fix any reporting window \(h>0\) and define the continuous sliding-window incidence observable
\[
J_h(t)=C(t)-C(t-h),\qquad t\ge h.
\]

Perfect continuous observation of \(J_h\) has exactly the same structural parameter indistinguishability classes as perfect continuous observation of \(C\). Consequently, the cumulative-incidence structural-identifiability classification established for this model transfers verbatim to fixed-window incidence:
\[
\text{known }S(0),E(0),I(0)
\quad\Longrightarrow\quad
\alpha,\beta,\gamma\text{ are globally structurally identifiable},
\]
whereas with unknown initial conditions the parameters are generically only locally identifiable, with the same twofold ambiguity
\[
(\alpha,\beta,\gamma)
\longmapsto
\left(\frac{\alpha\gamma}{\beta},\gamma,\beta\right).
\]

The same conclusion holds for instantaneous incidence
\[
j(t)=\dot C(t)=\beta S(t)I(t).
\]

Thus the practical superiority of incidence over cumulative incidence reported in the motivating paper is not caused by a different perfect-data structural ambiguity in this SEIR model. It must come from the finite sampling design, noise model, weighting, or numerical estimation procedure.

## Assumptions and scope

Structural identifiability is understood in the standard perfect-data sense: the chosen output is observed continuously and without noise. For \(J_h\), the observation is the continuous sliding-window output \(t\mapsto C(t)-C(t-h)\) for a fixed \(h>0\), not merely a finite list of non-overlapping reported counts.

The result concerns parameter identifiability. The additive level of \(C\) is auxiliary and does not feed back into the equations for \(S,E,I,R\).

The global/local classification quoted above is the one proved for cumulative incidence in the motivating paper. The present contribution proves that the same classification necessarily holds for fixed-window and instantaneous incidence.

## Proof

Since
\[
\dot C=\beta SI=-\dot S,
\]
every solution satisfies
\[
C(t)=C(0)+S(0)-S(t).
\]
Because \(S(t)\ge0\) and \(\dot S\le0\), \(S(t)\) has a finite limit, and therefore \(C(t)\) has a finite limit as \(t\to\infty\).

Take two admissible solutions, possibly with different parameters and initial conditions, and suppose their window-incidence outputs agree:
\[
J_{h,1}(t)=J_{h,2}(t)
\qquad\text{for every }t\ge h.
\]
Set
\[
D(t)=C_1(t)-C_2(t).
\]
Equality of the outputs gives
\[
D(t)=D(t-h)
\qquad\text{for every }t\ge h.
\]
Equivalently,
\[
D(t+h)=D(t)
\qquad\text{for every }t\ge0.
\]
Thus \(D\) is \(h\)-periodic on \([0,\infty)\).

Both \(C_1\) and \(C_2\) converge, so \(D\) also converges to some finite limit \(L\). For any fixed \(t\ge0\),
\[
D(t)=D(t+nh)
\]
for every integer \(n\ge0\). Letting \(n\to\infty\) gives
\[
D(t)=L.
\]
Hence
\[
C_1(t)-C_2(t)\equiv L.
\]

A constant shift of \(C\) does not alter \(\dot C=\beta SI\) and does not enter the equations for \(S,E,I,R\). Therefore two parameter vectors produce the same perfect \(J_h\) output if and only if, after at most an irrelevant additive shift of the auxiliary variable \(C\), they produce the same perfect cumulative-incidence output. Their parameter indistinguishability classes are identical.

For instantaneous incidence, equality of
\[
j_1(t)=\dot C_1(t)
\quad\text{and}\quad
j_2(t)=\dot C_2(t)
\]
for all \(t\) immediately implies
\[
C_1(t)-C_2(t)=\text{constant},
\]
so the same argument applies.

Saucedo et al. prove for cumulative incidence that the parameter vector is globally structurally identifiable when \(S(0),E(0),I(0)\) are known, and generically locally identifiable when they are unknown. Their nontrivial alternative parameter branch is
\[
(\alpha,\beta,\gamma)
\longmapsto
\left(\frac{\alpha\gamma}{\beta},\gamma,\beta\right).
\]
Because the observation equivalence above preserves the full parameter indistinguishability relation, these conclusions transfer exactly to \(J_h\) and \(j\).

## Verification

The proof above is analytic and does not rely on finite experiments.

The bundled script verifies algebraically that the source's alternative parameter map is an involution and preserves the three parameter combinations used in its cumulative-incidence input-output calculation:
\[
\alpha\gamma,\qquad
\beta\gamma,\qquad
\beta+\gamma.
\]

It also checks exact rational examples and the fixed set \(\beta=\gamma\). These computations support the transcription of the source's twofold branch; they are not used to prove the window-incidence equivalence.

## Relationship to prior work

Saucedo et al., first posted as arXiv:2401.15076 and later published as DOI 10.3934/math.20241204, explicitly define cumulative incidence by
\[
\dot C=\beta SI
\]
and practical incidence over reporting intervals by differences of \(C\). Their structural analysis establishes the cumulative-incidence classification but states that the available software tools could not handle incidence defined as a difference in time, so structural incidence was left unanalyzed.

The same paper reports that incidence is substantially better than cumulative incidence in its practical-identifiability experiments. Its discussion also notes that the synthetic cumulative-data noise model is unrealistic and that accumulating noisy incidence would introduce temporal correlation. The theorem above separates these practical effects from structural identifiability: under perfect continuous observation, cumulative and fixed-window incidence are parameter-equivalent for this closed SEIR system.

Tuncer and Le (2018), DOI 10.1016/j.mbs.2018.02.004, analyze structural and practical identifiability of classical outbreak models using prevalence and cumulative-incidence observations. The inspected published abstract confirms structurally identifiable cumulative-incidence cases and practical difficulties, but it does not supply the fixed-window equivalence theorem above.

## Limitations

The theorem does not say that incidence and cumulative-incidence data have equal Fisher information, equal condition numbers, equal robustness to noise, or equal practical identifiability at a finite observation grid.

The sliding-window structural output \(J_h(t)\) is a perfect continuous-time idealization. A finite sequence of reported interval counts can lose information because of sparse sampling, even though the corresponding continuous window output has the same structural ambiguity as cumulative incidence.

The result uses convergence of cumulative incidence, which follows here from the closed nonnegative SEIR identity
\[
C(t)=C(0)+S(0)-S(t).
\]
Models with demographic turnover, external forcing, or unbounded cumulative incidence require a separate argument.

## References

1. O. Saucedo, A. Laubmeier, T. Tang, B. Levy, L. Asik, T. Pollington, O. Prosper Feldman, “Comparative Analysis of Practical Identifiability Methods for an SEIR Model,” arXiv:2401.15076, first submitted 26 January 2024; AIMS Mathematics 9 (2024), 24722–24761, DOI: 10.3934/math.20241204.
2. N. Tuncer, T. T. Le, “Structural and practical identifiability analysis of outbreak models,” Mathematical Biosciences 299 (2018), 1–18, DOI: 10.1016/j.mbs.2018.02.004.
