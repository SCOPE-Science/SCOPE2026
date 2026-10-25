# Sharp nesting-depth tradeoff for subsequence universality of Dyck words

## Finding
Let \(\mathcal D_{n,h}\) denote the nonempty binary Dyck words of semilength \(n\) and nesting height at most \(h\), and let \(\iota(w)\) be the largest \(k\) such that every binary word of length \(k\) occurs as an order-preserving, not necessarily contiguous subsequence of \(w\). For every integer \(h\ge2\) and \(k\ge1\), the **largest** semilength of a Dyck word with nesting height at most \(h\) and universality index exactly \(k\) is
\[
M_h(k)=\begin{cases}
 h(k+1)/2,&k\text{ odd},\\
 hk/2+1,&k\text{ even}.
\end{cases}
\]
The bounds are all attained. In particular, if \(n=qh+r\) with \(0\le r<h\), then
\[
\min_{w\in\mathcal D_{n,h}}\iota(w)=
\begin{cases}
1,&1\le n\le h,\\
2q-1,&n>h,\ r=0,\\
2q,&n>h,\ r=1,\\
2q+1,&n>h,\ 2\le r<h.
\end{cases}
\]
At height one, the unique word is \((01)^n\), with index \(n\).

## Assumptions and scope
A Dyck word \(w\in\{0,1\}^{2n}\) has equally many zeros and ones and every prefix has at least as many zeros as ones; its height \(H(w)\) is the maximum prefix difference \(\#0-\#1\). The bounds are for **all** nonempty Dyck words of height at most \(h\), with arbitrary \(n\), not for a finite enumeration and not for circular or contiguous-substring universality. The alphabet for subsequence universality is always the fixed pair \(\{0,1\}\). Integers \(n,k,h\) are positive, and the claimed formula for \(M_h\) assumes \(h\ge2\).

## Proof
**Arch lemma.** Scan a binary word from left to right with a register \(L\in\{\bot,0,1\}\), initially \(\bot\). If \(L=\bot\), store the next symbol; if the next symbol equals the stored symbol, retain it; if it differs, increment a counter \(k\) and reset \(L=\bot\). After the scan, \(k=\iota(w)\). Indeed, this procedure counts the complete greedy arches, each being a shortest remaining prefix containing both symbols. Each complete arch supplies any prescribed next symbol, so all binary targets of length \(k\) are subsequences. Conversely, after the \(k\) complete arches the residual suffix uses only one symbol; the standard greedy first-occurrence construction of an absent target (take the symbol ending each arch, followed by the symbol missing from the residual suffix) yields an absent word of length \(k+1\). The last assertion also follows by induction on the first greedy arch: every embedding of its closing symbol must reach at least the end of that arch.

**Sharp upper bound for \(h\ge2\).** During a prefix scan let \(\ell\) be its length, \(K\) its number of completed arches, \(J=K\bmod 2\), \(H\) its current Dyck height, and \(L\) its register. Put
\[
 B(2q)=2hq+2,\qquad B(2q+1)=2h(q+1),\qquad R=\ell-B(K).
\]
The following potential depends only on \(H,L,J\):
\[
\Phi(H,L,J)=
\begin{cases}
-2,&L=\bot,\ J=0,\ H=0,\\
-H,&L=\bot,\ J=0,\ H>0,\\
H-2h+2,&L=\bot,\ J=1,\\
H-2,&L=0,\ J=0,\\
H-2h+2,&L=0,\ J=1,\\
-H,&L=1\quad(\text{either }J).
\end{cases}
\]
We claim \(R\le\Phi(H,L,J)\) after every Dyck-prefix step. Initially \(R=\Phi(0,\bot,0)=-2\). Whenever an input symbol does not complete an arch, the increase in \(R\) is \(1\). Completing an arch increases \(R\) by \(3-2h\) when \(J=0\), and by \(-1\) when \(J=1\). Substitution in the six displayed potential cases verifies \(\Phi_{\rm new}-\Phi_{\rm old}\) is at least the corresponding increase in \(R\): for a pending zero, equal-letter steps give equality, and closing steps leave slack \(0\) or \(2(h-H)\) (apart from the height-one-to-zero closing step, whose slack is \(2h-4\)); for a pending one, equal-letter steps give equality and closing steps leave slack \(2H\) or \(0\); for an empty register, starting with zero gives slack \(0\) or \(2H-2\), and starting with one gives slack \(0\) or \(2(h-H-1)\). The exceptional starting state \((H,L,J)=(0,\bot,0)\) is covered with equality. All the displayed slacks are nonnegative on reachable states. The necessary reachability conditions are \(H=h\Rightarrow L=0\) and \(H=h-1\Rightarrow L\ne1\). They follow together by induction on the prefix: only a zero can enter height \(h\), and only a one from height \(h\) can enter height \(h-1\) with register one; however a step reading one from \((h,0)\) completes an arch and resets its register. In particular, an empty register can occur only below height \(h\), so its transition reading one satisfies \(H\le h-1\).

At the end of a Dyck word \(H=0\). A reachable register is \(L=1\) or \(L=\bot\), and in either case \(\Phi(0,L,J)\le0\). Hence \(2n=\ell\le B(k)\), which is exactly the asserted bound \(n\le M_h(k)\).

**Attainment.** For odd \(k=2q-1\), take \(w=(0^h1^h)^q\), of semilength \(qh\). For even \(k=2q\), take \(w=(0^h1^h)^q01\), of semilength \(qh+1\). Their heights do not exceed \(h\). To see their exact indices, use the elementary path-matching representation of the binary arch count: retain an edge between adjacent positions whenever the two letters differ, and take a maximum matching of those edges. This matching size equals the number of greedy arches (the first available unequal edge is always safe to match). Every run of \((0^h1^h)^q\) has length at least two, so all its \(2q-1\) unequal-adjacency edges are pairwise vertex-disjoint. Appending \(01\) introduces two adjacent unequal-adjacency edges and increases the matching number by one, giving \(2q\).

For prescribed \(n\), let \(n=qh+r\). If \(n\le h\), the single mountain \(0^n1^n\) has index one. For \(n>h\), use \((0^h1^h)^q\) when \(r=0\), append \(01\) when \(r=1\), and append \(0^r1^r\) when \(r\ge2\). The same transition-edge argument gives indices \(2q-1\), \(2q\), and \(2q+1\), respectively. Comparing consecutive values of \(M_h(k)\) shows these are minimal. For \(h=1\), only the alternating Dyck word exists and its index is \(n\). This proves all assertions.

## Verification
The accompanying standalone `check.py` independently enumerates every Dyck word through semilength eight and tests all binary target subsequences at the proposed index and one higher. It also performs a min-plus dynamic program over Dyck-prefix height and arch-register states, checks the sharp formula over heights 2 through 150, checks all reachable potential inequalities in this finite height range, and tests explicit extremal constructions for heights 2 through 50. These tests corroborate but do not replace the symbolic all-height proof. Reproduce with `python3 check.py` using Python 3 and the standard library only.

## Relationship to prior work
The greedy-arch characterization and the universality index are established in Barker, Fleischmann, Harwardt, Manea, and Nowotka (2020) and studied algorithmically in Schnoebelen and Veron (2023). Mol, Rampersad, and Shallit (2023) use Dyck nesting level in the study of repetition avoidance and automatic sequences. Those inspected works do not state the sharp nesting-depth/index tradeoff or its exact extremizers. The general binary transition-edge-matching formulation is an independently known reduction and is *not* asserted as a novel ingredient. The new result is the global sharp height-constrained extremal bound established by the potential argument.

## Limitations
The claim is specific to binary Dyck words and their fixed-alphabet subsequence universality. No finite-height generating function, extremizer uniqueness, or alphabet-generalization is asserted. Literature searches and inspected primary articles found no exact prior implication, but unindexed or differently phrased equivalent results remain a residual originality risk. Independent mathematical validation has not occurred.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words* (2020), arXiv:2003.04629, https://arxiv.org/abs/2003.04629.
2. P. Schnoebelen, J. Veron, *On arch factorization and subword universality for words and compressed words* (2023), arXiv:2304.11932, https://arxiv.org/abs/2304.11932.
3. L. Mol, N. Rampersad, J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences* (2023), arXiv:2301.06145, https://arxiv.org/abs/2301.06145.
4. D. Adamson et al., *k-Universality of Regular Languages* (2023), arXiv:2311.10658, https://arxiv.org/abs/2311.10658.
