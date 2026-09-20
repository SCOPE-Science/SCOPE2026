# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The counterexample uses exactly the objects defined in the source. The grammar
\[
A_1\to A_2A_3,\quad A_2\to x_1,\quad A_3\to x_1'
\]
is in Chomsky normal form and all three nonterminals are essential. For the free group on the paired generators, its language is the singleton \(\{x_1x_1'\}\), which is contained in the group word problem.

Definition 3.1 makes the first coordinate of \(U\) a word of the free monoid \(\Sigma^*\), so \(\langle x_1x_1',e\rangle\) is distinct from \(1_U=\langle\varepsilon,e\rangle\). Definition 3.2 gives the four arcs used in the proof. Substitution into the published Floyd--Warshall-type recurrence gives
\[
\langle x_1,A_3\rangle\in g^2_{14},\qquad
\langle x_1',A_3'\rangle\in g^3_{44},
\]
and therefore
\[
\langle x_1x_1',e\rangle\in g^4_{14}.
\]
Thus the line-7 predicate is true and Algorithm 4.4 returns `False`, while the inclusion is true.

Potential failure modes were checked explicitly: the ordering is \(A_1,A_2,A_3,Z\) exactly as Section 4 prescribes; \(A_3A_3'=e\) is one of the defining relations of \(T\); the terminal inverse relation belongs to the group \(G\), not to the free-monoid first coordinate of \(U\); and the algorithm performs the line-7 check only after all four closure stages. The standalone verifier reproduces the exact set recurrence and obtains a final \(g^4_{14}\) of cardinality two, including the derivation label.

The conceptual diagnosis is also consistent with the source text: Theorem 2.1 gives \(W_1\subseteq L(G)\), whereas condition (ii) of Theorem 4.3 is written as \(W_1=\{\varepsilon\}\). The counterexample exploits precisely the distinction between a nonempty word equal to the group identity and the literal empty word.

## Originality

**PASS, to the best of our knowledge.** The primary Filomat article and its arXiv posting were inspected through Definitions 3.1--3.2, the \(K^k\) recurrence, Theorem 4.3, Algorithm 4.4, Theorem 4.5, Corollary 4.6, and Remark 4.7. Searches by exact title, DOI `10.2298/FIL2412157Y`, arXiv identifier `2602.18305`, “Theorem 4.3”, “Algorithm 4.4”, “counterexample”, “error”, and equivalent context-free/group-language terminology found the source and mirrors but no correction or prior counterexample.

No earlier SCOPE record was found under Anisimov, Yordzhev, the theorem/algorithm numbers, or the semiring/group-language terminology.

The observation is elementary once the two notions of equality are compared, so independent prior discovery is plausible even though no indexed source was located. The originality claim is therefore restricted to the explicit counterexample and diagnosis, and is not a guarantee of first discovery.

## Value

**PASS.** The example has only three nonterminals and uses a free group with an elementary decidable word problem. It therefore gives a minimal-scale, directly checkable false negative for the central correctness theorem behind the proposed general context-free inclusion algorithm. It also identifies the exact algebraic mismatch that a repair must address. This materially changes how the paper's algorithmic claim should be interpreted while leaving open the possibility of a corrected construction.

## Access and residual uncertainty

The journal article and the arXiv full text were accessible, and the relevant definitions, recurrence, theorem, pseudocode, complexity statement, and final remark were inspected. No specific inaccessible paper was identified as especially likely to contain this exact counterexample.

A later erratum, informal communication, or poorly indexed note could have noticed the same issue without appearing in the searches performed. No independent validation is asserted.
