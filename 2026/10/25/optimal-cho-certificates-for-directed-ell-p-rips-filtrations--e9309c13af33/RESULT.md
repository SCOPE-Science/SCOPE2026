# Optimal Cho certificates for directed \(\ell_p\) Rips filtrations

## Finding

**Theorem.** Let \(V\) be any set and let \(G:V\times V\to[0,\infty]\) be any directed dissimilarity with \(G(v,v)=0\) for every \(v\in V\). No symmetry or triangle inequality is imposed. For every \(p\in(0,\infty]\), all scales \(t\in[0,\infty]\), and every simplicial degree \(n\ge0\), the ordered-tuple monoidal Rips and Cho nerve constructions agree **as actual simplicial subsets**:
\[
R_{+_p}^{t}(G)=N_{+_p}^{t}(G)\subseteq EV.
\]
For finite \(p\), the exact filtration value of an ordered tuple \(y=(v_0,\ldots,v_n)\) with finite forward pair weights is computable by a longest-path recurrence. Put \(A_{ij}=G(v_i,v_j)^p\) for \(0\le i<j\le n\), \(D_0=0\), and
\[
D_j=\max_{0\le i<j}\bigl(D_i+A_{ij}\bigr)\quad(1\le j\le n).
\]
Then both constructions assign filtration value \(D_n^{1/p}\) to \(y\). Moreover, the explicit Cho parameters
\[
r_j=(D_j-D_{j-1})^{1/p},\qquad 1\le j\le n,
\]
attain the minimum possible \(\ell_p\)-norm. The recurrence and certificate use \(O(n^2)\) arithmetic operations and \(O(n)\) auxiliary storage.

This repairs the claimed separation for directed weights in Example 3.6 of Blaser–Brun–Gardaa–Salbu: its stated four-vertex counterexample is actually a Cho simplex at the claimed scale.

## Assumptions and scope

For \(0<p<\infty\) define the monoidal operation \(a+_p b=(a^p+b^p)^{1/p}\), with the extended-real conventions at infinity; for \(p=\infty\) put \(a+_\infty b=\max(a,b)\). Both operations are associative, commutative, order-preserving and have neutral element zero. The usual sources consider \(p\ge1\); the statement includes \(0<p<1\) because the argument requires only positivity of the exponent, not the norm triangle inequality.

The \(n\)-simplices of \(EV\) are tuples \(y=(v_0,\ldots,v_n)\), including repetitions. In the monoidal Rips filtration, \(y\) is present at scale \(t\) when every strictly increasing index subsequence \(i_0<\cdots<i_m\) obeys
\[
G(v_{i_0},v_{i_1})+_p\cdots+_pG(v_{i_{m-1}},v_{i_m})\le t.
\]
The empty product is zero. This is equivalent to testing every order-preserving map of indices: extra repeated indices introduce only zero diagonal weights. In Cho's nerve, \(y\) is present when there exist \(r_1,\ldots,r_n\in[0,\infty]\) with
\[
\bigl(+_p\bigr)_{j=1}^{n}r_j\le t,\qquad
G(v_i,v_j)\le\bigl(+_p\bigr)_{k=i+1}^{j}r_k
\quad(0\le i<j\le n).
\]
Here iterated \(+_p\) denotes the finite iterated monoidal product, not ordinary addition except when \(p=1\). The diagonal conditions hold by hypothesis. All statements refer to the inclusive (\(\le\)) filtration. They do not concern arbitrary monoidal lattices, or dissimilarities with nonzero diagonal.

## Proof

Fix first \(0<p<\infty\), a tuple of length \(n+1\ge2\), and a finite target scale \(t\). If one of its forward pair weights is infinite, the pair subsequence alone excludes the tuple from Rips, while any finite-total Cho certificate also excludes it. Thus suppose all forward weights are finite and set \(A_{ij}=G(v_i,v_j)^p\ge0\).

**Step 1 (exact Rips grade).** For each \(j\), the recurrence \(D_j=\max_{i<j}(D_i+A_{ij})\) computes the maximum total \(A\)-weight of all strictly increasing paths starting at index zero and ending at index \(j\). This follows inductively by splitting a path at its penultimate index. Because the weights are nonnegative, any increasing subsequence may be extended to start at zero and end at \(n\) without reducing its weight. Hence the maximum \(p\)-th power of the \(+_p\) length over *all* increasing subsequences is exactly \(D_n\). The Rips filtration value is \(D_n^{1/p}\).

**Step 2 (optimal Cho certificate).** The recurrence and \(A_{ij}\ge0\) give \(D_j\ge D_{j-1}\), by taking \(i=j-1\); so \(B_j=D_j-D_{j-1}\ge0\). For any \(i<j\), the recurrence implies \(D_j\ge D_i+A_{ij}\). Therefore
\[
A_{ij}\le D_j-D_i=\sum_{k=i+1}^{j}B_k.
\]
Taking \(p\)-th roots gives the required interval inequalities for \(r_j=B_j^{1/p}\). Their total \(+_p\)-length has \(p\)-th power \(\sum_{j=1}^{n}B_j=D_n\), attaining the Rips grade. Thus every Rips tuple has a Cho certificate at the same scale.

