# A sharp bridge-bottleneck boundary for two-seed SIR switchover on double stars

## Finding

A two-hub network with arbitrarily many terminal contacts need not exhibit the familiar reversal between central and geographically dispersed epidemic seeding. In the deterministic-one-step-recovery susceptible–infected–removed (SIR) model, consider two adjacent hubs, each attached to exactly \(n\geq 1\) private leaves. Compare the expected final number infected when the two hubs are seeded, \(H_n(p)\), with the corresponding expectation \(U_n(p)\) when two distinct seeds are chosen uniformly from all \(2n+2\) vertices. Each edge independently transmits with probability \(0\leq p\leq1\).

For every integer \(n\geq1\) and \(p\in[0,1]\),

\[
H_n(p)=2+2np,
\]

\[
\boxed{
H_n(p)-U_n(p)=
\frac{np(p-1)}{(n+1)(2n+1)}
\left[3n(n-1)p^2+(3n-1)p-4n^2+2n+2\right].
}
\]

The complete strict comparison on \(0<p<1\) is:

1. If \(n=1\), the uniformly seeded epidemic has strictly larger expected size for every \(p\).
2. If \(n=2\), central seeding is strictly more dangerous for \(0<p<p_*\), equality holds at \(p=p_*\), and uniform seeding is strictly more dangerous for \(p_*<p<1\), where
\[
\boxed{p_*=(\sqrt{265}-5)/12=0.9399017163\ldots.}
\]
3. If \(n\geq3\), central seeding is strictly more dangerous for every \(0<p<1\): there is no reversal even as transmission approaches certainty.

Both strategies coincide at \(p=0\) and \(p=1\). For every fixed \(0<p<1\), the strict central advantage for large networks occupies a positive limiting fraction of the population:

\[
\boxed{
\lim_{n\to\infty}
\frac{H_n(p)-U_n(p)}{2n+2}
=\frac{p(1-p)(4-3p^2)}4>0.
}
\]

Thus the six-vertex double star is the only member of this natural family to exhibit a genuine positive-to-negative seeding switchover. This is a comparison of *expected final outbreak sizes*, not a pointwise dominance statement for every edge realization or seed pair.

## Assumptions and scope

The contact graph has vertices \(a,b,a_1,\dots,a_n,b_1,\dots,b_n\), with precisely the edges \(ab\), \(aa_j\), and \(bb_j\) for \(1\leq j\leq n\). All vertices represent individuals; neither the hubs nor the leaves carry weights. Infection begins simultaneously from two distinct vertices. Every infected vertex attempts transmission to each susceptible neighbor independently with probability \(p\), and recovers permanently after one time step; the process ends after all infections recover. The central seed set is deterministically \(\{a,b\}\). The uniform seed set is sampled uniformly without replacement from all unordered vertex pairs, independently of transmissions.

For this SIR(1) rule on an undirected graph, the eventual infected set is exactly the union of bond-percolation components meeting at least one initial seed. All expectations below include both edge-retention and, for the uniform strategy, seed-selection randomness. The statement concerns all integer \(n\geq1\), the full closed physical probability interval, and nothing about varying recovery periods, weighted contacts, additional seeds, or random graph topologies.

## Proof

**1. The central strategy.** Each hub is seeded and every leaf is infected precisely when its unique hub edge is retained. Consequently, by linearity of expectation, \(H_n(p)=2+2np\).

**2. A component counting identity.** Set \(N=2n+2\). In a fixed percolated graph, a connected component of size \(k\) receives at least one of two uniformly chosen distinct seeds with probability

\[
1-\frac{(N-k)(N-k-1)}{N(N-1)}.
\]

Its contribution to the conditional expected outbreak size is therefore

\[
h_N(k)=k\left(1-\frac{(N-k)(N-k-1)}{N(N-1)}\right)
=\frac{k^2(2N-1-k)}{N(N-1)}.
\]

Conditional on the edge configuration, summing \(h_N(k)\) over all connected components yields the uniformly seeded expected final size. This identity allows a closed calculation because \(h_N\) is cubic.

**3. The two possible component structures.** Let \(X,Y\) be independent \(\operatorname{Bin}(n,p)\) random variables, counting retained leaf edges on the respective sides. Let \(B\) indicate whether the hub-to-hub bridge is retained; \(B\sim\operatorname{Bernoulli}(p)\), independently of \(X,Y\).

If \(B=1\), one component has size \(2+X+Y\) and the remaining \(2n-X-Y\) components are isolated singletons. If \(B=0\), the hub components have sizes \(1+X\) and \(1+Y\), and the same number of isolated singleton leaves remain. Thus

\[
\begin{aligned}
U_n(p)={}&p\,\mathbb{E}[h_N(2+X+Y)+(2n-X-Y)h_N(1)]\\
&+(1-p)\,\mathbb{E}[h_N(1+X)+h_N(1+Y)
 +(2n-X-Y)h_N(1)].
\end{aligned}
\]

