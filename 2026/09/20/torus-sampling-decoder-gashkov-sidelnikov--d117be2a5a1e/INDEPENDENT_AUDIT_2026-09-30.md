# Independent audit — 2026-09-30

**Record:** `2026/09/20/torus-sampling-decoder-gashkov-sidelnikov--d117be2a5a1e`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `0810b4039a84242fef572f0d8d62523f17822305`  
**Disposition:** **PASSED**

## Correctness — PASS

The character-sum derivation was checked line by line. For a length-three syndrome n=N(S) is neither 0 nor 1. The fiber equation for a=N(S-beta) is a quadratic in beta whose discriminant in characteristic three is Delta_n(a)=(n+1-a)^2-n; the number of norm-one roots is 1-chi(Delta_n(a)). Combining this with the source paper's length-two criterion and sum_a chi(a(a-1))=-1 gives M(S)=(q+2+J_n)/2. The quartic X(X-1)((n+1-X)^2-n) is squarefree for n notin{0,1}; its square leading coefficient gives two rational points at infinity, hence #C_n(F_q)=q+J_n+2=2M(S), and Hasse yields the stated half-density bound. The three choices of first summand in each minimum three-term decomposition give L(S)=M(S)/3. The supplied finite-field artifact independently enumerates q=9,27,81 and confirms the identity, divisibility, Hasse bound and leader multiplicities; no inconsistency was found.

## Originality — PASS (literature-bounded)

The motivating Shi–Li–Xia–Helleseth–Ozbudak preprint was posted on 17 September 2026 and explicitly supplies the norm-one-torus model, minimum additive-length classification and constructive weight-three decoders using quadratic-character sums and Weil bounds. The assigned record does not claim those ingredients. Searches for the exact successful-first-summand count, the genus-one curve C_n, or an elliptic-point-count formulation of the direct torus search did not locate the same theorem. Because the source preprint is extremely recent and the older Zetterberg decoding literature is broad, near-simultaneous or differently phrased overlap remains a material residual risk.

## Scientific value — PASS

The result upgrades an existence/sequential search into an exact success-count theorem and a uniform Las Vegas probe bound asymptotic to two, while also quantifying the number of minimum-weight leaders. The elliptic-curve formulation explains syndrome-to-syndrome fluctuations through Frobenius traces.

## Evidence and literature

- Shi et al., Norm-One Torus Decompositions and Decoding of Gashkov-Sidel'nikov Codes (2026): https://arxiv.org/abs/2609.20402
- Shi et al., Determining the Covering Radius of All Generalized Zetterberg Codes in Odd Characteristic (2025): https://doi.org/10.1109/TIT.2025.3544025
- Dodunekov and Nilsson, Algebraic Decoding of the Zetterberg Codes (1992): https://elib.dlr.de/33872/

## Limitations

- The theorem is specific to the characteristic-three norm-one-torus model for the original Gashkov-Sidelnikov families.
- It improves candidate-probe counts, not the bit complexity of the finite-field arithmetic used after a successful probe.
- The motivating preprint is only days older than this record, so the originality boundary is especially sensitive to near-simultaneous work.

The independent audit finds the record scientifically complete on correctness, originality, and value at the audited tree. The originality verdict is bounded by the literature access and searches described above and does not treat inaccessible material as read.
