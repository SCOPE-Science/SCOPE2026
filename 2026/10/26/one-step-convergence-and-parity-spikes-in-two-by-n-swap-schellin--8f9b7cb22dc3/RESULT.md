# One-step convergence and parity spikes in two-by-\(n\) swap Schelling games

## Finding
Fix any integer \(n\ge3\). Consider two colors of agents assigned to the labeled vertices of the complete bipartite graph \(K_{2,n}\), one agent per vertex. Every agent evaluates the fraction of **other agents in its open neighborhood** having its own color, using a common strictly symmetric, single-peaked payoff whose unique maximum is at \(1/2\). A swap between two differently colored agents is permitted precisely when both strictly improve their payoffs. All agents are mobile.

Let \(a\in\{0,1,2\}\) be the number of red agents in the two-vertex part, and let \(b\in\{0,\ldots,n\}\) be the number in the \(n\)-vertex part. The placement is a pure swap equilibrium exactly when

\[
\begin{aligned}
a=1,&\quad\text{or}\\
a=0\quad&\text{and }\bigl(b\le1\ \text{or}\ (2b=n)\bigr),\\
a=2\quad&\text{and }\bigl(b\ge n-1\ \text{or}\ (2b=n)\bigr).
\end{aligned}
\]

Moreover, every mutually beneficial swap from a non-equilibrium produces an equilibrium in exactly one swap; no longer strict improving path exists.

Write \(E_n(t)=\sum_{R=0}^{n+2}e_{n,R}t^R\), where \(e_{n,R}\) counts **vertex-labeled colorings** with exactly \(R\) red vertices that are equilibria (not permutations of individually labeled agents). The entire exact equilibrium spectrum is

\[
\boxed{E_n(t)=2t(1+t)^n+1+nt+nt^{n+1}+t^{n+2}
+\mathbf{1}_{\{n\ge4,\,2\mid n\}}\binom n{n/2}
\left(t^{n/2}+t^{n/2+2}\right).}
\]

Consequently the total number of equilibrium colorings is

\[
E_n(1)=2^{n+1}+2n+2+2\mathbf1_{\{n\ge4,\,2\mid n\}}\binom n{n/2}.
\]

The even-size exception has a macroscopic conditional effect. If \(n=2k\) for an integer \(k\ge2\), a uniformly chosen coloring with \(R=k\) reds is stable with probability
\[
\frac{(k+2)(3k+1)}{2(k+1)(2k+1)}\longrightarrow\frac34,
\]
whereas one with exactly balanced populations \(R=k+1\) is stable with probability
\[
\frac{k+1}{2k+1}\longrightarrow\frac12.
\]
The probability at \(R=k+2\) equals that at \(R=k\) by color reversal. Thus the two populations deviating by one from global balance have an asymptotic stability advantage \(1/4\) over perfectly balanced populations. Unconditionally under independent fair colors, equilibrium probability tends to \(1/2\), but with a parity-sensitive correction: \(1/2+1/\sqrt{2\pi n}+O(n^{-3/2})\) for even \(n\), and \(1/2+(n+1)/2^{n+1}\) for odd \(n\).

## Assumptions and scope
The graph has two labeled parts, of sizes \(2\) and \(n\ge3\), with all cross-edges and no within-part edges. No vertices are empty, all agents are exchangeable within each color, and swaps need the **strict** consent of both participants. If an agent has a fraction \(s\) of same-color neighbors in the open neighborhood, its utility is \(h(|s-1/2|)\), with a common strictly decreasing function \(h:[0,1/2]\to\mathbb R\); hence only the comparison of distances from \(1/2\) matters. This open-neighborhood convention is different from closed-neighborhood models that count each agent herself.

## Proof
First, swaps within the same part cannot strictly benefit both agents: every vertex of that part has exactly the same neighbor set, so an exchanged agent's same-color neighbor fraction stays unchanged. Swapping agents of equal colors also changes no coloring. All potentially profitable swaps therefore exchange differently colored agents across the two parts.

If \(a=1\), every agent in the large part has exactly one red and one blue neighbor, giving the optimal same-color fraction \(1/2\) no matter which color that agent has. Every across-part swap involves one such already-optimally-situated agent. Hence no pair strictly benefits, and every coloring with \(a=1\) is an equilibrium.

