# Higher-moment entropy continuity from controlled output-probability moments

## Finding
Let \(N=2^n\), let \(\mu\) be an ensemble of \(N\times N\) unitary matrices, and fix an input computational-basis state \(y\). Put
\[
P_x(U)=|\langle x|U|y\rangle|^2,\qquad S(U)=-\sum_{x=1}^N P_x(U)\log_2 P_x(U).
\]
Suppose that, for every \(x\), the law of \(P_x\) under \(\mu\) is within Kolmogorov distance \(\eta\in[0,1/2]\) of the Haar law \(\operatorname{Beta}(1,N-1)\). Let \(q\ge2\) be an integer for which the following **explicit moment bound** holds for every \(x\):
\[
\mathbb E_\mu P_x^q\le(1+\varepsilon)\mathbb E_{\rm Haar}P_x^q,
\quad 0\le\varepsilon\le1.
\tag{M_q}
\]
Define \(R_{N,q}=N^{q-1}/[(N+1)\cdots(N+q-1)]\). Then
\[
\boxed{\left|\mathbb E_\mu S-\mathbb E_{\rm Haar}S\right|
\le\frac{2q}{e(q-1)\ln2}\,\eta^{1-1/q}
\left(\frac{(2+\varepsilon)q!R_{N,q}}2\right)^{1/q}.}
\tag{1}
\]
For \(\eta=0\), the left side is zero. In particular, (1) applies to **even \(2\le q\le k\)** for a relative-error strong unitary design whose order-\(k\) moment operator dominates each nonnegative bidegree-\((q,q)\) matrix coefficient in the usual sense. The theorem does **not** claim that an ordinary order-\(k\) design necessarily controls moments through \(2k\).

If \(0<\eta\le e^{-2}\), \(L=\ln(1/\eta)\), and moment domination (\(M_q\)) is available for \(q=2\lceil L/2\rceil\), then
\[
\boxed{\left|\mathbb E_\mu S-\mathbb E_{\rm Haar}S\right|\le15\eta\ln(1/\eta).}
\tag{2}
\]
Consequently, if the generic strong-design marginal estimate \(\eta=O(\sqrt{N/[k(k+N)]}+\varepsilon)\) is applicable and the design controls all moments of orders through \(k\), then for \(N=2^n\), \(k=\Theta(n^2(\ln n)^2)\), and \(\varepsilon=O(n^{-2})\), this method gives \(O(1/n)\) expected entropy error. The hidden constants depend on the marginal estimate; this is a sufficient asymptotic scale, not an optimality claim. It requires the usual relative-moment implication from the specific design definition used.

## Proof
For an arbitrary cutoff \(B>0\), split the entropy summand as
\[
-p\log_2p=p\log_2(N/B)+\phi_B^+(p)-\phi_B^-(p),
\quad\phi_B^+(p)=p[\log_2(B/(Np))]_+,\quad
\phi_B^-(p)=p[\log_2(Np/B)]_+.
\]
Since \(\sum_x P_x=1\), the constant term is identical under both ensembles. The function \(\phi_B^+\) is unimodal and nonnegative, its superlevel sets are intervals, and its supremum is at most \(B/(Ne\ln2)\). If two real-valued laws have Kolmogorov distance at most \(\eta\), their probabilities of every interval differ by at most \(2\eta\). The layer-cake representation thus bounds the total difference of positive terms by \(2\eta B/(e\ln2)\).

On the domain \(Np/B\ge1\), put \(z=Np/B\). Calculus gives \(\ln z\le z^{q-1}/[e(q-1)]\) for \(q>1\); consequently
\[
\phi_B^-(p)\le \frac{N^{q-1}p^q}{e(q-1)B^{q-1}\ln2}.
\]
For \(P_x\sim\operatorname{Beta}(1,N-1)\),
\[
\mathbb E_{\rm Haar}P_x^q=\frac{q!}{N(N+1)\cdots(N+q-1)}.
\]
Summation, (\(M_q\)), and the triangle inequality bound the two nonnegative tail expectations together by
\[
\frac{(2+\varepsilon)q!R_{N,q}}{e(q-1) B^{q-1}\ln2}.
\]
Therefore the entropy difference is at most
\[
\frac1{e\ln2}\left(2\eta B+\frac{(2+\varepsilon)q!R_{N,q}}{(q-1)B^{q-1}}\right).
\]
When \(\eta>0\), this is minimized at
\(B^q=(2+\varepsilon)q!R_{N,q}/(2\eta)\), proving (1). The cutoff was arbitrary positive, so no unproved boundary requirement on \(B\) is needed. When \(\eta=0\), the marginal laws agree exactly, hence so do the expectations of the sum of the marginal entropy contributions.

