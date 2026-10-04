# Same-model review

## Correctness

PASS. The original stochastic term is \(\sigma_i(t,N_i)N_i\,dW_i\). Centering by \(U_i=N_i-N_i^*\) therefore gives \(\sigma_i(t,U_i+N_i^*)(U_i+N_i^*)\,dW_i\), not the Section-4 term \(\sigma_i(t,N_i)U_i\,dW_i\). For each of the paper's four choices of \(\sigma_i\), the original diffusion at \(U=0\) is nonzero whenever the immigration intensities are positive.

A constant Itô equilibrium requires zero diffusion. Itô's formula further gives the exact short-time slope
\[
\frac{d}{dt}\mathbb E\|N_t-P^*\|^2\bigg|_{t=0+}
=
\|G(P^*)\|^2>0.
\]
The source benchmark arithmetic was replayed exactly.

## Originality

PASS. The primary paper presents equations (4.1)–(4.2) as a mean-square stability analysis of equations (2.1)–(2.2), but the stochastic coefficients are different. General SDE stability literature states the standard zero-diffusion equilibrium requirement; no inspected source applies it to this paper or gives the four source-specific centered diffusion vectors and departure rates. Exact-title and correction searches found no published repair.

## Value

PASS. The paper's central conclusion that sufficiently small random immigration yields stability is tied to Theorem 4.3. The theorem applies only after the noise has been altered so that it vanishes at the deterministic equilibrium. This changes the scientific interpretation: the original nonzero-noise model may have stationary fluctuations, but it cannot possess the claimed asymptotically mean-square stable deterministic point \(P^*\).

## Closest literature and limitations

The primary source is DOI 10.3934/math.2024725. Senosiain and Tocino (2023), DOI 10.1007/s11075-022-01478-6, provide the closest inspected general mean-square-stability framework and explicitly assume vanishing drift and diffusion at an equilibrium position.

The finding does not classify invariant measures or moment boundedness of the original model. Theorem 4.3 may remain a valid result for the altered Section-4 SDE.

Same-model review: passed. Independent audit: not yet performed.
