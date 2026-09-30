# Independent Audit — 2026/09/15/023

Audit date: 2026-09-29 (UTC)
Audited tree: `125c69336c7d8a82ce2be62fd03aa06d3e0a9d92`

## Disposition

**PASSED** — All three axes pass. The record can remain at the source path with the independent-audit evidence attached.

## Correctness

**PASS**. The product action is free and ergodic. Its Koopman spectral measures lie on the Haar-null set T×{k alpha:k in Z}: for a Bernoulli basis vector tensored with a rotation eigenfunction the spectral measure is sigma_S×delta_{k alpha}. The Kronecker factor is exactly the irrational-rotation coordinate, and X→Z is relatively weakly mixing because the relative square is the product of S×S with the rotation action; hence no nontrivial relatively distal Host–Kra extension can lie between Z and X, so Z_<2>=Z. The coordinatewise XOR law on the Bernoulli factor is pairwise independent and diagonal-shift invariant, while g(y)=(-1)^{y_0} has zero conditional expectation over Z and triple product identically 1. This is a valid counterexample to the stated relative-independence claim.

## Originality

**PASS**. The XOR/Bernstein joining itself is classical, and Host’s 1991 theorem is a one-dimensional weakly-mixing singular-spectrum rigidity result. The nontrivial contribution here is the higher-rank spectral mechanism: a Bernoulli Lebesgue direction becomes singular as a Z^2 spectral measure after being supported on a one-dimensional slice of T^2, while the independent rotation coordinate is simultaneously identified as the complete 2-step Host–Kra factor. Existing PIJ literature supplies the joining ingredient but does not subsume this relative Z^2 counterexample; the submitted combination directly exposes why ambient T^2 singularity is too weak for the proposed extension of Host rigidity.

## Scientific value

**PASS**. This is a concise structural counterexample rather than a numerical curiosity. It identifies a precise failure mode—spectral singularity in the ambient rank can hide Lebesgue behavior along a subgroup—and cleanly separates the refuted main clause from the still-open trivial-Z_<2 subcase. That boundary information is useful for reformulating any viable higher-rank singular-spectrum joining theorem.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://doi.org/10.1007/BF02773866 — Bernard Host (1991): every pairwise-independent joining of weakly mixing one-dimensional systems with purely singular spectrum is independent.
- https://arxiv.org/abs/0704.3358 — Janvresse–de la Rue: classical pairwise-independent non-independent joinings for full-shift-type processes; establishes the XOR/PIJ ingredient as prior machinery.
- https://people.math.osu.edu/leibman.1/papers/hkz.pdf — Host–Kra–Ziegler factor background used only for the standard distal/nilsystem nature of Z_<2>.

Independent checks:
- Verified freeness: nonzero Bernoulli shifts have only periodic fixed sequences of measure zero, while nonzero irrational rotations have no fixed points; verified ergodicity by successive invariance under the two generators.
- Computed the spectral support sigma_S×delta_{k alpha} for basis tensors and hence singular maximal spectral type on T^2.
- Verified pairwise independence of (Y1,Y2,Y1⊕Y2), invariance under the shift, and the exact triple correlation g(Y1)g(Y2)g(Y1⊕Y2)=1.
- Checked that relative weak mixing of X over the rotation factor rules out a nontrivial intermediate distal factor, yielding Z_<2>=Z.

Limitations:
- The counterexample has nontrivial Z_<2>; it does not settle the record’s explicitly separated trivial-Z_<2 subcase.
- The originality claim is for the higher-rank relative counterexample and its spectral mechanism, not for the classical XOR joining itself.
- No inaccessible source is represented as read.
