# Independent mathematical audit

## correctness

PASS

For one-sign maximality H=A(F_p2)[p+1] is a subgroup with |H| dividing both the actual group order and the Hasse upper endpoint (p+1)^(2g). If |H| exceeded interval width W_g(p)=(p+1)^(2g)-(p-1)^(2g), the two multiples would coincide; nonmaximal cases thus have |H|<=W. Divide by lower bound (p-1)^(2g), clip at 1, and power the conditional bound for k independent samples. The minimality branch is symmetric using p-1. Expansion gives W_g(p)=4g p^(2g-1)+2sum_{r=1}^{g-1} C(2g,2r+1)p^(2g-2r-1) for g>=2, strictly larger than the proof's substituted 4g p^(2g-1). The original arXiv:2610.01924v1 Theorem 4.1 p20 was read and its displayed inequality directly shows the incorrect smaller constant. No claim smaller bound intrinsically impossible by a different structural theorem.

## originality

PASS

Direct reading of the 42-page original source (arXiv:2610.01924v1, Lemma 2.1 and Theorem 4.1 p20) establishes the stronger exact Hasse interval and the erroneous simplification to 4g p^(2g-1). The new result's point is a correction and explicit valid finite-p branchwise bound, not a new asymptotic order or a restatement of the cited interval. Sutherland's elliptic-curve g=1 argument has exact width 4p and cannot supply the g>=2 correction. Searches found no subsequent published correction; priority remains best-of-knowledge.

## value

PASS

A valid false-acceptance estimate is essential to the arbitrary-dimensional Monte Carlo extremality test used for cryptographic verification. Repairing an invalid width substitution while preserving the correct O(1/p) estimate is a substantive proof correction and an explicit usable guarantee, despite elementary binomial algebra. The result carefully avoids asserting a counterexample to the asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
