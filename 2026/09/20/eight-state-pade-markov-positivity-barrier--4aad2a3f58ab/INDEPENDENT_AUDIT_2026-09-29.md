# Independent audit — Eight-state barrier for Markov positivity of the [2/2] Padé map

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/eight-state-pade-markov-positivity-barrier--4aad2a3f58ab`  
**Assigned and audited tree:** `c88df40589edef0835b9e7c4b22313f443c65c20`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review.

## Correctness

PASS. Independent symbolic reconstruction of r(z)=(12+6z+z^2)/(12-6z+z^2) reproduces the Maclaurin coefficients through the first negative term, including a_6=0 and a_7=-1/1728. For the stated eight-state pure-birth generator, exact matrix functional calculus gives [r(hQ*)]_{1,8}=12 h^7 p(h)/(h^2+6h+12)^7 with p(h)=7h^6+126h^5+840h^4+2520h^3+3024h^2-1728, and [r(hQ*)]_{1,2}=12h(12-h^2)/(h^2+6h+12)^2. The unique positive root of p is 0.5966405618671684..., and the n<=7 shortest-path argument is sound: in the only delicate length-six case, every nonzero Q^7 contribution has six positive off-diagonal factors and one negative diagonal factor, while a seven-off-diagonal walk would contain a removable directed cycle contradicting shortest length six.

## Originality

PASS on a narrow, literature-bounded boundary. Zappavigna–Colaneri–Kirkland–Shorten (2012) already use the same first negative Padé coefficient with an 8x8 nilpotent shift and then a Hurwitz Metzler shift, but those matrices are not conservative CTMC generators. Lóczi–Ketcheson and classical absolute-monotonicity theory give radius-zero obstructions in the unrestricted monotonicity setting, not a minimal conservative state-space threshold. The recent Itkin–Kazbek preprint concerns rational maps for Fokker–Planck generators and its accessible abstract does not state this eight-state small-step threshold or the exact stochasticity window. No earlier SCOPE record with the same conservative threshold/window was located.

## Scientific value

PASS. The record sharpens a known nonconservative positivity obstruction into a genuine finite-state Markov result, proves the smallest state-space dimension for arbitrarily-small loss of positivity, and determines the full stochasticity interval for an explicit sharp witness. The non-monotone phenomenon that decreasing h below h0 destroys stochasticity is a concrete and useful warning for conservative time discretization.

## Independent checks

- Expanded the Padé map independently and verified a_6=0 and a_7=-1/1728.
- Constructed the 8x8 pure-birth generator symbolically and recovered the exact (1,8) and (1,2) entries and h0=0.5966405618671684....
- Checked the current main-path tree SHA against the assignment snapshot; it is unchanged.

## Literature and evidence

- https://doi.org/10.1016/j.laa.2011.12.021 — Zappavigna, Colaneri, Kirkland and Shorten (2012): prior nonconservative 8x8 Padé positivity obstruction and Hurwitz Metzler shift.
- https://doi.org/10.1112/S1461157013000326 — Lóczi and Ketcheson (2014): absolute-monotonicity radius-zero context for fourth-order two-stage rational schemes.
- https://arxiv.org/abs/2608.22703 — Itkin and Kazbek (2026): recent rational-map positivity work; accessible abstract does not state the audited finite conservative threshold/window.

## Limitations

- The exact global window is proved only for the displayed pure-birth witness; the n<=7 statement is a per-generator local-in-h result, not a uniform rate-independent CFL bound.
- The audit located and compared the closest known 2012 Padé positivity construction, but exhaustive historical Markov-chain literature coverage cannot be guaranteed.
- A web screenshot endpoint for an accessible prior-art PDF was blocked by URL restrictions; the text layer was available and inspected, and no inaccessible material is represented as read.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `c88df40589edef0835b9e7c4b22313f443c65c20`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
