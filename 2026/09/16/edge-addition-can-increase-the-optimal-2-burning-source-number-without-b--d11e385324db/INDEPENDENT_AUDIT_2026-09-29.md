# Independent audit — 2026-09-29

Record: `2026/09/16/edge-addition-can-increase-the-optimal-2-burning-source-number-without-b--d11e385324db`  
Audited source tree: `00cdd6765ee7f9d1764c8285585a81471bdc251a`  
Disposition: **passed**

## Correctness

The arm construction proves the claimed unbounded gap. In H, sources a and c finish in round L+2, while any putative schedule finishing by L+1 leaves at least one of the m=L+2 arms unseeded; the prefix-growth argument forces that arm's endpoint to wait until round L+2. Thus b_2(H)=L+2 and t_2(H)=2. In G, the four shortcut arms activate rapidly and the displayed schedule finishes by L+1; every optimal schedule therefore finishes before the unseeded-arm lower-bound time and must place a source in each of the k=q+2 unchanged arms, giving t_2(G)>=q+2. An independent exhaustive simulation also reproduces the seven-vertex control pair (b_2,t_2)=(4,2) for H and (3,3) after one edge is added.

## Originality

Jacobs–Messinger–Trenk, Ars Combinatoria 161 (2024), Lemma 2.4 explicitly claims both b_2(G)<=b_2(H) and t_2(G)<=t_2(H) for a spanning supergraph G. Its proof transfers a schedule but does not account for the changed optimal completion deadline. The audited family exposes exactly that gap and makes the t_2 failure unbounded. A focused search found no published correction or equivalent counterexample before this record.

## Scientific value

The result corrects a published monotonicity statement and separates fixed-deadline source monotonicity from the secondary optimum t_2 evaluated at each graph's own minimum completion time. The unbounded family is stronger than a single counterexample and clarifies the optimization mechanism.

## Limitations

- The family proves only b_2(G)<=q+5 and t_2(G)>=q+2; it does not determine the exact pair for every q.
- The originality search was focused rather than exhaustive, although the directly contradicted published lemma is clear.
- No other theorem of the cited 2-burning paper is rejected solely because it uses Lemma 2.4.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/16/edge-addition-can-increase-the-optimal-2-burning-source-number-without-b--d11e385324db
- https://arxiv.org/abs/2411.02050v2
- https://doi.org/10.61091/ars161-16
