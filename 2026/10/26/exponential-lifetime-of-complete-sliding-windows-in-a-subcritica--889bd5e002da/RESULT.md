# Exponential lifetime of complete sliding windows in a subcritical coupon collector

## Finding
Fix \(0<\alpha<1\). For each integer \(n\ge2\), let \((X_t)_{t\in\mathbb Z}\) be i.i.d. uniform on \(\{1,\ldots,n\}\), and set \(M=M_n=\lfloor\alpha n\log n\rfloor\), for all sufficiently large \(n\) so that \(M\ge n\). The length-\(M\) window is \(W_t=(X_{t-M+1},\ldots,X_t)\). Write \(A_t\) for the event that \(W_t\) contains all \(n\) coupon types, and \(E_0=A_0\cap A_{-1}^{c}\) for a stationary entry into complete coverage. Conditional on \(E_0\), let
\[
L_n=\min\{j\ge1:A_j^c\}
\]
be the number of consecutive complete windows beginning at that entry.

**Theorem.** For every fixed \(0<\alpha<1\), conditional on \(E_0\),
\[
\frac{L_n}{n^\alpha}\ \Longrightarrow\ \operatorname{Exp}(1),
\qquad
\frac{\mathbb E[L_n\mid E_0]}{n^\alpha}\longrightarrow1.
\]
Equivalently, for every fixed \(t\ge0\), \(\Pr(L_n>\lfloor tn^\alpha\rfloor\mid E_0)\to e^{-t}\). The expectation also has the **exact** finite-parameter expression
\[
\boxed{\mathbb E[L_n\mid E_0]=\frac{nS(M,n)}{(n-1)S(M-1,n-1)}},
\]
where \(S(k,j)\) is a Stirling number of the second kind. In particular, the rare complete-coverage episodes have a typical duration on the polynomial \(n^\alpha\) scale, distinct from their exponentially large inter-entry times.

## Assumptions and scope
All logarithms are natural. The samples are independent and exactly uniform; the window has a deterministic fixed length. The statement concerns the *stationary episode observed at its starting entry*, not a window sampled conditional on being complete (which length-biases episodes), nor the first completion time of an initially empty collector. The limit fixes \(\alpha\) before \(n\to\infty\). No higher-moment convergence or uniformity in \(\alpha\) is asserted.

For a finite alphabet of size \(N\), define the onto-word probability
\[
Q_N(k)=\frac{N!S(k,N)}{N^k}\quad(k\ge N),\qquad Q_N(k)=0\quad(k<N).
\]
The conditional event \(E_0\) has positive probability for \(M\ge n\).

## Proof
**1. Entry law and finite sandwich.** At a new entry, the newly appended coupon \(a=X_0\) is absent from the common middle block \(U=(X_{-M+1},\ldots,X_{-1})\); that block must cover the other \(N=n-1\) types, and the departing coupon \(X_{-M}\) must differ from \(a\). Hence, conditional on \(E_0\) and \(a\), \(U\) is uniformly distributed over all onto words of length \(m=M-1\) on \(N\) symbols, and all subsequent \(X_1,X_2,\ldots\) remain independent uniform coupons.

For \(0\le u\le m\), let \(R_u\) count the types from those \(N\) symbols absent from the suffix \(U_{u+1:m}\). If the suffix still covers all \(N\) types then all windows through time \(u\) are complete, since the just-appended \(a\) is not removed before time \(M\). Conversely, if the window at time \(u\) is complete but that suffix is not, each suffix-missing type must have appeared in the \(u\) fresh samples. A union bound, conditional on \(U\), therefore gives the **exact finite sandwich**
\[
\frac{Q_N(m-u)}{Q_N(m)}
\le\Pr(L_n>u\mid E_0)
\le\frac{Q_N(m-u)}{Q_N(m)}+\frac{u}{n}\mathbb E[R_u\mid E_0].
\tag{1}
\]
The first term is the exact probability that the suffix is onto, conditional on the full word being onto.

