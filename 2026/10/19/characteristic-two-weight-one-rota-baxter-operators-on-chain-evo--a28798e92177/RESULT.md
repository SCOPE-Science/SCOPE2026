# Characteristic-two weight-one Rota–Baxter operators on chain evolution algebras

## Finding
Let \(K\) be **any field of characteristic \(2\)**, and let \(n\geq2\). Let \(E_n(K)\) be the \(n\)-dimensional evolution algebra with natural basis \(e_1,\ldots,e_n\), satisfying \(e_i e_j=0\) for \(i\ne j\), \(e_i^2=e_{i+1}\) for \(i<n\), and \(e_n^2=0\). Write \(Q(x)=x^2\), where the square is the evolution-algebra product.

**Classification.** Every weight-one Rota–Baxter operator \(R:E_n(K)\to E_n(K)\) is uniquely determined by \(v=R(e_1)=\sum_{r=1}^{n}a_r e_r\), and its remaining columns are \(R(e_i)=Q^{i-1}(v)\). The admissible coefficient vectors are **exactly** the following disjoint types:

1. **Zero-middle type:** \(a_2=\cdots=a_{n-1}=0\), with \(a_1,a_n\in K\) arbitrary.
2. **Periodic-support types:** choose a unique \(j\in\{2,\ldots,n-1\}\), \(u\in K^\times\), \(a_1\in\{0,1\}\), and \(a_n\in K\). Set \(L=j-1\). For each \(r\in\{2,\ldots,n-1\}\), set \(a_r=0\) unless \(r=1+\ell L\) for some integer \(\ell\geq1\); in that case set
   \[
   a_{1+\ell L}=u^{\,\sum_{s=0}^{\ell-1}2^{sL}}.
   \]
   The displayed rule is applied only when \(1+\ell L\leq n-1\).

In particular, if \(K=\mathbb F_q\), where \(q=2^f\) and \(f\geq1\), the **exact number** of weight-one Rota–Baxter operators is
\[
\boxed{\ |\operatorname{RB}_{1}(E_n(\mathbb F_q))|=q^2+2(n-2)q(q-1).\ }
\]
Their ranks have the complete distribution
\[
\boxed{\quad N_0=1,\quad N_1=q-1,\quad
N_r=q(q-1)\ (2\leq r<n),\quad N_n=(n-1)q(q-1).\quad}
\]
The intermediate range is empty for \(n=2\). Each formula counts \(K\)-linear operators, not conjugacy orbits.

## Assumptions and scope
The ground field has characteristic exactly \(2\), with no perfectness or finiteness assumption for the classification. The evolution algebra is the **unperturbed chain** shown above; assertions are not made for all maximal-nilindex evolution algebras with additional upper-triangular structure constants. Operators are linear and satisfy the weight-one identity
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)+xy\bigr)
\quad\text{for all }x,y\in E_n(K).
\]
The algebra is generally nonassociative; no associativity of iterated products is presumed. The operator \(Q\) denotes a *single squaring map*, and its iterates are explicitly parenthesized by composition.

## Proof
**Step 1 (columns forced by characteristic two).** In this commutative algebra, \(Q(x+y)=Q(x)+Q(y)\) and \(Q(cx)=c^2Q(x)\). On substituting \(x=y=e_i\) in the Rota–Baxter identity, the two cross terms cancel in characteristic two, giving
\[
Q(R(e_i))=R(e_{i+1})\quad(1\leq i<n),
\qquad Q(R(e_n))=0.
\]
Since \(Q^n=0\) on the entire algebra, every operator satisfying the identity has \(R(e_i)=Q^{i-1}(v)\), where \(v=R(e_1)\), and conversely the diagonal basis identities hold for any \(v\). The coefficient of \(e_k\) in \(R(e_i)\) is \(a_{k-i+1}^{2^{i-1}}\) for \(k\geq i\), and zero for \(k<i\). Thus the \(e_n\)-coefficient \(a_n\) of \(v\) is unrestricted by subsequent columns.

**Step 2 (exact off-diagonal equations).** Because both sides of the Rota–Baxter identity are bilinear in \(x,y\), the basis-pair equations are necessary and sufficient. For \(i<j\), the product \(R(e_i)R(e_j)\) has \(e_{k+1}\)-coefficient \(a_{k-i+1}^{2^{i-1}}a_{k-j+1}^{2^{j-1}}\) for \(j\leq k<n\). The right-hand side is \(a_{j-i+1}^{2^{i-1}}R(e_{j+1})\), since the \(e_i\)-coefficient in \(R(e_j)\) vanishes. Coefficient comparison, using injectivity of every Frobenius power in a field, yields the exact system
\[
\tag{*}
a_{t+d}a_t^{2^d}=a_{d+1}a_t^{2^{d+1}}
\quad\text{for }d\geq1,\ t\geq1,\ t+d\leq n-1.
\]
Every pair \((d,t)\) in this range occurs by taking \(i=1\), \(j=d+1\), and \(k=d+t\); hence there are no omitted constraints. The component \(a_n\) never appears in \((*)\).

