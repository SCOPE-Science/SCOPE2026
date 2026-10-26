# Exact state complexity of translated maximal-digit residue sequences

## Finding

For integers \(b\ge3\), \(m\ge2\), and \(c\ge0\), let \(d_b(n)\) count the occurrences of digit \(b-1\) in the standard base-\(b\) representation of \(n\), with \(d_b(0)=0\). Define the binary automatic sequence \(f_c(n)=\mathbf 1_{\{d_b(n+c)\equiv0\pmod m\}}\). Let \(N_{b,m}(c)\) be the minimum number of states of a **complete** binary-output deterministic finite automaton reading *least-significant digits first* and computing \(f_c(n)\) on every finite base-\(b\) input word, including the empty word and redundant high-order zeroes.

For any integer interval \([u,v)\) and modulus \(m\), define its digit-count residue set
\[
\mathcal R_{b,m}[u,v)=\{d_b(z)\bmod m:u\le z<v\}.
\]
When \(c=0\), \(N_{b,m}(0)=m\). For \(c\ge1\), put \(J=\lfloor\log_b c\rfloor\), and for \(0\le j\le J\), let \(h_j=b^j\), \(q_j=\lfloor c/h_j\rfloor\), and \(r_j=c-q_jh_j\). Then the following finite, exact digit-interval formula holds:
\[
\boxed{N_{b,m}(c)=m+|\mathcal R_{b,m}[0,c)|+\sum_{j=0}^{J}\left(\mathbf1_{\{q_j\ge2\}}|\mathcal R_{b,m}[r_j,h_j)|+|\mathcal R_{b,m}[0,r_j)|\right).}
\]
Each interval residue set is computable by a standard bounded-digit dynamic program, without enumerating its (potentially enormous) interval.

The adjacent shifts at consecutive powers exhibit an **unbounded one-step state-complexity drop**. For every integer \(r\ge0\),
\[
N_{b,m}(b^r)=m+\sum_{j=0}^{r}\min\{m,j+1\}.
\]
For every integer \(r\ge1\),
\[
N_{b,m}(b^r-1)=m+\min\{m,r\}+r+\sum_{j=1}^{r-1}\min\{m,j\}.
\]
Consequently, for \(r\ge m\),
\[
\boxed{N_{b,m}(b^r-1)-N_{b,m}(b^r)=r-m.}
\]
For the base-four, modulus-three sequence \(\mathbf 1_{\{d_4(n)\equiv0\pmod3\}}\), introduced in a recent study of non-regular abelian complexity, this reads \(N_{4,3}(4^r-1)=4r\), \(N_{4,3}(4^r)=3r+3\) for \(r\ge3\).

## Assumptions and scope

Digits are \(0,\ldots,b-1\), with \(b\ge3\) throughout; \(d_b\) counts **only the maximal digit** \(b-1\), not the sum of the digits. Every finite input word is interpreted as an integer with its **first** digit in the units place. The empty input represents zero. Adding any number of extra high-order zeroes must not change the output. The formula is for the minimal *complete DFAO*, not for a most-significant-digit-first automaton or for a general linear subsequence.

## Proof

**1. Residual normal form.** After reading \(j\) low-order digits representing \(u\in[0,b^j)\), write \(c+u=b^jt+v\) with \(0\le v<b^j\). For any remaining input representing \(x\), the output is
\[
\mathbf1_{\{d_b(x+t)+d_b(v)\equiv0\pmod m\}}.
\]
Thus every reachable residual function has the form \(F_{t,a}(x)=\mathbf1_{\{d_b(x+t)+a\equiv0\pmod m\}}\), with \(t\ge0\) and \(a\in\mathbb Z/m\mathbb Z\). The transition under a new low digit \(z\in[0,b)\) is
\[
(t,a)\longmapsto\left(\left\lfloor\frac{t+z}{b}\right\rfloor,\;a+\mathbf1_{\{(t+z)\bmod b=b-1\}}\pmod m\right).
\]
The output in state \((t,a)\) is \(F_{t,a}(0)\). This constructs a complete finite DFAO once reachability is bounded.

**2. Pairwise inequivalence, including different additive offsets.** Suppose \(F_{t,a}=F_{s,e}\). For any \(x\ge0\), choose \(H\) so large that \(x+t,x+s<b^H\). For \(k=0,\ldots,m-1\), let \(w_k=\sum_{i=0}^{k-1}(b-1)b^{H+i}\). There is no carry across position \(H\), hence \(d_b(x+t+w_k)=d_b(x+t)+k\), and likewise for \(s\). Equality of the binary outputs for all \(k\) forces
\[
d_b(x+t)+a\equiv d_b(x+s)+e\pmod m
\]
for every \(x\): the two residue classes have exactly the same single value of \(k\) producing output one.

If \(t<s\), fix \(L\) with \(s-t\le b^L\). For every sufficiently large \(K\), set \(x=b^K-s\ge0\). Because \(b\ge3\), \(d_b(x+s)=d_b(b^K)=0\), whereas
\[
d_b(x+t)=d_b(b^K-(s-t))=(K-L)+d_b(b^L-(s-t)).
\]
The high \(K-L\) digits are all \(b-1\); the resulting difference cannot be constant modulo \(m\) as \(K\) varies. Interchange \(s,t\) for the other ordering. Therefore \(t=s\), and then necessarily \(a=e\pmod m\). Every different reachable pair is Myhill–Nerode distinguishable; there are no accidental state merges.

