# Free-algebra sizes are the tuple-orbit profile of the generic Brouwerian semilattice
## Finding
Let \(\mathbb B\) be the Fraïssé limit of the class of finite Brouwerian semilattices, and let \(F_n\) be the free Brouwerian semilattice on \(n\) generators. Then, for every \(n\ge 0\),
\[
\boxed{\bigl|\mathbb B^n/\operatorname{Aut}(\mathbb B)\bigr|=|F_n|.}
\]
Thus the ordered-tuple orbit profile starts
\[
\boxed{1,\ 2,\ 18,\ 623662965552330}
\]
for arities \(0,1,2,3\). In arity four, the orbit count is exactly \(|F_4|\), whose exact value is still unknown; the published free-algebra literature records that it has on the order of \(10^{14}\) decimal digits.

Equivalently, the orbit of an ordered tuple is completely determined by the congruence kernel of the evaluation map from the appropriate free algebra, and every congruence kernel occurs.

## Assumptions and scope
A Brouwerian semilattice is an algebra \((A,\wedge,\to,1)\) satisfying the relative-pseudocomplement adjunction. Carai and Ghilardi establish that this variety is locally finite and has the amalgamation property. Therefore its finite members form a Fraïssé class: hereditary closure is immediate, joint embedding follows by amalgamating over the one-element algebra, and there are only countably many finite isomorphism types. We use \(\mathbb B\) for its countable universal ultrahomogeneous limit.

The source paper works mainly with the order-dual co-Brouwerian signature. Order reversal preserves cardinalities and finite embeddings, so the free-algebra cardinalities quoted there are the same for Brouwerian semilattices.

## Proof
Fix \(n\). For an ordered tuple \(\bar a=(a_1,\ldots,a_n)\in\mathbb B^n\), local finiteness makes the generated subalgebra \(A_{\bar a}=\langle a_1,\ldots,a_n\rangle\) finite. Freeness gives a canonical surjective homomorphism
\[
\pi_{\bar a}:F_n\twoheadrightarrow A_{\bar a},\qquad x_i\mapsto a_i.
\]
Let \(\theta_{\bar a}=\ker \pi_{\bar a}\).

If \(g\in\operatorname{Aut}(\mathbb B)\) sends \(\bar a\) to \(\bar b\), then \(g\) carries every term value on \(\bar a\) to the corresponding term value on \(\bar b\), so \(\theta_{\bar a}=\theta_{\bar b}\).

Conversely, suppose \(\theta_{\bar a}=\theta_{\bar b}\). Define
\[
\varphi\bigl(\pi_{\bar a}(t)\bigr)=\pi_{\bar b}(t).
\]
Equality of kernels makes \(\varphi\) well defined, and it is an isomorphism \(A_{\bar a}\cong A_{\bar b}\) carrying each \(a_i\) to \(b_i\). Both subalgebras are finite, so ultrahomogeneity extends \(\varphi\) to an automorphism of \(\mathbb B\). Hence tuple orbits are in bijection with those congruences of \(F_n\) that occur as kernels.

Every congruence occurs. Indeed, if \(\theta\in\operatorname{Con}(F_n)\), the quotient \(F_n/\theta\) is finite by local finiteness and belongs to the same variety. Universality embeds it into \(\mathbb B\). Taking the images of the free generators gives a tuple whose evaluation kernel is exactly \(\theta\). Therefore
\[
\bigl|\mathbb B^n/\operatorname{Aut}(\mathbb B)\bigr|=|\operatorname{Con}(F_n)|.
\]

It remains to count congruences. In every Brouwerian semilattice, congruences are in bijection with deductive filters: a congruence \(\theta\) is sent to
\[
D_\theta=\{x:x\equiv_\theta 1\},
\]
and a deductive filter \(D\) determines
\[
x\equiv_D y
\quad\Longleftrightarrow\quad
(x\to y)\wedge(y\to x)\in D.
\]
These assignments are inverse; the verification uses only the adjunction defining \(\to\).

Because \(F_n\) is finite, every deductive filter has a least element: the meet of all its elements. Hence every filter is principal, of the form \(\uparrow m\), and different \(m\)'s give different filters. Consequently
\[
|\operatorname{Con}(F_n)|=|F_n|,
\]
which proves the formula.

Carai and Ghilardi record \(|F_0|=1\), \(|F_1|=2\), \(|F_2|=18\), and \(|F_3|=623662965552330\), while \(|F_4|\) is still unknown. This transfers that difficult free-algebra enumeration problem exactly to the oligomorphic orbit profile of \(\operatorname{Aut}(\mathbb B)\).

## Verification
The bundled `verify.py` provides an independent finite anchor at arity two. It enumerates all 23 labeled posets on at most three points and all 564 monotone two-variable Kripke models on them. Closing the two generators under conjunction and implication yields exactly 18 semantic elements, reconstructing the free two-generated implicative semilattice. It then verifies the residual law on the full 18-element operation tables, enumerates all deductive filters, and checks explicitly that there are 18, all principal. Finally it constructs the associated congruence for each filter, verifies operation compatibility, and checks that the 18 congruence partitions are distinct.

Replay output:

`VERIFY_OK 556584 exact assertions; 23 labeled posets, 564 Kripke models; free F_2 size=18; filters=congruences=18`

The all-arity theorem is the Fraïssé/free-algebra proof above; the computation is a low-arity independent check, not an extrapolation.

## Relationship to prior work
Carai and Ghilardi prove the two structural ingredients needed here: local finiteness and amalgamation for Brouwerian semilattices. They also quote the known sizes of the finite free algebras through three generators and emphasize that the four-generator cardinality remains unknown. Their full text contains no occurrence of “Fraïssé”, “automorphism”, “orbit”, or “congruence” in the sense used by the present statement.

The closest located neighboring result is an analogous tuple-orbit/free-congruence calculation for the random distributive lattice. That result concerns a different locally finite amalgamable variety and gives the closed value \(2^{2^n-2}\); it neither implies the Brouwerian count nor resolves the difficult free implicative-semilattice sequence. Exact and semantic searches under “Brouwerian semilattice”, “implicative semilattice”, “Fraïssé limit”, “tuple orbit”, and the numerical value \(623662965552330\) found no equivalent Brouwerian statement.

The numerical sequence itself is prior and is explicitly excluded from the originality claim. The claimed contribution is the exact identification of that sequence with the automorphism-orbit profile of the generic Brouwerian semilattice, including the transfer of the open \(|F_4|\) enumeration problem to arity four.

## Limitations
The result does not compute \(|F_4|\); it shows that the unknown free-algebra cardinality is exactly the fourth tuple-orbit number. The argument is a short synthesis of standard Fraïssé theory, the congruence-filter correspondence, and the source's local-finiteness/amalgamation results, so an equivalent formulation may exist as unindexed folklore. No independent audit has been performed.

## References
1. L. Carai and S. Ghilardi, *Existentially Closed Brouwerian Semilattices*, arXiv:1702.08352, first public 2017-02-27; *Journal of Symbolic Logic* 84 (2019), 1544–1575, DOI:10.1017/jsl.2019.71.
2. OEIS A393669, *Size of the free implicative semilattice on n generators*, recording \(1,2,18,623662965552330\) and the status of \(a(4)\).
