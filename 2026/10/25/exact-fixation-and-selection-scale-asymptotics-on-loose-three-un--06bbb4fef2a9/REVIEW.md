# Independent mathematical audit

## correctness

PASS

For m≥2 loose hyperedges {hub,leaf2j-1,leaf2j} with whole-edge overwrite (fitness-proportional parent then uniform incident edge) and r>0, synchronized leaf pairs remain synchronized. The sole initially discordant petal for leaf seeding resolves before other type changes with mutant success rate r versus resident-leaf 1 and hub 1/m, giving c=mr/[m(r+1)+1]. On synchronized states (resident hub,k mutant petals) and (mutant hub,k mutant petals), genuine-change conditional probabilities yield u_k=bv_k+(1-b)u_{k-1}, v_k=av_{k+1}+(1-a)u_k, with a=r/(r+2m),b=2mr/(2mr+1). Boundary u_0=0,v_m=1 and geometric increment ratio q=(1-b)/a give H and exact hub/leaf/uniform fixation. Checked neutral r=1 directly and independently simplified exact m=2 suppression polynomial by symbolic rational factorization. Recomputed advantaged r>1 1/m coefficient and deleterious r<1 exponential scale via q=r^-2(1+(r-r^-1)/(2m)+O_r(m^-2)). Pointwise fixed r only; no extrapolation across r→1. All states can reach an absorbing consensus with positive probability, so finite harmonic solution valid.

## originality

PASS

Best-of-knowledge: full published Liu–Masuda primary text materially inspected; despite matching update law their star means all leaf pairs, not loose disjoint petals. The exact all-fitness rational formula and precise two fixed-fitness asymptotics have specific new mathematical content. Baseline neutral i/N already known.

## value

PASS

Loose m-petal hyperstars form a canonical sparse linear 3-uniform hypergraph family and isolate group-overwrite versus ordinary graph replacement. The theorem gives exact hub-vs-leaf seeding, complete fixed-fitness large-size behavior, an explicit deleterious selection ratio and a sharp m=2 all-r suppression result. This is a motivated natural infinite-family classification, not an arbitrary sample of small hypergraphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