**3. Reachability by quotient layers.** At depth \(j\), the integer \(c+u\) traverses the entire interval \([c,c+b^j)\). Writing \(c=q_jb^j+r_j\), the residual quotient is either \(t=q_j\), with possible lower remainders \(v\in[r_j,b^j)\), or \(t=q_j+1\), with possible remainders \(v\in[0,r_j)\). Empty intervals give no states.

For \(c\ge1\), quotient \(t=0\) occurs at all sufficiently large depths, where the remainders include integers above \(c\) with any desired number \(0,\ldots,m-1\) of maximal digits. It thus gives exactly \(m\) states. Quotient \(t=1\) contributes exactly \(|\mathcal R_{b,m}[0,c)|\) states: at sufficiently large depths it arises from the carry branch with precisely those remainders; any earlier no-carry branch with quotient one has \(c=b^j+r_j\), so its remainder interval \([r_j,b^j)\) is contained in \([0,c)\).

Every quotient \(t\ge2\) belongs to **one and only one** depth \(j\in[0,J]\): for two different depths with positive quotients, the earlier quotient is at least \(b\ge3\) times the later quotient, so even adding one to the later quotient cannot make their candidate quotient sets overlap at values at least two. At depth \(j\), the no-carry quotient is at least two exactly when \(q_j\ge2\), and the carry quotient is at least two whenever \(q_j\ge1\). The corresponding residue sets are exactly those in the displayed formula. The initial \(j=0\) case works because \([0,1)\) contains only zero. For \(c=0\), only quotient zero occurs and its full \(m\) residues are reachable. This proves both finiteness and the exact state count.

**4. Adjacent-power formulas.** For \(c=b^r\), all carry intervals at depths \(j\le r\) are empty. The positive quotients \(b^{r-j}\) carry exactly \(\min\{m,j+1\}\) residues for \(0\le j\le r\), while quotient zero carries all \(m\) residues. For \(c=b^r-1\), at depths \(0\le j<r\) we have \(q_j=b^{r-j}-1\ge2\) and \(r_j=b^j-1\); each no-carry interval is the singleton \(\{b^j-1\}\), while each nonempty carry interval has exactly \(\min\{m,j\}\) maximal-digit counts modulo \(m\). The quotient-one set has cardinality \(\min\{m,r\}\). Summation gives both formulas and the difference \(r-m\) for \(r\ge m\).

## Verification

The included standalone `checker.py` implements a base-\(b\) interval digit DP and, independently, constructs and minimizes the complete reachable transducer of residual pairs. It compares these with the exact formula for 3,840 small parameter triples and 300 additional pseudorandom triples, and checks 40,000 direct input/output computations. It also verifies both adjacent-power identities. `checker_output.txt` records the successful execution. These finite checks corroborate the proof; they are **not** a proof of the universally quantified theorem.

## Relationship to prior work

Allouche, Rampersad, Rigo, Shallit and Stipulanti (2026, arXiv:2610.03837) introduce the binary sequence selecting integers whose base-four digit-three count is divisible by three. They establish its automaticity and prove that its abelian complexity is not 2-regular. They do not compute the complete minimal DFAO state complexity of *translated input sequences*. Moradi, Rampersad and Shallit (2025, arXiv:2512.10017) develop general state-complexity constructions and bounds under linear subsequences and shifts. Their bounds do not furnish the digit-interval exact formula or the unbounded adjacent-power drop for this maximum-digit family. Charlier, Cisternino and Massuir (2019 preprint, 2021 publication, arXiv:1910.08543) study the different images \(m\mathcal T+r\) of the Thue–Morse set, not the inverse translations \(\{n:d_b(n+c)\equiv0\pmod m\}\); the two operations do not imply one another. An earlier exact binary digit-sum translation result has a related residual-pair principle, but only the base-two digit-sum setting; the present theorem applies to all bases at least three with a different digit statistic and a base-dependent disjoint quotient-layer argument.

## Limitations

The exact layer-sum formula requires \(b\ge3\); for base two, distinct quotient levels can intersect, so this formula cannot simply be reused. The theorem does not address most-significant-first representations, nonmaximal marked digits, or arbitrary linear subsequences. Equivalent results in currently unindexed work remain a priority risk. The accompanying checker verifies finitely many parameters only. Independent scientific validation has not been performed.

## References

1. J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837, first publicly posted 2026-10-02, https://arxiv.org/html/2610.03837.
2. D. Moradi, N. Rampersad, J. Shallit, *Complexity of Linear Subsequences of k-Automatic Sequences*, arXiv:2512.10017, posted 2025-12-10, https://arxiv.org/abs/2512.10017.
3. É. Charlier, C. Cisternino, A. Massuir, *Minimal automaton for multiplying and translating the Thue-Morse set*, arXiv:1910.08543, posted 2019-10-18; *Electronic Journal of Combinatorics* 28(3) (2021), paper P3.12.
