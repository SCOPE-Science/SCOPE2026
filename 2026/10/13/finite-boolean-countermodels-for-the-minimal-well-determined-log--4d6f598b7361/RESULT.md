# Finite Boolean countermodels for the minimal well-determined logic

## Finding

Write \(\mathcal W\) for the minimal well-determined logic of Gorbunov and Rybakov in the propositional language with conjunction \(\wedge\) and implication \(\to\). **Every \(\mathcal W\)-non-theorem has a countermodel carried by a finite Boolean powerset semilattice, with a formula-specific explicit size bound.** For any formula \(\varphi\), let \(s(\varphi)\) be the number of syntactically distinct subformulas whose outermost symbol is either a propositional variable or an implication. If \(\varphi\notin\mathcal W\), it has a countermodel based on a Boolean algebra with at most \(2^{s(\varphi)}\) elements. Consequently, \(\varphi\in\mathcal W\) if and only if it is valid, under all allowed valuations and \(\mu\)-extensions, on all finite Boolean powerset meet-semilattices.

The two-element member of this class alone is not complete. The formula \(\chi=p\to((p\to q)\to p)\) is always true on a two-element semilattice, but is false under a suitable \(\mu\)-extension on the three-element chain.

## Assumptions and scope

All formulas are finite and built from propositional variables using exactly \(\wedge\) and \(\to\). A \(\mathcal W\)-matrix is a meet-semilattice \((M,\wedge,\top)\) with greatest element, ordered by \(a\le b\) if and only if \(a\wedge b=a\). Following the cited semantics, a valuation \(v\) of variables and an arbitrary function \(\mu\) from the entire formula language to \(M\) extend recursively by
\[
\llbracket p\rrbracket=v(p),\qquad
\llbracket\alpha\wedge\beta\rrbracket=\llbracket\alpha\rrbracket\wedge\llbracket\beta\rrbracket,\qquad
\llbracket\alpha\to\beta\rrbracket=
\begin{cases}
\top,&\llbracket\alpha\rrbracket\le\llbracket\beta\rrbracket,\\
\mu(\alpha\to\beta),&\text{otherwise}.
\end{cases}
\]
A formula is valid in a matrix when **every** valuation and every \(\mu\)-extension evaluate it to \(\top\).

Define \(K(p)=\{p\}\), \(K(\alpha\wedge\beta)=K(\alpha)\cup K(\beta)\), and \(K(\alpha\to\beta)=\{\alpha\to\beta\}\). Put \(T(\psi)=K(\psi)\setminus\mathcal W\). The required previously established syntactic characterization, Gorbunov--Rybakov Lemma 4.4 and its corollary, states
\[
\alpha\to\beta\in\mathcal W
\quad\Longleftrightarrow\quad
T(\beta)\subseteq T(\alpha),
\]
and that no variable belongs to \(\mathcal W\), whereas conjunction belongs to \(\mathcal W\) precisely when both conjuncts do. Thus \(\psi\in\mathcal W\) if and only if \(T(\psi)=\varnothing\). The present theorem applies to **formula validity**, not to arbitrary semantic consequence over premise sets and not automatically to extensions of \(\mathcal W\).

## Proof

Fix \(\varphi\). Let \(U=U_\varphi\) be the set of all *syntactically distinct* subformulas of \(\varphi\) that are variables or implications and do not belong to \(\mathcal W\). Since \(K(\psi)\) always consists of conjunction-indecomposable subformulas of \(\psi\), for every subformula \(\psi\preceq\varphi\) we have \(T(\psi)\subseteq U\). Let \(B=\mathcal P(U)\), with intersection as meet, inclusion as order, and \(U\) as greatest element. This is a finite Boolean algebra, even for \(U=\varnothing\).

Define a valuation on the *entire* set of variables by
\[
v(p)=\begin{cases}U\setminus\{p\},&p\in U,\\U,&p\notin U.\end{cases}
\]
Define the fallback function \(\mu\) on the *entire* formula language: for each implication subformula \(\theta\) of \(\varphi\) belonging to \(U\), set \(\mu(\theta)=U\setminus\{\theta\}\); otherwise set \(\mu(\theta)=U\). This is well-defined by syntactic identity, not by identifying interderivable formulas; assign the arbitrary value \(U\) to non-implication inputs of \(\mu\), too. The specification therefore defines a legitimate full \(\mu\)-extension without relying on a partial assignment.

