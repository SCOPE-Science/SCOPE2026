# Frobenius-rank idempotent zeta laws for binary graph evolution algebras

## Finding
Let \(M\in M_n(\mathbb F_2)\). For each positive integer \(f\), form the evolution algebra \(E_{M,f}\) over \(\mathbb F_{2^f}\) with natural basis \(e_1,\ldots,e_n\) and products \(e_i e_j=0\) for \(i\ne j\), \(e_i^2=\sum_j M_{ji}e_j\). Let \(N_f\) be the number of idempotents (including zero). Then
\[
N_f=2^{\dim_{\mathbb F_2}\ker(M^f-I_n)}.
\]
In particular, this gives every extension-field idempotent count of every binary graph evolution algebra directly from a finite binary matrix.

Put \(U=\operatorname{im}(M^n)\), \(r=\dim_{\mathbb F_2}U\), and \(L=\operatorname{ord}(M|_U)\), with \(L=1\) when \(U=0\). Exactly \(2^r\) geometric idempotents exist over \(\overline{\mathbb F}_2\), their smallest common field of definition is \(\mathbb F_{2^L}\), and the corresponding Artin zeta function is
\[
Z_E(T)=\exp\!\left(\sum_{f\ge1}N_f\frac{T^f}{f}\right)
=\prod_{d\mid L}(1-T^d)^{-c_d},\qquad
c_d=\frac1d\sum_{e\mid d}\mu(d/e)\,2^{\dim\ker(M^e-I_n)}.
\]
Here \(c_d\) is a nonnegative integer: the number of Frobenius orbits of geometric idempotents of exact length \(d\).

For the cycle graph \(C_5\), \(N_f=1\) unless \(3\mid f\), when \(N_f=16\), and
\[
Z_{C_5}(T)=(1-T)^{-1}(1-T^3)^{-5}.
\]
For the Petersen-graph evolution algebra, \(N_f=32\) for odd \(f\), \(N_f=64\) for even \(f\), and
\[
Z_{\mathrm{Petersen}}(T)=(1-T)^{-32}(1-T^2)^{-16}.
\]

## Assumptions and scope
All matrices have entries in the prime field \(\mathbb F_2\). The index convention \(M_{ji}\) in the multiplication table ensures that coefficient vectors satisfy exactly \(x=Mx^{[2]}\), where \(x^{[2]}\) means coordinatewise squaring. No symmetry, invertibility, connectedness, or regularity of \(M\) is assumed. Undirected simple graphs supply symmetric zero-diagonal examples. Counts refer to the algebras obtained from the same binary structure matrix by extension of scalars; they are not claims for arbitrary structure constants varying with the extension field.

## Proof
**Normal-basis reduction.** For \(f\ge1\), choose a normal basis \(\beta_0,\ldots,\beta_{f-1}\) of \(\mathbb F_{2^f}/\mathbb F_2\), indexed cyclically so that \(\beta_j^2=\beta_{j+1}\). Express any coefficient vector uniquely as \(x=\sum_{j=0}^{f-1}\beta_jv_j\), with \(v_j\in\mathbb F_2^n\). Since the entries of \(M\) lie in \(\mathbb F_2\), the idempotent equation \(x=Mx^{[2]}\) becomes \(v_j=Mv_{j-1}\) for every cyclic index \(j\). Therefore the complete cyclic system is equivalent to choosing \(v_0\in\ker(M^f-I_n)\); all other \(v_j\) are determined by iteration. This is a bijection of \(\mathbb F_2\)-vector spaces and proves the exact count.

**Geometric count and minimum field.** The Fitting decomposition over \(\mathbb F_2\) is \(\mathbb F_2^n=\ker(M^n)\oplus U\). Both summands remain invariant under coordinatewise Frobenius after scalar extension. On the nilpotent summand, repeated substitution into \(x=Mx^{[2]}\) gives \(x=M^n x^{[2^n]}=0\). On \(U\), the matrix \(M\) is invertible, so any geometric solution satisfies \(x^{[2]}=M^{-1}x\) and hence \(x^{[2^L]}=M^{-L}x=x\). Thus all solutions lie in \(\mathbb F_{2^L}\). The normal-basis formula gives exactly \(2^r\) solutions there, as \(M^L|_U=I\). Moreover, all geometric solutions lie in \(\mathbb F_{2^f}\) precisely when \(\dim\ker(M^f-I)=r\), which occurs precisely when \((M|_U)^f=I\); equivalently \(L\mid f\). This proves both the geometric count and minimality of \(L\).

