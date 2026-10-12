# A sharp class-size information threshold for \(\mathsf{S5}\) valuation extension

## Finding

Consider the valuation extension principle over \(\mathrm{RCA}_0\): every prescribed assignment of truth values to propositional variables on a countable Kripke frame extends to a truth-value assignment on **all finite modal formulas**, satisfying the Boolean and \(\Box\)-clauses. Write \(\mathrm{VEL}(\mathcal C)\) when only frames in the class \(\mathcal C\) are admitted.

Let \(\mathcal E_{=k}\) be the countable nonempty equivalence-relation frames in which **every equivalence class has exactly** \(k\) worlds, and let \(\mathcal E_{\le 2}\) be those with classes of size **one or two**. The following is the sharp class-size information threshold:

\[
\begin{aligned}
&\text{For each fixed integer }k\ge1,\quad
 \mathrm{RCA}_0\ \vdash\ \mathrm{VEL}(\mathcal E_{=k});\\
&\mathrm{RCA}_0\ \vdash\
 \bigl[\mathrm{VEL}(\mathcal E_{\le2})\ \longleftrightarrow\ \mathrm{ACA}_0\bigr].
\end{aligned}
\]

The lower bound for the second assertion already follows from the existence of a truth set for **one depth-one formula** \(\Box p_0\) under **one explicitly fixed atomic assignment** on each such frame. Hence neither large equivalence classes, unbounded modal depth, nor branching beyond one distinct neighbor causes the comprehension obstruction. The obstruction is the lack of an explicitly decidable indication of whether a world has a second class member.

## Assumptions and scope

All arguments are formalizable over the standard base system \(\mathrm{RCA}_0\), with \(\mathrm{ACA}_0\) denoting arithmetical comprehension. A frame is \(F=(W,R)\), where \(W\subseteq\mathbb N\) is nonempty and \(R\subseteq W\times W\) is given as a second-order set. In the classes above, \(R\) is reflexive, symmetric, and transitive. Thus these are \(\mathsf{S5}\) frames. Equivalence classes are \([w]_R=\{u\in W:R(w,u)\}\); the size restriction is an assumption about each class, not a supplied list or an oracle reporting that size.

Formulas are finitary expressions built from \(\bot\), numbered atomic propositions \(p_i\), implication, and \(\Box\). The atomic assignment is a set-coded function \(v:W\times\mathrm{Prop}\to\{0,1\}\). A full valuation is a set-coded function \(V:W\times\mathrm{Fml}\to\{0,1\}\) extending \(v\), such that

\[
 V(w,\bot)=0,\qquad
 V(w,\varphi\to\psi)=1-V(w,\varphi)(1-V(w,\psi)),
\]
\[
 V(w,\Box\varphi)=1\quad\Longleftrightarrow\quad
 (\forall u\in W)\bigl(R(w,u)\Rightarrow V(u,\varphi)=1\bigr).
\]

The quantifier in \(\mathrm{VEL}(\mathcal C)\) ranges over **every** frame satisfying the displayed assumptions and **every** atomic assignment. The assertion for \(\mathcal E_{=k}\) concerns each fixed positive \(k\); the construction also treats a supplied uniform value of \(k\). In contrast, in \(\mathcal E_{\le2}\) the class size can depend on the world and no class-size function is supplied.

## Proof

**Exact known class size needs no jump.** Fix a positive integer \(k\), a frame in \(\mathcal E_{=k}\), and atomic assignment \(v\). For each world \(w\), enumerate the increasing natural numbers \(u\in W\) such that \(R(w,u)\) until exactly \(k\) distinct values have been found. The promise \(|[w]_R|=k\) proves termination, and the resulting list enumerates all successors of \(w\). This is a total search computable relative to the given set \(R\), uniformly in \(w\) and the supplied \(k\). Therefore \(\Box\psi\) at \(w\) is simply the conjunction of the \(k\) recursively computed values of \(\psi\) at those listed worlds. Structural recursion on a finite formula now gives a uniform terminating oracle computation of \(V(w,\varphi)\) from \(R\oplus v\). Over \(\mathrm{RCA}_0\), its graph exists by \(\Delta^0_1\) comprehension. Induction on formula complexity proves all valuation equations and extension of \(v\).

**Unknown one-or-two class size is bounded above by arithmetical comprehension.** Suppose \(F\in\mathcal E_{\le2}\). In \(\mathrm{ACA}_0\), the set

\[
 D=\{w\in W:(\exists u\in W)\,[u\ne w\land R(w,u)]\}
\]

exists. For \(w\in D\), search for its unique distinct \(R\)-neighbor \(m(w)\); this halts, and for \(w\notin D\), put \(m(w)=w\). This yields a total map computable from \(D\oplus R\), with \([w]_R=\{w,m(w)\}\). Hence the modal recursion reduces to

\[
 V(w,\Box\psi)=V(w,\psi)\mathbin{\wedge}V(m(w),\psi).
\]

Again structural recursion computes one complete valuation from \(D\oplus R\oplus v\), yielding \(\mathrm{ACA}_0\vdash\mathrm{VEL}(\mathcal E_{\le2})\).

