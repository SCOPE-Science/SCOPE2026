# Free bi-Heyting chain algebras: complete term-profile normal form and exact size

## Finding
Fix an integer \(k\ge1\). Let \(C_n\) denote the bounded \(n\)-element chain, \(n\ge2\), equipped with its Heyting implication and co-Heyting subtraction. Let \(\mathcal V=\operatorname{HSP}\{C_n:n\ge2\}\) in the full signature \(\{0,1,\wedge,\vee,\to,\setminus\}\), and let \(F_{\mathcal V}(k)\) be the free \(k\)-generated algebra of this variety.

For \(0\le r\le k\), define
\[
T_{k,r}=\sum_{m=r}^k\binom{k}{m}2^{k-m}r!\left\{\begin{matrix}m\\r\end{matrix}\right\},
\]
where the braces denote a Stirling number of the second kind, with \(\left\{\begin{smallmatrix}0\\0\end{smallmatrix}\right\}=1\). Then there is a canonical finite product decomposition (with coordinates indexed by endpoint-marked ordered equality types of valuations)
\[
\boxed{F_{\mathcal V}(k)\cong\prod_{r=0}^{k}C_{r+2}^{\,T_{k,r}}.}
\]
In particular,
\[
\boxed{|F_{\mathcal V}(k)|=\prod_{r=0}^{k}(r+2)^{T_{k,r}}.}
\]
Thus \(F_{\mathcal V}(1)\cong C_2^2\times C_3\), of cardinality \(12\), and \(F_{\mathcal V}(2)\cong C_2^4\times C_3^5\times C_4^2\), of cardinality \(62\,208\). Every independent selection of one of the ordered input values or the endpoints on each equality type is represented by a formula in the full bi-Heyting language.

The single chain \(C_{k+2}\) detects every nonidentity between \(k\)-variable terms throughout \(\mathcal V\). No chain with fewer than \(k+2\) elements has this universal testing property. This finite-test observation is recorded as a companion to the normal form, rather than asserted as the new contribution by itself.

## Assumptions and scope
For a bounded linear order, use precisely the operations
\[
a\to b=\begin{cases}1,&a\le b,\\b,&a>b,\end{cases}\qquad
a\setminus b=\begin{cases}0,&a\le b,\\a,&a>b.\end{cases}
\]
Also \(a\wedge b=\min(a,b)\), \(a\vee b=\max(a,b)\). The product decomposition concerns **term functions modulo equality in all bounded finite chains**, equivalently equality in their generated variety. It does not assert the same result for all bi-Heyting algebras or all bi-Gödel algebras whose dual orders branch.

An endpoint-marked ordered equality type \(\tau\) of a \(k\)-tuple records all comparisons and equalities among \(0,x_1,\ldots,x_k,1\), with \(0<1\). If exactly \(r\) distinct interior values occur, the ordered values present in this type form a chain of \(r+2\) values. Every type is realized in \(C_{k+2}\).

## Proof
**1. Selection property.** On a chain, each primitive operation selects either one of its input values or an endpoint. By induction on terms, the value of every \(k\)-variable term is one of \(0,1,x_1,\ldots,x_k\). The identity of this selected value depends only on \(\tau\), because all primitive branching decisions are comparisons between selected inputs. Thus restriction to a fixed \(\tau\) determines a coordinate in \(C_{r+2}\).

**2. Sharp comparisons are definable.** Define the term
\[
D(a,b)=1\setminus(a\to b).
\]
Direct substitution into the displayed chain operations shows that \(D(a,b)=1\) exactly if \(a>b\), and \(D(a,b)=0\) otherwise. Its negation \(D(a,b)\to0\) is therefore the crisp test of \(a\le b\). For a type \(\tau\), form \(\chi_\tau\) by taking, for each ordered pair among \(0,x_1,\ldots,x_k,1\), the factor \(D(a,b)\) if \(a>b\) holds in \(\tau\), and \(D(a,b)\to0\) if it does not. Their finite meet equals \(1\) exactly on valuations of type \(\tau\), and \(0\) otherwise. For each type, choose a representative \(s_\tau\) among \(0,1,x_1,\ldots,x_k\) having the desired value at that type. The term
\[
\bigvee_{\tau}\bigl(\chi_\tau\wedge s_\tau\bigr)
\]
selects \(s_\tau\) independently at every type. Therefore the evaluation map from the term algebra onto the product of these finite coordinate chains is surjective. It is injective modulo the identities of \(\mathcal V\), since every type is realized in a member of the generating class. All coordinate operations agree with the bi-Heyting chain operations, establishing the stated algebra isomorphism.

