# Self-review

## Correctness
PASS. The proof has two independent exact components. First, the tight-frame POVM gives a matching lower bound \(d/n\) for the guessing probability, while \(|\psi_x\rangle\langle\psi_x|\preceq I\) gives the matching upper bound. Second, the uniform-rank subentropy formula follows from the source's normalized simplex representation and the exact beta moment \(\mathbb E(S\log S)\). Applying it to the two spectra produces the displayed harmonic gap. The equality case \(n=d\) is also exact.

The accompanying checker confirms explicit Fourier tight frames, POVM normalization, success probability, and the harmonic-gap sign over a finite test grid. Those tests support implementation correctness but do not substitute for the quantified analytic proof.

## Originality
PASS. The direct 2013 source states the all-cq inequality as Conjecture 2 and proves the pure-state case only for two labels, with numerical evidence for three labels. Searches under conditional-subentropy, tight-frame, projective-one-design, SIC, guessing-probability, and harmonic-number formulations found no statement of the exact formula \(Q(X|B)=\log(n/d)-(H_n-H_d)\).

The strongest overlap is arXiv:2607.01564, which proves the state-discrimination ingredient \(p_{\mathrm{guess}}=d/n\) for equiprobable tight frames. That component is treated as prior work. The inspected paper does not discuss subentropy or the 2013 conjecture. The older tight-frame/quantum-measurement source arXiv:quant-ph/0106070 likewise does not cover conditional subentropy. A differently indexed projective-design formulation remains a residual risk.

## Value
PASS. The result settles a natural infinite higher-dimensional sector of a published quantum-information conjecture and gives the exact amount by which the bound is strict for every overcomplete tight frame. Equal-weight tight frames/projective one-designs are canonical measurement and encoding objects, so the statement is not an arbitrary finite slice. The exact harmonic gap may also be useful when comparing discrimination and entropy-like quantities for structured ensembles.

## Closest literature and limitations
The 2013 source supplies the conjecture and subentropy machinery; the 2026 tight-frame encoding paper supplies the optimal discrimination probability; the 2001 frame paper supplies the foundational POVM/frame correspondence. The finding connects these ingredients through a new exact uniform-rank subentropy calculation. It does not settle nonuniform, mixed-state, or non-tight instances of the conjecture.

Self-review: passed. Independent audit: not yet performed.
