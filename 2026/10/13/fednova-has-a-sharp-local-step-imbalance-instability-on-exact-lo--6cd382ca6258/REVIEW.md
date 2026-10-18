# Independent mathematical audit

## correctness

PASS

With local quadratic step eta=1/a, the first local update reaches b_i and all later local gradients vanish. Hence FedNova normalized gradient d_i=a(x-b_i)/tau_i. Its prescribed tau_eff=(tau_1+tau_2)/2 for equal clients gives x^+=x-(tau_1+tau_2)/4[(x-b_1)/tau_1+(x-b_2)/tau_2]. Collecting terms yields affine coefficient M=-(tau_1-tau_2)^2/(4 tau_1 tau_2), fixed point (tau_2 b_1+tau_1 b_2)/(tau_1+tau_2), and |M|<1 iff 3-2sqrt(2)<tau_2/tau_1<3+2sqrt(2). Independent exact fractions verify M_{1,6}=-25/24 and stable ratios 2:3,3:16. Equality at irrational frontier cannot occur for integral tau_i.

## originality

PASS

Original FedNova objective-consistency work normalizes local SGD and proves horizon-dependent convergence, and FedShuffle compares improved scaling. The exact fixed-step 2-client exact-local-solve affine multiplier and sharp 6:1 divergence were not found as stated or implied by their inspected claims; general convergence with horizon-vanishing eta does not imply constant eta=1/a stability. Best-of-knowledge O pass.

## value

PASS

A sharply quantified mechanism in a widely used federated algorithm: heterogeneous local work can produce alternating global divergence even when each client step individually solves its quadratic exactly. The 6:1 first integer imbalance and false-affine fixed-point location provide practical boundary witnesses, not merely reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
