# Parity-separated near-complete cycle-cohesion tails in uniform permutations

## Finding
Let \(\Pi_n\) be a uniformly random permutation of \(\{1,\ldots,n\}\), represented by its disjoint cycles. Define its **cycle-boundary count**
\[
D_n=\sum_{i=1}^{n-1}\mathbf 1\{i\text{ and }i+1\text{ belong to different cycles of }\Pi_n\}.
\]
For each fixed nonnegative integer \(d\), as \(n\to\infty\),
\[
\boxed{\Pr(D_n=d)=\begin{cases}
 n^{-1}+O_d(n^{-2}),&d\text{ even},\\
 (d+1)n^{-2}+O_d(n^{-3}),&d\text{ odd}.
\end{cases}}
\]
The high-cohesion tail therefore alternates between two distinct polynomial orders. In particular, for every fixed \(k\ge0\),
\[
\lim_{n\to\infty}n\Pr(D_n=2k)=1,\qquad
\lim_{n\to\infty}n^2\Pr(D_n=2k+1)=2k+2.
\]
A finite exact run-composition formula, stated below, determines the entire distribution of \(D_n\) for every \(n\ge1\).

## Assumptions and scope
A cycle is a block of the cycle partition of a permutation; the cyclic ordering *inside* the block is irrelevant to \(D_n\). A boundary is between consecutive **labels**, not successive positions in one-line notation and not consecutive neighbors along a cycle. Here \(0\le D_n\le n-1\). All asymptotic error constants may depend on the fixed integer \(d\); no uniformity is claimed when \(d\) grows with \(n\). The model is the ordinary uniform permutation, equivalently the Ewens partition with parameter one, without conditioning on its number of cycles.

For integers \(r\ge1\), let \(\mathcal P_r\) be the set of partitions \(\mathcal B\) of \(\{1,\ldots,r\}\) in which adjacent integers lie in distinct blocks. For \(1\le r\le n\),
\[
 n!\Pr(D_n=r-1)=
 \sum_{\substack{\ell_1,\ldots,\ell_r\ge1\\\ell_1+\cdots+\ell_r=n}}
 \quad\sum_{\mathcal B\in\mathcal P_r}
 \prod_{B\in\mathcal B}\left(\sum_{j\in B}\ell_j-1\right)!.
\]
The formula uses ordinary factorials, with \(0!=1\). If \(r>n\), the probability is zero.

## Proof
**Exact enumeration.** Read the consecutive labels \(1,\ldots,n\) from left to right, recording the cycle containing each label. A permutation with \(D_n=r-1\) has exactly \(r\) maximal monochromatic runs, with lengths \(\ell_1,\ldots,\ell_r\). Equal cycle identifiers may recur at nonadjacent runs, but adjacent runs have different identifiers. The equality pattern of cycle identifiers is uniquely a partition \(\mathcal B\in\mathcal P_r\). A block \(B\) of that partition contains \(s_B=\sum_{j\in B}\ell_j\) labels and can be made into a single permutation cycle in exactly \((s_B-1)!\) ways. Distinct cycles can be ordered independently. Summing over the uniquely determined run data proves the formula.

**Asymptotic domination.** Fix \(r\) and consider an individual summand in this formula. Write \(m\) for the largest cycle-block size, and \(s=n-m\). There are at most \(B_r\binom{n-1}{r-1}=O_r(n^{r-1})\) choices of composition and allowable set partition, where \(B_r\) is a fixed Bell number. Since there are at most \(r\) cycles, \(m\ge n/r\).

If \(m\le n/2\), the product of the cycle factorials is at most \(m!(n-m)!\), hence the normalized weight is at most \(\binom nm^{-1}\). Uniformly for \(n/r\le m\le n/2\), this is exponentially small in \(n\) (for \(r=1\), this case is empty). Thus this whole class is exponentially negligible, even after summing the polynomial number of possible run data.

If \(m>n/2\), then \(s<n/2\). A summand has normalized weight at most
\[
 \frac{(m-1)!s!}{n!}=\frac1{m\binom ns}.
\]
For \(s\ge r+5\), monotonicity of \(\binom ns\) up to the midpoint bounds the sum of all such terms by \(O_r(n^{-7})\). It remains to handle the finitely many possibilities \(0\le s\le r+4\).

