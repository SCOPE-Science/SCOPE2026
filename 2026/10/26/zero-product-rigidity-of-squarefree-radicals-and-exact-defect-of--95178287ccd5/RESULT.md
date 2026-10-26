# Zero-product rigidity of squarefree radicals and exact defect of their unitizations

## Finding
For every field \(K\) and every integer \(r\ge 1\), put
\[
A_r=K[x_1,\ldots,x_r]/(x_1^2,\ldots,x_r^2),\qquad
J_r=(x_1,\ldots,x_r)\subset A_r.
\]
Every zero-product-preserving bilinear map on the **nonunital** nilpotent algebra \(J_r\) factors uniquely through multiplication \(J_r\times J_r\to J_r^2\). In particular, \(J_r\) is zero-product determined and has nilpotency index exactly \(r+1\). This holds in all field characteristics.

For the **unital** algebra \(A_r\), the space of universal zero-product-preserving bilinear forms is more complicated. Given any \(K\)-vector space \(V\), every bilinear \(F:A_r\times A_r\to V\) that vanishes whenever its input product vanishes is uniquely of the form
\[
F(a+u,b+v)=ab\,c+L(av)+R(bu)+H(uv),
\]
where \(a,b\in K\), \(u,v\in J_r\), \(c\in V\), \(L,R:J_r\to V\), and \(H:J_r^2\to V\) are linear. Conversely every such choice preserves zero products. It factors through multiplication on \(A_r\) exactly when \(L=R\) and \(H=L|_{J_r^2}\).

Equivalently, writing \(Z_2(B)\) for the linear span in \(B\otimes_K B\) of pure tensors \(s\otimes t\) with \(st=0\), there is a natural vector-space isomorphism
\[
(A_r\otimes_K A_r)/Z_2(A_r)\simeq K\oplus J_r\oplus J_r\oplus J_r^2.
\]
Its dimension is \(3\cdot2^r-r-2\), whereas \(\dim_K A_r=2^r\); thus its multiplication-map kernel has dimension \(2^{r+1}-r-2\). In particular, no \(A_r\) is zero-product determined.

In the symmetric subspace of zero-product-preserving bilinear maps, the factorization defect has dimension \(2^r-r-1\). It vanishes exactly when \(r=1\), and is nonzero for all \(r\ge2\).

Over \(K=\mathbb F_q\), the exact number of scalar-valued zero-product-preserving bilinear maps on \(A_r\) is \(q^{3\cdot2^r-r-2}\), and the number factoring through multiplication is \(q^{2^r}\). The corresponding numbers of symmetric maps are \(q^{2^{r+1}-r-1}\) and \(q^{2^r}\), respectively.

## Assumptions and scope
An associative, possibly nonunital, \(K\)-algebra \(B\) is **zero-product determined** if every bilinear \(F:B\times B\to V\) into any vector space \(V\) with \(st=0\Rightarrow F(s,t)=0\) has the form \(F(s,t)=h(st)\) for some linear map \(h:B^2\to V\), where \(B^2\) means the linear span of all products. The target \(V\) is arbitrary and need not be finite-dimensional. No restriction on field characteristic is imposed. The superscript on \(J_r^d\) denotes the linear span of products of \(d\) elements.

For each subset \(S\subseteq\{1,\ldots,r\}\), let \(x_S=\prod_{i\in S}x_i\), with \(x_\varnothing=1\). The \(x_S\) form a \(K\)-basis of \(A_r\), and
\[
x_Sx_T=\begin{cases}x_{S\cup T},&S\cap T=\varnothing,\\0,&S\cap T\ne\varnothing.\end{cases}
\]
The nonempty subsets index a basis of \(J_r\); subsets of cardinality at least two index a basis of \(J_r^2\). Consequently \(\dim J_r=2^r-1\) and \(\dim J_r^2=2^r-r-1\).

## Proof
**Step 1 (squarefree product classes).** For \(B=J_r\), put \(Z_2=Z_2(B)\). If nonempty sets \(S,T\) intersect, the class of \(x_S\otimes x_T\) in \((B\otimes B)/Z_2\) is zero. For disjoint nonempty sets, write \(U=S\cup T\). The class depends only on \(U\), as follows.

