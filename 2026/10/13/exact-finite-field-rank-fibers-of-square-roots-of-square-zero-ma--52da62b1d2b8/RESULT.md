# Exact finite-field rank fibers of square roots of square-zero matrices
## Finding
Fix a prime power \(q\), an integer \(n\ge1\), and a matrix \(N\in M_n(\mathbb F_q)\) with \(N^2=0\) and \(\operatorname{rank}N=r\). Write \(m=n-2r\). The rank-refined square-root fiber polynomial is
\[
\mathcal F_{N,q}(T)=\sum_{X\in M_n(\mathbb F_q):\ X^2=N}T^{\operatorname{rank}X}.
\]
Define the finite products \(U_h(q)=\prod_{i=1}^h(1-q^{-i})\), with \(U_0(q)=1\). For nonnegative integers \(a_1,a_2,a_3,a_4\), put
\[
D(a_1,a_2,a_3,a_4)=\sum_{\ell=1}^4\left(\sum_{j=\ell}^4a_j\right)^2,
\qquad Z_q(a_1,a_2,a_3,a_4)=q^{D(a_1,a_2,a_3,a_4)}\prod_{j=1}^4 U_{a_j}(q).
\]
**Theorem (complete finite-field square-root rank fiber).** For all such \(q,n,r,N\),
\[
\boxed{\mathcal F_{N,q}(T)=
\sum_{\substack{0\le a\le\lfloor r/2\rfloor\\b=r-2a\\0\le c\le\lfloor(m-b)/2\rfloor\\d=m-b-2c}}
\frac{q^{(m+r)^2+r^2}U_m(q)U_r(q)}{Z_q(d,c,b,a)}\,T^{3a+2b+c}.}
\]
The sum is empty whenever its stated nonnegative-integer constraints are inconsistent. Each individual summand is a positive integer.

A square root exists **if and only if** \(r\) is even or \(m\ge1\). When one exists, the set of its possible ranks is exactly the full integer interval
\[
\boxed{\left\lceil\frac{3r}{2}\right\rceil\le \operatorname{rank}X\le\left\lfloor\frac{n+r}{2}\right\rfloor.}
\]
The polynomial depends on \(N\) only through \((n,r,q)\). It counts *individual matrices*, not only similarity classes of possible roots.

## Assumptions and scope
All matrices have entries in \(\mathbb F_q\), without any restriction on the characteristic. The target is a *fixed* square-zero matrix. Its rational nilpotent Jordan partition is \((2^r,1^m)\). The summation variables are nonnegative integers; an empty product equals one and an empty sum zero. The formula covers \(r=0\), hence the enumeration of square-zero matrices by rank, as well as nonzero targets.

## Proof
**1. Exact possible root Jordan partitions.** If \(X^2=N\), then \(X^4=N^2=0\). Thus \(X\) is nilpotent and has Jordan blocks of size at most four, over \(\mathbb F_q\) itself. For \(j=1,2,3,4\), squaring a nilpotent Jordan block of size \(j\) splits it into blocks with sizes differing by at most one. Explicitly, the corresponding squared partitions are respectively \((1)\), \((1,1)\), \((2,1)\), and \((2,2)\). Hence if \(X\) has partition \((4^a,3^b,2^c,1^d)\), comparison with the fixed target partition \((2^r,1^m)\) is equivalent to
\[
2a+b=r,\qquad b+2c+d=m.
\]
Conversely these equations guarantee \(X^2\) is *similar* to \(N\), since nilpotent Jordan form is canonical over the finite base field. Its rank is \(3a+2b+c\).

**2. Finite-field centralizer orders.** Consider an arbitrary nilpotent matrix \(Y\) of partition \((1^{a_1},2^{a_2},3^{a_3},4^{a_4})\). As an \(\mathbb F_q[t]\)-module its underlying space is \(\bigoplus_{j=1}^4(\mathbb F_q[t]/(t^j))^{a_j}\). The algebra of endomorphisms commuting with \(Y\) has \(\mathbb F_q\)-dimension \(\sum_{i,j}\min(i,j)a_i a_j=\sum_{\ell=1}^4(\sum_{j\ge\ell}a_j)^2\). Modulo its Jacobson radical, its unit group maps onto \(\prod_j\mathrm{GL}_{a_j}(\mathbb F_q)\), with a kernel of the expected affine cardinality. Therefore
\[
|C_{\mathrm{GL}_n(\mathbb F_q)}(Y)|=q^{D(a_1,a_2,a_3,a_4)}\prod_{j=1}^4\prod_{h=1}^{a_j}(1-q^{-h})=Z_q(a_1,a_2,a_3,a_4).
\]
For \(N\) with partition \((2^r,1^m)\) this is \(q^{(m+r)^2+r^2}U_m(q)U_r(q)\).

