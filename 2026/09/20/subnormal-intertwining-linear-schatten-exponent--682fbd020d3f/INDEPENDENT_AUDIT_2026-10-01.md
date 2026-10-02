# Independent audit — 2026-10-01

**Record:** SCOPE-20260920-682fbd020d3f — Linear Schatten exponent for consecutive-power intertwinings

**Disposition:** passed

## Final claim

If \(A\) and \(B^*\) are subnormal and \(A^nX-XB^n\) and \(A^{n+1}X-XB^{n+1}\) lie in \(S_p\), then \(AX-XB\in S_{3np}\); no universal conclusion \(S_q\) is possible for all such data when \(q<(n+1)p\). Under the older range-inclusion hypotheses the cubic stop also yields the ideal refinement \(I^{1/(3\cdot2^{n-1})}\).

## C — correctness

The identities \(A^nC=D_{n+1}-D_nB\) and \(CB^n=D_{n+1}-AD_n\) put the two endpoint products in \(S_p\). Normal-extension complex interpolation for a subnormal operator proves \(T^nY\in S_p\Rightarrow TY\in S_{np}\). Hyponormality plus Douglas factorization then gives \(A^*C,CB^*\in S_{np}\), and \(CC^*C=CX^*A^*C-CB^*X^*C\in S_{np}\). Polar decomposition converts this exactly to \(C\in S_{3np}\). The diagonal root-of-unity example verifies the lower barrier \(q\ge(n+1)p\). No finite experiment is used as an infinite proof.

## O — originality

Kittaneh 2006 explicitly proves the consecutive-power implication under weaker range-inclusion hypotheses but obtains the exponential Schatten conclusion \(S_{2^{n+1}p}\). Its proof already reaches \(A^*C\) and \(CB^*\) in the \(2^{n-1}\)-root ideal, but then continues root extraction rather than using the cubic identity as in the audited claim. Kittaneh 1986 gives \(S_{8p}\) for \(n=2\). No inspected source or Resultary record implied the subnormal \(S_{3np}\) theorem or its \((n+1)p\) lower barrier.

### Source inspections

- **Some intertwining relations modulo operator ideals** (DOI:10.1017/S0017089505002910): PARTIAL_COVERAGE. The primary theorem gives the earlier exponential root-ideal/Schatten exponent and does not state or imply the subnormal \(3np\) interpolation sharpening.

## V — value

Replacing exponential dependence \(2^{n+1}p\) by a linear upper bound and pairing it with a linear-order lower obstruction materially locates the correct growth scale. The arbitrary-ideal cube-root refinement is also a genuine quantitative sharpening of the classical proof, making the result a motivated operator-ideal advance rather than a cosmetic reformulation.

## Residual risks

- Older commutant-modulo-ideal, subnormal interpolation, or symmetric-ideal literature may contain an equivalent \(O(n)\) exponent under different notation; no such implication was located.

This audit is a mathematical review, not external peer review, formal verification, or a guarantee of priority.
