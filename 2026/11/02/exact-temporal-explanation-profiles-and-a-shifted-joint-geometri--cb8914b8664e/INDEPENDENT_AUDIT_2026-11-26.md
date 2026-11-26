# Independent mathematical audit

## correctness

PASS

The strong-Until witness terms are incomparable by their distinct q-literals. On truth the present terms are exactly the minimal sufficient sets; a minimal transversal takes either all witness q-literals, or one p-literal at the earliest chosen blocker and exactly the q-literals for witnesses at or before that index. On falsehood a minimal lock is either all q-literals false or one false p_i and all q_j false through i; the latter is redundant at i=n−1. Minimal flips are the inclusion-minimal missing bits of a witness term. If the first true q is at z<n, its missing preceding p-bits dominate every later witness deficit, and a preceding q-deficit survives precisely through the last missing p before z. If all q are false the witness deficits have distinct q-bits and are incomparable. This accounts for n=1 and all-q-false traces. The last positive witness mass follows by multiplying its prefix probability 2^(−l−1) by the probability of no later witness; the last negative blocker mass sums a geometric run of (p=1,q=0) before the first true q. Earlier free bits supply the binomial factors. Dividing exact masses by the outcome probabilities and taking n→∞ yields the common geometric mixing variable G on {0,1,...} with parameter 1/2, and CXp count 1+G or 2+G. Coupling at the first false p and first true q gives a preconditioning failure probability at most 2^(1−n); the two conditioning probabilities stay positive. This yields TV convergence, and the geometric tails (or the finite mass formulas) justify moment convergence. The generating functions give E[A]=3/2, and Cov(A,C)=Var(G)/2=1. Independently compared complete minimal sets to completions through n=4 and matched every exact joint cell through n=8 by witness deficits and transversal enumeration. Replay: `python3 /workspace/branches/frozen_replay.py 1`.

## originality

PASS

The supported distinct contribution is the exact finite and limiting conditional joint law of the two explanation counts for strong Until, with explicit witness/blocker profiles supplying the count. The definitions, duality and general per-trace enumeration are established. The strongest matching finite-trace primary sources cover the setting and method but not the joint law in the inspected results. The closest catalog counting theorem concerns a different temporal predicate.

## value

PASS

Strong Until is a canonical temporal operator, and exact explanation counts quantify the behavior of two standard explanation outputs on a fully specified test distribution. The joint shift and common AXp marginal give a nontrivial comparison across truth values, including correlation information unavailable from one marginal or from existence/duality alone. The finite law also gives an exact benchmark for implementations on this basic predicate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
