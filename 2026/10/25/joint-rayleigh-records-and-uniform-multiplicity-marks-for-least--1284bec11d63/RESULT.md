# Joint Rayleigh records and uniform multiplicity marks for least partition gaps

## Finding

Let \(\lambda\) be uniformly distributed over the \(p(n)\) ordinary integer partitions of \(n\). Let \(\mu_\lambda(k)\) denote the number of occurrences of the part \(k\). For each fixed positive integer \(r\), put
\[
M_r=\min\{k\ge1:\mu_\lambda(k)<r\},\qquad c=\frac{\pi}{\sqrt6}.
\]
For fixed positive integers \(r_1,\ldots,r_t\), the vector of rescaled least multiplicity gaps has the joint limit
\[
\bigl(n^{-1/4}M_{r_i}\bigr)_{i=1}^t\ \Longrightarrow\
\left(\min_{0\le j<r_i}T_j\right)_{i=1}^t,
\]
where \(T_0,T_1,\ldots\) are independent with \(\Pr(T_j>x)=\exp(-cx^2/2)\) for \(x\ge0\). Equivalently, for every \(x_1,\ldots,x_t\ge0\), the joint upper-orthant survival limit is
\[
\exp\left(-c\int_0^\infty u\max(\{r_i:u\le x_i\}\cup\{0\})\,du\right).
\]
This law is generally **not independent** across thresholds. It has positive mass on coordinate-equality diagonals.

