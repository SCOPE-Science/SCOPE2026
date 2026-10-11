# Independent mathematical audit

## correctness

PASS

D=-pq+3p+3q+3. For p≥7 it is negative; p=3 gives D=12 and q≥13 is excluded because the divisors below 12 are {1,2,3,6}; p=5 forces q=7 and D=4, impossible from two distinct divisors. Fresh brute force below 100 reproduces only 30 and 66; the frozen verifier extends bounded regression below 1000 but is not used for exhaustiveness.

## originality

PASS

The 2023 and 2025 primary papers classify 2-near-perfect numbers with exactly two distinct prime factors, not the squarefree three-prime family 2pq. OEIS A341475 lists 30 and 66 but gives no exhaustion theorem for 2pq; Resultary returns the audited result as the exact hit.

## value

PASS

After the exactly-two-prime-factor classification, squarefree 2pq is the simplest natural three-prime-support layer and the theorem gives a complete infinite-family classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
