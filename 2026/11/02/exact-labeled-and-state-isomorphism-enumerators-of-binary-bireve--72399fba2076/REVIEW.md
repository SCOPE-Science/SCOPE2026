# Independent mathematical audit

## correctness

PASS

For binary input/output, each state output action is identity or flip and inverse-input reachability is a permutation iff delta0(A)=delta1(A), A=set of flippers. With d=delta1 and pi=d^-1 delta0 this becomes pi(A)=A: a bijection, giving choose(n,k)*n!*k!*(n-k)!=(n!)^2 machines for each |A|=k. Under state-only relabeling, Burnside fixes d and pi in centralizer C(sigma), and invariant A is a union of orbits of permutation pi on cycles of sigma. The cycle-index identity sum_tau prod_C (1+s^{|C|})=m!sum_{h=0}^m s^h gives U_n(t)=sum_{lambda partition n}prod_j j^{m_j}m_j!sum_{h=0}^{m_j}t^{jh}. Permutation transition orbits are SCCs; labeled SET construction yields n!*[z^n t^k]log F(z,t), with F=sum_n n!(sum_{k<=n}t^k)z^n. The unlabeled multiset inversion is V=sum_{r>=1}mu(r)/r log U(z^r,t^r). For uniform labeled machines, d uniform and pi weighted 2^{cycles}; common invariant j-subset expectation (j+1)(n-j+1)/((n+1)*C(n,j)), and union bound/Bonferroni yield connected probability 1-2/n+O(n^-2). Independently tested all (n!)^2*2^n raw pairs n<=4 under direct inverse-transition definitions and connected reachability: total 2,12,144,2880; connected 2,8,88,1776. No infinite conclusion drawn solely from experiments.

## originality

PASS

Qualified best-of-knowledge originality: compare exact statement and model rather than terminology. Known foundational tools, marginal/special cases and directly overlapping results are credited. No actually inspected stronger result is shown to imply the complete final claim. Unavailable or only partially inspected plausible primary work is identified in residual risks; failed searches are not treated as proof of novelty.

## value

PASS

A complete exact all-state-count census of a natural syntactic automata class, including labeled swap refinement, state-only isomorphism Burnside polynomial, connected components via generating functions and a sharp asymptotic almost-sure connectivity law, is a useful combinatorial classification. The choice of fixed binary alphabet is natural and the distinction from state-plus-alphabet symmetry affects explicit class counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
