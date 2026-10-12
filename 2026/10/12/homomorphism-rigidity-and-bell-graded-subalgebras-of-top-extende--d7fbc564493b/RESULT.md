# Homomorphism rigidity and Bell-graded subalgebras of top-extended Boolean Heyting algebras

## Finding

For every integer \(m\geq1\), let \(A_m\) be the Heyting algebra obtained by adjoining one new greatest element \(\top\) to the Boolean lattice \(\mathcal P([m])\). It has \(2^m+1\) elements. For \(n\geq1\), write \(\left\{\begin{smallmatrix}n\\m\end{smallmatrix}\right\}\) for a Stirling number of the second kind, taken to be zero when \(m>n\). Then the number and image-cardinality spectrum of all Heyting homomorphisms \(A_m\to A_n\) are

\[
\boxed{\sum_{h\in\operatorname{Hom}(A_m,A_n)}z^{|h[A_m]|}=m z^2+m!\left\{\begin{smallmatrix}n\\m\end{smallmatrix}\right\}z^{2^m+1}.}
\]

Every such map is either injective or has exactly two image elements. The injective maps are indexed by surjections \([n]\twoheadrightarrow[m]\), and the noninjective maps by a single chosen point of \([m]\).

Moreover, the proper and full Heyting subalgebras of \(A_m\) are exactly the two-element algebra \(\{\varnothing,\top\}\) and, for each set partition \(\pi\) of \([m]\), the algebra consisting of \(\top\) together with all unions of blocks of \(\pi\). Consequently their cardinality enumerator is

\[
\boxed{\sum_{C\leq A_m}z^{|C|}=z^2+\sum_{k=1}^{m}\left\{\begin{smallmatrix}m\\k\end{smallmatrix}\right\}z^{2^k+1}.}
\]

The subalgebra-inclusion order, after its two-element minimum is deleted, is the partition lattice ordered by **coarsening**. In particular \(A_m\) has \(B_m+1\) subalgebras, where \(B_m\) is the \(m\)-th Bell number. On the other hand, \(\operatorname{End}(A_m)\) has exactly \(m!+m\) elements, exactly \(m+1\) of which are idempotent, and there are only **two distinct embedded retract subalgebras**: the two-element minimum and \(A_m\) itself.

## Assumptions and scope

All algebras are nontrivial finite Heyting algebras in the full signature \((\wedge,\vee,\to,0,1)\). We require \(m,n\geq1\); no statement about a degenerate empty Boolean base is needed. A homomorphism preserves all operations and both constants. A retract means the image of an idempotent endomorphism; the number of retract subalgebras is not the number of retraction maps. The new top \(\top\) is different from the original Boolean maximum \([m]\). For \(x,y\in\mathcal P([m])\), Heyting implication is \(\top\) when \(x\subseteq y\), and otherwise is \(([m]\setminus x)\cup y\). Operations with the adjoined top are determined by residuation.

## Proof

**Step 1 (finite dual).** The Esakia dual of \(A_m\) is the rooted star \(P_m=\{r,\ell_1,\ldots,\ell_m\}\) ordered by \(r<\ell_i\) and with incomparable maximal leaves. Indeed, an upset of this star is either a subset of its leaves or the whole star, so its Heyting upset algebra is exactly \(A_m\). Finite Esakia duality identifies Heyting homomorphisms \(A_m\to A_n\) contravariantly with p-morphisms \(f:P_n\to P_m\) satisfying

\[
f[\uparrow x]=\uparrow f(x)\qquad\text{for every }x\in P_n.
\]

**Step 2 (all maps).** If \(f(r)\) is a target leaf \(\ell_j\), the equality at the root forces \(f[P_n]=\{\ell_j\}\), hence \(f\) is the constant map to that leaf. There are exactly \(m\) possibilities. Otherwise \(f(r)=r\) and the same equality forces \(f[P_n]=P_m\). A source leaf has a singleton upcone, so its image must be a target leaf. The induced leaf function \([n]\to[m]\) must be onto, and every such surjection uniquely gives a p-morphism. Their number is \(m!\left\{\begin{smallmatrix}n\\m\end{smallmatrix}\right\}\). An onto dual map induces an injective Heyting homomorphism, whose image has \(2^m+1\) elements. A constant dual map induces a homomorphism with image \(\{0,1\}\). This proves the homomorphism rank polynomial and its asserted dichotomy, including \(n<m\).

