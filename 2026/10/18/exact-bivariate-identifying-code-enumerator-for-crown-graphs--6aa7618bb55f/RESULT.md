# Exact bivariate identifying-code enumerator for crown graphs

## Finding
For each integer \(n\ge4\), let \(H_n\) be the crown graph with vertices \(A_1,\ldots,A_n,B_1,\ldots,B_n\), and with edges \(A_iB_j\) exactly when \(i\ne j\). An *identifying code* is a vertex set \(C\) such that all \(2n\) closed-neighborhood traces \(N[v]\cap C\) are nonempty and pairwise distinct. Count codes by the number of selected vertices on each side:

\[
\mathcal I_n(x,y)=\sum_{C\text{ identifying}}x^{|C\cap A|}y^{|C\cap B|}.
\]

The complete bivariate enumerator is

\[
\boxed{\begin{aligned}
\mathcal I_n(x,y)={}&(x+y+xy)^n+n(x+y+xy)^{n-1}\\
&-n\bigl(x^{n-1}+y^{n-1}+x^{n-1}y+xy^{n-1}\bigr)\\
&-n(n-1)\bigl(x^{n-2}y+xy^{n-2}\bigr).
\end{aligned}}
\]

Consequently, the ordinary cardinality enumerator has the particularly short form

\[
\boxed{\mathcal I_n(z,z)=(z^2+2z)^n+n(z^2+2z)^{n-1}-2n^2z^{n-1}-2nz^n.}
\]

For \(n\ge5\), the minimum identifying-code size and the number of minimum codes are

\[
\boxed{\gamma_{\mathrm{ID}}(H_n)=n-1,\qquad N_{\min}(H_n)=n\bigl(2^{n-1}-2n\bigr).}
\]

Each minimum code for \(n\ge5\) omits one matched index, selects exactly one of \(A_i,B_i\) at every other index, and selects at least two codewords from each bipartition class. For \(n=4\), the graph is the three-cube, and \(\gamma_{\mathrm{ID}}(H_4)=4\) with \(56\) minimum codes. This last numerical cube case was already known; it is included to make the polynomial valid at its first admissible order.

## Assumptions and scope
All graphs are finite, undirected, loopless, and labeled as above. The exponent of \(x\) records the selection count on \(A=\{A_i\}_{i=1}^n\), and the exponent of \(y\) records that on \(B=\{B_i\}_{i=1}^n\). Distinguishing uses **closed** neighborhoods of **all** vertices, including selected vertices; nonempty traces are also required. No result is claimed here for \(n\le3\). A crown graph is also \(K_{n,n}\) with the perfect matching \(\{A_iB_i\}\) removed, equivalently the bipartite Kneser graph \(H(n,1)\).

## Proof
Write \(X=\{i:A_i\in C\}\) and \(Y=\{i:B_i\in C\}\). At each matched index, classify membership as absent, \(A\)-only, \(B\)-only, or both. The closed-neighborhood traces are exactly

\[
I(A_i)=\bigl(\{A_i\}\cap C\bigr)\cup\{B_j:j\in Y\setminus\{i\}\},
\qquad
I(B_i)=\bigl(\{B_i\}\cap C\bigr)\cup\{A_j:j\in X\setminus\{i\}\}.
\]

**Separation within each side.** Selected \(A\)-vertices have different \(A\)-labeled elements in their traces and cannot share a trace with an unselected \(A\)-vertex. Two unselected vertices \(A_i,A_j\) with distinct indices have equal traces if and only if both indices lie outside \(X\cup Y\). The same statement holds for pairs of \(B\)-vertices. Therefore all pairs within each side are separated exactly when

\[
|[n]\setminus(X\cup Y)|\le1.
\tag{1}
\]

**Separation across the sides.** If \(I(A_i)=I(B_j)\), comparing the \(A\)-labeled part of the traces forces \(X\subseteq\{i,j\}\); comparing the \(B\)-labeled part forces \(Y\subseteq\{i,j\}\). Thus \(|X\cup Y|\le2\). For \(n\ge4\), condition (1) instead yields \(|X\cup Y|\ge n-1\ge3\), so cross-side equalities are impossible. Hence (1) is necessary and sufficient for separation of all \(2n\) traces.

**Nonempty traces.** Every selected vertex is covered by itself. An unselected \(A_i\) has a selected neighbor exactly when \(Y\setminus\{i\}\) is nonempty. Consequently all \(A\)-vertices are covered precisely under one of these three possibilities: \(|Y|\ge2\); \(|Y|=1\) and \(Y\subseteq X\); or \(Y=\varnothing\) and \(X=[n]\). Symmetrically, all \(B\)-vertices are covered precisely when \(|X|\ge2\); or \(|X|=1\) and \(X\subseteq Y\); or \(X=\varnothing\) and \(Y=[n]\). Together with (1) this is a necessary-and-sufficient classification of **all** identifying codes.

**Counting.** Condition (1) permits either zero or one absent matched index. The three possibilities at each occupied index have respective weights \(x,y,xy\). Before imposing coverage, their generating polynomial is

\[
(x+y+xy)^n+n(x+y+xy)^{n-1}.
\]

