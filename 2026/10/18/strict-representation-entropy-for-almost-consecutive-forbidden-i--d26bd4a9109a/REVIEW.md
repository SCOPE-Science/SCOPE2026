# Independent mathematical audit

## correctness

PASS

The greedy mex sequence strictly increases: all smaller positive values were already represented, and the previous mex becomes available as a singleton. For the legal-subset recurrence, if the top index n is selected, the only possible selection among the preceding k positions is n-k+c. With that position selected, any previous compatible index is at most n-2(k-c)<n-k, so no extra restriction from n remains. The admissible k-bit transfer matrix is primitive by paths through the all-zero word and its self-loop; the recurrence then identifies its Perron rate with the stated rho. The positive eventual greedy recurrence similarly gives growth rate lambda via its irreducible companion with a self-loop. At lambda, the count polynomial is -(lambda-1)lambda^c<0, and its factorized level function increases strictly above one. To check the truncation, choose fixed L so that lambda^(1-L)/(lambda-1)<1. Eventually even the sum of all terms through index n-L is below a_n, while no index n or later can occur. Counting each legal subset separately gives bounds d_(n-L) and d_(n-1) before division by a_n. For the second limit, w=k(lambda-1) satisfies w+log w=log k+O(w^2/k), with w tending to infinity and w=O(log k); thus w=W(k)+o(1). Uniformly on [lambda,lambda+2(lambda-1)/k] the derivative of the count polynomial is asymptotic to k. Its negative value at lambda is asymptotic to -(lambda-1); this gives a sign change on the interval and rho-lambda asymptotic to (lambda-1)/k. The example ratio independently evaluates to 1.011434032776249 by root bisection. This establishes exponential comparison, not a limiting prefactor; the eventual greedy recurrence is still a hypothesis outside the cited proved range. The uploaded finite verification was inspected, not executed.

## originality

PASS

The legal-subset recurrence and conditional root-ratio argument are prior. The supported distinct claim is the proven strict exponential growth on the whole stated singleton-exception recurrence range, without further assumptions of spectral dominance, and the explicit fixed-c asymptotic for its entropy excess. The inspected sources did not establish these conclusions.

## value

PASS

This resolves a stated representation-multiplicity question on a natural infinite recurrence regime, distinguishes a strict exponential effect from bounded mean multiplicity, and quantifies how rapidly the entropy gap shrinks with k. The truncation proof addresses the actual integer interval rather than simply counting all legal subsets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
