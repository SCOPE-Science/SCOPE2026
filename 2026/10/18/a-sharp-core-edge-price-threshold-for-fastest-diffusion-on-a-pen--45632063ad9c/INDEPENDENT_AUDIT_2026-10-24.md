# Independent mathematical audit

## correctness

PASS

For a K_{m+1} core plus one leaf, all edge weights independently variable subject to m spokes+leaf price 1 and inner edges price t, the submitted PSD certificate Y=alpha P_U+uu^T/(m+2)^2 has squared edge lengths 1,1,2alpha<=t. If L>=Pi (lambda2>=1) it implies budget>=trY. In mixed regime choose q=sqrt(1-t(m-1)/(2m)), alpha=t/2, x0=(2+1/q)/(m+2), y0=(m-1/q)/(m(m+2)), z0=(m+1+mq)/(m+2), attaining eigenvalues 0,1 mult m, and (m+2)x0z0>1 with cost C=m+1-(mq-1)^2/(m+2). At t>=2(m+1)/m the unit star attains cost m+1. Equality forces any rival Laplacian difference to be supported on one top eigendirection; absence of leaf-core nonedges forces difference zero, even at threshold. Independent symmetric Laplacian spectra and expenditure checks at m=2,4,7 and both price regimes agreed. Full proof is dual/equality, not sampled graphs.

## originality

PASS

General fastest-mixing SDP and its dual exist (Sun–Boyd–Xiao–Diaconis 2006), and group symmetry reduction exists (Boyd et al 2007); latter optimizes discrete-time SLEM. The natural single-leaf priced clique has an explicit cost-induced edge-deletion frontier and global uniqueness not stated in these inspected theorems. Fiedler tree limit accounts for high-price star support only. Possible prior specialist formula remains risk.

## value

PASS

Optimization on a clique with a single pendant bottleneck and priced redundant edges is a natural graph-design problem. The full size-dependent sharp price threshold, explicit nontrivial mixed allocation and unique optimizer at transition give reusable exact data beyond generic SDP solvability or a routine tree bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
