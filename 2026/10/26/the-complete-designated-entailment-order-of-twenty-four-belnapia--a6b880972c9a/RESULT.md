# The complete designated-entailment order of twenty-four Belnapian essence and accident operators

## Finding
In the four-valued modal semantics of Petrukhin (2026), fix one formula \(A\) and consider the twenty-four essence, accident, negative-essence, and negative-accident operators formed with the four exact-status tests and the positive- and negative-evidence tests. Under designated-truth entailment over all nonempty universal-accessibility models, the twenty-four operators are pairwise nonequivalent. Their implication order has exactly forty strict comparisons, all of them covers, between twelve accident variants and twelve essence variants. There are no other strict comparisons.

For two test sets \(Q,R\) in \(\mathcal Q=\{\{t\},\{b\},\{n\},\{f\},\{t,b\},\{b,f\}\}\), the complete strict implications are exactly:

\[
\begin{aligned}
\bullet_Q A\models_D\circ_R A &\iff Q\cap R=\varnothing,\\
\bullet_Q A\models_D\widetilde\circ_R A &\iff Q\subseteq R,\\
\widetilde\bullet_Q A\models_D\circ_R A &\iff R\subseteq Q.
\end{aligned}
\]

Here \(\models_D\) means preservation of a designated truth value at every pointed model, and the other operator pairs are comparable only by identity. There are twenty, ten, and ten comparisons of these respective forms. Of the \(24^2=576\) ordered tests, twenty-four identities and forty strict comparisons hold; 512 fail. Every failure has a countermodel of at most three worlds. Exactly 144 invalid comparisons have a one-world counterexample, 340 first have a two-world counterexample, and 28 first have a three-world counterexample; the uniform three-world cutoff is sharp.

## Assumptions and scope
The truth values are \(V=\{t,b,n,f\}\) with designated values \(\{t,b\}\), where \(t\) means positive evidence only, \(f\) negative only, \(b\) both, and \(n\) neither. Modal frames are nonempty with universal accessibility (one \(\mathsf{S5}\) equivalence class). For any formula \(A\) at a pointed world \(w\), put \(a=v(A,w)\) and \(S=\{v(A,u):u\in W\}\). Necessarily \(a\in S\ne\varnothing\). The six query sets are the four exact truth statuses and the two evidence-status sets \(T=\{t,b\}\), \(F=\{b,f\}\). No syntactic expressibility, proof-theoretic derivability, or designated falsity preservation is asserted. Identical-argument entailments only are classified: both sides contain the *same* formula \(A\).

Write \(\circ_Q,\bullet_Q,\widetilde\circ_Q,\widetilde\bullet_Q\) for the four corresponding operations in the source's Definition 6. Their designated-truth clauses, in this notation, are:

\[
\begin{array}{ll}
\bullet_Q:\ a\in Q\ \wedge\ S\setminus Q\ne\varnothing,&
\circ_Q:\ \neg(a\in Q\ \wedge\ S\setminus Q\ne\varnothing),\\
\widetilde\bullet_Q:\ a\notin Q\ \wedge\ S\cap Q\ne\varnothing,&
\widetilde\circ_Q:\ \neg(a\notin Q\ \wedge\ S\cap Q\ne\varnothing).
\end{array}
\]

The theorem uses only these truth clauses and does not identify the two members of a bilateral truth-value pair. The test set subscripts are semantic indices, not newly defined object-language operators.

## Proof
**Support sufficiency and completeness.** The four displayed truth predicates depend only on \((a,S)\). Conversely, every pair with \(a\in S\subseteq V\) and \(S\ne\varnothing\) is realized by an atomic formula \(A=p\) on a pointed universal frame having \(|S|\) worlds, one for each status and the designated point carrying status \(a\). There are precisely \(\sum_{S\ne\varnothing}|S|=4\cdot2^3=32\) such profiles. Thus comparing the displayed predicates on all thirty-two profiles is sufficient and necessary for universal same-argument designated entailment, for arbitrarily nested inputs \(A\).

