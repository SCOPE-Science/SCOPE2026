# A dihedral automorphism group for the fifteen-element power semigroup of \(C_4\)

## Finding
Let \(G=\mathbb Z/4\mathbb Z\), and let \(\mathcal P^*(G)\) be the monoid of all nonempty subsets of \(G\) under sumset addition. This monoid has fifteen elements. Its complete automorphism group is
\[
\operatorname{Aut}(\mathcal P^*(G))\cong C_4\rtimes_{-1}C_2\cong D_8,
\]
where \(D_8\) denotes the dihedral group of order eight. The subgroup preserving the reduced power monoid \(\mathcal P_0(G)=\{X\subseteq G:0\in X\}\) is precisely the subgroup induced by \(\operatorname{Aut}(G)\), and has order two. In particular there is a specific automorphism taking \(\{0,1\}\) to \(\{1,2\}\), so \(\mathcal P_0(G)\) is not characteristic in the full power monoid.

The classification is exact: writing all indices modulo four (modulo two for the \(B\)-family), every automorphism is uniquely a product of an automorphism of \(G\) applied elementwise and one of four transformations \(K_k\) described below. No additional permutations of the fifteen nonempty subsets are automorphisms.

## Assumptions and scope
The only base group is the cyclic group \(G=\mathbb Z/4\mathbb Z\), written additively. All subsets are nonempty. The product is \(X+Y=\{x+y:x\in X,\ y\in Y\}\). Write \(\Omega=G\) and, for \(i\in G\), set
\[
U_i=\{i\},\qquad A_i=\{i,i+1\},\qquad C_i=G\setminus\{i\},
\]
while \(B_i=\{i,i+2\}\) depends only on \(i\bmod2\). These are the fifteen distinct elements: four each of types \(U,A,C\), two of type \(B\), and \(\Omega\).

For each \(k\in G\), define a permutation \(K_k\) by
\[
K_k(U_i)=U_i,\quad K_k(A_i)=A_{i+k},\quad
K_k(B_i)=B_i,\quad K_k(C_i)=C_{i+2k},\quad
K_k(\Omega)=\Omega.
\]
For \(\alpha\in\{1,-1\}\), let \(\widehat\alpha(X)=\{\alpha x:x\in X\}\). The classification asserts that the eight maps \(K_k\circ\widehat\alpha\) are exactly all automorphisms.

## Proof
**1. Complete multiplication table.** Direct addition modulo four gives, for all applicable indices,
\[
\begin{aligned}
U_i+U_j&=U_{i+j},& U_i+A_j&=A_{i+j},\\
U_i+B_j&=B_{i+j},& U_i+C_j&=C_{i+j},\\
A_i+A_j&=C_{i+j+3},& B_i+B_j&=B_{i+j}.
\end{aligned}
\]
Every sum of two elements from *different* families among \(A,B,C\) equals \(\Omega\), as does \(C_i+C_j\). Also \(\Omega+X=\Omega\) for all \(X\). For instance \(A_i+A_j=\{i+j,i+j+1,i+j+2\}=C_{i+j+3}\). These rules exhaust every product.

**2. Reduction to a unit-fixing automorphism.** An invertible element of \(\mathcal P^*(G)\) must be a singleton: if \(X+Y=\{0\}\), then fixing any \(y\in Y\) shows \(X+y\subseteq\{0\}\), so \(X\) has one element, and similarly \(Y\) does. Thus the units are exactly \(\{U_i\}_{i\in G}\), forming \(G\). Any automorphism restricts to either \(i\mapsto i\) or \(i\mapsto-i\) on units. Composing with the inverse elementwise group automorphism yields an automorphism \(f\) fixing every \(U_i\). Also \(f(\Omega)=\Omega\), since \(\Omega\) is the unique absorbing element.

**3. Translation-equivariant orbit structure.** Since \(f(U_i)=U_i\), the multiplication table forces \(f(U_i+X)=U_i+f(X)\) for all \(i,X\). Under the translation action of the units, the orbits are precisely \(\{U_i\}\), \(\{A_i\}\), \(\{B_0,B_1\}\), \(\{C_i\}\), and \(\{\Omega\}\), of sizes \(4,4,2,4,1\). The singleton orbit is fixed pointwise, and the unique orbit of size two must map to itself. Of the other two size-four orbits, the \(A\)-orbit has squares distinct from \(\Omega\), whereas all squares in the \(C\)-orbit equal \(\Omega\). Thus these orbits cannot be interchanged. Translation equivariance consequently yields shifts
\[
f(A_i)=A_{i+k},\qquad f(B_i)=B_{i+\ell},\qquad f(C_i)=C_{i+m}
\]
for uniquely determined \(k,m\in G\) and \(\ell\in\mathbb Z/2\mathbb Z\).

