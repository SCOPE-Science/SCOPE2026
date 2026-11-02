# A threshold-dependent distance–degree inversion at a third vertex in uniform Cayley trees

## Finding

Let \(n\ge3\), and let \(T_n\) be uniformly distributed over the \(n^{n-2}\) labeled trees on \([n]\). Fix three **distinct** vertices \(u,v,w\), and put \(L=d_{T_n}(u,v)\), \(H=\deg_{T_n}(w)\). The degree marker \(w\) is **not** one of the endpoints whose distance is measured.

**Exact conditional law.** For each integer \(1\le\ell\le n-2\), let \(B,J,C\) be mutually independent with
\[
B\sim\operatorname{Bin}\!\left(n-\ell-2,\frac1n\right),\quad
J\sim\operatorname{Bernoulli}\!\left(\frac{\ell-1}{n-2}\right),\quad
C\sim\operatorname{Bernoulli}\!\left(\frac1{\ell+1}\right).
\]
Then
\[
\boxed{H\mid(L=\ell)\ \overset d=\ 1+B+J(1+C).}
\tag{1}
\]
At the terminal length \(\ell=n-1\), \(H=2\) almost surely. Equivalently, for \(1\le\ell\le n-2\), with \(a(z)=1+(z-1)/n\) and \(p=(\ell-1)/(n-2)\),
\[
\boxed{\mathbb E[z^H\mid L=\ell]
=z\,a(z)^{n-\ell-2}\left[1-p+pz\frac{\ell+z}{\ell+1}\right].}
\tag{2}
\]

**Opposite dependence at different thresholds.** For every \(n\ge3\),
\[
\Pr(H\ge2\mid L=\ell)\quad\text{is strictly increasing in }\ell,
\qquad\operatorname{Cov}(L,\mathbf1_{\{H\ge2\}})>0.
\tag{3}
\]
Indeed, for \(1\le\ell\le n-2\), the exact leaf probability is
\[
\Pr(H=1\mid L=\ell)
=\frac{n-\ell-1}{n-2}\left(1-\frac1n\right)^{n-\ell-2},
\tag{4}
\]
with value zero at \(\ell=n-1\). Nevertheless, for \(n\ge4\), the two conditional laws at \(L=n-2\) and \(L=n-1\) are *incomparable* under first-order stochastic order: the first has positive probability of \(H\ge3\), whereas the second has \(H=2\) surely.

**Sharp high-degree asymptotics.** For every fixed integer \(q\ge2\), define
\[
 b_2=-e^{-1},\quad b_3=0,\quad
 b_q=\frac{e^{-1}(q-3)}{(q-2)!}\quad(q\ge4).
\]
Then
\[
\boxed{\lim_{n\to\infty}\sqrt n\,
 \operatorname{Cov}\bigl(L,\mathbf1_{\{H\ge q\}}\bigr)
 =-\frac12\sqrt{\frac\pi2}\,b_q.}
\tag{5}
\]
In particular the covariance is positive at the nonleaf threshold \(q=2\) for **every** \(n\ge3\), but is strictly negative for all sufficiently large \(n\) at **every fixed** threshold \(q\ge4\). At \(q=3\), equation (5) asserts a vanishing leading coefficient, not a finite-size sign classification.

The conditional mean, though not asserted to be new independently of the known endpoint law, satisfies
\[
\boxed{\mathbb E[H\mid L=\ell]
=2-\frac{2(\ell+2)(n-\ell-1)}{n(\ell+1)(n-2)},}
\tag{6}
\]
and is strictly increasing for \(1\le\ell\le n-1\). Thus a longer distance raises the third vertex's **mean degree** and its **nonleaf probability**, while it eventually has **negative covariance with every fixed high-degree tail beginning at four**. This separation of mean and tail dependence is the substantive conclusion.

## Assumptions and scope

