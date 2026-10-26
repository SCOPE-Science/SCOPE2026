# Root-degree conditioning orders the nonroot offspring vector in uniform random recursive trees

## Finding

**Theorem.** For every integer \(n\ge3\), let \(T_n\) be the uniformly random recursive tree on \(\{1,\ldots,n\}\), rooted at vertex \(1\). Each vertex \(j\ge2\) selects its parent independently and uniformly from \(\{1,\ldots,j-1\}\). Write \(R\) for the number of children of the root and \(C_v\) for the number of children of nonroot vertex \(v\). There exists a simultaneous coupling of random vectors \(C^{[1]},\ldots,C^{[n-1]}\) with the prescribed conditional laws

\[
C^{[r]}\ \stackrel{d}{=}\ (C_2,\ldots,C_n)\mid\{R=r\},
\qquad 1\le r\le n-1,
\]

such that, almost surely,

\[
C^{[1]}_v\ge C^{[2]}_v\ge\cdots\ge C^{[n-1]}_v
\quad\text{for every }v\in\{2,\ldots,n\}.
\]

Equivalently, the nonroot leaf sets \(\mathcal L^{[r]}=\{v\ge2:C^{[r]}_v=0\}\) have their conditional laws and satisfy

\[
\mathcal L^{[1]}\subseteq\cdots\subseteq\mathcal L^{[n-1]}
\quad\text{almost surely}.
\]

For every \(1\le r\le n-2\), the conditional expected number of leaves is **strictly** increasing:

\[
\mathbb E[|\mathcal L|\mid R=r]
<\mathbb E[|\mathcal L|\mid R=r+1].
\]

For any bounded coordinatewise nondecreasing functional \(f\) on \(\mathbb N^{n-1}\), \(r\mapsto\mathbb E[f((C_2,\ldots,C_n))\mid R=r]\) is nonincreasing. The dual statement holds for increasing functionals on leaf sets. Strictness is not asserted for arbitrary functionals.

## Assumptions and scope

The tree is **uniform recursive**, not uniformly Cayley-labeled or uniformly plane ordered. The root always has child \(2\); thus \(R\in\{1,\ldots,n-1\}\). A leaf means outdegree zero, not undirected degree one. The coupling is existential and simultaneous over all allowable root degrees. It does not assert a stochastic order on the entire rooted-tree shapes.

## Proof

**Step 1: Factor root choices.** For each \(j=3,\ldots,n\), independently let \(B_j\) be Bernoulli with parameter \(1/(j-1)\), and \(U_j\) uniform on \(\{2,\ldots,j-1\}\); assume all these variables independent. Assign parent \(1\) to vertex \(2\), and assign parent \(1\) to vertex \(j\) if \(B_j=1\), otherwise parent \(U_j\). Each parent is then independent and uniform on its permitted range. Define \(A=\{j\ge3:B_j=1\}\), so \(R=1+|A|\).

For any \(a\subseteq\{3,\ldots,n\}\) with cardinality \(k\), conditioning on \(R=k+1\) gives

\[
\Pr(A=a\mid R=k+1)
=\frac{\prod_{j\in a}(j-2)^{-1}}
{e_k\big((j-2)^{-1}:3\le j\le n\big)},
\]

where \(e_k\) is the \(k\)-th elementary symmetric polynomial and \(e_0=1\). This follows because \(\Pr(B_j=1)/\Pr(B_j=0)=1/(j-2)\).

**Step 2: A nested weighted-subset lemma.** Given any positive real weights \(w_1,\ldots,w_m\), let \(\mu_k\) be the distribution on \(k\)-subsets \(a\subseteq\{1,\ldots,m\}\) with \(\mu_k(a)=\prod_{i\in a}w_i/e_k(w_1,\ldots,w_m)\). Then \(\mu_0,\ldots,\mu_m\) admit a coupling \(A_0\subseteq\cdots\subseteq A_m\).

Prove this by induction on \(m\). For a \(\mu_k\)-sample, the probability \(q_k\) of including the last element is

\[
q_k=\frac{w_m e_{k-1}(w_1,\ldots,w_{m-1})}
{e_k(w_1,\ldots,w_{m-1})+w_m e_{k-1}(w_1,\ldots,w_{m-1})}.
\]

