# Independent mathematical audit

## correctness

PASS

For 0<μ<1 write a=1−μ. Linearized one-edge SIS matrices M12=aI+λA12 and M23=aI+λA23 yield P=M23 M12 on three nodes; independently expanded determinant det(P−I)=[(a−1)^2(a+1)−aλ²][(a−1)(a+1)^2−aλ²]. The second factor is strictly negative for a∈(0,1), λ≥0; the nonnegative irreducible P increases in λ and crosses Perron radius 1 exactly once at λ_temp²=μ²(2−μ)/(1−μ). The averaged adjacency matrix (A12+A23)/2 has radius 1/√2, giving λ_agg=μ√2 and λ_temp/λ_agg=sqrt((2−μ)/(2(1−μ)))>1. Two vertices cannot host distinct single-edge snapshots; every two distinct edges on three vertices share an endpoint and define this unique pattern. The threshold is formal when >1 (transmission probability cannot exceed one), and no exact finite-population stochastic extinction claim is made. Independent algebra checks determinant and ratio.

## originality

PASS

Valdano et al. (2015) already give the arbitrary temporal infection-propagator matrix product criterion, and Speidel et al. (2016) discuss aggregate bias and a discrete-time inequality for random-with-replacement snapshots, not this fixed alternating period. Generic criterion is prior but does not state the exact minimal n=3 deterministic two-step factorized threshold or its quantitative ratio. No indexed exact worked example was located in Resultary and query-level literature searches; a lecture-note prior evaluation remains a possibility. Best-of-knowledge PASS.

## value

PASS

The precisely minimal temporal topology is a natural baseline for separating discretization/temporal ordering from network-size complexity. A closed-form exact ratio makes a reproducible analytic calibration of static aggregation and shows when the formal threshold leaves the physical probability interval. Although its calculation is short once the model is specified, an explicit sharp minimal-case diagnostic with natural physical interpretation and not known from the source is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
