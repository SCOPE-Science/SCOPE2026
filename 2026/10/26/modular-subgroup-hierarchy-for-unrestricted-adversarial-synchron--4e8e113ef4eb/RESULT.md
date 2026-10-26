# Modular subgroup hierarchy for unrestricted adversarial synchronization of cyclic automata

## Finding

Let \(n\ge2\). Consider the deterministic two-letter automaton on \(G=\mathbb Z/n\mathbb Z\) in which \(a(x)=x+1\) and \(b(x)=f(x)\) for an arbitrary function \(f:G\to G\). In the unrestricted adversarial synchronization game, Alice selects one letter on each turn and Bob can insert any finite word of letters between Alice's turns. Alice wins if the concatenated word sends every state to one state.

Define \(H_0=\{0\}\) and, recursively,
\[
H_{t+1}=\left\{d\in G:\ f(x+d)-f(x)\in H_t\ \text{for every }x\in G\right\}.
\]
Then every \(H_t\) is an additive subgroup, \(H_t\subseteq H_{t+1}\), and the sequence stabilizes after at most \(\Omega(n)\) strict increases, where \(\Omega(n)\) is the number of prime factors counted with multiplicity. **Alice wins the unrestricted game exactly when the stable subgroup is \(G\).** More precisely, for any two marked states with difference \(d\), against an adversary allowed an arbitrary initial word as well, Alice can merge them in at most \(t\) of her letter moves if and only if \(d\in H_t\).

The criterion is computable directly from the transition table in \(O(n^2\log n)\) elementary modular operations. It gives two infinite classifications:

1. For prime \(n\), Alice wins if and only if \(f\) is constant. For every composite \(n\), there exists a nonconstant \(f\) for which Alice wins; in fact, two of her moves suffice for an explicit construction.
2. If \(n=pq\) is a product of primes, the exact number of winning functions \(f:G\to G\), with the cycle letter fixed and the states labeled, is
\[
\boxed{\begin{cases}
 p^{p+1},&p=q,\\
 p\,q^p+q\,p^q-pq,&p\ne q.
\end{cases}}
\]
For distinct primes \(p,q\), the winning functions are exactly those constant on residue classes modulo \(p\) with all output values in one residue class modulo \(p\), or the analogous functions modulo \(q\). For \(p=q\), there is only the condition modulo \(p\). In both statements constant functions are included.

## Assumptions and scope

All arithmetic on states and function values is modulo \(n\). A period \(d\) of \(f\) means \(f(x+d)=f(x)\) for all \(x\). A function is constant on residue classes modulo a divisor \(r\) if \(f(x+r)=f(x)\) for all states. Having outputs in one residue class modulo \(r\) means there exists an integer \(s\) such that \(f(x)\equiv s\pmod r\) for every state.

Bob's inserted word can be empty. Allowing him to move first is equivalent for the initial full state set, since a reset word stays a reset word when prefixed by any word, and Bob may pass. We use the Bob-first convention for the exact two-state statement. Winning means Alice has a strategy guaranteeing a reset after finitely many turns, regardless of Bob's finite replies. The counts are for all \(n^n\) labeled choices of \(f\), with the specified cyclic letter \(a\), not for isomorphism classes and not for arbitrary pairs of transformations.

## Proof

**1. Subgroups and stability.** For any subgroup \(K\le G\), let \(\Phi(K)=\{d:f(x+d)-f(x)\in K\text{ for every }x\}\). The difference formula
\[
f(x+d+e)-f(x)=\bigl(f(x+d+e)-f(x+e)\bigr)+\bigl(f(x+e)-f(x)\bigr)
\]
shows that \(\Phi(K)\) is closed under addition; closure under negation follows by replacing \(x\) with \(x-d\). Thus it is a subgroup. Also \(H_0\subseteq H_1\); if \(H_{t-1}\subseteq H_t\), then \(\Phi(H_{t-1})\subseteq\Phi(H_t)\), proving induction. If two states have difference in \(H_t\), application of \(a\) leaves their difference unchanged, while application of \(b\) sends it into \(H_{t-1}\subseteq H_t\) for \(t\ge1\). Thus arbitrary words preserve the property of having difference in \(H_t\). If any two successive subgroups coincide, all later ones coincide.

**2. Exact pair-game characterization.** At \(t=0\), two states can already be merged if and only if their difference is zero. Suppose the characterization holds at \(t\). If a pair has difference \(d\in H_{t+1}\), then every initial word chosen by Bob leaves its difference in \(H_{t+1}\), by Step 1. Alice chooses \(b\), sending the difference into \(H_t\), and uses the strategy guaranteed by the induction hypothesis for the remaining \(t\) moves. Conversely, if \(d\notin H_{t+1}\), choose \(x\) with \(f(x+d)-f(x)\notin H_t\). Bob can rotate the pair by a power of \(a\) so its ordered states are \(x,x+d\). If Alice chooses \(a\), the difference remains \(d\notin H_t\); if she chooses \(b\), the difference is \(f(x+d)-f(x)\notin H_t\). In either case the remaining \(t\) moves cannot be forced to merge the marked pair. This proves the iff statement for all \(t\).

