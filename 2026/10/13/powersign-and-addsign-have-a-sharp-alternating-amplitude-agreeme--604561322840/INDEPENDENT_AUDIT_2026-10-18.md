# Independent mathematical audit

## correctness

PASS

Solve the two-step EMA recurrence: m_(2n)=(beta A-B)/(1+beta)*(1-beta^(2n)), m_(2n-1)=(A-beta B)/(1+beta)-(beta A-B)*beta^(2n-1)/(1+beta). These give exact sign thresholds beta<=r<1/beta for all-step agreement, zero even EMA at r=1/beta, alternating odd agreement/even disagreement for r>1/beta, and a unique transient odd sign crossing for r<beta with first strictly negative odd index 2N-1, N=floor((1+log((beta-r)/(1-beta*r))/log beta)/2)+1. Direct rational-arithmetic recurrence checked 2520 parameter/time cases and separately exact-zero odd boundaries; beta=0.9 window [0.9,10/9) holds. The base PowerSign/AddSign multipliers follow by source substitution.

## originality

PASS

Bello et al. introduced sign(g)sign(m) as an agreement gate for PowerSign/AddSign and state multipliers; their inspected experimental and motivation sections do not solve the persistent two-amplitude alternating input recurrence or identify the precise all-step agreement window. Adjacent Signum/EMA-periodic Resultary hits concern different algorithms. Best-of-knowledge new statement is a complete diagnostic gate phase diagram, not the primitive itself.

## value

PASS

The sign-agreement gate is the interpretable mechanism of these optimizers. A maximally reversing balanced gradient can nonetheless be classified as agreement at every step and amplified, an exact blind window of practical mathematical interest; its sharp amplitude boundaries and finite transient beyond them distinguish response regimes. This is motivated by the actual method rather than an arbitrary EMA algebra exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