For (2), \(R_{N,q}\le1\), \(q!^{1/q}\le q\), and \(2+\varepsilon\le3\) yield
\[
\left|\mathbb E_\mu S-\mathbb E_{\rm Haar}S\right|
\le\frac{4\sqrt{3/2}}{e\ln2}\,q\eta^{1-1/q}.
\]
Our chosen even \(q\) lies between \(L\) and \(2L\), so \(\eta^{-1/q}\le e\), and the right side is less than \(15\eta L\). With \(k=\Theta(n^2(\ln n)^2)\ll N=2^n\), the cited marginal scale is \(O(1/(n\ln n))\) when \(\varepsilon=O(n^{-2})\), and \(\eta\ln(1/\eta)=O(1/n)\).

For the design specialization, \(P_x^q\) is a polynomial of bidegree \((q,q)\) in the entries of \(U\) and their conjugates. Thus the ordinary relative moment-operator order-\(k\) comparison applies when \(q\le k\). We do not infer a bound at \(q>k\) from this ordinary moment comparison. If a stronger convention separately supplies (\(M_q\)) for additional orders, the same conditional theorem remains applicable to those orders.

## Why the order restriction matters
For conventional order-one unitary designs, second moments of \(P_x\) need not match Haar. For example, in dimension \(N=2^n\), the uniform Weyl/Pauli unitary ensemble is an exact unitary one-design and maps each fixed basis input to a uniformly distributed basis output. Its \(P_x\) takes values 0 and 1, unlike \(\operatorname{Beta}(1,N-1)\). Mixing this ensemble with Haar in proportions \(\delta\) and \(1-\delta\) remains an exact one-design, gives marginal Kolmogorov distance \(\eta=\delta(1-1/N)\), and lowers expected output entropy by \(\delta(H_N-1)/\ln2\), where \(H_N\) is the harmonic number. For \(\delta=0.1\) and \(N=2^{20}\), this entropy gap is about 1.94 bits, exceeding the putative \(q=2\) right-hand side of (1) (about 0.95 bits) **if** one were to apply it without the second-moment hypothesis. This is a concrete guard against assuming that the ordinary first design moment controls second moments; it does not address a separately defined stronger design notion that includes such control.

## Relationship to earlier work and limitations
Hung, *Random Quantum Circuits Beyond Moment Matching*, arXiv:2610.02135v1 (2026), gives a marginal Kolmogorov estimate for strong approximate unitary designs and states an \(O(\sqrt\eta)\) expected-entropy estimate. The present bound is a separate high-moment interpolation consequence: it applies under the explicitly displayed moment hypothesis, and its generic design-order corollary is conditional on the available order of the design's relative moment control. General unitary-design constructions do not by themselves identify the optimized entropy cutoff. The relevant source full text could not be retrieved for this independent review, so the exact strength of its squared-polynomial comparison and a possible implicit antecedent remain priority and applicability risks; the paper's abstract was accessible. No claim is made of an entirely new entropy functional, an information-theoretically necessary design order, concentration, or a result beyond the stated moment assumptions.

## Verification and scope
The proof above is analytic. The quantitative check \(\delta(H_{2^{20}}-1)/\ln2\approx1.94\), versus the invalid unrestricted \(q=2\) extrapolation near 0.95, follows directly from a one-design mixture. Finite arithmetic can check constants and the minimizer but does not prove any unverified design-moment implication. The full theorem is valid whenever (\(M_q\)) and the Kolmogorov hypothesis hold, including distributions unrelated to unitary designs.
