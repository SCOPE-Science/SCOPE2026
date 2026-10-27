# Equational probability spectra of finite Takasaki quandles recover their abelian groups

## Finding

For every nontrivial finite abelian group \(A\), let \(T(A)\) denote the one-operation algebra on \(A\) with \(x\triangleright y=2y-x\). Then

\[\operatorname{PSpec}(T(A))=\left\{\frac{|A[d]|}{|A|}:d\mid\exp(A)\right\},\qquad A[d]=\{a\in A:da=0\}.\]

Moreover this *unordered set of probabilities* determines the isomorphism type of \(A\). The spectrum is minimal, namely \(\{1/|A|,1\}\), if and only if \(A\) is an elementary abelian group of prime exponent. If \(A_p\) has exponent \(p^{e_p}\), then \(|\operatorname{PSpec}(T(A))|=\prod_{p\mid|A|}(e_p+1)\). In the cyclic case \(A=\mathbb Z/n\mathbb Z\), the spectrum is \(\{d/n:d\mid n\}\).

## Assumptions and scope

\(A\) is a nontrivial finite abelian group (written additively). The language contains exactly the binary operation \(\triangleright\), with no named constants, division operations, or underlying group addition. For terms \(t,s\) in their \(k\ge1\) distinct variables, \(\Pr_A(t=s)\) is the number of assignments satisfying the equation divided by \(|A|^k\). The equational probability spectrum is the set of these values for all such equations and all finite \(k\).

Let \(\exp(A)\) be the smallest positive integer annihilating \(A\). Define \(A[0]=A\) and \(A[d]\) for any integer \(d\) by the kernel of multiplication by \(d\). For prime \(p\), let \(A_p\) be the \(p\)-primary direct summand and write \(\exp(A_p)=p^{e_p}\).

## Proof

**1. Every equation has one scalar image.** By induction on term formation, every term in \(k\) variables is an integral affine expression \(t(x_1,\ldots,x_k)=\sum_{i=1}^k a_i x_i\) with \(\sum_i a_i=1\): each variable has this property, while the operation sends two coefficient vectors \(a,b\) to \(2b-a\), preserving their coefficient sum. Hence an equation \(t=s\) is equivalent to \(\sum_i c_i x_i=0\), where \(\sum_i c_i=0\) and all \(c_i\) are integers.

Set \(g=\gcd(c_1,\ldots,c_k)\), taking \(g=0\) when all coefficients vanish. The image of the group homomorphism \(F:A^k\to A\), \(F(x)=\sum_i c_i x_i\), is \(gA\). Containment in \(gA\) is immediate; the reverse inclusion follows from Bézout's identity (if \(g=0\), both images equal \(\{0\}\)). Every fiber of a homomorphism of finite groups has the same size, so

\[\Pr_A(t=s)=\frac{|\ker F|}{|A|^k}=\frac{1}{|gA|}=\frac{|A[g]|}{|A|}.\]

Because multiplication by \(g\) and by \(\gcd(g,\exp(A))\) have equal kernels, the probability belongs to the claimed finite set of values indexed by positive divisors of \(\exp(A)\).

**2. Every torsion ratio occurs as a two-variable equation.** Restrict to terms in variables \(x,y\). An integral affine term \(a x+(1-a)y\) is represented by its first coefficient \(a\). Variables \(x,y\) represent \(1,0\); the operation takes the pair of integers \((a,b)\) to \(2b-a\). Its closure contains every integer: from adjacent \(a,a+1\) it contains both \(a-1=2a-(a+1)\) and \(a+2=2(a+1)-a\), and induction starting at \(0,1\) generates all integers. Thus for each positive integer \(d\) some binary term \(t_d\) evaluates to \((d+1)x-dy\). The equation \(t_d(x,y)=x\) is exactly \(d(x-y)=0\), with probability \(|A[d]|/|A|\). This establishes the reverse inclusion. All term constructions are finite, though their size may depend on \(d\).

