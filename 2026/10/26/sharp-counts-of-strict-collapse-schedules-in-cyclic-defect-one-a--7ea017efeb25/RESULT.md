# Sharp counts of strict-collapse schedules in cyclic defect-one automata

## Finding
Let \(n\ge2\), \(1\le d<n\), and \(Q=\mathbb Z/n\mathbb Z\). The two letters act on states by
\[
a(i)=i+1\pmod n,\qquad b(0)=d,\quad b(i)=i\quad(i\ne0).
\]
Set \(g=\gcd(n,d)\). For a nonempty target \(S\subseteq Q\), its full-state image is reachable by a word if and only if \(S\) meets every residue class modulo \(g\). Whenever it is reachable, the least number of occurrences of \(b\) among reaching words is exactly \(k=n-|S|\).

A *strict-collapse deletion schedule for* \(H=Q\setminus S\) is a sequence of \(k\) distinct states in the comoving coordinates described below, recording the states removed at each successive effective use of \(b\), without regard to intervening rotations. Such schedules are not literal automaton words. If the maximal forward-\(d\) runs of \(H\) have lengths \(\ell_1,\ldots,\ell_r\), the exact number of schedules is
\[
N(H)=\frac{k!}{\ell_1!\cdots\ell_r!}.
\]
The empty deletion set has one empty schedule. When \(g=1\), for every \(1\le k<n\), putting \(r=\min(k,n-k)\), \(q=\lfloor k/r\rfloor\), and \(t=k-qr\), the sharp envelope over all missing sets with \(k\) elements is
\[
\max_{|H|=k}N(H)=\frac{k!}{(q!)^{r-t}((q+1)!)^t}.
\]
For \(g=1\), among reset words having the minimum possible number \(n-1\) of \(b\)-letters, the unique shortest word is
\[
b(a^{n-d}b)^{n-2},\qquad |w|=1+(n-2)(n-d+1).
\]
This last claim does **not** assert that words having more than \(n-1\) occurrences of \(b\) cannot reset more quickly.

## Assumptions and scope
Word actions are applied left to right to the full state set. A letter \(a\) is the cyclic permutation and \(b\) is idempotent and of rank \(n-1\). The notion of reaching a subset is the precise equality \(Qw=S\). There are no probabilistic assumptions. The full result includes noncoprime \(n,d\); the sharp count envelope and reset-word rigidity specialize to coprime \(n,d\).

## Proof
**An invariant and the minimum resource.** The \(g\) congruence classes modulo \(g\) are the orbits of addition by \(d\). Under \(a\), these classes are permuted, and under \(b\) each class maps into itself. Thus a full-state image always meets every such class. Since \(a\) is a permutation and \(b\) loses at most one image state, a word reaching \(|S|=n-k\) uses at least \(k\) copies of \(b\). Equality forces every copy to decrease rank by one.

**Coordinates for effective deletion.** After every prefix, undo the total number \(A\) of occurrences of \(a\) modulo \(n\). In these *comoving coordinates* the initial image is \(Q\). If a \(b\) is applied with cumulative rotation \(A\), put \(p=-A\pmod n\). In the comoving coordinates, the letter attempts to send \(p\) to \(p+d\). If both states are present, this deletes exactly \(p\) and decreases image rank by one. At a strict-collapse step, therefore, the site \(p\) is absent afterward, and \(p+d\) was not deleted earlier. Conversely, those two conditions ensure a strict collapse. Every sequence \(p_1,\ldots,p_k\) satisfying these conditions can be implemented: choose each intervening nonnegative rotation congruent to \(p_i-p_{i+1}\), and use a final rotation so that the total rotation is zero modulo \(n\). Its final image is \(Q\setminus\{p_1,\ldots,p_k\}\).

**Chains and all-target reachability.** A deletion order for \(H\) is legal exactly when \(p\) appears before \(p+d\) whenever both belong to \(H\). If \(H\) contains a full orbit under addition by \(d\), those requirements form a directed cycle and no such order exists; this is exactly the failure of \(S\) to meet that orbit. Otherwise, the induced directed graph on \(H\) is a disjoint union of finite directed paths: maximal \(d\)-successor runs. Their orders are forced internally but the runs may be arbitrarily interleaved. The multinomial number of interleavings is \(k!/\prod_j\ell_j!\). It is positive exactly when \(S\) meets every \(d\)-orbit, which are precisely the residue classes modulo \(g\). Combining construction, invariant, and minimum-resource bound proves the first assertions.

