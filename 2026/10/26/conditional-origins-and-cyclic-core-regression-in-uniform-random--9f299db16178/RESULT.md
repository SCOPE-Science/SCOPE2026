# Conditional origins and cyclic-core regression in uniform random mappings

## Finding

Let \(f\) be uniform among all \(n^n\) functions from \([n]\) to \([n]\), with \(n\ge2\). Write \(K_n\) for the number of vertices lying on directed cycles and \(L_n\) for the number of *origins*, vertices of indegree zero. Their dependence admits the following exact and asymptotic description.

**Origin deletion identity.** For each integer \(0\le t\le n-1\) and any real function \(h\) on \(\{1,\ldots,n\}\),
\[
\mathbb E[(L_n)_t h(K_n)]
=(n)_t\left(\frac{n-t}{n}\right)^n\mathbb E[h(K_{n-t})],
\]
where \((v)_t=v(v-1)\cdots(v-t+1)\), \((v)_0=1\), and the expectation on the right is for an independent uniform mapping of \(n-t\) labels. The identity holds for arbitrary \(h\), not only powers.

**Complete cyclic-core-conditioned origin law.** For all integers \(1\le k\le n\), the conditional probability generating function is
\[
\mathbb E[z^{L_n}\mid K_n=k]
=\sum_{t=0}^{n-k}\binom{n-k}{t}(z-1)^t
\left(1-\frac{t}{n}\right)^{n-k-1}.
\]
In particular,
\[
m_n(k):=\mathbb E[L_n\mid K_n=k]
=(n-k)\left(1-\frac1n\right)^{n-k-1},
\]
with \(m_n(n)=0\). For each \(1\le k<n\),
\[
m_n(k)-m_n(k+1)=\frac{k}{n}
\left(1-\frac1n\right)^{n-k-2}>0.
\]
Consequently \(\operatorname{Cov}(L_n,g(K_n))<0\) for every strictly increasing real function \(g\) on \(\{1,\ldots,n\}\). More generally the covariance is nonpositive for every nondecreasing \(g\).

**Second-order Rayleigh-scale regression and covariance.** If \(k_n\in\{1,\ldots,n\}\) and \(k_n/\sqrt n\to x\in[0,\infty)\), then
\[
\mathbb E[L_n\mid K_n=k_n]-\mathbb E L_n
\longrightarrow \frac1e\left(1-\frac{x^2}{2}\right).
\]
The covariance has the sharp asymptotic
\[
\operatorname{Cov}(K_n,L_n)
=-\frac{\sqrt{\pi/2}}{2e}\,\sqrt n+o(\sqrt n).
\]
The exact finite identity
\[
\operatorname{Cov}(K_n,L_n)
=n\left(1-\frac1n\right)^n
\bigl(\mathbb E K_{n-1}-\mathbb E K_n\bigr)
\]
provides a separate consistency check. In contrast, \(\operatorname{Var}(K_n)\asymp n\) and \(\operatorname{Var}(L_n)\asymp n\), so the correlation tends to zero.

## Assumptions and scope

Each of the \(n\) outgoing images is chosen independently and uniformly from \([n]\), permitting fixed points and loops. A vertex is cyclic if some positive iterate of the map returns to it. An origin has no incoming edges, including from itself. There is always at least one cyclic vertex; cyclic vertices have positive indegree, so origins are noncyclic. The formulas are exact for every integer \(n\ge2\), including the boundary \(k=n\); the origin-deletion identity only uses \(t\le n-1\), avoiding an undefined zero-label random mapping. Conditional generating polynomials use the convention that exponent zero selects the factor one; when \(k=n\), only the \(t=0\) term occurs.

## Proof

**1. Deleting specified origins.** Fix distinct labels \(v_1,\ldots,v_t\), with \(t\le n-1\). They are all origins precisely when none of the \(n\) images lands among them. This event has probability \(((n-t)/n)^n\). Conditional on it, images of the remaining \(n-t\) labels are independent uniform choices from the remaining labels, while images of the deleted labels also land among the remaining labels. Every deleted label has indegree zero and therefore cannot belong to any directed cycle; hence the number of cyclic vertices is distributed exactly as \(K_{n-t}\). Summing the identity against all \((n)_t\) ordered choices of labels gives the origin deletion identity for arbitrary \(h\).

