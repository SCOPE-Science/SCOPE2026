# Independent mathematical audit

## correctness

PASS

Generate iid labels even after the bounded first-emptying time T, but do not remove any more balls. Exactly one bin survives when n≥2, including a=0,n with T=0; R=n−T. If bin 1 survives, the fixed-horizon deficit (a−B)_+ is the number of label-2 draws after T, and (B−a)_+=0. Their expected contributions conditional on the stopped history are qR and zero. If bin 2 survives, reverse the roles to obtain pR for the positive excess (B−a)_+. Dividing by the respective probabilities and adding proves the identity. Taking successive integer differences gives (F_B(a)−q)/(pq), whose slopes increase strictly because every binomial atom is positive. Since F_B(0)=q^n<q and F_B(n−1)=1−p^n>q, the first q-crossing is interior, and a zero slope gives exactly the adjacent tie shown. For fixed p, Berry–Esseen and positive normal density near z_p bracket the quantile between np+√(npq)z_p plus and minus a p-dependent bounded integer correction. The standardized binomial has unit second moment, providing uniform integrability of both hinge losses; the normal moments at Φ(z_p)=q give limiting normalized loss φ(z_p)/(pq), hence the stated leading remainder. Read frozen VERIFICATION.md and verify.py without executing them. Independent exact enumeration of iid label histories at 208 allocations, covering four adjacent ties and degenerate splits, agrees with the formula and optimizing sets (python -I /workspace/branches/independent_checks.py 2). The asymptotic and all-real-p statements are justified by proof, not enumeration.

## originality

PASS

The binomial critical fractile and Gaussian limit calculations are standard once the objective is a binomial check loss. The supported distinction is the exact fixed-horizon loss representation of the biased first-depletion remainder, and the resulting all-size optimizer and explicit fixed-bias asymptotics in the same model as the prior unequal-selection example. Correa et al. already identify the phenomenon and conjecture a root-n scale in their unequal-selection discussion; the bound formula provides the precise two-bin shift. No inspected source gives or otherwise determines the exact reduction and optimizer for arbitrary bias and allocation. Scoped decision; not an absolute priority claim.

## value

PASS

For the first nonuniform case of a published allocation problem, the identity turns a stopping-time objective into an explicit static binomial loss. It replaces single-instance comparisons with a full finite rule including exact ties and gives the sign and leading size of the correction to proportional allocation plus the optimal expected remainder. The result addresses a natural two-bin question, without claiming a general multibin theorem or uniformity for p approaching the endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
