# Three diagonal points algebraically generate an elementary free projective plane

## Finding

Let \(T\) be the complete theory of open projective planes. Suppose \(M\models T\) contains an elementary submodel \(A\cong\pi^4\), where \(\pi^4\) is Marshall Hall's free projective plane on a generating quadrangle \(a,b,c,d\). Define the three diagonal points
\[
e=(a\vee c)\wedge(b\vee d),\qquad
f=(a\vee b)\wedge(c\vee d),\qquad
g=(a\vee d)\wedge(b\vee c).
\]
Then
\[
\boxed{\operatorname{acl}_M(e,f,g)=A\cong\pi^4}.
\]
Thus three parameters can algebraically generate a countably infinite elementary model. At the same time,
\[
\operatorname{dcl}_M(e,f,g)\subsetneq\operatorname{acl}_M(e,f,g),
\]
and none of the four free generators \(a,b,c,d\) is definable over \(e,f,g\).

## Assumptions and scope

The language is the two-sorted incidence language of projective planes, with the usual definable join and meet operations \(\vee\) and \(\wedge\). The statement is conditional only on an elementary copy \(A\cong\pi^4\) inside a model of \(T\). Hyttinen and Paolini prove that the free planes \(\pi^n\), \(4\le n\le\omega\), form an elementary chain, so such elementary copies occur naturally in the standard free models.

The claim concerns algebraic and definable closure over a specific three-point parameter set. It does not assert that every three-element set has infinite algebraic closure, nor that three is a minimal arity for this phenomenon.

## Proof

Hyttinen and Paolini's Proposition 7.1 uses exactly the displayed quadrangle and diagonal points. They show that the involution
\[
a\leftrightarrow b,\qquad c\leftrightarrow d
\]
extends to an automorphism of \(A\) fixing \(e,f,g\). Consequently
\[
a,b,c,d\notin\operatorname{dcl}_A(e,f,g).
\]

The same proposition then observes that the finite complete-quadrilateral configuration with points \(a,b,c,d,e,f,g\) and the six lines
\[
abg,\quad cdg,\quad adf,\quad bcf,\quad ace,\quad bde
\]
is closed over \(\{e,f,g\}\) in the sense used in their algebraic-closure analysis. Using their hyperfree characterization, they conclude
\[
a,b,c,d\in\operatorname{acl}_A(e,f,g).
\]

Now use the fact that \(a,b,c,d\) generate \(A=\pi^4\) as a projective plane. Every element \(x\in A\) is obtained from \(a,b,c,d\) by a finite term in \(\vee\) and \(\wedge\), hence
\[
x\in\operatorname{dcl}_A(a,b,c,d)\subseteq\operatorname{acl}_A(e,f,g).
\]
Therefore \(A\subseteq\operatorname{acl}_A(e,f,g)\), while the reverse inclusion is automatic, so
\[
\operatorname{acl}_A(e,f,g)=A.
\]

Finally, because \(A\preccurlyeq M\), algebraic closure of parameters from \(A\) does not acquire new elements in \(M\): if a formula over \(A\) has finitely many solutions in \(M\), elementarity makes \(A\) contain exactly that same finite solution set. Hence
\[
\operatorname{acl}_M(e,f,g)=\operatorname{acl}_A(e,f,g)=A.
\]
The automorphism argument above also gives the strict definable-closure inclusion in \(M\).

## Verification

The bundled script `verify_complete_quadrilateral.py` independently checks the finite incidence pattern used in Proposition 7.1. It encodes the four quadrangle vertices, the three diagonal points, and the six three-point lines, verifies that every non-parameter vertex \(a,b,c,d\) is incident with exactly three displayed lines, verifies that the three diagonal parameters each have degree two, and verifies that the involution \((a\ b)(c\ d)\) preserves all six lines while fixing \(e,f,g\). It then replays the logical closure chain
\[
\{a,b,c,d\}\subseteq\operatorname{acl}(e,f,g)
\Longrightarrow
\langle a,b,c,d\rangle\subseteq\operatorname{acl}(e,f,g).
\]
It returns `VERIFY_OK`.

This finite script is a consistency check of the combinatorial witness, not a replacement for the model-theoretic theorem that closed-over configurations are algebraic. That theorem is taken from the cited paper.

## Relationship to prior work

Hyttinen and Paolini explicitly prove \(\operatorname{acl}\ne\operatorname{dcl}\) by means of this complete-quadrilateral witness, and later identify algebraic closure with their iterative \(\operatorname{cl}^*\) construction. The additional observation here is that their witness does much more than exhibit one algebraic-but-not-definable point: once all four quadrangle generators are algebraic over the three diagonals, term closure forces the whole free plane \(\pi^4\) into the same algebraic closure. Elementarity then gives the exact equality \(\operatorname{acl}_M(e,f,g)=\pi^4\).

Targeted searches for the formulations “three diagonal points algebraically generate \(\pi^4\),” “three parameters have algebraic closure equal to a free projective plane,” and equivalent complete-quadrilateral wording found the underlying Proposition 7.1 but no source stating this exact closure equality. The current and previous ledgers were also checked; the closest owned result concerns the finite-arity type spectrum of existentially closed projective planes, a different theory and a different invariant.

## Limitations

The result is a short consequence of a published proof, so the main originality risk is uncatalogued folklore or an observation implicit in lecture notes. No minimality statement is made about the number three: smaller parameter sets may have interesting algebraic closure, and this finding does not classify them. The claim also does not enumerate the elements of \(\operatorname{dcl}(e,f,g)\); it only proves that this definable closure is proper inside \(\pi^4\).

## References

1. Tapani Hyttinen and Gianluca Paolini, *First-Order Model Theory of Free Projective Planes*, arXiv:1811.03351, first posted 8 November 2018; *Annals of Pure and Applied Logic* 172 (2021), no. 2, 102888, DOI 10.1016/j.apal.2020.102888. In particular Proposition 7.1 and Corollary 7.15.
2. Marshall Hall, *Projective Planes*, Transactions of the American Mathematical Society 54 (1943), 229–277.
