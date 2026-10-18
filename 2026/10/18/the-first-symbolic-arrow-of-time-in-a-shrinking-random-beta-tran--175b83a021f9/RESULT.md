# The first symbolic arrow of time in a shrinking random beta transformation

## Finding
For each integer \(n\ge3\), let \(\lambda_n\in(1,2)\) be the unique solution of
\[
 2\sum_{k=2}^{n}\lambda_n^{-k}=1,
 \qquad q_{n,k}=2\lambda_n^{-k},\qquad
 \mu_n=\sum_{k=2}^{n} kq_{n,k}.
\]
Consider the stationary binary affine-branch digit process \((Z_j)_{j\in\mathbb Z}\) under the unique maximal-entropy measure for the shrinking random \(\beta_n\)-transformation of Jiang and Dajani, with the first-return coding specified below. A word \(w\) is reversed by reversing its symbol order, and \(p_n(w)=\Pr[(Z_0,\dots,Z_{|w|-1})=w]\).

**Theorem.** Every binary word of length at most four is time-reversal symmetric: \(p_n(w)=p_n(w^{\mathrm{rev}})\). At length five the symmetry is broken; in particular,
\[
 \Delta_n:=p_n(00010)-p_n(01000)
 =\frac{q_{n,2}-q_{n,2}^2-q_{n,3}}{8\mu_n}
 =-\frac{\lambda_n^{-(n+3)}}{2\mu_n}<0.
\]
Every reversal discrepancy for a five-symbol word is either zero or \(\pm\Delta_n\). Precisely eight unordered reversal pairs have a nonzero discrepancy. Thus the total-variation distance between the forward and reversed five-symbol distributions equals
\[
 \mathsf{TV}_{5,n}=8|\Delta_n|=\frac{4\lambda_n^{-(n+3)}}{\mu_n},
 \qquad \lim_{n\to\infty}2^n\mathsf{TV}_{5,n}=\frac16.
\]
In particular, for every finite \(n\ge3\), five is the shortest word length detecting time irreversibility in this stationary digit process, while the entire five-word arrow of time vanishes with an exact exponential leading constant as \(n\to\infty\).

## Assumptions and scope
For \(n\ge3\), let \(\beta_n\in(1,2)\) solve \(\beta_n^n=\sum_{j=0}^{n-2}\beta_n^j\). The shrinking random \(\beta_n\)-map, its two affine branches, and its maximal-entropy measure are as defined in Jiang and Dajani, *Shrinking random \(\beta\)-transformation* (2016). An induced orbit departing the switch region traverses a return path of length \(k\in\{2,\dots,n\}\), with two possible digit labels. The associated binary word is
\[
 B(b,k)=b(1-b)^{k-1},\qquad b\in\{0,1\}.
\]
This is the source's first-return symbolic coding. The observation \(Z_j\) is the **affine-branch digit at each ordinary unit-time iteration**, not the return-time digit or a digit sampled only at returns. All probabilities refer to the stationary maximal-entropy measure; they do not assert statements about Lebesgue initialization or other invariant measures. Endpoint coding ambiguities are null for this measure. At a return-section boundary, two paths of each length \(k\) are available. The Parry (Perron) probability of any such complete loop is \(\lambda_n^{-k}\), so return blocks \(B(b,k)\) are independent with probabilities \(q_{n,k}/2=\lambda_n^{-k}\). The digit process at ordinary times is the stationary length-biased suspension of these independent blocks.

## Proof
**1. Excursion weights and stationary time sampling.** The first-return graph has one distinguished return vertex and exactly two excursion paths of each length \(2\le k\le n\). The graph has Perron eigenvalue \(\lambda_n\), characterized by the renewal equation \(2\sum_{k=2}^n\lambda_n^{-k}=1\). Under its Parry measure, a path \(i_0,\dots,i_k\) with the same initial and terminal vertex has probability \(\lambda_n^{-k}\), conditional on starting at that vertex: the Perron eigenvector factors in the transition probabilities telescope. Successive excursions therefore form independent pairs \((b,k)\) of probabilities \(\lambda_n^{-k}\). The mean excursion length is \(\mu_n\).

