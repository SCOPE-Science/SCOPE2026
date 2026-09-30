# Independent audit — 2026-09-28

Record: `2026/09/10/046`  
Audited tree: `c4dba6c69b697c54dc8fa7878cea6d23a8102468`  
Disposition: **passed**

## Correctness
I independently replayed the decisive Dhar argument. After subdividing each of the nine `K3,3` edges at its midpoint, the model has `15` vertices, `18` edges, and genus `4`. Put chips at `m00,m11,m22` and subtract the test point `a0`. Starting the burn at `a0` eventually burns every vertex; each chip-bearing midpoint burns when two of its neighbors are already burned. Hence `D0-a0` is `a0`-reduced with coefficient `-1` at `a0` and cannot be equivalent to an effective divisor. Since `D0` itself is effective, `r(D0)=0`.

For the metric step, Hladký–Král'–Norine prove equality of graph-divisor rank and the rank on the corresponding metric graph. Applying that theorem to the subdivided model, followed by uniform rescaling of edge lengths by `1/2`, gives the original unit-length `K3,3` with chips at edge midpoints and preserves rank.

## Originality
The literature located in this audit treats divisorial gonality and graph/metric rank generally but does not record this specific matching-midpoint divisor. The exact cell computation therefore appears original within the searched literature, without claiming an exhaustive search.

## Scientific value
The rank-zero witness decisively blocks the proposed rank-one lifting-gap example and supplies a compact certificate future work can reuse.

## Limitations
No statement is made about other degree-3 divisors or about lifting once this divisor fails the rank condition.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/046
- https://arxiv.org/abs/0709.4485
- https://arxiv.org/abs/1810.08665
- https://arxiv.org/abs/2002.07753
