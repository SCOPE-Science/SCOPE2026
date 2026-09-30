# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/psi-divisibility-cyclic-sylow-obstruction-z-groups--80065f617da2`  
Assigned source tree: `e9b6b56d8f5223d49863e22392d61d5b5e741411`  
Audited current source tree: `e9b6b56d8f5223d49863e22392d61d5b5e741411`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `0bc951620fd3988464f50aafd1bd92e65c445d26`  
Disposition: **passed**

## Correctness

**independently_supported**. The cyclic-Sylow obstruction is correct. With t=|P|, A=psi(P), C=C_H(P), h=psi(H), c=psi(C), the standard normal-cyclic-Sylow formula gives psi(G)=th+(A-t)c. Psi-divisibility of H gives h|(A-t)c, while PC=P×C is a subgroup of coprime direct-product type and gives Ac|psi(G), hence Ac|t(h-c). Writing h=dx,c=dy with gcd(x,y)=1 and x>y, the first condition yields x|A-t and the second yields A|t(x-y). For cyclic P of order p^a, A=(p^(2a+1)+1)/(p+1)≡1 mod p, so gcd(A,t)=1 and A|x-y. But 0<x-y<x<=A-t<A, a contradiction. Schur-Zassenhaus then makes every normal cyclic Sylow subgroup central in a psi-divisible group. Standard ZM-group structure excludes every nonnilpotent Z-group, while the known abelian classification gives exactly cyclic square-free groups. Thus the square-free-order corollary follows.

## Originality

**qualified_supported_open_problem_resolution**. Harrington-Jones-Lamarche established the abelian classification. Lazorec's 2020/2021 paper gives the same normal-cyclic-Sylow sum formula but proves only a ZM(p^alpha,n,r) nondivisibility result under an additional arithmetic condition and explicitly asks whether any nonnilpotent group of square-free order can be psi-divisible. Lazorec's 2023 paper still reports only cyclic square-free examples as known. Targeted searches did not locate the two-subgroup divisibility obstruction or the resulting full Z-group classification. The standard semidirect-product formula and Z-group structure are prior art; novelty is supported for the short structural obstruction and its consequences, subject to normal indexing risk.

## Scientific value

**high_within_current_finite_group_problem**. The theorem converts a restricted arithmetic obstruction into a structural one and gives a theoretical negative answer to a published square-free-order open problem, while classifying all psi-divisible Z-groups. It does not settle whether nonabelian psi-divisible groups exist in full.

## Independent checks

- Re-derived both divisibility consequences using the subgroups H and P×C_H(P) without cancelling any non-coprime psi(C) factor.
- Checked gcd(psi(P),|P|)=1 for cyclic p-groups and the resulting strict inequality contradiction.
- Inspected Lazorec's open paper at the stated ZM proposition and square-free-order open problem.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/psi-divisibility-cyclic-sylow-obstruction-z-groups--80065f617da2
- https://arxiv.org/abs/2003.01678
- https://doi.org/10.1007/s40840-020-00987-8
- https://doi.org/10.1155/2014/835125
- https://doi.org/10.55016/ojs/cdm.v18i2.73182
## Limitations

- The theorem does not classify all finite psi-divisible groups or settle the existence of nonabelian examples in full.
- The obstruction requires a normal cyclic Sylow subgroup with nontrivial complement action.
- The standard normal-cyclic-Sylow formula and ZM structure are prior inputs rather than new results.