The stationary unit-time probability of being at offset \(j\in\{0,\dots,k-1\}\) within an excursion of type \((b,k)\) is
\[
 \Pr\{(b,k,j)\}=\frac{q_{n,k}}{2\mu_n}.
\]
The output at \(j=0\) is \(b\), and at all later offsets it is \(1-b\). From these states one advances deterministically within the excursion, and at its end chooses a fresh \((b',k')\) with probability \(q_{n,k'}/2\). This defines an explicit stationary finite-state Markov realization of the complete observed process. The stationary law is invariant under the simultaneous flip of all binary labels \(b\mapsto1-b\).

**2. Two particular cylinder probabilities.** Write \(q_k=q_{n,k}\) and \(\mu=\mu_n\). Starting exactly at a new excursion, the probabilities of the auxiliary words \(010\), \(10\) and \(1000\), respectively, are
\[
 F(010)=\frac{q_2}{4},\qquad F(10)=\frac12,\qquad
 F(1000)=\frac{2-2q_2-q_3}{4}.
\]
These follow directly from the initial block \(b(1-b)^{k-1}\) and independent subsequent blocks. A first-excursion prefix of \(00010\) or \(01000\) is impossible. At an arbitrary stationary time, if the observed current symbol is zero and \(\ell\ge1\) symbols of its current excursion remain, the total mass for such starting offsets is \(\Pr(k\ge\ell+1)/(2\mu)\) (the exceptional excursion-start cases cannot realize the two patterns). For \(00010\), only residual lengths \(\ell=2,3\) contribute. For \(01000\), only residual length \(\ell=1\) contributes. Conditioning on the next fresh excursion gives
\[
 p_n(00010)=\frac{2-q_2-q_2^2-2q_3}{8\mu},\qquad
 p_n(01000)=\frac{2-2q_2-q_3}{8\mu}.
\]
Thus \(\Delta_n=(q_2-q_2^2-q_3)/(8\mu)\).

Since \(q_2=2\lambda_n^{-2}\), \(q_3=2\lambda_n^{-3}\), and the Perron equation implies
\[
 (\lambda_n-2)(\lambda_n+1)=-2\lambda_n^{-(n-1)},
\]
we obtain \(q_2-q_2^2-q_3=-4\lambda_n^{-(n+3)}\). This proves the strictly negative explicit discrepancy.

**3. No earlier asymmetry, and the complete five-word classification.** For an arbitrary stationary binary process invariant under simultaneous bit complementation, the length-\(m\) word probabilities satisfy two families of linear identities: for each word \(u\) of length \(m-1\),
\[
 \sum_{a\in\{0,1\}}p(au)=\sum_{a\in\{0,1\}}p(ua),
 \qquad p(w)=p(\overline w).
\]
The first is stationarity and the second is bit-flip symmetry. Elementary elimination of these linear constraints shows: (i) every reversal difference for lengths \(m\le4\) is zero; (ii) at length five the space of reversal-difference functionals modulo these identities is one-dimensional. One can verify the last finite algebra statement without any genericity assumption: order the \(2^m\) words lexicographically, put the displayed identities into a rational matrix, eliminate by exact row reduction, and check each vector \(e_w-e_{w^{\mathrm{rev}}}\) modulo the row span. The complete standard-library exact-arithmetic implementation is `verify.py`. Its rank at length five is \(23\), and it confirms the following exhaustive nonzero reversal pairs, with \(p_n(w)-p_n(w^{\mathrm{rev}})\) given relative to \(\Delta_n\):

| \(w\) | \(w^{\mathrm{rev}}\) | Difference |
|---|---|---|
| \(00010\) | \(01000\) | \(\Delta_n\) |
| \(00011\) | \(11000\) | \(-\Delta_n\) |
| \(00110\) | \(01100\) | \(-\Delta_n\) |
| \(00111\) | \(11100\) | \(\Delta_n\) |
| \(01001\) | \(10010\) | \(\Delta_n\) |
| \(01101\) | \(10110\) | \(-\Delta_n\) |
| \(10011\) | \(11001\) | \(\Delta_n\) |
| \(10111\) | \(11101\) | \(-\Delta_n\) |

The four other unordered nonpalindromic reversal pairs have zero difference. With \(32\) words, each unordered pair contributes twice its absolute difference in the defining sum \(\frac12\sum_w|p_n(w)-p_n(w^{\mathrm{rev}})|\), proving \(\mathsf{TV}_{5,n}=8|\Delta_n|\).

**4. Parameter-limit coefficient.** As \(n\to\infty\), the solutions \(\lambda_n\) increase to \(2\). The exact identity in Step 2 implies \(2-\lambda_n=2/[(\lambda_n+1)\lambda_n^{n-1}]\), hence \(n(2-\lambda_n)\to0\). Furthermore
\[
 \mu_n=2\sum_{k=2}^{n}k\lambda_n^{-k}\longrightarrow
 2\sum_{k=2}^{\infty}k2^{-k}=3.
\]
Consequently \(2^n\lambda_n^{-(n+3)}\to1/8\), giving \(2^n|\Delta_n|\to1/48\), and finally \(2^n\mathsf{TV}_{5,n}\to1/6\).

## Verification
Running `python verify.py` with a standard Python interpreter outputs `VERIFY_OK 434 rational word comparisons; reversal-constraint rank 23 ; 10 high-precision parameter identities`. The checker independently realizes the length-biased excursion suspension for seven arbitrary rational excursion-length distributions (length maxima three through nine), compares all words of lengths one through five against their reversals using exact fractions, verifies the five-word total variation formula, and performs exact row-span checks of the finite stationarity and complement identities. It also checks the defining Perron identity at ten parameters using high-precision decimal arithmetic. The finite computations do **not** prove the asymptotic assertion: the infinite step is supplied by the explicit Perron identity and dominated geometric-series argument above. The exact finite linear algebra is an exhaustive proof of the universal five-word elimination step, not statistical sampling.

## Relationship to prior work
Jiang and Dajani (2016) introduce this family, establish its return structure and unique maximal-entropy measure, and describe the graph/return-block model. The first-return coding and Parry measure used in Step 1 are antecedents, not original findings. Baker and Dajani (2015) investigate induced **ordinary** random beta transformations, distinct from this shrinking family. Arola-Fernández and Lacasa (2023) give general cautions about symbolic time irreversibility and show that stationary binary words shorter than four cannot detect it; this is weaker than the all-length-four reversal identity valid under complement symmetry here. The new, narrow contribution is the exact first nonreversible digit length, complete five-word discrepancy law, and shrinking-family exponential constant. No claim is made that the generic renewal identities, the Parry construction, or broad symbolic-irreversibility concepts were unknown.

## Limitations
The result concerns the binary affine-branch observation under the stationary maximal-entropy measure of the special \(\beta_n\) family, not all beta transformations or all invariant measures. Neither unconditioned physical-state time reversal nor arbitrary longer-word distributions are classified. Historical novelty is a documented best-knowledge assessment, not absolute priority certification: an earlier unindexed treatment of complement-symmetric renewal word reversal could imply the finite-state argument. No independent scientific audit has been performed.

## References
1. K. Jiang and K. Dajani, *Shrinking random \(\beta\)-transformation* (first arXiv submission 2016-02-17), arXiv:1602.05337, https://arxiv.org/abs/1602.05337.
2. S. Baker and K. Dajani, *Induced Random \(\beta\)-transformation* (2015), arXiv:1509.06194, https://arxiv.org/abs/1509.06194.
3. L. Arola-Fernández and L. Lacasa, *Irreversibility of symbolic time series: a cautionary tale* (2023), arXiv:2303.11868, https://arxiv.org/abs/2303.11868.
