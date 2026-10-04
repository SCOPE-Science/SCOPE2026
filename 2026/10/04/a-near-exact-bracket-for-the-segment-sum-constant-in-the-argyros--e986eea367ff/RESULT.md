# A near-exact bracket for the segment-sum constant in the Argyros–Motakis tree norm
## Finding
Let \(T\) be the dyadic tree identified with \(\mathbb N\) by \(V(n,i)=2^n+i\), and let \(X_\alpha\) be the Banach space defined by Argyros and Motakis in arXiv:2609.31276v1. For a nonempty finite segment \(s\subset T\), put
\[
x_s=\sum_{n\in s}e_n,
\qquad
C_{\rm seg}=\sup_s\|x_s\|_\alpha.
\]
Then
\[
C_0\le C_{\rm seg}\le C_1,
\]
where
\[
C_0=\left(1+\frac1{9}+\frac1{1089}\right)^{1/2}
=1.054528038866988820252943\ldots
\]
and
\[
C_1=\left(1+\frac1{9}+\frac1{1089}+\frac{4^{-37}}3\right)^{1/2}.
\]
In particular,
\[
0\le C_1-C_0<8.368\times10^{-24}.
\]
Thus the published uniform estimate \(1\le\|x_s\|_\alpha\le2\) can be replaced by a bracket determining its optimal universal segment-sum constant to more than twenty decimal places.

## Assumptions and scope
The norm, tree labelling, comparable and incomparable averages, restriction operation, and very-fast-growing condition are exactly those of Sections 2.2--2.4 of arXiv:2609.31276v1. If \(\beta_j^*\) is a generator, write \(s_j=s(\beta_j^*)\) and \(h_j=\max\operatorname{supp}(\beta_j^*)\). A successive family is very fast growing when
\[
s_{j+1}>2^{h_j}.
\]
The claim concerns only the optimal constant for sums of the canonical basis vectors over finite tree segments. It does not alter any qualitative structural theorem about \(X_\alpha\), its dual, or its bidual.

## Proof
Fix a finite segment \(s\), set \(x=x_s\), and take a norming functional
\[
x^*=\sum_i\lambda_i\alpha_i^*\in G,
\qquad
\sum_i\lambda_i^2\le1,
\]
where \(\alpha_i^*=\beta_i^*|_{I_i}\) and the generators \(\beta_i^*\) form a very-fast-growing family. Delete generators whose restricted supports miss \(s\), and reindex the remaining terms. A subfamily of a very-fast-growing family is still very fast growing. The proof of Proposition 3.1 in the source gives, for every remaining term,
\[
a_i:=|\alpha_i^*(x)|\le \frac1{s_i}.
\]
For the first remaining generator, \(a_1\le1\) and \(h_1\ge1\). Hence \(s_2>2^{h_1}\ge2\), so \(s_2\ge3\) and
\[
a_2\le\frac13.
\]
We next show \(h_2\ge5\). If \(s_2\ge4\), successiveness gives at least four distinct integer support coordinates strictly larger than \(h_1\ge1\), hence \(h_2\ge5\). If \(s_2=3\), the generator cannot be a comparable average because comparable averages have even size. It is therefore an incomparable average on three pairwise incomparable tree nodes. Among the labels \(2,3,4\), the nodes \(2\) and \(4\) are comparable, so three pairwise incomparable nodes with labels greater than \(1\) cannot all lie below \(5\). Again \(h_2\ge5\).

