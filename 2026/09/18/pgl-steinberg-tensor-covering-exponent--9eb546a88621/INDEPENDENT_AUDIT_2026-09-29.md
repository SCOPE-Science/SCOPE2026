# Independent audit — 2026-09-29

Record: `2026/09/18/pgl-steinberg-tensor-covering-exponent--9eb546a88621`  
Assigned and audited source tree: `34245d1437932e87e6b3dd1006b91c6d4fa5e9a9`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **repaired**

## Correctness

**supported**. The representation-theoretic proof is correct. Monteiro–Stasinski supply all nonlinear center-trivial irreducibles in St^2, self-duality supplies the trivial constituent, and every nontrivial center-trivial linear λ is absent because λSt is an irreducible distinct from St (a semisimple diagonal element with nonzero Steinberg value witnesses the distinction). Thus the square misses exactly those linears. If χ were absent from St^3, then χSt would be supported only on the d−1 missing linears; each can occur with multiplicity at most one because λSt is irreducible, forcing χ(1)St(1)≤d−1, contradicting St(1)≥q>d−1. The S_3 exception is direct. Twisting then gives the stated full compatible central-character fiber for GL_n(q) from the third power onward.

## Originality

**repaired_repository_precedence**. The original record’s first-discovery framing is not sustainable inside SCOPE. An earlier repository record, 2026/09/17/steinberg-covering-number-for-pgln--e3667d632f22, published at 2026-09-17T23:23:16Z, already proves the same universal Steinberg cube and exact 2/3 covering exponent. The present record can still add value through its exact description of every missing square constituent, its shorter degree-obstruction proof, and its twisted GL central-character-fiber corollary, but it must be presented as an alternate/refining derivation rather than a separate discovery. The staged repair makes that precedence explicit throughout the research files.

## Scientific value

**retained_as_corroborating_refinement**. After repair, the record remains useful as an independent alternate proof and as a compact exact square-support/twisting refinement. Its value is corroborative and expository relative to the prior SCOPE theorem, not priority for the 2/3 exponent itself.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/pgl-steinberg-tensor-covering-exponent--9eb546a88621
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/steinberg-covering-number-for-pgln--e3667d632f22
- https://arxiv.org/abs/2609.17319
- https://arxiv.org/abs/1209.1768
- https://doi.org/10.37236/13289

## Limitations

- The exact 2/3 covering exponent and universal cube are not new relative to the earlier 2026/09/17 SCOPE record.
- The exact square-support description is a short consequence of the same recent nonlinear-coverage theorem.
- The main external input is a September 2026 preprint, so attribution may evolve with later revisions.
