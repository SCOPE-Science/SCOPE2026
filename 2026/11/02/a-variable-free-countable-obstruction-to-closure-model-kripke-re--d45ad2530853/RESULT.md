# A variable-free countable obstruction to closure-model Kripke representation

## Finding

There exists a countable closure model \(\mathcal M=(W,G,\operatorname{cl},V)\) in the sense of Nishimura, satisfying both model-relative generalization and closure under modus ponens at every world, with the following simultaneous properties:

1. All propositional letters have empty valuations. The failure of the Kripke-representability condition \(\mathsf{KRep}\) is witnessed entirely by formulas without propositional letters.
2. Except at one distinguished world \(z\), the modal operation is ordinary Kripke necessity for a relation of outdegree at most two.
3. For **every finite set of formulas** \(\Phi\), a Kripke relation on the *same* world set, with the *same* valuation, agrees with \(\mathcal M\) on the truth of every formula in \(\Phi\) at every world.
4. No single Kripke relation on that world set agrees with \(\mathcal M\) on all formulas simultaneously.

The mechanism is a filter of cofinite modal truth sets which is finitely, but not globally, realized inside the model. In contrast with a previously published infinite counterexample using countably many propositional letters, no letter is needed here.

## Assumptions and scope

The Boolean modal language is built from \(\top\), negation, implication, a unary \(\Box\), and any optional set of propositional letters. Put \(\bot=\neg\top\), use the usual Boolean abbreviations, and write \(\Box^0\varphi=\varphi\) and \(\Box^{j+1}\varphi=\Box(\Box^j\varphi)\). The propositional valuation below makes every letter false at every world.

Let \(N=\{0,1,2,\ldots\}\). On \(N\) define a Kripke relation \(S\) by
\[
S[0]=\varnothing,\qquad S[n]=\{0,n-1\}\quad(n\geq1).
\]
For \(n=1\), the displayed set contains just one point. Thus all successor sets have cardinality at most two. Let \(\mathcal K\) be the Kripke model \((N,S,V_0)\) with all atoms false. Denote its formula truth set by \(E(\varphi)=\{n\in N:\mathcal K,n\models\varphi\}\).

Add one new world \(z\), put \(W=N\cup\{z\}\), and define the generator \(G:W\to\mathcal P(\mathbf{MF})\) by
\[
G(n)=\{\varphi:S[n]\subseteq E(\varphi)\}\quad(n\in N),
\qquad
G(z)=\{\varphi:N\setminus E(\varphi)\text{ is finite}\}.
\]
Let \(\operatorname{cl}\) be the identity operation on sets of formulas. Assign every propositional letter the empty truth set on \(W\). The definitions of the generators refer solely to the independently defined Kripke model on \(N\); hence they are not circular.

A closure model satisfies the condition \(\mathsf{G}\) if every formula valid on its closure frame belongs to each \(\operatorname{cl}(G(w))\); it satisfies \(\mathsf{K}\) if membership of \(\alpha\) and \(\alpha\to\beta\) implies membership of \(\beta\). These are Nishimura's conditions. We establish the stronger model-relative version of \(\mathsf{G}\), in which validity means truth at every world in the displayed model.

## Proof

**1. Truth and closure rules.** Structural induction on formulas shows that \(\mathcal M,n\models\varphi\) exactly when \(\mathcal K,n\models\varphi\) for each \(n\in N\). In the modal step, the membership clause \(\varphi\in G(n)\) is precisely the Kripke universal condition over \(S[n]\). At the exceptional world, the definition gives
\[
\mathcal M,z\models\Box\varphi
\quad\Longleftrightarrow\quad
N\setminus E(\varphi)\text{ is finite}.
\]
If \(\varphi\) is true at all of \(W\), it is true throughout \(N\), and so belongs to \(G(z)\) and to every \(G(n)\). This proves model-relative generalization (and therefore the frame-relative condition \(\mathsf{G}\)). Each \(G(n)\) is closed under modus ponens because all points of \(S[n]\) satisfy its members. The family of cofinite subsets of \(N\) is closed under finite intersections and upward inclusion. Thus \(G(z)\) is also closed under modus ponens. Condition \(\mathsf{K}\) holds everywhere.

**2. Variable-free nonrepresentability.** For every \(j\geq0\) put
\[
\delta_j=\Box^{j+1}\bot\land\neg\Box^j\bot,
\qquad \chi_j=\neg\delta_j.
\]
An induction using the successor sets above proves
\[
\mathcal K,n\models\Box^k\bot\quad\Longleftrightarrow\quad n<k
\qquad(n,k\geq0).
\]
Hence \(E(\delta_j)=\{j\}\) and \(E(\chi_j)=N\setminus\{j\}\). In particular every \(\chi_j\) belongs to \(G(z)\), while world \(j\) falsifies \(\chi_j\). Therefore no world of \(N\) satisfies all members of \(G(z)\).

