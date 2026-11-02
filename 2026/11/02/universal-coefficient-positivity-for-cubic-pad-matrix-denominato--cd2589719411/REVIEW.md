# Scientific review: Universal coefficient positivity for cubic Padé matrix denominators

## Correctness — PASS

PASS: The explicit normalized Padé denominator is checked against the general factorial formula. After the exact translation z=t+w (t=k+1), its cubic has one real root r in (1/2,2/3) and the conjugate pair -r/2±ib. Its positive pole R=t+r is strictly smallest in modulus. Partial fraction residues A>0 and B obey A>2|B| because an exact squared-residue difference equals 9r^4(1-r)(r^3-4r^2+10r-4)/(4(2-3r)^2)>0. Consequently c_n≥(A-2|B|)R^(-n)>0 for every independent k,n≥0. Matrix convergence and positivity follow from the matrix power series and Perron-Frobenius. Symbolic algebra and 15,914 executable tests checked, not substituted for, the infinite proof.

**Primary evidence.** The normalized denominator and cubic translation appear in `RESULT.md`; the sign-reduced residue identity supplies a uniform analytic certificate for every integer numerator degree and Taylor index. The `verify.py` code replays the exact polynomial identities and 15,914 assertion-level symbolic/rational checks from the actual extracted package. These tests do not establish infinitely many cases on their own.

**Risk.** Symbolic algebra reflects the displayed formula; the root interval, positive sign factors and Perron–Frobenius consequences must be understood analytically. The proof explicitly handles all real-root, conjugate-root and matrix boundary cases.

## Originality — PASS (historical-priority risk remains)

PASS under available historical evidence: The 2019 Fasi–Higham Conjecture 3.2 states the odd-denominator positivity question but does not prove the all-k cubic specialization. The 2025 Al-Mohy–Liu primary preprint studies the same [3+p/3] matrix denominator in numerical matrix-function algorithms but not its reciprocal-coefficient signs. Scardino (October 28, 2026) proves all-n only at k=0, and eventual positivity under a spectral condition for other k, so his claims do not imply all n for k≥1; his degree-five counterexamples concern a different denominator order. Comparisons with primary literature, indexed mathematical findings and accessible historical claims identified no equivalent or broader proven all-k,m=3 result. Older Padé root-asymptotic work was only bibliographically accessible, so historical priority is not certified.

**Source distinctions.** Fasi–Higham, Conjecture 3.2 (2019), asks the general odd-degree question. Scardino (2026), Theorems 3.1, 7.1, 8.2, proves the zero-numerator case and conditional eventual signs, while giving counterexamples for degree five; neither result establishes all coefficient indices for arbitrary positive numerator degrees in the cubic case. Al-Mohy–Liu (2025), Sections 2–3, uses the same Padé denominators for numerical matrix functions but does not prove reciprocal positivity. Comparisons with indexed mathematical findings found closest differing objects including a degree-three Chebyshev semi-iterate, [2/2] Padé Markov positivity, and Lanczos exponential positivity; accessible existing claims were separately checked for this exact implication.

**Risk.** Earlier equivalent Padé or recurrence formulas cannot be categorically excluded. A plausible older Driver–Temme full text was inaccessible and is not treated as excluded or as a novelty certificate. No unperformed independent assessment is implied.

## Mathematical value — PASS

PASS: The exact all-degree cubic case of a named unresolved Padé reciprocal-positivity problem is substantive: it proves simultaneous positivity for infinitely many numerator degrees and all Taylor orders, including the finite initial coefficients not supplied by available eventual-positivity theorems. In numerical linear algebra it gives an exact positive-cone and sharp spectral-radius guarantee for denominators of [3+p/3] Padé matrix φ-function recovery, rather than a limited collection of low-order numerical examples. No general odd-degree theorem, matrix rational numerator guarantee, or complexity improvement is claimed.

**Scope.** The result is one cohesive cubic-denominator theorem with the positive-matrix inverse as a consequence. It does not prove any higher odd degree or full method performance bound. The numerical denominator occurs in practical \([3+p/3]\) exponential Padé and matrix \(\varphi\)-function recovery for \(p\ge0\).

Self-review: passed. Independent audit: not yet performed.
