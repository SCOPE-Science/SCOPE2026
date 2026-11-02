# Square-zero block injections: exact rank census and a parity-Poisson transition

## Finding

Let \(M_{k,m}\) be the inverse monoid of block-stable, block-order-preserving partial bijections on \(k\) ordered blocks, each of cardinality \(m\), where \(k,m\ge 2\). Its zero is the empty map. For an element \(f\) satisfying \(f^2=0\), let \(T(f)\) be the number of domain blocks and let \(H(f)=k-2T(f)\), the number of blocks belonging to neither the domain nor the image.

**Theorem.** For every pair of integers \(k,m\ge2\):

1. The number of square-zero elements with \(T(f)=t\) is
   \[
   c_{k,m}(t)=\begin{cases}\displaystyle\frac{k!}{t!^2(k-2t)!}(m!)^t,&0\le t\le\lfloor k/2\rfloor,\\[2mm]0,&\text{otherwise}.\end{cases}
   \]
   The zero map is included at \(t=0\). The rank of the underlying partial map is \(mt\). The total square-zero count is \(C_{k,m}=\sum_t c_{k,m}(t)\).
2. With \(m\) fixed and \(k\to\infty\), choose \(f\) uniformly from the square-zero elements. Put \(s=\sqrt{m!}\) and \(p_0=(1+2s)^{-1}\). Then
   \[
     \frac{H}{k}\ \xrightarrow{\mathbb P}\ p_0,
     \qquad
     \frac{H-kp_0}{\sqrt{k}}\ \xrightarrow{\mathrm d}\
        N\bigl(0,p_0(1-p_0)\bigr).
   \]
   In particular, the block rank satisfies \(T/k\to s/(1+2s)\) in probability. The probability that a uniform element of the full monoid is square-zero has the sharp equivalent
   \[
      \frac{C_{k,m}}{|M_{k,m}|}\sim
      \frac{\sqrt{1+2s}}{1+s}\left(\frac{1+2s}{(1+s)^2}\right)^k.
   \]
3. In a simultaneous limit \(k\to\infty\) and \(m=m(k)\to\infty\) with
   \[\lambda_k=\frac{k}{2\sqrt{m!}}\longrightarrow\lambda\in(0,\infty),\]
   restrict to any subsequence for which the parity \(r=k\bmod2\) is fixed. The law of \(H\) converges in **total variation** to a Poisson\((\lambda)\) random variable conditioned to have parity \(r\):
   \[
      \lim\Pr(H=h)=
      \begin{cases}
         \displaystyle\frac{\lambda^h}{h! Z_r(\lambda)},&h\ge0,\ h\equiv r\pmod2,\\
         0,&\text{otherwise},
      \end{cases}
      \quad Z_0(\lambda)=\cosh\lambda,\quad Z_1(\lambda)=\sinh\lambda.
   \]
   If instead \(m! / k^2\to\infty\), then \(\Pr(H=k\bmod2)\to1\). Thus the critical crossover from a near-maximal square-zero block rank to nontrivial bounded vacancies occurs when \(m!\) is of order \(k^2\).

## Assumptions and scope

Fix the blocks \(B_1<\cdots<B_k\), each with \(m\) labeled points. An element consists of two equally sized subsets \(D=\{d_1<\cdots<d_t\}\) and \(I=\{i_1<\cdots<i_t\}\) of \(\{1,\dots,k\}\) and, for each \(j\), a bijection \(B_{d_j}\to B_{i_j}\). It is undefined off \(\bigcup_{d\in D}B_d\). Composition is ordinary composition of partial maps. This is precisely the monoid presented in Caneco–Fernandes–Quinteiro (2019). There are no primality or finiteness-of-field assumptions. The limit with fixed \(m\) treats \(m\) as an integer constant, and the critical window treats \(m(k)\) as an arbitrary integer sequence meeting the stated limit.

## Proof

**Step 1: support characterization.** For each selected block \(B_d\), the map is a bijection onto a selected image block \(B_i\). Its square is defined at some point of \(B_d\) if and only if \(B_i\) is a domain block. Since every block map is surjective, this equivalence holds without exceptions. Hence \(f^2=0\) exactly when \(D\cap I=\varnothing\).