Exactly six disjoint classes of separated-but-not-covering sets must be removed. If \(Y=\varnothing\) and \(X\ne[n]\), there is exactly one missing index, with polynomial \(nx^{n-1}\); symmetrically, \(ny^{n-1}\). If \(Y\) is a singleton outside \(X\), the sole \(B\)-only index is chosen in \(n\) ways, while either no further index is absent or one of the other \(n-1\) indices is absent. These two families contribute \(nx^{n-1}y\) and \(n(n-1)x^{n-2}y\); interchanging sides contributes \(nxy^{n-1}\) and \(n(n-1)xy^{n-2}\). They are disjoint for \(n\ge4\), since a set triggering both opposite singleton failures would occupy at most two indices. Subtracting the six contributions proves the displayed bivariate formula. Substituting \(x=y=z\) and collecting like terms proves the univariate formula.

**Minimum and optimizer count.** Condition (1) forces at least \(n-1\) codewords. For \(n\ge5\), a code of that size occupies exactly \(n-1\) indices and uses one vertex per occupied index. The coverage conditions then say that both sides must receive at least two selections. Choose the omitted index in \(n\) ways, then choose which of the remaining \(n-1\) indices belong to \(A\) so that neither class has size less than two. The count is

\[
n\sum_{a=2}^{n-3}\binom{n-1}{a}=n(2^{n-1}-2n),
\]

which is positive for every \(n\ge5\). When \(n=4\), a size-three code would select one vertex at three indices; neither selected side can then have two vertices, so none is covering. The coefficient of total degree four in the already proved polynomial is \(56\), which establishes the stated boundary minimum and count. This completes the proof.

## Verification
The standalone standard-library program `verify.py` constructs adjacency directly from the graph definition, forms each closed-neighborhood trace for every initial subset, and independently tests the stated index-occupancy criterion. It exhausts every subset for \(4\le n\le10\): \(1,398,016\) graph-subset decisions. It compares complete **bivariate** coefficient distributions, not just minima. It additionally checks the resulting symbolic polynomial for \(11\le n\le50\), including coefficient positivity, side-exchange symmetry, and the total number of codes. Running `python3 verify.py` reproduces `verification_output.txt` and ends with `VERIFICATION_OK`. These finite tests corroborate but do not replace the proof for arbitrary \(n\).

## Relationship to prior work
Foucaud and Lehtilä's 2022 work on identifying codes proves general upper bounds for twin-free bipartite graphs. It neither gives the above crown-specific classification nor counts codes by selections on the two sides. The crown-graph study of Glen, Kitaev, and Pyatkin (2016) uses the same graph family, but its invariant is word-representation number. Venugopal and Vidya (2022) study a stronger, differently defined multiple-intruder location-domination parameter and report a crown-graph scalar result, not the closed-neighborhood identifying-code distribution. Hudry, Junnila, and Lobstein (2024, Section 6) explicitly record that the three-cube has \(56\) minimum identifying codes; that boundary count is **not** claimed as new.

Related existing exact enumerations for identifying codes of chain graphs and threshold graphs do not cover this family: the crown graph has an induced \(2K_2\) on two matched index pairs, while chain graphs and threshold graphs are \(2K_2\)-free. A related classification of edge-metric bases in crown graphs has an index-pair skeleton resembling the **minimum-size** cases, but it concerns a distinct edge-distance invariant and does not count all identifying codes or impose the closed-neighborhood coverage conditions. Searches did not identify an earlier equivalent bivariate result; that absence is not proof of publication priority.

## Limitations
The displayed formula is asserted only for \(n\ge4\); \(H_3\) admits cross-side signature collisions not excluded by the index-coverage bound. Source discovery cannot rule out unindexed or inaccessible prior enumerations, and the existing edge-metric-basis work is a meaningful source of possible structural overlap. Independent verification by an external researcher has not been performed. The proof is exact and infinite-family; the finite verification program is supporting evidence only.

## References
1. F. Foucaud and T. Lehtilä, *Revisiting and improving upper bounds for identifying codes*, arXiv:2204.05250 (first posted 11 April 2022), SIAM J. Discrete Math. 36 (2022), 2619–2634, DOI: 10.1137/22M148999X.
2. O. Hudry, V. Junnila, and A. Lobstein, *On Iiro Honkala's Contributions to Identifying Codes*, arXiv:2402.08264 (2024), Fundamenta Informaticae 191 (2024), 165–196, DOI: 10.3233/FI-242178, in particular Section 6.
3. M. Glen, S. Kitaev, and A. Pyatkin, *On the representation number of a crown graph*, arXiv:1609.00674 (2016), Discrete Appl. Math. 244 (2018), 89–93.
4. K. Venugopal and K. A. Vidya, *Multiple intruder locating domination in chordal and bipartite graphs*, Advances and Applications in Mathematical Sciences 21(10) (2022), 5731–5742, especially Proposition 8. PDF: https://www.mililink.com/upload/article/1101917171aams_vol_2110_august_2022_a14_p5731-5742_k._venugopal_and_k._a._vidya.pdf.
