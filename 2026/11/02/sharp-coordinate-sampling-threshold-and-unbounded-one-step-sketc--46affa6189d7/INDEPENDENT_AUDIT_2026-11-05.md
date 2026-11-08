# Independent mathematical audit

## correctness

PASS

For SPD A=alpha I+E with alpha=(L+mu)/2 and ||E||<=(L-mu)/2, ||SAb||>=alpha||Sb||-||E||, so zero implies (kappa-1)/(kappa+1)>=theta=||Sb||>=sqrt(s/n). Let u=Pb/theta and u±=(b±u)/sqrt(2(1±theta)); H=u+u+^T-u-u-^T sends b to u and u to b with spectrum +/-1,0. A0=I-theta H has condition number (1+theta)/(1-theta) and S A0b=0. Unique maximizing s-row selector is obtained from first s coordinates of amplitude q>1. A_eta=(1+eta)I-theta H has SA_eta b=eta Sb, sketched coefficient 1/eta, true residual sqrt(1-theta^2)/eta; ordinary GMRES optimum theta sqrt(1-theta²)/||A_eta b||. Their ratio ||A_eta b||/(theta eta) diverges as eta->0, while for s fixed, n grows, A_eta approaches identity conditioning. This does not assert DEIM/Q-DEIM s>1 operational equivalence or failure under affine-residual subspace embedding.

## originality

PASS

The primary 2026 deterministic sketching paper optimizes sampling of Krylov basis and then solves sampled-image least squares; its inspected Algorithm 5 and stability discussion do not state the sharp SPD annihilation frontier or this residual divergence formula. General randomized sketch guarantees require embedding the full affine residual space span{b,Ab} and so do not imply performance for this weaker basis-only selector. The result correctly separates s=1 DEIM/Q-DEIM from s>1 global basis-only optimization. Potential implicit oblique-projection literature remains.

## value

PASS

Supplies a sharp necessary-and-attainable operator-image annihilation condition and an important concrete failure mode of a plausible basis-only coordinate row-selection heuristic in sketched Krylov methods, even in well-conditioned SPD systems; identifies exactly which embedding assumption is insufficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
