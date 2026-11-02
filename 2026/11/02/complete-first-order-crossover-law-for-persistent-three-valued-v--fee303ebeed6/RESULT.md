# Complete first-order crossover law for persistent three-valued valuations on two-level frames

## Finding

Let \(K_{a,b}\) be the ordinal sum of an antichain of \(a\) minimal worlds and an antichain of \(b\) maximal worlds, where \(a,b\ge1\). Uniformly choose a one-atom, persistent and glut-free bilateral valuation: every world receives exactly one of the three statuses \(\mathrm N\) (neither true nor false), \(\mathrm T\) (true only), or \(\mathrm F\) (false only), and signed information cannot be lost along the world order. View each valuation as a first-order structure in the signature consisting of the world order and unary predicates for positive and negative atomic truth.

The number of admissible valuations and the probability of a nonneutral minimal world are exactly
\[
 Z_{a,b}=3^b+2(2^a-1),\qquad w_{a,b}=\frac{2(2^a-1)}{3^b+2(2^a-1)}.
\]
For every first-order sentence \(\varphi\), there exist binary values \(\epsilon_0,\epsilon_{\mathrm T},\epsilon_{\mathrm F}\in\{0,1\}\), determined solely by \(\varphi\), such that whenever \(a,b\to\infty\),
\[
 \Pr_{a,b}(\varphi)=(1-w_{a,b})\epsilon_0+
 \frac{w_{a,b}}2(\epsilon_{\mathrm T}+\epsilon_{\mathrm F})+o(1).
\]
Consequently the sequence of random first-order structures satisfies a first-order convergence law if and only if \(w_{a,b}\) converges, equivalently if and only if \(a-(\log_2 3)b\) converges in the extended real line. If \(w_{a,b}\to w\in[0,1]\), the **exact** spectrum of limiting first-order sentence probabilities is
\[
 \mathcal S(w)=\left\{(1-w)i+\frac w2(j+k):i,j,k\in\{0,1\}\right\}.
\]
If \(b=n\) and \(a=\lfloor n\log_2 3\rfloor\), the cluster set of the probability of a nonneutral minimal world is the entire interval \([1/2,2/3]\), and the only first-order sentences possessing limits along this critical sequence have limits \(0\) or \(1\).

## Assumptions and scope

The underlying frame has \(a\) labelled minimal worlds and \(b\) labelled maximal worlds, with every minimal world below every maximal world and no other strict comparisons. The random choice is uniform **over admissible complete one-atom valuations**, not over arbitrary colorings and not over frames. Positive and negative atomic truth are represented by unary first-order predicates \(T(x)\) and \(F(x)\); the order \(x\le y\) is another first-order relation. Glut freedom is \(\neg(T(x)\land F(x))\), and persistence requires that \(T(x)\Rightarrow T(y)\) and \(F(x)\Rightarrow F(y)\) whenever \(x\le y\). No independence between the states of different worlds is assumed before conditioning on a phase. Both level sizes tend to infinity in every asymptotic assertion. The formula \(\varphi\) is fixed as they grow, with no growing quantifier rank or additional variables outside the stated signature.

## Proof

**1. Exact phase decomposition.** If every minimal world is neutral, each maximal world can independently have any of the three statuses, providing \(3^b\) valuations (phase \(0\)). If some minimal world is \(\mathrm T\), persistence makes every maximal world \(\mathrm T\). A minimal world cannot then have status \(\mathrm F\), since every maximal world lies above it and gluts are forbidden. Every minimal world is instead freely \(\mathrm N\) or \(\mathrm T\), with at least one \(\mathrm T\), providing \(2^a-1\) valuations (phase \(+\)). The symmetric case provides \(2^a-1\) valuations (phase \(-\)). The cases are exclusive and exhaustive. The phase weights are \(1-w_{a,b},w_{a,b}/2,w_{a,b}/2\), respectively.

**2. Conditional typicality.** Fix any positive integer \(q\). In phase \(0\), every minimal world has status \(\mathrm N\), while the maximal statuses are independent uniform choices from \(\{\mathrm N,\mathrm T,\mathrm F\}\). As \(b\to\infty\), each of these three maximal status classes has at least \(q\) representatives with probability tending to one, by binomial concentration (or an elementary union bound). Phase \(+\) has every maximal world \(\mathrm T\); its minimal worlds are independent equiprobable choices from \(\{\mathrm N,\mathrm T\}\) conditioned on at least one \(\mathrm T\). Conditioning changes the probability of a fixed event by at most a quantity tending to zero, since the excluded all-\(\mathrm N\) event has probability \(2^{-a}\). Hence both minimal status classes have at least \(q\) representatives with probability tending to one. Phase \(-\) is symmetric. In all cases the deterministic one-status level has at least \(q\) worlds as its level size tends to infinity.

**3. First-order normal form.** Construct three countable reference structures \(M_0,M_+,M_-\), each the ordinal sum of two countably infinite antichains. In \(M_0\), all minimal worlds have status \(\mathrm N\), and maximal worlds have infinitely many of each status \(\mathrm N,\mathrm T,\mathrm F\). In \(M_+\), the minimal worlds have infinitely many of statuses \(\mathrm N,\mathrm T\), and all maximal worlds have status \(\mathrm T\). In \(M_-\), replace \(\mathrm T\) with \(\mathrm F\). Within each reference structure, the world-order relation and signed predicates depend only on the six possible rank/status combinations. If a finite sampled model has at least \(q\) representatives of every rank/status combination present in its reference structure and none of any other, Duplicator wins the \(q\)-round Ehrenfeucht–Fraïssé game between the finite and countable structures: at each round she selects a fresh point of the same rank and status as Spoiler's point, or the previously matched point if it is repeated. Equalities, the entire ordinal-sum order, and unary predicates are preserved. Thus every first-order sentence of quantifier rank at most \(q\) has the same truth value in the two structures. Set \(\epsilon_s(\varphi)=1\) exactly when \(M_s\models\varphi\). Conditional typicality yields the stated formula with an error tending to zero uniformly over the three phases; it is independent of the path along which \(a,b\to\infty\).

