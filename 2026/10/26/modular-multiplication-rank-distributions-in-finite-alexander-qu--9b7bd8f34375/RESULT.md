# Modular multiplication-rank distributions in finite Alexander quandle algebras with cyclic displacement Sylow subgroup

## Finding
Let \(K=\mathbb F_q\) have characteristic \(p\). Let \(A\) be a finite abelian group of cardinality \(N\), and let \(\varphi\in\operatorname{Aut}(A)\). Put \(H=(1-\varphi)A\), \(h=|H|\), and \(k=N/h\). Suppose the Sylow \(p\)-subgroup of \(H\) is nontrivial and cyclic of order \(m=p^a\), where \(a\ge1\). Write \(H\cong C_m\times B\), where \(p\nmid |B|\). For each orbit \(O\) of the \(q\)-Frobenius action on the characters of \(B\), put \(d_O=|O|\). Thus \(\sum_O d_O=|B|\).

For the Alexander quandle algebra \(E=K[\operatorname{Alex}(A,\varphi)]\), with products \(e_xe_y=e_{\varphi x+(1-\varphi)y}\), define \(L_u(v)=uv\) and \(R_u(v)=vu\). Then the complete distributions of the ranks of these linear operators are
\[
\sum_{u\in E}X^{\operatorname{rank}_K L_u}
=\prod_O\left(1+\sum_{t=1}^m\big(q^{d_Okt}-q^{d_Ok(t-1)}\big)X^{d_Ot}\right),
\]
\[
\sum_{u\in E}X^{\operatorname{rank}_K R_u}
=q^{N-h}\prod_O\left(1+\sum_{t=1}^m(q^{d_O}-1)q^{d_O(t-1)}X^{kd_Ot}\right).
\]
The exact number of **ordered** pairs, including zero factors, with zero product is
\[
Z(E):=|\{(u,v)\in E^2:uv=0\}|
=q^{N-h}\prod_O\left(q^{d_Okm}+(q^{d_O}-1)\sum_{t=1}^m q^{d_O(t-1+k(m-t))}\right).
\]
In particular, the three distributions depend on \(\varphi\) and \(A\) only through \(N\) and the abstract group \(H\). No assumption that \(1-\varphi\) is invertible or that \(K\) is a splitting field is needed.

## Assumptions and scope
Throughout, \(A\) is finite abelian, \(\varphi\) is an automorphism, and the coefficient field is \(\mathbb F_q\) of characteristic \(p\). The nontrivial cyclic \(p\)-Sylow assumption is essential to the stated one-variable truncated-polynomial formulas. The variables \(u,v\) range independently over all \(q^N\) elements of \(E\). The term rank always means rank of a \(K\)-linear map on the \(N\)-dimensional vector space \(E\). The trivial Frobenius orbit is included, and all arithmetic in the displayed formulas is arithmetic of nonnegative integers.

## Proof
**1. Separate the two inputs.** Let \(R=K[A]\) be the ordinary commutative group algebra, and let \(\alpha,\beta\colon R\to R\) be the algebra homomorphisms induced respectively by \(\varphi\) and \(1-\varphi\). The already-known group-ring transport identity (Zhang, Proposition 2.1) is \(uv=\alpha(u)\beta(v)\), interpreting the left product in the quandle algebra and the right product in \(R\). The map \(\alpha\) is invertible. The image of \(\beta\) is the subalgebra \(S=K[H]\), and \(\beta\) is surjective onto \(S\) with kernel dimension \(N-h\). Choose an arbitrary linear section of \(\beta\). Then \(v\) decomposes uniquely as its image \(z\in S\) and a kernel coordinate \(w\in K^{N-h}\), while \(\alpha(u)\) may range over all of \(R\).

**2. The free-module reduction.** Select one representative of each coset of \(H\) in \(A\). These \(k\) group elements give an \(S\)-basis of \(R\), so \(R\cong S^k\). Under invertible linear changes of both inputs and of the output, multiplication therefore has precisely the form
\[
((a_1,\ldots,a_k),(z,w))\longmapsto(a_1z,\ldots,a_kz),
\qquad a_i,z\in S,\quad w\in K^{N-h}.
\]
This reduction preserves individual operator ranks, up to a bijection in the variables \(u\) and \(v\), and preserves the ordered zero-product count.

**3. Local factors and valuations.** Since \(m=p^a\), the characteristic-\(p\) identity \((g-1)^m=g^m-1=0\) identifies \(K[C_m]\) with \(K[T]/(T^m)\). Because \(p\nmid |B|\), Maschke semisimplicity and Frobenius orbit descent give
\[
S\cong\prod_O S_O,\qquad S_O=\mathbb F_{q^{d_O}}[T]/(T^m).
\]
Fix one factor and write \(Q=q^{d_O}\). Define \(\nu(0)=m\) and \(\nu(z)=\max\{j:T^j\mid z\}\) for \(z\ne0\). For \(0\le j<m\), exactly \((Q-1)Q^{m-j-1}\) elements have \(\nu(z)=j\), since those divisible by \(T^j\) but not \(T^{j+1}\) form a difference of two ideals. Multiplication by such \(z\) has \(\mathbb F_Q\)-rank \(m-j\).

