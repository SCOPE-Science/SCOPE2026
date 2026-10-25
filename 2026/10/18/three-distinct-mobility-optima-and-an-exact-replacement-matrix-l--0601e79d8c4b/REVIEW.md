# Independent mathematical audit

## correctness

PASS

For home-vertex visits q=h/(h+d), neighbor visits p=1/(h+d), classify encounters at focal homes (2qp E[1/(1+Bin(d−1,p))]) and common neighbor sites (p² E[1/(1+Bern(q)+Bin(d−2,p))]). This gives W=sI+aA+b(A²−dI), with a=2h(1−(1−p)^d)/(d(h+d)), b the claimed one-dimensional integral and s=q(1−p)^d+d²p²(1−p)^(d−1). Conditional weights normalize to one in each realized group, so W is symmetric and row-stochastic. The exact derivative s′ has sign(h−1). For triangle-free edges a(x) has unique maximizer x∈(0,1/d), root (1−x)^(d−1)(2−(d+1)x)=1, strictly below 1/(2d); hence h*>d. Bare meeting probability 2h/(h+d)^2 maximizes at d. Lambert asymptotics follow from e^(−y)(2−y)=1. Independently checked s′ symbolic differentiation for all d=2,..,9 and d=2 root; full analytic arguments carry all degrees.

## originality

PASS

Best-of-knowledge PASS for all-regular-graph exact adjacency polynomial and sharp h_temperature=1<h_encounter=d<h_replacement. General territorial-raider replacement group-sum formula and individual temperature definitions are prior art. No inspected source derives the full structural reduction or full degree-dependent peak hierarchy.

## value

PASS

The polynomial W=sI+aA+b(A²−dI) exposes common-neighbor effects invisible to identical per-vertex temperatures, while rigorously separating crowd-normalized replacement from raw meeting and total temperature; 1<d<h* holds for every triangle-free regular degree. This is an exact structural tool for multiplayer interactions rather than an arbitrary parameter optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