**4. Crossover and its converse.** Put \(d_{a,b}=a-(\log_2 3)b\). Directly,
\[
 w_{a,b}=\frac{2^{d_{a,b}+1}(1-2^{-a})}{1+2^{d_{a,b}+1}(1-2^{-a})}.
\]
As \(a\to\infty\), the factor \(1-2^{-a}\to1\). The strictly increasing homeomorphism from the extended real line to \([0,1]\), given on finite arguments by \(W(t)=2^{t+1}/(1+2^{t+1})\), shows that \(w_{a,b}\) converges if and only if \(d_{a,b}\) has an extended-real limit. In that case step 3 gives a limit for every sentence. Conversely, the sentence asserting \(\exists x\,[\operatorname{Min}(x)\land(T(x)\lor F(x))]\), where \(\operatorname{Min}(x)\) abbreviates \(\forall y\,(y\le x\Rightarrow x\le y)\), has probability **exactly** \(w_{a,b}\) by step 1. A first-order convergence law therefore forces convergence of \(w_{a,b}\).

**5. Exact spectrum.** Let \(E_0,E_+,E_-\) be the first-order sentences saying respectively that no minimal world is signed, that some minimal world is positively signed, and that some minimal world is negatively signed. Glut freedom, persistence and the complete two-level comparison imply that precisely one of these sentences holds in every admissible model. Their reference-structure truth values form the three standard basis vectors. Every subset of the three phases is selected by a disjunction of some of these sentences (the empty selection by a contradiction). Its limiting probability is the corresponding subset sum of \(1-w,w/2,w/2\). Conversely, step 3 expresses every possible first-order limit as precisely such a subset sum. This proves \(\mathcal S(w)\) without assuming its elements are distinct.

**6. Dense critical cluster set.** Let \(\alpha=\log_2 3\), which is irrational: a rational equality \(\alpha=p/q\) with positive integers would imply \(2^p=3^q\), impossible by unique factorization. For \(a_n=\lfloor n\alpha\rfloor\), \(b_n=n\), we have \(d_n=-\{n\alpha\}\). Fractional parts of successive multiples of an irrational number are dense in \([0,1]\); this classical density statement follows from the pigeonhole/irrational rotation argument. Hence the closure of the limiting values of \(d_n\) is \([-1,0]\), and continuity of \(W\) gives the full cluster interval \(W([-1,0])=[1/2,2/3]\). A sentence's phase-profile probability is affine in \(w\). To converge when \(w\) has this nondegenerate cluster interval, its affine coefficient must vanish, i.e. \(\epsilon_0=(\epsilon_{\mathrm T}+\epsilon_{\mathrm F})/2\). All three coefficients are binary, so this equality forces all three to be \(0\) or all three to be \(1\). The resulting sentence limits are exactly \(0\) or \(1\), and such limits are attained by a contradiction and a tautology.

## Verification

The accompanying standalone `checker.py` enumerates all assignments on the labelled two-level frames for \(1\le a,b\le5\), independently checks glut freedom and persistence, and verifies the three phase counts and exact formula for \(w_{a,b}\). It also checks the critical scaling identity numerically for selected large parameters. The executed output was `ALL_CHECKS_OK size_pairs=25 admissible_models=2385 scales=4`. The enumerations test finite cases only: the general first-order limit classification is proved by conditional concentration and the Ehrenfeucht–Fraïssé argument above, not inferred from a finite dataset.

## Relationship to prior work

Sedlár and Vigiani (2026) provide the relevant generalized Nelson semantics: bilateral persistence, with the glut-free \(\mathbf N_1\) case. This work **takes those semantics as a premise** and studies a different question: the full first-order asymptotic law of random, uniformly conditioned one-atom valuations on complete two-level frames. Koponen (2026) analyzes general conditions on finite-model properties and random expansions; its general conceptual context does not by itself give this concrete three-phase law. Counting isotone maps and order polynomials form additional background, but standard chain-target order-polynomial formulas do not immediately apply to the branching three-element information order or imply the probabilistic first-order spectrum. Closely related research on finite weak-order mapping counts and random finite-poset types concerns different source/target classes or invariants, not this law.

## Limitations

Only **one atomic proposition**, glut-free persistent three-valued valuations, complete two-level finite orders, and fixed first-order sentences in the signed atomic signature are treated. The conditioning is uniform over valid valuations; it is not the same distribution as independent world colors. There is no assertion for unrestricted Kripke frames, multiple atoms, gluts, formulas of growing quantifier rank, or the entire modal language under arbitrary random frames. The exact phase-count formula is elementary, but the value of the statement lies in the complete logical crossover and spectrum. No historical-priority guarantee is claimed: an equivalent law in earlier literature on random isotone maps or Nelson models may remain unindexed or inaccessible. Independent validation has not been performed.

## References

- I. Sedlár and P. Vigiani, *Modal Extensions of Generalised Nelson Logics*, arXiv:2610.10008v1 (first posted October 7, 2026), https://arxiv.org/abs/2610.10008 . Definitions of bilateral persistence and the glut-free \(\mathbf N_1\) case.
- V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first posted October 12, 2026), https://arxiv.org/abs/2610.16163 . General context concerning limits of random first-order expansions.
- A. Ehrenfeucht, *An application of games to the completeness problem for formalized theories*, Fundamenta Mathematicae **49** (1961), 129–141. Classical finite-rank back-and-forth method.
