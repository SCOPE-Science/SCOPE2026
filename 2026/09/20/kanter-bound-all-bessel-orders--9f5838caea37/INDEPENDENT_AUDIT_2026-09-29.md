# Independent audit — A Kanter-type lower bound for the generalized Bessel sum at every real order

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/20/kanter-bound-all-bessel-orders--9f5838caea37`  
**Assigned and audited tree:** `b358da6fc7478f62c095dfb05746d1497843cd55`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review without a substantive research-file edit.

## Correctness

PASS. The Baricz–Pogány integral representation and opposite-angle pairing reduce the claimed gamma inequality to positivity of a one-dimensional weighted difference G_r. Logarithmic differentiation gives the asserted unique sign change because c tanh(2rc)-2r(1-c^2) is strictly increasing from negative to positive. The boundary functional is finite and the matched-cutoff evaluation F(r)=psi(r+1/2)-log r+Ei(-4r) differentiates to a Laplace transform whose kernel has exactly one sign change; together with F(0+)=F(infinity)=0 and F'(0+)=pi^2/2-4>0 this forces F(r)>0. Weighting by the decreasing factor (1-c^2)^{nu+1/2} then gives strict positivity for nu>-1/2, and the r=0 and half-order boundary equalities and the asymptotic constant check correctly.

## Originality

PASS, to the best of the audited literature boundary. Baricz–Pogány explicitly advertise an open problem concerning a generalization of the modified-Bessel sum inequality, while the 2026 Veestraeten paper rewrites the same generalized expression in confluent-hypergeometric form but does not state the gamma lower bound audited here. Searches using the exact gamma quotient, the 1F1 equivalent, Kanter terminology, and the generalized Bessel sum found no earlier full-real-order statement. Differently phrased special-function inequalities remain a residual risk, but no covering theorem was located.

## Scientific value

PASS. The theorem gives a closed-form asymptotically sharp lower bound over the entire natural real-order range nu>=-1/2, exactly recovers the classical nu=0 Kanter inequality, and supplies an equivalent hypergeometric inequality. The one-sign-change transfer from a boundary functional is also a reusable analytic mechanism rather than an isolated numerical bound.

## Independent checks

- Recomputed the derivative-sign function in the one-sign-change lemma and the endpoint sign pattern of G_r.
- Checked the boundary functional derivative kernel and the r=0 and nu=-1/2 equality cases; numerical spot checks across separated positive r and nu agreed with the exact proof.
- Compared current literature records for Baricz–Pogány and Veestraeten against the exact gamma/1F1 statement and found no covering result.
- Checked that the current main-path tree is unchanged from the assignment snapshot.

## Literature and evidence

- https://arxiv.org/abs/1301.5429 — Baricz and Pogány, open-access preprint of the 2014 paper; its abstract explicitly notes an open problem at the end.
- https://doi.org/10.1007/s00440-006-0043-0 — Mattner and Roos (2007), classical nu=0 Kanter concentration bound context.
- https://doi.org/10.1007/s00009-026-03050-1 — Veestraeten (2026), recent treatment of the generalized expression and its confluent-hypergeometric representation.

## Limitations

- The lower bound is asymptotically sharp, but finite-r pointwise optimality is not proved.
- No probabilistic concentration theorem is claimed for arbitrary real order nu.
- Search cannot exclude a substantially differently phrased or poorly indexed prior special-function inequality.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `b358da6fc7478f62c095dfb05746d1497843cd55`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
