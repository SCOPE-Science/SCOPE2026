# Full rational \(A_5\)-character of the 1,560-sphere coset complex

## Finding
Let \(G=A_5\) and let \(X=|\Delta C(G)|\) be the order complex of the poset of all left cosets of all proper subgroups of \(G\), ordered by inclusion. Under left multiplication, the entire nonzero reduced rational homology module is
\[
\widetilde H_2(X;\mathbb Q)\cong 100V_6\oplus95V_4\oplus116V_5,
\]
where \(V_6\), \(V_4\), and \(V_5\) denote the irreducible rational \(G\)-representations of dimensions six, four, and five, respectively. The six-dimensional rational irreducible complexifies to the two Galois-conjugate three-dimensional complex irreducibles. The character on the five complex conjugacy classes (identity, involution, order three, and the two order-five classes) is
\[
\chi=(1560,-84,-21,5,5).
\]
In particular, the module is not a direct sum of 26 regular representations, despite having dimension 26 times the group order. No other positive-degree reduced rational homology occurs. The underlying homotopy type \(\bigvee^{1560}S^2\) is **previously established** by Ramras and is not a new assertion here.

## Assumptions and scope
The alternating group \(G=A_5\) consists of all 60 even permutations of five letters. The coset poset contains one element for each set \(xH\), with \(x\in G\) and \(H<G\); subgroups include the identity subgroup and exclude \(G\). A simplex is a nonempty strict chain of such coset sets, and the action is \(g(xH)=(gx)H\). Homology coefficients for the new character and decomposition are \(\mathbb Q\). The assertions concern this specific finite group and its full proper-subgroup coset complex, not a parabolic-coset complex.

## Proof
**Homology concentration.** Ramras proves that this exact coset complex is a wedge of 1,560 two-dimensional spheres [1, Proposition 4.9]. Consequently its reduced cellular chain Euler character coincides with the character of \(\widetilde H_2(X;\mathbb Q)\): the other reduced homology groups vanish. We do not claim to reprove Ramras's global homotopy result.

**Equivariant chain reduction.** For each proper subgroup \(H<G\) let \(w(H)\) be the alternating number of subgroup chains beginning at \(H\):
\[
 w(H)=\sum_{H=H_0< H_1<\dots<H_k<G}(-1)^k
 =1-\sum_{H<K<G}w(K).
\]
Any coset chain has a unique smallest coset \(xH\), and its subsequent cosets are precisely \(xK\) for strict subgroup inclusions \(H<K<G\). Since a fixed strict chain has pairwise distinct cardinalities, a group element fixes the simplex if and only if it fixes every coset in the chain; its action on the oriented simplex has sign \(+1\). Hence the reduced Lefschetz character is exactly
\[
 \chi(g)=-1+\sum_{H<G}w(H)\,f_g(H),\qquad
 f_g(H)=\#\{xH:g(xH)=xH\}.
\]
The group-theoretic formula
\[
 f_g(H)=\frac{|C_G(g)|\,|g^G\cap H|}{|H|}
\]
follows by counting \(x\) with \(x^{-1}gx\in H\), then dividing by \(|H|\). The sum has one term per actual subgroup, not merely one per isomorphism type.

**Finite exact subgroup enumeration.** Enumerating subgroup closures from the identity subgroup gives exactly 59 subgroups, one of which is \(G\). Among the 58 proper subgroups, the table of (order, number, common weight) is

| Subgroup order | 1 | 2 | 3 | 4 | 5 | 6 | 10 | 12 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Number | 1 | 15 | 10 | 5 | 6 | 10 | 6 | 5 |
| Weight \(w(H)\) | 60 | −4 | −2 | 0 | 0 | 1 | 1 | 1 |

For representative element orders \(1,2,3,5\), the weighted subgroup contributions, in the eight subgroup-order columns of this table, are respectively
\[
\begin{array}{c|rrrrrrrr|r}
 1&3600&-1800&-400&0&0&100&36&25&1560\\
 2&0&-120&0&0&0&20&12&5&-84\\
 3&0&0&-40&0&0&10&0&10&-21\\
 5&0&0&0&0&0&0&6&0&5
\end{array}
\]
where the final entry is the sum of contributions minus one. Both order-five conjugacy classes have the same result. A second computation directly enumerates all 1,018 actual proper cosets and all fixed chains, yielding the identical four traces for every one of the 60 group elements, not just chosen representatives.

