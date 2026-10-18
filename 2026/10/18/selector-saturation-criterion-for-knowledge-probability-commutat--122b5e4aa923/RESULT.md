# Selector-saturation criterion for knowledge-probability commutation

## Finding

An exact condition characterizes when taking the lower subjective probability across an S5 information cell agrees, on **every event**, with first taking the known part of that event and then assigning it probability. The condition says that all probability measures in a source information cell have the same masses on target information cells, and that the source cell contains **every joint extreme selection** of one target world per positively weighted target cell. The resulting bound on the size of the source information cell is sharp.

Let \(K\) act on events by S5 knowledge, and \(\mathsf{Pr}\) assign a world's probability to events. The quantitative identity being classified is
\[
(K\mathsf{Pr}(P))(w)=(\mathsf{Pr}(KP))(w)
\quad\text{for every }w\in W,\ P\subseteq W.
\]
The formula on the left is the minimum of the probabilities of \(P\) across worlds epistemically accessible from \(w\); the formula on the right is the probability, assessed at \(w\), that \(P\) holds everywhere in the accessible information cell. In the two-layer syntax of the motivating probabilistic-epistemic logic, \(\mathsf{Pr}\) may be indexed by a separate probability agent, while \(K\) is the knowledge modality of a fixed knowledge agent.

## Assumptions and scope

Fix a finite nonempty world set \(W\), an equivalence relation \(E\) on \(W\), and a probability vector \(\mu_w\) on \(W\) at each \(w\in W\). These vectors are unrestricted: they need not have full support and need not concentrate on the equivalence class of \(w\). In particular, the theorem applies to the full-power-set probability algebras allowed by the finite probabilistic-model semantics.

Let \(\mathcal B=W/E\) denote the set of nonempty information cells. For \(P\subseteq W\) define
\[
K_E(P)=\bigcup\{D\in\mathcal B:D\subseteq P\}.
\]
For a fixed source cell \(C\in\mathcal B\), define condition **(M)**: the number \(q_C(D)=\mu_v(D)\) is independent of \(v\in C\) for each target cell \(D\in\mathcal B\). These nonnegative numbers sum to one. Write \(\mathcal J_C=\{D\in\mathcal B:q_C(D)>0\}\), which is nonempty.

Define condition **(S)**: for **every function** \(s\) on \(\mathcal J_C\) satisfying \(s(D)\in D\), there exists \(v\in C\) such that
\[
\mu_v=\sum_{D\in\mathcal J_C}q_C(D)\,\delta_{s(D)}.
\]

**Theorem.** The following are equivalent: (i) for every \(w\in W\) and \(P\subseteq W\), \(\min_{v\in[w]_E}\mu_v(P)=\mu_w(K_E(P))\); (ii) **(M)** and **(S)** hold for every source cell \(C\). Furthermore, every such source cell satisfies
\[
|C|\ \ge\ \prod_{D\in\mathcal J_C}|D|.
\]
The bound cannot be improved as a condition on a single source cell with prescribed positive target-cell masses.

## Proof

**Necessity of block-mass uniformity.** Assume (i), and let \(C\) be any source cell. For a target block \(D\in\mathcal B\), take \(P=D\). Since \(D\) is a union of entire \(E\)-blocks, \(K_E(D)=D\). Consequently
\[
\mu_w(D)=\min_{v\in C}\mu_v(D)\qquad(w\in C),
\]
which is independent of \(w\). This proves (M), including the same statement for every target block.

**Necessity of complete selector coverage.** Fix \(C\), its common block-mass vector \(q_C\), and any selector \(s(D)\in D\) on \(\mathcal J_C\). Let
\[
P=W\setminus\{s(D):D\in\mathcal J_C\}.
\]
Every positive-mass block has an excluded point, while all remaining blocks have mass zero. Thus \(\mu_w(K_E(P))=0\) for all \(w\in C\). Condition (i) implies that some \(v\in C\) has \(\mu_v(P)=0\), the minimum being attained because \(C\) is finite. Hence \(\mu_v\) is supported on the selected points and, by (M), assigns mass exactly \(q_C(D)\) to \(s(D)\) in each \(D\in\mathcal J_C\). This is (S).

