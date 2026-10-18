# Review of the square-zero image spectrum

## Correctness — PASS

The endomorphism coordinates are valid for all primes and exponents \(b\geq2\): the upper-left, upper-right and divided lower-left entries are residues modulo \(p\), and the lower-right entry is modulo \(p^b\). Computing the square on both generators forces the top-left coefficient and the reduction modulo \(p\) of the lower-right coefficient to vanish, reducing the complete system to the single congruence \(z^2+p^{b-1}vw=0\pmod {p^b}\). The valuation split is exhaustive. At even exponent it yields \((2p-1)p^{b/2}\) maps; at odd exponent the ordinary and cancellation strata combine to \(p^{(b+3)/2}\). Direct examination of the two generator images proves their cyclicity and identifies every exact order stratum. The homogeneous boundary \(b=1\) is treated separately. The accompanying `verify.py` re-enumerates endomorphisms and explicitly constructs images in fourteen finite test configurations; its final output is `VERIFY_OK`. The proof, not finite tests, establishes the infinite theorem.

## Originality — PASS, with literature limitations

Hillar--Rhea's arXiv:math/0605185v1 and Mader's 2012 *The automorphism group of finite abelian p-groups* provide structural endomorphism contexts; the former supplies the general endomorphism-coordinate framework and automorphism criteria, not the square-zero image spectra. Mader similarly treats automorphism orders, invariant subgroups and ring structure, without counting square-zero image-order fibers. Edmunds's arXiv:1402.3699v1 analyzes commuting idempotents \(E^2=E\), not nilpotent \(T^2=0\) endomorphisms; Theorem 5.9 and related sections do not count the present objects. Targeted searches in published mathematical records and previously available claims did not identify an equivalent formula or a stronger covering classification. Unlike title matching, these comparisons distinguish invertible maps, idempotents and square-zero maps by their defining equations and exact image statistics. Search and access are not exhaustive; specialized references not found here might imply some or all formulas. Accordingly novelty is evaluated against materially examined primary literature, not certified globally.

## Mathematical value — PASS

A square-zero additive endomorphism is a differential, so classifying all its possible image orders measures natural differential structures on a finite abelian group. The family \(C_p\oplus C_{p^b}\) is the first nonhomogeneous rank-two primary family, allowing its parameter \(b\) to vary arbitrarily. The result is a complete all-prime, all-exponent census rather than an isolated numerical value: every square-zero image is cyclic, every image-order multiplicity is explicit, and an extra maximal-order stratum appears precisely when \(b\geq3\) is odd. These are motivated structural and arithmetic distinctions and are not supplied by generic automorphism counts.

## Boundaries and remaining risks

The argument makes no claim for \(C_{p^a}\oplus C_{p^b}\) with \(a>1\) or higher primary rank. The result concerns all homomorphisms with \(T^2=0\), not conjugacy classes, and counting labeled operators is intentional. A duplicate theorem in unlocated specialized literature cannot be excluded. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
