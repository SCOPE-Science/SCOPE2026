# Independent mathematical audit

## correctness

PASS

Verified the full evaluation law and its boundaries, not just the finite tests. In the gamma expansion of N_n(X)/X, the coefficient at X^(k−1) is (n−1)!/[(k−1)!(n−k+1)!] times the Vandermonde sum Σ_j binom(k−1,j)binom(n−k+1,n−k−j)=binom(n,n−k). This recovers the defining coefficient. At even x the quotient is an odd unit since its constant coefficient is one. At odd x the gamma endpoint has valuation h=s₂(m+1)−1 for n=2m+1; for n=2m first divide by 1+X, and the endpoint is (2m−1)C_(m−1)x^(m−1) of valuation h=s₂(m)−1. A term r indices below the endpoint has valuation at least h+2r−s₂(r)>h by the binary carry inequality and the factor (1+x)^(2r), excluding cancellation even in Z₂. Restore x and, in even degree, 1+x. This includes n=1 and n=2, and the x=0 and x=−1 evaluations without division by zero. The qualifying even residues are x≡0 mod 2^r; the odd residues are all or none in odd degree and x≡−1 mod 2^max(1,r−h) in even degree. Intersecting at all r gives the two asserted Z₂ zero sets. Independent bounded replay: `cd /workspace && python checks/independent_replay.py 2` passed 8,800 direct Horner evaluations and 234 full fiber checks. The frozen verification is finite corroboration. Its Python 3.8 compatibility note is too broad for int.bit_count (use 3.10+); the novelty paragraph's ‘all prime-power’ phrase means powers of two under the explicit Finding and scope. Neither affects the theorem.

## originality

PASS

The supported distinction is a uniform valuation of polynomial values for odd weights, particularly the exact excess ν₂(x+1) in even degree, with the resulting fibers and two-adic zero sets. The gamma identity, Catalan valuation, even-index vanishing at −1 and coefficient divisibility have prior coverage and are not credited as new. The statement-level checks did not establish coverage of the uniform evaluation law; this is a bounded best-knowledge judgment.

## value

PASS

Uniform control of possible cancellation in a natural Catalan refinement gives a sharp, reusable parity-dependent arithmetic invariant: all odd weights have one order in odd index, while even index singles out exact distance to one root. It answers the entire two-adic root and residue-lifting question without a finite cutoff or individual-weight search. The new content is the strict minimum over all other gamma terms, not recomputing a known Catalan valuation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