**Step 3 (all subalgebras).** Let \(C\leq A_m\). The inclusion dualizes to a surjective p-morphism \(q:P_m\twoheadrightarrow Q\) onto the finite Esakia dual \(Q\) of \(C\). The image of the source root is the least point of \(Q\). Each leaf maps to a maximal point since the source leaf upcone is a singleton. If \(Q\) is not singleton, its least point cannot be a leaf image, so \(Q\) must itself be a rooted star with \(k\geq1\) leaves, where \(k\leq m\); the source leaves map onto these \(k\) leaves. Conversely, every partition of \([m]\) into \(k\) nonempty fibers yields such a quotient and hence a Heyting subalgebra of cardinality \(2^k+1\), concretely the collection of unions of its blocks together with \(\top\). Two partitions give the same subalgebra if and only if they are identical, because the atoms of its Boolean portion recover their blocks. The singleton dual quotient gives exactly \(\{0,1\}\). This proves the Stirling polynomial, Bell total, and the coarsening order statement.

**Step 4 (endomorphisms and retracts).** Set \(n=m\) in Step 2. A surjective map between equal finite leaf sets is a permutation, and all the remaining dual maps are the \(m\) constants to leaves. Hence \(\operatorname{Aut}(A_m)\cong S_m\), and there are \(m!+m\) endomorphisms. Each constant dual map is idempotent, while the only idempotent permutation is the identity. All \(m\) nonidentity idempotents have the same algebraic image \(\{0,1\}\), proving the stated retract classification.

**Example.** At \(m=3\), the subalgebra polynomial is \(z^2+z^3+3z^5+z^9\), whereas the endomorphism image polynomial is \(3z^2+6z^9\) and the idempotent image polynomial is \(3z^2+z^9\).

## Verification

Run the self-contained standard-library program \(\texttt{python3 verify.py}\). Its completed finite run reports: `VERIFY_OK 1836 exact assertions; 82174 dual function tables; 32906 candidate subalgebras; 81210 direct algebra function tables; 35 dual-induced homomorphisms; m,n<=5 dual and m<=4 subalgebras`. It independently enumerates p-morphisms for \(1\leq m,n\leq5\), enumerates every possible subset containing the two constants for \(m\leq4\) and tests the actual Heyting operation tables, and checks selected homomorphism counts directly by enumerating algebraic function tables. The finite tests support but do not substitute for the proof above.

## Relationship to prior work

Bumpus and Kocsis introduce and use precisely the family obtained by adjoining a new maximum to a finite Boolean algebra, including in the proof of their Theorem 3.8 on material implication and finite satisfiability gaps. They do not enumerate its full hom-sets, subalgebra lattice, or retract spectra in that argument. Martins and Moraschini provide finite Esakia-morphism and quotient tools, while Bezhanishvili, Carai, and Morandi set out finite Esakia duality categorically. The classical partition-lattice and Stirling/Bell numbers, and the general Esakia duality, are established mathematics and are not originality claims. Adams studies maximal subalgebras of general Heyting algebras; the accessible abstract does not establish coverage of this paired homomorphism/retract classification. The proposed contribution is the simultaneous exact classification for this explicit satisfiability-gap witness family, especially the discrepancy between its Bell-graded subalgebras and its only two retract subalgebras.

## Limitations

The result addresses only the one-top extensions of finite Boolean algebras, not arbitrary finite subdirectly irreducible Heyting algebras. It does not classify congruences or homomorphisms into arbitrary codomains. Finite exhaustive tests reach only the stated parameter bounds. Although exact theorem and code are supplied, an unindexed earlier derivation or a consequence implicit in older subalgebra literature is a remaining originality risk. Independent mathematical audit has not yet been performed.

## References

1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (initial release 2021-10-21), *Journal of Symbolic Logic* 90 (2025), 533–551, DOI:10.1017/jsl.2024.2; see Definition 1.7, Corollary 2.8, and Theorem 3.8.
2. M. Martins and T. Moraschini, *On locally finite varieties of Heyting algebras*, arXiv:2306.15997v1 (2023-06-28), Section 2 (Esakia quotients and elementary reductions).
3. G. Bezhanishvili, L. Carai, and P. J. Morandi, *Heyting frames and Esakia duality*, arXiv:2302.07913v1 (2023-02-15), Lemma 2.3 and Theorem 2.2.
4. M. E. Adams, *Maximal subalgebras of Heyting algebras*, *Proceedings of the Edinburgh Mathematical Society* 29 (1986), 359–365, DOI:10.1017/S0013091500017806.
