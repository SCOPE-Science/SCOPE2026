# Independent audit — 2026/09/12/062
Assigned/current tree: `745e2ea12d695d51901579f9fe85fb0769b41e67`  
Disposition: **repaired**

## Correctness

Ringel’s genus formula gives genus 4. Euler then gives 17 faces and total face-boundary length 72. In a simple bipartite rotation-system embedding every face has even length at least 4, so the total excess over 4 is 72-4·17=4. The only possibilities are two 6-faces or one 8-face. Independent face tracing of the two explicit rotation systems printed in the record gives exactly {4^15,6^2} and {4^16,8}; hence both possibilities occur and the classification is complete.

## Originality

The Euler-excess exclusion is elementary and the known minimum-genus literature is extensive. Grannell–Knor enumerate K_{m,n} only through m,n<=7, so it does not cover K(4,9); Sun’s face-distribution theorem concerns complete graphs, not complete bipartite graphs. Focused search did not locate this exact K(4,9) two-multiset statement, but no priority claim is made.

## Scientific value

The result completely settles a concrete small face-distribution case and supplies explicit witnesses, but the structural content is limited because Euler excess leaves only two candidates.

## Independent checks

- Independent successor-rule tracer recovered 17 faces and length multiset 4^15,6,6 for witness A.
- The same tracer recovered 17 faces and length multiset 4^16,8 for witness B.
- Euler excess proves no third multiset is possible.

## Limitations

- The referenced output/artifacts/verify.py and witnesses.json are absent from the audited Git tree.
- The audit therefore used the rotation tables printed in RESULT.md and a separately written face tracer.
- The classification is only for orientable cellular minimum-genus embeddings.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/12/062
- https://grannell.net/Papers/kmn.pdf
- https://arxiv.org/abs/1708.02092
