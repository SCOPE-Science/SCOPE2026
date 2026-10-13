# Logarithmic revisit allocation for rare-species occupancy with calibrated false positives

## Finding

**Theorem (rare-occupancy revisit law, including a singular no-false-positive boundary).** Fix calibrated detection probabilities \(0<f<p<1\). At independently occupied or empty sites, let occupancy have probability \(\psi\in(0,1)\). Conditional on a site's occupancy, each of its \(k\ge1\) visits independently returns a positive detection with probability \(p\) (occupied) or \(f\) (empty). Suppose each visit costs one unit, and consider the asymptotic local-Fisher-information efficiency of a uniform \(k\)-visits-per-site design for estimating the unknown occupancy probability \(\psi\), with \(p,f\) **known externally**.

Write \(I_k(\psi)\) for the Fisher information about \(\psi\) contributed by the \(k\) observations at a single site, and \(J_k(\psi)=I_k(\psi)/k\) for information per visit. Every \(\psi\in(0,1)\) admits a maximizing positive integer \(k_\psi\). Set
\[
 d=p\log\frac{p}{f}+(1-p)\log\frac{1-p}{1-f}>0.
\]
Then **every** selection of maximizing integers satisfies
\[
 \lim_{\psi\downarrow0}\frac{k_\psi}{\log(1/\psi)}=\frac{1}{d},
 \qquad
 \lim_{\psi\downarrow0}\psi\log(1/\psi)\max_{k\ge1}J_k(\psi)=d.
\]
For contrast, if \(f=0\) and \(0<p<1\), the optimal integer is uniquely \(k_\psi=1\) whenever
\[
 0<\psi<\frac{p}{2-2p+p^2},
\]
and \(\lim_{\psi\downarrow0}\psi\max_{k\ge1}J_k(\psi)=p\). Thus fixed, arbitrarily small **positive** false-positive probability changes the rare-occupancy optimum from one visit to a logarithmically diverging number of repeat visits.

## Assumptions and scope

Sites have independent occupancy indicators \(Z\sim\operatorname{Bernoulli}(\psi)\) and fixed occupancy status during visits. Given \(Z=1\), observations are iid \(\operatorname{Bernoulli}(p)\); given \(Z=0\), they are iid \(\operatorname{Bernoulli}(f)\). Both detection probabilities are exactly calibrated and treated as known, not as estimated nuisance parameters. All sites use the same positive integer \(k\), each visit has the same cost, and no site-entry/setup cost applies. The criterion is Fisher information per expected visit, as in a large survey budget \(B\) with \(B/k\) independent sites. The rare-occupancy limit is taken in this *per-visit efficiency objective*: any implementation with a literal finite \(B\) must also allow \(B\) to grow so that \(B/k\) remains large. The theorem does not assert optimality for a finite number of sites, joint estimation of detection parameters, or minimizing nonasymptotic mean-squared error.

For a binary visit-history \(y\in\{0,1\}^k\), let \(P_k(y)\) and \(Q_k(y)\) be its probabilities at occupied and empty sites, respectively. The site-history likelihood is
\[
 m_{k,\psi}(y)=\psi P_k(y)+(1-\psi)Q_k(y),\qquad
 I_k(\psi)=\sum_{y\in\{0,1\}^k}
 \frac{(P_k(y)-Q_k(y))^2}{m_{k,\psi}(y)}.
\]
These formulas also apply at \(f=0\) by dropping zero-probability histories in the usual way.

## Proof

