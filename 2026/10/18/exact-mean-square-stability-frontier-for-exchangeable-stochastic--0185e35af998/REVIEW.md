# Independent mathematical audit

## correctness

PASS

Itô's formula yields the exact positive-semidefinite preserving covariance lift K'=AK+KA^T+2r²diag_i(DK_ii+HΣ_{j≠i}K_jj), with r=α/L, L=β+(s-1)c, δ=D+(s-1)H. Starting at K=I by permutation equivariance gives u' and v' exactly from 2r[[-β+rδ,-c(s-1)],[-c,-(β+(s-2)c)]]. Dominating xx^T≤||x||²I and using trace Φ_t(I)=Σ E||X(t;e_i)||² proves the u exponent controls every deterministic initial vector. The larger eigenvalue is r[-β-B+rδ+sqrt((B-β+rδ)^2+4c²(s-1))]. Its determinant sign reduces precisely to ((β-c)L²-αδB)/L. c=0 decouples consistently. Independently checked the moment-lift algebra and the two-species witness (s=2,α=1,β=2,c=1,D=0,H=4): symmetric rates (-8±2sqrt(13))/9<0 and antisymmetric rate -20/9; the printed source threshold would exclude it. This is linear Itô mean-square stability only.

## originality

PASS

The exact second-moment frontier corrects the stronger claimed if-and-only-if inequality for the same system as transcribed in the source package. Published general multiplicative-noise mean-square theory permits moment lifts but the searched nearby published SCOPE finding concerns a different predator–prey drift/noise geometry. Because the complete original Zheng article could not be accessed, its Eq. (10)–(12) textual comparison is provisional and there is explicit priority and source-fidelity risk.

## value

PASS

The precise noise-induced mean-square stability frontier of a symmetric s-species linearization is a natural invariant; the derived covariance correction changes the published necessary/sufficient prediction at admissible integer species count, with an explicit two-species witness and exact decay/growth exponent. This is more than a parameter rename or tiny numeric correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
