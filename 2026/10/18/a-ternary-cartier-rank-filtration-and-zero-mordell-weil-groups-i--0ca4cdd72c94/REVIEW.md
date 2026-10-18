# Scientific assessment

## Correctness — PASS

For every positive \(s\), the branch polynomial is squarefree, the genus is \(3^s\), and the correct inverse-Frobenius-semilinear Cartier matrix has exactly two allowed row-to-column types. Its nonzero entries lie in \(\mathbb F_3\), so semilinear twisting does not change subsequent powers. The base-three word dynamics is a proof valid for every exponent, with a sharp final surviving word at \(2s\) and disappearance at \(2s+1\). The geometric corollary follows by checking Katsura's polynomial normal form and Assumption (*) and applying his Theorem 4.1, rather than inferring Mordell–Weil vanishing directly from a numerical test. The supplied checker confirms all ranks for \(1\leq s\leq6\) and checks the digit model independently.

## Originality — PASS, with stated risk

Achter–Howe (arXiv:1710.10726, Section 3) provide the general coefficient formula, and Katsura (arXiv:2609.23430, Theorem 4.1) provides the general Mordell–Weil/Cartier connection. Neither inspected primary text states the closed all-iterate rank sequence for \(y^2=t^{2\cdot3^s+2}-t\) or applies it to this quasi-elliptic family. The digit-shift lemma and full survivor enumeration bridge those theorems. Published mathematical-record searches for exact polynomial, rank profile, and aliases, plus reviewed published claim summaries, found no equivalent statement. Garton–Thunder–Weir consider distributions of \(a\)-numbers rather than the specific family, based on their inspected abstract. Older full papers (including Ito 1992) were not comprehensively inspected; an implicit previously known specialization remains possible. Lack of a search hit is not presented as historical proof of priority.

## Mathematical value — PASS

This is an exact, non-asymptotic and all-genus computation of a natural Cartier filtration and two geometric invariants, with a uniform vanishing result for the Mordell–Weil groups of a meaningful infinite quasi-elliptic family. It is motivated by the relationship in Katsura's recent work and requires non-obvious ternary dynamics rather than just substituting into the textbook coefficient formula.

## Boundaries and further investigation

The result does not compute full Jacobian \(3\)-torsion schemes, Newton polygons, or the fibration's full singular-fiber classification. The self-contained combinatorial argument is universal, but the finite code checks are not a proof for unbounded \(s\). Full-text priority risks and independent external validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
