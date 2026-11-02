# Scientific assessment

## Correctness — PASS

The theorem fixes the alphabet, weight, endpoint overlap lengths, and self-pair quantifier. Shorter-gap rotation orbits partition all weight-two words; forbidding rotations by one and two gives \(\lfloor P/3\rfloor\) per orbit. The explicit three-spaced selection achieves the sum, and the proof checks every possible kind of weight-preserving length-one or length-two shift, including the two-marker deletion and antipodal tie. The standalone program independently checks all pairs at small lengths and successor constraints at larger lengths. Main residual correctness risk is an overlooked boundary case in the case distinction; direct checks through length 120 mitigate but cannot prove away that risk.

## Originality — PASS (best-knowledge, qualified)

The most closely matching primary paper, Blackburn–Nasr Esfahani–Kreher–Stinson (arXiv:2211.10309), gives bounds for unrestricted overlap-free codes and constructions for other parameter regimes; its full accessible text does not present the weight-two exact capacity. The WMU primer paper by Yazdi–Kiah–Gabrys–Milenkovic (arXiv:1709.05214) treats general and balanced code constructions and does not establish the present sparse two-marker maximum. Related published finite non-overlap code classifications concern a strictly stronger set of forbidden overlap lengths and different compositions. Actual semantic-result searches and prior-claim comparisons did not produce a dominating theorem, but an unindexed equivalent specialization remains possible. This assessment is not a claim of independently certified publication priority.

## Mathematical value — PASS

The fixed weight-two condition is a natural sparse-composition model for synchronized identifiers and cannot be answered from the unrestricted exponential-alphabet bounds. The result computes an infinite family of exact constrained capacities, proves the asymptotic one-third packing fraction, and identifies the half-length antipodal correction. The constructive attainment of separate necklace bounds requires controlling cross-necklace overlap edges and is the substantive part. No downstream general-weight theorem is asserted.

## Closest literature and limitations

Blackburn et al., 2022 (arXiv:2211.10309), Theorem 1 and constructions; Yazdi et al., 2017 (arXiv:1709.05214), weakly mutually uncorrelated and balanced codes. Remaining risk: an equivalent special case in unindexed or obscure coding literature. Only two markers and the two longest forbidden proper overlaps are covered; no third-party verification has been performed.

Self-review: passed. Independent audit: not yet performed.
