# Independent mathematical audit

## correctness

PASS

PASS is for the replacement files, not the original. The original fails twice: after multiplying by delta the omitted O(x) remainder contributes O(delta*x), which is not a uniform O(delta^2*y); and dropping the zeta shift before raising to 1/delta does not preserve relative equivalence under delta*X→infinity. In the repair the monotone defining series has one solution and bounds it uniformly away from any x>=epsilon for large X. DLMF's convergent series with the pole terms removed has uniform R=-zeta(-delta)*x+O(x^2) (functional equation plus Stirling for the tail). With B=-zeta(1-delta)>0 and z=(Gamma(delta)/(X+B))^(1/delta), log(x/z)=-log(1-R/(X+B))/delta=O(x/(1+delta*X)); convergence of the ratio to one allows x to be replaced by z. Gamma(delta) and B both equal delta^(-1)-gamma_E+O(delta), so the leading elementary formula contributes an extra O(delta) in relative error. The relative power-law ratio has log -log(1+B/X)/delta+o(1); bounding this term above and below proves the iff condition delta^2*X→infinity and the limits exp(-1/c) and zero on the two smaller scales. Along delta=exp(-2X), the original pure O(delta) relative error is disproved by a correction asymptotic to exp(-X)/2; along (delta,X)=(j^(-2),j^3), the original relative endpoint ratio tends to zero. These are analytic checks, not simulation. The corrected scope remains the reduced periodic saddle, with no bound on the omitted finite-temperature term or on the force.

## originality

PASS

For the replacement, credit the original model, saddle equation, gamma and zeta terms of the forward expansion, and both fixed-dimension endpoints to Jakubczyk–Napiórkowski–Sęk, and the full polylogarithm expansion to DLMF. The supported distinct result is the joint relative inverse estimate and its sharp separation between a logarithmic crossover on the delta*X scale and relative recovery of the power law on the delta^2*X scale. Neither the anchor's separate limits nor the distinct indexed sources inspected state this comparison. The verdict is best-of-knowledge and does not claim an exhaustive priority result.

## value

PASS

A uniform saddle approximation is useful precisely because the known endpoint expressions can be wrong by an arbitrarily large relative factor near the critical dimension. The corrected result identifies distinct logarithmic and relative scales and quantifies the latter boundary by exp(-1/c), including why one cannot retain the originally claimed error. It is not a claim of novelty for a Gamma/zeta expansion, nor a purported formula for the full finite-temperature force.

The dated certificate retains the supplied scientific assessment, sources and limitations.