**2. Counting the conditional forest.** The number of mappings with exactly \(k\) cyclic vertices is
\[
\binom nk k!\,k n^{n-k-1}=k(n)_k n^{n-k-1}.
\]
Indeed, select the cyclic vertex set, permute its \(k\) labels, and attach a labeled directed forest rooted at those vertices; the latter count is \(k n^{n-k-1}\). Dividing by \(n^n\) shows
\[
\Pr(K_n=k)=\frac{k(n)_k}{n^{k+1}},\qquad 1\le k\le n.
\]
Now condition on a particular cyclic set \(R\) of size \(k\). Its attached rooted forest is uniform over the \(k n^{n-k-1}\) forests. For a fixed set \(T\) of \(t\) nonroots, requiring every element of \(T\) to be an origin means each is a tree leaf. Delete them; the remaining forest has \(k(n-t)^{n-t-k-1}\) choices and each deleted label can choose its parent in \([n]\setminus T\) in \((n-t)^t\) ways. The ratio to the unrestricted forest count is
\[
\Pr(T\subseteq\{\text{origins}\}\mid K_n=k)
=\left(\frac{n-t}{n}\right)^{n-k-1}.
\]
This remains correct for \(t=n-k\), because the residual forest consists of the \(k\) roots and the Cayley forest expression equals one. Summing over ordered nonroot \(t\)-tuples gives
\[
\mathbb E[(L_n)_t\mid K_n=k]
=(n-k)_t\left(1-\frac tn\right)^{n-k-1}.
\]
Expanding \(z^{L_n}=(1+(z-1))^{L_n}\) yields the stated finite generating polynomial.

