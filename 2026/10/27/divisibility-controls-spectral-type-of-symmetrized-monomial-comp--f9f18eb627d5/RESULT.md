# Divisibility controls spectral type of symmetrized monomial composition products

## Finding
For distinct integers \(m,n\ge2\), on \(H^2(\mathbb D)\) write \(U_m=C_{z^m}\), \(U_n=C_{z^n}\), and form the self-adjoint operator
\[H_{m,n}=U_mU_n^*+U_nU_m^*.\]
Its spectrum and Fredholm essential spectrum both equal \([-2,2]\), and \(2\) is always an eigenvalue from the constants. Nevertheless its spectral type changes arithmetically:

1. If \(m\mid n\) or \(n\mid m\), then \(H_{m,n}\) is unitarily equivalent to \([2]\oplus0_{\infty}\oplus\bigoplus_{j=1}^{\infty}(S+S^*)\), where \(S\) is the unilateral shift on \(\ell_2(\mathbb N_0)\). Its absolutely continuous spectrum fills \([-2,2]\), its only eigenvalues are \(0\) and \(2\), and it has no singular-continuous part.
2. If neither integer divides the other, then \(H_{m,n}\) is unitarily equivalent to \([2]\oplus\bigoplus_{\ell=1}^{\infty}\bigoplus_{j=1}^{\infty}A_\ell\), where \(A_\ell\) is the adjacency matrix of a path with \(\ell\) vertices (including the zero matrix when \(\ell=1\)). Its spectral measure is purely atomic for every vector; its eigenvalues are exactly
\[\{2\}\cup\left\{2\cos\left(\frac{\pi j}{\ell+1}\right):\ell\ge1,\ 1\le j\le\ell\right\},\]
which are dense in \([-2,2]\), but \(-2\) is not an eigenvalue.

Thus the *same* spectral interval is purely point in the nondivisible case and has a nontrivial absolutely continuous component of infinite multiplicity in the divisible case.

## Assumptions and scope
All operators act on the usual complex Hardy Hilbert space with orthonormal basis \(e_k(z)=z^k\), \(k\ge0\). The symbols are distinct integral monomials of degrees at least two. The operator \(H_{m,n}\) is the self-adjoint sum of the product and its adjoint, not the product alone. Pure-point spectrum refers to the completeness of eigenvectors (all spectral measures atomic), not merely density of the point spectrum. Essential spectrum is Fredholm essential spectrum. The unilateral shift \(S\) has multiplicity one; countably many copies occur.

## Proof
Since \(U_a e_k=e_{ak}\), \(U_a\) is an isometry and
\[U_n^*e_k=\begin{cases}e_{k/n},&n\mid k,\\0,&n\nmid k.\end{cases}\]
In particular \(U_mU_n^*e_0=e_0\). On positive indices, \(T=U_mU_n^*\) maps \(e_{nk}\) to \(e_{mk}\) for \(k\ge1\), annihilating the other basis vectors. Regard this as the directed graph with edges \(nk\to mk\), \(k\ge1\). Since source and target are individually unique, every vertex has indegree and outdegree at most one. A directed cycle would imply \((m/n)^j=1\) for some positive \(j\), impossible for distinct positive \(m,n\). The operator \(T+T^*\) therefore is the adjacency operator of the graph's undirected path components, with weight one on each edge.

If \(m=nr\) for an integer \(r\ge2\), the positive multiples of \(n\) are invariant under \(T\), and under the basis identification \(e_{nk}\mapsto e_k\) it acts as \(e_k\mapsto e_{rk}\). Every positive \(k\) is uniquely \(r^hu\), with \(r\nmid u\) and \(h\ge0\). For each such \(u\), the orbit is a unilateral ray, and there are infinitely many \(u\). Every positive index outside \(n\mathbb N\) is isolated. Thus the asserted decomposition holds. If \(n=mr\), interchange \(m,n\) (which replaces \(T\) by \(T^*\) but fixes \(H_{m,n}\)).

