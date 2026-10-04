# A five-element idempotent translation monoid shared by \(\mathsf{S4}\) and \(\mathsf{Grz}\)
## Finding

For a modal formula \(\alpha(p)\), let \(\tau_\alpha\) be the modal-to-modal translation that fixes Boolean connectives and propositional variables and replaces
\[
\Diamond\varphi
\]
by
\[
\alpha(\tau_\alpha\varphi).
\]
Dvorkin proved that, without parameters, the normal additive formulas have exactly five equivalence classes in each of \(\mathsf{S4}\) and \(\mathsf{Grz}\).

Use the following representatives:
\[
0=\bot,\qquad a=p,\qquad e=\Diamond p.
\]
For \(\mathsf{S4}\), put
\[
g=\Diamond\Box\Diamond p,\qquad h=p\vee g.
\]
For \(\mathsf{Grz}\), put
\[
g=\Diamond\Box p,\qquad h=p\vee g.
\]

Define
\[
\alpha\star\beta:=\tau_\alpha(\beta).
\]
Dvorkin's composition identity gives
\[
\tau_\alpha\circ\tau_\beta=\tau_{\alpha\star\beta}.
\]
Modulo equivalence in the target logic, both \(\mathsf{S4}\) and \(\mathsf{Grz}\) therefore have the same multiplication table:
\[
\begin{array}{c|ccccc}
\star&0&a&e&g&h\\
\hline
0&0&a&0&0&a\\
a&0&a&a&a&a\\
e&0&a&e&g&h\\
g&0&a&g&g&h\\
h&0&a&h&g&h
\end{array}
\]

Consequently, the parameter-free normal translation classes form a five-element monoid with identity \(e\), every element is idempotent,
\[
x\star x=x,
\]
and the monoid is noncommutative, since
\[
0\star a=a\ne0=a\star0.
\]
Thus every parameter-free normal self-interpretation of either logic stabilizes after one iteration:
\[
\tau_\alpha^n\equiv\tau_\alpha
\qquad(n\ge1).
\]

## Assumptions and scope

Equivalence is equivalence in the target logic. The result concerns parameter-free **normal additive** formulas, exactly the formulas that define the modal-to-modal interpretations considered by Dvorkin.

For \(\mathsf{Grz}\), Dvorkin's representative \(g=\Diamond\Box p\) is equivalent in \(\mathsf{Grz}\) to \(\Diamond\Box\Diamond p\). This allows the same finite-frame semantic calculation to treat the nontrivial element \(g\) in both logics.

The claim is only about parameter-free translations. Dvorkin shows that parameters substantially enlarge the family of available interpretations, so no finite five-element classification is asserted in the parameterized setting.

## Proof

The published classification gives the five normal classes listed above. Closure under \(\star\) follows because composition of two modal-to-modal interpretations is again such an interpretation. Associativity follows from composition of translations, and \(e=\Diamond p\) is the identity because
\[
\tau_{\Diamond p}\varphi=\varphi.
\]

Most entries of the table are formal. Every translation fixes \(p\) and \(\bot\), hence
\[
\alpha\star0=0,\qquad \alpha\star a=a.
\]
Since \(e=\Diamond p\),
\[
\alpha\star e=\alpha,
\]
and \(e\star\beta=\beta\). Translating by \(0\) kills every outer diamond, while translating by \(a=p\) erases modal operators, giving the first two rows. Since \(h=p\vee g\),
\[
\alpha\star h=p\vee(\alpha\star g).
\]
It remains only to prove the two nontrivial identities
\[
g\star g=g,\qquad h\star g=g.
\]