To rule out \(z\) itself, set \(\theta=\neg\Box\chi_0\). Because \(0\in S[n]\) whenever \(n\geq1\), and \(\chi_0\) is false at world \(0\), the Kripke truth set of \(\theta\) is \(N\setminus\{0\}\). So \(\theta\in G(z)\). Yet \(\Box\chi_0\) is true at \(z\), since \(\chi_0\) is cofinite on \(N\). Consequently \(\theta\) is false at \(z\). It follows that
\[
\bigcap_{\psi\in G(z)}\{w\in W:\mathcal M,w\models\psi\}=\varnothing.
\]
On the other hand, \(\bot\notin G(z)\). Nishimura's \(\mathsf{KRep}\) condition would require membership of every formula in \(G(z)\) whenever the displayed intersection is contained in its truth set. With empty intersection, that condition would incorrectly force \(\bot\in G(z)\). Thus \(\mathcal M\) is not \(\mathsf{KRep}\).

Indeed, suppose a relation \(R\) on the same \(W\), with the same valuation, preserved truth of *every* formula. Every \(R[z]\)-successor would then satisfy every member of \(G(z)\); the intersection above makes this impossible unless \(R[z]=\varnothing\). That would make \(\Box\bot\) true at \(z\), contrary to \(\bot\notin G(z)\). Hence no such relation exists.

**3. Every finite observation has a Kripke realization.** Every formula \(\varphi\) has an eventual truth value on \(N\): there is a cutoff \(c_\varphi\) beyond which either all worlds satisfy it or all worlds falsify it. This follows by structural induction. Atomic formulas are constantly false, and Boolean connectives preserve eventual constancy. For \(n\geq1\),
\[
\mathcal K,n\models\Box\varphi
\quad\Longleftrightarrow\quad
\mathcal K,0\models\varphi\ \text{and}\ \mathcal K,n-1\models\varphi,
\]
which preserves eventual constancy for the box.

Given a finite \(\Phi\), gather every immediate operand \(\psi\) of every occurrence of \(\Box\) in any formula of \(\Phi\). Choose \(m\in N\) beyond all the finitely many associated cutoffs. Then, for every gathered \(\psi\),
\[
\mathcal K,m\models\psi
\quad\Longleftrightarrow\quad E(\psi)\text{ is cofinite in }N.
\]
Take \(R_\Phi[n]=S[n]\) for all \(n\in N\) and \(R_\Phi[z]=\{m\}\). In the Kripke model \((W,R_\Phi,V)\), all formulas have their original truth values on \(N\). Structural induction through the finitely many subformulas in \(\Phi\) shows the truth values at \(z\) also agree, since the modal step is exactly the preceding cofinite-versus-\(m\) equivalence. This proves the finite-approximation assertion.

## Verification

The standalone `checker.py` performs a finite-prefix independent implementation of the variable-free semantics, including a symbolic eventual-value bit. It checks the displayed singleton truth sets for \(101\) consecutive \(\delta_j\), the exceptional-world separator \(\theta\), and finite-locality across \(1000\) pseudorandom modal formulas and the explicit witness family. Its recorded output is `ALL_CHECKS_OK`. The program is corroborative only: the induction, infinitely many separating formulas and nonrepresentability conclusion are proved above, not inferred from finite tests.

Run it with `python3 checker.py`; no third-party packages are needed.

## Relationship to prior work

Nishimura [1] introduces closure semantics, defines \(\mathsf G\), \(\mathsf K\), and \(\mathsf{KRep}\) in Sections 2 and 4.3, and gives in Example 4.24 a countably infinite \(\mathsf G\)-and-\(\mathsf K\) countermodel to \(\mathsf{KRep}\) using countably many propositional letters. The present construction is not a claim that infinite separation is new; the distinct result is **variable-free** separation together with the single-exceptional-world and all-finite-observations properties.

Hansen, Kupke and Pacuit [2], particularly Section 4.2, study modal saturation and give a variable-free infinitely satisfiable-but-unrealized sequence on a countable Kripke frame. That is a relevant predecessor for the finite-realizability mechanism. It does not state the particular closure-model \(\mathsf G+\mathsf K\)-versus-\(\mathsf{KRep}\) construction and simultaneous same-carrier finite Kripke approximation proved here. Nonprincipal filters and finite/cofinite Boolean algebras themselves are established tools, not claimed as discoveries.

## Limitations

This is an existence theorem, not a classification of all infinite nonrepresentable closure models. It asserts nonrepresentability on the **same world set with the same valuation**; it does not deny representations after adjoining an ideal world. The example relies on a countably infinite carrier; the finite-carrier representation phenomenon is already known. Equivalent older constructions under neighborhood filter or ultrafilter terminology remain a priority risk. No independent external mathematical audit has been performed.

## References

[1] Yuki Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations*, arXiv:2610.01433 (first posted October 1, 2026), Sections 2, 4.3 and Example 4.24. https://arxiv.org/html/2610.01433v2

[2] Helle Hvid Hansen, Clemens Kupke and Eric Pacuit, *Neighbourhood Structures: Bisimilarity and Basic Model Theory*, *Logical Methods in Computer Science* **5**(2:2), 2009; arXiv:0901.4430, Sections 4.2–4.3. https://arxiv.org/abs/0901.4430