**The lower bound holds for genuine \(\mathsf{S5}\) matching frames.** Work over \(\mathrm{RCA}_0\) and assume \(\mathrm{VEL}(\mathcal E_{\le2})\). Let \(f:\mathbb N\to\mathbb N\) be an arbitrary injection. Set \(W=\mathbb N\), designate the even world \(2n\) for each possible output \(n\) and the odd world \(2s+1\) for each input \(s\), and form the relation

\[
 R(x,y)\Longleftrightarrow
 x=y\ \lor\
 (\exists n,s)\,[x=2n\land y=2s+1\land f(s)=n]\ \lor\
 (\exists n,s)\,[y=2n\land x=2s+1\land f(s)=n].
\]

For fixed \(x,y\) these cases reduce to elementary parity tests and one evaluation of \(f\); thus \(R\) exists in \(\mathrm{RCA}_0\). Injectivity makes the nonloop edges a matching: every odd world is paired with one even world, and an even world is paired with at most one odd world. Consequently \(R\) is an equivalence relation with classes of size one or two.

Prescribe \(v(2n,p_0)=1\) for all \(n\), \(v(2s+1,p_0)=0\) for all \(s\), and zero for every other atomic proposition. This assignment exists by recursive comprehension. Let \(V\) be any full extension supplied by the principle. Reflexivity and the construction give, for every \(n\),

\[
 V(2n,\Box p_0)=1
 \quad\Longleftrightarrow\quad
 \neg(\exists s)\,[f(s)=n].
\]

Therefore \(\{n:V(2n,\Box p_0)=0\}\) is exactly the range of \(f\) and exists by \(\Delta^0_1\) comprehension relative to \(V\). The existence of the range of every injection is equivalent to \(\mathrm{ACA}_0\) over \(\mathrm{RCA}_0\). This establishes the reverse implication and the advertised depth-one restriction.

**The boundary is genuinely informational.** If class size is identically two, the known-size argument computes the unique partner by searching for it; no arithmetical comprehension is required. If size may be one or two but a set explicitly identifies the two-member classes, the same base-theory argument works relative to that set. Requiring that the size be no greater than two without supplying which worlds are isolated is precisely what permits the range encoding above.

## Verification

The standalone `verify.py` checks the modal evaluation formula against direct quantification over all accessibility successors on every labeled equivalence partition into blocks of size at most two through six worlds. It checks eleven formula shapes and all one-variable assignments, as well as finite injective-range encodings. Running `python verify.py` produced:

`VERIFY_OK frames=119 valuations=5898 formula_world_comparisons=375078 range_checks=30`

These finite tests check the implementation and boundary constructions only. The reverse-mathematical assertions for arbitrary countable frames are established by the preceding comprehension arguments, not by finite enumeration.

## Relationship to prior work

Takeda and Yokoyama (arXiv:2607.01970, Proposition 2.4) showed that unrestricted valuation extension implies \(\mathrm{ACA}_0\) using a universal accessibility relation. Takeda (arXiv:2608.22822, Theorem 2.27) went further: valuation extension over all image-finite frames is equivalent to \(\mathrm{ACA}_0\); its lower-bound proof uses a directed partial-function frame \(R(n,m)\Leftrightarrow f(m)=n\). Thus the **upper** implication for \(\mathcal E_{\le2}\) is already covered by that theorem, and a one-successor lower-bound construction is also prior work. The present result instead establishes the reversal inside reflexive, symmetric, transitive frames with two-point-or-smaller equivalence classes and contrasts it with base-theory extension for exact uniform class size. Neither these S5 restrictions nor the exact-size/unknown-size contrast occurs in the inspected statements or constructions.

Friedman (2017), *Concrete Mathematical Incompleteness: Basic Emulation Theory*, uses injection-coded equivalence relations to derive arithmetical comprehension in a different maximal-emulation principle. Thus encoding a range by singleton/two-element classes is itself not claimed as a new technique; the claim is its exact application to the modal valuation-extension principle, together with the uniform-class-size contrast.

## Limitations

The theorem is about **set existence over second-order arithmetic**, not about ordinary classical existence of semantic evaluations; it does not claim any complexity gap for fixed finite frames. It treats propositional, finitary, one-box modal formulas on countable equivalence frames; it does not cover arbitrary infinitely branching frames, temporal operators, or quantified modal logic. The finite verifier is not a proof assistant or an infinite-frame certificate. The originality comparison is limited to the inspected primary manuscripts, the older related emulation construction, and targeted available searches; an equivalent older result using different reverse-mathematical terminology remains a residual risk.

## References

1. Y. Takeda and K. Yokoyama, *Bisimulations in second-order arithmetic*, arXiv:2607.01970v1, first publicly submitted 2026-07-02, especially Definition 2.1, Proposition 2.2, and Proposition 2.4. https://arxiv.org/abs/2607.01970
2. Y. Takeda, *Frame definability in second-order arithmetic*, arXiv:2608.22822v1, first publicly submitted 2026-08-24, especially Section 2.1, Theorem 2.26, and Theorem 2.27. https://arxiv.org/abs/2608.22822
3. H. M. Friedman, *Concrete Mathematical Incompleteness: Basic Emulation Theory*, October 10, 2017, Section 2, 'Maximal Emulation/3'. https://u.osu.edu/friedman.8/
