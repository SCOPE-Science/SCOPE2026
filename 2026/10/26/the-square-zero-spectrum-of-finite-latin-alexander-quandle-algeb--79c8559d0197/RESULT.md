# The square-zero spectrum of finite latin Alexander quandle algebras

## Finding

Let \(A\) be a finite abelian group, let \(\varphi\) and \(1-\varphi\) be automorphisms of \(A\), and let \(K\) be a field whose characteristic does not divide \(|A|\) and which contains the roots of unity of order \(\exp(A)\). In the generally nonassociative quandle algebra \(E=K[\operatorname{Alex}(A,\varphi)]\), a square-zero linear subspace means a \(K\)-linear subspace \(W\) such that \(u*v=0\) for **every ordered pair** \(u,v\in W\).

Write \(\widehat A=\operatorname{Hom}(A,K^\times)\). Let \(T\) be the permutation of \(\widehat A\) defined by
\[
T(\chi)=\chi\circ\bigl((1-\varphi)\varphi^{-1}\bigr).
\]
For a subset \(S\subseteq\widehat A\), let \(E_S\) denote the linear subspace whose Fourier transforms vanish outside \(S\). Then:

1. **Complete subspace classification.** A linear subspace \(W\subseteq E\) has \(W*W=0\) if and only if \(W\subseteq E_S\) for some set \(S\) such that \(S\cap T(S)=\varnothing\). Each such \(E_S\) is square-zero. The same condition classifies individual elements with \(u*u=0\) via their Fourier supports.
2. **Sharp dimension and extremizers.** If the cycle lengths of \(T\) are \(\ell_1,\ldots,\ell_r\), then
\[
\max_{W*W=0}\dim_K W=\sum_{i=1}^r\left\lfloor\frac{\ell_i}{2}\right\rfloor.
\]
Every maximum-dimensional square-zero subspace is exactly an \(E_S\) with \(S\) a maximum independent set of the cycle graph of \(T\). Their total number is \(\prod_i c_{\ell_i}\), where \(c_1=1\), \(c_\ell=2\) for even \(\ell\), and \(c_\ell=\ell\) for odd \(\ell\ge3\).
3. **Finite-field enumeration.** If \(K=\mathbb F_q\), the exact number of square-zero elements of \(E\), including zero, is
\[
\#\{u\in E:u*u=0\}=\prod_{i=1}^r I_{\ell_i}(q-1),\qquad
I_\ell(t)=\sum_{j=0}^{\lfloor\ell/2\rfloor}\frac{\ell}{\ell-j}\binom{\ell-j}{j}t^j.
\]
Here \(I_1(t)=1\); for \(\ell=2\) this expression gives \(1+2t\).
4. **Rigidity boundary.** The algebra has no nonzero square-zero element if and only if \(2\varphi=1\) on \(A\), equivalently if and only if the Alexander quandle is commutative.

For the odd-prime dihedral quandle \(R_p=\operatorname{Alex}(\mathbb Z/p\mathbb Z,-1)\), let \(d=\operatorname{ord}_p(-2)\), and write \(r=(p-1)/d\). The maximum dimension is \(r\lfloor d/2\rfloor\), the number of maximum-dimensional spaces is \(c_d^r\), and over a splitting finite field \(\mathbb F_q\) the number of square-zero elements is \(I_d(q-1)^r\). For example, \(p=3\) yields only the zero element, \(p=5\) yields maximum dimension two and two maximizing spaces, and \(p=11\) yields maximum dimension four and twenty-five maximizing spaces.

## Assumptions and scope

The product \(*\) is the bilinear extension of \(a\triangleright b=\varphi(a)+(1-\varphi)(b)\). The requirement that \(1-\varphi\) be invertible means the quandle is latin; it ensures that \(T\) is a permutation. The splitting and nonmodular requirements ensure that the finite Fourier transform is invertible. No claim is made for fields not meeting these conditions or for arbitrary nonlatin quandles. "Square-zero" means \(u*u=0\) for an element; "square-zero subspace" means the stronger all-ordered-products condition \(W*W=0\). No associativity or power-associativity is assumed.

## Proof

**Fourier multiplication.** For \(u=\sum_a u_a e_a\in E\), set \(\widehat u(\chi)=\sum_a u_a\chi(a)\). By character orthogonality and the assumptions on \(K\), this is a linear isomorphism \(E\cong K^{\widehat A}\). Define \(\Phi(\chi)=\chi\circ\varphi\) and \(\Psi(\chi)=\chi\circ(1-\varphi)\). Direct expansion of the basis product gives, for every \(u,v,\chi\),
\[
\widehat{u*v}(\chi)=\widehat u(\Phi\chi)\widehat v(\Psi\chi).
\]
Both \(\Phi\) and \(\Psi\) are permutations and \(T=\Psi\Phi^{-1}\).

**Square-zero support criterion.** If \(u*u=0\), then for each \(a=\Phi\chi\), the two factors \(\widehat u(a)\) and \(\widehat u(Ta)\) have product zero. Since \(K\) is a field, no two neighboring points of the cycle permutation \(T\) may belong to the support of \(\widehat u\). Conversely, this independent-support condition makes every Fourier coordinate of \(u*u\) vanish. For a subspace \(W\), put \(S=\bigcup_{u\in W}\operatorname{supp}\widehat u\). If \(W*W=0\) and \(a\in S\), choose \(u\in W\) with \(\widehat u(a)\ne0\). Then, for **every** \(v\in W\), the product equation at \(\Phi^{-1}a\) forces \(\widehat v(Ta)=0\); hence \(Ta\notin S\). Therefore \(S\cap T(S)=\varnothing\). The converse is immediate, and proves assertion 1.

