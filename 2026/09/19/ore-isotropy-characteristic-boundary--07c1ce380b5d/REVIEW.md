# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The characteristic-zero extension was checked at each place where the recent proof could depend on the ground field. The automorphism theorem used in the argument is explicitly over arbitrary fields, while the locally nilpotent derivation classification is explicitly over an arbitrary field of characteristic zero. The normalization of h uses only division by its leading coefficient and by deg(h), hence is valid over every characteristic-zero field. After normalization, comparison of the next-to-leading coefficient forces the translation parameter to vanish without requiring roots or algebraic closure. The two degree-bounding arguments use characteristic zero exactly through nonvanishing integer coefficients and ordinary derivative degree. Once D(x)=0, the PBW centralizer argument gives D(t) in k[x], and the resulting derivation is locally nilpotent.

The positive-characteristic obstruction was checked directly on generators. For A_x with [t,x]=x, E(x)=x and E(t)=0 respects the defining relation, is locally finite on the PBW basis, and is not locally nilpotent. A triangular automorphism sigma_r commutes with E exactly when x r'(x)=0, equivalently r lies in k[x^p]. Thus sigma_{x^{mp}} has degree mp and produces unbounded isotropy for every field of characteristic p.

## Originality

PASS, to the best of our knowledge. The recent source arXiv:2609.19470v1 states the differential Ore-extension theorem under the standing assumption that k is algebraically closed of characteristic zero. Its cited automorphism input is older and arbitrary-field, and its cited LND input explicitly works over arbitrary characteristic-zero fields. Targeted searches for the paper title/identifier together with arbitrary-field and positive-characteristic variants, and searches for the explicit A_x Euler derivation/Frobenius triangular isotropy mechanism, did not locate the exact theorem that the criterion holds for all and only characteristic-zero fields.

The arbitrary-field automorphism theorem and arbitrary-characteristic-zero LND theorem are prior art and are not claimed as new. Positive-characteristic pathologies of ordinary LNDs are also known, and the 2021 Kaygorodov--Lopes--Mashurov paper explicitly motivates iterative higher derivations in characteristic p. Bavula's 2024 paper gives positive-characteristic automorphism groups. The originality claim is only the removal of algebraic closedness from this specific isotropy criterion, the exact characteristic boundary, and the locally finite A_x Frobenius-isotropy counterexample.

All key sources used for the proof were accessible: the full recent preprint, the full 2021 paper, and the arbitrary-field automorphism source/statement. No specific inaccessible paper was identified whose known title or abstract strongly suggests it contains the same isotropy criterion. Residual risk remains because the main source is extremely recent, the extension is short after combining its proof with older arbitrary-field inputs, and older automorphism/derivation literature may phrase an equivalent observation differently.

## Value

PASS. The result sharpens a new theorem by identifying its exact field-theoretic hypothesis. It is not merely a base-field relaxation: a single explicit enveloping-type algebra A_x shows failure over every positive characteristic, and the counterexample is locally finite, so adding local finiteness does not repair the criterion. The description k[x^p]=ker(x d/dx) also isolates the mechanism responsible for unbounded isotropy.

## Scope and limitations

The result does not address whether algebraic closedness can be removed from the first Weyl algebra, polynomial plane, free algebra, or quantum statements in the recent paper. It does not classify all positive-characteristic isotropy groups and does not replace iterative higher derivations by ordinary derivations in positive characteristic.