Suppose the large cycle occupies \(t\) of the \(r\) runs. Because adjacent runs cannot belong to the same cycle,
\(t\le\lceil r/2\rceil\). Every other run has positive length, so \(s\ge r-t\). With \(s\) fixed, the lengths of the other runs admit only \(O_r(1)\) choices, while distributing \(n-s\) labels among the \(t\) large-cycle runs gives \(O_r(n^{t-1})\) choices. The number of permutations on the \(s\) exceptional labels is at most \(s!\), and the large cycle has exactly \((n-s-1)!\) cyclic orders. The resulting contribution has order at most
\[
 O_r\bigl(n^{t-s-2}\bigr).
\]

**Even boundary count.** Set \(r=2k+1\). Then \(t\le k+1\), \(s\ge2k+1-t\). The only way to attain order \(n^{-1}\) is \(t=k+1\), \(s=k\). Necessarily the large cycle fills exactly the odd-numbered runs and every even-numbered run is one exceptional label. Conversely every such configuration contributes, irrespective of the cycle partition among those exceptional labels. Its exact count is
\[
 k!\binom{n-k-1}{k}(n-k-1)!.
\]
All remaining run configurations are \(O_k(n^{-2})\) in probability. Dividing the displayed count by \(n!\) proves \(\Pr(D_n=2k)=n^{-1}+O_k(n^{-2})\), including \(k=0\), where it is exactly \(1/n\).

**Odd boundary count.** Set \(r=2k+2\). Now \(t\le k+1\) and \(s\ge2k+2-t\). The only order-\(n^{-2}\) case is \(t=s=k+1\). The large cycle occupies every other run; there are two choices of alternation, and every other run is one exceptional label. These configurations contribute exactly
\[
 2(k+1)!\binom{n-k-2}{k}(n-k-2)!.
\]
All other contributions are \(O_k(n^{-3})\) in probability. Dividing by \(n!\) gives \(2(k+1)n^{-2}+O_k(n^{-3})\). Both cases establish the theorem.

## Verification
The attached standalone Python checker independently enumerates each permutation for \(1\le n\le8\), extracts its cycle partition, counts label boundaries, and compares the counts for **every** boundary value with a second computation using the exact run-composition/set-partition formula. There were 36 exact comparisons. It also evaluates 16 parity-scaled cases for \(n=12,20,30,50\) and \(d=0,1,2,3\), giving 52 checks in total; all passed. For \(n=8\), the exact count vector for \(d=0,\ldots,7\) was \((5040,1812,6042,5539,7744,7134,5102,1907)\), summing to \(8!\). The error estimates and infinite limits follow from the proof above, not from those finite calculations. Reproduce with `python3 checker.py` using the Python standard library.

## Relationship to prior work
Classical Ewens sampling identifies the probability weight of a cycle partition as proportional to the product of factorials of block sizes minus one. Munagi studied successions **within ordinary set partitions** and their unweighted enumeration. Brualdi and Deutsch counted entire cycles supported on consecutive labels; Mansour and Shattuck counted consecutive elements adjacent **within cyclic order**. None of these is the present boundary statistic: two consecutive labels in the same cycle need not be consecutive within that cycle, and the cycle partition here carries factorial weights. The present claim is the sharp fixed-boundary asymptotic and its even/odd order separation, not an assertion that the unweighted succession enumeration or the Ewens partition formula is new.

## Limitations
Only fixed-deficit tails for uniform permutations are covered. The result does not describe the central distribution of the boundary statistic, Ewens parameters other than one, cyclic wrap-around boundaries, or a regime where \(d\) increases with \(n\). The high-cohesion event is not a statement about adjacency within a cycle's cyclic ordering. Exhaustive finite checks provide reproducibility, not an infinite proof. Earlier weighted-partition literature not located during the comparison could potentially contain an equivalent theorem.

## References
1. W. J. Ewens, *The sampling theory of selectively neutral alleles*, Theoretical Population Biology **3** (1972), 87–112.
2. A. O. Munagi, *Set partitions with successions and separations*, International Journal of Mathematics and Mathematical Sciences (2005), 451–463. DOI: 10.1155/IJMMS.2005.451.
3. A. O. Munagi, *Extended set partitions with successions*, European Journal of Combinatorics **29** (2008), 1298–1308. DOI: 10.1016/j.ejc.2007.06.003.
4. R. A. Brualdi and E. Deutsch, *Adjacent q-Cycles in Permutations*, arXiv:1005.0781 (first posted 13 May 2010).
5. T. Mansour and M. Shattuck, *Counting permutations by the number of successions within cycles*, Discrete Mathematics **339** (2016), 1368–1376. DOI: 10.1016/j.disc.2015.12.004.
