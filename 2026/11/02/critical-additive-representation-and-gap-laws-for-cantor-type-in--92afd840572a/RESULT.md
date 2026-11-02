# Critical additive representation and gap laws for Cantor-type integer sumsets

## Finding
For each integer \(p\ge2\) and each real \(1<\alpha<2\), put
\[
a_j=\lfloor\alpha p^j\rfloor,\qquad C=\left\{\sum_{j\ge0}\varepsilon_j a_j:\ \varepsilon_j\in\{0,1\},\ \varepsilon_j=0\text{ eventually}\right\}.
\]
Write \(hC\) for the sum of \(h\) independent elements of \(C\), not scalar dilation. Let \(K=(p-1)C\), and define the canonical base-\(p\) digits of \(m\ge0\) by \(m=\sum_{j\ge0}d_j(m)p^j\), \(0\le d_j(m)<p\). Put \(F(m)=\sum_{j\ge0}d_j(m)a_j\). Let \(\eta_j=a_j-pa_{j-1}\) for \(j\ge1\), so \(0\le\eta_j<p\), and put \(G_j=1+\sum_{i=1}^j\eta_i\), including \(G_0=1\). Define \(\operatorname{ord}_p(t)=\max\{j\ge0:p^j\mid t\}\), valid also for composite \(p\).