**Step 3 (reverse inclusion and sharpness).** Given *any* Cho parameters \(r_j\) for the tuple, take an increasing subsequence \(i_0<\cdots<i_m\). The pairwise interval inequalities and disjointness of the intervals imply
\[
\sum_{k=0}^{m-1}G(v_{i_k},v_{i_{k+1}})^p
\le\sum_{k=0}^{m-1}\sum_{h=i_k+1}^{i_{k+1}}r_h^p
\le\sum_{h=1}^{n}r_h^p.
\]
Maximizing over subsequences proves the Rips grade is at most every Cho certificate's total length. Combined with Step 2 this proves equality of optimal values and filtrations.

**Step 4 (boundaries).** For \(p=\infty\), both constructions have exact grade \(\max_{i<j}G(v_i,v_j)\): the reverse inclusion follows from the interval maxima, and the forward inclusion uses \(r_j\) equal to the maximum forward pair weight. At scale \(t=\infty\), every tuple belongs to both constructions (for positive dimension, take all \(r_j=\infty\)). In degree zero, the zero diagonal ensures that every vertex belongs to both at every nonnegative scale. This also covers the case of an empty vertex set vacuously. Hence the equality holds in every degree and at every scale, not merely up to homotopy.

## Verification

The bundled `verify.py` uses an **independent, direct subsequence enumeration** to obtain the Rips grade and compares it with the recurrence. For small integer \(p\)-power matrices it independently exhausts all nonnegative integer Cho parameter vectors up to the Rips grade and confirms the optimal integer value; the theorem itself gives optimality over **all real** parameter vectors. It tests 1,510 matrices, including every \(3\)-symbol upper-triangular matrix through length four and seeded samples through length seven. Additional numeric checks for exponents below and above one were made; these are finite sanity checks, not the proof of the universal theorem.

In the four-vertex directed graph of Blaser–Brun–Gardaa–Salbu, Example 3.6, the specified forward weights are
\[
G(v_0,v_1)=1,\quad G(v_0,v_2)=3,\quad G(v_0,v_3)=4,\quad
G(v_1,v_2)=3,\quad G(v_1,v_3)=3,\quad G(v_2,v_3)=1.
\]
With \(p=2\), the recurrence gives \((D_0,D_1,D_2,D_3)=(0,1,10,16)\). Thus
\[
(r_1,r_2,r_3)=(1,3,\sqrt6),\qquad r_1^2+r_2^2+r_3^2=16.
\]
The six required pair bounds are respectively \(1\le1\), \(3\le\sqrt{10}\), \(4\le4\), \(3\le3\), \(3\le\sqrt{15}\), and \(1\le\sqrt6\). The purported counterexample therefore lies in both filtrations at radius four. The published exclusion argument reverses the inequality implied by its second pair bound: \(3\le\sqrt{r_1^2+r_2^2}\) yields \(r_1^2+r_2^2\ge9\), not \(\le9\).

## Relationship to prior work

Cho's nerve construction and its interval parameterization originate in Cho's *Quantales, persistence, and magnitude homology*, Proposition 13 (2019 preprint). Ivanov–Xu's *On \(\ell_p\)-Vietoris–Rips complexes*, Proposition 2.6 (2024 preprint), proves equality with Cho's nerve on **metric spaces**. Indeed, their inductive parameter proof is very close and appears to use no symmetry or triangle inequality; the present proof instead states the full directed, triangle-free extension explicitly, provides an exact longest-path formula and optimal certificate, and diagnoses a subsequently published counterexample assertion.

Blaser–Brun–Gardaa–Salbu's *Monoidal Rips: stable multiparameter filtrations of directed networks* (first posted 18 March 2025; journal 2026) introduces monoidal Rips on directed weighted graphs, establishes the always-valid inclusion of Cho's nerve in monoidal Rips, and asserts in Example 3.6 that the reverse inclusion fails even for \(+_2\). The theorem proves the reverse inclusion on the whole \(+_p\) family and gives a concrete certificate for their own instance. It does **not** assert equality for other monoidal products in arbitrary lattices.

## Limitations

The proof is a statement about \(+_p\) on the extended nonnegative reals, with zero diagonal. It does not characterize which other commutative monoidal lattices have the same equality, establish new stability bounds, or classify nonzero-diagonal cases. The recurrence is a standard longest-path calculation on an acyclic index graph; the new conclusion is its precise interpretation as a universally optimal Cho certificate for arbitrary directed networks. Prior metric-space proofs are close enough that independent appraisal should examine whether this extension and its correction of the explicit directed counterexample meet a separate novelty threshold.

## References

1. S. Cho, *Quantales, persistence, and magnitude homology*, arXiv:1910.02905 (first submitted 7 October 2019), Proposition 13. https://arxiv.org/abs/1910.02905
2. S. O. Ivanov and X. Xu, *On \(\ell_p\)-Vietoris–Rips complexes*, arXiv:2411.01857 (first submitted 4 November 2024), Proposition 2.6. https://arxiv.org/abs/2411.01857 ; journal DOI: 10.1007/s41468-026-00247-x.
3. N. Blaser, M. Brun, O. H. Gardaa, and L. M. Salbu, *Monoidal Rips: stable multiparameter filtrations of directed networks*, arXiv:2503.14019 (first submitted 18 March 2025), Definition 3.1 and Examples 3.5–3.6; *Journal of Applied and Computational Topology* 10, article 6 (2026), DOI: 10.1007/s41468-026-00237-z.
