# The complete conditional leaf-count stochastic-order diagram of a uniform Cayley tree

## Finding

**Theorem.** For every integer \(n\ge5\), let \(T_n\) be a uniform labeled *unrooted* tree on the vertex set \(\{1,\ldots,n\}\). Fix one vertex \(v\), write \(D=\deg_{T_n}(v)\) and let \(L\) be the number of leaves (vertices of degree one). For \(1\le d\le n-1\), put \(Q_d=\mathcal L(L\mid D=d)\). Let \(P\succ_{\mathrm{st}}Q\) mean that \(\Pr_P(X\ge t)\ge\Pr_Q(X\ge t)\) for every real \(t\), with a strict inequality for some \(t\).

The **complete strict first-order stochastic-order diagram** is

\[
Q_1\succ_{\mathrm{st}}Q_2,
\qquad Q_2\prec_{\mathrm{st}}Q_3\prec_{\mathrm{st}}\cdots\prec_{\mathrm{st}}Q_{n-1},
\qquad Q_{n-1}\succ_{\mathrm{st}}Q_1.
\]

For every integer \(d\) with \(3\le d\le n-2\), the distributions \(Q_1\) and \(Q_d\) are **incomparable**: neither stochastically dominates the other. The displayed relations and their transitive consequences comprise every comparable pair. At \(n=4\) the order is \(Q_2\prec_{\mathrm{st}}Q_1\prec_{\mathrm{st}}Q_3\); at \(n=3\), \(Q_1=Q_2\) (both give exactly two leaves).

There is a surprising distinction between dependence and covariance:
\[
\operatorname{Cov}(D,L)=0\qquad(n\ge3),
\]
although \(D\) and \(L\) are not independent. The degree-three and degree-one conditional expectations cross at an exact size threshold: \(\mathbb E[L\mid D=3]>\mathbb E[L\mid D=1]\) for \(4\le n\le8\), but the inequality reverses for all \(n\ge9\). This expectation reversal does not remove the stochastic incomparability for \(n\ge5\).

## Assumptions and scope

Every labeled unrooted tree is equally likely; the distinguished vertex is fixed *before* sampling. Both \(D\) and \(L\) refer to ordinary undirected vertex degree. Every conditioning event \(D=d\), for \(1\le d\le n-1\), has positive probability. Let \(E_m(t)\) denote the number of empty boxes after \(t\ge0\) independent draws uniformly selecting one of \(m\ge1\) boxes. Let \(\left\{{t\atop b}\right\}\) denote a Stirling number of the second kind, with \(\left\{{0\atop0}\right\}=1\).

The exact conditional law is
\[
Q_d=\mathcal L\left(E_{n-1}(n-d-1)+\mathbf1_{\{d=1\}}\right).
\]
Writing \(m=n-1\), \(t=n-d-1\), \(r=\ell-\mathbf1_{\{d=1\}}\) and \(b=m-r\), its point probabilities are
\[
\Pr(L=\ell\mid D=d)=
\frac{\binom mb\,b!\,\left\{{t\atop b}\right\}}{m^t}
\quad(0\le b\le m),
\]
with probability zero for inadmissible \(b\). Its expectation is
\[
\mathbb E[L\mid D=d]=\mathbf1_{\{d=1\}}+(n-1)
\left(\frac{n-2}{n-1}\right)^{n-d-1}.
\]

## Proof

**1. Coding and the exact law.** The Prüfer code of a uniform labeled tree is a uniform word of length \(n-2\) on \(n\) symbols, and each vertex degree is one plus its symbol multiplicity. Given \(D=d\), the distinguished symbol occurs exactly \(d-1\) times. At all remaining \(n-d-1\) code positions, conditional exchangeability and independence make the symbols iid uniform among the other \(n-1\) vertices. Such a vertex is a leaf precisely if its symbol is absent, and \(v\) itself is a leaf precisely when \(d=1\). This proves the occupancy representation. For exactly \(b\) occupied boxes, choose their labels and count surjections from \(t\) draws onto those boxes; the number is \(\binom mb b!\left\{{t\atop b}\right\}\). Division by \(m^t\) gives the mass function. Each non-distinguished vertex remains empty with probability \(((m-1)/m)^t\), yielding the expectation formula.

**2. Strict comparisons within degrees at least two.** Couple all empty-box counts by drawing one infinite iid sequence of box labels. Increasing the number of draws can only reduce the number of empty boxes. As \(d\) increases from \(2\) through \(n-1\), the required draw count \(n-d-1\) decreases by one. Each adjacent pair is strictly ordered because with positive probability the deleted draw is the first occurrence of its label. Therefore \(Q_2\prec_{\mathrm{st}}\cdots\prec_{\mathrm{st}}Q_{n-1}\).

**3. The extra leaf at degree one.** In the same coupling, let \(t=n-3\) and compare \(E_m(t)\) with \(1+E_m(t+1)\). Their difference is either zero or one, since a final draw can create at most one newly occupied box. The latter variable is the degree-one leaf count, the former the degree-two leaf count. The difference is strictly positive with positive probability: the final draw repeats an existing box label. Thus \(Q_1\succ_{\mathrm{st}}Q_2\). The star case \(d=n-1\) has \(L=n-1\) deterministically, whereas every other degree allows fewer than \(n-1\) leaves with positive probability, proving \(Q_{n-1}\succ_{\mathrm{st}}Q_1\).