Otherwise both quotients \(m/n\) and \(n/m\) are nonintegral. Choose primes \(p,q\) satisfying \(v_p(n)>v_p(m)\) and \(v_q(m)>v_q(n)\). Along every forward edge the \(p\)-valuation decreases by the positive amount \(v_p(n)-v_p(m)\), so there is no infinite forward path. Along every backward edge the \(q\)-valuation decreases by \(v_q(m)-v_q(n)\), so there is no infinite backward path. Consequently every component is finite.

Moreover, every path size appears infinitely often. For a prescribed \(L\ge1\) number of edges, put \(a_s=v_s(n)\), \(b_s=v_s(m)\), and choose the positive integer \(k_0\) with
\[v_s(k_0)=a_s+(L-1)\max\{a_s-b_s,0\}\]
for each prime \(s\) dividing \(mn\), and valuation zero elsewhere. Then \(k_j=k_0(m/n)^j\), \(0\le j\le L\), are all integers; \(n\mid k_j\) for \(j<L\), but \(n\nmid k_L\) because \(v_p(k_L)=b_p<a_p\). There is no predecessor to \(k_0\), since \(v_q(k_0)=a_q<b_q\), so \(m\nmid k_0\). These \(L+1\) vertices therefore form an entire path. Multiplying every vertex by any prime not dividing \(mn\) produces pairwise distinct full path components of the same size. The isolated components of length one also occur infinitely often, e.g. sufficiently many positive indices coprime to \(mn\). Hence every \(A_\ell\) has infinite multiplicity.

The path adjacency \(A_\ell\) has an orthonormal eigenbasis of discrete sine vectors with eigenvalues \(2\cos(\pi j/(\ell+1))\), \(1\le j\le\ell\). These eigenvectors, the isolated basis vectors, and \(e_0\) form an orthonormal basis for the nondivisible case, proving pure-point spectral type and the eigenvalue formula. Their eigenvalues are dense in \([-2,2]\); the operator norm is two, which gives the spectrum. Every eigenvalue has infinite multiplicity on positive indices, while the eigenvalue two from \(e_0\) is also a limit point. Thus every spectral point is essential.

In the divisible case, the standard discrete sine transform \(e_j\mapsto\sqrt{2/\pi}\sin((j+1)\theta)\) identifies \(S+S^*\) with multiplication by \(2\cos\theta\) on \(L^2((0,\pi),d\theta)\), giving purely absolutely continuous spectral type and spectrum \([-2,2]\), with no eigenvalues. The complementary isolated vertices give eigenvalue zero of infinite multiplicity and the constant gives eigenvalue two. Infinitely many shift copies make the whole interval essential. This concludes all assertions.

## Verification
The formulas are exact and do not rely on finite enumeration. A separate finite graph diagnostic examined pairs \((m,n)\) equal to \((2,3),(6,4),(12,18),(6,3),(3,6),(4,2),(4,9),(24,18),(25,10),(2,5)\), using positive vertices up to 15000, and confirmed that sampled components were paths of degree at most two. The finite cutoff is not used to establish spectral type or completeness; the infinite valuation argument and explicit path construction supply those proofs.

## Relationship to prior work
Leng and Zhao (arXiv:2610.15472v1, first posted 11 October 2026) investigate Schatten membership of products \(C_\varphi C_\psi^*\) and \(C_\psi^*C_\varphi\) on Hardy/Bergman spaces, including finite Blaschke and inner symbols; their Theorem 3.24 gives a Schatten-class equivalence for inner right symbols. Their results address ideal membership, not the self-adjoint symmetrization's arithmetic spectral-type classification. General unilateral-shift and finite-Jacobi-matrix spectral theory supplies the sine diagonalizations, but the all-pairs multiplicative orbit decomposition and divisibility criterion require separate analysis.

## Limitations
Only integral monomial symbols and the symmetrized two-term operator are treated. No claim is made that the point-spectrum sets determine the ordered pair \((m,n)\); indeed these sets are constant within each divisibility class. A full historical priority check for equivalent graph-operator formulations remains necessary. The finite diagnostic does not certify an infinite theorem.

## References
1. Qianrui Leng and Xianfeng Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1 (11 October 2026), https://arxiv.org/html/2610.15472v1.
2. Classical unilateral-shift spectral theory (discrete sine transform) and finite path Jacobi matrices; their required identities are proved above, without reliance on uninspected external lemmas.
