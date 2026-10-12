# The first binary excess for truncated-polynomial evolution envelopes

## Finding
For \(A_n=\mathbb F_2[t]/(t^n)\), write \(\operatorname{edim}(A_n)\) for the least dimension of an evolution \(\mathbb F_2\)-algebra that contains \(A_n\) as an ideal. The exact initial profile is
\[
(\operatorname{edim}(A_1),\operatorname{edim}(A_2),\operatorname{edim}(A_3),\operatorname{edim}(A_4))=(1,3,5,8).
\]
In particular, \(\operatorname{edim}(A_4)=8>7=2\cdot4-1\), the first strict excess over this classical interpolation bound in the binary truncated-polynomial family. The dimension-eight envelope is explicit, and an exhaustive, independently rerunnable rank test excludes dimension seven or less.

## Assumptions and scope
The coefficient field is exactly \(\mathbb F_2\), and \(1\le n\le4\). An evolution algebra is a commutative, generally nonassociative algebra with a natural basis \(f_1,\ldots,f_m\) satisfying \(f_if_j=0\) for \(i\ne j\). An ideal embedding is an injective algebra homomorphism \(\iota:A_n\hookrightarrow E\) such that \(\iota(A_n)E\subseteq\iota(A_n)\). Multiplication on \(A_n\) is ordinary truncated polynomial multiplication. No result for larger \(n\) or other fields is claimed.

## Proof
**Reduction to a finite symmetric-bilinear rank problem.** For a finite-dimensional commutative unital algebra \(A\) over any field, define \(S(A)\) to be the smallest \(m\) for which there exist linear functionals \(\ell_j:A\to K\) and elements \(v_j\in A\) such that, for all \(x,y\in A\),
\[
xy=\sum_{j=1}^{m}\ell_j(x)\ell_j(y)v_j.
\]
Then \(\operatorname{edim}(A)=S(A)\). Indeed, in an ideal embedding \(\iota:A\to E\), write \(\iota(x)=\sum_j\ell_j(x)f_j\) in a natural basis. For each nonzero \(\ell_j\), the ideal condition implies \(f_j^2\in\iota(A)\). Therefore \(f_j^2=\iota(v_j)\), giving the stated decomposition with no more than \(\dim E\) terms. Conversely, from such a decomposition form a vector space \(E\) with basis \(f_1,\ldots,f_m\), define \(f_i f_j=0\) for distinct indices and \(f_j^2=\sum_i\ell_i(v_j)f_i\), and put \(\iota(x)=\sum_i\ell_i(x)f_i\). The decomposition implies \(\iota(xy)=\iota(x)\iota(y)\), and each \(f_j\iota(x)=\ell_j(x)\iota(v_j)\), so the image is an ideal. If \(\iota(x)=0\), then \(x=x\cdot1=\sum_j\ell_j(x)\ell_j(1)v_j=0\), proving injectivity. This argument uses the full bilinear multiplication, not polarization, so is valid in characteristic two.

**Explicit eight-term upper bound.** Represent \(a=a_0+a_1t+a_2t^2+a_3t^3\) by its coordinate vector. Take the eight linear functionals
\[
(\ell_1,\ldots,\ell_8)=(a_0,a_1,a_0+a_1,a_2,a_0+a_2,a_1+a_2,a_3,a_0+a_3),
\]
with respective output elements
\[
(v_1,\ldots,v_8)=(1+t+t^2+t^3,\ t+t^2+t^3,\ t,\ t^2+t^3,\ t^2,\ t^3,\ t^3,\ t^3).
\]
In \(\mathbb F_2[t]/(t^4)\), direct coefficient comparison on all sixteen ordered basis pairs \((t^i,t^j)\), \(0\le i,j<4\), yields
\[
ab=\sum_{h=1}^{8}\ell_h(a)\ell_h(b)v_h.
\]
The reduction above builds an eight-dimensional evolution algebra with \(A_4\) as an ideal. This provides \(\operatorname{edim}(A_4)\le8\).

