# Exact mixed-prime formula for a finite abelian factor

## Finding
For every nontrivial finite \(p\)-group \(P\) and finite abelian \(q\)-group \(A\) with \(p\ne q\), the minimum degree of a faithful complex representation satisfies \(\delta(P\times A)=\delta(P)+\max\{0,d(A)-d(Z(P))\}\). Equivalently, the saving relative to \(\delta(P)+\delta(A)\) is exactly \(\min\{d(A),d(Z(P))\}\), where \(d(B)\) is the minimum number of generators of a finite abelian group \(B\).
Here \(\delta(X)\) denotes the minimum degree of a faithful complex representation of a finite group \(X\). In particular, the formula is a statement about complex linear representations, not permutation or projective representations.

## Assumptions and scope
All groups are finite; representations are complex and linear. The primes \(p\) and \(q\) are distinct. The group \(P\) is nontrivial, and \(A\) is a finite abelian \(q\)-group. The notation \(Z(P)\) means the center of \(P\). The result does not assume that \(P\) is extraspecial, normally monomial, or of a fixed nilpotency class.

## Proof
Put \(s=d(Z(P))\) and \(r=d(A)\). Every irreducible representation of \(P\times A\) is a tensor product \(\rho\otimes\lambda\), where \(\rho\) is irreducible for \(P\) and \(\lambda\) is a linear character of \(A\).

First, for every such pair,
\[
\ker(\rho\otimes\lambda)=\ker\rho\times\ker\lambda.
\]
Indeed, if \(\rho(g)\lambda(a)=I\), then \(\rho(g)\) is a scalar whose order is a power of \(p\), while \(\lambda(a)\) has order a power of \(q\). Since \(p\ne q\), the common scalar must be \(1\); hence \(g\in\ker\rho\) and \(a\in\ker\lambda\). The reverse inclusion is immediate. Consequently, a direct sum of tensor products is faithful precisely when its selected \(P\)-characters have trivial common kernel and its selected \(A\)-characters have trivial common kernel.

For a finite abelian group \(B\), a set of linear characters has trivial common kernel exactly when it generates the dual character group. Thus at least \(r\) constituents are needed to separate \(A\). Also, any faithful set of irreducible characters of \(P\) contains a faithful subset of size \(s\): their restrictions to \(Z(P)\) generate its dual, and a minimal generating subset has size \(s\); a nontrivial normal subgroup of a finite \(p\)-group intersects its center nontrivially. In particular, a minimum-degree faithful representation of \(P\) has exactly \(s\) irreducible constituents.

Consider any faithful representation of \(P\times A\) with \(m\) irreducible constituents. The two preceding observations give \(m\ge r\) and a subset of \(s\) constituents whose \(P\)-parts are faithful. The sum of the degrees of that subset is at least \(\delta(P)\); each remaining constituent has degree at least \(1\). Therefore its total degree is at least
\[
\delta(P)+\max\{0,r-s\}.
\]

For the reverse inequality, take a minimum-degree faithful representation of \(P\) with its \(s\) irreducible constituents. Choose \(r\) characters generating the dual of \(A\). If \(r\le s\), attach these characters to \(r\) of the \(P\)-constituents and attach the trivial character to the others. This gives a faithful representation of degree \(\delta(P)\). If \(r>s\), attach the first \(s\) generating characters to the \(P\)-constituents and add \(r-s\) one-dimensional constituents inflated from the remaining generators of \(A\). The resulting faithful representation has degree \(\delta(P)+r-s\). The lower and upper bounds agree, proving the formula.

## Verification
The key kernel identity is checked for every irreducible tensor factor, not only for a chosen example. The lower bound uses the minimum number of generators of the center and of \(A\); the upper bound constructs a faithful character set in both boundary regimes \(r\le s\) and \(r>s\). No finite computation is used as a substitute for the universal argument. As consistency checks, the formula gives degree \(3\) for the product of an extraspecial group of order \(8\) with \(C_3^2\), and degree \(3\) for the order-\(16\) example with center rank two multiplied by \(C_3^2\), matching the two corresponding examples in the 2026 source.

## Relationship to prior work
The 2026 paper on representation dimensions of finite \(p\)-groups proves additivity for two factors of the same prime and explicitly shows that additivity can fail for nilpotent groups of distinct prime orders. Its mixed-prime examples include an extraspecial group times \(C_3^2\) and a group with center \(C_2^2\) times \(C_3^2\). The present statement supplies an exact formula for every finite \(p\)-group \(P\) and every finite abelian \(q\)-group \(A\) with \(p\ne q\), rather than only isolated examples. The known center-rank description of minimal faithful representations of \(p\)-groups and the identity \(\delta(A)=d(A)\) are inputs; the new comparison is the exact rank correction for the coprime direct product.

## Limitations
The abelian factor must have prime-power order coprime to \(|P|\). The formula does not cover a nonabelian second factor, a same-prime direct product, or representations over fields of positive characteristic. Literature searches cannot rule out an older implicit equivalent; the novelty assessment is therefore comparative rather than an absolute proof of priority. Independent audit has not been performed.

## References
1. G. Kaur, A. Kulshrestha, and A. Udeep, “On the representation dimension of finite \(p\)-groups,” arXiv:2608.18814v1 (first public 19 August 2026), especially §2, Lemma 1, and §3, Theorem 2 and Example 2.
2. A. Meyer and Z. Reichstein, “Some consequences of the Karpenko–Merkurjev theorem,” *Documenta Mathematica*, Extra Volume: Suslin (2010), Theorem 1.2.
3. A. Moretó, “On the minimal dimension of a faithful linear representation of a finite group,” arXiv:2102.01463v3 (2021), especially the discussion of faithful constituents for \(p\)-groups and Lemma 3.4 on finite abelian groups.
