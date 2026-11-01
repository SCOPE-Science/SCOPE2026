# Scientific review

## Correctness — PASS
The exact group \(C_{p^2}\times C_p\), counting inner products, unnormalized coset sums, and all \(p\ge2\) prime are fixed. All maximal cyclic subgroups are enumerated by an elementary order argument; character triviality gives an exhaustive three-case spectral partition, positive full rank, and explicit exclusive witnesses for all \(2p\) direction families. A positive-sum inequality and its equality conditions prove the weighted optimum for every positive direction-weight assignment. The standalone exact-integer checker separately constructs every coset and normal Gram matrix for primes \(2,3,5,7\). No finite test is used as an infinite-parameter proof.

## Originality — PASS with bounded-search risk
Ilmavirta's original paper describes maximal Radon transforms and the elementary abelian square \(C_p^2\), but does not state the present nonhomocyclic spectral and optimal-conditioning theorem; its relevant Section 7.3 was read. The published square cyclic-grid scalar-view theorem covers \((\mathbb Z/N)^2\), not \(C_{p^2}\times C_p\), and its full public result was inspected. Kingston and Svalbe's 2005 projective Fourier-slice paper addresses square arrays; only publication metadata and abstract were available. Kumar's 2020 paper counts maximal cyclic rank-two subgroups, with only accessible abstract metadata examined; its Radon consequences, if any, are not resolved by full-text inspection. Focused searches for group aliases, prime-power cases, maximal cyclic transforms, and exact spectra found no statement implying all the present conclusions. An overlooked equivalent formulation remains possible; search failure alone is not a proof of novelty.

## Value — PASS
This is a natural next structural case after elementary abelian prime grids in maximal-cyclic finite tomography: the smallest nonelementary rank-two abelian prime-power group. The theorem simultaneously resolves whether every maximal direction is needed, the complete nonconstant singular spectrum, and whether scalar reweighting can remove the conditioning obstruction. The inseparable \(p-1\)-dimensional Fourier sector gives a sharp \(\sqrt p\) barrier, relevant to acquisition stability. The statement is not claimed for other prime-power ranks, fewer cosets, or arbitrary frequency-dependent preconditioners.

## Limitations and verification status
The sources provide background definitions and neighboring results, not independent verification of this theorem. The exact code tests finitely many primes; the all-prime proof is analytic. Published-priority review is bounded and independent auditing remains outstanding.

Self-review: passed. Independent audit: not yet performed.
