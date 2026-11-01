# Two matching defects amplify the longest scan cycle in complete-graph parity dynamics

## Finding

Let \(n\ge4\) be even, let \(0\le k\le n/2\), and let \(G_{n,k}\) be \(K_n\) with the disjoint edges \(\{1,2\},\{3,4\},\ldots,\{2k-1,2k\}\) deleted. Every vertex carries an element of a finite field \(\mathbb F_q\) of characteristic two. One **sweep** visits vertices in the order \(1,2,\ldots,n\), replacing the visited state by its **current state plus the current states of all its graph neighbors**; all other states retain their current values. Let \(F\) be the one-sweep map and set \(m=n-2k\) and \(M=m+1\), an odd positive integer.

The map \(F\) is linearly conjugate over \(\mathbb F_q\) to the direct sum of (i) the cyclic right shift on the zero-sum hyperplane of \(\mathbb F_q^M\), of dimension \(m\), and (ii) the map
\[
H_k(d,b)=\bigl(d,\,b+(I_k+J_k)d\bigr)
\]
on \(\mathbb F_q^k\oplus\mathbb F_q^k\), where \(J_k\) is the all-ones matrix. For \(k=0\), the second summand is absent. When \(m=0\), the first summand is the zero-dimensional space. In particular, the complete rational/Jordan splitting is
\[
 F\sim C_m\oplus
 \begin{cases}
 J_2(1)^{\oplus k},& k\text{ even},\\
 J_2(1)^{\oplus(k-1)}\oplus J_1(1)^{\oplus2},&k\text{ odd},
 \end{cases}
\]
where \(C_m\) is the companion matrix of \(1+z+\cdots+z^m\) and \(J_j(1)\) is an ordinary Jordan block. Here the indicated Jordan blocks are absent at \(k=0\). The characteristic polynomial is
\[
\chi_F(z)=(1+z)^{2k}(1+z+\cdots+z^m).
\]