**Unified theorem.** The complete increasing enumeration of \(K\) is \(F(0)<F(1)<\cdots\), and its consecutive gap is exactly
\[
F(m+1)-F(m)=G_{\operatorname{ord}_p(m+1)}.
\]
The index-frequency of a gap of any specified positive size \(r\) therefore exists and is
\[
\lim_{M\to\infty}\frac{\#\{0\le m<M:F(m+1)-F(m)=r\}}M
=(p-1)\sum_{\substack{j\ge0\\G_j=r}}p^{-j-1}.
\]
Moreover,
\[
\#(K\cap[0,X])=\frac X\alpha+O_p(\log(X+2))\qquad(X\to\infty).
\]
The gaps of \(K\) are bounded precisely when \(\alpha\) has a terminating base-\(p\) expansion.

For every \(x\in K\), let \(R(x)\) count **ordered** \((p-1)\)-tuples from \(C\) summing to \(x\). The exact fiber law is
\[
R(F(m))=\prod_{j\ge0}\binom{p-1}{d_j(m)}.
\]
For \(C_L\), the subset sums of the first \(L\) denominations, write \(R_L\) for the analogous ordered representation function. Its first and second moments are exactly
\[
\sum_x R_L(x)=2^{(p-1)L},\qquad
\sum_x R_L(x)^2=\binom{2p-2}{p-1}^{L}.
\]
For \(p\ge3\) and uniformly random \(m\in\{0,\dots,p^L-1\}\), the standardized \(\log R(F(m))\) converges in distribution to a standard Gaussian as \(L\to\infty\). More precisely, set
\[
\mu_p=\frac1p\sum_{d=0}^{p-1}\log\binom{p-1}{d},\qquad
\sigma_p^2=\frac1p\sum_{d=0}^{p-1}\left(\log\binom{p-1}{d}-\mu_p\right)^2>0.
\]
Then \((\log R(F(m))-L\mu_p)/(\sigma_p\sqrt L)\) tends to \(N(0,1)\). For \(p=2\), \(R\equiv1\) on \(K\), so no nondegenerate normal limit is asserted.

Finally, the exact minimum positive integer \(h\) for which \(hC=\mathbb Z_{\ge0}\) is
\[
\boxed{H(p,\alpha)=\max\{p,\lfloor p\alpha\rfloor-1\}.}
\]
For \(p\ge3\) and \(1\le h\le p-2\), the sharp counting scale is
\[
\#\bigl(hC\cap[0,X]\bigr)=\Theta_{p,\alpha,h}\bigl(X^{\log_p(h+1)}\bigr),
\]
so the critical order \(p-1\) is the first one with positive density, while order \(H(p,\alpha)\) is the first with every nonnegative integer covered.

## Assumptions and scope
The base \(p\) is an arbitrary integer at least two (not necessarily prime); \(1<\alpha<2\) is any real, rational or irrational. Every subset sum has finite support. The convention for the base-\(p\) expansion of \(\alpha\) is the floor-generated expansion \(\eta_j=a_j-pa_{j-1}\), which terminates whenever possible. Ordered representations distinguish permutations of the \(p-1\) summands. All density statements refer to the nonnegative integers. The asymptotic gap frequencies are by **successive elements of \(K\)**, not by ambient integer positions. Natural logarithms are used in the limit law.

## Proof
**1. The digital carrying gap.** Since \(a_0=1\) and \(a_j=pa_{j-1}+\eta_j\), with \(0\le\eta_j\le p-1\), let \(s_{j-1}=\sum_{i<j}a_i\). Direct induction gives
\[
a_j-(p-1)s_{j-1}=1+\sum_{i=1}^j\eta_i=G_j\ge1.
\]
At a base-\(p\) carry of length \(j=\operatorname{ord}_p(m+1)\), the last \(j\) digits of \(m\) are \(p-1\), and the next digit increases by one. Consequently \(F(m+1)-F(m)=a_j-(p-1)s_{j-1}=G_j\). Thus \(F\) is strictly increasing. Every element of \((p-1)C\) has a coefficient expansion with digits in \(\{0,\ldots,p-1\}\) because each of its \(p-1\) subset-sum terms contributes either zero or one to each coefficient. Conversely, any such coefficient vector can be assigned to \(p-1\) distinct slots independently at each index. Every element therefore equals some \(F(m)\); strict increase proves uniqueness of its digit vector and complete enumeration.

**2. Gap frequencies, boundedness, and density.** The integers \(m+1\) divisible by \(p^j\) but not \(p^{j+1}\) have natural density \((p-1)/p^{j+1}\); this remains valid for composite bases. For a specified gap size \(r\), restrict to \(\operatorname{ord}_p(m+1)<J\) and let \(J\to\infty\); the omitted index proportion is at most \(p^{-J}\). This gives the stated exact sum, even if infinitely many \(j\)'s have the same \(G_j\). Because \(G_j\) is nondecreasing, it stays bounded exactly when only finitely many base-\(p\) digits \(\eta_j\) are positive. Furthermore,
\[
0\le\alpha m-F(m)=\sum_jd_j(m)\{\alpha p^j\}
\le(p-1)(1+\lfloor\log_p m\rfloor)\qquad(m\ge1).
\]
Also \(F(m)\ge m\). Hence, for any \(F(m)\le X\), the right-hand error is \(O_p(\log(X+2))\). Inverting the strictly increasing enumeration between \(\alpha m-O_p(\log(m+2))\) and \(\alpha m\) proves the claimed counting estimate.

**3. Every ordered representation fiber and its moments.** At each digit \(j\), choose the \(d_j(m)\) out of \(p-1\) ordered summand slots in which to include \(a_j\). Uniqueness from step 1 excludes any alternative coefficient vector. Independent choices across indices yield \(R(F(m))=\prod_j\binom{p-1}{d_j(m)}\). At finite depth \(L\) the same bijection identifies the entire support of \(R_L\) with \(0\le m<p^L\). Thus
\[
\sum_x R_L(x)=\prod_{j=0}^{L-1}\sum_{d=0}^{p-1}\binom{p-1}{d}=2^{(p-1)L}
\]
and
\[
\sum_x R_L(x)^2
=\left(\sum_{d=0}^{p-1}\binom{p-1}{d}^2\right)^L
=\binom{2p-2}{p-1}^L,
\]
by Vandermonde's identity. For uniform \(m<p^L\), its \(L\) base digits are independent and uniform in \(\{0,\ldots,p-1\}\), so \(\log R(F(m))\) is the sum of \(L\) independent copies of \(\log\binom{p-1}{D}\). For \(p\ge3\), the logarithms are not constant; their finite variance is positive. The classical independent-identically-distributed central limit theorem gives the asserted limit. For \(p=2\) the summand is identically zero.

**4. The sharp covering order.** For any \(h\ge1\), \(hC\) consists of digit sums \(\sum_jc_ja_j\) with \(0\le c_j\le h\). If \(h\le p-1\), this is contained in \((p-1)C\). Since \(\alpha>1\), at least one digit \(\eta_j\) is nonzero; then \(G_j\ge2\), so \(K\) omits at least one integer and cannot equal \(\mathbb Z_{\ge0}\). If \(h<p\) this already proves incompleteness. Independently, if \(h<a_1-1\), integer \(h+1<a_1\) is impossible using \(a_0=1\) at most \(h\) times and larger denominations at least \(a_1\). Both lower bounds imply \(h\ge\max\{p,a_1-1\}\).

For the reverse inequality, take \(h\ge\max\{p,a_1-1\}\). At depth zero the numbers \(0,\ldots,h\) occur. Suppose coefficients \(0,\ldots,h\) at indices \(<j\) cover \([0,hs_{j-1}]\) continuously. At \(j=1\), \(a_1\le h+1\). For \(j\ge2\), the digit recurrence and \(s_{j-2}\ge1\) give
\[
a_j\le p a_{j-1}+(p-1)\le p s_{j-1}+1\le h s_{j-1}+1.
\]
Thus the intervals \([c a_j,c a_j+hs_{j-1}]\), for \(0\le c\le h\), touch or overlap and cover the entire interval \([0,hs_j]\). Induction and \(s_j\to\infty\) prove \(hC=\mathbb Z_{\ge0}\), with minimum \(H(p,\alpha)\).

**5. Sharp sparse-order exponent.** If \(1\le h\le p-2\), distinct coefficient vectors \(0\le c_j\le h\) have distinct sums by the strict digital ordering already established. All represented values at most \(X\) use only indices \(j\le\lfloor\log_p X\rfloor\), because \(a_j\ge p^j\). This gives an upper bound of order \((h+1)^{\log_p X}=X^{\log_p(h+1)}\). Conversely, for any \(L\), all \((h+1)^L\) coefficient vectors supported below \(L\) give distinct values bounded by \(h\alpha(p^L-1)/(p-1)\). Choosing \(L=\lfloor\log_p(c_{p,\alpha,h}X)\rfloor\) for a suitable fixed positive constant gives the matching lower bound for all sufficiently large \(X\).

## Verification
The accompanying standalone `verify.py` performs exact rational-arithmetic checks for twenty choices of integer base and rational parameter. It constructs complete critical digit sets, checks 48,780 consecutive-gap identities, checks 1,760 ordered-representation fibers by direct tuple enumeration, verifies exact second moments, and verifies all-integer finite-prefix covering in twenty cases. It prints `VERIFY_OK` when complete. These finite computations corroborate but do not establish the unrestricted theorem. The infinite gap-frequency limit follows from exact divisibility densities and a vanishing tail; the normal limit follows from the ordinary i.i.d. central limit theorem.

## Relationship to prior work
Norbert Hegyvári's 2023 work, *On arithmetic sums of Cantor-type sequences of integers* (arXiv:2307.07237), defines these integer sets, proves the base-digit increment identity in Lemma 2.2, and proves \(C+C=\mathbb Z_{\ge0}\) in base two. Its Theorem 2.1 studies the **dilated** sum \(C+(p-1)\cdot C\), not the repeated \((p-1)\)-fold Minkowski sum studied here. Thus the crucial digit increment is an acknowledged input, not presented as new. The results established here classify the ordered critical sumset, its full gap frequencies, exact representation fibers and collision moments, the logarithmic normal law, and the sharp covering threshold for all bases.

A different generalized exponential-denomination setting was studied in *On exponential type sequences* (Discrete Applied Mathematics 338 (2023), 187–189), which gives general density and completeness criteria; the floor-perturbed coefficients, exact critical fibers, and the stated phase diagram are not among its accessible theorems. Brown's classic completeness criterion supplies the standard interval-induction idea and is not claimed as new. Real linear Cantor-set Minkowski sums constitute a related but different continuum setting.

## Limitations
This result does not establish priority over inaccessible or unindexed literature or characterize representation distributions above the critical order. The limit theorem concerns a uniformly chosen **index** among the first \(p^L\) critical-sumset elements, not a uniformly chosen ambient integer. The exact phase diagram addresses equality with all nonnegative integers, not mere eventual cofiniteness at intermediate orders. The reproducible finite checks are not a substitute for the mathematical proof.

## References
1. N. Hegyvári, *On arithmetic sums of Cantor-type sequences of integers*, arXiv:2307.07237, initial posting 14 July 2023. https://arxiv.org/abs/2307.07237
2. *On exponential type sequences*, Discrete Applied Mathematics 338 (2023), 187–189. https://doi.org/10.1016/j.dam.2023.05.023
3. E. Bołdyriew, J. Haviland, P. Lâm, J. Lentfer, S. J. Miller, F. Trejos Suárez, *Completeness of Positive Linear Recurrence Sequences*, arXiv:2010.01655 (discussion of Brown's criterion). https://arxiv.org/abs/2010.01655
4. K. G. Hare and N. Sidorov, *The Minkowski sum of linear Cantor sets*, Acta Arithmetica 212 (2024), 173–193. https://doi.org/10.4064/aa230315-14-7