Let \(F=(W,R)\) be a finite reflexive transitive frame. A world \(y\) is **maximal** when every \(R\)-successor of \(y\) is \(R\)-equivalent to \(y\). Put
\[
R'(x,y)\quad\Longleftrightarrow\quad R(x,y)\ \text{and}\ y\ \text{is maximal}.
\]
Dvorkin proves that on finite \(\mathsf{S4}\)-frames the operator defined by
\[
\gamma(p):=\Diamond\Box\Diamond p
\]
is exactly inverse image along \(R'\). For finite \(\mathsf{Grz}\)-frames the same calculation applies because
\[
\Diamond\Box p\leftrightarrow\Diamond\Box\Diamond p
\]
is derivable in \(\mathsf{Grz}\). Hence on the finite completeness classes for either target logic, the translation determined by \(g\) replaces \(R\) by \(R'\).

Now evaluate \(\gamma\) on the transformed frame \(F_g=(W,R')\). If \(y\) is maximal in the original frame, then
\[
R'[y]
\]
is exactly the maximal \(R\)-cluster containing \(y\). For every \(z\) in that cluster, \(R'[z]\) is the same cluster. Therefore, for every \(A\subseteq W\),
\[
x\models_{F_g}\Diamond\Box\Diamond A
\]
holds exactly when some maximal \(R\)-cluster accessible from \(x\) meets \(A\), which is exactly
\[
R'[x]\cap A\ne\varnothing.
\]
Thus the operator \(\gamma\) on \(F_g\) is again the ordinary diamond for \(R'\). The semantic substitution lemma for completely additive translations now gives
\[
g\star g\equiv g.
\]

For \(h=p\vee g\), the induced finite-frame relation is
\[
S=\mathrm{id}_W\cup R'.
\]
We claim that evaluating \(\gamma\) on \((W,S)\) still yields inverse image along \(R'\). If \(R'[x]\cap A\ne\varnothing\), choose a point \(y\in R'[x]\cap A\). The point \(y\) lies in a maximal original cluster, and every point of that cluster \(S\)-accesses the whole cluster, so \(x\models_S\Diamond\Box\Diamond A\).

Conversely, suppose \(x\models_S\Diamond\Box\Diamond A\). Choose an \(S\)-successor \(y\) witnessing the outer diamond. If \(y\) lies in a maximal original cluster, the inner \(\Box\Diamond A\) forces that cluster to meet \(A\), hence \(R'[x]\cap A\ne\varnothing\). If \(y=x\) is nonmaximal, finiteness provides a maximal original cluster accessible from \(x\). Taking any point \(z\) in that cluster as one of the worlds quantified by the box forces that same cluster to meet \(A\). Again \(R'[x]\cap A\ne\varnothing\). Hence
\[
h\star g\equiv g.
\]

The remaining column follows from \(h=p\vee g\), producing the displayed table. Since \(\mathsf{S4}\) and \(\mathsf{Grz}\) are determined by the finite frame classes used above, the equivalences hold in the logics themselves.

## Verification

The proof reconstructs the two nontrivial products semantically and derives all other products by the translation laws.

The bundled `verify.py` independently generates every reflexive transitive relation on at most four labelled worlds and, for the \(\mathsf{Grz}\) check, every reflexive transitive antisymmetric relation on at most four labelled worlds. It evaluates every valuation of \(p\), computes all twenty-five translated products, and checks them against the displayed table. The frame counts checked are
\[
1,4,29,355
\]
for \(\mathsf{S4}\) preorders and
\[
1,3,19,219
\]
for finite partial orders. The checker returns `VERIFY_OK`.

These finite computations are not used as an infinite proof. The general argument uses the explicit maximal-cluster calculation together with finite completeness.

## Relationship to prior work

Dvorkin proves three ingredients used here: the exact five normal parameter-free classes for each of \(\mathsf{Grz}\) and \(\mathsf{S4}\); the identity
\[
\tau_\alpha\tau_\beta\varphi=\tau_{\tau_\alpha\beta}\varphi;
\]
and the finite-frame characterization of \(\Diamond\Box\Diamond p\) by accessibility to maximal worlds. The paper then identifies the five normal logics interpretable in each target logic and explicitly postpones a systematic study of interpretability.

The paper uses composition in individual arguments, but it does not state the complete multiplication table of the five translation classes, the fact that the two target logics yield the same abstract composition monoid, or the resulting idempotence of every parameter-free normal translation.

Searches for modal-to-modal composition tables, idempotent parameter-free interpretations, five-element translation monoids, and the corresponding \(\mathsf{S4}/\mathsf{Grz}\) terminology did not locate an equivalent statement in the checked literature.

## Limitations

The result does not classify translations with parameters. It also classifies translations themselves, not just their inverse-image interpreted logics; different translations can in general induce related or coincident logical behavior.

The semantic proof uses finite completeness. The formula \(\Diamond\Box\Diamond p\) is not completely additive on all infinite reflexive transitive frames, so the finite-frame relation \(R'\) must not be promoted to a pointwise representation on arbitrary infinite \(\mathsf{S4}\)-frames.

Search non-detection is not a proof that no equivalent semigroup observation appears in an unindexed source.

## References

[1] Lev V. Dvorkin, “On Interpretations of Normal Modal Logics,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 321–340. arXiv:2606.31871. DOI:10.4204/EPTCS.447.18.

[2] Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge Tracts in Theoretical Computer Science 53, Cambridge University Press, 2001. DOI:10.1017/CBO9781107050884.
