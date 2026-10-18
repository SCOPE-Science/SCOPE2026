# Sharp birthday window for bisimulation-minimal random finite S5 models

## Finding
Let an equivalence relation on \(n\) labelled worlds be chosen uniformly from all \(B_n\) equivalence relations, and then independently color each world uniformly from a palette of \(q_n\) atomic valuation types. The resulting one-agent \(\mathsf{S5}\) Kripke model is *bisimulation-minimal* when no two distinct worlds are bisimilar. Let \(X_n\) count unordered same-color pairs belonging to the same equivalence class. With \(\alpha_n\) defined by \(\alpha_n e^{\alpha_n}=n\), the sharp threshold is \(q_n\asymp n\alpha_n\sim n\log n\). More precisely:

\[
\frac{q_n}{n\log n}\longrightarrow\theta\in(0,\infty)
\quad\Longrightarrow\quad
X_n\xrightarrow{d}\operatorname{Poisson}\left(\frac{1}{2\theta}\right),\qquad
\Pr(\text{bisimulation-minimal})\longrightarrow e^{-1/(2\theta)}.
\]

If the ratio tends to zero, the minimality probability tends to zero; if it tends to infinity, the probability tends to one. The statement applies to arbitrary positive integer palettes and, in particular, to \(q_n=2^{p_n}\) uniformly sampled valuations of \(p_n\) propositional atoms. The discrete powers-of-two restriction is respected: a finite-window limit is asserted only along sequences for which the displayed ratio converges.

For every finite \(n,q\ge1\), the exact number of bisimulation-minimal labelled models is
\[
 n!\,[z^n]\prod_{j=1}^{\min(n,q)}(1+z^j)^{\binom qj}.
\]
The exact finite hypergraph counting form is classical; the asserted new result is the probabilistic bisimulation threshold and its Poisson window.

## Assumptions and scope
An \(\mathsf{S5}\) model has carrier \([n]\), a reflexive, symmetric, transitive accessibility relation \(E\), and one of \(q\) fully distinguishable propositional colors on each world. All \(B_n\) partitions are equiprobable; colors of distinct worlds are independent and uniform, independent of \(E\). Bisimulation is standard atom-respecting back-and-forth bisimulation *within the entire model*, not graph isomorphism or equality of partitions. The logarithm is natural. All limits are as \(n\to\infty\).

## Proof
**1. Exact bisimulation criterion.** Let \(C_E(w)\) be the \(E\)-class of \(w\), and let \(S(C)\) be its set of colors. The relation identifying two worlds precisely when their own colors agree and \(S(C_E(w))\) agrees is a bisimulation: each possible successor color is witnessed in both equivalence classes. Conversely, bisimilar worlds have equal colors by atomic harmony; the back-and-forth clauses force equality of successor-color sets. Thus two worlds are bisimilar precisely when the two pairs \((\text{color}(w),S(C_E(w)))\) are equal. Therefore minimality is equivalent to (i) no repeated color within a class and (ii) distinct classes carrying distinct color sets.

**2. Exact labelled count.** Under (i)–(ii), the collection of equivalence classes is represented uniquely by a finite set of pairwise distinct nonempty subsets of \([q]\), with total subset size \(n\). Choosing such a collection contributes the coefficient of \(z^n\) in \(\prod_{j=1}^q(1+z^j)^{\binom qj}\). For each choice, assigning the \(n\) distinct world labels bijectively to its \(n\) distinct color occurrences gives \(n!\) models. This is the same elementary generating mechanism used for simple hypergraphs; it is not claimed as a novel independent enumeration theorem.

**3. Pair statistics of the uniform set partition.** Write \(B_m\) for the \(m\)-th Bell number and \(r_j=B_{n-j}/B_n\). A fixed collection of \(j\) independent equivalences among world labels has probability \(r_j\), because contracting the corresponding vertices leaves a partition of \(n-j\) objects. Standard Bell-number saddle-point asymptotics (equivalently, the concentrated Dobinski representation) yield, for each fixed \(j\),
\[
 r_j\sim\left(\frac{\alpha_n}{n}\right)^j,
 \qquad \alpha_n e^{\alpha_n}=n,\qquad \alpha_n\sim\log n.
\]
For a partition \(\pi\), let \(T(\pi)=\sum_{C\in\pi}\binom{|C|}{2}\) count unordered within-class pairs, and let \(H(\pi)=\sum_{C\in\pi}\binom{|C|}{3}\). Then
\[
 \mathbb ET=\binom n2r_1\sim\tfrac12n\alpha_n,
 \qquad\mathbb EH=\binom n3r_2=O(n\alpha_n^2).
\]
Two *distinct* within-class pair constraints always impose two independent vertex identifications, whether the pairs meet or not. Hence
\[
 \mathbb E[T(T-1)]
 =\binom n2\left(\binom n2-1\right)r_2,
 \qquad \frac{T}{n\alpha_n}\xrightarrow{\mathbb P}\frac12,
\]
where the last conclusion follows from \(r_2/r_1^2\to1\) and the second-moment method. In particular, \(T/(n\log n)\to1/2\) in probability.

