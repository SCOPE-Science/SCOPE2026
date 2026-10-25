# Nilpotency-height rank profiles and a lattice extreme law for order-preserving partial isometries

## Finding
For every integer \(n\ge1\), let \(\mathcal O_n\) be the inverse monoid of all order-preserving partial isometries of the chain \([n]=\{1,\ldots,n\}\), with the empty map as zero. For a nilpotent element \(f\), let \(\nu(f)=\min\{j\ge1:f^j=0\}\), and define the rank-refined cumulative nilpotency polynomial
\[
H_{n,k}(z)=\sum_{\substack{f\in\mathcal O_n\\f\text{ nilpotent},\ \nu(f)\le k}}z^{|\operatorname{Dom}f|}\qquad(k\ge1).
\]
For integers \(\ell\ge0\) and \(k\ge1\), define \(R_{\ell,k}(z)\) through the explicit rational generating function
\[
\sum_{\ell\ge0}R_{\ell,k}(z)t^\ell
=\frac{\sum_{j=0}^{k-1}(zt)^j}{1-t\sum_{j=0}^{k-1}(zt)^j}.
\]
Then, writing \(n-d=q_dd+r_d\), where \(0\le r_d<d\), the complete joint rank–nilpotency-height distribution is
\[
\boxed{H_{n,k}(z)=1+2\sum_{d=1}^{n-1}\left(R_{q_d+1,k}(z)^{r_d}R_{q_d,k}(z)^{d-r_d}-1\right).}
\]
Thus the exact number of nilpotent maps of rank \(r\) and least zero power **equal** to \(k\) is \([z^r](H_{n,k}(z)-H_{n,k-1}(z))\) for \(k\ge2\), with the empty map at \((r,k)=(0,1)\). The number of nilpotents, recovered at \(k=n\), is the previously known \(2^{n+1}-2n-1\).

There is also a sharp lattice extreme law. If \(F_n\) is uniformly selected from all nilpotents of \(\mathcal O_n\), and integer sequences \(k_n\) satisfy \(n2^{-k_n}\to\theta\) for some \(0<\theta<\infty\), then
\[
\boxed{\lim_{n\to\infty}\Pr\bigl(\nu(F_n)\le k_n\bigr)=\exp(-\theta/2).}
\]
Consequently \(\nu(F_n)-\log_2 n=O_{\mathbb P}(1)\), and in particular \(\nu(F_n)/\log_2n\to1\) in probability. This is a lattice limit, not a claim of an unqualified nonlattice Gumbel weak limit.

## Assumptions and scope
All sets are finite and \(n\ge1\). A partial map \(f:S\to[n]\) is an order-preserving isometry when it is strictly order preserving on \(S\) and preserves the distance between every pair of domain points. Each nonempty such map is uniquely a partial translation \(f(x)=x+a\) for one integer displacement \(a\) and a nonempty subset \(S\subseteq[n]\cap([n]-a)\). Every nonempty displacement-zero map is a partial identity and is not nilpotent. Every nonempty map with \(a\ne0\) is nilpotent. The empty map is a single monoid element, independent of displacement, and has \(\nu=1\). Rank always means domain cardinality (equivalently image cardinality).

## Proof
**Partial translations and chains.** For \(x<y\) in the domain, order-preserving isometry gives \(f(y)-f(x)=y-x\), so \(f(x)-x\) is constant. If its displacement is nonzero, iterated translations eventually leave the finite chain, so the map is nilpotent; when the displacement is zero a nonempty map is idempotent and not nilpotent. Reflection \(x\mapsto n+1-x\) exchanges displacements \(d\) and \(-d\) without altering rank or least zero power.

Fix a positive displacement \(d\). Its admissible domain is \([n-d]\), and a map is exactly the choice of a binary support mask \(S\subseteq[n-d]\). Partition these \(n-d\) positions into residue-class chains modulo \(d\); there are \(r_d\) chains of length \(q_d+1\) and \(d-r_d\) chains of length \(q_d\) (possibly zero). A nonzero \(j\)-th power is present precisely when the mask has a run of at least \(j\) consecutive ones in one of these chains. In particular, if \(L\) is the maximum run length, \(\nu=L+1\), with \(L=0\) for the empty mask.

