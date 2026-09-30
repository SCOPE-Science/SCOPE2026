# Independent Audit — 2026/09/12/024

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `61b66909a82e429122f52c0f74e8aa797e64399d`  
**Disposition:** **PASSED**

## Correctness

The arithmetic route is sound. In Q(sqrt(2)), 7 splits; at the two 7-adic embeddings sqrt(2) is congruent to 10 or 39 mod 49, so epsilon=1+sqrt(2) is 11 or 40, and neither residue lies in the local norm subgroup characterized by u^6=1 mod 49. Thus the base-unit norm index in the cyclic first layer is 7. Chevalley's ambiguous class-number formula then gives a trivial fixed 7-class subgroup; a nontrivial finite 7-group acted on by a 7-group would have nontrivial fixed points, so the full 7-primary class group of k1 is trivial. Sinnott/circular-unit index formulas preserve this 7-part, and standard stabilization for the totally ramified cyclotomic Z7-extension yields lambda=mu=0 from the consecutive trivial 7-class groups.

## Originality

The closest accessible classical paper of Fukuda and Komatsu studies split odd primes in real quadratic cyclotomic Z_p-extensions and gives p=7 numerical tables, but explicitly says their class-group input A0 had only been determined for p=3 or 5 in those examples, so it does not certify this Q(sqrt(2)), p=7 case by its stated theorems. Targeted searches found no source stating the exact first-layer norm obstruction and 7-maximality result for this field. A companion 1986 Journal of Number Theory paper was identified but its full text could not be lawfully read in this run because publisher verification required human action; the audit does not claim to have read it.

## Scientific value

An explicit proof of Greenberg-type vanishing for the concrete split prime p=7 over Q(sqrt(2)), together with a first-layer circular-unit maximality certificate, is a nontrivial arithmetic datum. The local norm calculation is compact and independently checkable and closes the field-specific case without relying on a black-box degree-14 class-group computation.

## Limitations

- The 1986 Journal of Number Theory companion paper could not be read in full because publisher verification required human action; the audit records this explicitly and does not attribute any unverified example to it.
- The audit accepts the standard circular-unit/class-number bridge and cyclotomic stabilization theorems rather than reproving them from first principles.
- The result is field- and prime-specific and does not establish a new general criterion beyond the cited Iwasawa theory.

## Evidence

- [Fukuda–Komatsu, On Z_p-extensions of real quadratic fields](https://doi.org/10.2969/jmsj/03810095): Gives stabilization criteria for split odd primes and examples for p=3,5,7; the paper states that in its example table A0 had been determined only for p=3 or 5, so the p=7 rows were not all covered by its theorems.
- [Fukuda–Komatsu, On the lambda invariants of Z_p-extensions of real quadratic fields](https://doi.org/10.1016/0022-314X(86)90093-4): A close 1986 companion paper with sufficient conditions and examples. Full text remained inaccessible in this automated run after lawful OA/arXiv attempts and an institutional-access attempt reached human verification; no claims from its unread body are used.
- [Gras, Application of the notion of Phi-object](https://arxiv.org/abs/2112.02865): Provides characterwise class-number/cyclotomic-unit formulas relevant to the record's finite-layer index bridge.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `61b66909a82e429122f52c0f74e8aa797e64399d`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
