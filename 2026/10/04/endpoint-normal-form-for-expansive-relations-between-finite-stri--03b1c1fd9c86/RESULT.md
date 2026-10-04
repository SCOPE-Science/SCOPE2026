# Endpoint normal form for expansive relations between finite strict chains
## Finding

For integers \(m,n\ge 1\), let
\[
C_m=(\{0,\ldots,m-1\},<),\qquad C_n=(\{0,\ldots,n-1\},<),
\]
where \(<\) is the strict transitive relation. For \(R\subseteq C_m\times C_n\), write
\[
R_i=\{j\in C_n:iRj\}.
\]
Call \(R\) total when every \(R_i\) is nonempty, and expansive when it is both forward and backward confluent in the sense of Fernández-Duque.

Then \(R\) is total and expansive if and only if
\[
a_i=\min R_i,\qquad b_i=\max R_i
\]
exist for every row and satisfy
\[
a_0<a_1<\cdots<a_{m-1},\qquad b_0<b_1<\cdots<b_{m-1}.
\]

Consequently, total expansive relations \(C_m\to C_n\) exist exactly when \(m\le n\). Every such relation satisfies the sharp bounds
\[
m\le |R|\le m(n-m+1).
\]
The upper bound is attained by a unique relation:
\[
R_i=\{i,i+1,\ldots,i+n-m\}\qquad(0\le i<m).
\]
The lower bound is attained exactly by functional expansive relations. These are precisely the strictly increasing maps \(C_m\to C_n\), so there are
\[
\binom{n}{m}
\]
of them.

The exact number of all total expansive relations is
\[
E_{m,n}=
\sum_{\substack{
0\le a_0<\cdots<a_{m-1}<n\\
0\le b_0<\cdots<b_{m-1}<n\\
a_i\le b_i\ \text{for all }i}}
2^{\sum_{i=0}^{m-1}\max(b_i-a_i-1,0)}
\]
for \(m\le n\), and \(E_{m,n}=0\) for \(m>n\). In particular,
\[
E_{m,m}=1.
\]

## Assumptions and scope

The chains use the strict transitive relation \(<\), not its reflexive closure. Totality is required on the source only; surjectivity onto the target is not assumed.

Forward confluence means: if \(i<j\) and \(iRu\), then some \(v\) satisfies \(jRv\) and \(u<v\). Backward confluence means: if \(i<j\) and \(jRv\), then some \(u\) satisfies \(iRu\) and \(u<v\).

The result is specific to finite strict chains. It does not claim the same endpoint description for branching transitive frames or preorders with nontrivial clusters.

## Proof

Assume \(R\) is total and expansive. Fix \(i<j\). By forward confluence applied to \(b_i\in R_i\), some \(v\in R_j\) satisfies \(b_i<v\), hence
\[
b_i<b_j.
\]
By backward confluence applied to \(a_j\in R_j\), some \(u\in R_i\) satisfies \(u<a_j\), hence
\[
a_i<a_j.
\]
Thus both endpoint sequences are strictly increasing.

Conversely, assume every row is nonempty and both endpoint sequences are strictly increasing. If \(i<j\) and \(u\in R_i\), then
\[
u\le b_i<b_j,
\]
so \(b_j\in R_j\) witnesses forward confluence. If \(i<j\) and \(v\in R_j\), then
\[
a_i<a_j\le v,
\]
so \(a_i\in R_i\) witnesses backward confluence. Hence \(R\) is expansive.

Strict increase of \((a_i)\) forces \(m\le n\). Conversely, if \(m\le n\), the graph \(i\mapsto i\) is total and expansive.

For the upper size bound, strict increase gives
\[
a_i\ge i,\qquad b_i\le n-m+i.
\]
Therefore
\[
|R_i|\le b_i-a_i+1\le n-m+1,
\]
and summing gives \(|R|\le m(n-m+1)\). Equality forces \(a_i=i\), \(b_i=n-m+i\), and every point between the endpoints to lie in the row. Hence the displayed interval relation is the unique maximizer.

The lower bound \(|R|\ge m\) is totality. Equality holds exactly when every row is a singleton. The endpoint criterion then says that the unique target in each row increases strictly, so minimum-size relations are exactly strictly increasing maps, counted by \(\binom{n}{m}\).

Finally, fix admissible endpoint sequences \((a_i)\) and \((b_i)\). If \(a_i=b_i\), there is one row with those endpoints. If \(a_i<b_i\), its two endpoints are forced and each of the \(b_i-a_i-1\) interior points is independently present or absent. Thus the row count is
\[
2^{\max(b_i-a_i-1,0)}.
\]
Multiplying over rows and summing over all admissible endpoint pairs yields the formula for \(E_{m,n}\).

## Verification

The packaged checker exhaustively enumerates every binary relation \(R\subseteq C_m\times C_n\) for \(1\le m,n\le4\). It tests totality, forward confluence, and backward confluence directly from the quantified definitions, independently tests the endpoint characterization, and checks agreement for every relation.

It also verifies the exact weighted endpoint sum, the existence threshold \(m\le n\), the sharp minimum and maximum sizes, uniqueness of the maximum relation, and the count \(\binom{n}{m}\) of minimum-size relations. Running `python verify.py` prints `VERIFY_OK`.

The finite enumeration is only a consistency check; the proof above establishes the theorem for all positive \(m,n\).

## Relationship to prior work

Fernández-Duque introduces expansive relations as relations that are both forward and backward confluent, describes total expansive relations as the bisimulation-invariant analogue of homomorphisms, proves closure properties under unions and composition, and uses them as the relation notion underlying simulations in the Fine-selection proof for intuitionistic \(\mathsf{K4}\). The source does not classify them on finite chains or derive endpoint, extremal-size, or counting formulas.

A related earlier paper by Gabelaia, Kuznetsov, Mihailescu, Razmadze, and Uridia studies surjective bounded morphisms between finite linear temporal structures. That setting is functional and surjective, whereas the theorem here concerns multivalued source-total expansive relations and permits non-surjective targets. The earlier abstract therefore does not imply the endpoint normal form or census.

The classification is also reminiscent of the Egli-Milner two-sided comparison of subsets of a chain, but here the condition is imposed coherently across all rows of one modal-logic relation, producing strict endpoint sequences and sharp global extremal data.

## Limitations

The theorem is specific to finite strict chains. With branching or clusters, minima and maxima need not encode all confluence witnesses. The exact census is a weighted endpoint sum rather than a simpler closed product.

The 2026 motivating preprint was inspected in full text. For the 2024 finite-linear bounded-morphism comparison, accessible metadata and abstract were inspected, but a lawful open full-text copy was not located in the bounded search; this is a residual bibliographic risk, not a mathematical implication gap.

## References

[1] David Fernández-Duque, “Fine Selection for Intuitionistic Modal Logic,” arXiv:2609.27078, first submitted 22 September 2026.

[2] David Gabelaia, Evgeny Kuznetsov, Radu-Casian Mihailescu, Konstantine Razmadze, and Levan Uridia, “Temporal logic of surjective bounded morphisms between finite linear processes,” *Journal of Applied Non-Classical Logics* 34(1), 2024. DOI:10.1080/11663081.2023.2269432.