**Step 3 (classification of solutions).** If \(a_2=\cdots=a_{n-1}=0\), every equation \((*)\) holds and \(a_1,a_n\) are arbitrary. Otherwise let \(j\) be the smallest index in \(\{2,\ldots,n-1\}\) with \(a_j\ne0\), and put \(u=a_j\). Taking \(t=1\) and \(d=j-1\) in \((*)\), and cancelling \(u\), shows \(a_1^{2^{j-1}}=a_1^{2^j}\), which in a characteristic-two field forces \(a_1\in\{0,1\}\). Taking \(t=j\) and dividing \((*)\) by \(u^{2^d}\) gives
\[
a_{j+d}=a_{d+1}u^{2^d}\qquad(1\leq d\leq n-j-1).
\]
With \(L=j-1\), this recurrence is \(a_r=a_{r-L}u^{2^{r-j}}\) for \(j<r<n\). Since \(a_2,\ldots,a_{j-1}=0\), induction forces zero coefficients except at \(r=1+\ell L\) and the stated geometric-Frobenius exponent at every such index.

Conversely, the listed coefficient vectors satisfy \((*)\). For \(t=1\) this follows because \(a_1=0\) or \(1\). For \(t\geq2\), the equation is trivial when \(a_t=0\). If \(a_t\ne0\), write \(t=1+hL\) with \(h\geq1\). When \(d\) is not a multiple of \(L\), both \(a_{t+d}\) and \(a_{d+1}\) vanish. When \(d=kL\), both nonzero sides agree because the geometric exponent sums concatenate:
\[
\sum_{s=0}^{h+k-1}2^{sL}=
\sum_{s=0}^{k-1}2^{sL}
+2^{kL}\sum_{s=0}^{h-1}2^{sL}.
\]
This proves sufficiency and uniqueness for all characteristic-two fields.

**Step 4 (count and rank).** Over \(\mathbb F_q\), the zero-middle family has \(q^2\) vectors. There are \(n-2\) possible indices \(j\), each with \((q-1)\cdot2\cdot q\) parameter choices, all disjoint. This proves the total count. Since the operator is upper triangular with diagonal \(a_1,a_1^2,\ldots,a_1^{2^{n-1}}\), it is invertible exactly when \(a_1\ne0\). The zero-middle family contributes \(q(q-1)\) invertible operators, and each of the \(n-2\) other families contributes \(q(q-1)\) with \(a_1=1\). The zero map is unique; the remaining zero-middle maps with \(a_1=0\) have rank one exactly when \(a_n\ne0\). For a periodic-support family with \(a_1=0\), the successive nonzero columns begin at rows \(j,j+1,\ldots,n\), so their rank is exactly \(n-j+1\). Hence each rank from \(2\) through \(n-1\) occurs exactly \(q(q-1)\) times, completing the distribution.

## Verification
The accompanying standalone script `verify.py` uses explicit polynomial arithmetic over \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\). It independently enumerates all possible first columns, constructs every forced linear map, tests every basis-pair Rota–Baxter identity, computes matrix ranks by finite-field elimination, and compares the resulting sets and histograms with the classification. It passes for \(2\leq n\leq8\) over \(\mathbb F_2\), \(2\leq n\leq6\) over \(\mathbb F_4\), \(2\leq n\leq5\) over \(\mathbb F_8\), and \(2\leq n\leq4\) over \(\mathbb F_{16}\) (19 configurations). These finite checks are not the proof of the arbitrary-field theorem; the proof is Steps 1–4 above.

## Relationship to prior work
Qaralleh, Mukhamedov and Khakimov (arXiv:2601.08669, first version January 13, 2026) study weight-zero and weight-one operators on maximal-nilindex evolution algebras **under their explicit characteristic-zero hypothesis**. Their triangular structure and rational diagonal recurrence do not classify the characteristic-two locus. Their follow-up (arXiv:2606.22623) concerns pointwise-local **weight-zero** operators over characteristic-zero fields. The present calculation isolates a different field characteristic and weight, and classifies an exact infinite-dimensional family of examples \(E_n(K)\) across all \(n\), including finite-field ranks and cardinalities. The classification is not claimed for arbitrary perturbations of the evolution-chain multiplication. Related classifications of weight-zero operators on associative exterior algebras likewise concern different products and weights.

## Limitations
The full classification is restricted to the unperturbed chain evolution algebras and to weight one in characteristic two. No assertion about characteristic-zero or odd-characteristic fields, about weight zero, or about general upper-triangular perturbations is made. The formulas count raw linear maps, not equivalence classes under automorphisms. Computations cover the enumerated finite examples only. Prior literature could contain an unindexed equivalent characteristic-two treatment; independent bibliographic and mathematical review remain appropriate.

## References
1. I. Qaralleh, F. Mukhamedov and O. Khakimov, *Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669 (2026), initial version January 13, 2026; author-posted full manuscript available at https://www.researchgate.net/publication/399754899_Rota-Baxter_operators_of_nilpotent_evolution_algebras_with_maximal_nilindex.
2. I. Qaralleh, F. Mukhamedov and O. Khakimov, *Local Rota--Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex*, arXiv:2606.22623 (2026); author-posted full manuscript available at https://www.researchgate.net/publication/407507209_Local_Rota--Baxter_operators_of_weight_zero_on_nilpotent_evolution_algebras_with_maximal_nilindex.
