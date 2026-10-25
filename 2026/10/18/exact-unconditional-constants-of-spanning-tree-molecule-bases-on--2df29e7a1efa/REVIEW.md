# Independent mathematical audit

## correctness

PASS

The real Lipschitz-free vertex space with the graph shortest-path metric is the weighted ℓ1 edge-flow quotient by the cycle space. Disjoint cactus cycles split this as an ℓ1 direct sum, each cycle quotient being ℓ1(C,w)/span(1_C), plus bridge coordinates. The basis from a spanning tree omits exactly one edge a_C from each cycle. Since an operator norm on such a quotient is the maximum of its values on unit edge generators, signed tree-edge diagonal operators have unit ratios on retained geodesic edges; the omitted-edge image gives min_t[h|t|+Σw_e|ε_e+t|], attained at t=−1,0,1. This equals min(S,h+S−|S_+−S_-|) and maximization over signs gives the exact discrepancy K=max(1,max_C min(S_C,h_C+S_C−Δ_C)/h_C). Weighted geodesicity enforces edge endpoint distances w_e, including all boundary cases. For integer lengths, K_C=S_C/h_C iff Δ_C≤h_C. The reduction from even-total PARTITION maps retained lengths to 2a_i and omitted h=1, preserves simple-cycle geodesicity and uses parity to force Δ∈{0}∪[4,∞), proving NP-completeness for binary encoding. Independent exact dual-section vertex maximization matches the formula on six separately selected weighted/unweighted cycles.

## originality

PASS

Best-of-knowledge priority conclusion, not exhaustive novelty certification. The published closely related theorem computes ||P_S|| (coordinate suppression), while the present statement computes sign multipliers ||D_ε||=||2P_S−I||. Knowledge of the scalar norm ||P_S|| alone does not provide the full sign-multiplier norm; the discrepancy Δ_C and NP-complete threshold require additional analysis. The nearest exact published cactus result shares quotient decomposition and is relevant strong partial coverage, but its 2-point weighted cut min(W,L−W)/h is not identical to maximizing the signed image with three-breakpoint median and does not supply the NP-completeness criterion; therefore it does not imply the complete claimed theorem as stated.

## value

PASS

A spanning-tree molecule basis is a natural coordinate system for finite transportation spaces. The exact weighted-cactus unconditional constant quantifies worst sign perturbations uniformly across arbitrary weighted cycles and bridge attachments, and the PARTITION reduction exposes substantive arithmetic complexity already on a single cycle. It is different from easier coordinate-suppression constants and not an isolated finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