All trees are unrooted, simple, connected, uniformly sampled and labeled. The three labels \(u,v,w\) remain distinct and fixed; label symmetry allows taking them as \(1,2,3\). The graph distance counts edges. The threshold \(q\) in (5) is fixed before \(n\to\infty\). Independence in (1) is an equality in conditional distribution, not a coupling asserted simultaneously at all different lengths. The strict inequality in (3) requires \(n\ge3\). The stochastic-order incomparability requires \(n\ge4\). No assertion of a universal sign for \(q=3\) is made.

## Proof

**1. Fixing the marked path.** Suppose that the \(u\)-to-\(v\) path has \(\ell\) edges and a specified ordered list of \(\ell-1\) internal labels. Put \(m=\ell+1\) and \(r=n-m\). Removing the path edges from a completion gives a directed forest on all \(n\) labels, oriented toward the \(m\) path vertices as prescribed roots. Conversely, each such forest gives exactly one completed tree. By the rooted-forest matrix-tree formula, the number of completions is
\[
\det(nI_r-\mathbf1_r\mathbf1_r^{\mathsf T})=m n^{r-1}
\qquad(r\ge1).
\tag{7}
\]
For \(r=0\), there is one completion. All ordered internal label lists have the same count, hence, conditional on \(L=\ell\), vertex \(w\) occurs internally on the marked path with probability \(p=(\ell-1)/(n-2)\). In particular
\[
\Pr(L=\ell)=\frac{(\ell+1)(n-2)_{\ell-1}}{n^\ell},
\qquad 1\le\ell\le n-1,
\tag{8}
\]
where \((a)_j\) is the descending factorial, with the empty product equal to one.

**2. Marking the incident edges.** If \(w\) is one of the \(m\) prescribed path roots and has two neighbors already on the path, give each additional incident forest edge weight \(z\). The root-deleted weighted Laplacian has diagonal shift \(z-1\), so its determinant is
\[
\det\bigl((n+z-1)I_r-\mathbf1_r\mathbf1_r^{\mathsf T}\bigr)
=(n+z-1)^{r-1}(m+z-1).
\tag{9}
\]
Dividing by (7), its additional degree has generating function
\[
\left(1+\frac{z-1}{n}\right)^{r-1}
\left(1+\frac{z-1}{m}\right).
\tag{10}
\]
This is the product generating function of an independent binomial and Bernoulli variable. Hence the full path-internal degree is \(2+B+C\).

If instead \(w\) is outside the prescribed path, weighting **every** edge incident to \(w\) gives, after ordering \(w\) first among the \(r\) nonroots, the root-deleted Laplacian
\[
\begin{pmatrix}
(n-1)z&-z\mathbf1_{r-1}^{\mathsf T}\\
-z\mathbf1_{r-1}&(n+z-1)I_{r-1}-\mathbf1_{r-1}\mathbf1_{r-1}^{\mathsf T}
\end{pmatrix}.
\]
Its determinant is \(m z(n+z-1)^{r-1}\). Division by (7) yields degree generating function \(z(1+(z-1)/n)^{r-1}\): the degree is \(1+B\). Both formulas also hold at \(r=1\), where the exponents equal zero. Mixing the two path-membership cases proves (1) and (2). When \(r=0\), the entire tree is the marked path and \(w\) has degree two.

**3. A strict nonleaf regression but no global stochastic order.** The probability of a leaf is the outside-path weight \(1-p=(n-\ell-1)/(n-2)\) times \(\Pr(B=0)\); this proves (4). Put \(s=n-\ell-1\). For \(1\le s\le n-2\), the sequence \(s(1-1/n)^{s-1}\) is strictly increasing with \(s\), because the ratio for the next \(s\) is \((1+1/s)(1-1/n)>1\). Therefore (4) decreases strictly with \(\ell\); the terminal leaf probability is zero. Conditioning on \(L\) then proves the positive covariance in (3), since \(L\) has at least two possible values.

