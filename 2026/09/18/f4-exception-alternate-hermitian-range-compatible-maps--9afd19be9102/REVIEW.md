# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The correction was checked directly against the definitions and theorem statements in arXiv:2609.20363v1.

The source explicitly notes that in characteristic two with an involution of the second kind every Hermitian scalar is alternate-Hermitian. The reverse inclusion is immediate in characteristic two, so for the nonidentity involution of \(\mathbb F_4\) the scalar Hermitian and alternate-Hermitian sets coincide. The off-diagonal matrix conditions also coincide because minus equals plus. Hence \(\mathcal H_2(\mathbb F_4)=\mathcal{AH}_2(\mathbb F_4)\).

Theorem 1.6 classifies range-compatible homomorphisms on the former space as local maps plus scalar multiples of the explicitly displayed \(\Phi_0\), and the source proves \(\Phi_0\) nonlocal. Since additive maps over \(\mathbb F_2\) are automatically \(\mathbb F_2\)-linear, \(\Phi_0\) is a direct counterexample to Theorem 1.7(a). Theorem 1.3 already isolates \(n=2,|\mathbb D|=4\) as the only possible alternate-Hermitian exception, so the corrected statement has no additional cases.

The dimension/counting claim was checked algebraically: local maps form \(\mathbb F_4^2\), the exceptional multiples form a one-dimensional \(\mathbb F_4\)-space, and their intersection is zero because a nonzero local multiple of \(\Phi_0\) would make \(\Phi_0\) itself local. Thus the range-compatible space is \(\mathbb F_4^3\), containing 64 maps, 16 local and 48 nonlocal.

A standalone exact finite-field script exhaustively enumerates all 65536 \(\mathbb F_2\)-linear maps on the 16-element domain and independently obtains exactly those 64 classified maps, with no missing or extraneous cases.

## Originality

Originality is asserted only to the best of our knowledge and is intentionally narrow. The exceptional map \(\Phi_0\), its range compatibility and nonlocality, and the Hermitian classification are all contained in arXiv:2609.20363v1 and are prior work. Earlier range-compatible results on symmetric and alternating spaces are also prior work.

The novelty claim is restricted to diagnosing that the source's own characteristic-two identification and Theorem 1.6 force a counterexample to Theorem 1.7(a), formulating the corrected alternate-Hermitian linear classification, and recording the exact 64/16/48 count with exhaustive verification. Searches for the arXiv identifier, title, theorem number, alternate-Hermitian terminology, the F4 exceptional case, correction, and erratum did not locate a public correction or equivalent diagnosis. The arXiv submission history still lists only v1.

Because the contradiction is obtained by combining nearby statements in a very recent paper, independent discovery or a subsequent author revision is a substantial residual originality risk. This is not evidence against the mathematical correction.

## Value

Theorem 1.7 is presented as the full linear classification and is explicitly intended for later applications to bounded-rank Hermitian matrix spaces. The missing exception changes an unconditional locality statement into a sharp one-case exception and gives the complete exceptional family. The correction is therefore small in scope but structurally important: it prevents the alternate-Hermitian branch of the advertised classification from being applied incorrectly in the unique four-element case.
