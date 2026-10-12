# Linear witness-star normalization for propositional FMT semantics

## Finding

Let \(\Gamma\) be any finite nonempty set of propositional formulas in the language with atoms, \(\bot\), conjunction, disjunction and implication. Let \(I(\Gamma)\) be the set of its **distinct syntactic implication subformulas**. Every rooted propositional Fitting–Marek–Truszczyński (FMT) model \(\mathcal M\), finite or infinite, has a rooted FMT model \(\mathcal M_\Gamma\) obtained by retaining at most
\[
1+|I(\Gamma)|
\]
original worlds, including the original root, which preserves the truth value of **every subformula of every member of \(\Gamma\)** at **every retained world**.

More strongly, \(\mathcal M_\Gamma\) can be put in a *witness-star normal form*: the root accesses every retained world for every formula-indexed relation; for each \(\theta\in I(\Gamma)\) there is at most one distinguished witness \(w_\theta\), and each nonroot \(\theta\)-accessibility row is either empty or the singleton \(\{w_\theta\}\). All other nonroot relation rows may be empty. A distinguished witness is needed exactly when the original root refutes \(\theta\).

Consequently, for every fixed finite set \(X\) of closed negative axioms of the kind considered by Kurahashi–Noguchi, the following root-satisfiability problem is **NP-complete**: given \(\varphi\), decide whether some FMT frame validating \(X\) has a valuation making \(\varphi\) true at its root. A positive instance has a witness-star model with at most \(1+|I(\{\varphi\}\cup X)|\) worlds. This is a semantic, designated-root satisfiability statement; it is not an assertion that the same complexity holds for arbitrary-world satisfiability or that derivability has a particular lower bound.

## Assumptions and scope

A propositional FMT frame is \(\mathcal F=(W,r,(R_\alpha)_{\alpha\in\mathrm{Fm}})\), where \(W\ne\varnothing\), \(r\in W\), each \(R_\alpha\subseteq W^2\), and \(rR_\alpha u\) for **all** formulas \(\alpha\) and worlds \(u\). A model adds an arbitrary valuation \(V\). Atoms, \(\bot\), \(\land\) and \(\lor\) have their usual local clauses, while
\[
u\Vdash A\to B\quad\Longleftrightarrow\quad
\forall v\,(uR_{A\to B}v\ \Longrightarrow\ (v\Vdash A\ \Longrightarrow\ v\Vdash B)).
\]
The formula indices are syntactic: different implication formulas need not share relations. The root-universality clause, unrestricted nonroot accessibility, and finite \(\Gamma\) are essential to this result. If \(X\) is used, its formulas are closed (variable-free) and their valuations are therefore frame-independent. In the complexity statement, \(X\) is fixed in advance, rather than supplied as an unrestricted additional input requiring a test of intuitionistic derivability.

## Proof

**Witness selection.** Fix a model \(\mathcal M\) and finite \(\Gamma\). For each \(\theta=(A\to B)\in I(\Gamma)\) such that \(r\not\Vdash\theta\), root universality supplies \(w_\theta\in W\) with \(w_\theta\Vdash A\) and \(w_\theta\not\Vdash B\). Put
\[
S=\{r\}\cup\{w_\theta:\theta\in I(\Gamma),\ r\not\Vdash\theta\}.
\]
Then \(|S|\le1+|I(\Gamma)|\). Restrict the atomic valuation to \(S\). For **every** formula index \(\alpha\), set the successor set at \(r\) to be all of \(S\). For an implication \(\theta\in I(\Gamma)\) and \(u\in S\setminus\{r\}\), set
\[
R'_\theta(u)=\begin{cases}
\varnothing,&u\Vdash_\mathcal M\theta,\\
\{w_\theta\},&u\not\Vdash_\mathcal M\theta.
\end{cases}
\]
The second case is always well-defined: if the original \(\theta\) fails at any \(u\), some world refutes its material consequent, so it also fails at the universally accessing root, and \(w_\theta\) was selected. For all other indices, set their nonroot rows empty. This defines an FMT frame on \(S\).

**Simultaneous truth lemma.** Induct on the syntactic construction of every subformula \(\psi\) of \(\Gamma\), proving
\[
\forall u\in S\qquad
(u\Vdash_\mathcal M\psi\ \Longleftrightarrow\ u\Vdash_{\mathcal M_\Gamma}\psi).
\]
Atoms and \(\bot\) are immediate, and Boolean conjunction and disjunction follow locally. Let \(\psi=\theta=(A\to B)\), assuming the claim for \(A,B\). At the root, \(r\not\Vdash_\mathcal M\theta\) exactly when a counterexample to \(A\Rightarrow B\) exists anywhere in \(W\). In that case the selected \(w_\theta\in S\) is still a counterexample by induction. In the opposite case every old world satisfies \(A\Rightarrow B\), hence every retained world does; the new root relation is universal on \(S\). Thus the root truth agrees. For a nonroot \(u\), a originally true \(\theta\) has an empty new row and stays true; a originally false \(\theta\) has the selected counterexample \(w_\theta\) as its sole successor and stays false. This finishes the induction, including nested implications and arbitrarily many formula indices.

**Closed-axiom transfer.** For any closed formula \(C\), its truth at any world is independent of the valuation, by induction on \(C\) (there are no atom occurrences). If the original frame validates every member of the finite set \(X\), then every \(C\in X\) is true at each original world under every valuation. Taking \(\Gamma=\{\varphi\}\cup X\) preserves this truth at each retained world, and valuation independence makes the new frame validate \(X\). The root truth value of \(\varphi\) is also preserved.