Every initial configuration is periodic without a transient. The **exact maximum least period** (equivalently, the order of \(F\)) is
\[
\boxed{L(n,k)=\begin{cases}n-2k+1,&k=0\text{ or }1,\\2(n-2k+1),&2\le k\le n/2.\end{cases}}
\]
For each integer \(t\ge1\), put \(g_t=\gcd(M,t)\) and
\[
b_t=\begin{cases}2k,&t\text{ even},\\k+\mathbf1_{\{k\text{ odd}\}},&t\text{ odd}.\end{cases}
\]
The **exact population of configurations fixed after \(t\) sweeps** is
\[
\boxed{\#\operatorname{Fix}(F^t)=q^{g_t-1+b_t}.}
\]
Consequently, for every divisor \(d\) of \(L(n,k)\), the number of configurations of least period \(d\) and the number of corresponding distinct orbits are, respectively,
\[
P_d=\sum_{e\mid d}\mu(d/e)q^{\gcd(M,e)-1+b_e},\qquad O_d=P_d/d.
\]
The values are zero for \(d\nmid L(n,k)\).

In particular, on every even-order complete graph with \(n\ge8\), deleting **one** edge reduces the maximum scan period from \(n+1\) to \(n-1\), whereas deleting **two disjoint** edges raises it to \(2(n-3)>n+1\). The ratio of the last period to the complete-graph period tends to \(2\).

## Assumptions and scope

The graph is simple, undirected, and labelled exactly as above. Deleted matching endpoints are consecutive in the scan and scanned before the \(m\) untouched vertices. The scan is repeated without changing the order. All additions are in characteristic two; \(q\) may be any power of two. The update includes the visited vertex's **old current state**, not merely its neighbors. A sweep, rather than a single site visit, is one unit of time. No assertion is made for arbitrary permutations that interleave unmatched vertices, odd \(n\), other characteristics, or self-exclusive updates.

## Proof

**1. Exact paired and unpaired updates.** Write the states on the deleted-edge pairs as \((p_i,q_i)\), for \(1\le i\le k\), and those on unpaired vertices as \((z_1,\ldots,z_m)\). Put \(d_i=p_i+q_i\), \(D=\sum_i d_i\), and \(S=D+\sum_jz_j\). Before updating a matched endpoint, its closed graph neighborhood is the entire vertex set except its missing-edge partner. Thus the first endpoint becomes \(p_i'=S+q_i\). The total sum after that visit is \(p_i+q_i=d_i\); the second becomes \(q_i'=d_i+p_i'=S+p_i\). The total sum after the second visit returns to \(S\), and the pair sum remains \(d_i\). Every matched pair therefore starts its visit with the same \(S\). Each remaining unpaired vertex has a full closed neighborhood, so after all matched pairs the unpaired update is
\[
(z_1,\ldots,z_m)\longmapsto (S,z_1,\ldots,z_{m-1}).
\]
These identities also hold at \(k=0\) or \(m=0\) with empty-coordinate conventions.

**2. An explicit invertible conjugacy.** Since \(m\) is even, define \(y_j=z_j+D\) and \(E(y)=y_2+y_4+\cdots+y_m\) (zero if \(m=0\)). Define \(b_i=p_i+E(y)\). The transformation from \((p_i,q_i,z_j)\) to \((d_i,b_i,y_j)\) is invertible: recover \(D\) from the \(d_i\), then \(z_j=y_j+D\), \(p_i=b_i+E(y)\), and \(q_i=p_i+d_i\). Direct substitution from Step 1 gives
\[
 d_i'=d_i,\qquad y'=(\sum_j y_j,y_1,\ldots,y_{m-1}),\qquad b_i'=b_i+d_i+D.
\]
Indeed, \(S=D+\sum_j y_j\), and \(E(y')\) is the sum of odd-indexed \(y_j\); hence \(E(y)+E(y')=\sum_jy_j\). This proves the stated direct sum with \(b'=b+(I_k+J_k)d\).

**3. Jordan structure.** On the \((d,b)\) coordinates, \(H_k=I+N\), where \(N(d,b)=(0,(I_k+J_k)d)\), so \(N^2=0\). If \(k\) is even, \(I_k+J_k\) has rank \(k\): a vector in its kernel satisfies \(d=(\sum d_i)\mathbf1\), and summing forces \(\sum d_i=0\). If \(k\) is odd, its kernel is exactly the span of \(\mathbf1\), so its rank is \(k-1\). Each rank-one part of a square-zero map gives one Jordan block of size two; the remaining \(2k-2\operatorname{rank}(N)\) dimensions give size-one blocks. The companion polynomial of the shift block is \(1+z+\cdots+z^m\), since the displayed shift satisfies precisely this length-\(m\) recurrence. This proves the claimed Jordan forms and characteristic polynomial.

**4. Periods and fixed-space dimensions.** Extend \(y\in\mathbb F_q^m\) to the \(M=m+1\) coordinates \((\sum_jy_j,y_1,\ldots,y_m)\). Their sum is zero, and the action of \(C_m\) becomes a cyclic rotation of these \(M\) coordinates. Its \(t\)-fixed vectors are constant on \(\gcd(M,t)\) rotation cycles. Every such cycle has odd length because \(M\) is odd, so the zero-sum constraint gives one independent equation; their fixed-space dimension is \(g_t-1\). For \(M\ge3\), a vector with two consecutive nonzero coordinates of equal magnitude and all others zero on the zero-sum hyperplane has least period exactly \(M\); for \(M=1\), the block is absent.

In characteristic two, \(H_k^{2}=I\), and its fixed space for odd powers has dimension \(2k-\operatorname{rank}(I_k+J_k)=k+\mathbf1_{\{k\text{ odd}\}}\); even powers fix all \(2k\) coordinates. When \(k=0\) or \(1\), \(H_k\) is the identity. When \(k\ge2\), \(I_k+J_k\ne0\) and a state of least period two exists. The rotation order \(M\) is odd, so combining the two independent blocks yields a state of period \(2M\) for \(k\ge2\), and period \(M\) for \(k\le1\). Counting the fixed-space vectors gives \(q^{g_t-1+b_t}\). Möbius inversion on least-period divisors yields \(P_d\) and \(O_d\). Each local update has a coefficient of one on its own coordinate and is therefore invertible, consistent with the absence of transients.

**5. Two-defect amplification.** At \(k=0\), \(M=n+1\); at \(k=1\), \(M=n-1\); at \(k=2\), \(M=n-3\) and the rank-one nilpotent shear adds a factor of two. For even \(n\ge8\), \(2(n-3)>n+1\). This proves the asserted nonmonotone defect response.

## Verification

The accompanying standalone `code/verify_scan.py` directly compares the original sequential local updates against the conjugated formula for every binary configuration, every even \(n\in\{4,6,8,10\}\), and every allowed matching size. It also checks each claimed order and each divisor-wise fixed population, covering 7,728 labelled initial configurations.

Independently, `code/verify_direct.cpp` constructs direct update tables using parity and locally evolving bits. It follows all 757,296 binary configurations for all even \(n\) from 4 through 16 and all admissible matching sizes, finds actual primitive periods, and verifies the divisor-sum counts and sharp maximum periods. The outputs are embedded as `checks/verify_scan.out` and `checks/verify_direct.out`. Compile using `c++ -O2 -std=c++17 code/verify_direct.cpp -o verify_direct` and execute `./verify_direct`; run the Python script with `python3 code/verify_scan.py`. Neither program is an exhaustive test over all graph sizes or finite fields; the unbounded claims are proved algebraically above.

For example, at \(n=8\) the possible maximal periods for \(k=0,1,2\) are respectively \(9,7,10\). At \(k=2\), the populations of least periods \(1,2,5,10\) are \(4,12,60,180\), summing to \(2^8\).

## Relationship to prior work

Sequential graph dynamical systems and their dependence on scan order are established in Aledo, Martínez and Valverde's survey. Chen and Reidys give a general matrix representation of linear sequential systems (arXiv:1510.04930, Theorem 3.1). Neither general framework states the present explicit matching-block similarity, precise Jordan ranks, fixed-point counts, and nonmonotone two-edge order amplification. The single-deleted-edge case is separately known, and is treated here only as the comparison baseline, not as an independently new result.

A method-oriented earlier paper by Chen, Li and Zheng analyzes linear sequential dynamics on digraphs (DOI:10.1016/j.amc.2003.10.023). Only its abstract could be inspected; this is a residual prior-art uncertainty and no claim is made that its unread full text excludes a related specialization. Searches did not locate an equivalent formula for this particular family and scan, but literature discovery is not a proof of historical novelty.

## Limitations

The classification is limited to the specified matching-block scan on even-order matching-deleted complete graphs and finite characteristic-two fields. It does not extend automatically to interleaved scans, odd-order graphs, or other fields. The algorithms verify a finite range while the theorem relies on the exact coordinate conjugacy. Earlier general linear-system matrix formulas could compute particular examples but do not themselves establish that the formulas here were historically unknown.

## References

1. Ricky X. F. Chen and Christian M. Reidys, *Linear sequential dynamical systems, incidence algebras, and Möbius functions*, arXiv:1510.04930, first posted 2015-10-16. https://arxiv.org/abs/1510.04930
2. Juan A. Aledo, Silvia Martínez and Jose C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), article 594294, first published 2015-03-24. https://doi.org/10.1155/2015/594294
3. William Y. C. Chen, Xueliang Li and Jie Zheng, *Matrix method for linear sequential dynamical systems on digraphs*, Applied Mathematics and Computation 160 (2005), 197–212. https://doi.org/10.1016/j.amc.2003.10.023