If \(a=0\), both agents in the small part are blue. Every across-part red-blue swap that changes the coloring exchanges one of them with a red agent in the large part, so requires \(b\ge1\). The red agent's initial same-color neighbor fraction is \(0\), while its post-swap fraction is \((b-1)/n\); it strictly improves exactly when \(2\le b\le n\). The blue agent initially has same-color neighbor fraction \((n-b)/n\), and afterward has fraction \(1/2\), so it strictly improves exactly when \(2b\ne n\). Combining the conditions gives instability iff \(b\ge2\) and \(2b\ne n\). The case \(a=2\) follows from exchanging red and blue: instability occurs iff \(b\le n-2\) and \(2b\ne n\). This proves the stated if-and-only-if classification, including all boundaries.

Each profitable swap must start from \(a=0\) or \(a=2\) and exchange differently colored agents in opposite parts, so it makes \(a=1\). This is always an equilibrium. Thus all strict better-response paths from non-equilibria have exactly one move.

For enumeration, choose which vertex of the two-vertex part is red if \(a=1\) (two choices), then choose any \(b\) red vertices of the large part. This contributes \(2t(1+t)^n\). When \(a=0\), the additional stable colorings have \(b=0\) or \(1\), contributing \(1+nt\); when \(a=2\), they have \(b=n-1\) or \(n\), contributing \(nt^{n+1}+t^{n+2}\). When \(n\) is even and at least \(4\), the otherwise-excluded exceptional value \(b=n/2\) contributes \(\binom n{n/2}t^{n/2}\) for \(a=0\), and \(\binom n{n/2}t^{n/2+2}\) for \(a=2\). These classes are disjoint, proving the polynomial.

For \(n=2k\), \(k\ge2\), the coefficients at \(R=k\) and \(R=k+1\) are respectively \(2\binom{2k}{k-1}+\binom{2k}k\) and \(2\binom{2k}k\). Dividing by \(\binom{2k+2}k\) and \(\binom{2k+2}{k+1}\), respectively, simplifies to the displayed ratios. Their difference is
\[
\frac{k(k+3)}{2(k+1)(2k+1)}>0,
\]
which tends to \(1/4\). Color reversal gives the second off-balance peak. Finally, each of the \(2^{n+2}\) colorings is equally likely under independent fair coloring. Divide \(E_n(1)\) by \(2^{n+2}\) and apply the central-binomial Stirling estimate to obtain the stated two parity regimes.

## Verification
The accompanying `verify.py` independently enumerates all \(2^{n+2}\) colorings for each \(2\le n\le10\), assesses every possible swap using the original open-neighborhood utilities at both agents' **destination** vertices, and compares the resulting stability indicator with the theorem. It checks that every improving swap reaches an equilibrium and matches all the coefficients of the closed-form polynomial. It also checks the central-population rational identities for even \(n\) through \(98\). Execute with `python3 verify.py`. The computation is a finite consistency check, not a substitute for the proof for unbounded \(n\).

## Relationship to prior work
Bilò, Bilò, Lenzner and Molitor (arXiv:2204.12599; first public version April 26, 2022) introduce symmetric single-peaked swap Schelling games and analyze equilibrium existence, integration welfare and improvement properties on bipartite graphs, **using closed neighborhoods**; their model counts the current agent herself. The present theorem is for open neighborhoods and counts all equilibria on the natural unbalanced complete-bipartite family, with an exact one-step convergence and a parity-sensitive conditional stability law. Their closed-neighborhood statements do not imply this open-neighborhood enumeration. Agarwal, Elkind, Gan and Voudouris (arXiv:1909.02421; 2019) study strategic swaps with **open-neighborhood but monotone same-color utility**, and therefore do not imply the present strict peak-at-one-half behavior. A related earlier result on balanced \(K_{m,m}\) in the same open-neighborhood payoff model concerns **equal-sized parts**, while here \(K_{2,n}\) is asymmetric for \(n\ge3\); the \(K_{2,2}\) limiting case is not asserted as a new result. No originality assertion is made for the general definitions of swap equilibria, the model of single-peaked preferences, or elementary binomial identities.

## Limitations
The theorem does not cover different peak fractions, heterogeneous preference functions, empty vertices, transfers rather than bilateral strict swaps, or arbitrary complete bipartite graphs. The counting regards colorings of labeled graph vertices; counting placements of individually labeled agents requires multiplying by color-specific factorials at fixed color totals. Literature-search coverage is not a proof of uniqueness, and equivalent formulations may exist in unindexed sources. No independent audit or independent mathematical validation has occurred.

## References
1. Davide Bilò, Vittorio Bilò, Pascal Lenzner and Louise Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599 (first version April 26, 2022), https://arxiv.org/abs/2204.12599 .
2. Aishwarya Agarwal, Edith Elkind, Jiarui Gan and Alexandros A. Voudouris, *Swap Stability in Schelling Games on Graphs*, arXiv:1909.02421 (first version September 5, 2019), https://arxiv.org/abs/1909.02421 .
