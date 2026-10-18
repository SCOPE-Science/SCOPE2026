# A branching-spectrum dichotomy for modal valuation extension

## Finding
Fix any **nonempty finite** set \(S\subseteq\mathbb N\). An \(S\)-branching Kripke frame is a countable nonempty frame \(F=(W,R)\) such that the set \(R[w]=\{u\in W:wRu\}\) has cardinality in \(S\) for every world \(w\). Let \(\mathrm{VEL}(S)\) assert that every assignment of Boolean values to the propositional variables at the worlds of every such frame extends to a full truth valuation on all classical propositional modal formulas.

**Theorem (branching-spectrum classification).** Over \(\mathrm{RCA}_0\):

\[
\mathrm{VEL}(S)\ \begin{cases}
\text{is provable in }\mathrm{RCA}_0,&|S|=1,\\
\text{is equivalent to }\mathrm{ACA}_0,&|S|\ge2.
\end{cases}
\]

For \(X\)-computable instances, the unique full valuation is uniformly computable from \(X'\). For singleton \(S\), it is computable from \(X\) itself. These bounds are sharp: for every fixed \(S\) with at least two possible outdegrees and every \(X\), an explicit \(X\)-computable instance has a valuation computing \(X'\), with the reversal visible at modal depth one. In particular, the unique valuation for a corresponding computable instance has exactly the Turing degree of the ordinary halting set.

## Assumptions and scope
The modal language has countably many propositional letters, falsum, Boolean implication, and the unary normal modality \(\Box\). Negation abbreviates implication into falsum. Truth is Boolean: \(V(w,\Box\varphi)=1\) exactly when every successor of \(w\) makes \(\varphi\) true; this includes the vacuous case of no successors. All sets of worlds and accessibility relations are coded as sets of natural numbers, as in second-order arithmetic. No seriality, reflexivity, transitivity, finite-world assumption, or decidable successor enumeration is imposed beyond the indicated outdegree restriction. \(S\) is a fixed external *finite* subset of the standard natural numbers, not a variable infinite family. \(\mathrm{ACA}_0\) is arithmetic comprehension, equivalently closure under the Turing jump relative to each parameter set.

The contribution is the complete classification by the **allowed degree spectrum**, including sharp oracle bounds. Takeda's prior image-finite theorem and its degree-zero-or-one special construction are explicitly prior results, not claimed here as novel.

## Proof
**1. Effective upper bound.** Let an instance \(F=(W,R),v\) be computable in \(X\), and put \(K=\max S\). For each world \(w\), ask \(X'\), separately for each \(1\le j\le K\), whether there exist \(j\) pairwise distinct successors of \(w\). The question is \(\Sigma^0_1(X)\), so the answers give the **exact** outdegree \(d(w)\) in \(S\). An \(X\)-search then lists all \(d(w)\) distinct successors. Evaluating a formula recursively on its finite syntax tree, including calling this terminating successor-list procedure at each \(\Box\), computes the unique valuation from \(X'\). Uniqueness is structural induction on formulas. The recursion is uniform in the oracle and instance codes; it is not merely a bound on each fixed modal depth. The same procedure is formalizable in \(\mathrm{ACA}_0\), using comprehension to construct the set coding the total valuation.

If \(S=\{k\}\), the exact successor count \(k\) is known without consulting any jump. Searching for \(k\) distinct successors always terminates, and the assertion that these exhaust the row follows from the frame hypothesis. For \(k=0\), the list is empty. The entire syntactic evaluation is now computable directly in \(X\), and \(\mathrm{RCA}_0\)'s recursive comprehension constructs its graph. Therefore \(\mathrm{RCA}_0\vdash\mathrm{VEL}(\{k\})\) for every fixed \(k\).

**2. The padded halting gadget.** Assume \(|S|\ge2\). Fix \(k=\min S\) and any \(\ell\in S\) with \(\ell>k\); let \(d=\ell-k\). Given an arbitrary set \(X\), form a countably infinite frame with three disjoint kinds of worlds: a fixed set \(D\) of exactly \(k\) distinct worlds, testing worlds \(s_e\) for all Turing indices \(e\), and dummy worlds \(u_{e,t,j}\), where \(e,t\in\mathbb N\) and \(0\le j<d\). The frame's world set is independent of \(X\).