**Rational character decomposition.** The characters \(V_4\) and \(V_5\) arise as the respective augmentation modules of the natural five-point action and the six-point action on Sylow-five subgroups; their character norms are one. The rational \(V_6\) is the Galois descent of the direct sum of the two conjugate complex icosahedral three-dimensional irreducibles, so its character norm is two and it is irreducible over \(\mathbb Q\). The rational character vectors of \(V_6,V_4,V_5\), in the class order stated above, are
\[
 (6,-2,0,1,1),\quad(4,0,1,-1,-1),\quad(5,1,-1,0,0).
\]
The class sizes are \(1,15,20,12,12\). Taking character inner products with \(\chi\) gives respectively \(200,95,116\). The norm of the rational six-dimensional character is two (it is the sum of conjugate complex three-dimensional irreducibles), so its **rational module multiplicity** is \(200/2=100\); the other rational multiplicities are 95 and 116. Their dimensions sum to \(100\cdot6+95\cdot4+116\cdot5=1560\). The trivial-character inner product is zero.

## Verification
Run `python3 verify.py` with Python 3.9 or later. The standalone standard-library verifier constructs all 60 even permutations, the group multiplication table, all 59 subgroups, and all 1,018 proper cosets. It checks the 58 proper-subgroup weights, the fixed-chain Lefschetz trace for all 60 elements by direct coset containment recursion, a separate subgroup-conjugacy counting formula, explicit full chain-count profiles, and rational character multiplicities. Successful execution terminates with `ALL_CHECKS_PASSED`. The direct fixed-chain dimension vectors by element order \(1,2,3,5\) are respectively \((1018,6867,8310,900)\), \((82,195,30,0)\), \((40,60,0,0)\), \((18,12,0,0)\); alternating sums with the reduced augmentation contribution \(-1\) reproduce the stated character.

## Relationship to prior work
Brown [2] introduced this full proper-subgroup coset poset and related its reduced Euler characteristic to the probabilistic zeta function. Ramras [1] proved its precise nonequivariant homotopy type, including the 1,560-sphere count. Neither of those established nonequivariant numerical statements alone implies how the 60 left translations act on individual homology classes. The present result evaluates the full rational \(A_5\)-character and its exact rational irreducible multiplicities. Douvropoulos and Josuat-Vergès [3] calculate an equivariant homology character for **parabolic** coset posets of finite Coxeter groups; their domain uses a restricted family of parabolic subgroups of a Coxeter group, not the 58 proper subgroups of the non-Coxeter group \(A_5\). Their formula does not cover the present object.

## Limitations
The character is rational; no integral equivariant homology lattice, equivariant wedge decomposition, or extension to other groups is claimed. The topological concentration uses the cited theorem of Ramras, while the finite character arithmetic is exactly reproducible from the included verifier. A finite computation of the 60-element action is exhaustive only because the group and coset poset are explicitly finite. Remaining bibliographic risk includes unidentified group-coset equivariant Lefschetz computations and portions of Brown's original article not inspected in full.

## References
[1] D. A. Ramras, *Connectivity of the coset poset*, arXiv:math/0208176 (first posted 23 August 2002), especially the \(A_5\) result; revised paper *Connectivity of the coset poset and subgroup poset of a group*, Proposition 4.9. https://arxiv.org/abs/math/0208176 ; https://pi.math.cornell.edu/~kbrown/ramras.pdf

[2] K. S. Brown, *The Coset Poset and Probabilistic Zeta Function of a Finite Group*, Journal of Algebra 225 (2000), 989–1012. https://doi.org/10.1006/jabr.1999.8221

[3] T. Douvropoulos and M. Josuat-Vergès, *Homology character of the parabolic coset poset*, arXiv:2509.11905 (2025), Sections 1, 2 and 4. https://arxiv.org/html/2509.11905v1