**Exhaustive seven-term obstruction.** There are exactly fifteen nonzero linear functionals on the four-dimensional \(\mathbb F_2\)-space \(A_4\). Label each by its four-bit coefficient vector \(w\in\{1,\ldots,15\}\). A term \(\ell_w(a)\ell_w(b)v\) contributes the symmetric rank-one matrix \(P_w=(w_iw_j)_{0\le i,j<4}\) to each output-coordinate slice. The four required symmetric multiplication matrices are
\[
B_k=\bigl(\mathbf 1_{i+j=k}\bigr)_{0\le i,j<4},\qquad 0\le k<4.
\]
A representation using at most seven terms exists only if some set of at most seven of the fifteen matrices \(P_w\) spans every \(B_k\). Any such set can be extended to seven distinct nonzero functionals. The supplied exact computation enumerates **all** \(\binom{15}{7}=6435\) seven-element sets, row-reduces their ten upper-triangular coefficients over \(\mathbb F_2\), and checks membership of the four target slices. Not one passes. Thus \(\operatorname{edim}(A_4)>7\), giving the equality eight.

**Lower ranks.** The same complete finite test for \(n=1,2,3\) returns minimum support sizes \(1,3,5\). Every possible nonzero linear functional is included, so this is a proof for these finite-dimensional binary problems, rather than sampling. Combined with the value eight, this establishes the asserted initial profile and first strict excess.

## Verification
Run `python3 verify.py` with Python 3.8 or later. The source reconstructs all fifteen possible symmetric rank-one slices, checks all 6,435 seven-subsets, enumerates the exact optimal support sizes for dimensions one through four, and directly verifies the stated eight-term formula on all \(16^2=256\) ordered pairs of elements of \(A_4\). Expected output ends with `LOWER_BOUND_6435_SEVEN_SUPPORTS_OK`, `EXPLICIT_EIGHT_TERM_DECOMPOSITION_256_PRODUCTS_OK`, and `VERIFY_OK`. The rank computation uses integer bit masks with exact \(\mathbb F_2\) arithmetic and contains no randomized or floating-point steps.

## Relationship to prior work
Costoya, Fernández Ouaridi, and Viruel (2026) introduced the minimum evolution-envelope dimension and proved the value \(2n-1\) for \(K[t]/(t^n)\) **provided** the characteristic is different from two and the field has at least \(2n-1\) elements (their Theorem 5.6). These hypotheses exclude the present binary case; their discussion of the three-element field also does not compute the binary fourth-order value. The general ideal-embedding framework is theirs and is not asserted as new here.

Couveignes and Ezome (2021/2022) discuss symmetric bilinear complexity of multiplication in \(K[t]/(t^n)\) (Section 7), record the general lower bound \(2n-1\), and obtain equality when sufficiently many field elements are available. That result leaves the exact four-dimensional binary symmetric complexity unidentified. Morse (2026) proves the full, **seven-output** four-term binary polynomial product needs nine AND gates in a stronger circuit model. Here the multiplication is truncated to the **first four outputs**, and the relevant model is symmetric bilinear decomposition; the full-product lower bound cannot be transferred to this projection. Closely related classical small-field polynomial-multiplication algorithms may encode the same value under different terminology.

## Limitations
The theorem is limited to \(n\le4\) and the base field \(\mathbb F_2\). An exact finite-exhaustion proof has no implication for higher dimensions, other characteristics, unrestricted Boolean-circuit complexity, or the classification of minimum envelopes up to isomorphism. Existing older rank tables may conceal an equivalent statement; the literature comparison is not a proof of global novelty. The displayed embedding construction is dimension-optimal, not canonical or unique.

## References
- C. Costoya, A. Fernández Ouaridi, A. Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784v1, 26 September 2026, Sections 3–5 and Theorem 5.6. https://arxiv.org/pdf/2609.32784
- J.-M. Couveignes, T. Ezome, *The equivariant complexity of multiplication in finite field extensions*, arXiv:2110.13763, Section 7. https://arxiv.org/pdf/2110.13763
- G. Morse, *Unrestricted Boolean Multiplicative Complexity of Four-Term Binary Polynomial Multiplication: Rational Places, Hasse Jets, and the Failure of Nonlinear Feedback*, arXiv:2608.30238v1, 31 August 2026. https://arxiv.org/abs/2608.30238
