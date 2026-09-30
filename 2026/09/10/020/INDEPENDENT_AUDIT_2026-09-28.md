# Independent Audit — 2026/09/10/020

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `0ab1f618d4fe4328d81bd8f16256fb985055d21e`  
**Disposition:** **PASSED**

## Correctness

The kernel identity is correct under the stated fixed-standard-contact-form convention. Substituting the degree-2 basis relations into Takeuchi's Lemma 5.1 gives exact cancellation between the bar-Box_t Box_t numerator and Q_t. The stored independent Fraction replay confirms this for z^2, and the direct vector-field sweep kills the full H_{2,0} plus H_{0,2} basis while degree one remains nonzero. Hence P_t u*=0 and the proposed negative pairing witness is indeed false.

## Originality

Takeuchi's 2024 analysis supplies the operator formulas and proves infinitely many negative eigenvalues in odd total-degree sectors, with a remark excluding kernel there. In the inspected source I found no statement that the full even degree-2 space H_{2,0}+H_{0,2} is annihilated. The audited result is a concrete new finite-dimensional consequence requiring an explicit cancellation calculation, not merely a quotation of the prior theorem.

## Scientific value

The identity has scientific value as an exact spectral constraint on a canonical non-embeddable CR family: it rules out an apparently natural degree-2 negativity witness and clarifies where Paneitz negativity cannot be detected. It is narrow but reusable in subsequent spectral/embeddability analyses.

## Limitations

- Fixed standard contact form and real |t|<1 only.
- Does not establish a new Kohn closed-range, Szego, or uniform negativity theorem.
- Originality conclusion is limited to the explicit degree-2 kernel identity relative to the closest source inspected.

## Evidence

- [Takeuchi, CR Paneitz operator on non-embeddable CR manifolds](https://arxiv.org/abs/2407.16185): Provides the Rossi operator identities and odd-degree negative-eigenvalue analysis; the inspected paper does not state the full H_{2,0}+H_{0,2} kernel identity.
- [Chanillo–Chiu–Yang, Embeddability for three-dimensional CR manifolds and CR Yamabe invariants](https://arxiv.org/abs/1007.5020): Provides qualitative Rossi Paneitz negativity/degree-one context, distinct from the degree-2 kernel calculation.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `0ab1f618d4fe4328d81bd8f16256fb985055d21e`; no repository writes were made by this audit.