**2. Local estimate for onto occupancy.** Let \(k/N=\rho\) with \(\rho=\alpha\log n+o(1)\), uniformly in a range \(k\in[m-O(n^\alpha),m]\), where \(N=n-1\). Define \(\tau>0\) uniquely by \(\rho=\tau/(1-e^{-\tau})\), and let independent \(D_i\) have zero-truncated Poisson law
\[
\Pr(D_i=j)=\frac{\tau^j}{j!(e^\tau-1)},\qquad j\ge1.
\]
Conditioning \((D_1,\ldots,D_N)\) on \(\sum_iD_i=k\) gives exactly the occupancy-count vector of a uniform onto word of length \(k\). Here \(\tau=\alpha\log n+o(1)\), \(e^{-\tau}=n^{-\alpha}(1+o(1))\), and \(\operatorname{Var}(D_i)\sim\tau\).

The span-one lattice local central limit theorem, uniformly in this range, yields
\[
\Pr(\textstyle\sum_{i=1}^N D_i=k)
\sim (2\pi N\operatorname{Var}(D_i))^{-1/2},
\qquad
\Pr(\textstyle\sum_{i=2}^N D_i=k-1)
\sim(2\pi N\operatorname{Var}(D_i))^{-1/2},
\tag{2}
\]
and \(\sup_z\Pr(\sum_{i=2}^N D_i=z)=O((N\tau)^{-1/2})\). For clarity, these statements follow by Fourier inversion using the characteristic function \((e^{\tau e^{it}}-1)/(e^\tau-1)\): on a fixed small arc its centered logarithm is \(-\operatorname{Var}(D_i)t^2/2+O(\tau|t|^3)\), and outside that arc its absolute value has exponential damping in \(\tau\). The shifted sum in (2) lies \(\rho-1=O(\log n)\) above its mean, negligible compared with the \(\sqrt{N\tau}\) standard deviation. This is the same local-estimate method as the zero-truncated-Poisson lemma in the source paper's Appendix A; it also establishes the displayed shifted version.

Let \(h_N(k)\) be the chance that a specified position is the sole occurrence of its color in a uniform onto word of length \(k\). Conditioning on the count vector and using (2),
\[
\begin{aligned}
h_N(k)
&=\frac Nk\,\frac{\tau}{e^\tau-1}
\frac{\Pr(\sum_{i=2}^ND_i=k-1)}{\Pr(\sum_{i=1}^ND_i=k)}\\
&=e^{-\tau}(1+o(1))=n^{-\alpha}(1+o(1)),
\end{aligned}
\tag{3}
\]
uniformly over the stated range. The exact identity \(Q_N(k-1)/Q_N(k)=1-h_N(k)\) follows by deleting the first position of an onto word. Taking \(u=\lfloor tn^\alpha\rfloor\), for fixed \(t\ge0\), produces
\[
\log\frac{Q_N(m-u)}{Q_N(m)}
=\sum_{k=m-u+1}^m\log(1-h_N(k))=-un^{-\alpha}(1+o(1))\longrightarrow-t.
\tag{4}
\]

**3. Fresh draws cannot repair lost colors at this scale.** Under the conditional onto law, let \(C_1\) denote the count of one specified symbol in \(U\). Given \(C_1=j\), its positions are a uniform \(j\)-subset of \(\{1,\ldots,m\}\), so the probability it is entirely inside the first \(u\) slots is at most \((u/m)^j\). The ratio of the shifted occupancy local mass to the central mass in (2) is uniformly bounded even for arbitrary \(j\), by the supremum bound, so
\[
\Pr(C_1=j\mid U\text{ onto})\le C\frac{\tau^j}{j!(e^\tau-1)}
\quad(j\ge1).
\]
Consequently, with \(s=u/m\),
\[
\mathbb E[R_u\mid E_0]
\le CN\sum_{j\ge1}\frac{\tau^js^j}{j!(e^\tau-1)}
=CN\frac{e^{\tau s}-1}{e^\tau-1}
=O_\alpha(un^{-\alpha})=O_{\alpha,t}(1),
\tag{5}
\]
because \(\tau s=O(n^{\alpha-1})\to0\). The error term in (1) is \(O_{\alpha,t}(n^{\alpha-1})\to0\). Equations (1), (4), and (5) prove the claimed exponential survival limit.