Consequently \(s_3>2^{h_2}\ge32\), so \(s_3\ge33\) and
\[
a_3\le\frac1{33}.
\]
The support of the third generator contains \(s_3\) distinct integer coordinates after the second support, hence
\[
h_3\ge h_2+s_3\ge38.
\]
For later generators, Proposition 3.1 gives \(a_i<2^{-h_{i-1}}\). The numbers \(h_i\) are strictly increasing integers, so
\[
\sum_{i\ge4}a_i^2
<\sum_{r=38}^{\infty}4^{-r}
=\frac{4^{-37}}3.
\]
If \(s_2=3\) this yields
\[
\sum_i a_i^2\le1+\frac19+\frac1{1089}+\frac{4^{-37}}3.
\]
If \(s_2\ge4\), the second term improves to \(a_2^2\le1/16\), so the same displayed bound still holds. Cauchy--Schwarz now gives
\[
|x^*(x)|\le
\left(\sum_i\lambda_i^2\right)^{1/2}
\left(\sum_i a_i^2\right)^{1/2}
\le C_1.
\]
Taking the supremum over \(G\) proves \(C_{\rm seg}\le C_1\).

For the lower bound, use the leftmost segment
\[
s_0=\{1,2,4,8,16,32,64\}.
\]
Consider the three generators
\[
\beta_1^*=e_1^*,
\qquad
\beta_2^*=\frac{e_3^*+e_4^*+e_5^*}{3},
\qquad
\beta_3^*=\frac1{33}\sum_{n=64}^{96}e_n^*.
\]
The nodes \(3,4,5\) are pairwise incomparable, and the nodes \(64,\ldots,96\) all lie on the same tree level and are pairwise incomparable. The supports are successive, with \(h_1=1\), \(h_2=5\), and sizes \(1,3,33\). Therefore
\[
3>2^1,
\qquad
33>2^5,
\]
so the family is very fast growing. Restrict the three generators to the singleton intervals \(\{1\}\), \(\{4\}\), and \(\{64\}\). With
\[
(\lambda_1,\lambda_2,\lambda_3)
=\frac{(1,1/3,1/33)}{C_0},
\]
the coefficient vector has Euclidean norm one, hence the resulting functional belongs to \(G\). Its value at \(x_{s_0}\) is exactly \(C_0\). Thus \(\|x_{s_0}\|_\alpha\ge C_0\), proving the lower bound.

## Verification
The proof uses only the published definitions of the two average classes, the very-fast-growing inequality, closure of the norming set under interval restrictions, and the pointwise estimate in Proposition 3.1. The lower witness is finite and explicit. The accompanying script `artifacts/verify_segment_bound.py` checks the tree relations for the witness, the two very-fast-growing inequalities, and the high-precision numerical endpoints from the exact formulas.

The upper estimate is infinite-dimensional but not experimental: the only infinite tail is bounded by the convergent geometric series \(\sum_{r=38}^{\infty}4^{-r}=4^{-37}/3\). No finite computation is used as a substitute for this proof.

## Relationship to prior work
Argyros and Motakis prove in Proposition 3.1 that every nonempty finite segment satisfies
\[
1\le\|x_s\|_\alpha\le2.
\]
Their proof already contains the key estimate \(|\alpha_i^*(x_s)|\le1/s(\beta_i^*)\), but it bounds the evaluations first in \(\ell_1\) before applying Cauchy--Schwarz. Keeping the evaluation vector in \(\ell_2\), and exploiting the first two forced size jumps of a very-fast-growing family, yields the much smaller upper bound above. The explicit three-generator witness supplies a nearly matching lower bound.

Targeted searches for the paper title together with “segment sum”, “sharp constant”, “Proposition 3.1”, “very fast growing”, and the numerical value found the source paper but no statement giving this bracket or a stronger segment-sum constant. Searches of the indexed research records for the same object and parameter likewise returned no covering claim.

## Limitations
The exact value of \(C_{\rm seg}\) is not proved. The certified gap is smaller than \(8.368\times10^{-24}\), but it is nonzero. The upper bound deliberately uses only coarse information after the third generator; further combinatorics of antichains and the fixed tree labelling could in principle close the remaining gap. The source is very recent, so an unindexed independent sharpening remains a residual originality risk.

## References
Spiros A. Argyros and Pavlos Motakis, “Explicitly Defined Norms on \(JT_*\) Spaces,” arXiv:2609.31276v1, first public 2026-09-25. In particular, Sections 2.2--2.4 and Proposition 3.1.
