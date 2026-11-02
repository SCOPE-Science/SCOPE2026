# Scientific review: all-order interval-bootstrap positivity certificate

## Correctness — PASS

The claim has two components: the rational diagonal product formula for every order and the low-energy positive-semidefiniteness classification for every finite size. The proof derives a weighted derivative-norm recurrence for every Legendre eigenfunction, then identifies the formal rational bootstrap diagonal by rational-function uniqueness at infinitely many nonresonant physical energies. A separate reflection-symmetry argument removes odd-step resonance ambiguities and establishes that *all* matrix entries at each physical energy recover the actual Gram matrix. Each open pole gap has one strictly negative diagonal except at its unique physical energy. The pole points are excluded, and no higher-energy assertion is made. The actual packaged `verify.py` was run successfully, with 54 exact finite assertions including symbolic identities through diagonal order six and exact Legendre norms; finite checks are a supplement, not a universal proof. Source: Sword and Vegh [1], especially their definitions (3.39)–(3.42), recursion (3.10), and analytic eigenstates (2.18). Residual risk: scrutiny of the algebraic reduction and the rational continuation proof is warranted in independent review, though their steps are explicitly supplied.

## Originality — PASS, with publication-priority limitations

Sword and Vegh [1] provide the same bootstrap matrix and report finite-size exact spectral isolation. In section 4.4, their determinant checks reach size 12 and direct positivity checks size five; they explicitly leave a general arbitrary-size proof open. The new theorem supplies an all-order product for individual diagonals and an exact sign certificate for every finite size. The reviewed public version and the 2024 journal edition are the same original work, not two independent replications. Searches for the specific model, alternative ordering, spectral-gap factorization, and arbitrary-size positivity, including indexed mathematical findings, did not disclose a covering theorem. Other accessible results concern different operators and do not establish this rational identity. A 2024/2025 institutional thesis by the first author is discoverable, but its full text was not readable through the available source route; it remains a material publication-priority risk. Other later unpublished treatments may exist. No claim of independently certified novelty is made.

## Mathematical value — PASS

This resolves the motivating source's expressly open all-size classification for the original alternatively ordered matrix rather than merely giving a new parametrization of known numbers. The exact factorization explains why a single diagonal entry rules out each interval of spurious trial energies and why the energy levels are isolated for every matrix size. It removes the need for successively larger characteristic determinants and supplies a structural certificate directly in the bootstrap's positive-semidefinite constraints. The result is confined to the natural no-flux Legendre operator and original operator ordering; it does not claim a broader spectral theorem or off-spectrum physical states.

## Closest literature and limitations

[1] Lewis Sword and David Vegh, *Quantum mechanical bootstrap on the interval: obtaining the exact spectrum*, arXiv:2402.03434v1 (5 February 2024), Phys. Rev. D 109, 126002 (2024), https://arxiv.org/html/2402.03434v1 . Full material inspected: model, recurrence, two-operator ordering, explicit matrix, main findings and appendices.

[2] Xihe Hu, *Different Bootstrap Matrices in Many QM Systems*, arXiv:2206.00767 (2022), https://arxiv.org/abs/2206.00767 . Relevant general background but complete content not read; no statement of full noncoverage is inferred from a title or abstract.

[3] Lewis Sword, *Black holes, matrix & tensor witnesses and the quantum mechanical bootstrap*, doctoral thesis submitted 25 July 2024, repository metadata https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/99744/phd_thesis_lewis_sword_150962779_QMUL_SPCS_minor_corrections.pdf?isAllowed=y&sequence=2 . Full text inaccessible through the attempted route; possible overlap explicitly unresolved.

Pole values and energies beyond the final pole of a given matrix are not classified. This is a self-review, not an independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