**1. An exact missing-information identity.** Assume \(0<f<p<1\). Since all histories have \(Q_k(y)>0\), define the likelihood ratio \(L_k(y)=P_k(y)/Q_k(y)\). Set
\[
 R_k(\psi)=\mathbb E_{P_k}\left[\frac{1}{1-\psi+\psi L_k}\right].
\]
The complete-data occupancy score is \((Z-\psi)/[\psi(1-\psi)]\), with Fisher information \(1/[\psi(1-\psi)]\). Conditional on the observations, the posterior occupancy probability is \(\psi L_k/(1-\psi+\psi L_k)\). The conditional-variance identity, or direct substitution in the displayed finite sum, yields
\[
 I_k(\psi)=\frac{1-R_k(\psi)}{\psi(1-\psi)}.
\]
In particular, \(0<I_k(\psi)\le1/[\psi(1-\psi)]\). The upper bound implies \(J_k(\psi)\to0\) as \(k\to\infty\) for each fixed \(\psi\), whereas \(J_1(\psi)>0\). Hence at least one finite positive maximizing integer exists.

**2. Achievability just beyond the logarithmic threshold.** Put \(T=\log(1/\psi)\) and fix \(\eta>0\). Take \(k=\lceil(1+\eta)T/d\rceil\). Under \(P_k\), \(\log L_k\) is the sum of \(k\) independent bounded log-likelihood increments, each of expectation \(d\). The strong or weak law of large numbers for triangular sequences (here \(k\to\infty\)) gives \(\log L_k/k\to d\) in probability. Consequently \(\log(\psi L_k)/T\to\eta\), so \(\psi L_k\to\infty\) in probability. The integrand defining \(R_k\) is between zero and \(1/(1-\psi)\), a uniformly bounded envelope for \(\psi\le1/2\); it converges to zero in probability. Thus \(R_k(\psi)\to0\), and
\[
 J_k(\psi)=\frac{(1-o(1))d}{(1+\eta)\psi T}.
\]
In particular, the maximum efficiency is asymptotically at least \(d/(\psi T)\) after letting \(\eta\downarrow0\).

**3. Uniform exclusion of allocations below the threshold.** Fix \(\varepsilon\in(0,1)\), and \(0<\theta<1\). Under \(P_k\), let
\[
 M_\theta=\mathbb E_{P_1}\left[\left(\frac{P_1}{Q_1}\right)^\theta\right]
 =p^{1+\theta}f^{-\theta}+(1-p)^{1+\theta}(1-f)^{-\theta}.
\]
The finite-alphabet expression satisfies \(\log M_\theta=\theta d+O(\theta^2)\) as \(\theta\downarrow0\). Choose \(\theta>0\) so small that \((1-\varepsilon)\log M_\theta/d<\theta\). From the exact identity in Step 1,
\[
 1-R_k(\psi)=\mathbb E_{P_k}
 \left[\frac{\psi(L_k-1)}{1-\psi+\psi L_k}\right]
 \le \mathbb E_{P_k}\min\left\{1,\frac{\psi L_k}{1-\psi}\right\}
 \le\left(\frac{\psi}{1-\psi}\right)^\theta M_\theta^k.
\]
Here the integrand can be negative if \(L_k<1\); dropping its negative part is legitimate, and \(\min\{1,u\}\le u^\theta\) for \(u\ge0\). There is a constant \(c>0\) such that **uniformly** over all integers \(1\le k\le(1-\varepsilon)T/d\), the last bound is \(O(e^{-cT})\). Since \(k\ge1\), this implies \(J_k(\psi)=o(1/(\psi T))\) uniformly throughout the low-revisit range.

**4. Uniform exclusion of allocations above the threshold.** For any integer \(k\ge(1+\varepsilon)T/d\), the universal bound in Step 1 gives
\[
 J_k(\psi)\le\frac{d}{(1+\varepsilon)\psi(1-\psi)T}.
\]
Compare this strict asymptotic loss and the low-revisit loss in Step 3 against the achievable lower bound from Step 2 with \(0<\eta<\varepsilon\). Thus for sufficiently small \(\psi\), every maximizing integer lies between \((1-\varepsilon)T/d\) and \((1+\varepsilon)T/d\). Since \(\varepsilon\) is arbitrary, \(k_\psi/T\to1/d\). The universal bound with \(\varepsilon\downarrow0\) and Step 2 with \(\eta\downarrow0\) then squeeze the normalized maximal information to \(d\).