**Forbidden-run polynomial.** A binary word with no run of \(k\) ones has a unique decomposition into zero or more blocks consisting of \(j\in\{0,\ldots,k-1\}\) ones followed by one zero, plus a final block of at most \(k-1\) ones. Weight a one by \(z\) and a letter by \(t\). The nonterminal blocks contribute \(t\sum_{j=0}^{k-1}(zt)^j\); the terminal block contributes \(\sum_{j=0}^{k-1}(zt)^j\). Summing the geometric series gives the displayed rational series for \(R_{\ell,k}(z)\). Independence of the residue chains gives the product for each displacement. Removing its one empty mask, doubling for both signs, and restoring the unique zero map proves \(H_{n,k}(z)\). With \(k=n\), all masks are admitted; summing \(2^{n-d}-1\) over positive displacements gives \(2^{n+1}-2n-1\).

**Limit law for a fixed displacement.** For fixed \(d\ge1\), select the mask uniformly from all \(2^{n-d}\) masks for displacement \(d\), temporarily including the empty one. Assume \(n2^{-k_n}\to\theta\in(0,\infty)\), so \(k_n=\log_2n+O(1)\). In each residue chain, mark every position at which a run of \(k_n\) ones begins, provided it is the chain's first position or the immediately preceding bit is zero. Let \(W_n\) be the total number of such marked starts. Then \(\{\nu\le k_n\}=\{W_n=0\}\).

For a start away from the first position, its indicator has expectation \(2^{-(k_n+1)}\); a first-position start has expectation \(2^{-k_n}\). There are \(n+O(dk_n)\) eligible starts and only \(d\) boundary starts, whence \(\mathbb EW_n\to\theta/2\). Starts on the same residue chain separated by at most \(k_n\) are incompatible (the later preceding zero would fall in the earlier run). Starts separated by at least \(k_n+1\), or on distinct chains, inspect disjoint bits and are independent. For every fixed positive integer \(h\), the number of ordered \(h\)-tuples of starts involving two positions separated by at most \(k_n\) is \(O_h(n^{h-1}k_n)\); their joint expectation is zero. Removing these tuples and the \(O_h(dn^{h-1})\) tuples containing boundary starts leaves \(n^h(1+o(1))\) independent interior tuples, each with joint probability \(2^{-h(k_n+1)}\). Thus \(\mathbb E(W_n)_h\to(\theta/2)^h\) for all \(h\), so by factorial moments \(W_n\) converges to a Poisson variable of mean \(\theta/2\). Hence \(\Pr(\nu\le k_n)\to e^{-\theta/2}\) for each fixed \(d\).

**Mixing displacements.** Among the nonzero nilpotents, the absolute displacement \(D_n\) takes value \(d\in\{1,\ldots,n-1\}\) with weight \(2(2^{n-d}-1)\). The zero map has probability \((2^{n+1}-2n-1)^{-1}\to0\). For each fixed \(d\), \(\Pr(D_n=d)\to2^{-d}\); moreover \(\Pr(D_n>M)\le C2^{-M}\) for an absolute constant \(C\) and sufficiently large \(n\). Conditioned on a nonzero shift of magnitude \(d\), the mask is uniform among nonempty supports, whose exclusion from the full binary model has vanishing probability. Truncate the mixture at \(M\), apply the fixed-displacement limit, and let \(M\to\infty\). The same limit \(e^{-\theta/2}\) follows for the uniform nilpotent ensemble.

The upper-tail union bound \(\Pr(\nu(F_n)>k)\le Cn2^{-k}+o(1)\) follows by summing over possible runs for every displacement. For lower tails, taking \(k=\lfloor\log_2n\rfloor-J\) with fixed \(J\), the lattice-limit result along convergent subsequences of \(n2^{-k}\in[2^J,2^{J+1}]\) yields \(\limsup\Pr(\nu(F_n)\le k)\le\exp(-2^{J-1})\). Sending \(J\to\infty\) establishes tightness of \(\nu-\log_2 n\) and the ratio conclusion.

