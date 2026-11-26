# Independent mathematical audit

## correctness

PASS

Conditioning on the history including the nonanticipating choice, the two possible nonzero jumps +b and -a occur with probabilities (1-p)a/(a+b) and (1-p)b/(a+b). They balance in mean and their squared contributions sum to (1-p)ab. The stopped A-count is a martingale; its expected squared increment is the expected loss of X(N-X), by expanding that quadratic. Consequently the exact identity holds at each finite truncation with terminal potential at that truncation. Since ab=(a-1)(b-1)+a+b-1>=ell-1 and potential is nonnegative, the truncated expected number of events is bounded uniformly; monotone convergence gives finite mean and almost sure termination before passing to the terminal identity by bounded and monotone convergence. Conditional summation of the propagation indicators gives E P=(1-p)E tau, and the same drift argument after an arbitrary history gives conditional remaining mean at most B. Hence survival of each length-L block conditional on the past has probability at most B/L<=1/2, giving the stated tail without a Markov selector assumption. A connected fixed graph at p=0 has ab=1 throughout and terminal consensus, so equality is exact; the one-edge one-dissenter example at p=0 has ab=ell-1 and stops at its first event. At p>0 the same one-edge example with identity rewiring has geometric wait and also attains its state-dependent bound, although that extension is not needed. Under the stated unit Poisson clock convention the pre-absorption holding mean is at most one; conditional summation yields the separate physical-time expectation bound. Inspected the frozen verifier, including its finite transient equations, without executing it. Nothing here bounds inactive update attempts or guarantees consensus on a fragmenting network.

## originality

PASS

The same microscopic proportional adoption rule is already in Golovin–Mölter–Kuehn, and for their process the budget can be derived directly from it. The special case is not a new update model and its derivation uses standard stopped-quadratic-variation machinery. The supported distinct result is the explicit finite-population identity with terminal fragmentation correction and sharp event budget over the larger class of all admissible nonanticipating selection and opinion-preserving rewiring, with its uniform tail. No inspected earlier theorem states or covers that budget on this class.

## value

PASS

The study of persistence of activity in adaptive proportional voting motivates a sharp finite event budget not visible from conserved expected opinion count. The exact terminal correction quantifies how fragmentation reduces cumulative mixed-group exposure. The guarantee works without connectivity, specified topology laws or even a Markov selector, and the quadratic order and group-size denominator are backed by equality cases. Its value is this explicit process-specific control, not the textbook martingale technique or a claim about actual time under arbitrary rate conventions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
