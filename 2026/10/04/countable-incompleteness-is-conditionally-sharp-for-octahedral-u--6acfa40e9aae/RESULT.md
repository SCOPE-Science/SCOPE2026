# Countable incompleteness is conditionally sharp for octahedral ultrapowers

## Finding
Let \(\mathcal U\) be a free countably complete ultrafilter on an infinite set \(I\). For every separable real Banach space \(X\), the canonical diagonal isometry
\[
j:X\longrightarrow X_{{\mathcal U}},\qquad j(x)=[i\mapsto x]_{{\mathcal U}},
\]
is surjective. In particular, for \(X=\ell_1\), one has \(X_{{\mathcal U}}\cong\ell_1\) isometrically. Although \(\ell_1\) is octahedral, it is not rigid octahedral. Hence \(X_{{\mathcal U}}\) is not rigid octahedral and therefore not \(\omega_1\)-rigid octahedral.

Thus, if a free countably complete ultrafilter exists, the countable-incompleteness assumption in Rueda Zoca's 2026 ultrapower rigidification theorem is sharp with respect to the class of free ultrafilters: an octahedral space need not rigidify at all under a free countably complete ultrapower.

## Assumptions and scope
All Banach spaces are real. A countably complete ultrafilter is one closed under countable intersections. The statement is conditional on the availability of a free countably complete ultrafilter. No existence or consistency assertion for such an ultrafilter is made here.

The recent source proves that if \(X\) is octahedral, then \(X_{{\mathcal U}}\) is \(\omega_1\)-rigid octahedral for every countably incomplete ultrafilter \(\mathcal U\) over any infinite index set. The present finding identifies a genuine obstruction on the opposite side of that hypothesis.

## Proof
First prove the separable-collapse lemma. Let \(f:I\to X\) be bounded. Because \(X\) is separable, for each integer \(n\ge1\) the bounded range of \(f\) has a countable cover by open balls of radius \(2^{-n}\). If the inverse image of every ball in this cover failed to belong to \(\mathcal U\), then the complement of every inverse image would belong to \(\mathcal U\). Countable completeness would put the intersection of those complements in \(\mathcal U\), but that intersection is empty. Hence there is \(x_n\in X\) such that
\[
A_n=\{i\in I:\|f(i)-x_n\|<2^{-n}\}\in\mathcal U.
\]
For \(m,n\ge1\), the set \(A_m\cap A_n\) belongs to \(\mathcal U\) and is nonempty. Choosing an index in that intersection gives
\[
\|x_m-x_n\|<2^{-m}+2^{-n}.
\]
Thus \((x_n)\) is Cauchy and converges to some \(x\in X\). Given \(\varepsilon>0\), choose \(n\) with \(2^{-n}+\|x_n-x\|<\varepsilon\). On \(A_n\),
\[
\|f(i)-x\|<2^{-n}+\|x_n-x\|<\varepsilon.
\]
Therefore \(\lim_{{\mathcal U}}\|f(i)-x\|=0\), so \([f]_{{\mathcal U}}=j(x)\). Every ultrapower class is constant modulo \(N_{{\mathcal U}}\), proving that \(j\) is onto.

Next, \(\ell_1\) is octahedral. Given finitely many \(u^1,\ldots,u^m\in S_{{\ell_1}}\) and \(\varepsilon>0\), choose a coordinate \(k\) with \(|u^r_k|<\varepsilon/2\) for every \(r\). With \(e_k\) the \(k\)-th unit vector,
\[
\|u^r+e_k\|_1=1-|u^r_k|+|1+u^r_k|>2-\varepsilon
\]
for every \(r\).

Finally, \(\ell_1\) is not rigid octahedral. Let
\[
x=(2^{-1},2^{-2},2^{-3},\ldots)\in S_{{\ell_1}}.
\]
If \(y\in S_{{\ell_1}}\) satisfied both \(\|x+y\|_1=2\) and \(\|-x+y\|_1=2\), equality in the coordinatewise triangle inequality would force \(y_n\ge0\) for every \(n\) from the first equality and \(y_n\le0\) for every \(n\) from the second. Hence \(y=0\), a contradiction. The finite set \(\{x,-x\}\) therefore has no exact octahedral witness. Since \(X_{{\mathcal U}}\cong\ell_1\), the ultrapower is not rigid octahedral.

## Verification
The collapse argument was checked directly from the quotient definition of an ultrapower and uses countable completeness only in the countable-cover step. The obstruction to rigid octahedrality uses the exact equality case of the \(\ell_1\) triangle inequality and the explicit positive vector \(x=(2^{-n})_{{n\ge1}}\). No finite experiment, asymptotic numerical evidence, or unproved classification is used.

Rueda Zoca defines \(\kappa\)-rigid octahedrality by exact simultaneous norm-two witnesses for all families of size below \(\kappa\), and Proposition 8.1 states the countably incomplete ultrapower implication. Avilés--Cabello Sánchez--Castillo--González--Moreno explicitly note that countably complete ultrapowers of sufficiently small Banach spaces collapse to the diagonal copy; the proof above specializes and strengthens the needed part to every separable Banach space without invoking cardinal-size machinery.

## Relationship to prior work
Rueda Zoca, arXiv:2609.24414v1, proves that octahedrality of \(X\) is equivalent to \(\omega_1\)-rigid octahedrality of \(X_{{\mathcal U}}\) for every countably incomplete ultrafilter, and records the earlier theorem of Hardtke for free ultrafilters on \(\mathbb N\). Every free ultrafilter on \(\mathbb N\) is countably incomplete, so those results do not test free countably complete ultrafilters.

Avilés et al. discuss the opposite regime and state that, for countably complete ultrafilters, diagonal embeddings are onto for Banach spaces below the relevant measurable-cardinal threshold. The present result uses that collapse mechanism to produce an explicit sharpness witness for the new rigidification theorem: the standard octahedral space \(\ell_1\) returns unchanged and is not rigid octahedral.

## Limitations
The result is conditional on the existence of a free countably complete ultrafilter. It does not provide such an ultrafilter and makes no set-theoretic consistency claim beyond that hypothesis. It also does not weaken Rueda Zoca's positive theorem for countably incomplete ultrafilters. The novelty claim is limited to the explicit sharpness consequence for octahedral rigidification; the diagonal-collapse phenomenon for countably complete ultrafilters is prior literature.

## References
1. Abraham Rueda Zoca, *Transfinite octahedrality in spaces of operators*, arXiv:2609.24414v1, first submitted 2026-09-21. Proposition 8.1 and Sections 1, 2.1, 8.
2. Antonio Avilés, Félix Cabello Sánchez, Jesús M. F. Castillo, Manuel González, Yolanda Moreno, *On ultrapowers of Banach spaces of type \(\mathcal L_\infty\)*, Fundamenta Mathematicae 222 (2013), 195–212, DOI: 10.4064/fm222-3-1. Remark 3.5(c).
3. Jan-David Hardtke, *Summands in locally almost square and locally octahedral spaces*, Acta et Commentationes Universitatis Tartuensis de Mathematica 22 (2018), 149–162, DOI: 10.12697/ACUTM.2018.22.13. Proposition 4.1.