For fixed \(s\ge1\), let \(J_s=\mu_\lambda(M_s)\in\{0,\ldots,s-1\}\). Then
\[
\bigl(n^{-1/4}M_s,J_s\bigr)\ \Longrightarrow\ (Y_s,U_s),
\]
where \(Y_s=\min_{0\le j<s}T_j\) and \(U_s\) is uniform on \(\{0,\ldots,s-1\}\), independent of \(Y_s\). In particular, for every fixed \(1\le r<s\),
\[
\lim_{n\to\infty}\Pr(M_r=M_s)=\frac rs.
\]
The number \(B_s=\#\{1\le r\le s:M_r=M_s\}=s-J_s\) consequently tends to the uniform distribution on \(\{1,\ldots,s\}\).

## Assumptions and scope

All partitions are unrestricted ordinary partitions of an integer \(n\ge0\), with equal probability. The parameters \(s,t,r_1,\ldots,r_t\) are fixed as \(n\to\infty\); no assertion is made for thresholds growing with \(n\). Write \(p(k)=0\) for negative integers \(k\), and \(p(0)=1\). Limits of variables with continuous coordinates are understood as weak convergence; the stated exact equality-probability limit is proved separately rather than inferred solely from weak convergence.

## Proof

**1. Exact multivariate survivor.** For integers \(L_i\ge0\), the event \(M_{r_i}>L_i\) means that the multiplicity of each part \(k\le L_i\) is at least \(r_i\). Put \(L_*=\max_i L_i\) and \(a_k=\max(\{r_i:k\le L_i\}\cup\{0\})\). Removing \(a_k\) mandatory copies of every part \(k\le L_*\) is a bijection onto the partitions of
\[
n-H,\qquad H=\sum_{k=1}^{L_*} k a_k.
\]
Consequently the **exact** formula is
\[
\Pr(M_{r_i}>L_i\text{ for every }i)=\frac{p(n-H)}{p(n)}.
\tag{1}
\]
This includes contradictory or vacuous boundary choices under the convention \(p(v)=0\) for \(v<0\).

**2. Joint scaling limit.** The Hardy–Ramanujan formula with its classical relative error gives, uniformly for integers \(0\le h\le K\sqrt n\) and fixed \(K\),
\[
\frac{p(n-h)}{p(n)}=\exp\left(-\frac{ch}{\sqrt n}\right)(1+o(1)).
\tag{2}
\]
For \(L_i=\lfloor x_i n^{1/4}\rfloor\), \(H=O(\sqrt n)\). With \(k/n^{1/4}\) as the Riemann variable,
\[
\frac H{\sqrt n}\longrightarrow\int_0^\infty u\max(\{r_i:u\le x_i\}\cup\{0\})\,du.
\tag{3}
\]
Using (1)–(3) gives the advertised joint survival function. If \(T_j\) are independent with \(\Pr(T_j>x)=e^{-cx^2/2}\), then the joint survivor of \(\min_{0\le j<r_i}T_j\) is
\[
\exp\left[-\frac c2\sum_{j=0}^{\max_i r_i-1}
\left(\max(\{x_i:r_i>j\}\cup\{0\})\right)^2\right].
\]
This equals the preceding expression because the maximum-valued integer step function in (3) is the sum of its superlevel indicators. Since the limiting coordinates have continuous marginals, convergence of all these upper-orthant probabilities establishes weak joint convergence. Identical threshold ranks may simply be repeated.

**3. Exact mark count.** Fix \(s\ge1\), \(m\ge1\), and \(0\le j<s\). The event \(M_s=m\) and \(J_s=j\) forces \(s\) copies of each part below \(m\), exactly \(j\) copies of \(m\), and imposes no restrictions on parts above \(m\). If \(A=s m(m-1)/2+j m\), coefficient extraction from
\[
q^A(1-q^m)\prod_{k\ge1}(1-q^k)^{-1}
\]
therefore gives
\[
\Pr(M_s=m,J_s=j)=\frac{p(n-A)-p(n-A-m)}{p(n)}.
\tag{4}
\]
Summing (4) over \(0\le j<s\) telescopes to the known single-threshold mass \((p(n-s m(m-1)/2)-p(n-s m(m+1)/2))/p(n)\).

**4. Marked local limit.** For fixed \(0<\varepsilon<K\) and \(m\in[\varepsilon n^{1/4},K n^{1/4}]\), put \(x=m/n^{1/4}\). The uniform Hardy–Ramanujan expansion yields
\[
\frac{p(n-A)}{p(n)}=e^{-csx^2/2}(1+o(1))
\]
and
\[
1-\frac{p(n-A-m)}{p(n-A)}=cx\,n^{-1/4}+o(n^{-1/4}),
\]
with both errors uniform in that compact range and in the finitely many marks \(j\). Thus (4) gives the **uniform marked local limit**
\[
n^{1/4}\Pr(M_s=m,J_s=j)\longrightarrow cx\exp(-csx^2/2).
\tag{5}
\]
For any interval \([a,b]\subset(0,\infty)\), summing (5) gives
\[
\Pr(a\le n^{-1/4}M_s\le b,J_s=j)\longrightarrow
\int_a^b cx\exp(-csx^2/2)\,dx.
\tag{6}
\]
The exact tail identity \(\Pr(M_s>L)=p(n-sL(L+1)/2)/p(n)\) controls mass below a small positive \(a\) and above a large finite \(b\). Sending \(a\downarrow0\), \(b\uparrow\infty\), the integral (6) has total mass \(1/s\) for each \(j\), proving the uniform mark and independence from the limiting location, whose density is \(scx e^{-csx^2/2}\).

**5. Exact equality mechanism.** If \(M_s=m\), all part sizes below \(m\) have multiplicity at least \(s\). For fixed \(r<s\), therefore
\[
\{M_r=M_s\}=\{J_s<r\}.
\tag{7}
\]
The limiting uniformity of \(J_s\) yields \(\Pr(M_r=M_s)\to r/s\). Also \(M_r=M_s\) holds among \(1\le r\le s\) precisely for \(r>J_s\), so \(B_s=s-J_s\) has the claimed discrete uniform limit. For completeness, (4) telescopes over \(j<r\) to the exact identity
\[
\#\{\lambda\vdash n:M_r(\lambda)=M_s(\lambda)\}
=\sum_{m\ge1}\left[p\left(n-\frac{s m(m-1)}2\right)-
 p\left(n-\frac{s m(m-1)}2-rm\right)\right].
\tag{8}
\]
All terms with negative arguments vanish, so the sum is finite.

## Verification

A self-contained exact-arithmetic script `verify.py` reproduces formulas (1), (4), and (8) by enumerating all partitions for \(0\le n\le26\) and contrasting with independent Euler-pentagonal recurrence calculations of \(p(n)\). It also computes mark masses and coincidence proportions at \(n=1000,4000,16000\). The program prints `VERIFY_OK` when its tests pass. For example \(\Pr(M_1=M_3)\) is numerically \(0.383255\), \(0.368383\), \(0.357980\) at these three sizes, respectively, approaching the predicted \(1/3\). The finite checks do not establish the limit; that follows from the preceding argument.

## Relationship to prior work

Wagner's *Limit distributions of smallest gap and largest repeated part in integer partitions* (2011), Theorem 1, proves each fixed-rank Rayleigh marginal and local limit, but does not describe simultaneous least-gap ranks or the defect multiplicity at their shared stopping location. Ballantine and Merca's *Bisected theta series, least r-gaps in partitions, and polygonal numbers* (2017 preprint; subsequent publication), Section 1, introduces the exact counting statistic for inequalities between consecutive least gaps; its identities do not state the joint law or uniform coalescence distribution. Bhowmick and Meher's *On the Moments of Least r-Gaps of Partitions and a Conjecture of Baruah and Talukdar* (first posted 2026-09-25), Sections 1–3, establishes single-rank moment identities and parity-asymptotic relations. Here the additional ingredients are simultaneous mandatory-multiplicity removal and a local count resolving the exact multiplicity at the first deficient part. The shared single-rank marginal is prior work, not claimed new.

## Limitations

The rank parameters are fixed and the partitions are uniformly sampled; no growing-rank, rate-of-convergence, or other partition-ensemble theorem is asserted. Baruah and Talukdar's 2025 article on least-gap arithmetic and asymptotics was available as a publisher preview rather than accessible full text, leaving some priority risk for implicitly related formulas. Since Wagner's local-limit methods are close to the techniques here, a broader result in unindexed or inaccessible literature remains possible. Exact discrete coincidences require the marked local argument and cannot be justified by weak convergence alone.

## References

1. S. Bhowmick and N. K. Meher, *On the Moments of Least r-Gaps of Partitions and a Conjecture of Baruah and Talukdar*, first posted 2026-09-25, arXiv:2609.31104, https://arxiv.org/abs/2609.31104.
2. S. Wagner, *Limit distributions of smallest gap and largest repeated part in integer partitions*, Ramanujan J. 25 (2011), 229–246, DOI:10.1007/s11139-010-9264-z; author copy https://www.math.tugraz.at/~wagner/limitdist.pdf.
3. C. Ballantine and M. Merca, *Bisected theta series, least r-gaps in partitions, and polygonal numbers*, arXiv:1710.05960, first posted 2017-10-16, https://arxiv.org/abs/1710.05960.
4. N. D. Baruah and P. Talukdar, *Arithmetic and Asymptotic Properties for Some Functions Related to the Least r-Gaps of Partitions*, Ann. Comb. 30 (2026), 525–551, published online 2025-07-07, DOI:10.1007/s00026-025-00772-z (full text not accessible in this review).
5. G. H. Hardy and S. Ramanujan, *Asymptotic formulae in combinatory analysis*, Proc. London Math. Soc. (2) 17 (1918), 75–115.
