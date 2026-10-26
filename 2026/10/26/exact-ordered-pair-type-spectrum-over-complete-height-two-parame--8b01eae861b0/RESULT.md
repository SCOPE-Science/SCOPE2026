# Exact ordered-pair type spectrum over complete height-two parameter posets

## Finding
Let \(\mathbb P\) be the countable universal homogeneous partial order. For integers \(a,b\geq0\), let \(P_{a,b}=A\sqcup B\) have \(|A|=a\), \(|B|=b\), each level an antichain, and every element of \(A\) strictly below every element of \(B\). Each parameter is named separately. Let \(T_2(a,b)\) count complete types of **ordered distinct** pairs \((x,y)\) with \(x,y\notin P_{a,b}\) over these parameters. Write \(C(a,b)\) for those types satisfying \(x<y\) and \(I(a,b)\) for those satisfying \(x\parallel y\). Then

\[
\begin{aligned}
C(a,b)={}&4^a2^b+2^a4^b+3^{a+b}+3^a+3^b\\
 &-2^{a+b}-2^{a+1}-2^{b+1}+1,\\[2mm]
I(a,b)={}&4^{a+b}+4^a+4^b+2(3^a2^b+2^a3^b)\\
 &-4\cdot2^{a+b}-2(2^a+2^b)+2,\\
T_2(a,b)={}&2C(a,b)+I(a,b).
\end{aligned}
\]

There are equally many types with \(x<y\) and \(y<x\). In the balanced regime \(a=b=n\to\infty\), the proportion of comparable ordered pairs is
\[
\frac{2C(n,n)}{T_2(n,n)}\sim 2\left(\frac9{16}\right)^n,
\]
so asymptotically almost all pair types are incomparable. The exact small cases include \(T_2(0,0)=3\), \(T_2(1,0)=19\), \(T_2(1,1)=66\), and \(T_2(2,2)=746\).

## Assumptions and scope
A type is complete in the first-order theory of \(\mathbb P\), over an individually named finite induced copy of \(P_{a,b}\). The two added variables are ordered and unequal to each other and to every parameter. We do not quotient the parameters by their automorphisms, and do not count equality types. The formula also includes empty levels: \(a=0\) or \(b=0\) gives an antichain parameter set. No claim concerns arbitrary height-two posets with missing cross-comparabilities.

By homogeneity and the finite-extension property, such complete types are in bijection with finite labelled partial orders on \(P_{a,b}\cup\{x,y\}\) that preserve the induced order on the parameters. Every such extension is realized, and any two realizations of the same finite order pattern have the same complete type.

## Proof
**1. Local states and the compatibility principle.** Fix the comparison \(\rho\in\{<,>,\parallel\}\) of \(x,y\). For a parameter \(z\), define its local state as the ordered pair \((\operatorname{rel}(z,x),\operatorname{rel}(z,y))\), each coordinate in \(\{<,>,\parallel\}\). Requiring the induced order on \(\{x,y,z\}\) to be transitive leaves six states when \(x<y\) or \(x>y\), and seven states when \(x\parallel y\).

For two distinct parameters \(z,w\) in one level, retain a pair of states precisely when those states together with \(z\parallel w\) give a transitive induced four-point poset. For \(z\in A,w\in B\), instead test the fixed relation \(z<w\). All single-state self-pair tests inside a level pass. An assignment of local states to all parameters is a valid extension **if and only if** every same-level and cross-level pair of assigned states is compatible. Necessity is immediate. For sufficiency, transitivity on any three vertices involving at most two parameters is checked by one of these tests. A triple of three parameters is already transitive in \(P_{a,b}\). This exhausts all triples, establishing sufficiency.

**2. Support enumeration.** For fixed \(\rho\), let \(U,V\) be the sets of local states actually used on \(A,B\). The pair is permitted when each support is pairwise internally compatible and all its cross pairs are compatible. Because every state is self-compatible, a support of size \(i\) used on \(a\) distinctly named parameters contributes \(i!\,S(a,i)\) assignments, where \(S\) is a Stirling number of the second kind (with the usual empty-support convention). Thus the bivariate exponential generating function is
\[
F_\rho(e^s-1,e^t-1),\qquad
F_\rho(X,Y)=\sum_{i,j}c^{(\rho)}_{ij}X^iY^j,
\]
where \(c^{(\rho)}_{ij}\) counts compatible pairs of **supports** of cardinalities \(i,j\). (It is not the coefficient of \(X^iY^j\) that directly counts labelled assignments; the substitution is essential.)

