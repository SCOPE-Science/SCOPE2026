# Complex midpoint quandle algebras and the Wieferich-square isomorphism obstruction

## Finding

For any finite abelian group \(G\) of odd order, let \(M(G)\) be the midpoint quandle with \(x*y=(x+y)/2\) and let \(\mathcal A(G)=\mathbb C[M(G)]\), a nonassociative complex algebra. The algebraic isomorphism type of \(\mathcal A(G)\) is exactly the cycle type of the doubling permutation \(T_G:g\mapsto2g\) on \(G\). In particular, for two such groups,
\[
\mathcal A(G)\cong\mathcal A(H)\quad\Longleftrightarrow\quad
|G[2^r-1]|=|H[2^r-1]|\quad\text{for every }r\ge1.
\]
Here \(G[n]=\{g\in G:ng=0\}\). The cyclic factor lengths of the primary parts give an exact arithmetic criterion. For each odd prime \(p\), write
\[
G_p\cong\bigoplus_i C_{p^{e_i}},\qquad
H_p\cong\bigoplus_j C_{p^{f_j}},\qquad
s_p=v_p\!\left(2^{\operatorname{ord}_p(2)}-1\right).
\]
Then
\[
\mathcal A(G)\cong\mathcal A(H)
\quad\Longleftrightarrow\quad
\sum_i\min(t,e_i)=\sum_j\min(t,f_j)
\quad\text{for all odd primes }p\text{ and integers }t\ge s_p.
\]
The empty primary-component sum is zero. Consequently the group-to-algebra map is injective on isomorphism classes of groups of any fixed odd order \(N\) **if and only if** \(p^2\nmid N\) for every base-two Wieferich prime \(p\), meaning \(2^{p-1}\equiv1\pmod{p^2}\).

For example, \(p=1093\) has \(\operatorname{ord}_{1093}(2)=364\) and \(v_{1093}(2^{364}-1)=2\). The two nonisomorphic connected midpoint quandles from \(C_{1093^2}\) and \(C_{1093}\oplus C_{1093}\) have **isomorphic complex quandle algebras**: each doubling action has one fixed point and precisely \(3282\) cycles of length \(364\).

The same Fourier coordinates yield the full complex algebra automorphism group. If \(m_\ell\) is the number of cycles of doubling length \(\ell\), then
\[
|\operatorname{Aut}_{\mathbb C}(\mathcal A(G))|
=\prod_{\ell\ge1}\bigl[\ell(2^\ell-1)\bigr]^{m_\ell}m_\ell!.
\]
For example, its order is \(60\) for \(G=C_5\), and \(882\) for \(G=C_7\).

## Assumptions and scope

All groups are finite abelian of **odd** order; the coefficient field is \(\mathbb C\). The quandle-algebra product is extended bilinearly from \(e_xe_y=e_{(x+y)/2}\), where the inverse of multiplication by two exists in \(G\). The isomorphisms are complex-linear multiplicative bijections; they need not map original quandle basis elements to original basis elements. For primes \(p\) absent in a group, its list of \(p\)-primary exponents is empty. The assertion about fixed order \(N\) includes the trivial group. All finite midpoint quandles here are Latin and connected; group-nonisomorphism entails quandle-nonisomorphism, as can also be established using the displacement group and its regular action.

## Proof

**1. Fourier evolution basis.** Let \(\widehat G=\operatorname{Hom}(G,\mathbb C^\times)\). For \(u=\sum_g a_ge_g\), put \(\widehat u(\chi)=\sum_g a_g\chi(g)\). Character orthogonality gives an invertible complex-linear transform from \(\mathcal A(G)\) to functions on \(\widehat G\). By the midpoint multiplication law,
\[
\widehat{uv}(\chi)
=\widehat u(\chi\circ[1/2])\,\widehat v(\chi\circ[1/2]).
\]
For coordinate delta functions \(E_\chi\), it follows that
\[
E_\chi E_\psi=0\ (\chi\ne\psi),\qquad
E_\chi^2=E_{\chi^2}.
\]
Indeed the sole character \(\rho\) satisfying \(\rho\circ[1/2]=\chi\) is \(\rho=\chi^2\). Thus \(\mathcal A(G)\) is a *permutation evolution algebra*, with square-map permutation the doubling permutation on \(\widehat G\).