**4. Every remaining comparison is impossible.** For \(n\ge5\), the degree-one law has minimum \(2\) and maximum \(n-1\), each occurring with positive probability: respectively all \(n-2\) code entries are distinct, or they all coincide. For \(3\le d\le n-2\), there are \(1\le n-d-1\le n-4\) remaining draws, so the degree-\(d\) law has minimum \(d\ge3\) (all draws hit different boxes) and maximum \(n-2\) (all hit one box), both with positive probability. Consequently \(Q_1\) assigns positive mass below the minimum of \(Q_d\), ruling out \(Q_1\succcurlyeq_{\mathrm{st}}Q_d\). Conversely \(Q_1\) assigns positive mass above the maximum of \(Q_d\), ruling out \(Q_d\succcurlyeq_{\mathrm{st}}Q_1\). These pairs are incomparable. This and steps 2–3 exhaust the diagram. For \(n=4\), \(Q_2\) is the constant two-leaf law and \(Q_3\) is the constant three-leaf law; the degree-one law is nonconstant between them. The case \(n=3\) is immediate.

**5. Zero covariance despite nonlinear dependence.** For any labeled tree, \(\sum_u\deg(u)=2(n-1)\) deterministically. By permutation symmetry, the quantity \(\operatorname{Cov}(\deg(u),L)\) is the same for each vertex \(u\). Summing over all \(u\) gives \(n\operatorname{Cov}(D,L)=\operatorname{Cov}(2(n-1),L)=0\). Yet the strict relation \(Q_1\succ_{\mathrm{st}}Q_2\) shows the conditional laws differ, so \(D\) and \(L\) are not independent.

**6. An exact conditional-mean reversal.** Set \(p=(n-2)/(n-1)\). The degree-three mean minus the degree-one mean equals
\[
\Delta_n=\frac{2n-3}{n-1}\,p^{\,n-4}-1.
\]
Direct exact fractions at \(n=4,5,6,7,8\) give respectively \(2/3,\ 5/16,\ 19/125,\ 79/1296,\ 41/16807\), all positive. At \(n=9,10\), they are \(-10039/262144\) and \(-326521/4782969\), both negative. For every \(n\ge11\), the prefactor is less than \(2\), while
\[
p^{n-4}\le\exp\!\left(-\frac{n-4}{n-1}\right)
\le e^{-7/10}<\frac12.
\]
The last strict bound follows from \(e^{7/10}>1+7/10+(7/10)^2/2+(7/10)^3/6>2\). Hence \(\Delta_n<0\) for all \(n\ge11\). The same expression shows \(\Delta_n\to2/e-1<0\).

## Verification

The accompanying standalone Python 3 file `verify.py` independently reconstructs every labeled tree by a heap-based Prüfer decoder for each \(3\le n\le8\), checks conditional probability masses by Stirling-number occupancy counting, checks every pairwise stochastic-order assertion including every claimed incomparability, and checks zero covariance with exact rational arithmetic. It separately checks the mean crossing for \(4\le n\le10\). The check executed successfully with **255 exact assertions over 280391 decoded labeled trees**. These finite checks do not establish the unrestricted theorem; the proof above supplies that argument.

To replay from a directory containing the files: `python3 verify.py`. The program needs only the Python standard library.

## Relationship to prior work

The Prüfer correspondence, its degree-multiplicity identity and all standard occupancy enumeration are classical and are *not* claimed as new. Addario-Berry, Donderwinkel, Maazoun and Martin (2021) develop coding methods and partial orders for random trees with given degrees, primarily to study geometry, height and related processes. Berzunza Ojeda, Holmgren and Janson (2023) analyze fringe subtree counts and asymptotic distributions with given degree statistics; their relevant public seminar predates the preprint. The present claim is restricted to a full first-order stochastic **comparability classification** of the global leaf count when one marked degree is conditioned, with a nonlinear-dependence/zero-covariance contrast and exact conditional-mean boundary. The classical degree-sequence enumerator implicitly determines its probability masses; therefore those masses, the marginal moments and the Prüfer coding identity are not themselves priority claims. Existing exact enumerators could permit derivations of some of this classification without stating it explicitly; historical priority remains open.

## Limitations

Only uniformly random *unrooted labeled* Cayley trees are considered. The marked vertex is fixed, not selected by degree. A conditional first-order stochastic ordering does not claim an almost-sure monotone coupling across all degree categories in the incomparable range. The diagram concerns sample-size-specific conditional distributions and is not a claim about arbitrary given-degree random trees. Any implicit coverage by old general joint generating functions is a residual priority risk. No independent scientific validation has been performed.

## References

- G. Berzunza Ojeda, C. Holmgren and S. Janson, *Fringe trees for random trees with given vertex degrees*, arXiv:2312.04243 (first preprint December 7, 2023); public seminar abstract dated April 13, 2023, Uppsala University.
- L. Addario-Berry, S. Donderwinkel, M. Maazoun and J. Martin, *The Foata–Fuchs proof of Cayley's formula, and its probabilistic uses*, arXiv:2107.09726 (first submitted July 20, 2021).
- H. Prüfer, *Neuer Beweis eines Satzes über Permutationen*, Archiv der Mathematik und Physik 27 (1918), 742–744 (classical coding).
