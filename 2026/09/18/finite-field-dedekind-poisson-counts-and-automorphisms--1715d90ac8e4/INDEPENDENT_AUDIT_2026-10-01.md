    # Independent mathematical audit — 2026-10-01

    ## Record

    **Finite-field enumeration and automorphism orders for Dedekind Poisson algebras**

    Disposition: **PASSED**.

    ## Correctness — PASS

    The finite-field reduction and counting are correct. In characteristic two, perfectness makes the diagonal quadratic map a square of a linear form, so anisotropy forces active dimension one. In odd characteristic, Chevalley--Warning forces active dimension at most two. In dimension two, the zero-bracket anisotropic form has one similarity class; for nonzero bracket the operator \(T\) defined by \(\omega(u,v)=\beta(u,Tv)\) satisfies \(T^2=\kappa I\) with nonsquare \(\kappa\), and conjugacy preserves \(\kappa\). This yields the stated class counts. Independent brute-force checks over \(\mathbf F_3,\mathbf F_5,\mathbf F_7\) reproduced one zero-bracket active class, \((q-1)/2\) mixed active classes, and active similitude orders \(2(q^2-1)\) and \(q^2-1\). The triangular automorphism count gives the stated powers of \(q\).

    ## Originality — PASS

    The arbitrary-field source gives the structural classification and simultaneous-similarity criterion, but it does not, in the material available for inspection, solve the finite-field orbit count or give the all-dimensional enumeration and automorphism-order formulas. The finite-field orbit reduction and stabilizer computation are therefore a genuine specialization theorem rather than a restatement of a listed case.

    ### Equivalent formulations

Searches: Dedekind Poisson finite field isomorphism classes automorphism group; Dedekind Poisson q+5 finite fields; published SCOPE search: Dedekind Poisson finite fields

Evidence: No source located an equivalent all-dimension finite-field count or the displayed automorphism formulas.

Reasoning: The arbitrary-field classification parameterizes Type II objects by simultaneous-similarity classes of forms; it does not identify those finite-field orbits by the nonsquare scalar \(\kappa\) or count their stabilizers in the inspected material.

### Broader coverage

Searches: Plakosh Pypka Dedekind Poisson Algebras over Arbitrary Fields arXiv:2609.13767; Petrov Pypka low-dimensional Poisson algebras arbitrary fields arXiv:2609.13784

Evidence: The Plakosh--Pypka abstract states a complete structural classification over arbitrary fields; the low-dimensional paper overlaps normal-form phenomena in small dimensions.

Reasoning: The broader structural theorem is essential prior art, but an orbit classification by finite-field invariants and explicit automorphism orders is additional work. The low-dimensional classification does not supply the stable all-dimensional counts.

### Exact database or table

Searches: finite field Dedekind Poisson number of isomorphism classes q+5; finite field Dedekind Poisson automorphism order; published-record semantic query: Dedekind Poisson finite fields

Evidence: No exact table with the claimed counts or stabilizer orders was located. The semantic record-search service returned no usable result during this audit.

Reasoning: The exact quantities are natural finite-field moduli counts rather than values copied from a known table.

### Claim versus prior implication

Searches: arXiv:2609.13767 arbitrary-field classification simultaneous similarity; finite-field anisotropic binary quadratic form similarity classes

Evidence: The prior classification reduces the problem to an orbit problem but does not by itself enumerate the orbits or their stabilizers; the finite-field argument uses additional dimension-collapse and binary-form calculations.

Reasoning: The claimed formulas are not obtained by substituting a parameter into an already enumerated stronger theorem. They require solving the remaining finite-field moduli problem.

    ## Source inspections

    - **Dedekind Poisson Algebras over Arbitrary Fields** (arXiv:2609.13767): trigger — direct source of the structural classification used by the record; material read — primary abstract and theorem-level public summaries of the arbitrary-field classification; full arXiv text could not be retrieved through the lawful routes available in this audit; assessment — BROAD_PRIOR_STRUCTURE, no located exact finite-field enumeration or automorphism table. Evidence: The abstract explicitly claims a complete arbitrary-field classification and highlights characteristic-two information, but does not state finite-field class counts or automorphism-group orders.
- **On the Structure of Low-Dimensional Poisson Algebras over Arbitrary Fields** (arXiv:2609.13784): trigger — plausible overlap with three-dimensional normal forms; material read — available abstract/search material; assessment — PARTIAL_OVERLAP only in low-dimensional normal-form context. Evidence: The source is low-dimensional and does not provide the all-dimensional Dedekind finite-field count/stabilizer table located here.

    ## Checked sources

    - arXiv:2609.13767
- arXiv:2609.13784
- Belitskii et al., Linear Algebra Appl. 402 (2005)
- published SCOPE repository searches

    ## Residual risks

    - The full text of arXiv:2609.13767 was not lawfully retrievable during this run; the originality assessment therefore retains a concrete risk that an internal corollary or remark could state part of the finite-field specialization.
- Both relevant Poisson papers are very recent, so simultaneous-work risk remains.

    ## Scientific value — PASS

    A complete finite-field enumeration with automorphism orders is a natural exact classification invariant, not an arbitrary slice. It turns the abstract simultaneous-similarity parameter into explicit moduli counts in every dimension and records stabilizer sizes that future counting or probabilistic work can directly use.

    ## Limitations

    The finite-field enumeration is a specialization of a recent arbitrary-field classification. Full primary text of that classification was not retrievable during this audit, so originality is best-of-knowledge with an explicit source-access risk.

    This document records a mathematical assessment of the stated claim and its literature context. It does not convert historical same-model review evidence into independent evidence.