**2. Monomial rigidity and cycle classification.** More generally, in an algebra with basis \(E_i\), zero cross-products and square products \(E_i^2=E_{\tau(i)}\) for a permutation \(\tau\), multiplication of arbitrary vectors is their coordinatewise product followed by the permutation. Suppose a complex algebra isomorphism sends \(E_i\) to \(v_i\). The equations \(v_i v_j=0\), \(i\ne j\), force pairwise disjoint supports of the \(v_i\). Since the vectors form a basis in the same finite dimension, every support is a singleton. Hence every isomorphism is monomial, \(v_i=\lambda_iE_{\pi(i)}\) with all \(\lambda_i\ne0\). Comparing squares gives
\[
\pi\tau=\tau'\pi,\qquad \lambda_{\tau(i)}=\lambda_i^2.
\]
Conversely any permutation conjugacy of \(\tau,\tau'\) yields an algebra isomorphism by taking all scalars one. Finite abelian groups are isomorphic to their character groups (noncanonically), and the doubling permutations are intertwined by any such group isomorphism. Two finite permutations are conjugate exactly when their fixed-point counts for every positive power agree: Möbius inversion recovers the number of primitive cycles via \(\ell m_\ell=\sum_{r\mid\ell}\mu(\ell/r)\#\operatorname{Fix}(T^r)\). For doubling, \(\#\operatorname{Fix}(T^r)=|G[2^r-1]|\). This proves the first equivalence.

**3. Arithmetic classification.** By the structure theorem for finite abelian groups,
\[
v_p\bigl(|G[2^r-1]|\bigr)=\sum_i\min\bigl(e_i,v_p(2^r-1)\bigr).
\]
Let \(d_p=\operatorname{ord}_p(2)\). The valuation \(v_p(2^r-1)\) is zero when \(d_p\nmid r\). When \(r=d_p u\), the lifting-the-exponent lemma for odd \(p\) gives
\[
v_p(2^r-1)=s_p+v_p(u).
\]
As \(u\) ranges over positive integers, this attains every integer \(t\ge s_p\). Therefore the fixed-point data are identical for all powers precisely when the displayed truncated exponent sums agree for every prime and every \(t\ge s_p\). This also handles the \(p\)-components absent from one side.

**4. Sharp Wieferich boundary.** If \(s_p=1\), the profile at consecutive integers reconstructs the multiset of cyclic exponents: the difference between its values at \(t\) and \(t-1\) is the number of exponents at least \(t\), with the value at \(t=0\) set to zero. For odd primes, \(s_p>1\) is equivalent to the Wieferich congruence \(2^{p-1}\equiv1\pmod{p^2}\), because \(d_p\mid p-1\) and the quotient \((p-1)/d_p\) is prime to \(p\). If no squared Wieferich prime divides \(N\), then every nontrivial \(p\)-primary component having \(s_p>1\) has exponent sum one and is necessarily \(C_p\). Every primary component is therefore determined. Conversely, if \(s_p\ge2\) and \(p^2\mid N\), let \(T\) be any abelian group of order \(N/p^2\). Compare \(G=C_{p^2}\oplus T\) and \(H=C_p\oplus C_p\oplus T\). For each \(t\ge s_p\ge2\), replacing one exponent two by two exponents one leaves \(\sum\min(t,e_i)\) unchanged; the same holds after adjoining the identical factors from \(T\). Thus the complex algebras are isomorphic but \(G\not\cong H\) (their \(p\)-primary ranks differ). The criterion is sharp for every odd \(N\).

**5. All automorphisms.** In Step 2, the commuting permutation \(\pi\) can independently permute the \(m_\ell\) doubling cycles of each length \(\ell\), with \(\ell\) possible cyclic rotations. There are \(\ell^{m_\ell}m_\ell!\) such centralizing permutations for that length. Choose a root-of-unity scalar \(\lambda\) at one coordinate in each cycle. The square relation forces the remaining scalars as \(\lambda^2,\lambda^{2^2},\ldots\) and closure exactly requires \(\lambda^{2^\ell-1}=1\); there are \(2^\ell-1\) choices over \(\mathbb C\). Multiply independently over the cycles to obtain the automorphism-group order. The characteristic-zero coefficient field is essential for this root-count formula.

## Verification

Run the included standalone standard-library program `verify.py` with Python 3. It performs exact integer/arithmetic tests, not floating-point approximation. It enumerates the doubling permutations of all \(150\) finite odd-order abelian groups of order at most \(240\), compares every same-order pair (\(193\) comparisons), checks seven independent finite-field Fourier-multiplication identities, and exhaustively checks the monomial automorphism cases \(C_5\) and \(C_7\) over splitting finite fields (orders \(60\) and \(882\)). For the large explicit witness, it confirms \(1093\) is prime, \(d_{1093}=364\), the exact modular valuation is two, the full cycle-count formula gives \(3282\), and fixed-point counts of the two candidate groups agree over two entire periods. All checks passed. Finite computations support but do not replace Steps 1--5, which establish the claims for all finite odd-order abelian groups.

## Relationship to prior work

Elhamdadi--Ta--Virgin (2026) develop Fourier analysis of Alexander quandle algebras to study idempotents. Zhang (2026) applies related group-ring methods, and the older quandle-ring literature considers examples of distinct quandles with isomorphic algebras. These sources motivate the question but do not in their inspected statements give a classification of the complex midpoint algebra isomorphism type, its sharp arithmetic reconstruction boundary, or the explicit Wieferich-square counterfamily. General monomial rigidity of permutation evolution algebras is an existing structural principle; it is proved directly here and is not claimed as new on its own. The new synthesis identifies precisely which finite-group data the complex midpoint quandle algebra retains, when it fully determines the group, and when it necessarily fails.

## Limitations

This theorem classifies **complex** midpoint quandle algebras of **finite odd-order abelian groups**, not arbitrary Alexander quandles, noncommutative coefficient rings, or characteristic-\(p\) algebra forms. An algebra isomorphism in the Wieferich examples does not imply an isomorphism of the underlying quandles. The cycle criterion does not provide an explicit basis-preserving quandle isomorphism. Relevant literature might use the language of permutation evolution algebras or cyclic-power dynamics, so priority beyond the inspected sources and searches remains subject to independent bibliographic review. The arithmetic criterion is a proved theorem, not a claim that no other equivalent formulation appears elsewhere.

## References

- M. Elhamdadi, L. Ta and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (first public September 3, 2026), https://arxiv.org/abs/2609.03799.
- Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (first public October 6, 2026), https://arxiv.org/abs/2610.08204.
- M. Elhamdadi, N. Fernando and K. Tsvelikhovskiy, *Ring Theoretic Aspects of Quandles*, arXiv:1805.05908, https://arxiv.org/abs/1805.05908.
- V. Bardakov and collaborators, related *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550, https://arxiv.org/abs/2608.01550.
- F. Costoya, V. Mayorga and A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterranean Journal of Mathematics (2025), DOI:10.1007/s00009-025-02924-0.