**Sharp coprime envelope.** Assume \(g=1\), so addition by \(d\) is a single cycle. Every maximal deleted run is nonempty and must be followed by an undeleted vertex; consequently its count \(r'\) satisfies \(r'\le\min(k,n-k)\). For fixed \(r'\), the product of factorial run lengths is smallest when the lengths differ by at most one: replacing lengths \(u,v\) with \(u-1,v+1\), for \(u\ge v+2\), decreases the product. Increasing the number of runs while keeping total \(k\) never increases the minimum factorial product, as one can split a positive-length run. Thus the maximal permissible \(r=\min(k,n-k)\), with balanced lengths \(q\) and \(q+1\), gives the displayed upper bound. Place these runs on the single \(d\)-cycle, separating them by distinct survivors; since \(n-k\ge r\), the bound is realized.

**The resource-minimal reset word.** Under \(g=1\), a singleton target has a deleted complement consisting of exactly one \(d\)-successor run of length \(n-1\). Hence any reset word with just \(n-1\) copies of \(b\) has a unique order of deletion sites \(p_{j+1}=p_j+d\pmod n\). If the cumulative rotation before copy \(j\) is \(A_j\), this yields \(A_{j+1}-A_j\equiv-d\pmod n\); the least nonnegative number of intervening \(a\)-letters is \(n-d\), since \(1\le d<n\). There are \(n-2\) gaps, so every such reset word has length at least \((n-1)+(n-2)(n-d)\). The word \(b(a^{n-d}b)^{n-2}\) realizes exactly those gaps and resets the full state set. Equality disallows all leading/trailing \(a\)-letters and all extra full-cycle turns between \(b\)-letters; hence equality holds for that word alone.

## Verification
The standalone checker `artifacts/verify.py` independently uses zero-one BFS on all subset states, assigning cost zero to \(a\) and cost one to \(b\), and brute-force enumerates all deletion-site permutations. For every \(n\in\{2,\ldots,8\}\), all \(1\le d<n\), and all nonempty subsets, it checks the reachable-target characterization, the minimum count of \(b\), and the factorial run-interleaving formula. For coprime pairs it checks the sharp envelope across every cardinality and executes the claimed constrained reset witness. The executable check ended with `VERIFY_OK 3048 subset/automaton cases`. These finite checks support but do not replace the proof for all \(n\).

## Relationship to prior work
Don (2015; journal 2016) proved strong subset reachability for aperiodically \(1\)-contracting and coprime circular automata. In particular, the coprime subset-reachability statement here is **known**, not a claimed novelty. The new quantitative point is the characterization and sharp factorial enumeration of all schedules using the least possible number of nonpermutation letters, plus the exact target-set obstruction without coprimality and the resource-constrained reset length. The published result *Two-defect reachability in cyclic defect-one automata* treats arbitrary rank-\(n-1\) transitions for deletion of two states, not arbitrary-size deletion-set order enumerators. Generic shortest-reset-word algorithms treat unrestricted length rather than the minimal number of nonpermutation letters.

## Limitations
The counted objects are normalized sequences of distinct strict-collapse sites, not automaton words; many words realize any single such schedule. The reset length is optimal under **exactly \(n-1\) occurrences of \(b\)**, and the globally shortest reset-word threshold is not determined for all parameters. The sharp schedule-count envelope is proved for coprime displacement, not arbitrary \(g\). Historical priority is assessed to the extent of inspected literature; unindexed earlier equivalent counts cannot be excluded. No independent mathematical audit has been performed.

## References
1. H. Don, *The Černý Conjecture and 1-Contracting Automata*, arXiv:1507.06070 (first public 2015-07-22); *Electronic Journal of Combinatorics* 23(3) (2016), P3.12. https://arxiv.org/abs/1507.06070 ; doi:10.37236/5616.
2. A. Kisielewicz, J. Kowalski and M. Szykuła, *Computing shortest reset words of synchronizing automata*, online 2013-11-17; *Journal of Combinatorial Optimization* 29 (2015), 88–124; doi:10.1007/s10878-013-9682-0.
3. *Two-defect reachability in cyclic defect-one automata*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-two-defect-reachability-in-cyclic-defect-one-automata--3d0ad329ab1e.