**Positive comparisons.** An implication from \(\bullet_Q\) to \(\circ_R\) fails exactly when both positive accidents hold: the local status must belong to \(Q\cap R\), and witnesses must lie outside each test set. Because every test set is a proper nonempty subset of \(V\), any chosen local element of their intersection admits the required witnesses. Hence this implication holds exactly when the intersection is empty. Similarly, \(\bullet_Q\not\models_D\widetilde\circ_R\) holds precisely if some local status lies in \(Q\setminus R\), together with an outside-\(Q\) and an inside-\(R\) witness. These exist whenever \(Q\setminus R\ne\varnothing\). The implication therefore holds exactly if \(Q\subseteq R\). Finally, \(\widetilde\bullet_Q\not\models_D\circ_R\) is possible precisely when the local status belongs to \(R\setminus Q\); suitable inside-\(Q\) and outside-\(R\) witnesses always exist. It follows that this implication holds exactly if \(R\subseteq Q\).

**Completeness and distinctness.** Every essence variant is designated true on a singleton model; every accident variant is not. Hence no essence entails any accident. For two different essences, and for two different accidents, the thirty-two-profile criterion gives a falsifying profile; the same holds for the one remaining direction from \(\widetilde\bullet_Q\) to \(\widetilde\circ_R\), and from \(\bullet_Q\) to \(\bullet_R\), and for all cross-variant cases not among the three displayed families. These exhaustive finite assertions can also be checked without appeal to a heuristic: `verify.py` constructs all profiles and tests each of the \(24^2\) directed comparisons against the three set-theoretic conditions. Every quantified profile occurs on a genuine finite model as shown above, so this is an exact finite decision, not a finite approximation to an infinite claim. The twenty-four distinct profile signatures prove pairwise nonequivalence. Direct enumeration of six test sets in the three criteria yields \(20+10+10=40\) valid strict comparisons. Since all strict implications go from an accident to an essence, no chain has more than one strict step and each strict implication is a cover.

**Small countermodels and sharpness.** For a failed implication, choose a falsifying pointed profile. Any truth/failure of the four operator predicates can require at most two different existential witnesses in addition to the local point, while the universal requirements remain true when worlds are removed. Thus every failure admits a pointed model of at most three worlds. All singleton frames designate the twelve essences and fail to designate the twelve accidents, producing 144 invalid implications first witnessed at size one. Exhaustive enumeration of assignments on one, two, and three labelled worlds using the source's original clauses yields the remaining first-witness histogram 340 and 28, with no missing comparisons. Sharpness is witnessed by \(\widetilde\bullet_{\{t\}}p\not\models_D\widetilde\circ_{\{b\}}p\) at a world where \(p=n\) and two further worlds have \(p=t\) and \(p=b\). It cannot be witnessed with fewer than three worlds: the local status must lie outside both disjoint singleton test sets, and the witnesses for \(t\) and \(b\) must be separate.

## Verification
`verify.py` uses two separately programmed evaluations of the designated clauses and enumerates the \(4^m\) valuations on \(m=1,2,3,4\) labelled worlds; it also enumerates the thirty-two pointed support profiles, all 576 implication pairs, and minimal countermodel sizes. Running `python3 verify.py` produced `BELNAP_24_IMPLICATIONS_OK 24 40 512 144 340 28`. The full semantic reduction above makes finite checking exhaustive for all nonempty universal frames and arbitrary formulas, rather than a finite-model-only observation. No independence or third-party verification is asserted.

## Relationship to prior work
Petrukhin, *Essence and Accident Modalities Meet Belnapian Truth Values* (2026), Definition 6, introduces the twenty-four indexed operators and proves specific relationships, reduction results and modal translation/decidability facts. The present result fixes a *common argument* in both operators and provides the complete designated-truth entailment order, together with the sharp witness-size distribution. Those claims are not supplied by the source's cited results on individual operator semantics or transformations of arguments. Fan, *Logics of Essence and Accident* (2015), studies corresponding classical two-valued modalities; the status-indexed four-valued family and its designated-entailment graph are different objects. This classification uses the established semantic clauses; it does not claim that the clauses themselves are new.

## Limitations
The classification concerns the designated truth coordinate only, a universal accessibility relation and a common formula argument. It does not extend unchanged to arbitrary Kripke frames, designated falsity or derivability. Counts of minimal countermodel orders rely on exhaustive finite enumeration with the attached checker; no independent audit has occurred. Priority relative to possible specialized publications not identified in the inspected material remains uncertain.

## References
1. Y. Petrukhin, *Essence and Accident Modalities Meet Belnapian Truth Values*, *Studia Logica* (2026), DOI: `10.1007/s11225-026-10250-z`; preprint arXiv:2610.08323. The first verified public version is dated 2026-07-15.
2. J. Fan, *Logics of Essence and Accident*, arXiv:1506.01872 (2015).