We prove by structural induction, **simultaneously for all subformulas** \(\psi\) of \(\varphi\), that
\[
\boxed{\llbracket\psi\rrbracket=U\setminus T(\psi).}
\]
If \(\psi\) is a variable \(p\), then \(p\notin\mathcal W\), so \(T(p)=\{p\}\) and \(p\in U\), and the formula follows from the definition of \(v\). If \(\psi=\alpha\wedge\beta\), the induction hypothesis and the complement identity give
\[
\llbracket\psi\rrbracket=(U\setminus T(\alpha))\cap(U\setminus T(\beta))
=U\setminus(T(\alpha)\cup T(\beta))=U\setminus T(\psi).
\]
Finally let \(\psi=\alpha\to\beta\). For the values given by the induction hypothesis, the semantic condition triggering the fixed value \(U\) is
\[
\llbracket\alpha\rrbracket\subseteq\llbracket\beta\rrbracket
\quad\Longleftrightarrow\quad
T(\beta)\subseteq T(\alpha)
\quad\Longleftrightarrow\quad
\psi\in\mathcal W.
\]
In this case the implication evaluates to \(U\), and \(T(\psi)=\varnothing\). Otherwise \(\psi\notin\mathcal W\), hence \(\psi\in U\); its fallback evaluates to \(U\setminus\{\psi\}\), which is \(U\setminus T(\psi)\), because \(K(\psi)=\{\psi\}\). This completes the induction.

If \(\varphi\notin\mathcal W\), then \(T(\varphi)\ne\varnothing\); its constructed value \(U\setminus T(\varphi)\) is a proper subset of \(U\). Hence it is not top. The bound follows from \(|U|\le s(\varphi)\) and \(|B|=2^{|U|}\). In the reverse direction, Gorbunov--Rybakov's general soundness theorem (their Theorem 7.2) says all \(\mathcal W\)-theorems are valid on all meet-semilattices with top, including these finite Boolean algebras. Together these statements establish finite Boolean completeness.

For the two-value boundary, let \(\chi=p\to((p\to q)\to p)\). In any two-element semilattice \(\{0<1\}\), if \(v(p)=0\), then the antecedent of the outer implication is bottom and the outer result is necessarily \(1\). If \(v(p)=1\), then the consequent \((p\to q)\to p\) is necessarily \(1\), so the outer result is again \(1\). The fallback values never matter in these two cases. On the three-element chain \(0<1<2\), set \(v(p)=1\), \(v(q)=0\), \(\mu(p\to q)=2\), \(\mu((p\to q)\to p)=0\), and \(\mu(\chi)=0\), with arbitrary values elsewhere. Then the inner, middle and outer implications evaluate respectively to \(2,0,0\), so \(\chi\) is refuted. All three order tests are strict in the fallback cases. This proves that restricting to a single two-element matrix is insufficient.

## Verification

Run `python3 verify_finite_boolean_w.py` with a standard Python 3 interpreter. The supplied checker computes theorem membership by the published recursive syntax criterion and directly implements the independently defined \(\mu\)-extension evaluation on finite Boolean sets. It enumerates all distinct formulas built from two variables with between one and five variable leaves (respectively \(2,8,64,640,7168\) formulas), tests the canonical identity on all their subformulas, tests 5,000 additional deterministic random three-variable formula trees, and checks all 576 combinations of relevant two-valued input/fallback assignments for the displayed separating formula. It also verifies the three-point countervaluation explicitly. Its output records 12,882 canonical checks. **Finite verification corroborates the identities but does not establish the unlimited-size theorem; the symbolic induction is the proof.**

## Relationship to prior work

Gorbunov and Rybakov (2026), Lemma 4.4, give the exact syntax-level membership criterion used above; their Sections 6--7 give the nonstandard implication semantics, soundness and completeness. Their completeness countermodel is the quotient of the entire formula language by interderivability, without an asserted finite Boolean reduction. Their conclusion explicitly identifies the finite-model-property question as a natural problem for the semantics. The contribution here is a **formula-dependent finite powerset countermodel**, a uniform elementary size bound, and the accompanying two-value obstruction. Neither polynomial decidability alone nor general algebraic completeness implies the asserted finite Boolean completeness without an additional semantic construction. Older equivalent representations under different terminology remain a literature risk.

## Limitations

The \(2^{s(\varphi)}\) bound is an explicit upper bound, **not** asserted optimal. The construction depends on the membership characterization proved in the cited work; it is not an independent rederivation of that syntactic lemma. The result applies to theoremhood/formula validity in exactly the stated \(\mu\)-extension semantics and does not establish finite matrices for arbitrary extensions or strong completeness for premise sets. The three-element example is not itself a Boolean algebra; it only proves the two-element *single-matrix* semantics is insufficient. A separate three- or four-element Boolean countermodel is guaranteed by the main construction for this non-theorem, but is not claimed to be minimal. Prior coverage from obscure algebraic-semantics literature cannot be categorically excluded.

## References

1. Igor Gorbunov and Mikhail Rybakov, *Semantics for the minimal well-determined logic*, arXiv:2607.15664v1 (first public version July 17, 2026), DOI:10.48550/arXiv.2607.15664. In particular Lemma 4.4, Corollary 4.8, Section 7 and Theorem 8.2. https://arxiv.org/abs/2607.15664
2. The authors' CC0 open full-text copy, https://www.researchgate.net/publication/410594465_Semantics_for_the_minimal_well-determined_logic (Sections 4, 6, 7, 8, 9 inspected).