For \(n\ge4\), at \(\ell=n-2\) the binomial in (1) is zero, and
\[
 \Pr(H\ge2\mid L=n-2)=\frac{n-3}{n-2}<1,
 \quad
 \Pr(H\ge3\mid L=n-2)
 =\frac{n-3}{(n-2)(n-1)}>0.
\]
At \(\ell=n-1\), those probabilities are one and zero respectively. The opposing inequalities prove stochastic-order incomparability. Direct expectation of (1) gives (6); for successive lengths its increment is
\[
\frac{2(\ell^2+3\ell+n+2)}{n(\ell+1)(\ell+2)(n-2)}>0.
\]
This is a statement about the mean, not about increasing stochastic order.

**4. Rayleigh scaling and cancellation of first-order tail effects.** Formula (8) gives \(X_n=L/\sqrt n\Rightarrow X\), where \(X\) has Rayleigh density \(x e^{-x^2/2}\) for \(x>0\). The product form
\[
\Pr(L=\ell)=\frac{\ell+1}{n}
\prod_{j=2}^{\ell}\left(1-\frac jn\right)
\le\frac{\ell+1}{n}
\exp\left(-\frac{\ell(\ell+1)-2}{2n}\right)
\tag{11}
\]
provides uniform bounds on scaled moments and permits polynomially weighted tail truncation.

Fix a compact interval of positive \(x\)'s, put \(\ell=x\sqrt n\) along integer values, and write \(t=z-1\). Uniformly for bounded complex \(z\), the conditional probability generating function (2) satisfies
\[
\mathbb E[z^H\mid L=\ell]
=z e^t\left[1+\frac1n\left(-2t+\frac{1-x^2}{2}t^2\right)
+O(n^{-3/2})\right].
\tag{12}
\]
The unconditional Prüfer-code distribution \(H\overset d=1+\operatorname{Bin}(n-2,1/n)\) gives
\[
\mathbb E[z^H]
=z e^t\left[1+\frac1n\left(-2t-\frac12t^2\right)
+O(n^{-2})\right].
\tag{13}
\]
The potentially dominant order-\(n^{-1/2}\) terms **cancel** between the loss of off-path offspring and the increasing chance of lying on the path. Subtracting (13) from (12) gives
\[
\mathbb E[z^H\mid L=\ell]-\mathbb E[z^H]
=\frac{2-x^2}{2n}\,z e^{z-1}(z-1)^2+O(n^{-3/2}).
\tag{14}
\]
For each fixed integer \(q\ge2\), taking the sum of coefficients corresponding to degrees at least \(q\), the coefficient of the signed generating function \(z e^{z-1}(z-1)^2\) is
\[
 \Pr(Y=q-3)-\Pr(Y=q-2)=b_q,
 \qquad Y\sim\operatorname{Poisson}(1),
\tag{15}
\]
with the convention that negative Poisson indices have probability zero. This yields exactly the constants in the finding.

For completeness, the passage from local expansion to covariance is justified by (11) and the following uniform truncation bound: for \(\ell\le n/2\) and bounded \(z\), the difference of the conditional and unconditional generating functions is bounded by a constant times \((1+\ell^2/n)/n\). One sees this directly by writing their ratio as
\[
\left(1+\frac tn\right)^{-\ell}
\left[1+\frac{\ell-1}{n-2}
\left(z\frac{\ell+z}{\ell+1}-1\right)\right]
\]
and cancelling the linear \(\ell t/n\) terms; the remaining terms are bounded by second-order remainders. By Cauchy coefficient estimates the same bound holds for the fixed-degree tail difference. The contribution from \(\ell>n/2\) is exponentially small by (11). Thus the portion with \(x\notin[\delta,M]\) can be made arbitrarily small after multiplying the covariance by \(\sqrt n\), first letting \(n\to\infty\), then \(\delta\downarrow0\) and \(M\to\infty\).

