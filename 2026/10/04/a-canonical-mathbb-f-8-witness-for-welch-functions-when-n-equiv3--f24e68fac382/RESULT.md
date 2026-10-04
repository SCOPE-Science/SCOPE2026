# A canonical \(\mathbb F_8\) witness for Welch functions when \(n\equiv3\pmod 6\)
## Finding
For every odd integer \(n=2m+1\ge 9\) with \(3\mid n\), the Welch function \(W_n(X)=X^{2^m+3}\) on \(\mathbb F_{2^n}\) is not third-order sum-free. The unique subfield \(\mathbb F_8\subset\mathbb F_{2^n}\), viewed as a three-dimensional \(\mathbb F_2\)-linear subspace, is an explicit zero-sum witness: \(\sum_{x\in\mathbb F_8}W_n(x)=0\). Equivalently, the Hou--Zhao obstruction polynomial \(g(X,Y)\) vanishes identically on \(\mathbb F_8^2\). Hence their Conjecture 5.10 is proved for the infinite progression \(n\equiv3\pmod 6\).

This gives a canonical witness, rather than a determinant or search certificate, for every admissible dimension in the progression \(n\equiv3\pmod 6\). In particular it contains the computed cases \(n=9\) and \(n=15\) from the motivating paper and extends them to infinitely many dimensions.

## Assumptions and scope
Let \(n=2m+1\ge9\) be odd and suppose \(3\mid n\). The Welch function is
\[
W_n:\mathbb F_{2^n}\to\mathbb F_{2^n},\qquad W_n(x)=x^{2^m+3}.
\]
A function on \(\mathbb F_{2^n}\) is third-order sum-free when the sum of its values over every three-dimensional \(\mathbb F_2\)-affine subspace is nonzero. The claim concerns only the progression \(3\mid n\); it does not settle dimensions coprime to \(3\).

## Proof
Because \(3\mid n\), finite-field subfield theory gives the unique subfield \(A=\mathbb F_8\subset\mathbb F_{2^n}\). As an \(\mathbb F_2\)-vector space, \(A\) has dimension three, so it is an allowed affine subspace.

Write \(n=6r+3\). Then \(m=(n-1)/2=3r+1\), hence \(m\equiv1\pmod3\). For every nonzero \(x\in\mathbb F_8\), one has \(x^7=1\), while the powers of \(2\) modulo \(7\) have period three. Therefore
\[
2^m+3\equiv 2+3\equiv5\pmod7.
\]
Consequently
\[
\sum_{x\in\mathbb F_8}W_n(x)=\sum_{x\in\mathbb F_8^\times}x^5.
\]
If \(\zeta\) generates the cyclic group \(\mathbb F_8^\times\) of order seven, then
\[
\sum_{x\in\mathbb F_8^\times}x^5=\sum_{j=0}^6\zeta^{5j}=0,
\]
because \(\zeta^5\ne1\). Thus \(A=\mathbb F_8\) is a zero-sum three-flat, and \(W_n\) is not third-order sum-free.

The same witness is visible directly in the polynomial criterion of Hou--Zhao. Their obstruction is
\[
g(X,Y)=Y^{2^m}(X^2+X)+Y^2(X^{2^m}+X)+Y(X^{2^m}+X^2).
\]
On \(\mathbb F_8\), the congruence \(m\equiv1\pmod3\) gives \(z^{2^m}=z^2\). Substitution makes the first two terms equal and the third zero, so \(g\) vanishes identically on \(\mathbb F_8^2\). Choosing \(x\in\mathbb F_8\setminus\mathbb F_2\) and \(y\in\mathbb F_8\setminus\langle1,x\rangle\) therefore also satisfies their equivalent failure criterion.

## Verification
The standalone script `verify.py` implements \(\mathbb F_8\) as \(\mathbb F_2[z]/(z^3+z+1)\). It checks the field identities, the zero sum for every odd multiple of three through \(n=201\), and the identity \(g(x,y)=0\) for all \(64\) pairs in \(\mathbb F_8^2\). Its replay output is `VERIFY_OK n_cases=34 subfield_sum=0 g_pairs=64`. These finite checks are regression tests only; the infinite statement is proved above.

## Relationship to prior work
Hou and Zhao define third-order sum-freedom, derive an equivalent Dickson-matrix criterion for the Welch function, and state as Conjecture 5.10 that \(W_n\) is not third-order sum-free for every odd \(n\ge7\). Their Table 1 verifies dimensions through \(n=15\), including \(n=9\) and \(n=15\), but the inspected first public version does not give an infinite \(3\mid n\) argument or the \(\mathbb F_8\) witness. The earlier paper of Ebeling--Hou--Rydell--Zhao proves a \(3\mid n\) result for the multiplicative inverse function, a different power function, so it does not imply the present Welch statement.

The motivating preprint lists primary MSC2020 11G20 and was first publicly submitted on 2026-09-25. A later revision is catalogued on 2026-09-28; that revision was not materially available for full-text comparison here, so overlap with changes unique to that revision remains a bibliographic risk.

## Limitations
The proof settles only the progression \(n\equiv3\pmod6\), not the remaining odd dimensions in Conjecture 5.10. The novelty comparison is strongest against the full first public version of the motivating paper and indexed literature searched by the theorem's objects and equivalent formulations. An unindexed observation, or a change appearing only in the later revision, could reduce originality. The verifier is bounded and is not used as proof of the infinite theorem.

## References
1. X.-d. Hou and S. Zhao, *Further Results on Sum-Freedom of Binary and q-ary Functions*, arXiv:2609.31489v1, first submitted 2026-09-25; especially §5.3, Corollary 5.9, Conjecture 5.10, and Table 1.
2. A. Ebeling, X.-d. Hou, A. Rydell, and S. Zhao, *On Sum-Free Functions*, Finite Fields and Their Applications 110 (2026), Article 102744, DOI:10.1016/j.ffa.2025.102744; arXiv:2410.10426.
