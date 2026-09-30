# Independent audit — Exact first integral reveals a two-sided blow-up dichotomy for exponential memory

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/exact-first-integral-memory-blowup-dichotomy--7383b48da300`
**Audited tree:** `e7ca3a0103efa9d865bb398e1388c7f4199f5686`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The first integral and two-sided classification are correct. With w=(1-v)^{-1}, division by u'=w gives the linear equation dw/du-(alpha u-beta)w=beta, so e^{-Phi(u)}w-beta int_0^u e^{-Phi} is constant. For w0>0 the bracket Q stays positive as u increases and gives finite-time u->+infinity, v->1^-; for w0<0 it stays negative as u decreases and gives finite-time u->-infinity, v->1^+; v0=1 is singular initially. Gaussian-tail inversion gives the stated leading constants and subleading logarithmic term. A symbolic differentiation independently gives dH/dt=0.

### Independent checks

- Independently differentiated H=e^{-Phi(u)}w-beta int_0^u e^{-Phi(s)} ds along u'=w, w'=(alpha u-beta)w^2+beta w and obtained dH/dt=0 identically.
- Checked sign-monotonicity of Q(u): Q'=beta e^{-Phi}>0, which prevents branch crossing and makes the positive and negative finite-time Gaussian-tail integrals immediate.
- Verified constant histories for alpha=beta=1: phi=2 gives u0=v0=2 and the negative branch; phi=1 gives v0=1 and an initially undefined right-hand side.
- Re-derived tau~e^{-Phi(u)}/(L_sigma |alpha u-beta|) and inverted it to recover A3=sqrt(2/alpha), A4=1/sqrt(2 alpha) and the submitted first correction.
- Independently read the source full text: Theorem 2 states the universal positive-history claim, while Section 4 explicitly restricts the proof to 0<=v<1 before introducing w and Phi_3.

## Originality

PASS to the best of current searchable knowledge. After ordinary arXiv/OA full-text retrieval attempts failed, all 26 pages of Ichida arXiv:2609.15470v1 were independently read through authorized institutional retrieval. Theorem 2 (paper p.5) quantifies over every positive bounded history, whereas its proof (paper p.12 onward) explicitly says it is focusing on 0<=v(t)<1 and works in Phi_3={u>=0,w>=1}. No public correction or source-specific first-integral/trichotomy sharpening was located through 2026-09-29. Standard integrating-factor and Gaussian-tail methods are excluded from the novelty claim.

### Literature checked

- https://arxiv.org/abs/2609.15470 — Ichida, Memory-induced blow-up solutions and their dynamical transitions in distributed delay differential equations, v1. Full text independently inspected through authorized institutional access after ordinary arXiv/OA retrieval failed.
- https://sites.google.com/view/yuichida/%E8%AB%96%E6%96%87-papers — Author publication page; currently lists the paper as submitted and links the same arXiv preprint; no correction was located.

## Scientific value

The result repairs a material missing hypothesis in a main source theorem: admissible positive bounded histories can start below, on, or above v(0)=1, and these cases have qualitatively different outcomes. It also replaces unspecified positive blow-up amplitudes by universal leading constants and identifies where beta and the initial history enter at lower order.

## Limitations

- The result is only for the F2 single-exponential-memory model, not F1 or F3.
- For v0>1 the mathematical real-valued trajectory eventually becomes negative; a biological nonnegative-state interpretation should terminate at state-space exit rather than claim physical negative blow-up.
- The source is very recent, so an unindexed author revision remains a residual priority risk.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