Given two nonempty proper subsets \(S,S'\subsetneq U\) which are incomparable by inclusion, both mixed products in
\[
(x_S+x_{S'})\bigl(x_{U\setminus S}-x_{U\setminus S'}\bigr)=0
\]
vanish individually, while the two diagonal products cancel. Expanding the associated tensor and removing its two zero-product mixed terms proves
\[
[x_S\otimes x_{U\setminus S}]=[x_{S'}\otimes x_{U\setminus S'}].
\]
If instead \(S\subsetneq S'\), choose \(W=U\setminus S'\). Then \(W\) is a nonempty proper subset of \(U\), incomparable with each of \(S\) and \(S'\). Two applications of the preceding identity connect their classes. Equality or reverse inclusion is immediate or analogous. Thus all ordered nontrivial splittings of \(U\) represent one class.

Multiplication sends that class to \(x_U\). Consequently the classes for sets \(|U|\ge2\) span the quotient and have linearly independent images (the distinct squarefree monomials in \(J_r^2\)). Multiplication therefore induces an isomorphism
\[
(J_r\otimes J_r)/Z_2(J_r)\xrightarrow{\sim}J_r^2.
\]
This proves the zero-product determination property, including for arbitrary target vector spaces.

**Step 2 (zero products in the unitization).** Every \(a+u\in A_r\) with \(a\ne0\) is invertible: \(u\) is nilpotent and the finite geometric-series inverse exists. Hence a zero-product pair in \(A_r\) either has a zero factor, or both factors lie in \(J_r\) and have zero product. Under the canonical vector-space decomposition
\[
A_r\otimes A_r\cong(K\otimes K)\oplus(K\otimes J_r)\oplus(J_r\otimes K)\oplus(J_r\otimes J_r),
\]
all zero-product tensors are therefore contained in the final summand, and their span there is exactly \(Z_2(J_r)\). Combining this with Step 1 yields the stated canonical quotient \(K\oplus J_r\oplus J_r\oplus J_r^2\).

**Step 3 (bilinear maps and defects).** Linear maps out of the quotient in Step 2 correspond exactly to tuples \((c,L,R,H)\), and evaluation on pure tensors is precisely the displayed formula. Multiplication sends a tuple's coordinates to \(ab\in K\) and \(av+bu+uv\in J_r\). Since these four components can be independently tested with \((1,1)\), \((1,u)\), \((u,1)\), and \((u,v)\), factorization is equivalent to \(L=R\) and \(H=L|_{J_r^2}\). The quotient has dimension
\[
1+2(2^r-1)+(2^r-r-1)=3\cdot2^r-r-2,
\]
and multiplication surjects onto \(A_r\), so its defect is \(2^{r+1}-r-2\).

Interchanging the inputs swaps \(L\) and \(R\), leaving \(c\) and \(H\) unchanged. Therefore a bilinear map is symmetric exactly when \(L=R\). Symmetric maps have parameter dimension \(1+(2^r-1)+(2^r-r-1)=2^{r+1}-r-1\); comparison with all multiplication-factorizing maps, of dimension \(2^r\), gives symmetric defect \(2^r-r-1\). That dimension is zero exactly for \(r=1\). Over a finite field, independent parameter choices yield the stated powers of \(q\).

Finally, the top squarefree monomial \(x_{\{1,\ldots,r\}}\) is a nonzero product of \(r\) members of \(J_r\), while any product of \(r+1\) elements of \(J_r\) is zero. The nilpotency index is exactly \(r+1\).

## Verification
The included `verify.py` constructs squarefree multiplication tables over the prime fields of orders \(2\), \(3\), and \(5\). For each tested dimension, it systematically constructs the span of all zero-product tensors using complete left-multiplication kernels and checks the predicted quotient dimension. For the smaller cases it also directly tests every ordered pair of algebra elements. It verifies \(r=1,2,3\) over the specified fields and includes a symmetric-map nonfactorization witness for \(r=2\). The program terminates with `VERIFY_OK`. Finite-field computation is a consistency check only; the proof above applies to every field and every positive \(r\).

## Relationship to prior work
Gardella and Thiel (2023), Example 2.16, prove that the **one-generator** nilpotent algebra \(xK[x]/(x^m)\) ceases to be zero-product balanced (and hence is not zero-product determined) when \(m\ge4\); their Example 2.17 supplies another nonunital failure. The nonunital **squarefree multigenerator** algebras here instead remain zero-product determined at unbounded nilpotency index. The difference is substantive: all tensor product splittings of a squarefree monomial can be joined through incomparable subsets.

Jia and Xiao (2026) study the **unital** finite-dimensional zero-Jordan-product-determined property, completing an idempotent-generation criterion. Brešar's corresponding unital zero-product-determination criterion, recalled there and by Gardella–Thiel, already implies that \(A_r\) is not zero-product determined. We do not claim that non-determination as new. The present contribution is the explicit full universal bilinear-map classification and defect, the symmetric threshold, and the positive nilpotent radical family. In characteristic other than two, symmetric zero-product maps can also be interpreted through Jordan zero products; no such equivalence is asserted in characteristic two.

## Limitations
The classification concerns the stated squarefree complete-intersection family, not arbitrary finite local or nilpotent algebras. All dimension formulas use \(K\)-linear bilinear maps, not additive but nonlinear maps. The exact finite-field counts treat labelled bilinear forms, not automorphism orbits. Published classification theorems may permit independent indirect derivations of parts of the formulas; exhaustive novelty certification is not claimed. No independent mathematical audit has been performed.

## References
1. Hongyu Jia and Zhankui Xiao, *Finite dimensional zero Jordan product determined algebras are generated by idempotents*, arXiv:2607.05941v1, first submitted 2026-07-07. https://arxiv.org/abs/2607.05941
2. Eusebio Gardella and Hannes Thiel, *Zero-product balanced algebras*, Linear Algebra and its Applications 670 (2023), 121–153, DOI:10.1016/j.laa.2023.04.015. https://research.chalmers.se/publication/535620/file/535620_Fulltext.pdf