**4. Poisson law inside classes.** Conditional on \(\pi\), put \(I_{uv}=\mathbf1\{\text{color}(u)=\text{color}(v)\}\) for each within-class unordered pair \(uv\). Then \(X_n=\sum I_{uv}\), each indicator has probability \(1/q_n\), and indicators attached to disjoint pairs are independent. A dependency-graph Poisson bound using intersecting edge pairs gives, with an absolute constant \(K\),
\[
 d_{\rm TV}\!\left(\mathcal L(X_n\mid\pi),
 \operatorname{Poisson}(T(\pi)/q_n)\right)
 \le K\frac{T(\pi)+H(\pi)}{q_n^2}.
\]
Indeed each pair has at most \(2(|C|-2)\) neighbors in its class, and the joint probability of two distinct intersecting pair indicators is \(q_n^{-2}\). The expectation of this total-variation bound tends to zero when \(q_n/(n\log n)\to\theta\in(0,\infty)\), since the numerator has expectation \(O(n\log^2 n)\). The random Poisson mean \(T/q_n\) converges in probability to \(1/(2\theta)\); mixing gives the asserted limiting Poisson distribution.

**5. Distinct-class coincidence is negligible in the window.** Write \(N_1\) for the number of singleton partition classes. Exactly
\[
 \mathbb E[N_1(N_1-1)]=n(n-1)r_2=O(\log^2 n).
\]
Condition on \(\pi\) and require no within-class color collision. Two distinct classes having identical color sets must have the same size \(a\). Singleton-pair coincidence has probability \(1/q_n\). For \(a\ge2\), the probability that two prescribed disjoint classes both have distinct internal colors and equal sets is at most \(1/\binom{q_n}{a}\), hence at most \(1/\binom{q_n}{2}\) once \(q_n\ge2n\). Since there are at most \(n^2\) ordered class pairs, a union bound gives
\[
 \Pr(\exists\text{ two distinct classes with equal color sets},X_n=0)
 \le\frac{\mathbb E[N_1(N_1-1)]}{2q_n}
      +\frac{n^2}{\binom{q_n}{2}}=o(1)
\]
for \(q_n\asymp n\log n\). The finite minimality probability therefore differs from \(\Pr(X_n=0)\) by \(o(1)\), giving the limiting \(e^{-1/(2\theta)}\).

**6. Both sides of the threshold.** If \(q_n/(n\log n)\to\infty\), \(\Pr(X_n>0)\le \mathbb ET/q_n\to0\); the distinct-class coincidence bound in Step 5 also vanishes, proving minimality with probability tending to one. If \(q_n/(n\log n)\to0\), conditional on any \(\pi\) the distinct-edge collision indicators are *pairwise independent*, including for overlapping pairs, so
\[
 \operatorname{Var}(X_n\mid\pi)
 =T(\pi)\frac1{q_n}\left(1-\frac1{q_n}\right).
\]
Chebyshev therefore yields \(\Pr(X_n=0\mid\pi)\le q_n/T(\pi)\) when \(T(\pi)>0\) (the case \(q_n=1\) is also immediate). Since \(T/(n\log n)\to1/2\), the right side tends to zero in probability, and bounded convergence gives \(\Pr(X_n=0)\to0\). Minimality implies \(X_n=0\), proving the subcritical conclusion.

## Verification
The bundled `verify_s5.py` independently enumerates all set partitions and valuations for \(1\le n\le5\), \(1\le q\le4\). On each model it performs iterative atom-respecting modal partition refinement, then compares the observed count of bisimulation-minimal models with the coefficient formula calculated by an unrelated generating-polynomial dynamic program. All twenty instances match (`VERIFY_OK 20 independent partition-refinement/coefficient comparisons`). These computations check the finite classification, not the infinite Poisson limit; that limit is proved by Steps 3–6.

## Relationship to prior work
Sliusarev (2024) studies uniform \(\mathsf{S5}\) **frames** and almost-sure modal *validity*; it does not count bisimulation-minimal random-valued models or identify a growing-palette critical window. Earlier work by Halpern and Kapron on modal zero-one laws addresses finite propositional vocabularies and asymptotic formula validity rather than this random quotient statistic. Chern, Diaconis, Kane and Rhoades supply probabilistic tools and Bell/set-partition asymptotics. Klazar's enumeration of simple hypergraphs covers the elementary finite product coefficient, which is used here as a known counting representation, not passed off as novel. The structural and probabilistic combination—Bell partition sampling, color-sensitive bisimulation, and the Poisson threshold at \(n\log n\)—is the present contribution.

## Limitations
The theorem is only for one-agent equivalence accessibility, uniform set partitions, and independent equiprobable valuation types. It does not establish a corresponding threshold for multi-agent models, nonuniform partitions, correlated atoms, modal formula validity, or non-equivalence frames. A closely equivalent formulation in unsurveyed literature remains possible; novelty is not an independent certification. The numerical verifier covers finite parameter cases only.

## References
- V. Sliusarev, *Modal logics of almost sure validities in some classes of euclidean and transitive frames*, arXiv:2406.10770 (first posted 2024-06-16), especially the \(\mathsf{S5}\) frame section. https://arxiv.org/abs/2406.10770
- J. Y. Halpern and B. M. Kapron, *Zero-one laws for modal logic* (1994). https://www.cs.cornell.edu/info/people/halpern/papers/0-1law_modal_logic.pdf
- P. Chern, P. Diaconis, D. Kane, and R. Rhoades, *Central Limit Theorems for some Set Partition Statistics*, arXiv:1502.00938 (2015). https://arxiv.org/abs/1502.00938
- M. Klazar, *Extremal problems for ordered hypergraphs: small patterns and some enumeration*, arXiv:math/0305048 (2003), Section 4. https://arxiv.org/abs/math/0305048