The finite, exact support enumeration reduces to checking three- and four-point transitivity. Its two independent coefficient matrices, with rows and columns indexed \(0,1,2,3,4\), are
\[
(c^{(<)}_{ij})=
\begin{pmatrix}
1&6&10&6&1\\
6&20&24&12&2\\
10&24&20&7&1\\
6&12&7&1&0\\
1&2&1&0&0
\end{pmatrix},\qquad
(c^{(\parallel)}_{ij})=
\begin{pmatrix}
1&7&14&10&2\\
7&26&38&24&5\\
14&38&44&26&6\\
10&24&26&16&4\\
2&5&6&4&1
\end{pmatrix}.
\]
The \(x>y\) matrix equals the \(x<y\) matrix by exchanging the two variables. To reproduce every entry, enumerate the nine formal two-coordinate relations for one parameter, reject nontransitive three-point states, enumerate all subsets of the remaining six or seven states and retain only internally compatible supports, then test all ordered pairs of these supports against the cross-level compatibility matrix. The standalone program performs precisely these operations.

**3. Evaluation.** Set \(u=e^s,v=e^t\). Substitution \(X=u-1,Y=v-1\) in the first matrix polynomial gives
\[
\begin{aligned}
F_{<}(u-1,v-1)={}&u^4v^2+u^2v^4+u^3v^3+u^3v+uv^3\\
 &-u^2v^2-2u^2v-2uv^2+uv.
\end{aligned}
\]
The second gives
\[
\begin{aligned}
F_{\parallel}(u-1,v-1)={}&u^4v^4+u^4v+uv^4+2u^3v^2+2u^2v^3\\
 &-4u^2v^2-2u^2v-2uv^2+2uv.
\end{aligned}
\]
Since \([s^a/a!]\,e^{is}=i^a\), and similarly for \(t\), extracting coefficients proves the displayed expressions for \(C\), \(I\), and \(T_2\), for every \(a,b\ge0\).

**4. Asymptotics.** At \(a=b=n\), the leading term of \(C(n,n)\) is \(9^n\), followed by \(2\cdot8^n\). The leading term of \(T_2(n,n)\) is \(16^n\), all others bounded by a constant multiple of \(9^n\). Dividing gives the stated asymptotic equivalence. This is a statement about uniform counting of complete pair types, not about a probability distribution on actual pairs in the countable structure.

## Verification
Run `python verify.py` (Python standard library only). It reconstructs both compatibility matrices directly from three- and four-point strict transitivity, performs the binomial basis transform independently, and checks the resulting formulas for all \(0\le a,b\le7\) in each of three pair orientations (192 comparisons). A second routine enumerates every assigned comparison on \(P_{a,b}\cup\{x,y\}\) and tests transitivity directly for all \(a+b\le4\), giving fifteen independently checked parameter-size cases. It also checks the balanced leading terms. Its recorded output is `verification_output.txt`. These finite tests corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work
Classical work on the random homogeneous poset supplies homogeneity and its finite-extension property, not this bivariate two-type formula. The complete-type/finite-order-pattern correspondence is standard; its use here is not claimed as new. The previously considered antichain-parameter pair count is recovered at \(a=0\) or \(b=0\): \(T_2(0,b)=4\cdot4^b+6\cdot3^b-8\cdot2^b+1\). The contribution is the exact interaction of **two nonempty comparable parameter levels** and its exponentially decaying comparability proportion. Pretzel's insertion-position construction is relevant background, but the abstract available for that paper discusses dimensional bounds and does not resolve the present pair enumeration; the full text was not inspected.

## Limitations
The originality assessment is based on identifiable available literature and searches, not an exhaustive proof of priority. Highly specialized unindexed pair-extension enumeration may exist. No claim is made about counting tuples of arity greater than two, about arbitrary height-two parameter relations, or about independently certified results. The finite verification does not constitute a proof for all parameters. The proof is internal to finite-poset combinatorics plus the standard homogeneity fact.

## References
1. J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566, publicly posted 2010-09-03, especially §3.1 (generic partial order, extension property). https://arxiv.org/abs/1009.0566
2. P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz, and C. Szabó, *Reducts of the random partial order*, arXiv:1111.7109, publicly posted 2011-11-30, especially §2–3 (types and extension property). https://arxiv.org/html/1111.7109v2
3. O. Pretzel, *A construction for partially ordered sets*, Discrete Mathematics 32 (1980), 59–68, doi:10.1016/0012-365X(80)90100-4. Abstract-level comparison only; no claim of full-text examination.
