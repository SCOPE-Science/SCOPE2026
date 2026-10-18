# Odd-characteristic cycle-sum division through square-zero divisor blocks

## Finding
Let \(K\) be a field of characteristic \(p\ge3\). In the algebra \(\mathcal C_K\) of finite formal linear combinations of permutation cycles, with basis \(C_n\) (\(n\ge1\)) and multiplication
\[
C_mC_n=\gcd(m,n)C_{\operatorname{lcm}(m,n)},
\]
every division question \(AX=B\) reduces to a finite algebra of square-zero local blocks. For an integer \(m=p^a u\), where \(a\ge0\) and \(p\nmid u\), write \(R_m\) for the span of \(C_d\) over all positive divisors \(d\mid m\). Then
\[
\boxed{R_m\cong\prod_{r\mid u}(K\oplus K^a),\qquad
(\alpha,v)(\beta,w)=(\alpha\beta,\alpha w+\beta v).}
\]
The product has \(\tau(u)\) blocks, where \(\tau\) counts divisors; at \(a=0\) each block is simply \(K\). There is a retraction \(\mathcal C_K\longrightarrow R_m\) fixing \(R_m\). Thus if the supports of \(A,B\) divide \(m\), solvability of \(AX=B\) among arbitrary finite cycle sums is **equivalent** to solvability in \(R_m\).

For a finite coefficient field \(K=\mathbb F_q\) of odd characteristic, the number of ordered divisible pairs, **not** triples of solutions, is exactly
\[
\boxed{\#\{(A,B)\in R_m^2:\exists X\in\mathcal C_K,\ AX=B\}
=\left((q-1)q^{2a+1}+q(q^a-1)+1\right)^{\tau(u)}.}
\]
The local solvability conditions below provide a constructive decision procedure and count every solution within \(R_m\).

## Assumptions and scope
All indices are positive integers; every formal sum has finite support. For \(n=p^k v\) with \(p\nmid v\), set \(D_n=v^{-1}C_n\) (the reciprocal exists in \(K\)). An arbitrary element of \(R_m\) can be uniquely expanded in the basis \(D_{p^k d}\), with \(0\le k\le a\) and \(d\mid u\). The ring has a unit \(D_1=C_1\); the zero element is the empty formal sum.

Define \(T_a(K)=K\oplus K^a\) with the displayed multiplication. For coordinates \(A_r=(\alpha_r,v_r)\) and \(B_r=(\beta_r,w_r)\) in \(T_a(K)\), the equation \(AX=B\) is solvable if and only if, **for every divisor \(r\mid u\)**, one of these mutually exclusive conditions holds:

1. \(\alpha_r\ne0\), without restriction on \((\beta_r,w_r)\);
2. \(\alpha_r=0\), \(v_r\ne0\), \(\beta_r=0\), and \(w_r\in Kv_r\);
3. \(\alpha_r=0\), \(v_r=0\), and \((\beta_r,w_r)=(0,0)\).

For a field of order \(q\), a block meeting condition 1, 2, or 3 has respectively \(1\), \(q^a\), or \(q^{a+1}\) possible block-solutions. Multiply over the blocks to obtain the complete finite-truncation fiber count. The global infinite solution set may be larger than this finite-truncation fiber; the equivalence asserted here concerns existence.

## Proof
**Normalization.** For positive integers \(m=p^i u\) and \(n=p^j v\) with \(p\nmid uv\), direct substitution in the cycle product gives
\[
D_mD_n=p^{\min(i,j)}D_{\operatorname{lcm}(m,n)}
=\begin{cases}0,&i,j\ge1,\\D_{\operatorname{lcm}(m,n)},&\min(i,j)=0.\end{cases}
\]
Here the coefficient is read in \(K\); the identity uses \(\gcd(u,v)\operatorname{lcm}(u,v)=uv\). In particular the span of all positive-\(p\)-valuation basis elements is square-zero, and the \(p\)-free part acts by least common multiple. Associativity follows from the displayed rule or from the original cycle-product construction.

**Explicit coordinate isomorphism.** Fix \(m=p^a u\). For each divisor \(r\mid u\) and basis index \(p^k d\) with \(d\mid u\), put
\[
\Phi_m(D_{p^k d})_r=
\begin{cases}0,&d\nmid r,\\(1,0),&d\mid r,\ k=0,\\(0,e_k),&d\mid r,\ 1\le k\le a,\end{cases}
\]
where \(e_k\) denotes the \(k\)-th standard basis vector of \(K^a\). The identity
\[
\mathbf1_{d\mid r}\mathbf1_{e\mid r}=\mathbf1_{\operatorname{lcm}(d,e)\mid r}
\]
and square-zero multiplication in each block prove that \(\Phi_m\) is multiplicative. For each fixed \(k\), the matrix \((\mathbf1_{d\mid r})_{r,d\mid u}\) is the divisor zeta matrix, with a unit diagonal when divisors are ordered compatibly with divisibility; hence it is invertible over **every** field. Consequently \(\Phi_m\) is an algebra isomorphism. For reproducibility, inversion uses the ordinary integer Möbius function:
\[
\text{the coefficient of }D_{p^k d}\text{ in }X
=\sum_{r\mid d}\mu(d/r)\,\bigl(\Phi_m(X)_r\bigr)_k,
\]
where the coordinate \(k=0\) is the scalar coordinate. This is the inverse of the zeta transform \(z_k(r)=\sum_{d\mid r}c_k(d)\).

