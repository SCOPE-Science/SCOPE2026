# Reachability normal form for multiple modal reductions in pure necessitation

## Finding
Let \(\mathbf N\) be the pure logic of necessitation: classical propositional logic with modus ponens and necessitation, but no modal distribution axiom. Let \(\Phi\subseteq\mathbb N_{>0}\times\mathbb N_{>0}\), and define
\[
L_{\Phi}=\mathbf N+\{\Box^{n}A\to\Box^{m}A:(m,n)\in\Phi\}.
\]
On \(\mathbb N\), form the directed graph \(G_{\Phi}\) having an edge
\[
k+n\longrightarrow k+m
\]
for every \((m,n)\in\Phi\) and every \(k\ge 0\). For all \(a,b\in\mathbb N\) and every propositional variable \(p\),
\[
L_{\Phi}\vdash \Box^{a}p\to\Box^{b}p
\quad\Longleftrightarrow\quad
b\text{ is reachable from }a\text{ in }G_{\Phi}.
\]
Hence a positive modal-reduction schema \(\Box^{v}A\to\Box^{u}A\) is redundant over \(L_{\Phi}\) exactly when \(u\) is reachable from \(v\) in \(G_{\Phi}\).

## Assumptions and scope
All reduction exponents in \(\Phi\) are positive. The theorem classifies the one-variable iterated-box implications \(\Box^{a}p\to\Box^{b}p\), and therefore redundancy of positive reduction schemata, for an arbitrary finite or infinite family \(\Phi\). It does not classify arbitrary formulas of \(L_{\Phi}\), and it does not cover reduction principles with a zero exponent.

## Proof
For the forward construction, every edge \(k+n\to k+m\) is itself an available axiom instance: substitute \(\Box^{k}p\) for \(A\) in \(\Box^{n}A\to\Box^{m}A\). A finite path from \(a\) to \(b\) therefore gives \(\Box^{a}p\to\Box^{b}p\) by repeated propositional transitivity.

For the converse, write \(r\leadsto s\) for reachability in \(G_{\Phi}\), including the empty path, and define the predecessor set
\[
E_r=\{s\in\mathbb N:s\leadsto r\}.
\]
Then
\[
E_a\subseteq E_b\quad\Longleftrightarrow\quad a\leadsto b.
\]
Indeed, if \(a\leadsto b\), every predecessor of \(a\) is also a predecessor of \(b\). Conversely, \(a\in E_a\), so \(E_a\subseteq E_b\) implies \(a\in E_b\), hence \(a\leadsto b\).

Work in the Boolean algebra \(\mathcal P(\mathbb N)\). Define a unary operation \(f\) by
\[
f(E_r)=E_{r+1},\qquad f(\mathbb N)=\mathbb N,
\]
and set \(f(X)=\varnothing\) for every other \(X\subseteq\mathbb N\). This is well-defined. If \(E_r=E_s\), then \(r\leadsto s\) and \(s\leadsto r\). Every edge of \(G_{\Phi}\) remains an edge after adding one to both endpoints, so the two paths shift to paths \(r+1\leadsto s+1\) and \(s+1\leadsto r+1\), giving \(E_{r+1}=E_{s+1}\). Also, because all exponents in \(\Phi\) are positive, every \(E_r\) is nonempty and no \(E_r\) equals \(\mathbb N\), so the clauses do not conflict.

The Boolean-algebra interpretation with \(\Box X=f(X)\) is sound for \(\mathbf N\): propositional tautologies are Boolean-valid, modus ponens preserves validity, and necessitation preserves validity because \(f(\mathbb N)=\mathbb N\). It also validates every reduction axiom in \(\Phi\). For \((m,n)\in\Phi\) and \(X=E_r\),
\[
f^{n}(E_r)=E_{r+n}\subseteq E_{r+m}=f^{m}(E_r),
\]
because \(r+n\to r+m\) is an edge. For \(X=\mathbb N\), both sides are \(\mathbb N\); for every other \(X\), positivity of \(m,n\) makes both iterates \(\varnothing\).

Now assign \(p\) the value \(E_0\). Inductively, \(\Box^{r}p\) has value \(E_r\). If \(a\not\leadsto b\), then \(E_a\nsubseteq E_b\), so the Boolean implication \(\Box^{a}p\to\Box^{b}p\) is not top in this sound model. Thus it is not derivable in \(L_{\Phi}\). This proves the equivalence.

For redundancy, if \(u\) is reachable from \(v\), the theorem gives \(\Box^{v}p\to\Box^{u}p\); substitution-invariance then yields every instance \(\Box^{v}A\to\Box^{u}A\). If \(u\) is not reachable from \(v\), the variable instance already fails in the model above.

## Verification
The necessity direction was checked independently against its defining algebraic construction: the modal operation is total, fixes top, and validates every generating reduction inequality on all subsets of \(\mathbb N\). The key equivalence \(E_a\subseteq E_b\iff a\leadsto b\) is proved directly and is the only order fact used.

As a non-proof sanity check, for every \(1\le m,n\le5\) and \(0\le a,b<15\), a breadth-first search of the single-reduction graph agreed with the closed-form reachability conditions obtained by iterating the unique step size; no discrepancy occurred. The theorem itself does not depend on this finite check.

## Relationship to prior work
Fitting, Marek, and Truszczyński introduced \(\mathbf N\) as classical propositional logic plus necessitation. Kurahashi and Sato studied extensions by a single modal-reduction principle, and Sato's recent interpolation work continues that single-principle setting. Knudstorp recently proved a finite-model-property theorem for arbitrary families of reduction principles over the normal modal logic \(\mathbf K\). The sources inspected below do not state the present exact reachability criterion for the iterated-box fragment of pure \(\mathbf N\), nor its corresponding redundancy criterion for arbitrary positive families.

The theorem is complementary to those results: it makes no finite-model-property or interpolation claim, and instead gives a complete syntactic consequence test for the depth-only fragment together with an explicit separating Boolean-algebra model whenever reachability fails.

## Limitations
The originality comparison is search-bounded rather than an exhaustive theorem-index proof; a broader algebraic or non-normal-modal source could contain an equivalent result under different terminology. The restriction to positive exponents is substantive in the countermodel because it ensures the non-special subsets collapse to \(\varnothing\) after one modal step. Cases involving exponent zero require a modified construction. No claim is made about arbitrary modal formulas beyond the iterated-box implication fragment.

## References
1. M. C. Fitting, V. W. Marek, and M. Truszczyński, “The Pure Logic of Necessitation,” *Journal of Logic and Computation* 2(3), 349–373 (1992), DOI 10.1093/logcom/2.3.349.
2. T. Kurahashi and Y. Sato, “The Finite Frame Property of Some Extensions of the Pure Logic of Necessitation,” *Studia Logica* 114, 297–323, DOI 10.1007/s11225-024-10154-w; preprint arXiv:2305.14762.
3. Y. Sato, “Uniform Lyndon interpolation for the pure logic of necessitation with a modal reduction principle,” *Journal of Logic and Computation* (2025), DOI 10.1093/logcom/exaf048; arXiv:2503.10176.
4. S. B. Knudstorp, “Knocking Down Boxes: The FMP for \(\mathbf K\oplus\Box^{m+k}p\to\Box^{m}p\),” arXiv:2510.00864.
5. H. Kogure, “Arithmetical Completeness for Some Extensions of the Pure Logic of Necessitation,” *Studia Logica* (2026), DOI 10.1007/s11225-026-10246-9; preprint arXiv:2409.00938.
