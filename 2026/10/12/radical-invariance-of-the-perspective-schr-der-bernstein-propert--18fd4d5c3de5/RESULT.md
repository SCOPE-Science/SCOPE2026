# Radical invariance of the perspective–Schröder–Bernstein property for semiregular rings
## Finding
Let \(R\) be a semiregular ring and write \(J=J(R)\). Recall that a module has the perspective–Schröder–Bernstein (PSB) property when any two direct summands which are each perspective to a direct summand of the other are themselves perspective. Then

\[
R_R\;\mathrm{has\ PSB}\quad\Longleftrightarrow\quad (R/J)_{R/J}\;\mathrm{has\ PSB}.
\]

Thus PSB is radical-invariant inside the class of semiregular rings: its truth is determined entirely by the von Neumann regular quotient \(R/J(R)\).

## Assumptions and scope
Rings are associative with identity and modules are unital right modules. A semiregular ring is one for which \(R/J(R)\) is von Neumann regular and idempotents lift modulo \(J(R)\). For idempotents \(e,f\), write \(e\sim_{rlr} f\) when there are idempotents forming a right-associate/left-associate/right-associate chain from \(e\) to \(f\). The standard idempotent criterion says that \(eR\) and \(fR\) are perspective exactly when \(e\sim_{rlr}f\).

The claim concerns the PSB property only. It does not assert the Schröder–Bernstein property, transitivity of perspectivity, or any finiteness condition.

## Proof
Set \(\overline R=R/J\), and use bars for reduction modulo \(J\).

First suppose \(\overline R_{\overline R}\) has PSB. Let \(eR\) and \(fR\) be direct summands of \(R_R\) that are mutually subperspective. Choose direct summands \(f'R\subseteq fR\) and \(e'R\subseteq eR\) such that

\[
e\sim_{rlr}f',\qquad f\sim_{rlr}e'.
\]

Reduction modulo \(J\) preserves right- and left-associate chains, so

\[
\overline e\sim_{rlr}\overline{f'},\qquad
\overline f\sim_{rlr}\overline{e'}.
\]

Hence \(\overline e\,\overline R\) and \(\overline f\,\overline R\) are mutually subperspective. PSB in \(\overline R\) gives \(\overline e\sim_{rlr}\overline f\). Khurana–Mittal Lemma 2.5, applied with the ideal \(J\subseteq J(R)\), lifts this relation to \(e\sim_{rlr}f\). Therefore \(eR\) and \(fR\) are perspective, so \(R_R\) has PSB. This is the lifting mechanism already used in the last paragraph of their proof of Theorem 2.6.

Conversely suppose \(R_R\) has PSB. Let \(\overline e\,\overline R\) and \(\overline f\,\overline R\) be mutually subperspective direct summands of \(\overline R\). Choose direct summands \(\overline{e'}\,\overline R\subseteq \overline e\,\overline R\) and \(\overline{f'}\,\overline R\subseteq \overline f\,\overline R\) such that

\[
\overline e\sim_{rlr}\overline{f'},\qquad
\overline f\sim_{rlr}\overline{e'}.
\]

Write the corresponding decompositions as

\[
\overline e=\overline{e'}+\overline{e''},\qquad
\overline f=\overline{f'}+\overline{f''},
\]

with each displayed pair orthogonal. Because \(R\) is semiregular, finite orthogonal families of idempotents modulo \(J\) lift to finite orthogonal families. Choose orthogonal lifts \(e',e''\) and \(f',f''\), and put \(e=e'+e''\), \(f=f'+f''\). Then \(e'R\) is a direct summand of \(eR\), and \(f'R\) is a direct summand of \(fR\). By Lemma 2.5 again,

\[
e\sim_{rlr}f',\qquad f\sim_{rlr}e'.
\]

Thus \(eR\) and \(fR\) are mutually subperspective in \(R_R\). PSB in \(R\) yields \(e\sim_{rlr}f\). Reducing this chain modulo \(J\) gives \(\overline e\sim_{rlr}\overline f\), so the original quotient summands are perspective. Hence \(\overline R_{\overline R}\) has PSB.

Both implications are proved.

## Verification
The proof was checked at the level of the idempotent formulation of perspectivity. The only lifting inputs are: (i) perspectivity is equivalent to an \(rlr\)-chain of idempotents; (ii) such a chain lifts across an ideal contained in the Jacobson radical, as stated in Khurana–Mittal Lemma 2.5; and (iii) semiregularity permits finite orthogonal idempotent lifting, the same lifting step used explicitly in their proof of Theorem 2.6. No finite experiment or computational search is used as a substitute for the universal argument.

The two directions use logically different information. Quotient-to-ring PSB needs the \(rlr\)-lifting lemma. Ring-to-quotient PSB additionally needs orthogonal lifting so that a nested quotient summand lifts as a nested summand upstairs. Reduction of an \(rlr\)-chain is immediate because equality of principal right or left ideals and the witnessing idempotent relations survive a quotient map.

## Relationship to prior work
Khurana and Mittal prove that if a semiregular ring has the ordinary Schröder–Bernstein property, then both the ring and its semiprimitive quotient have PSB. Their Lemma 2.5 lifts perspectivity chains through ideals contained in the Jacobson radical. In the final paragraph of the proof of Theorem 2.6 they in fact use the implication “quotient PSB implies ring PSB.” The converse implication needed for the equivalence above is not stated there; it is obtained by lifting the two nested quotient decompositions to orthogonal idempotents and then applying PSB upstairs.

The earlier Keef–Koşan paper introduces the PSB property and establishes several broad classes having it. The accessible publisher preview and abstract do not state a Jacobson-radical quotient criterion. Focused searches for PSB together with semiregular rings, Jacobson radicals, quotient rings, and idempotent lifting found no statement equivalent to the displayed biconditional.

## Limitations
The theorem requires semiregularity for the descent direction because nested quotient summands must be lifted compatibly. No claim is made that PSB descends through arbitrary ideals, or even arbitrary ideals in the Jacobson radical when idempotent lifting fails. The foundational Keef–Koşan full article was not available through an open full-text source during this check; its publisher preview and abstract were inspected, so a residual terminology-indexing risk remains.

## References
1. D. Khurana and S. Mittal, *Perspectivity and the perspective-Schröder-Bernstein Property*, arXiv:2609.39491v1, 2026. In particular Lemma 2.5 and Theorem 2.6.
2. P. W. Keef and M. T. Koşan, *The perspective-Schröder–Bernstein property for modules and abelian groups*, Journal of Algebra and Its Applications, DOI 10.1142/S0219498828500090, published online 28 July 2026.