**3. Strict regression.** Put \(q=1-1/n\). For \(1\le k\le n-1\), direct cancellation gives
\[
(n-k)q^{n-k-1}-(n-k-1)q^{n-k-2}
=\frac{k}{n}q^{n-k-2},
\]
strictly positive, including \(k=n-1\) (when the expression equals one). For independent copies \(K,K'\) with the law of \(K_n\),
\[
2\operatorname{Cov}(m_n(K),g(K))
=\mathbb E[(m_n(K)-m_n(K'))(g(K)-g(K'))].
\]
The integrand is nonpositive for nondecreasing \(g\); it is strictly negative with positive probability for strictly increasing \(g\), since \(\Pr(K_n=k)>0\) for every \(1\le k\le n\). The tower property identifies this covariance with \(\operatorname{Cov}(L_n,g(K_n))\). The deletion identity for \(t=1\) with \(h(K)=K\) yields the exact covariance formula.

**4. Rayleigh scaling and uniform integrability.** The exact distribution above can be rewritten
\[
\Pr(K_n=k)=\frac kn\prod_{j=0}^{k-1}\left(1-\frac jn\right).
\]
For \(k/\sqrt n\to x>0\), the product tends to \(e^{-x^2/2}\). Its Gaussian upper bound \(\exp[-k(k-1)/(2n)]\) establishes both weak convergence of \(K_n/\sqrt n\) to the Rayleigh variable \(X\) of density \(x e^{-x^2/2}\), and uniform boundedness of all fixed positive moments of \(K_n/\sqrt n\). In particular,
\[
\mathbb EX=\sqrt{\pi/2},\quad
\mathbb EX^2=2,\quad
\mathbb EX^3=3\sqrt{\pi/2}.
\]
The elementary expansion, uniform for \(k=O(\sqrt n)\), is
\[
(n-k)q^{n-k-1}=
\frac ne+\frac1{2e}-\frac{k^2}{2en}+o(1).
\]
On the other hand \(\mathbb EL_n=nq^n=n/e-1/(2e)+o(1)\); subtraction yields the stated quadratic conditional displacement. To justify averaging this displacement against \(K_n/\sqrt n\), use the exact bound
\[
\left|m_n(k)-\mathbb EL_n\right|
\le q^{n-1}+\sum_{j=1}^{k-1}\frac jn
\le1+\frac{k^2}{2n},
\]
which follows from \(m_n(1)-\mathbb EL_n=q^{n-1}\) and the difference formula. Uniform bounded fourth moments imply uniform integrability of \((K_n/\sqrt n)(m_n(K_n)-\mathbb EL_n)\). Therefore
\[
\frac{\operatorname{Cov}(K_n,L_n)}{\sqrt n}
\to \frac1e\mathbb E\left[X\left(1-\frac{X^2}2\right)\right]
=-\frac{\sqrt{\pi/2}}{2e}.
\]
Finally \(\operatorname{Var}(K_n)/n\to2-\pi/2>0\) from Rayleigh moment convergence. For the origin count, ordinary empty-box covariance calculations give
\[
\operatorname{Var}(L_n)
=nq^n(1-q^n)+n(n-1)\bigl[(1-2/n)^n-q^{2n}\bigr]
=n(e^{-1}-2e^{-2})+O(1).
\]
These yield vanishing correlation as asserted.

## Verification

The standalone Python 3 standard-library checker `verify_random_mapping_origins.py` exhaustively enumerates all uniform mappings of sizes \(2\) through \(7\), checks cyclic-point probabilities, the complete conditional factorial-moment formula, the arbitrary-origin deletion law for low orders, exact covariance identities, and strict signs. It also checks exact algebraic formulas at sizes up to \(40\) and the asymptotic coefficient numerically at sizes \(500,2000,10000\). Run `python verify_random_mapping_origins.py`. The executed checker reported `PASS 1086 checks`. These finite computations are not used to infer the theorem for arbitrary \(n\); the analytic proof above covers all sizes.

## Relationship to prior work

Arney and Bender (1982) explicitly study origins and cyclic vertices in random mappings. Their Section 7 gives a generating-function calculus marking the number of origins and the **number of cycles**, rather than the number of *cyclic vertices*; their Sections 2, 5, and 9 give related marginal and local statistics. Hansen and Jaworski (arXiv:math/0603529v1, 22 March 2006), Theorem 1, give a general formula for the cyclic-vertex distribution in terms of exchangeable indegrees; that framework can encode origin statistics, so the present finite joint enumeration is not claimed to be independent of their broad framework. The intended added conclusions are the explicit whole-population deletion identity, the complete finite conditional law in elementary form, the strict antitone origin regression, and the quadratic Rayleigh-scale correction with its sharp covariance coefficient. Hansen and Jaworski (2010) provide further cyclic-core-conditioned component-size distribution results. General random-mapping generating functions in Flajolet and Odlyzko's classic work supply more background. No inspected primary statement was found giving this combination of conditional regression and second-order covariance; this is a claim of best-knowledge novelty, not proof of historical priority.

## Limitations

The results require independent uniform images and do not automatically extend to mappings with prescribed or nonuniform indegrees. The assertion is conditional *mean* monotonicity, not a first-order stochastic ordering of the entire leaf-count distribution. The regression limit holds when \(k/\sqrt n\) tends to a finite nonnegative number; no assertion is made for arbitrary larger scales. The covariance coefficient describes the leading term only, not an explicit finite error rate. Early work on origins, conditioned indegree sequences, and general random-mapping calculus may imply portions of these formulas after further derivation; independent historical-priority review has not been performed.

## References

1. J. Arney and E. A. Bender, *Random mappings with constraints on coalescence and number of origins*, Pacific J. Math. **103** (1982), 269–294. DOI: https://doi.org/10.2140/pjm.1982.103.269 ; open primary PDF: https://msp.org/pjm/1982/103-2/pjm-v103-n2-p03-p.pdf .
2. J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529v1 (first public 22 March 2006), https://arxiv.org/pdf/math/0603529 . Later journal article: *Random mappings with exchangeable in-degrees*, Random Structures & Algorithms **33** (2008), 105–126, DOI: https://doi.org/10.1002/rsa.20187 .
3. J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria **94** (2010), 341–359, https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/ .
4. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, in EUROCRYPT '89, LNCS 434 (1990), 329–354, DOI: https://doi.org/10.1007/3-540-46885-4_34 .