## Verification
The included standalone Python checker enumerates all nonzero signed partial translations for \(1\le n\le11\), computes powers by direct partial-map composition, and compares every rank coefficient of each cumulative polynomial with an independent trailing-one finite-state dynamic program. It checks \(8045\) distinct nilpotents in total. It also evaluates the exact cumulative formula at \(n=128,256,512,1024,2048,4096\) along \(k=\log_2 n\) and confirms numerical convergence to \(e^{-1/2}\). Run `python checks/check_odp_nilpotency.py` from the package root using Python 3 standard library. These finite checks corroborate, but do not prove, the infinite asymptotic statement; the proof is above.

## Relationship to prior work
Order-preserving partial isometries and their translation structure were studied by Al-Kharousi, Kehinde and Umar (2014, 2016). Ali, Jada and Zubairu (2018/2019), in particular their Proposition 2.5 and Theorem 2.6, count nilpotents and analyze the subsemigroup they generate, rather than the least-power filtration refined simultaneously by domain rank. OEIS A183155 already gives the total count and OEIS A183153 gives the unrefined rank census of all order-preserving partial isometries; these are recovered or respected, not asserted to be new. The longest-run extreme approximation itself is classical (Gordon, Schilling and Waterman; and later analyses including Konstantopoulos, Liu and Yang), and is credited accordingly. The contribution here is the exact semigroup-specific two-parameter filtration and the proof that mixing the displacement preserves the sharp lattice extreme law.

## Limitations
The theorem concerns order-preserving partial **isometries**, not all injective order-preserving maps, arbitrary partial contractions, or order-reversing isometries. The asymptotic law is for uniform sampling among nilpotents, not sampling only a prescribed displacement growing with chain size. Existing general results about longest Bernoulli runs are not independently reproved beyond the elementary factorial-moment argument needed here. Equivalent priority under different terminology (partial translations, powers, height filtration) has not been excluded with certainty; a 2014 combinatorial paper and 2016 foundational semigroup paper were not fully accessible during the comparison, though the 2019 full text on nilpotents was inspected. No claim is made that the total nilpotent count or the Bernoulli longest-run law is new.

## References
1. B. Ali, M. A. Jada and M. M. Zubairu, *On the ranks of certain semigroups of order-preserving partial isometries of a finite chain*, Journal of Algebra and Related Topics 6(2), 15–33 (2018 volume; author-uploaded 5 April 2019). DOI: 10.22124/JART.2019.10875.1109. https://www.researchgate.net/publication/332080181_On_the_ranks_of_certain_semigroups_of_order_preserving_partial_isometries_of_a_finite_chain
2. F. Al-Kharousi, R. Kehinde and A. Umar, *Combinatorial results for certain semigroups of partial isometries of a finite chain*, Australasian Journal of Combinatorics 58(3), 365–375 (2014). https://squ.elsevierpure.com/en/publications/combinatorial-results-for-certain-semigroups-of-partial-isometrie/
3. F. Al-Kharousi, R. Kehinde and A. Umar, *On the semigroup of partial isometries of a finite chain*, Communications in Algebra 44(2), 639–647 (2016). DOI: 10.1080/00927872.2014.984838. https://arxiv.org/abs/1101.0049
4. C. Namnak, E. Laysirikul and N. Sawatraksa, *Natural Partial Order on the Semigroups of Partial Isometries of a Finite Chain*, Thai Journal of Mathematics, 97–108 (public page dated 16 May 2023). https://thaijmath.com/index.php/thaijmath/article/view/760
5. OEIS A183153, rank census; and A183155, zero-fixed-point/total nilpotent count. https://oeis.org/A183153 ; https://oeis.org/A183155
6. L. Gordon, M. F. Schilling and M. S. Waterman, *An extreme value theory for long head runs*, Probability Theory and Related Fields 72, 279–287 (1986). DOI: 10.1007/BF00699107.
7. T. Konstantopoulos, Z. Liu and X. Yang, *Laplace transform asymptotics and large deviation principles for longest success runs in Bernoulli trials*, Journal of Applied Probability 53 (2016). https://arxiv.org/abs/1507.02935
