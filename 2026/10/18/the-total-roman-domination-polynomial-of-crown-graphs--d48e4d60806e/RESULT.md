# The total Roman domination polynomial of crown graphs

## Finding
For each integer \(n\ge2\), let \(\mathrm{Cr}_n=K_2\times K_n\) be the crown graph, equivalently \(K_{n,n}\) with the edges of one fixed perfect matching deleted. Its two named parts are \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with \(a_i b_j\in E\) exactly when \(i\ne j\).

A *total Roman dominating function* is a map \(f:V(\mathrm{Cr}_n)\to\{0,1,2\}\) such that every vertex labeled zero has a neighbor labeled two, and every positively labeled vertex has a positively labeled neighbor. Define the full weight enumerator
\[
R_n(z)=\sum_{f\ \mathrm{total\ Roman}}z^{\sum_{v}f(v)}.
\]
Put
\[
\begin{aligned}
Q_n(z)&=(1+z)^{n-1}-1,\\
F_n(z)&=(1+z+z^2)^n-(1+z)^n-nz^2(1+z)^{n-1},\\
U_n(z)&=(z+z^2)^n-z^n-nz^{n+1},\\
V_n(z)&=(1+z)^n-1-nz,
\end{aligned}
\]
where \(F_1(z)=0\). Then the following **exact identity of integer polynomials** holds for every \(n\ge2\):
\[
\boxed{\begin{aligned}
R_n(z)={}&F_n(z)^2
+2nz^2Q_n(z)\bigl(F_n(z)-F_{n-1}(z)\bigr)\\
&+2U_n(z)V_n(z)
+nz^4Q_n(z)^2\\
&+n(n-1)z^6(1+z)^{2n-4}
+2nz^{n+2}Q_n(z)+z^{2n}.
\end{aligned}}
\]
Consequently, every coefficient counts all distinct labelings on the named vertices, not only minimum-weight labelings. The least exponent and its coefficient are
\[
(\gamma_{tR}(\mathrm{Cr}_n),[z^{\gamma_{tR}(\mathrm{Cr}_n)}]R_n)=
\begin{cases}
(4,1),&n=2,\\
(6,31),&n=3,\\
(6,n^2(n-1)),&n\ge4.
\end{cases}
\]
For instance, \(R_2(z)=z^4(1+z)^4\), while
\[
R_3(z)=31z^6+72z^7+78z^8+50z^9+21z^{10}+6z^{11}+z^{12}.
\]

## Assumptions and scope
All graphs are finite, simple, and have the specified named vertices. The graph product is the **direct/tensor product**, not the Cartesian product. Both layers have size \(n\ge2\). A function's weight is \(\sum_v f(v)\), so changing labels at named vertices produces a different function. No symmetry quotient is taken. Only the total Roman condition above is counted; this is not perfect, independent, quasi-total, or ordinary Roman domination.

## Proof
Write \(A_2,B_2\) for the vertices labeled two in the respective parts and \(A_+,B_+\) for vertices labeled one or two. If a vertex \(a_i\) is zero, its defenders are exactly the vertices of \(B_2\) at indices other than \(i\). If \(a_i\) is positive, its possible positive neighbors are exactly the vertices of \(B_+\) at indices other than \(i\). The same facts with \(A,B\) exchanged are both necessary and sufficient for feasibility. Split all functions by whether the numbers of twos in the two layers are zero, one, or at least two. The following seven disjoint cases exhaust the nine ordered possibilities after exchanging layers.

1. **At least two twos in each layer.** Every zero has a defender and every positive has a positive neighbor. The one-layer enumerator with at least two twos is \(F_n\), obtained by subtracting zero- and one-two assignments from \((1+z+z^2)^n\). Contribution: \(F_n^2\).

2. **At least two twos in one layer, exactly one in the other.** Let the latter unique two have index \(j\). At index \(j\), the first layer must be positive to avoid an undefended zero; its enumerator is \(F_n-F_{n-1}\). The layer with its unique two must also contain at least one additional positive vertex: otherwise the positive vertex at index \(j\) in the first layer has no positive neighbor. The enumerator for that layer is \(z^2Q_n\). There are \(n\) choices of \(j\) and two layer orders. Contribution: \(2nz^2Q_n(F_n-F_{n-1})\).

3. **At least two twos in one layer, none in the other.** Every vertex in the first layer must be positive, since the opposite layer has no defenders. There must be at least two twos in this first layer; its enumerator is \(U_n\). The other layer consists only of zeros and ones and must have at least two ones, to give every positive vertex in the all-positive first layer a positive neighbor. Its enumerator is \(V_n\). Contribution: \(2U_nV_n\).

