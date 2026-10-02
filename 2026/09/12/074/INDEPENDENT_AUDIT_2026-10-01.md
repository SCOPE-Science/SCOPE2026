# Independent mathematical audit — SCOPE-20260912-074

Disposition: **repaired**.

## Correctness
**PASS** — The main construction is correct after repairing two exposition defects. The Ulm quotient statement is: Z/p summands contribute to f0 and Z/p² summands contribute to f1; the original sentence incorrectly said a Z/p² summand contributes to both, although the final values f0=f1=aleph_0 were still correct. The transported block law swaps p-divisibility of two named socle elements while preserving block isomorphism. Projection to a block proves purity. The two dovetailed divisibility searches give C <=_T A_C, while a C-oracle computes the finite block operations, giving A_C <=_T C. The c.e. minimal-pair existence attribution is also corrected to Lachlan and Yates (with Jockusch-Soare as a later construction).

## Originality
**PASS** — The inspected computable-p-group literature focuses on effective categoricity and isomorphism complexity, while Melnikov's degree-spectrum paper concerns different abelian-group spectra. Resultary found no prior SCOPE result with this exact bounded p-group and transported p-divisibility coding. No inspected source was found to state that this specific natural length-2 group realizes every c.e. degree.

### Equivalent formulations
The final claim is equivalently a uniform coding of c.e. sets into isomorphic copies via definable p-divisibility witnesses.

### Broader coverage
No stronger inspected theorem mechanically supplied the exact witness construction.

### Exact database or table search
Search failure is not itself novelty proof.

### Claim versus prior implication
The transported-table coding is additional content.

## Value
**PASS** — The construction answers a natural existence question at finite Ulm length with an explicit length-2 witness and sharp coding mechanism. Although elementary once seen, it identifies a concrete bounded p-group whose copy degrees contain a classical minimal-pair phenomenon; this is a motivated structural fact rather than an arbitrary coding slice.

## Source inspections
- **Calvert-Cenzer-Harizanov-Morozov, Effective categoricity of Abelian p-groups** (arXiv:0805.1889): full arXiv HTML abstract/introduction structure Assessment: Addresses effective categoricity and computable copies, not this noncomputable-copy degree-spectrum coding. Evidence: The abstract seeks Delta-alpha categoricity characterizations for broad p-group classes.
- **Lachlan/Yates minimal-pair theorem; Jockusch-Soare later construction** (Yates, JSL 31 (1966) 158-168; Lachlan, Proc. LMS 16 (1966) 537-569; Jockusch-Soare, JSL 36 (1971) 66-78): Cambridge abstract/extract for minimal-pair literature Assessment: The existence theorem is due independently to Lachlan and Yates; Jockusch-Soare later simplified/generalized it. The public result is repaired accordingly. Evidence: Cambridge extract explicitly states that Yates and Lachlan independently proved existence of minimal pairs of r.e. sets.
- **Melnikov, New Degree Spectra of Abelian Groups** (Notre Dame J. Formal Logic 58 (2017), DOI 10.1215/00294527-2017-0006): abstract/indexed summary Assessment: Highlighted constructions concern torsion-free abelian groups and nonlow degree classes, not this bounded p-group. Evidence: The abstract states torsion-free abelian groups with spectra characterized by nonlow_beta degrees.
- **Resultary semantic search** (Resultary local research index): top hits for bounded p-group/minimal-pair spectrum Assessment: SCOPE074 was the only direct match. Evidence: No prior exact SCOPE statement for this G was returned.

## Residual risks
- The full degree spectrum of G is not characterized; only the stated c.e.-degree inclusion is audited.
- The original source misattributed primary minimal-pair existence and misstated individual Ulm-summand contributions; both are repaired without changing the final existence claim.