Using (14)–(15) and \(\operatorname{Cov}(L,\mathbf1_{\{H\ge q\}})=\mathbb E[(L-\mathbb EL)(\Pr(H\ge q\mid L)-\Pr(H\ge q))]\), we obtain
\[
\lim_{n\to\infty}\sqrt n\operatorname{Cov}(L,\mathbf1_{\{H\ge q\}})
=\frac{b_q}{2}\operatorname{Cov}(X,2-X^2)
=-\frac{b_q}{2}\sqrt{\frac\pi2},
\]
since \(\mathbb EX=\sqrt{\pi/2}\), \(\mathbb EX^2=2\) and \(\mathbb EX^3=3\sqrt{\pi/2}\). This proves (5).

## Verification

The standalone script `verify_third_vertex_degree.py` implements the exact conditional joint distribution of path membership and degree, and independently enumerates every Prüfer code for \(3\le n\le8\). It compares all nonzero and zero joint cells, the path-length probabilities, leaf probabilities, means and boundary cases using rational arithmetic. Further exact arithmetic checks test strict nonleaf regression, mean regression and stochastic-order incomparability through \(n=104\), plus a degree-sum covariance identity through \(n=54\). Larger-size floating-point tests examine the predicted sign inversion but are **not** a proof of the asymptotic theorem. The complete script runs under standard Python 3 with no external dependencies.

## Relationship to prior work

The rooted-forest extension count and Cayley multinomial framework are classical; Pitman's 1996 publicly dated technical report (later published in 1999) explicitly contains the rooted-forest count and Moon's unrooted forest-extension theorem. Aldous and Pitman's 1998 technical report gives a general \(p\)-tree spanning-subtree formula and discusses the membership of a third vertex on a marked path. Those results are used as background, **not** claimed new here. Neither inspected text states the path-conditioned degree law for a *third* vertex, its stochastic-order obstruction, or the threshold-dependent covariance constants in (5).

A separately published study of **endpoint** degree versus marked-pair distance proves the endpoint binomial–Bernoulli distribution and strictly negative stochastic regression. By degree conservation, its conditional mean formula already implies (6), so (6) is **not** an independent novelty claim. It does not furnish the nonendpoint **degree distribution** (1) or the high-degree sign reversal (5). The Cambridge open text by Berzunza Ojeda and Janson treats distance profiles and conditioning on the root degree of simply generated trees, but its inspected sections do not assert these three-marked-vertex finite laws. General forest identities can be specialized to derive parts of the present statement; whether an equivalent full threshold theorem appears under different terminology remains the main historical-priority uncertainty.

## Limitations

The result applies to uniform labeled Cayley trees, not arbitrary conditioned Galton–Watson trees or nonuniform weighted trees. The negative covariance in (5) holds for each **fixed** threshold \(q\ge4\) once \(n\) is sufficiently large; no explicit all-\(n\) cutoff is asserted. The leading constant at \(q=3\) is zero, and its sign beyond leading order is not resolved here. The pointwise conditional tail probabilities at thresholds at least three need not be monotone; the negative result is about their **unconditional covariance** with length. No independent historical-priority or correctness audit is claimed.

## References

1. J. Pitman, “Coalescent Random Forests,” Berkeley Statistics Technical Report 457, catalog first public date 1996-09-01, [technical-report record](https://statistics.berkeley.edu/tech-reports/457), [full text](https://statistics.berkeley.edu/sites/default/files/tech-reports/457.pdf). The revised report's displayed date is later and is not used as the first-public anchor.
2. D. Aldous and J. Pitman, “A Family of Random Trees with Random Edge Lengths,” Berkeley Statistics Technical Report 526, [1998 catalog](https://live-statistics.pantheon.berkeley.edu/tech-reports/526), [full text](https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/526.pdf). See discrete \(p\)-trees, Lemmas 4–5 and the spanning-subtree discussion.
3. “Exact negative regression between endpoint degree and distance in a uniform Cayley tree,” [public mathematical record](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae), specifically `RESULT.md`.
4. G. Berzunza Ojeda and S. Janson, “The distance profile of rooted and unrooted simply generated trees,” *Combinatorics, Probability and Computing* **31** (2022), 368–410, [open full text](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/distance-profile-of-rooted-and-unrooted-simply-generated-trees/B32482FCA00F9FCF73A32330A3396DF3).
