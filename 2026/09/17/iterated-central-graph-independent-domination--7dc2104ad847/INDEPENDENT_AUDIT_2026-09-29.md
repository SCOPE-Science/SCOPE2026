# Independent audit — 2026-09-29

Record: `2026/09/17/iterated-central-graph-independent-domination--7dc2104ad847`  
Assigned and audited source tree: `f878707c50fc9ac1ab17a59350b6edb2ce520526`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported**. The all-iterate formula follows correctly from the stated second-iterate theorem and the record's independence-number lemma. Independently checking the lemma: if I is independent in C(H), its original-vertex part X must be a clique of H and its subdivision vertices can only come from edges of H-X, so |I|<=|X|+|E(H-X)|; connectedness gives at least |X| edges incident with X for every clique X, while all M subdivision vertices themselves form an independent set, hence alpha(C(H))=M. Substituting a=|V(J)|, b=|E(J)| into the cited second-iterate formula gives M=b+binom(a,2), N=a+b and simplifies exactly to 2M=a(a-1)+2b. The exceptional start G=K2,k=3 is handled correctly through C(K2)=P3. An independent brute-force check on the smallest connected starts also agrees with the k=3 formula.

## Originality

**qualified_current_extension**. Cabrera-Martínez, López-Carmona, Rios-Villamar and Serrano-Díaz posted their central-graph independent-domination paper on 14 September 2026 and publicly describe formulas for central graphs; targeted searches through 29 September did not locate this higher-iterate collapse or the exact identity i(C^k(G))=2|E(C^{k-2}(G))|. The contribution is therefore best described as a short higher-iterate consequence of a very recent second-iterate theorem, with no broad priority claim for the elementary alpha(C(H)) lemma.

## Scientific value

**meaningful_structural_extension**. The result turns a second-iterate formula into an exact closed recurrence for every later central iterate and shows that all k>=3 independent-domination numbers depend only on the starting order and size. That is a clean reusable structural consequence, albeit an elementary one once the recent second-iterate theorem is available.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/iterated-central-graph-independent-domination--7dc2104ad847
- https://arxiv.org/abs/2609.16357

## Limitations

- The proof imports Theorem 2.12 of the very recent arXiv:2609.16357 rather than reproving that theorem.
- The elementary identity alpha(C(H))=|E(H)| may exist elsewhere in central-graph literature; the originality assessment is confined to the higher-iterate independent-domination identity.
- Because the source preprint is only about two weeks old, unindexed concurrent work cannot be excluded.
