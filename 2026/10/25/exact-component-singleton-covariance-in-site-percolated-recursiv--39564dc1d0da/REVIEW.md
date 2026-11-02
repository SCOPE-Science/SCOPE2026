# Independent mathematical audit

## correctness

PASS

Conditional on retained vertex count M, component count K, singleton count I, the four cases for a newly attached and independently retained vertex have probabilities q, p(1-M/n), pI/n, p(M-I)/n. This yields i_(n+1)=(1-p/n)i_n+pq and i_n=a*n+b*h_n; the forest identity E[K]=np-(n-1)p^2 and Bernoulli score Cov(M,I)=pq*d(E I)/dp supply the missing cross terms. Expansion of Delta K Delta I=Delta K gives the displayed linear covariance recurrence. Multiplying by 1/h_n and summing yields C_n=c*n-2p^2q+h_n*[pq(1+2p)-c+p^2q((b-bprime)s_n+b/2(s_n^2-t_n))]. Gamma/harmonic estimates imply the O_p(n^-p log^2 n) correction and positivity of c follows from (1-p)+p^2(3+5p+2p^2)>0. Independent enumeration exactly summed all recursive-tree parent choices and retention subsets through n=6 at p=1/4,1/2,3/4 (18 cases), matching the rational formula; this is a check, not a proof for general n.

## originality

PASS

Gu–Yuan arxiv:2408.12515 studies precisely independent site percolation of uniform random recursive trees and provides the cluster-size Markov transition generator, so the underlying process is known and the mixed covariance is computable in principle from prior dynamics. Its actual 24-page paper, including Eq (1.5), Theorems 1–2 and proof sections, does not state the compact exact cross covariance or positive coefficient c. Kalay–Ben-Naim treats fixed-number fragmentation and Janson fluctuations of total component counts, neither explicit singleton–total cross moment. An unindexed earlier extraction from the known generator remains a priority risk; no assertion of an entirely novel Markov model.

## value

PASS

The number of retained connected components and the count of singleton components are natural, distinct measures of fragmentation. Their exact covariance for every n and p, with a nontrivial strictly positive linear asymptotic coefficient and explicit finite-size harmonic correction, quantifies clustering beyond known first moments or marginal laws. No arbitrary statistic slice: both observables are canonical and a future researcher can use this mixed moment directly. Does not establish joint CLT or finite-n sign for every size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