**4. Left ranks.** With \((a_1,\ldots,a_k)\) fixed, the left operator sends \(z\mapsto(a_1z,\ldots,a_kz)\); its kernel in \(S_O\) is \(\operatorname{ann}(a_1,\ldots,a_k)\), of dimension \(j=\min_i\nu(a_i)\), and its \(\mathbb F_Q\)-rank is \(m-j\). For \(1\le t\le m\), tuples with rank \(t\) are exactly the tuples in \((T^{m-t}S_O)^k\) but not in \((T^{m-t+1}S_O)^k\). Their number is \(Q^{kt}-Q^{k(t-1)}\). The unique rank-zero tuple is the zero tuple. Multiplication of contributions over independent factors \(O\) gives the first formula, using \(\dim_K\mathbb F_Q=d_O\).

**5. Right ranks.** With \(z\in S_O\) fixed, the right operator sends \((a_1,\ldots,a_k)\mapsto(a_1z,\ldots,a_kz)\), so its \(\mathbb F_Q\)-rank is \(k(m-\nu(z))\). Exactly \((Q-1)Q^{t-1}\) elements \(z\) have rank \(kt\) for \(1\le t\le m\); the unique zero has rank zero. Each \(z\in S\) has exactly \(q^{N-h}\) preimages under \(\beta\). Independence over factors gives the second formula.

**6. Zero products.** For a fixed \(z\in S_O\) with \(\nu(z)=j\), exactly \(Q^{kj}\) tuples \((a_1,\ldots,a_k)\) satisfy \(a_iz=0\) for every \(i\). At \(z=0\) the count is \(Q^{km}\). For nonzero \(z\), sum over \(j=0,\ldots,m-1\):
\[
Q^{km}+\sum_{j=0}^{m-1}(Q-1)Q^{m-j-1+kj}
=Q^{km}+(Q-1)\sum_{t=1}^m Q^{t-1+k(m-t)}.
\]
Multiply the local contributions over \(O\), and multiply by \(q^{N-h}\) for the independent kernel choices in the second input. This proves the third formula and completes the theorem.

## Verification
The standalone program `verify.py` enumerates all vectors over the specified prime fields, builds the quandle multiplication tensor directly, and computes the rank of each left and right multiplication matrix by Gaussian elimination **without using the group-algebra decomposition**. It reconstructs the coefficient distributions and compares the resulting number of ordered zero products with the theorem. Running `python verify.py` prints `VERIFY_OK`; the checked cases are \((A,K,\varphi)=(C_3,\mathbb F_3,-1)\), \((C_4,\mathbb F_2,-1)\), \((C_6,\mathbb F_3,-1)\), and \((C_{12},\mathbb F_2,-1)\). In the last case, \(H\cong C_6\), the field does not split the prime-to-\(p\) part of \(H\), and the formula gives \(444928\) ordered zero products. All finite tests are corroboration, not an exhaustive proof in unbounded dimension.

## Relationship to prior work
Zhang (2026, Proposition 2.1) supplies the group-ring transport identity used in Step 1; the identity is **not** asserted to be new. Churchill et al. (2026, Section 6) study the zero-divisor graph of certain **extended** quandle rings, including selected finite-field examples, not complete rank distributions of this modular Alexander family. Ta (2026, Theorem 4.3) treats zero-divisor existence for medial quandle rings over integral domains; this does not determine finite-field rank distributions or the number of zero-product pairs. Elhamdadi–Ta–Virgin (2026, Sections 3–6) establish a Fourier approach for quandle-algebra idempotents, not the present modular valuation enumeration. The new step is the explicit valuation-level distribution of both multiplication operators under a nonsemisimple cyclic Sylow factor, plus its zero-product census and the non-latin nonsplitting descent.

## Limitations
The proof does not treat noncyclic \(p\)-primary displacement subgroups, nonabelian \(A\), or infinite Alexander quandles. Searches cannot exclude all unindexed equivalent prior results; the reduction employs standard group-algebra theory, and novelty is claimed only for the combined explicit modular rank formulas, not the transport identity or truncated-polynomial decomposition. The graph degree distribution of an **extended unitalization** is a different object; no conclusion about that graph is asserted.

## References
- G. Churchill, I. R. Churchill, N. Fernando, and B. Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149v1 (2026-08-10), Section 6; https://arxiv.org/html/2608.09149v1.
- M. Elhamdadi, L. Ta, and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (2026-09-03), Sections 3–6; https://arxiv.org/html/2609.03799v1.
- Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1 (2026-10-06), Proposition 2.1; https://arxiv.org/html/2610.08204v1.
- L. Ta, *The zero divisor and augmentation conjectures for medial quandle rings*, arXiv:2610.20306v1 (2026-10-14), Theorem 4.3; https://arxiv.org/html/2610.20306v1.