**4. Exact evaluation.** For \(Z\sim\operatorname{Bin}(k,p)\), its first three raw moments are

\[
\mathbb{E}Z=kp,\quad
\mathbb{E}Z^2=kp+k(k-1)p^2,\quad
\mathbb{E}Z^3=kp+3k(k-1)p^2+k(k-1)(k-2)p^3.
\]

Apply these identities to the preceding cubic expression, using \(X+Y\sim\operatorname{Bin}(2n,p)\). Collecting terms and subtracting from \(2+2np\) gives precisely the displayed boxed difference formula. The algebraic identity is also independently checked by explicit enumeration of the percolated graph and every seed pair for the first six values of \(n\); that finite check is corroboration, not the infinite-family proof.

**5. Sharp sign classification.** Let

\[
Q_n(p)=3n(n-1)p^2+(3n-1)p-4n^2+2n+2.
\]

For \(0<p<1\), the sign of \(H_n(p)-U_n(p)\) is the opposite of the sign of \(Q_n(p)\). When \(n=1\), \(Q_1(p)=2p>0\), proving strict uniform dominance. When \(n=2\), \(Q_2(p)=6p^2+5p-10\), a strictly increasing function on \([0,1]\) with opposite signs at the endpoints and unique root \((\sqrt{265}-5)/12\). When \(n\geq3\), \(Q_n\) is increasing on \([0,1]\), while

\[
Q_n(1)=2-(n-1)^2<0.
\]

Hence \(Q_n(p)<0\) throughout this interval and central seeding always dominates. The factors \(p(p-1)\) prove endpoint equality.

**6. Macroscopic comparison.** For fixed \(p\in(0,1)\), divide the exact difference by \(2n+2\), then divide numerator and denominator by the appropriate powers of \(n\). The quadratic term \(n^2(3p^2-4)\) in \(Q_n(p)\) gives the asserted positive limit \(p(1-p)(4-3p^2)/4\), since \(4-3p^2>0\) on the stated interval. This completes the proof.

## Verification

The standalone program `verification/bistar_verify.py` constructs each double-star graph without relying on the component-moment derivation. It enumerates every retained-edge subset and every unordered seed pair and then compares the exact symbolic outbreak difference with the theorem. It covers \(n=1,\ldots,6\), using \(10{,}920\) edge configurations and \(907{,}792\) edge-configuration/seed-pair cases. All differences simplify identically to zero. Run from the directory containing this document with `python verification/bistar_verify.py`; Python and SymPy are required. The program's finite checks do not establish the formula for unbounded \(n\), which is proved above through the binomial-moment identity.

## Relationship to prior work

Ódor, Czifra, Komjáthy, Lovász, and Karsai introduced and investigated central-versus-uniform epidemic-seeding switchover on geometric and random networks, using the bond-percolation interpretation of SIR(1) [1]. Their comparison gives the epidemiological motivation, but their model classes and main results do not state a complete exact double-star, fixed-two-seed threshold. Their follow-up overview discusses general seeding effects and sufficient conditions for switchover [2]. Keliger, Lovász, Móri, and Ódor establish weak switchover on certain general graphs and strong switchover under additional hypotheses [3]. Those hypotheses do not force a reversal on a two-hub tree with numerous pendant leaves: in particular, the double star has many degree-one edge cuts and the seed count here remains exactly two as the graph grows. The result above provides an exact boundary and a macroscopic no-switchover example not logically supplied by those sufficient theorems. It does not claim that the bond-percolation representation or the general phenomenon was first discovered here.

## Limitations

The result compares expectations and does not rank the complete outbreak-size distributions. It assumes exactly two simultaneous seeds, independent identical transmission along every edge, a one-step infectious period, and a deterministic two-hub double-star network. Its large-network gap is not asserted for a sequence of transmission parameters converging to one. The calculation is an exact characterization of this family, not a criterion for arbitrary sparse networks or a claim about real-world COVID-19 spread. Equivalent results in earlier work on finite influence maximization or tree percolation may be less readily discoverable; priority requires independent checking.

## References

[1] G. Ódor, D. Czifra, J. Komjáthy, L. Lovász, and M. Karsai, *Switchover phenomenon induced by epidemic seeding on geometric networks*, arXiv:2106.16070 (initial public submission 2021-06-30), later PNAS 118 (2021), e2112607118. https://arxiv.org/abs/2106.16070

[2] G. Ódor, D. Czifra, J. Komjáthy, L. Lovász, and M. Karsai, *Longer-term seeding effects on epidemic processes: a network approach*, Scientia et Securitas 2 (2022), 409–417. https://doi.org/10.1556/112.2021.00078

[3] D. Keliger, L. Lovász, T. F. Móri, and G. Ódor, *Switchover phenomenon for general graphs*, arXiv:2304.11971 (initial public submission 2023-04-24), later J. Graph Theory 108 (2025), 560–581. https://arxiv.org/abs/2304.11971
