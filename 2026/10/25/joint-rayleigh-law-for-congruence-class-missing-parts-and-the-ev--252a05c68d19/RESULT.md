# Joint Rayleigh law for congruence-class missing parts and the even partition companion

## Finding

Let \(p(n)\) be the number of ordinary (unrestricted) partitions of \(n\). For a partition \(\lambda\) of \(n\), write \(M_r(\lambda)\) for the least **positive** part absent from \(\lambda\) and congruent to \(r\pmod h\). Here \(h\ge1\) is fixed and \(0\le r<h\).

For a uniform random partition \(\lambda\) of \(n\), the joint convergence
\[
 (n^{-1/4}M_0,\ldots,n^{-1/4}M_{h-1})
 \ \xrightarrow{d}\ (X_0,\ldots,X_{h-1})
\]
holds, where the limit coordinates are independent and satisfy
\[
 \Pr(X_r>x)=\exp\!\left(-\frac{\pi x^2}{2h\sqrt6}\right),\qquad x\ge0.
\]
For each fixed nonempty \(R\subseteq\{0,\ldots,h-1\}\), the first missing positive part whose residue is in \(R\) belongs to each residue class of \(R\) with asymptotic probability \(1/|R|\), and its value divided by \(n^{1/4}\) has survival limit
\[
 \exp\!\left(-\frac{|R|\pi x^2}{2h\sqrt6}\right).
\]

As a concrete consequence of Andrews and El Bachraoui's exact partition interpretations, let \(a_e(n)\) count partitions whose first missing part not congruent to \(1\pmod4\) is congruent to \(3\pmod4\). Let \(b_e(n)\) count overpartitions whose largest part is even and not overlined, whose odd parts are distinct, and for which only even parts may be overlined. Their even-companion coefficient is \(t_e(n)\). Then as \(n\to\infty\),
\[
 a_e(n)=b_e(n)\sim\frac{p(n)}3
 \sim\frac{\exp(\pi\sqrt{2n/3})}{12\sqrt3\,n},
 \qquad t_e(n)\sim\frac{2p(n)}3.
\]

## Assumptions and scope

Partitions are ordinary multisets of positive integer parts, with no restriction on multiplicities. A part is *absent* if its multiplicity is zero. The modulus \(h\) and all chosen residues are fixed independently of \(n\). Each \(M_r\) exists for every finite partition. The joint statement is convergence in distribution, not independence at finite \(n\). For the even-companion consequence, \(a_e,b_e,t_e\) are the statistics defined in the June 2026 paper, rather than arbitrary similarly named series.

## Proof

**1. Exact multivariate survival count.** Fix real \(x_r\ge0\) for \(0\le r<h\), put \(k_r=\lfloor x_r n^{1/4}\rfloor\), and define
\[
 T_n=\sum_{r=0}^{h-1}\ \sum_{\substack{1\le j\le k_r\\j\equiv r\pmod h}}j.
\]
The event \(M_r>k_r\) for *every* \(r\) says that every positive part appearing in the inner sums occurs at least once. Removing one obligatory copy of each such part is a bijection with ordinary partitions of \(n-T_n\). Consequently the **exact** joint survival probability is
\[
 \Pr_n\{M_r>k_r\ \text{for all }r}=\frac{p(n-T_n)}{p(n)}
\]
whenever \(n\ge T_n\); set \(p(v)=0\) for \(v<0\).

**2. Arithmetic-progression summation.** Uniformly for fixed \(h\),
\[
 \sum_{\substack{1\le j\le k\\j\equiv r\pmod h}}j
 =\frac{k^2}{2h}+O_h(k+1).
\]
With \(k_r=\lfloor x_r n^{1/4}\rfloor\) this gives
\[
 T_n=\frac{\sqrt n}{2h}\sum_{r=0}^{h-1}x_r^2+O_{h,\mathbf x}(n^{1/4}+1).
\]