**Step 2: exact count.** For each \(0\le t\le k/2\), choose \(t\) domain indices and \(t\) disjoint image indices in \(k!/(t!^2(k-2t)!)\) ways. The order condition uniquely pairs the two sorted lists. Each of the \(t\) block bijections has exactly \(m!\) choices. This proves the formula, including \(t=0\).

**Step 3: fixed-block limit.** Set \(a=m!\) and \(s=\sqrt a\). Let \(X_1,\dots,X_k\) be independent random variables in \(\{-1,0,1\}\) with
\[\Pr(X_j=0)=p_0=\frac1{1+2s},\qquad \Pr(X_j=1)=\Pr(X_j=-1)=p=\frac{s}{1+2s}.\]
Condition on \(S_k=\sum_jX_j=0\). The three labels encode unused, domain, and image blocks. A configuration with \(t\) each of the latter two has unconditional probability \(s^{2t}/(1+2s)^k=a^t/(1+2s)^k\), so the conditional distribution of its number \(H\) of zeros is exactly the required rank distribution.

The ordinary one-dimensional lattice local central limit theorem gives
\[\Pr(S_k=0)\sim (4\pi kp)^{-1/2}.\]
For \(h\equiv k\pmod2\) and \(t=(k-h)/2\), the joint mass is
\[\Pr(S_k=0,H=h)=\frac{k!}{h!t!^2}p_0^h p^{2t}.\]
Applying Stirling's formula uniformly to \(h=kp_0+z\sqrt{k}\) with \(z\) in a fixed compact set yields
\[\Pr(H=h\mid S_k=0)=\frac{2+o(1)}{\sqrt{2\pi k p_0(1-p_0)}}
\exp\left(-\frac{(h-kp_0)^2}{2k p_0(1-p_0)}\right).\]
The factor \(2\) is the parity lattice spacing. Here is a tail justification for using the compact-uniform local estimate. Before conditioning, \(H\) is exactly \(\mathrm{Bin}(k,p_0)\). Conditional on \(H=h\), the remaining \(k-h\) signs are fair and independent, and \(\Pr(S_k=0\mid H=h)\) is either zero (for odd \(k-h\)) or \(2^{-(k-h)}\binom{k-h}{(k-h)/2}\). Fix any \(\eta\) with \(0<\eta<1-p_0\). On \(h\le(p_0+\eta)k\), the latter probability is at most \(C_{m,\eta}/\sqrt{k}\), while \(\Pr(S_k=0)\ge c_m/\sqrt{k}\). Hence the conditional probability of any subset in this region is at most a constant times its unconditioned binomial probability. The omitted region \(h>(p_0+\eta)k\) has exponentially small unconditioned probability and therefore vanishing conditional probability as well. Binomial normal tightness now makes the centered conditional laws tight on the \(\sqrt{k}\) scale. Summing the displayed local masses over the parity mesh proves the Gaussian limit and the law of large numbers.

The full monoid size from Proposition 2.1 of Caneco–Fernandes–Quinteiro is \(\sum_{t=0}^k\binom kt^2 a^t\). It equals \((1+s)^{2k}\Pr(U_k=V_k)\) where \(U_k,V_k\) are independent \(\mathrm{Bin}(k,s/(1+s))\). Another lattice local central limit theorem gives
\[|M_{k,m}|\sim\frac{1+s}{\sqrt{4\pi ks}}(1+s)^{2k}.\]
Similarly, \(C_{k,m}=(1+2s)^k\Pr(S_k=0)\sim (1+2s)^k\sqrt{1+2s}/\sqrt{4\pi ks}\). Their ratio is the claimed square-zero probability equivalent.

**Step 4: critical parity-Poisson limit.** Put \(r=k\bmod2\) and \(h=r+2j\), \(j\ge0\), with \(t_0=(k-r)/2\). Dividing the exact mass at \(h\) by that at \(r\) gives
\[\frac{\Pr(H=r+2j)}{\Pr(H=r)}=\frac{r!}{(r+2j)!}\left(\frac{1}{m!}\right)^j\prod_{\ell=0}^{j-1}(t_0-\ell)^2.\]
For each fixed \(j\), the right-hand side tends to \(r!\lambda^{2j}/(r+2j)!\). If \(\lambda_k\le L\), it is bounded above by \(r!L^{2j}/(r+2j)!\), a summable majorant. Dominated convergence identifies the normalizing constant as \(r!\lambda^{-r}Z_r(\lambda)\) and gives convergence of each probability and, by summability, total-variation convergence. If \(m!/k^2\to\infty\), the same domination with \(\lambda_k\to0\) makes the total mass outside \(h=r\) tend to zero. This proves every statement.

