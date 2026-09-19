# Neutral-letter constant-circuit membership is NL-complete for arbitrary DFAs

## Statement

Let \(\mathcal A=(Q,\Sigma,\delta,q_0,F)\) be a complete deterministic finite automaton, and suppose that a distinguished letter \(\#\in\Sigma\) acts as the identity on every state:

\[
\delta(q,\#)=q\qquad(q\in Q).
\]

Thus \(\#\) is a neutral letter of \(L(\mathcal A)\). Consider the decision problem

\[
\textsc{Neutral-DFA-Constant-Circuit}:
\quad
\text{is }\operatorname c(L(\mathcal A))\in O(1)?
\]

for the unbounded-fan-in circuit measure of Göller--Manuel.

**Theorem.** The problem is \(\mathbf{NL}\)-complete under logspace many-one reductions. Hardness already holds for the fixed alphabet

\[
\Sigma=\{0,1,\#\}
\]

with \(\#\) an identity transition at every state.

Equivalently, recognizing an alphabetic language from an arbitrary deterministic presentation is \(\mathbf{NL}\)-complete, even over a fixed ternary alphabet with a syntactic neutral letter.

The result complements two known endpoints. For a **minimal** DFA, recognition of 1-piecewise-testable/alphabetic languages is in \(\mathrm{AC}^0\). For NFAs, Göller--Manuel prove \(\mathbf{PSPACE}\)-completeness of constant-circuit membership, and their hardness construction itself adds a fresh letter as a self-loop at every NFA state. Thus the neutral-letter case exhibits a sharp representation-sensitive progression from minimal deterministic presentations, through arbitrary deterministic presentations, to nondeterministic presentations.

## Why constant circuit complexity becomes alphabeticity

Göller--Manuel prove that for every regular neutral-letter language \(L\subseteq\Sigma^+\), the following are equivalent:

1. \(\operatorname c(L)\in O(1)\);
2. \(L\) is idempotent and commutative;
3. membership depends only on the set of letters occurring in the word;
4. \(L\) is a finite Boolean combination of support languages.

Call the third property **alphabeticity**. Since the distinguished letter \(\#\) acts identically on every state of \(\mathcal A\), it is neutral, so the circuit-complexity decision problem above is exactly alphabeticity recognition on this input class.

## A right-congruence criterion that avoids minimization

For states \(p,r\in Q\), write

\[
p\equiv_R r
\]

when they accept the same set of suffixes, i.e. when their right languages are equal. Only reachable states matter.

**Lemma.** \(L(\mathcal A)\) is alphabetic if and only if, for every reachable \(q\in Q\) and all letters \(a,b\in\Sigma\),

\[
\delta(q,a)\equiv_R\delta(q,aa)
\tag{1}
\]

and

\[
\delta(q,ab)\equiv_R\delta(q,ba).
\tag{2}
\]

Here \(\delta(q,w)\) denotes the usual extension of the transition function to words.

**Proof.** If the language is alphabetic, replacing \(a\) by \(aa\), or swapping adjacent letters \(a,b\), preserves the support of every surrounding word, so (1) and (2) hold in every reachable context.

Conversely, (1) says that insertion/deletion of a duplicate adjacent letter preserves membership in every context, and (2) says that swapping adjacent letters preserves membership in every context. These local rewrites generate the free semilattice congruence: any two words with the same support can be sorted by adjacent swaps and then reduced to the same duplicate-free canonical word. Hence membership depends only on support. ∎

The point is that the raw transition equalities
\(\delta(q,a)=\delta(q,aa)\) and \(\delta(q,ab)=\delta(q,ba)\) need not hold in a nonminimal DFA. They need only hold modulo right-language equivalence. This is precisely where arbitrary presentations differ from minimal DFAs.

## NL upper bound

It is enough to recognize non-alphabeticity in \(\mathbf{NL}\). A certificate consists of:

- a reachable state \(q\);
- letters \(a,b\);
- one of the two candidate pairs
  \[
  (\delta(q,a),\delta(q,aa))
  \quad\text{or}\quad
  (\delta(q,ab),\delta(q,ba));
  \]
- a suffix distinguishing the two states.

Reachability of \(q\) can be witnessed by a simple path of length less than \(|Q|\). If two states are right-language-distinguishable, then in the product automaton \(Q\times Q\) there is a simple path of length less than \(|Q|^2\) to a pair with exactly one accepting component. A nondeterministic machine can guess both paths symbol by symbol while storing only the current state(s) and counters, using \(O(\log |Q|)\) work space.

Therefore non-alphabeticity is in \(\mathbf{NL}\), alphabeticity is in \(\mathbf{coNL}\), and the Immerman--Szelepcsényi theorem \(\mathbf{NL}=\mathbf{coNL}\) yields

\[
\textsc{Neutral-DFA-Constant-Circuit}\in\mathbf{NL}.
\]

This argument does not require constructing the minimal DFA.

## NL hardness over a fixed ternary alphabet

Use directed \(s\)-to-\(t\) reachability on graphs of outdegree at most two; this restriction remains \(\mathbf{NL}\)-complete. By \(\mathbf{NL}=\mathbf{coNL}\), its complement is also \(\mathbf{NL}\)-complete. Assume \(s\ne t\).

Given such a graph \(G=(V,E)\), assign the at most two outgoing edges of every vertex labels \(0\) and \(1\). Construct a complete DFA \(\mathcal A_G\) over \(\{0,1,\#\}\) with states

\[
V\cup\{\bot\},
\]

start state \(s\), and sole accepting state \(t\). For \(v\ne t\), a labelled edge is followed when present and a missing labelled edge goes to \(\bot\). Set

\[
\delta(t,0)=\delta(t,1)=\bot,
\qquad
\delta(\bot,0)=\delta(\bot,1)=\bot,
\]

and make \(\#\) an identity transition on every state:

\[
\delta(q,\#)=q.
\]

The construction is logspace computable.

If \(t\) is unreachable from \(s\), then

\[
L(\mathcal A_G)=\varnothing,
\]

which is alphabetic and has constant circuit complexity.

If \(t\) is reachable, choose a nonempty labelled word \(w\in\{0,1\}^+\) describing a path that reaches \(t\) for the first time at its end. Then

\[
w\in L(\mathcal A_G)
\]

but, because the first symbol of the second copy immediately sends \(t\) to \(\bot\),

\[
ww\notin L(\mathcal A_G).
\]

Yet \(w\) and \(ww\) contain exactly the same set of letters. Hence \(L(\mathcal A_G)\) is not alphabetic and therefore does not have constant circuit complexity.

Thus

\[
t\text{ unreachable from }s
\iff
\operatorname c(L(\mathcal A_G))\in O(1),
\]

which is a logspace reduction from the complement of bounded-outdegree reachability. This proves \(\mathbf{NL}\)-hardness and hence the theorem.

## Representation gap

The theorem isolates a complexity cost that is invisible at the level of the language itself.

For minimal DFAs, Masopust records the classical criterion that 1-piecewise testability is equivalent to the literal transition identities

\[
paa=pa,
\qquad
pab=pba,
\]

for every state and letters, and states that the test is in \(\mathrm{AC}^0\). In an arbitrary DFA these identities may fail inside a class of equivalent states, so one must determine whether the corresponding successor states have equal right languages. The theorem shows that this semantic quotienting cost is already exactly \(\mathbf{NL}\)-complete, even though the target language class is one of the simplest nontrivial regular-language varieties.

At the other end, the 2026 NFA result is \(\mathbf{PSPACE}\)-complete. Its hardness proof adds a fresh symbol \(\$\) as a self-loop on every state, so the hard instances also possess a syntactically explicit neutral letter. Consequently the deterministic/nondeterministic gap persists even after neutral-letter structure is supplied in the strongest possible automaton-level form.

## Verification

`artifacts/verify.py` performs two independent finite checks.

First, for every complete two-active-letter DFA with a fixed start state on one, two, or three states, and every accepting set, it compares the right-congruence criterion (1)--(2) with the criterion obtained after explicit DFA minimization. The two classifications agree on all 5,898 automata checked.

Second, it exhaustively checks the hardness construction for all labelled partial outdegree-two graphs on two and three vertices, all ordered distinct choices of \(s,t\), verifying that the constructed language is alphabetic exactly when \(t\) is unreachable. It checks 24,738 graph instances. The recorded output is in `artifacts/verification.txt`.

These finite checks are sanity tests; the theorem is proved by the arguments above.

## Relation to prior work and originality boundary

Göller and Manuel (2026) characterize neutral-letter regular languages of constant circuit complexity as exactly the alphabetic/idempotent-commutative languages, and prove \(\mathbf{PSPACE}\)-completeness when a regular language is presented by an NFA. Their paper does not state a deterministic-input complexity classification.

Masopust and Thomazo (2015) analyze \(k\)-piecewise testability for **minimal** DFAs. For \(k=1\) they give a deterministic-logspace upper bound based on the local idempotence and commutation identities. Masopust (2016) records the corresponding minimal-DFA test as lying in \(\mathrm{AC}^0\). These results do not cover arbitrary, nonminimal DFA presentations.

The new claim here is specifically the exact \(\mathbf{NL}\)-completeness of semantic alphabeticity/constant-circuit membership for arbitrary deterministic presentations carrying an identity neutral letter, with hardness over a fixed ternary alphabet, together with the resulting minimal-DFA / arbitrary-DFA / NFA representation comparison.

Targeted searches for “1-piecewise testability” with arbitrary or nonminimal DFAs, alphabetic-language DFA recognition, semilattice-language recognition, and \(\mathbf{NL}\)-hardness did not locate this classification. Because the proof is short once right-language equivalence is used, an unpublished folklore observation remains a material originality risk. The motivating circuit-complexity paper is also very recent, so near-simultaneous observation is possible.

## Limitations

The theorem assumes a syntactically explicit identity letter, so it does not classify constant-circuit membership for arbitrary DFAs without a neutral letter. It concerns recognition from an automaton presentation, not the circuit complexity of evaluating a fixed regular language. It does not improve the \(\mathbf{PSPACE}\) result for NFAs or the \(\mathrm{AC}^0\) upper bound for minimal DFAs. The originality claim is limited to the arbitrary-DFA complexity classification and the fixed-alphabet neutral-letter restriction.

## References

1. S. Göller and A. Manuel, *Rational Reductions and Regular Languages of Constant Circuit Complexity*, arXiv:2609.18484v1, 16 Sep 2026. https://arxiv.org/abs/2609.18484
2. T. Masopust and M. Thomazo, *On the Complexity of k-Piecewise Testability and the Depth of Automata*, DLT 2015, LNCS 9168, 364--376. https://doi.org/10.1007/978-3-319-21500-6_29
3. T. Masopust, *Piecewise Testable Languages and Nondeterministic Automata*, MFCS 2016 / arXiv:1603.00361. https://arxiv.org/abs/1603.00361