For every world \(w\), put \(wRa\) for each \(a\in D\). In addition, put

\[
s_e R u_{e,t,j}\quad\Longleftrightarrow\quad
\text{the oracle-}\!X\text{ computation }e\text{ first halts at exactly stage }t,
\quad 0\le j<d.
\]

There are no further edges. First-halting-at-a-given-stage is decidable by a bounded computation using \(X\), so the complete edge relation exists in \(\mathrm{RCA}_0\) relative to \(X\). Every dummy and base world has exactly \(k\) successors. Every test world has exactly \(k\) successors if the computation never halts, and exactly \(\ell\) if it does: a deterministic computation has at most one first-halting stage, producing precisely \(d\) extra edges. Therefore **every world has outdegree in \(\{k,\ell\}\subseteq S\)**, even when \(k=0\).

Make a distinguished atomic variable \(p\) true at every base world in \(D\) and at every testing world \(s_e\), and false at every dummy world. Other propositional variables can all be false. This assignment is independent of the halting set. Every base successor of \(s_e\) satisfies \(p\), while every potential extra dummy successor refutes \(p\). Consequently, for every correct total valuation \(V\),

\[
V(s_e,\neg\Box p)=1\quad\Longleftrightarrow\quad e\in X'.
\]

Taking the \(s_e\)-section of any full valuation by \(\Delta^0_1\) comprehension yields \(X'\). Since \(X\) was arbitrary, \(\mathrm{VEL}(S)\) implies closure under the relative Turing jump, equivalent over \(\mathrm{RCA}_0\) to \(\mathrm{ACA}_0\). The preceding upper bound gives the converse. For a computable instance choose \(X=\varnothing\); both Turing reductions apply, so its unique full valuation has degree exactly \(\mathbf 0'\).

## Verification
The proof was checked at the level of definitions, relative computability, arity counting, and the full range of parameters \(k\ge0\), \(\ell>k\): every row has exactly one of the two permitted degrees, and the modal test formula recognizes halting without higher modal nesting. The upper algorithm decides every finite row with a single jump oracle, then runs a finite computation on the formula tree. The lower argument constructs a set in \(\mathrm{RCA}_0\) from the resulting full valuation and yields arithmetic comprehension. No computer experiment is used as evidence of the universal theorem.

## Relationship to prior work
Yuto Takeda, *Frame definability in second-order arithmetic*, arXiv:2608.22822v1 (public August 24, 2026), Theorem 2.27, proves that the unrestricted image-finite valuation-extension principle is equivalent to \(\mathrm{ACA}_0\). Its lower-bound frame has **zero or one** successor per world; this exact special case of the lower argument here is already covered. The same work develops the general unbounded-frame, finite-depth, and computational-strength results. The present finding concerns **every finite set of permitted outdegrees**, including serial classes \(\{k,\ell\}\) with \(k\ge1\), and the sharp single-jump degree bound uniformly over these classes. The image-finite upper bound in the cited theorem does imply the present upper direction; it does not state or by itself yield the complete singleton/non-singleton lower-bound dichotomy. The earlier modal formalization of Shimomichi, Takeda and Yokoyama supplies background rather than this branching-spectrum classification.

## Limitations
The result is for classical Boolean propositional modal semantics, countable frames, and fixed finite outdegree sets \(S\). It does not address infinite allowed degree sets, nonnormal modalities, infinitary syntax, or unbounded image-infinite frames. The construction establishes an exact oracle complexity and reverse-mathematical equivalence, not an independent priority certification; historical results with a more general padding or finite-branching transfer theorem could imply part of it. The lower-bound case \(S=\{0,1\}\) belongs to prior work. No independent audit has been performed.

## References
1. Y. Takeda, *Frame definability in second-order arithmetic*, arXiv:2608.22822v1, August 24, 2026; particularly Section 2.1, Theorem 2.27, and its image-finite lower-bound argument. https://arxiv.org/abs/2608.22822
2. S. Shimomichi, Y. Takeda, K. Yokoyama, *Completeness theorems for modal logic in second-order arithmetic*, arXiv:2503.01191v1, March 3, 2025. https://arxiv.org/abs/2503.01191
3. S. G. Simpson, *Subsystems of Second Order Arithmetic*, 2nd ed., 2009, for the standard jump/comprehension equivalence.