**Zeta function.** Frobenius permutes the finite set of \(2^r\) geometric solutions, and its permutation order is \(L\) by the preceding minimality result. A cycle of length \(d\) contributes \(d\) fixed points to the \(f\)-th Frobenius power exactly when \(d\mid f\). Thus \(N_f=\sum_{d\mid f}d c_d\), and Möbius inversion gives the stated \(c_d\). The standard formal logarithm identity for finite permutation cycles gives the product expression for \(Z_E(T)\). No convergence assumption on the formal variable \(T\) is involved.

**Cyclic Cayley formula.** Suppose \(M\) is multiplication by a polynomial \(a(t)\) on \(R=\mathbb F_2[t]/(t^n-1)\). Then \(\ker(M^f-I_n)\) is the kernel of multiplication by \(a(t)^f-1\). Euclidean division in \(\mathbb F_2[t]\) shows
\[
\dim\ker(M^f-I_n)=\deg\gcd(t^n-1,a(t)^f-1).
\]
For a cycle graph on \(n\ge3\) vertices, \(a(t)=t+t^{n-1}\). For \(C_5\), the binary adjacency matrix satisfies \(M^4=M\), \(\operatorname{rank}M=4\), and \(M\) has order three on its stable four-space. It has no nonzero vector fixed by \(M\) or \(M^2\), establishing the \(C_5\) formula.

**Petersen graph.** Label its ten vertices by the two-element subsets of \(\{1,2,3,4,5\}\), adjacent precisely when disjoint. The ordinary strongly regular parameters are \((10,3,0,1)\). Reducing the common-neighbor identity modulo two gives \(M^2=M+J\), where \(J\) is the all-ones matrix; consequently \(M^3=M\). Exact binary elimination on this explicit ten-by-ten matrix gives \(\dim\ker(M-I)=5\) and \(\operatorname{rank}(M^2)=6\). Since \(M^3=M\), odd powers equal \(M\), even positive powers equal \(M^2\), and the two idempotent counts and zeta factors follow.

## Verification
Run the standalone file `verify.py` with Python 3. It contains independent integer/bit-level matrix arithmetic and explicit finite-field multiplication in \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\). It exhaustively compares direct idempotent enumeration with the rank formula for **all 530 binary matrices of sizes one through three**, at each of the three extension degrees. It separately enumerates every field-valued vector for \(C_5\) over the fields of orders two, four, and eight, and for the Petersen graph over fields of orders two and four. The completed test prints `VERIFY_OK`. These finite checks do not substitute for the general normal-basis and Fitting proofs.

## Relationship to prior work
Giacomelli's *Expander Evolution Algebras* (first public version May 12, 2026; arXiv:2605.12672v1) defines graph-derived evolution algebras, treats the five-cycle and Petersen graph as named examples, and raises questions about finite-field algebraic invariants. The exact extension-field idempotent distribution, least splitting degree, and idempotent zeta function are not among its displayed results in the inspected relevant sections. Narkuziyev (arXiv:2005.05793; also arXiv:1803.11415) discusses idempotents of permutation-based evolution algebras, a different structural subfamily. Earlier special-family calculations establish parity-dependent idempotent counts for elementary-abelian Cayley graphs whose binary adjacency matrix squares to zero or the identity, and for complete graphs. Both are strict special cases of the present matrix-rank mechanism; neither provides the general matrix formula, arbitrary splitting degree, or zeta classification. Those earlier results are not represented as new here. The present theorem is a characteristic-two, prime-field-matrix transfer principle that applies to arbitrary binary structure matrices and gives complete arithmetic point counts; it is not an existence theorem for idempotents over arbitrary fields.

## Limitations
The formula requires \(M\) to be defined over \(\mathbb F_2\). For matrices with coefficients outside the prime field, Frobenius does not commute with the fixed coefficient matrix and the same \(M^f\) expression need not hold. It does not provide classifications of the idempotent multiplication table or automorphism groups. Exact uniqueness or priority cannot be inferred from research-index searches; equivalent unindexed work, including formulations as additive-polynomial fixed points, remains possible. 

## References
- P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1 (first posted 2026-05-12), https://arxiv.org/html/2605.12672 .
- B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793 (2020), https://arxiv.org/abs/2005.05793 .
- B. A. Narkuziyev, *On absolute nilpotent and idempotent elements of an evolution algebra corresponding to permutations*, arXiv:1803.11415 (2018), https://arxiv.org/abs/1803.11415 .
