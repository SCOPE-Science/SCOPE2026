# Independent mathematical audit

## correctness

PASS

For p±=(1±x)/2, the two-copy diagonal input distributions have trace distance x, whereas the normalized-square target outputs differ by 2x/(1+x²). Any single CPTP map has output separation <=x. Triangle inequality with uniform error δ forces δ>=x(1-x²)/(2(1+x²)). Its derivative has sign 1-4x²-x⁴; maximize at x²=sqrt5-2, giving δ*=(sqrt5-1)/4 sqrt(sqrt5-2). The channel discarding one of two input copies returns rho_p with error |p-f(p)| exactly the same bound. Hence minimax equality for ALL deterministic CPTP maps, not just diagonal channels. Independently verified exact symbolic identities and constant.

## originality

PASS

Raghoonanan–Byrnes study two-copy SWAP branches and signed access to rho², not a uniform minimax approximation of the normalized square by arbitrary deterministic physical channels. Huggins et al. provide virtual distillation for observable estimation, and earlier public reviews distinguish physical unconditional mixtures from signed estimators. The assessed exact worst-case trace-distance constant and optimal discard channel do not follow as stated from these qualitative virtual-distillation claims.

## value

PASS

A sharp operational impossibility radius specifies precisely how close ANY deterministic two-copy-to-one process can uniformly approach normalized power purification, with an elementary attainable optimal channel. It quantifies the physical-state vs signed-estimator distinction rather than just restating nonlinear impossibility. Meaningful even for commuting inputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