## Verification

The accompanying standalone file `verify.py` enumerates actual partial maps, applies composition twice, checks the full-monoid sizes and every square-zero rank count for 17 configurations with \(1\le m\le3\) and \(1\le k\le7\) (using some \(m=1\) boundary cases as independent diagnostics), and compares critical-window distributions of both parities with parity-conditioned Poisson probabilities. It also computes fixed-\(m\) mean and variance diagnostics at \(k=200,800\). Run `python3 verify.py`; successful completion prints `VERIFY_OK`. Finite tests corroborate, but do not establish, the infinite limits, which follow from the proof above.

## Relationship to prior work

Caneco, Fernandes and Quinteiro (2019, arXiv:1905.11489v1) define these normally ordered inverse monoids and compute their total sizes, ranks as generating sets, and presentations. Their Proposition 2.1 supplies the total size used in the probability quotient. They do not give the square-zero rank distribution or the two-parameter critical vacancy law in the inspected text. Garba (1994) studies nilpotents of ordinary partial order-preserving injections, corresponding to the unblocked special case, and subsequent nilpotent-generated subsemigroups. Laradji and Umar (2015) derive counting and asymptotic formulas for nilpotents of ordinary order-preserving or order-reversing partial injections. Their unblocked, all-nilpotents question is distinguished from square-zero elements in block-wreath inverse monoids when the block size grows. That earlier study is not a claim of novelty for the general notion of nilpotency. Classical central trinomial coefficients (OEIS A002426) already coincide with the unblocked square-zero total \(m=1\); generalized central trinomial coefficients also represent the exact finite sum as a coefficient. These combinatorial identities are credited. The focus here is the algebra-specific block-rank profile and its factorial-scale, parity-sensitive double limit. The 2024 work of Kachalla–Madu–Ngulde concerns decomposition as products of nilpotents, a different question. Novelty relative to inaccessible older sources is not asserted as certain.

## Limitations

The proof concerns **square-zero** elements only, not all nilpotent elements or a classification of the nilpotent-generated subsemigroup. The fixed-\(m\) and factorial-critical results are separate asymptotic regimes; no universal uniform-in-\(k,m\) central limit theorem is claimed. The critical total-variation limit is conditioned on fixed parity, since \(H\equiv k\pmod2\) exactly. The 1994 Garba article and 2015 Laradji–Umar article on ordinary monotone partial injections were located, but their complete texts could not be inspected here; institutional retrieval requires an interactive authorization. Equivalent results under generalized trinomial terminology, or a previously published factorially weighted enumeration for the block family, remain publication-priority risks. Mathematical verification is not independent external validation.

## References

1. R. Caneco, V. H. Fernandes, and T. M. Quinteiro, *Ranks and presentations of some normally ordered inverse semigroups*, arXiv:1905.11489v1, submitted 2019-05-27. https://arxiv.org/abs/1905.11489 (especially Sections 1–3, Proposition 2.1).
2. G. U. Garba, *Nilpotents in semigroups of partial one-one order-preserving mappings*, Semigroup Forum 48 (1994), 37–49. DOI:10.1007/BF02573652.
3. A. Kachalla, B. A. Madu, and S. G. Ngulde, *Expressing Partial Order-Preserving Transformations as Products of Nilpotents*, International Journal of Development Mathematics 1 (2024), 112–125, DOI:10.62054/ijdm/0103.08.
4. OEIS A002426, *Central trinomial coefficients*. https://oeis.org/A002426.
5. Z.-W. Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887, submitted 2010-08-23. https://arxiv.org/abs/1008.3887.
6. A. Laradji and A. Umar, *Combinatorial results for semigroups of order-preserving or order-reversing subpermutations*, J. Difference Equ. Appl. 21 (2015), 269–283. DOI:10.1080/10236198.2015.1005080.
