# Scientific review of corrected quantitative result

## Correctness — PASS

The proved claim is the explicit lower bound on the *relative* gap \(1-\omega_\mathrm Q/\omega_\mathrm{NS}\ge(d-2t)/(512(d-t)\binom dt^3)\) for all \(t\ge2,d>2t\). It follows from the branch-vector score-deficit identity, spectral Poincaré inequality for the Kneser disjointness matrix, translation-covariant deviation control, and a radius-\(t\) sphere containing a vertex in Hamming layer \(t-2\) not in the reference sphere. The key mismatch bound is \(h^2\ge1/(256\binom dt^3)\). Finite numeric tests confirm selected instances but are not the unrestricted proof.

## Originality — PASS for quantitative strengthening only

Wang's 2026 manuscript proves finite-dimensional nonattainment, but on 12 October 2026 a published formal proof already established the strict **supremum** inequality for the same binary hypercube game. The original qualitative first-separation attribution is therefore withdrawn. That earlier quantitative bound for the relative deficit is \(1/[k^4(4\sqrt2 t+2)^2]\), \(k=\binom dt\). The corrected bound \((d-2t)/[512(d-t)k^3]\) exceeds it for every parameter, with minimum bound ratio \((1320+320\sqrt2)/1536>1\) at \((d,t)=(5,2)\). The stronger coefficient and dependence on \(k\) are not found in the inspected earlier proof. Priority remains best-of-knowledge.

## Value — PASS

The improvement by one full power of the number of local outputs is a substantive all-parameter quantitative strengthening, explaining a sharper stability mechanism through Kneser expansion and incompatible Hamming layers. No optimal constant or quantum-over-classical separation is claimed.

## Sources and limitations

Primary sources: Wang, arXiv:2610.12949v1, Theorems 5.5, 6.4 and §7; the public 2026-10-12 formal proof at https://www.trureturing.org/research/wang-2026-hypercube-rendezvous-quantum-gap/ and https://github.com/the-omega-institute/trureturing/commit/e49cc795f9ba7da8af100046ca34dd602be46c05; Cui et al., *Quantum Perfect Matchings*, doi:10.1007/s00023-025-01632-5. The formal prior proof settles the qualitative question and cannot be ignored. The comparative claims were checked by explicit formulas, not titles. Other unidentified quantitative bounds remain a priority risk. Complete historical review evidence remains preserved in the source Git history.