**3. Uniform partition-ratio estimate.** The classical Hardy–Ramanujan formula is
\[
 p(v)=\frac{\exp(\pi\sqrt{2v/3})}{4v\sqrt3}\,(1+O(v^{-1/2}))
\]
for positive integers \(v\to\infty\). For \(T=O(\sqrt n)\), a Taylor expansion of the square root and the prefactor yields
\[
 \frac{p(n-T)}{p(n)}
 =\exp\!\left(-\frac{\pi T}{\sqrt{6n}}+O(n^{-1/2})\right).
\]
Substitution of the displayed asymptotic for \(T_n\) proves
\[
 \lim_{n\to\infty}\Pr_n\{n^{-1/4}M_r>x_r\ \text{for all }r}
 =\prod_{r=0}^{h-1}\exp\!\left(-\frac{\pi x_r^2}{2h\sqrt6}\right).
\]
The right-hand side is the multivariate survival function of independent, continuously distributed Rayleigh-type variables. It determines the joint weak limit; the marginal variables have no atoms, including at zero.

**4. Competing residues and the even companion.** The distinct residue-class minima \(M_r\) cannot tie at finite \(n\), since their values lie in disjoint congruence classes. The limiting vector has almost surely no equal coordinate, and its coordinates are independent and identically distributed. The continuous-mapping theorem therefore gives a uniform limiting winning residue on any fixed nonempty set \(R\), as well as the displayed minimum survival law. For \(h=4\) and \(R=\{0,2,3\}\), the winner \(3\) is exactly the event counted by \(a_e(n)\), so \(a_e(n)/p(n)\to1/3\). Andrews and El Bachraoui prove the exact identities \(a_e(n)=b_e(n)=t_e(n)/2\). Combining these with Hardy–Ramanujan proves the claimed three asymptotics.

## Verification

The standalone `verify.py` uses only standard-library exact integer arithmetic. It checks the finite-partition coefficient identities via independent generating-function calculations, verifies the even-companion overpartition interpretation for small sizes, and reports representative ratios. Run `python3 verify.py` and require `VERIFY_OK`. Such finite checks are consistency tests; the all-\(n\) conclusion depends on the exact bijection and classical partition asymptotics above.

## Relationship to prior work

Andrews and El Bachraoui (2026), Section 3 and Theorem 4, introduce \(a_e(n)\), \(b_e(n)\), and \(t_e(n)\), and prove their exact equality relations. They do not give the limiting density \(1/3\) or a joint congruence-class missing-part law. Wagner's single least-gap asymptotics (2011) concern one minimal missing part; his restricted-partition examples choose partitions *from a restricted allowed-part set*, not unrestricted partitions tracked simultaneously across residues. Chern and Xia (2025) develop moments of generalized minimal excludants, including single congruence-class statistics, but the relevant theorems do not state a joint independence limit for the full residue vector. Classical partition asymptotics provide the analytic input; the multivariate exact survival bijection connects the coordinates.

## Limitations

The modulus must stay fixed in the stated theorem; no growing-modulus uniformity, effective convergence rate for competing-residue probabilities, or exact finite-\(n\) independence is asserted. More general multiparameter partition-statistics methods could imply the limit indirectly; priority for the particular joint law is therefore subject to broader bibliographic review.

## References

1. G. E. Andrews and M. El Bachraoui, *On a two-color partition series and its companions*, arXiv:2606.30208v1 (June 29, 2026), especially Definition 1, Theorem 4, and Section 9; https://arxiv.org/abs/2606.30208.
2. S. Chern and E. X. W. Xia, *Asymptotics for moments of the minimal partition excludant in congruence classes*, arXiv:2507.14431v1 (July 19, 2025); https://arxiv.org/abs/2507.14431.
3. S. Wagner, *On the distribution of the smallest missing part in partitions*, Ramanujan Journal, DOI: 10.1007/s11139-010-9264-z (2011).
4. G. H. Hardy and S. Ramanujan, classical asymptotic partition formula (1918), as stated in standard references on integer partitions.