**3. Exact fiber multiplicities.** Fix an admissible root partition \(\lambda=(4^a,3^b,2^c,1^d)\). Every matrix of class \(\lambda\) has square in the single similarity class of \(N\). Conjugation by \(\mathrm{GL}_n(\mathbb F_q)\) acts transitively on this target class, so each fixed target receives the same number of square roots of type \(\lambda\). Orbit-stabilizer gives
\[
\#\{X:X^2=N,\ \operatorname{type}(X)=\lambda\}=
\frac{|\mathrm{GL}_n|/Z_q(d,c,b,a)}{|\mathrm{GL}_n|/|C_{\mathrm{GL}_n}(N)|}
=\frac{q^{(m+r)^2+r^2}U_m(q)U_r(q)}{Z_q(d,c,b,a)}.
\]
In particular the displayed rational-looking expression is a positive integer. Sum over all admissible partitions, using their ranks from step one, to obtain the theorem.

**4. Existence and exact rank interval.** If \(r\) is even, take \(a=r/2\), \(b=0\), \(c=d=0\) initially, and distribute the available \(m\) one-blocks using \(c\) and \(d\). If \(r\) is odd, every admissible type has odd \(b\), so \(m\ge1\) is necessary; it is sufficient to choose \(a=(r-1)/2\), \(b=1\). Fix \(a=\lfloor r/2\rfloor\) and \(b\in\{0,1\}\) in either case. As \(c\) runs over \(0,1,\ldots,\lfloor(m-b)/2\rfloor\), with \(d=m-b-2c\), the ranks \(3a+2b+c\) run through every integer from \(\lceil 3r/2\rceil\) through \(\lfloor(n+r)/2\rfloor\). For arbitrary admissible \(a,c\), \(\operatorname{rank}X=2r-a+c\ge2r-\lfloor r/2\rfloor\), and the constraint \(2c\le m-r+2a\) implies \(2\operatorname{rank}X\le3r+m=n+r\). These are the same endpoints, proving the claimed exact support.

## Verification
The accompanying standalone `verify.py` uses integer arithmetic and exact finite-field operations to enumerate every matrix in \(M_n(\mathbb F_q)\) for \((n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)\). It directly squares each matrix and independently computes its rank, comparing every fixed canonical square-zero target with the symbolic formula. The extension field \(\mathbb F_4\) is implemented using \(t^2+t+1\). Further coefficient and sharp-support consistency checks cover \(1\le n\le15\) and field orders \(2,3,4,5,7\). Expected terminal output: `VERIFY_OK_NILPOTENT_SQUARE_ROOT_FIBERS`.

For a nonzero target of rank one in dimension three, the formula yields \(q(q-1)\) roots, all of rank two. In dimension five, rank one, the polynomial is
\[
q^3(q^3-1)T^2+q^3(q^2-1)(q^3-1)T^3.
\]
For \((n,r,q)=(6,2,2)\), the rank-three and rank-four multiplicities are \(192\) and \(672\), respectively. These examples are finite checks; they do not replace the general proof above.

## Relationship to prior work
The classical work of Borwein–Richmond and the subsequent treatment by Öztürk describe the existence and Jordan-block structures of nilpotent roots. These antecedents already imply the admissible partitions in step one and should not be construed as novel here. The finite-field centralizer-order formula is classical as well. The present finite-field assertion is their combination into the **complete rank-refined cardinality of the fiber over each fixed square-zero matrix**, including its exact coefficients for arbitrary \(n\), \(q\), and \(r\). Britnell–Wildon address commuting similarity classes, and Oblak addresses possible commuting nilpotent indices, rather than these fixed power-map fiber sizes. Hua studies simultaneous-conjugacy orbits of nilpotent tuples rather than this individual-root count. The literature comparison is not an assertion of absolute priority.

## Limitations
The target is required to satisfy \(N^2=0\); no formula is asserted for arbitrary nilpotent targets or nonnilpotent matrices. The proof establishes cardinalities over finite fields and all ranks, not geometric properties of the root varieties or an independent novelty certification. An equivalent finite-field fiber enumeration might exist in less accessible literature. Independent mathematical audit has not been performed.

## References
- P. Borwein and L. B. Richmond, *How Many Matrices Have Roots?*, Canadian Journal of Mathematics 36(2), 1984, 286–299. DOI: 10.4153/CJM-1984-018-0. Full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F9E87144067D96B0AF5E918476A4A5EB/S0008414X00021660a.pdf/how-many-matrices-have-roots.pdf
- P. Oblak, *The upper bound for the index of nilpotency for a matrix commuting with a given nilpotent matrix*, arXiv:math/0701561, 2007, https://arxiv.org/html/math/0701561v2
- J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, 2010, https://arxiv.org/abs/1001.0811
- S. Öztürk, *On m-th roots of nilpotent matrices*, Electronic Journal of Linear Algebra, 2021, author manuscript https://users.metu.edu.tr/sozkap/fixedmthroot.pdf
- J. Hua, *On Numbers of Tuples of Nilpotent Matrices over Finite Fields under Simultaneous Conjugation*, arXiv:2102.07290, 2021, https://arxiv.org/abs/2102.07290
