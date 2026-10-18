# Review: arithmetic of a rigid characteristic-five Artin–Schreier curve

## Correctness — PASS

The curve \(y^5-y=x^4+x^2+x\) has a unique pole of order \(4\), giving genus \(6\) and exactly one rational place at infinity. Exhaustive arithmetic in explicit irreducible polynomial models of the fields \(\mathbb F_{5^n}\), for \(1\le n\le6\), independently counts fibres of the Artin–Schreier map and trace-zero inputs; their agreement yields point counts \(6,6,156,646,3501,15576\). Newton's identities and the genus-six functional equation uniquely yield the stated degree-twelve zeta numerator. The supplied program proves its reduction modulo \(2\) irreducible by a full finite-field polynomial criterion, and verifies that its value at \(1\) is the prime \(11731\). Simplicity is claimed only over \(\mathbb F_5\). The package's full executable was checked, not merely its recorded output.

## Originality — PASS, with residual risk

Tafazolian–Kazemifard, arXiv:2610.13279, supply the model and prove genus, rank and geometric automorphism-group rigidity; the inspected manuscript does not report a zeta polynomial, Jacobian order, or simplicity. The zeta-function theorems of Bouw–Ho–Malmskog–Scheidler–Srinivasan–Vincent (arXiv:1410.7031) and McGuire–Yılmaz (DOI:10.1016/j.jpaa.2018.11.005) cover different Artin–Schreier equations of degree \(5^h+1\), not this quartic equation; the general theory does not imply the exact numerator without arithmetic computation. Published mathematical searches and comparisons with preexisting mathematical claims identified no equivalent calculation. The precise isogeny-class-table search could not be inspected completely, and unindexed arithmetic computations remain possible.

## Mathematical value — PASS

The curve is not an arbitrary small-field example: it is the smallest characteristic-five genus in the newly identified zero-rank, no-extra-automorphism stratum. Its complete Weil polynomial determines all extension-field point counts; its irreducibility and prime order give concrete Jacobian arithmetic unavailable from the published geometric classification. The result makes no general-family claim, no claim of geometric simplicity, and no claim to determine the endomorphism ring.

## Closest sources and limitations

The principal comparison is arXiv:2610.13279, Lemma 3.3 and Theorem 1.1. Adjacent general zeta formulas from arXiv:1410.7031 and DOI:10.1016/j.jpaa.2018.11.005 do not specialize to degree four in characteristic five. A database query remained inaccessible, so overlap risk is not asserted to be zero. The executable certifies the exact finite computations; it is not independent validation.

Self-review: passed. Independent audit: not yet performed.