Use \(q_0=0\) and \(q_m=1\). Newton log-concavity \(e_k^2\ge e_{k-1}e_{k+1}\) for positive weights (indeed Newton's stronger normalized form) implies \(q_k\le q_{k+1}\), since the relevant odds are \(w_m e_{k-1}/e_k\), nondecreasing in \(k\). Couple the indicators of whether the last element appears at levels \(k,k+1\) monotonically. Conditional on the two indicator values, the remaining subsets have \(\mu'_k,\mu'_{k+1}\) when both indicators are zero, \(\mu'_k,\mu'_k\) when they are zero and one, and \(\mu'_{k-1},\mu'_k\) when both are one. Each case admits inclusion under the inductive hypothesis. This constructs an inclusion coupling for each adjacent pair. Since all state spaces are finite, disintegrate the pair couplings into transition kernels and chain them to obtain a single simultaneous coupling of every level. The induction begins at \(m=1\).

**Step 3: Transfer the ordering to trees.** Apply the lemma to \(w_j=1/(j-2)\), for \(j=3,\ldots,n\). Let \(A_k\) denote its coupled level-\(k\) subset. Independently sample one shared family \((U_j)\), and construct tree \(T^{[k+1]}\) by attaching every \(j\in A_k\) to the root, and every other \(j\ge3\) to \(U_j\). These trees have exactly the required laws conditioned on \(R=k+1\). For any \(v\ge2\), its number of children in the level-\(k\) tree is

\[
C^{[k+1]}_v=\sum_{j=v+1}^n\mathbf1\{j\notin A_k\}\mathbf1\{U_j=v\}.
\]

The nested inclusion \(A_k\subseteq A_{k+1}\) makes this sum nonincreasing, pointwise for every \(v\). The zero-coordinate sets are therefore nested increasing leaf sets.

**Step 4: Strict leaf-count comparison.** Each pair of adjacent root-attachment subsets satisfies \(|A_{k+1}\setminus A_k|=1\). The event \(U_j=j-1\) for every \(3\le j\le n\), independent of all \(A_k\), has probability \(1/(n-2)!>0\). On this event every nonroot chosen parent \(U_j\) is distinct. Moving the unique newly root-attached vertex to the root then removes the sole child from its former parent, making exactly one additional nonroot leaf. Thus the coupled leaf count increases with positive probability for every adjacent level, proving the displayed strict conditional inequalities. Taking expectations of bounded increasing functionals establishes the remaining assertions.

## Verification

The self-contained Python 3 program `verify.py` enumerates every recursive tree on \(n\in\{3,\ldots,9\}\), grouping leaf-set masks by root degree. It checks exact strict leaf-count expectation inequalities, all principal upward leaf events, and all leaf-count upper-tail events. For \(n\le6\) it additionally enumerates **every** upward-closed family of possible leaf sets and checks its exact conditional probability order; it uses rational arithmetic throughout. It checks weighted elementary-symmetric normalizations. The program passed 2,579 exact conditional-order assertions over 46,232 enumerated recursive trees. Those finite checks test rather than replace the unrestricted coupling proof.

## Relationship to prior work

Janson's *Asymptotic degree distribution in random recursive trees* (first published November 16, 2004) develops distributional limit theory for aggregate vertex-degree counts. Eslava, López and Ortiz's 2024 *Quenched worst-case scenario for root deletion in targeted cutting of random recursive trees* (Section 3) explicitly separates independent root-parent Bernoulli choices from common alternative parents and couples an unconditioned tree to a tree conditioned on a **range** of root degrees. The latter paper permits an arbitrary root-indicator coupling and does not establish the simultaneous inclusion ordering at **every exact degree**. The present weighted-subset monotone coupling is an additional step with a full coordinatewise descendant consequence.

The separately reported *Equal-share covariance of root degree and leaves in a random recursive tree* establishes an exact aggregate covariance; the present result is a conditional **multivariate stochastic-order** statement, which is not implied by that covariance formula. Conversely, the present theorem establishes the covariance sign but not that earlier result's exact covariance constant. The weighted-subset nesting lemma itself is a standard-looking consequence of Newton inequalities and is not claimed as new in isolation.

## Limitations

The result assumes independent uniform recursive-parent choices and one fixed labeled root. Uniform labeled Cayley trees, preferential-attachment trees, and weighted recursive trees with different conditional parent structures are not covered. It gives no sharp distribution of leaf counts or quantitative conditional expectation gaps. Broader stochastic-covering literature may offer alternate general proofs, and historical priority is provisional pending independent comparison. Published background uses related couplings, so a hidden statement implying the same multivariate ordering remains possible.

## References

1. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83, DOI: 10.1002/rsa.20046; first publicly released by publisher 2004-11-16.
2. L. Eslava, S. I. López and M. L. Ortiz, *Quenched worst-case scenario for root deletion in targeted cutting of random recursive trees*, Journal of Applied Probability, published online 2024-09-03, Cambridge Core article 67AD3B9A74E836628FA23229D25AA358, Section 3.
3. *Equal-share covariance of root degree and leaves in a random recursive tree*, publicly available mathematical research record 2026/10/4/SCOPE-equal-share-covariance-of-root-degree-and-leaves-in-a-random-rec--ab0acf44833f; related but not equivalent aggregate covariance statement.