**Retraction.** Write any index as \(n=p^k v\) with \(p\nmid v\). Define the following \(K\)-linear map on the entire infinite basis:
\[
\rho_m(D_n)=\begin{cases}
D_{\gcd(v,u)},&k=0,\\
0,&k\ge1,\ a=0,\\
D_{p^{\min(k,a)}\gcd(v,u)},&k\ge1,\ a\ge1.
\end{cases}
\]
It fixes each basis element whose index divides \(m\). To check multiplication, use
\[
\gcd(\operatorname{lcm}(v,w),u)
=\operatorname{lcm}(\gcd(v,u),\gcd(w,u))
\]
for the \(p\)-free indices. The other coordinate is governed by \(\min(k,a)\) and \(\max(k,j)\); if both inputs have positive \(p\)-valuation, their product vanishes before and after the map. Hence \(\rho_m\) is a unital algebra homomorphism with image \(R_m\). If \(A,B\in R_m\) and \(AX=B\) for some \(X\in\mathcal C_K\), then \(A\rho_m(X)=B\), proving the claimed full-to-finite reduction. The reverse implication is immediate.

**Local division and counting.** In \(T_a(K)\), multiplication by \((\alpha,v)\) sends \((\gamma,z)\) to \((\alpha\gamma,\alpha z+\gamma v)\). If \(\alpha\ne0\), it is a unit with a unique solution for every target. If \(\alpha=0\) and \(v\ne0\), its image is exactly \(\{(0,\gamma v):\gamma\in K\}\); the coefficient \(\gamma\) is unique while \(z\) is free. If \((\alpha,v)=(0,0)\), only the zero target is reached. This proves the three cases and fiber cardinalities.

Finally, for \(K=\mathbb F_q\), there are \((q-1)q^a\) unit first factors, each with \(q^{a+1}\) reachable targets; there are \(q^a-1\) nonzero pure-nilpotent factors, each with exactly \(q\) reachable targets; the zero factor has one. These disjoint cases sum to
\[
(q-1)q^{2a+1}+q(q^a-1)+1
\]
solvable ordered pairs per block. Since the \(\tau(u)\) blocks are independent, multiplication proves the boxed total.

## Verification
The accompanying `verify.py` constructs the normalized finite ring directly from the original cycle multiplication. It exhaustively checks bijectivity of the coordinate transform, multiplicativity, finite division-fiber counts, and sample retraction identities. The verified prime-field configurations are \((p,m)=(3,1),(3,3),(3,6),(3,9),(5,5),(5,10),(7,7)\); additional characteristic-two cases serve only as controls, not as a new claim. The enumeration includes \(271441\) solvable pairs for \(p=5,m=10\), in a ring of \(625\) elements. Run `python verify.py` with standard Python 3; no dependencies are needed. These finite checks are supplementary to the proof for arbitrary fields and all positive indices.

## Relationship to prior work
Gadouleau and Johnson's *Semirings of formal sums and injective partial transformations* (arXiv:2603.26508v1; public March 27, 2026) introduces the finite-cycle formal-sum algebra, solves the division problem over \(\mathbb F_2\) in Theorem 3.9 and discusses its binary cycle structure in Section 3. Its Section 5 explicitly identifies other prime fields as a possible direction. The binary result, the gcd/lcm multiplication and the standard Möbius inversion used here are prior foundations. The present assertion concerns odd-characteristic coefficient fields: it identifies square-zero local factors at every divisor cutoff, proves a full-algebra retraction that reduces division to those factors, and gives an exact \(\mathbb F_q\) enumeration not stated in the inspected binary theory.

## Limitations
Only sums of cycles are treated, not sums of chains and cycles. The exact pair-count formula requires a **finite** field; the decomposition and decision criterion hold over arbitrary fields of odd positive characteristic. The enumeration measures divisibility of pairs in one finite divisor subalgebra, not the number of solutions throughout the infinite algebra. The normalized decomposition also works for characteristic two, but that characteristic is deliberately excluded from the originality claim because of existing binary results. Equivalent unpublished or unindexed analyses may exist; bibliographic searches cannot certify absence. No independent audit has been performed.

## References
Gadouleau, M., and Johnson, M., *Semirings of formal sums and injective partial transformations*, arXiv:2603.26508v1 (first submitted March 27, 2026), especially §§2–3 and §5. https://arxiv.org/abs/2603.26508 .
