# Independent audit — 2026-09-30

Record: `2026/09/19/sdpi-relay-capacity-counterexample-template--75866f4b972e`  
Assigned and audited source tree: `4f70d6d9552b81372ed77e6a5b36a2d43b3a23f5`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `debff59e99f441578657499c33d9c7c73db70297`  
Disposition: **passed**

## Correctness

**independently_supported**. The product-relay template is correct. The noiseless B component contributes D bits/use independently, while a second message can be decoded through W1 and block-Markov forwarded through W2, achieving D+min(C1,C2). The two standard cutset cuts give D+C1 and D+C2, so this is exact capacity. Decode-forward in the proposed characterization is at most C1. Under Shiu's relaxed compress-forward feasible set, conditioning on each (B,X_r) leaves the Markov chain A→Y_r→Yhat_r through the same W1, so the defined post-processing SDPI gives I(A;Yhat_r|B,X_r)<=eta I(Y_r;Yhat_r|B,X_r). Combining this with the relaxed rate constraint yields R_CF<=H(B|X_r)+eta I(X_r;B,Z)<=D+eta C2. Hence the max of the three proposed terms is bounded by max(C1,D+eta C2). The BSC specialization uses the standard binary symmetric contraction coefficient (1-2p)^2; the resulting open region and gap 4p(1-p)[1-h2(q)] follow algebraically.

## Originality

**qualified_abstraction_of_recent_counterexample**. Ponniah's September 2026 preprint proposes the three-scheme characterization, and Shiu's counterexample already uses a noiseless source-destination component plus BSC relay links and a BSC strong data-processing inequality at one parameter choice. The audited record abstracts that mechanism to arbitrary product component channels via an input-free post-processing contraction coefficient, derives a simple general sufficient condition, and exposes an open two-parameter BSC counterexample region. Current searches did not locate this general template. Because the abstraction is short and follows immediately after a very recent counterexample, folklore and near-simultaneous priority risk are material.

## Scientific value

**meaningful_generalization_and_failure_mechanism**. The theorem shows that the failure of the proposed relay-capacity formula is robust rather than a single numerical accident: any strict information contraction in the relay observation can create a certified gap once the noiseless component is large enough. It also yields a stronger explicit BSC witness while making clear that it is not a general relay-capacity theorem.

## Literature and evidence checked

- https://arxiv.org/abs/2609.15709
- https://arxiv.org/abs/2609.18727
- https://doi.org/10.1109/TIT.1979.1056088
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/sdpi-relay-capacity-counterexample-template--75866f4b972e

## Limitations

- The theorem concerns the split product relay architecture and the specific proposed DF/C-CF/U-CF characterization, not all relay coding schemes.
- The post-processing contraction upper bound can be loose, so the sufficient counterexample region need not be exhaustive.
- No sharpness of the certified gap is claimed.
- The abstraction follows a very recent counterexample and therefore has high concurrency/folklore risk.