**Sharp dimensions and count.** The cycle decomposition of \(T\) is a disjoint union of loops, ordinary edges, and cycles of length at least three. An independent set in a cycle of length \(\ell\) has size at most \(\lfloor\ell/2\rfloor\), with equality achieved; a loop contributes no vertices. Every \(W\) satisfying the support criterion is contained in the coordinate subspace \(E_S\), hence \(\dim W\le |S|\). Equality at the global maximum forces \(W=E_S\), with \(S\) a maximum independent set. In an even cycle there are exactly two alternating maximum independent sets; in an odd cycle of length at least three there are exactly \(\ell\); a loop has one, namely the empty set. These independent choices across cycles prove assertion 2.

**Exact square-zero-element count.** Fourier inversion makes arbitrary coordinate values independent choices. Fix an independent support \(S\): there are exactly \((q-1)^{|S|}\) Fourier vectors with support *exactly* \(S\). Summing over all independent sets factors over the cycles. The number of independent \(j\)-subsets of a length-\(\ell\) cycle is \(\frac{\ell}{\ell-j}\binom{\ell-j}{j}\), including the loop convention \(j=0\) only. This proves assertion 3.

**Rigidity.** There exists a nonzero square-zero element exactly when \(T\) has a nontrivial cycle, equivalently when \(T\ne1\). Since characters separate the points of \(A\), \(T=1\) is equivalent to \((1-\varphi)\varphi^{-1}=1\), or \(2\varphi=1\). The latter is precisely the condition \(a\triangleright b=b\triangleright a\) for every \(a,b\in A\). This proves assertion 4.

**Prime-dihedral specialization.** On \(\widehat{\mathbb Z/p\mathbb Z}\cong\mathbb Z/p\mathbb Z\), the permutation \(T\) is multiplication by \(-2\). The trivial character is fixed, and the \(p-1\) nontrivial characters split into \(r=(p-1)/d\) cycles, each of length \(d\). Substitution in assertions 2 and 3 gives all specialized formulas.

## Verification

The standalone `verify.py` checker works over exact prime fields, explicitly constructs each quandle multiplication table, inverts the discrete Fourier transform, and checks the product of every pair of Fourier coordinate basis vectors. It independently enumerates independent subsets of the character-cycle graph and checks the dimension, maximizing-space count, and exact square-zero-element count for cyclic quandles of orders \(3,5,7,9,11,13,15\). For orders \(3\) and \(5\) it also exhaustively enumerates **all** Fourier vectors and tests their squares by direct coefficient multiplication. Run `python3 verify.py`; the successful terminator is `VERIFY_OK`.

These bounded calculations are verification examples, not a replacement for the all-finite-abelian-group proof.

## Relationship to prior work

The Fourier multiplication identity is established in Elhamdadi–Ta–Virgin, *Fourier Analysis and Idempotents in Quandle Algebras* (arXiv:2609.03799, Sections 3 and 6), and in Ta, *The zero divisor and augmentation conjectures for medial quandle rings* (arXiv:2610.20306, Proposition 5.1). Zhang, *Group-ring methods for Alexander quandle rings* (arXiv:2610.08204, Proposition 2.1), also supplies the transported-multiplication framework. These are substantive antecedents, **not** new claims here.

The new conclusion identifies the full square-zero-subspace geometry, its sharp maximum and extremizers, its exact finite-field point count, and its commutative-versus-square-zero rigidity boundary. Ta's paper proves results about zero divisors and augmentations of idempotents, not these square-zero classifications. Churchill–Churchill–Fernando–Kousik (arXiv:2608.09149, Sections 5–6) studies nilpotence and zero-divisor graphs of selected quandle rings, particularly their extensions, but not this uniform cycle-invariant theorem. Sangare–Ta (arXiv:2608.01550v2) studies idempotents, automorphism groups and commutator widths. The cycle combinatorics are proved above rather than attributed to these sources.

## Limitations

The formulas require a splitting field of nonmodular characteristic and a finite latin Alexander quandle; modular coefficients and nonlatin quandles may have different behavior. The independent-set calculation is a combinatorial consequence of an established Fourier multiplication identity, so novelty rests in the **complete structural extraction and the arithmetic rigidity consequences**, not in rediscovering the identity. Equivalent coverage in older literature on nonassociative algebras or generalized Fourier-twisted products cannot be excluded absolutely. Independent review has not been performed.

## References

1. L. Ta, *The zero divisor and augmentation conjectures for medial quandle rings*, arXiv:2610.20306v1, 14 October 2026, Sections 2, 4–6; https://arxiv.org/html/2610.20306v1.
2. M. Elhamdadi, L. Ta, B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1, 3 September 2026, Sections 3–6; https://arxiv.org/html/2609.03799v1.
3. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1, 6 October 2026, Sections 2–3; https://arxiv.org/html/2610.08204v1.
4. G. Churchill, I. R. Churchill, N. Fernando, B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1, 10 August 2026, Sections 5–6; https://arxiv.org/html/2608.09149v1.
5. B. Sangare, L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v2, 11 August 2026, Sections 3–5; https://arxiv.org/html/2608.01550v2.