**4. Multiplication forces precisely four shifts.** Since \(B_0+B_0=B_0\), preservation of this identity forces \(B_\ell+B_\ell=B_\ell\). Only \(B_0\) is idempotent in the \(B\)-orbit; hence \(\ell=0\). Applying \(f\) to \(A_i+A_j=C_{i+j+3}\) gives
\[
C_{i+j+3+m}=A_{i+k}+A_{j+k}=C_{i+j+3+2k},
\]
so \(m=2k\) in \(G\). Conversely, all the multiplication rules in step 1 are preserved by \(K_k\), including products involving \(\Omega\); each \(K_k\) is bijective. Therefore the unit-fixing automorphisms are exactly \(K_0,K_1,K_2,K_3\).

**5. Group structure and reduced-submonoid stabilizer.** Composition satisfies \(K_kK_\ell=K_{k+\ell}\), and the induced inversion automorphism \(\widehat{-1}\) satisfies
\[
\widehat{-1}\,K_k\,\widehat{-1}=K_{-k}.
\]
The intersection of the four-element kernel with the two elementwise group automorphisms is trivial, giving the displayed semidirect product. An elementwise group automorphism preserves \(\mathcal P_0(G)\). A nonidentity \(K_k\) does not preserve it: \(A_0\) and \(A_3\) are exactly the \(A\)-sets containing zero, and translation by \(k\ne0\) cannot preserve this two-element family \(\{A_0,A_3\}\) simultaneously. In particular \(K_1(A_0)=A_1=\{1,2\}\). Hence the stabilizer of \(\mathcal P_0(G)\) in the full automorphism group has exactly two elements.

## Verification
The standalone Python 3 checker `verify.py` constructs the entire fifteen-element multiplication table using integer arithmetic and verifies the displayed products for all indices. It enumerates every translation-equivariant orbit-preserving permutation fixing singleton units: there are \(4\cdot2\cdot4=32\) candidates. Exactly the four \(K_k\) preserve all 225 ordered products. Composing them with the two group automorphisms yields exactly eight distinct valid automorphisms, two preserving the reduced power monoid; the witness \(\{0,1\}\mapsto\{1,2\}\) is checked. The recorded output is in `verification_output.txt`.

The code checks these finite instances exhaustively *within the proved orbit-restricted candidate class*; the proof of why every automorphism belongs to that class is step 3, not an inference from testing arbitrary permutations.

## Relationship to prior work
Tringali and Wen (2026, Conjecture 5.2) ask whether, for every cancellative monoid, all automorphisms of its large power monoid preserve the reduced submonoid. The result supplies a full even-torsion cyclic classification and an explicit failure of this proposed invariance. Earlier small-group failures do not determine the automorphism group of \(C_4\): the order-four group has a separate two-element coset orbit, and this orbit forces a different group law from the odd-order case.

Rago (2025, Theorem 13) classifies automorphisms of *reduced* power monoids of finite abelian groups; that theorem gives \(\operatorname{Aut}(\mathcal P_0(C_4))\cong C_2\), but does not compute the automorphisms of the *full* fifteen-element power semigroup or whether the reduced submonoid is characteristic there. Antoniou and Tringali (2018/2021, Sections 3–5) study factorization and minimal length arithmetic, not this automorphism classification. The present result is consistent with those results and identifies exactly the additional full-power symmetries and their action.

## Limitations
This is a complete classification only for \(C_4\). It does not classify the full power semigroup for other cyclic groups or arbitrary finite abelian groups, and it does not resolve the separate conjecture about the large power monoid of the infinite cyclic group. Since this is a small exact case, an equivalent historical semigroup computation might exist outside the sources inspected. The exhaustive checker is finite corroboration, not an independent mathematical audit.

## References
1. Salvatore Tringali and Kerou Wen, *On the automorphisms of the power semigroups of a numerical semigroup*, arXiv:2604.26901 (first public 2026-04-29), especially Sections 1, 2, and Conjecture 5.2. https://arxiv.org/abs/2604.26901
2. Balint Rago, *The automorphism group of reduced power monoids of finite abelian groups*, arXiv:2510.17533 (2025-10-20), especially Theorem 13. https://arxiv.org/abs/2510.17533
3. Austin A. Antoniou and Salvatore Tringali, *On the Arithmetic of Power Monoids and Sumsets in Cyclic Groups*, arXiv:1804.10913 (2018-04-29); Pacific Journal of Mathematics 312 (2021), 279–308, Sections 3–5. https://arxiv.org/abs/1804.10913
