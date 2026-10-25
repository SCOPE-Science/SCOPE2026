# Independent mathematical audit

## correctness

PASS

For independent Bernoulli p incidences and canonical top concept, conditioning on a fixed t-object subteam gives per-attribute failure probability p^t-p^m and exact mean 2^-m sum_t binom(m,t)(1-p^t+p^m)^N, including t=0,m boundaries. With beta=-log p and r_m=(log N)/beta, the uniform probability of mismatch outside a width m^1/4 band is at most exp(-beta m^1/4)+exp(-exp(beta m^1/4)/2), and the central-binomial band mass is O(m^-1/4). Markov and Borel-Cantelli give actual-context almost-sure threshold approximation under arbitrary cross-size coupling, and boundedness L1. Binomial CLT at r_m=m/2+(b/beta)sqrt m yields Phi(-2b/beta). Choosing fixed binomial-tail cutoffs yields regimes c<beta/2 ->1, c>beta/2 ->0, plus exponential mean decay -D(min(c/beta,1)||1/2), including c>=beta saturation at -log2 from the full-object subteam lower bound. Read direct complete-matrix enumerator to cross-check formula; numerical values are not proof of a.s. limits.

## originality

PASS

Sakurai 2021 studies expected TOTAL concept counts in Bernoulli random contexts, not stability of top concept. Zhi 2014 and Mouakher/Ko 2022 address computation of concept stability for fixed contexts, not sharp Gaussian crossover under exponentially many random attributes. Best-of-knowledge new quenched critical-window and exact large-deviation rate. Related random set-covering threshold analogies may imply part after reduction and 2022 full paper not examined; residual risk recorded.

## value

PASS

Top concept intensional stability is canonical measure of attribute preservation upon random deletion of objects. An exponential attribute scaling naturally causes a phase transition with nontrivial Gaussian critical width, and a coupling-independent almost-sure law and exact unstable-side rate provide a useful rigorous stochastic calibration benchmark; not an arbitrary limit parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
