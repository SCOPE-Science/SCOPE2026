# Scientific review: A sharp modulo-eight distribution law for the semi-Pell sequence

## Correctness — PASS
The recurrence gives \(u(2m+1)=1+2\sum_{k=1}^m u(k)\), and the previous modulo-four classification permits a parity count of indices whose odd parts are three modulo four. Exact digit recursions prove the higher-bit expression \(Q(m)\). The sign-transfer matrix obeys \(T^{\mathsf T}T=2I\) and \(T^4=-4I\), yielding the rational dyadic enumeration and a uniform signed aligned-block estimate. Every cutoff decomposes into aligned binary blocks, and the even-odd sequence recursion gives the square-root frequency error. Dyadic cutoffs with exponent \(r=4a+1\) provide matching lower errors for **each** of the four classes.

The self-contained `verify.py` checks 65,535 positive terms, the higher-digit congruence for 32,768 odd inputs, sixteen exact dyadic distributions, and the finite transfer identities. Infinite statements follow from algebra and induction, not computational extrapolation.

## Originality — PASS within the inspected evidence
Keith and Munagi, arXiv:1912.11148v1 (2019), Theorem 2, give only \(u(2m+1)\equiv2m+1\pmod4\). Their 2023 journal follow-up, Theorem 6, also treats a modulo-four classification; Ballantine and Beck, arXiv:2303.11493v1, Section 6, provide self-similar partition interpretations and lower-congruence information. The four exact modulo-eight census functions and all-cutoff sharp residue frequency theorem were not found in the inspected results. Known growth analyses of this series supply size information, not modular densities. published-finding corpus searches targeting semi-Pell, binary digit statistics, modulo-eight frequency, and dyadic counts returned no covering record. More general unindexed digital identities are a genuine remaining priority risk.

## Mathematical value — PASS
This is a complete higher-2-adic classification of a natural, previously studied number-theoretic sequence. Its new adjacent-bit formula supports an exact four-class census at every dyadic scale and a quantitatively sharp natural-density theorem. The optimal discrepancy for all four residues gives structural information unavailable from parity or modulo-four congruences alone. It may guide analogous work on higher powers of two and other self-similar sequences.

## Closest literature and limitations
- Keith--Munagi 2019, arXiv:1912.11148v1, Theorem 2 (same sequence, modulo four).
- Keith--Munagi 2023, DOI 10.61091/ojac-1802, Theorem 6 (broader composition interpretation and modulo four).
- Ballantine--Beck 2023, arXiv:2303.11493v1, Section 6 (self-similar partition interpretation and congruences).
- OEIS A129095/A129096 (sequence and bisection tables).

Only modulus eight and the four odd residue classes are covered; sharp implied constants and higher moduli are not determined. Searches do not certify absolute priority, and some potentially relevant portions of later primary work remain uninspected. Independent scientific verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