**3. Recover the abelian group from the unordered probabilities.** The least spectrum element is \(1/|A|\), since \(x=y\) attains it and every displayed ratio has numerator at least one. Thus the spectrum determines \(N=|A|\) and the integer set \(\mathcal T=\{N\alpha:\alpha\in\operatorname{PSpec}(T(A))\}=\{|A[d]|:d\mid\exp(A)\}\).

For each prime \(p\mid N\), form the strictly increasing list of the elements of \(\mathcal T\) that are powers of \(p\):

\[1=p^{s_0}<p^{s_1}<\cdots<p^{s_{e_p}}=|A_p|.\]

These are *exactly* the successive cardinalities \(|A_p[p^j]|\), \(0\le j\le e_p\). Indeed, the primary decomposition gives \(|A[d]|=\prod_q|A_q[d]|\); a pure \(p\)-power factor forces every \(q\ne p\) factor to be one. Conversely taking \(d=p^j\) realizes each \(p\)-power torsion subgroup, and these sizes strictly increase for \(j<e_p\). The integer \(s_j-s_{j-1}\) is exactly the number of cyclic \(p\)-primary factors whose orders are at least \(p^j\). Therefore the multiplicity of \(\mathbb Z/p^j\mathbb Z\) is

\[(s_j-s_{j-1})-(s_{j+1}-s_j),\]

where \(s_{e_p+1}=s_{e_p}\). This recovers all elementary divisors, hence determines \(A\) up to isomorphism.

**4. Further consequences.** For each \(p\), precisely the \(e_p+1\) values \(|A_p[p^j]|\) occur, and products across distinct primes are pairwise distinct by unique prime factorization. Thus the number of probabilities is \(\prod_p(e_p+1)\). It equals two exactly when \(N\) has only one prime divisor and \(e_p=1\), i.e. \(A\) is nontrivial elementary abelian of prime exponent. For cyclic \(A\) of order \(n\), \(|A[d]|=\gcd(n,d)\), so the displayed spectrum consists of all positive divisor ratios \(d/n\).

## Verification

The standalone `verify.py` enumerates all binary-term coefficient classes modulo the exponent for fifteen finite direct products of cyclic groups, exhaustively compares each pair of resulting binary terms on the group's \(|A|^2\) input pairs, and reconstructs the elementary divisors from the unordered resulting spectrum. It returned `VERIFY_OK 15`. These are finite checks; the proof above handles all finite abelian groups, all equations, and unbounded term depth.

## Relationship to prior work

Carles Cardó's 2026 works introduce and analyze equational probability spectra and prove minimality constraints for groupoids, including examples for cyclic groups in the *group signature* and a complete semigroup minimality classification [1,2]. The present result instead determines the full set of probabilities for the binary-only *nonassociative* Takasaki quandle of an arbitrary finite abelian group, and proves the stronger reconstruction theorem. The shared linear-algebraic observation about homomorphism fibers is elementary; the identified new statement is the complete core-quandle spectrum and its reconstruction power. Work of Sakia and Kiania concerns reconstruction from the *lattice of subquandles*, an invariant different from this probability set [3].

## Limitations

The result does not concern arbitrary Alexander quandles, nonabelian core quandles, or signatures enlarged by constants and other operations. It does not claim that different kinds of quandles with the same spectrum must be isomorphic. Sources outside the inspected material, including unindexed manuscripts, may contain equivalent conclusions. The computational examples cannot establish the infinite-family theorem independently.

## References

[1] C. Cardó, *On semigroups and groupoids with minimal probabilistic spectrum*, arXiv:2603.19487v1 (first posted 19 March 2026); inspected using the full freely accessible arXiv HTML of v2, https://arxiv.org/html/2603.19487v2.

[2] C. Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446v1 (first posted 9 April 2026), full HTML https://arxiv.org/html/2604.08446v1.

[3] A. Sakia and D. Kiania, *On the lattice of subquandles of a Takasaki quandle*, Communications in Algebra 49 (2021), 99–113, doi:10.1080/00927872.2020.1797065; title and abstract examined.