4. **Exactly one two in each layer, at the same index \(i\).** Each layer must have at least one further positive vertex; otherwise the opposite two at index \(i\) is isolated among positives. Both sides are independently counted by \(z^2Q_n\), giving \(nz^4Q_n^2\).

5. **Exactly one two in each layer, at different indices \(i\ne j\).** The first layer must have a one at index \(j\), and the second must have a one at index \(i\); other vertices may be zero or one. Both layers then have at least two positives, so all positive vertices have positive neighbors. Each ordered pair of distinct indices contributes \(z^6(1+z)^{2n-4}\), yielding \(n(n-1)z^6(1+z)^{2n-4}\).

6. **Exactly one two in one layer, none in the other.** The first layer must be entirely positive; given the unique two at index \(i\), its weight is \(n+1\). The other layer must contain a one at index \(i\), to avoid an undefended zero, and at least one more one, to give the two at index \(i\) a positive neighbor. The enumerator is \(zQ_n\). There are \(n\) choices of \(i\) and two layer orders, yielding \(2nz^{n+2}Q_n\).

7. **No twos in either layer.** Every vertex must be positive, and every positive label is one. Since \(n\ge2\), every vertex has positive neighbors. Contribution: \(z^{2n}\).

The sum of these seven exhaustive, disjoint contributions is precisely the asserted identity. Every necessity used in the cases comes from the two local neighborhood conditions; each displayed sufficient condition makes both conditions hold, so no functions are missed or overcounted.

For the minimum-weight consequences, inspect the least nonzero coefficient of the seven explicit terms, keeping the small cases separate. For \(n=2\) the identity simplifies to \(z^4(1+z)^4\). For \(n=3\) the only contributions at weight six are the diagonal two-defender configuration, the same-index two-defender configurations, the one-defender configurations, and the all-one function, yielding \(31\). For \(n\ge4\) the least weight is six; the weight-six terms count \(n(n-1)\) adjacent defender pairs and \(n(n-1)^2\) same-index defender pairs, hence \(n^2(n-1)\). This last consequence also follows by direct coefficient extraction from the polynomial, independently of the verbal classification.

## Verification
Run `python3 VERIFY_CROWN.py` in the same directory. The script uses only Python's standard library. It constructs the seven-term polynomial using integer coefficient convolution and **independently** loops through every \(\{0,1,2\}\)-assignment to both layers for \(2\le n\le6\); it checks the two graph-theoretic conditions directly from the adjacency relation. The script compared all \(597861\) assignments and every polynomial coefficient, with agreement in all five cases. It also checks the minimum coefficients and polynomial boundary coefficients for \(7\le n\le30\). See `VERIFY_CROWN_OUTPUT.txt`. Finite computations corroborate the proof; they do not replace the uniform seven-case argument.

## Relationship to prior work
Cabrera Martínez, Kuziak, Peterin, and Yero (2020) studied total Roman domination on direct products. Their Theorem 10 and Corollary 11 establish the minimum value \(6\) for the applicable complete-graph products and characterize small optimum-weight cases, but do not enumerate **all** total Roman functions by weight. The current identity therefore does **not** claim novelty for the minimum value. Thakkar and Badiyani (2022) characterized minimal total Roman functions in arbitrary graphs; their partial-order minimality notion and criterion do not give this whole-weight distribution. A published full enumerator for connected complete multipartite graphs concerns a different graph class: \(\mathrm{Cr}_n\) is not complete multipartite for \(n\ge3\). A published perfect Roman result for crown graphs uses a different labeling condition and does not imply total Roman counts.

## Limitations
The theorem concerns only crown graphs of the stated form, labeled vertices, and ordinary total Roman domination. It makes no claim for arbitrary direct products, arbitrary bipartite graphs with other deleted matchings, or other Roman domination variants. Literature comparisons cannot exclude uncatalogued equivalent formulations. The verification is finite; the infinite assertion relies on the disjoint case analysis. Independent scientific validation has not been performed.

## References
- A. Cabrera Martínez, D. Kuziak, I. Peterin, and I. G. Yero, *Dominating the direct product of two graphs through total Roman strategies*, arXiv:2005.13608v1, first publicly available 2020-05-27; *Mathematics* **8** (2020), 1438, doi:10.3390/math8091438. See especially Theorem 10 and Corollary 11.
- D. K. Thakkar and S. M. Badiyani, *Total Roman domination number of graphs*, *TWMS J. Applied and Engineering Mathematics* **12** (2022), 445–455. See Definitions 2.2–2.4 and Theorem 3.3.
- A. Cabrera Martínez, I. Peterin, and I. G. Yero, *Roman domination in direct product graphs and rooted product graphs*, *AIMS Mathematics* **6** (2021), 11084–11096, doi:10.3934/math.2021643; note that ordinary Roman and total Roman domination are different conditions.