**Sufficiency.** Assume (M) and (S). For every \(v\in C\) and event \(P\), the measure of \(P\) is at least the total mass of all target cells wholly contained in \(P\):
\[
\mu_v(P)\ge\sum_{D\subseteq P}q_C(D)=\mu_w(K_E(P))\qquad(w\in C).
\]
For each positive-mass target cell that is **not** contained in \(P\), choose one excluded point \(s(D)\in D\setminus P\); in each fully contained positive-mass cell choose any point. By (S), a world \(v\in C\) realizes the corresponding selector distribution. That measure gives \(\mu_v(P)=\sum_{D\subseteq P}q_C(D)\). Combining the lower bound and this attaining row proves (i).

**Sharp cardinal bound.** Distinct selectors on \(\mathcal J_C\) yield different probability vectors because all \(q_C(D)>0\). Condition (S) requires every one to occur as some \(\mu_v\), and therefore requires at least \(\prod_{D\in\mathcal J_C}|D|\) distinct worlds in \(C\). For a sharp, genuinely multi-block example, let \(W\) have three epistemic classes \(C=\{0,1,2,3\}\), \(D=\{4,5\}\), and \(H=\{6,7\}\). Give the four worlds of \(C\) the four measures
\[
\tfrac12\delta_d+\tfrac12\delta_h,\qquad (d,h)\in D\times H.
\]
At worlds in \(D\cup H\), take their respective point masses. Conditions (M) and (S) hold in each class. For source class \(C\), the exact bound is \(|C|=2\cdot 2=4\). The same argument realizes equality whenever the target classes and source cardinality permit assigning all joint selectors to distinct source worlds; extra source worlds may repeat any admissible measure.

**Epistemic-support corollary.** If every \(\mu_w\) is supported on its **own** information cell \([w]_E\), then condition (M) holds with \(q_C(C)=1\) and all other block masses zero. The theorem reduces to: in each cell \(C\), the measures \(\{\mu_v:v\in C\}\) must be exactly the point masses \(\{\delta_z:z\in C\}\), each once. Thus each information cell implements a permutation of deterministic beliefs. This is a corollary under an additional support assumption, not the unrestricted theorem.

## Verification

The standalone file `verify_commutation.py` uses only Python's standard library. It independently enumerates all equivalence partitions on sets of up to three worlds and all worlds' probability distributions with half-integer masses, comparing both sides of the numerical modal identity on **every** Boolean event with the independent (M)+(S) characterization. It compares 1,099 finite partition/measure instances without a discrepancy. It separately evaluates the eight-world sharp example with two independently selected target classes. Run `python3 verify_commutation.py`. These finite enumerations corroborate the proof; they do not establish its universal quantifiers.

## Relationship to prior work

Kozhemiachenko and Sedlár (2026) introduce the two-layer probability/action/knowledge semantics used to formulate both expressions; their definitions permit arbitrarily varying subjective probability measures at different worlds, and their examples include probabilities of knowledge and lower subjective probabilities. Their main results address syntax, expressive ability, and computational complexity rather than this exact universal commutation characterization.

Belief functions as lower envelopes of compatible probability measures and representation by extreme selections are established in imprecise-probability theory (Halpern; related lower-prevision literature). The present claim does **not** introduce these general tools. It identifies their exact simultaneous-realization requirement within a **finite S5 epistemic class** and proves a sharp world-budget obstruction for universal equality of two differently nested modal-probabilistic constructions. Existing general belief-function representation theorems supply context but were not located as a statement of the classwise equivalence, sharp source-world bound, and deterministic-belief corollary together.

## Limitations

The theorem concerns finite world sets, an S5 knowledge relation, probability measures defined on all subsets, and all Boolean event valuations. It does not cover arbitrary measurable spaces without additional measurable-selection assumptions, or arbitrary modal expressions for which the inner probability operation is syntactically undefined. It describes equality of the **two displayed expressions** for any event, not a general commutation result for every epistemic and probabilistic operator. The novelty comparison is limited by possible equivalent results in earlier imprecise-probability or epistemic-probability literature. Independent audit has not been performed.

## References

1. D. Kozhemiachenko and I. Sedlár, *Reasoning About Probabilities, Actions, and Knowledge in Fuzzy Modal Logic*, arXiv:2604.22459v1, first posted April 24, 2026. https://arxiv.org/html/2604.22459v1
2. J. Y. Halpern, *Belief functions and lower envelopes*, accessible background manuscript. https://www.cs.cornell.edu/info/people/halpern/papers/DS_update1.pdf
3. F. G. Cozman, *Lower Envelopes* (background on lower probabilities and coherent credal sets). https://www.cs.cmu.edu/afs/cs/user/fgcozman/www/QuasiBayesianInformation/Old/BriefIntroduction/BriefIntroduction/node6.html