**NP upper bound.** For fixed \(X\), the number of distinct implication subformulas of \(\{\varphi\}\cup X\) is at most linear in the length of \(\varphi\) plus a constant. A nondeterministic verifier guesses at most this many worlds plus one, atomic truth tables on the variables occurring in \(\varphi\), and the finitely many relevant formula-indexed relations. This is polynomial-size data. It checks root-universality, evaluates every subformula bottom-up at every world, checks each closed formula of \(X\) at every world (equivalent to frame validation), and checks \(\varphi\) at the root. The witness theorem proves completeness of this certificate scheme.

**NP lower bound.** Reduce Boolean 3-SAT. For each Boolean variable \(b_i\), introduce two fresh atoms \(p_i,q_i\), representing the positive and negative literals, respectively. For a 3-CNF \(F\), set
\[
\Theta_F=
\bigwedge_i\bigl[(p_i\lor q_i)\land((p_i\land q_i)\to\bot)\bigr]
\ \land\
\bigwedge_{C\text{ clause of }F}\ \bigvee_{\ell\in C}t(\ell),
\]
where \(t(b_i)=p_i\) and \(t(\neg b_i)=q_i\). At an FMT root, every \(p_i\lor q_i\) holds exactly when at least one of the pair holds locally. As the root accesses itself for the relation of \((p_i\land q_i)\to\bot\), that implication forces the two atoms not to hold together at the root. Thus a root satisfying \(\Theta_F\) supplies an ordinary satisfying Boolean assignment to \(F\). Conversely, a satisfying assignment gives a one-world FMT model of \(\Theta_F\) with all relations reflexive and the intended literal valuations. Every closed negative axiom in \(X\) is an intuitionistic theorem, hence a classical tautology, and therefore is valid on this one-world frame. The reduction is polynomial and proves NP-hardness for each fixed \(X\). Combining the bounds gives NP-completeness.

## Verification

The standalone Python 3 standard-library program `verify_fmt.py` directly evaluates the formula-indexed relational semantics, reconstructs the normal form, and checks all retained-world/subformula truth values. It tests 1,150 pseudorandom finite rooted models on one to five worlds, a four-world case requiring three distinct selected witnesses, and 360 independently generated small 3-CNF instances against the dual-rail one-world reduction. The observed summary was `CHECK_OK compression_cases=1150 max_random_retained_worlds=4 distinct_witness_worlds=4 dualrail_instances=360`. Run `python3 verify_fmt.py` from the directory containing the file. These finite tests are diagnostic; the unrestricted theorem rests on the preceding structural induction, not on enumeration.

## Relationship to prior work

Kurahashi and Noguchi introduced propositional FMT frames with a universal root (Definitions 4.1–4.2) and proved the finite frame property for \(\mathbf{VF}\) and its finite closed negative extensions (Theorem 5.10). Their saturated-tableau construction establishes existence of finite countermodels but does not state this one-witness-per-implication star normal form, the linear bound on retained worlds, or designated-root NP-completeness. Their Lemma 4.5 supplies the frame-invariance observation for closed formulas.

The modal counterpart of FMT semantics goes back to Fitting, Marek and Truszczyński. Kurahashi and Sato study the finite frame property for modal extensions of pure necessitation, with formula-indexed accessibility but without the universal-root condition used here. Tominaga's 2026 published meeting summary reports NP-completeness for satisfiability of consistent closed-formula extensions of the *modal* pure logic of necessitation. That complexity statement is close in motivation but does not give the explicit rooted propositional witness-star normalization, nor identify its semantic designated-root problem. The 2026 Kurahashi–Noguchi paper relates the two logics by a translation preserving derivability; this does not, by itself, identify the two satisfiability notions. The modal complexity overlap remains a literature risk because only Tominaga's public abstract was available.

## Limitations

The result applies to **unrestricted propositional FMT frames with a universal root**; it does not automatically preserve additional frame conditions such as transitivity or arbitrary schemes. The bound counts distinct *syntactic* implication subformulas, not semantic equivalence classes, and is an upper bound rather than a proved universally optimal bound. No complexity assertion is made for freely varying or non-intuitionistically-valid axiom sets, for unrooted FMT models, for arbitrary-world satisfiability, or for exact derivability complexity. Random checks cover only their stated finite cases. The original 1992 modal paper and the full account underlying the 2026 Tominaga meeting abstract were not materially accessible for a whole-document comparison, so implicit prior coverage cannot be excluded with certainty.

## References

1. T. Kurahashi and M. Noguchi, *Very weak subintuitionistic logics*, arXiv:2605.20769v1 (first publicly available 2026-05-20), Definitions 4.1–4.2, Lemma 4.5, Theorem 5.10, §6 and Appendix A. https://arxiv.org/abs/2605.20769 ; author-hosted full text: https://www.researchgate.net/publication/405089771_Very_weak_subintuitionistic_logics
2. T. Kurahashi and Y. Sato, *The Finite Frame Property of Some Extensions of the Pure Logic of Necessitation*, Studia Logica, online 2024-11-04, DOI 10.1007/s11225-024-10154-w. https://link.springer.com/content/pdf/10.1007/s11225-024-10154-w.pdf
3. K. Tominaga, *Complexity of the pure logic of necessitation*, abstract in Mathematical Society of Japan, Autumn 2026 Meeting, titles and summaries, final version 2026-07-31, p. 15. https://www.mathsoc.jp/en/assets/file/meeting/kobe26sept/summary26sept_en_20260731.pdf
4. M. Fitting, V. W. Marek and M. Truszczyński, *The Pure Logic of Necessitation*, Journal of Logic and Computation 2 (1992), 349–373, DOI 10.1093/logcom/2.3.349 (bibliographic and related-literature comparison; full text not inspected).
