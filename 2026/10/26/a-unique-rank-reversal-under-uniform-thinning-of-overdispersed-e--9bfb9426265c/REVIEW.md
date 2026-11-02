# Independent mathematical audit

## correctness

PASS

The negative-binomial pgf after independent Bernoulli thinning is [1+(p R/k)(1-z)]^{-k}. Standard Galton-Watson fixed-point theory gives zero survival for pR<=1. For positive survival s, the inverse p=Phi_k(s)/R with Phi_k(s)=k[(1-s)^(-1/k)-1]/s is continuous strictly increasing by its initial-interval-average integral formula. Set s=1-exp(-t), t>0; for 0<k1<k2 the ratio H(t)=k1/k2 (exp(t/k1)-1)/(exp(t/k2)-1) rises strictly from 1 to infinity since a/(1-exp(-at)) increases in a>0. Thus with R1>R2 exactly one H=R1/R2 crossing exists beyond p=1/R2 and the strict pre/post rankings follow. Matching p for both inverse maps handles all positive parameters; the physically meaningful thinning domain restricts p to [0,1]. Independent exact-algebraic extinction-root evaluation checks the 4,1/2 vs 3,1 crossing at 5/9 and the reversal at p=1/2 and p=1; finite checks do not replace proof.

## originality

PASS

Best-of-knowledge: the published negative-binomial branching and population-wide mean scaling are acknowledged premises, but the inspected primary research does not assert the complete pairwise single-crossing classification for distinct R and k. The new step is a global monotone ratio of inverse survival curves and a physical p<=1 criterion, not a new epidemic offspring model.

## value

PASS

This solves a natural ranking question for competing heterogeneous epidemic branching mechanisms controlled by a common parameter. It distinguishes a uniform physical thinning reversal from a purely formal p>1 extrapolation and gives a sharp unique crossing law across all positive mean/dispersion pairs, beyond routine single-curve evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
