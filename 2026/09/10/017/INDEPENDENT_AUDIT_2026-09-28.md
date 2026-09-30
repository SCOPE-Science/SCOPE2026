# Independent Audit — 2026/09/10/017

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `edc8cc9b46132f8ab68e710d9af8d3f2d4a8eaa7`  
**Disposition:** **PASSED**

## Correctness

The arithmetic claim checks out. The factorization f=(x^2+1)(x^4+30x^2+1) is exact, D_1 and D_2 have the stated rational witnesses, and any Q_2-point on 7u^2=x^2+1 would yield a primitive Z_2 solution X^2+Z^2=7U^2. Modulo 8 every such solution has X,Z,U even, contradicting primitivity. Thus D_7(Q_2)=empty and hence D_7(Q)=empty. The assigned artifacts encode the same finite checks; the conclusion does not depend on the asserted Hilbert-symbol mnemonic.

## Originality

Balakrishnan–Dogra already analyze this exact X_31 benchmark and its rational points by quadratic/non-abelian Chabauty, so the curve and its rational-point problem are not new. The audited claim is narrower and method-specific: in the primary comparison inspected, I found no statement identifying the factorization twist D_7 and certifying its elimination by this 2-adic primitive mod-8 obstruction. Flynn–Wetherell-style covering collections are established prior methodology, so originality is limited to the explicit certificate for this benchmark, not to the method or curve.

## Scientific value

The result has modest but real scientific value as a short, exact, independently replayable descent certificate on a standard rank-exceeds-genus benchmark. It supplies a classical local-obstruction cross-check complementary to the heavier Chabauty analysis, while correctly disclaiming a complete X(Q) census.

## Limitations

- Does not determine D_1 or D_2 and does not give a full rational-point census.
- Novelty is only for the explicit D_7 local certificate; the benchmark curve and covering-collection method are prior art.
- Literature comparison was targeted to the exact benchmark and nearest covering literature, not an exhaustive proof of priority.

## Evidence

- [Balakrishnan–Dogra, Quadratic Chabauty and rational points II: Generalised height functions on Selmer varieties](https://academic.oup.com/imrn/article/2021/15/11923/5718597): Treats the family including a=31 and its rational-point problem by generalized heights/non-abelian Chabauty; does not supply the audited D_7 mod-8 covering certificate in the inspected text.
- [Flynn–Wetherell, Covering collections and a challenge problem of Serre](https://doi.org/10.4064/aa98-2-9): Establishes covering-collection methodology; supports that the method itself is not new.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `edc8cc9b46132f8ab68e710d9af8d3f2d4a8eaa7`; no repository writes were made by this audit.