**5. The zero-false-positive boundary.** For \(f=0\), a positive observation cannot occur at an empty site. The sufficient event is whether at least one visit detects the species. At an occupied site its probability is \(a_k=1-(1-p)^k\); thus this event is Bernoulli with parameter \(\psi a_k\), and its Fisher information is exactly
\[
 I_k(\psi)=\frac{a_k}{\psi(1-\psi a_k)}.
\]
The sequence \(a_k\) is strictly concave with \(a_k/k\le a_2/2=p(1-p/2)\) for every integer \(k\ge2\). Therefore for such \(k\),
\[
 J_k(\psi)\le\frac{p(1-p/2)}{\psi(1-\psi)},
 \qquad J_1(\psi)=\frac{p}{\psi(1-\psi p)}.
\]
The latter exceeds the former precisely if \(\psi<p/(2-2p+p^2)\), proving the stated unique optimizer and its limit.

## Verification

The accompanying standard-library Python script `verify.py` reconstructs the finite-binomial-mixture Fisher information by exact rational arithmetic and compares it with the latent missing-information identity for 72 independent parameter combinations. It also checks the \(f=0\) reduction and unique-one-visit inequalities for 84 exact combinations and performs four finite numerical plausibility checks of the logarithmic scale. To run: `python verify.py`. These checks **do not prove the two limits**; the uniform large-deviation-moment argument and LLN proof above establish those infinite-domain conclusions.

## Relationship to prior work

Royle and Link (2006) established the two-binomial false-positive/false-negative occupancy mixture; that model is used, not claimed as novel. MacKenzie and Royle (2005) studied efficient survey allocation when false positives are absent and detection is ordinarily unknown; their classical guidance addresses a different information matrix. Clement (first online 18 July 2016) studied efficient repeat-visit designs with false positives, providing numerical tables for \(\psi\in\{0.2,0.5,0.8\}\) and estimating detection probabilities as unknown nuisance parameters. Those tables do **not** imply this calibrated-detection rare-occupancy asymptotic or its \(f=0\) discontinuity; the distinction in nuisance-parameter assumptions is essential. The contribution here is the rigorous leading logarithmic law with its Bernoulli Kullback–Leibler constant, the leading optimal-information limit, and the contrast at zero false-positive rate. Related general hypothesis-testing information inequalities motivate the proof but do not by themselves supply the stated constrained design optimum.

## Limitations

For every fixed positive \(f\), the limit is \(\psi\downarrow0\) with \(p,f\) held fixed; it makes no uniform assertion as \(f\downarrow0\). Known \(p,f\) is a strong calibration assumption. The design family is restricted to homogeneous fixed numbers of visits per site and equal marginal costs, not adaptive stopping, heterogeneous habitats, site-entry overheads, or simultaneous inference on \(\psi,p,f\). If available visits \(B\) are literally held finite, \(k\le B\) and the diverging-\(k\) conclusion is inapplicable. Asymptotic Fisher efficiency is a local criterion, not a finite-sample risk or a promise of normal approximation in a rare-event regime. Novelty relative to unlocated specialized information-design literature is not independently established.

## References

1. Royle, J. A. and Link, W. A. (2006), “Generalized site occupancy models allowing for false positive and false negative errors,” *Ecology* 87(4), 835–841. https://www.uvm.edu/~tdonovan/Occupancy%20Exercises/Exercise12/Royle_Link_2006.pdf.
2. MacKenzie, D. I. and Royle, J. A. (2005), “Designing occupancy studies: general advice and allocating survey effort,” *Journal of Applied Ecology*. https://doi.org/10.1111/j.1365-2664.2005.01098.x.
3. Clement, M. J. (2016), “Designing occupancy studies when false-positive detections occur,” *Methods in Ecology and Evolution* 7, 1538–1547; first online 18 July 2016. https://doi.org/10.1111/2041-210X.12617.
