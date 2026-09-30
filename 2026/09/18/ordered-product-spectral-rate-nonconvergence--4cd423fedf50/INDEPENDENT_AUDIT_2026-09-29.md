# Independent audit — 2026-09-29

**Record:** `2026/09/18/ordered-product-spectral-rate-nonconvergence--4cd423fedf50`
**Disposition:** **PASSED**

## Correctness

**PASS** — Along the displayed period-four orbit the fiber Jacobians telescope exactly to Q^{n+L}D^LQ^{-n}. Orthogonal endpoint factors leave singular values e^{aL},e^{bL}, giving a simple top Lyapunov exponent a. For even L the spectral radius is e^{aL}; for odd L the dominant 2x2 block has characteristic polynomial z^2+e^{(a+b)L}, giving spectral rate (a+b)/2. The residue-class transversality argument and the moving-frame non-invariance diagnosis are algebraically sound.

## Originality

**PASS** — General failures or conditional convergence of normalized spectral-radius growth are prior mathematics and are explicitly excluded from the record’s novelty claim. The source-specific contribution—a smooth deterministic period-four Jacobian counterexample to the unrestricted convergence assertion in arXiv:2609.18017, together with the endpoint-pairing criterion and frame-dependence explanation—was not found in current searches.

## Scientific value

**PASS** — The counterexample directly corrects the theoretical interpretation of a newly proposed diagnostic without disputing its reported finite-data measurements. It also identifies the exact missing hypothesis on periodic residue classes and clarifies why singular-value growth, unlike endpoint spectral radius, is an intrinsic asymptotic quantity.

## Independent checks

- Differentiated the polynomial map at the period-four orbit and verified the off-diagonal derivative terms vanish at v=0.
- Multiplied the Jacobian fiber blocks symbolically and recovered Q^{n+L}D^LQ^{-n}; independently evaluated a=2,b=1 for L=1,...,12, obtaining alternating rates 3/2 and 2 while the top singular-value rate stays 2.
- Checked that the co-rotating frame R_n=Q^n converts all fiber steps to D, confirming finite-horizon spectral radius is not invariant under unequal endpoint frames.

## Findings

- The counterexample is a genuine smooth polynomial dynamical system, not an arbitrary matrix sequence.
- A simple top Lyapunov exponent does not prevent persistent parity oscillation of the finite-product spectral-radius rate.
- The record correctly limits novelty: Aoun--Sert and Martinez Ramos already establish broader spectral-radius asymptotic theory under different hypotheses.

## Literature evidence

- https://arxiv.org/abs/2609.18017 — Sornette, Saiprasad and Troude, A New Route to Chaos through the Geometric Composition of Non-Normal Amplification; current arXiv source introducing h_L and the ordered-product diagnostic.
- https://arxiv.org/abs/2507.19624 — Martinez Ramos, Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles; proves convergence under additional strong hypotheses.
- https://arxiv.org/abs/1908.07469 — Aoun and Sert, Law of large numbers for the spectral radius of random matrix products; prior general spectral-radius asymptotics excluded from the record’s novelty claim.

## Limitations

- The result corrects a general convergence interpretation; it does not recompute or invalidate the source paper’s finite-L Hénon or Ikeda measurements.
- The periodic transversality condition is sufficient residue-class by residue-class, not asserted as a complete aperiodic characterization.
- The novelty claim is source-specific rather than a claim that spectral-radius nonconvergence is new.

## Publication consequence

The audited claim may remain at its source path. This audit does not modify the research statement; it adds only the independent-audit evidence and updates the independent-audit verification channel.
