# Scientific review: exact revival thresholds under telegraph noise

## Correctness — PASS

For the specified stationary telegraph process and independent isotropic qubit depolarizer, the known unital-qubit criterion gives the exact entanglement-breaking inequality. The sign lobes of telegraph coherence are explicit. The negative second derivative of the logarithmic coherence-to-threshold ratio proves that each lobe has at most one non-entanglement-breaking interval; the strict translation inequality orders the critical rates. Upper and lower analytical bounds at successive extrema yield the Lambert-count and static-noise asymptotics with bounded index error. A standalone implementation independently checks telegraph matrix exponentiation and the partial-transposed Choi eigenvalues on finite test sets. Remaining mathematical limits are fixed parameters, fair stationary switching, and a single-qubit channel; finite tests do not prove the asymptotics.

## Originality — PASS, with priority limitations

Ruskai (arXiv:quant-ph/0302032) proved the foundational unital-qubit entanglement-breaking criterion. Zhou, Lang and Joynt (arXiv:0912.3313, Eq. (37), Sections V–VII) directly established telegraph-driven entanglement sudden death/revival and **qualitative finiteness of revivals under relaxation**. D'Arrigo and collaborators (arXiv:1210.1122) gave an equivalent telegraph coherence function. Shrikant, Srikanth and Banerjee (arXiv:1805.11411) examined related but different qubit channel constructions. The present claimed gap is narrower: exact, strictly ordered per-lobe depolarization thresholds for an explicitly independent isotropic depolarizer, the unique active interval within every lobe, and the two-term Lambert-W count versus singular static-noise scaling. This is not claimed to invent entanglement revivals or qualitative finite revival. Searches and direct primary-source comparisons did not locate those sharp statements; a broader unlocated theorem may imply them, and independent priority review remains necessary.

## Value — PASS

The channel-wide number of entanglement-preserving recovery windows is a natural and operationally meaningful discriminator between coherent oscillations and preserved quantum correlations. The count laws quantify how the number of recoveries diverges as an independent Markovian noise rate vanishes. The sharp negative logarithmic correction and the different inverse-rate endpoint behavior supply more information than a routine single crossing calculation. The scope is restricted to a stationary two-state fluctuator, pure phase rotation, and isotropic Markovian noise; no claim is made about hardware operating costs or other entanglement witnesses.

Self-review: passed. Independent audit: not yet performed.
