# The smallest common-cover witness to finite-field BV non-rigidity
## Finding
For every odd prime \(p\), put \(K=\mathrm{SU}(4)\times\mathrm{SU}(2)\). Let
\[
\Gamma_4=\{(\zeta I_4,I_2):\zeta^4=1\}\cong C_4,\qquad
\Gamma_{22}=\{(\varepsilon I_4,\delta I_2):\varepsilon,\delta\in\{\pm1\}\}\cong C_2\times C_2.
\]
For \(G_4=K/\Gamma_4\) and \(G_{22}=K/\Gamma_{22}\), the shifted free-loop homology algebras over \(\mathbf F_p\) are isomorphic as graded algebras, equivalently as BV algebras, exactly when \(p\equiv1\pmod4\). When \(p\equiv3\pmod4\), they are not isomorphic. Rank \(4\) is minimal among such pairs having a common simply connected universal cover and fundamental groups \(C_4\) and \(C_2\times C_2\).

## Assumptions and scope
The coefficient field is \(\mathbf F_p\) for an odd prime \(p\). The groups are compact, connected and semisimple. The minimality statement is restricted to pairs with a common simply connected universal cover. No claim is made in characteristic \(2\) or for arbitrary pairs with different universal covers.

The source criterion applies because the simply connected factors \(\mathrm{SU}(4)\) and \(\mathrm{SU}(2)\) have torsion-free integral homology and the two covering kernels have order \(4\), which is invertible in \(\mathbf F_p\) for odd \(p\).

## Proof
Both quotients have common simply connected universal cover \(K\), so they have the same classical exponent multiset \(\{1,1,2,3\}\). Their fundamental groups are the covering kernels:
\[
\pi_1(G_4)\cong C_4,\qquad \pi_1(G_{22})\cong C_2\times C_2.
\]
Corollary 9.3 of arXiv:2610.04164v1 says that, for exterior pairs over an integral domain, graded-algebra isomorphism of shifted free-loop homology is equivalent to equality of exponent multisets together with isomorphism of the corresponding group algebras; the same conditions are equivalent to BV-algebra isomorphism.

For odd \(p\),
\[
\mathbf F_p[C_4]\cong\mathbf F_p[t]/(t^4-1)
=\mathbf F_p[t]/((t-1)(t+1)(t^2+1)).
\]
If \(p\equiv1\pmod4\), then \(-1\) is a square in \(\mathbf F_p\), so
\[
\mathbf F_p[C_4]\cong\mathbf F_p^4.
\]
Also
\[
\mathbf F_p[C_2\times C_2]\cong
\mathbf F_p[C_2]\otimes_{\mathbf F_p}\mathbf F_p[C_2]\cong\mathbf F_p^4.
\]
Hence the two BV algebras are isomorphic.

If \(p\equiv3\pmod4\), then \(t^2+1\) is irreducible and
\[
\mathbf F_p[C_4]\cong\mathbf F_p\times\mathbf F_p\times\mathbf F_{p^2},
\]
whereas \(\mathbf F_p[C_2\times C_2]\cong\mathbf F_p^4\). These semisimple algebras are not isomorphic, so Corollary 9.3 gives non-isomorphic graded loop-homology algebras and BV algebras.

For minimality, a common simply connected semisimple cover supporting a \(C_4\) kernel must have a simple factor whose centre contains an element of order \(4\). The least possible rank is \(3\), attained by \(\mathrm{SU}(4)\), whose centre is cyclic \(C_4\). A cyclic \(C_4\) contains no \(C_2\times C_2\), so an additional simple factor with even-order centre is necessary and has rank at least \(1\), attained by \(\mathrm{SU}(2)\). Thus the total rank is at least \(4\), and \(K=\mathrm{SU}(4)\times\mathrm{SU}(2)\) attains the bound.

## Verification
The proof is symbolic. The finite-field dichotomy uses the factorization of \(t^4-1\) and the criterion that \(-1\) is a quadratic residue modulo an odd prime exactly when \(p\equiv1\pmod4\). Rank minimality uses the centre classification of simply connected compact simple Lie groups and rank additivity. No finite experiment is used as an infinite proof.

## Relationship to prior work
arXiv:2610.04164v1 proves the general BV-classification theorem and Remark 9.6 records the abstract group-algebra coincidence \(\mathbf F_p[C_4]\cong\mathbf F_p[C_2\times C_2]\) when \(p\equiv1\pmod4\). It does not exhibit the smallest common-cover compact semisimple realization or prove a sharp rank threshold. The present finding supplies that realization and the rank-\(4\) minimum, and records the complementary \(p\equiv3\pmod4\) separation for this pair.

## Limitations
The rank-minimality statement requires a common universal cover. It does not classify all compact Lie-group pairs with coincident finite-field loop BV algebras. Characteristic \(2\) is excluded because the order-\(4\) covering kernels are not units.

## References
1. Mukilraj K, “Integral string topology of the symplectic group and BV rigidity for compact Lie groups,” arXiv:2610.04164v1, first public 2026-10-03, primary MSC 55P50; see Theorem 3.2, Corollary 3.12, Corollary 9.3, Remark 9.6 and Example 9.7.