**4. Exact mean and its asymptotics.** For the finite stationary, irreducible sliding-window chain, each complete window belongs to exactly one finite episode begun at a new entry. Thus the stationary mass of complete windows equals the entry intensity times the entry-conditioned mean episode length:
\[
\pi_{n,M}=\mu_{n,M}\,\mathbb E[L_n\mid E_0].
\]
The exact quantities are \(\pi_{n,M}=n!S(M,n)/n^M\) and \(\mu_{n,M}=(n-1)(n-1)!S(M-1,n-1)/n^M\), giving the asserted exact mean. Alternatively, condition on a complete window: the preceding window is incomplete exactly if its final-position coupon is unique in the complete window and the departing earlier coupon differs from it, which has probability \((1-1/n)h_n(M)\). Hence
\[
\mathbb E[L_n\mid E_0]=\bigl[(1-1/n)h_n(M)\bigr]^{-1}\sim n^\alpha
\]
by the same local estimate (3) with \(N=n,k=M\). This completes the proof.

## Verification
The accompanying `verify.py` is self-contained Python 3 code using exact rational arithmetic. It enumerates entry-conditioned onto words and all short future sequences for small alphabets, checks both sides of the finite sandwich (1), solves exact finite-state mean-exit systems, and compares their answers with the exact Stirling-number mean formula. Its recorded execution reports `VERIFY_OK 98 exact finite-state / combinatorial assertions`.

The finite checks test identities and boundary cases, not the infinite local limit theorem. The asymptotic step uses the explicitly described zero-truncated-Poisson Fourier local limit, including its shifted form. No independent mathematical audit has been performed.

## Relationship to prior work
Long (2026), *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, computes the stationary onto-window mass and entry intensity, proves rare-entry exponential limits for the **time to the first complete window**, and uses a last-occurrence bound to control later entries. Its Remark 4.4 discusses typical clump length heuristically, but does not state the conditional lifetime law above. The present result instead determines the entire asymptotic distribution of the consecutive complete-window **episode following an entry**, and identifies its exact mean and scale. The local limit technique in the proof is an extension of the paper's Appendix A, not a new general probability theorem.

The original 2012 discussion of expiring coupons (Joriki, Mathematics Stack Exchange question 44338) anticipated the small chance that a sliding deletion destroys completeness and the rarity of entries. Its heuristic is a historical antecedent, not an explicit rigorous law for episode length under entry conditioning. The mean identity is already directly implied by the stationary flux and mass in Long (2026), and is not asserted to be independently novel.

The classical coupon-collector occupancy and lattice local central limit theorems are background tools. The new content is their combination with the stationary entry conditioning and the uniform repair-error estimate (5). An unidentified earlier scan-statistics result could imply this specialization; a historical priority guarantee is not claimed.

## Limitations
Only independent uniform coupon draws and fixed \(\alpha\in(0,1)\) are treated. The argument does not address critical \(\alpha=1\), a fixed linear window, arbitrary nonuniform weights, length-biased episodes sampled at a random complete time, or joint limits for multiple episodes. It proves convergence in distribution and first moments only. Full historical priority and independent mathematical validation remain open.

## References
1. C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1, first submitted April 29, 2026. Sections 2–8 and Appendix A. https://arxiv.org/abs/2604.26298
2. P. Erdős and A. Rényi, *On a classical problem of probability theory*, Magyar Tud. Akad. Mat. Kutató Int. Közl. 6 (1961), 215–220. Background for occupancy tails.
3. V. V. Petrov, *Sums of Independent Random Variables*, Springer-Verlag, 1975, Chapter VII. Background for lattice local limit methods.
4. N. M. Temme, *Asymptotic estimates of Stirling numbers*, Studies in Applied Mathematics 89 (1993), 233–243. Background for surjection-count asymptotics.
5. Joriki, answer to *A different kind of coupon collector problem* (2012), Mathematics Stack Exchange question 44338, https://math.stackexchange.com/questions/44338/a-different-kind-of-coupon-collector-problem . Historical heuristic only.
