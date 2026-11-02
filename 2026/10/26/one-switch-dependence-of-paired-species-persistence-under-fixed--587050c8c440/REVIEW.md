# Independent mathematical audit

## correctness

PASS

With a,b neighborhood sizes, h overlap, and q uniformly retained partners out of N, avoidance indicators have probabilities binom(N-a,q)/binom(N,q), binom(N-b,q)/binom(N,q), and joint binom(N-a-b+h,q)/binom(N,q), giving the exact covariance determinant. On nondegenerate q<=N-max(a,b), ratio R_q=binom(d,q)binom(N,q)/(binom(N-a,q)binom(N-b,q)), d=N-a-b+h, has successive ratio (d-q)(N-q)/((N-a-q)(N-b-q)); its difference from one has sign h(N-q)-ab. R is unimodal, followed by zero when q>d; hence strict disjoint negative, nested positive, partial overlap Nh<=ab negative (with q=1 tie on equality), or Nh>ab exactly one positive-to-negative phase transition and at most one zero. Smallest such reversal requires N>=5; N=5,a=b=2,h=1 has cov [1/25,1/100,-1/100,0]. Bernoulli independent survival instead gives strictly positive covariance for h>0. Independent rational binomial code verified 15,344 nondegenerate q cases for all feasible a,b,h through N=15, including boundaries. Infinite classification rests on ratio proof.

## originality

PASS

PASS for the all-parameter single-sign-switch theorem and sharp five-partner example. Joag-Dev–Proschan negative association applies to increasing functions of DISJOINT coordinate sets; overlapping A,B are outside that hypothesis. Memmott et al. simulate aggregate pollinator removal responses, not exact pairwise covariance phase law. Similar reliability/hypergeometric indicator inequalities may yet imply this result.

## value

PASS

Exact shared-neighborhood co-survival dependence is a natural building block for the variance of total surviving species in a fixed-quotas ecological network. The theorem shows that overlap can produce positive dependence at low retained quota but negative dependence at high quota, in contrast to independent partner retention; the sharp one-switch classification is a useful structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