**3. Coordinate multiplicities.** To have exactly \(r\) ordered interior values, first choose \(m\) of the \(k\) named variables that take interior values, in \(\binom{k}{m}\) ways. Assign each of the other \(k-m\) variables one of the two endpoints, in \(2^{k-m}\) ways. Finally partition the \(m\) variables surjectively into \(r\) nonempty interior value-classes and linearly order these classes, in \(r!\left\{\begin{smallmatrix}m\\r\end{smallmatrix}\right\}\) ways. Summation over \(m\) gives \(T_{k,r}\). Independent coordinates yield the cardinality product.

**4. Exact finite test and its boundary.** Every term evaluation in any chain uses only the endpoint-marked type of at most \(k\) interior values; it is reproduced in \(C_{k+2}\). Thus an equation in \(k\) variables holds in \(C_{k+2}\) iff it holds in every chain and hence in \(\mathcal V\). Conversely, put
\[
\theta_k=D(x_1,0)\wedge D(1,x_k)\wedge\bigwedge_{i=1}^{k-1}D(x_{i+1},x_i).
\]
For \(k=1\), interpret the empty meet as \(1\). The term \(\theta_k\) is nonzero precisely when \(0<x_1<\cdots<x_k<1\). Consequently, the equation \(\theta_k\approx0\) holds in every chain of size at most \(k+1\), but fails in \(C_{k+2}\). This proves sharpness **among single finite-chain equational tests**.

## Verification
The accompanying self-contained Python checker uses integer representatives of the finite chain operations, independently generates all endpoint-marked order types for \(k=1,2,3\), verifies their multiplicities \((2,1)\), \((4,5,2)\), and \((8,19,18,6)\), and checks the strict-comparison indicator for every tested valuation. It checks that every type has a crisp characteristic formula, enumerates all \(62\,208\) independent two-variable profiles, verifies closure counts of \(4,12,12,12\) for one variable over \(C_2,C_3,C_4,C_5\), and tests the strict-chain witness for \(k=1,2,3\). Run \(\texttt{python3 checker.py}\); expected status: \(\texttt{ALL\_CHECKS\_OK}\). These finite tests corroborate the symbolic proof, but do not substitute for the proof for arbitrary \(k\).

## Relationship to prior work
Martins, *There are only countably many locally tabular bi-intermediate logics of co-trees* (arXiv:2602.21960v1, February 25, 2026), places the logic of chains within a locally tabular variety of bi-Gödel algebras. Bezhanishvili, Martins, and Moraschini, *Bi-intermediate logics of trees and co-trees* (arXiv:2211.14776), identify the variety generated by linear bi-Heyting algebras and its dual characterization. Those results supply the broader logical setting, not the explicit coordinate-by-coordinate free algebra decomposition and exact multiplicities proved here.

Carai's *Free algebras and coproducts in varieties of Gödel algebras* (arXiv:2406.05480) characterizes free Gödel **Heyting** algebras and shows their algebras also carry co-Heyting operations. The universal property in the **expanded** bi-Heyting signature is different; the present argument explicitly uses co-implication to define sharp order comparisons and independent selectors. The separately known order-type/finite-testing phenomenon for Heyting Gödel chains is not presented as a priority claim. The 2026 paper of Badia, Kowalski, and Olkhovikov discusses expressive power in general bi-intuitionistic logic, not these finite-chain term counts.

## Limitations
The theorem is specific to the variety generated by bounded chains, with co-implication included in the language. It does not enumerate terms in free bi-Gödel algebras on branching co-trees, free Gödel algebras in the smaller Heyting signature, or arbitrary non-chain bi-Heyting algebras. The available literature comparison does not exclude every historically equivalent treatment under other terminology; independent expert or archival review has not been performed.

## References
1. M. Martins, *There are only countably many locally tabular bi-intermediate logics of co-trees*, arXiv:2602.21960v1, February 25, 2026. https://arxiv.org/abs/2602.21960
2. N. Bezhanishvili, M. Martins, T. Moraschini, *Bi-intermediate logics of trees and co-trees*, arXiv:2211.14776, November 27, 2022. https://arxiv.org/abs/2211.14776
3. L. Carai, *Free algebras and coproducts in varieties of Gödel algebras*, arXiv:2406.05480v1, June 8, 2024. https://arxiv.org/abs/2406.05480
4. G. Badia, T. Kowalski, G. Olkhovikov, *Definable Classes of Models and Frames in Bi-intuitionistic Logic*, arXiv:2607.18956v1, July 21, 2026. https://arxiv.org/abs/2607.18956
