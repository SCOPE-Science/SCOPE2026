# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The argument was checked independently at the level of each mathematical mechanism.

- **Exact/Frobenius structure.** Euler characteristic is additive on conflations and changes sign under shift, while contractible complexes have Euler characteristic zero. A split kernel or cokernel between objects of \(\mathcal A_H\) again has Euler characteristic in \(H\), proving weak idempotent completeness. The standard contractible cone sequences remain internal and supply enough projectives and injectives.
- **Ideal cotorsion pair.** The stable extension formula
  \[
  \operatorname{Ext}^1(X,Y)\cong\bigoplus_n\operatorname{Hom}(H^nX,H^{n+1}Y)
  \]
  gives orthogonality directly. The converses use two adjacent one-dimensional stalks of total Euler characteristic zero, so the test objects belong to every \(\mathcal A_H\), including \(H=\{0\}\).
- **Object-ideal property and completeness.** Every required factor object can be corrected by a zero-differential summand of opposite Euler characteristic supported on the allowed side of the cohomological cut. The explicit special ideal approximation sequences have kernel or cokernel of Euler characteristic zero, while the middle term has the same Euler characteristic as the original object.
- **Object obstruction.** Long exact cohomology forces a special \(\mathcal F_H\)-precover to have Euler characteristic equal to that of \(H^{\leq0}(A)\), and dually for \(H^{\geq2}(A)\). When the relevant class vanishes, the unstabilized standard cone sequence lies in \(\mathcal A_H\), proving sufficiency.
- **Total-Betti threshold.** For any conflation,
  \[
  \beta(Y)=\beta(X)+\beta(Z)-2\sum_n\operatorname{rank}\delta_n.
  \]
  This proves closure modulo \(2\). For every \(m>2\), a rank-one connecting map between \(S^0(k^m)\) and \(S^1(k^m)\) produces middle Betti number \(2m-2\), disproving extension closure.

Adversarial checks included the subgroup \(H=\{0\}\), arbitrary field characteristic, the distinction between weak and full idempotent completeness, the distinction between ideal and object approximations, and the possibility that the higher-modulus total-Betti condition might survive through a different congruence. No hidden divisibility or characteristic assumption was found.

## Originality — PASS, qualified

The 2026 Ren–Wang preprint already proves the parity case: bounded complexes with even total cohomology dimension, the corresponding complete ideal cotorsion pair, and parity obstructions to special object approximations. Since total Betti number and Euler characteristic agree modulo \(2\), that work is exactly the \(H=2\mathbb Z\) member of the present family and is not claimed as new.

The novelty claim is limited to:

1. the construction for every additive subgroup \(H\leq\mathbb Z\);
2. uniform Euler-zero stabilizers replacing parity doubling;
3. the exact pair \((o_-,o_+)\in(\mathbb Z/H)^2\) of object-approximation obstructions;
4. completeness of the object pair exactly when \(H=\mathbb Z\), with one universal simultaneous witness for every proper \(H\);
5. realization of every obstruction pair for \(H=m\mathbb Z\);
6. the sharp classification that total-Betti divisibility defines an extension-closed subcategory only for moduli \(1\) and \(2\).

Searches using the source paper, arbitrary Euler-characteristic subgroups, congruence-valued truncation obstructions, higher-modulus total cohomology conditions, object ideals, and cotorsion completeness did not locate these statements. The foundational 2013 ideal-approximation paper and subsequent Frobenius-category work establish the surrounding theory but no located theorem subsumes the subgroup construction.

Residual originality risk remains because the parity paper is a recent first version, and the subgroup generalization is elementary once Euler additivity is isolated. Older exact-category or \(K_0\)-based literature may contain an equivalent observation under different language. Accordingly the originality conclusion is only to the best of our knowledge.

## Value — PASS

The result identifies the structural mechanism behind the parity counterexample rather than merely changing a numerical parameter. It separates two phenomena that coincide modulo \(2\): Euler-characteristic subgroup cuts extend uniformly to every subgroup, while total-Betti congruence fails to define an exact subcategory for every modulus above \(2\). The quotient-valued obstruction pair gives a complete object-by-object criterion and exhibits two independent failure coordinates.