**3. Full-state criterion and algorithm.** If the eventual subgroup is all of \(G\), then every pair of states has a bounded-move winning strategy. Alice can select two currently distinct images, merge them by that pair strategy, and repeat: arbitrary intervening words never increase the number of distinct images. At most \(n-1\) such merges are needed, so Alice wins from the full set. Conversely, if the subgroup stabilizes properly, choose a pair whose difference lies outside it. Step 2 says Bob can defeat any proposed finite bound on Alice's pair-merging moves. More concretely, after each of Alice's moves, Bob rotates the still-distinct marked pair so that applying \(b\) on Alice's next move also keeps its difference outside the stable subgroup; \(a\) never changes the difference. This inductively prevents synchronization forever, including from the full set. Therefore the criterion is exact. Every strict subgroup inclusion at least doubles subgroup size, giving at most \(\Omega(n)\le\log_2 n\) strict increases. Constructing each \(H_{t+1}\) checks at most \(n^2\) differences, establishing the stated time bound.

**4. Prime/composite and semiprime cases.** If \(n\) is prime, the only subgroups are \(\{0\}\) and \(G\). The first step reaches \(G\) exactly when \(f(x+d)=f(x)\) for every \(x,d\), i.e., precisely when \(f\) is constant. Otherwise it stabilizes at \(\{0\}\). Now let \(n\) be composite, and choose \(r\mid n\) with \(1<r<n\). Set \(f(x)=r\) when \(x\equiv1\pmod r\), and \(f(x)=0\) otherwise. This nonconstant map has period \(r\), hence \(rG\subseteq H_1\), and all its outputs are congruent modulo \(r\). Consequently \(H_2=G\), so Alice wins in two moves against arbitrary intervening words.

Finally, suppose \(n=pq\) with primes \(p,q\). The subgroup lattice has at most two nontrivial proper subgroups, namely multiples of \(p\) and of \(q\) (one if \(p=q\)). If \(H_1=\{0\}\), the chain stays there. If \(H_1=G\), \(f\) is constant. Otherwise \(H_1\) is the subgroup of multiples of one of these prime divisors \(r\), and no proper larger subgroup contains it. Winning is equivalent to \(H_2=G\), i.e., all \(f(x)\) are congruent modulo \(r\). Together with \(rG\subseteq H_1\), this says exactly that \(f\) is periodic modulo \(r\) and its image lies in one residue class modulo \(r\). Conversely either property pair forces \(H_2=G\). For a fixed \(r\), choose the output residue class in \(r\) ways and choose the \(r\) independent outputs from the \(n/r\) elements of that class, giving \(r(n/r)^r\) maps. For \(p=q\) this is \(p^{p+1}\). For distinct \(p,q\), the two sets have intersection exactly the \(n\) constant maps: having both periods forces period \(\gcd(p,q)=1\). Inclusion-exclusion gives the stated total.

## Verification

The standalone `verify.py` contains two algorithms implemented separately: the modular subgroup iteration and a complete attractor calculation on all nonempty image subsets, where Bob's arbitrary replies are represented by transitive closure under both letters. The latter algorithm does **not** call or rely on the subgroup recurrence. Both agree on **every** function \(f:G\to G\) for \(n=2,3,4,5,6\); their exact winning counts are respectively \(2,3,8,5,36\), among respectively \(4,27,256,3125,46656\) possible functions. It also checks a three-stage winning example at \(n=8\), with subgroup sizes \(1,2,4,8\). The proof above, not these finite checks, establishes the all-\(n\) statements.

## Relationship to prior work

Lipin and Volkov (2026) introduced and analyzed the unrestricted adversarial synchronization game, established a general relation-iteration and two-token criterion (their Section 3), and gave general recognition algorithms. Those results and the game definition are used as context; the present result identifies the **explicit modular subgroup collapse** for the natural class with one full-cycle letter, gives a sharp prime/composite distinction, and enumerates all winning maps at semiprime orders. The general algorithms in that paper do not state this cyclic arithmetic classification or the counting formulas. Singh and Raj (2018) summarize ordinary synchronization of circular automata, including the known prime-order synchronization result for nonpermutation letters; ordinary synchronization is weaker than winning against arbitrary adversarial replies, and their results do not entail the game classification.

## Limitations

The two-letter assumption and the fixed full-cycle letter are essential to this criterion as stated. The explicit counting formulas are proved only for orders with two prime factors counted with multiplicity, not all composite orders. More factors permit longer subgroup chains, as the verified eight-state example illustrates. The result does not claim a new bound for reset-word length in general automata. An equivalent specialization in unindexed literature remains possible; no independent scientific audit has been performed.

## References

1. A. E. Lipin and M. V. Volkov, *Adversarial Synchronization*, arXiv:2601.18362, first publicly available 2026-01-26, Sections 2, 3 and 5. https://arxiv.org/abs/2601.18362
2. S. N. Singh and A. Raj, *On the Synchronization of Circular Semi-Flower Automata*, arXiv:1808.01711, 2018, Sections 1 and 2. https://arxiv.org/abs/1808.01711
