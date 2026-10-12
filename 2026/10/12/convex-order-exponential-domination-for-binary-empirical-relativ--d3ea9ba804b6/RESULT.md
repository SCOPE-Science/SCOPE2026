# Convex-order exponential domination for binary empirical relative entropy
## Finding
Let \(P=(p,1-p)\) with \(0<p<1\). Draw one observation \(I\sim P\), let \(\widehat P=\delta_I\), and define the empirical relative entropy
\[
V=D(\widehat P\|P)=-\log P(I).
\]
Write
\[
X=V-\mathbb EV.
\]
If \(E\sim\operatorname{Exp}(1)\), then
\[
X\preceq_{\mathrm{cx}}E-1.
\]
That is, for every convex function \(\phi\) for which both expectations exist,
\[
\mathbb E\phi(X)\le \mathbb E\phi(E-1).
\]
Equivalently, every stop-loss transform satisfies
\[
\mathbb E(X-a)_+\le \mathbb E(E-1-a)_+
\qquad\text{for every }a\in\mathbb R.
\]
A direct corollary is the centered-gamma moment-generating-function bound
\[
\log\mathbb E e^{tX}
\le
-t-\log(1-t),
\qquad 0\le t<1.
\]
The MGF inequality is already covered by the published information-concentration theorem for monotone log-concave discrete laws. The finding here is the stronger full convex-order statement.

## Assumptions and scope
The law \(P\) is binary and nondegenerate, and the sample size is exactly one. Natural logarithms are used. The claim compares the centered information content of a Bernoulli outcome with a centered unit exponential. It does not assert the same convex-order domination for larger sample sizes, larger alphabets, or arbitrary discrete laws.

## Proof
Relabel the two outcomes if necessary so that \(0<p\le q=1-p\). Put
\[
d=\log\frac{q}{p}\ge0.
\]
The centered information content has the two-point representation
\[
X=
\begin{cases}
qd,&\text{with probability }p,\\
-pd,&\text{with probability }q.
\end{cases}
\]
Indeed, the two information values differ by \(d\), and centering gives the displayed mean-zero pair.

First note that
\[
pd\le p\log\frac1p\le \frac1e<1.
\]
Hence the lower atom of \(X\) lies strictly above \(-1\), the lower endpoint of \(E-1\).

For a real threshold \(a\), define the stop-loss transform
\[
S_X(a)=\mathbb E(X-a)_+.
\]
For \(Y=E-1\),
\[
S_Y(a)=
\begin{cases}
-a,&a\le-1,\\
e^{-(1+a)},&a>-1.
\end{cases}
\]
For \(X\),
\[
S_X(a)=
\begin{cases}
-a,&a<-pd,\\
p(qd-a),&-pd\le a<qd,\\
0,&a\ge qd.
\end{cases}
\]

The comparison is now pointwise. If \(a\le-1\), the transforms agree. If \(-1<a<-pd\), put \(b=-a\in(0,1)\); then
\[
S_X(a)=b\le e^{b-1}=S_Y(a)
\]
by \(\log b\le b-1\). If \(a\ge qd\), the inequality is immediate.

It remains to take \(-pd\le a<qd\). The desired inequality is equivalent to
\[
R(a):=p(qd-a)e^{1+a}\le1.
\]
Its derivative has the sign of \(qd-a-1\). If \(d\ge1\), the unique maximizer on this interval is
\[
a_*=qd-1,
\]
and
\[
R(a_*)=p e^{qd}
=p^p q^q\le1.
\]
If \(d<1\), the critical point lies to the left of the interval, so \(R\) is decreasing there and
\[
R(a)\le R(-pd)
=pd\,e^{1-pd}\le1,
\]
because \(0\le pd<1\) and \(x e^{1-x}\le1\) for \(0\le x\le1\). Thus
\[
S_X(a)\le S_Y(a)
\]
for every real \(a\). Since \(X\) and \(Y\) are integrable and have the same mean zero, the stop-loss characterization of convex order gives
\[
X\preceq_{\mathrm{cx}}Y.
\]

Finally, \(x\mapsto e^{tx}\) is convex. For \(0\le t<1\),
\[
\mathbb E e^{t(E-1)}=\frac{e^{-t}}{1-t},
\]
which yields the stated MGF corollary.

## Verification
The proof is analytic and covers every \(0<p<1\) and every real stop-loss threshold. The bundled script `verify_binary_information_convex_order.py` independently constructs the centered two-point information law and the centered unit exponential stop-loss transform. It checks representative probabilities over many decades, thresholds spanning both supports, and the resulting MGF inequality for representative \(t\)-values. Its successful replay output is stored in `verification_output.txt`.

The finite computation is a regression check only. The universal quantifiers are established by the piecewise stop-loss proof above.

## Relationship to prior work
Bhatt and Pensia study concentration of centered empirical relative entropy and identify the binary statistic as the basic object in alphabet-reduction arguments. Their 2021 preprint does not state a convex-order comparison with a centered exponential.

Agrawal states the conjectured gamma MGF bound
\[
\log\mathbb E\exp\!\left(t(V_{n,k,P}-\mathbb EV_{n,k,P})\right)
\le
(k-1)\log\frac{e^{-t/n}}{1-t/n}
\]
for \(0\le t<n\). For \(n=1\) and \(k=2\), this is exactly the exponential-test-function corollary above.

Melbourne and Palafox-Castillo prove that the centered information content of every monotone log-concave discrete law obeys precisely this unit-gamma MGF bound. A Bernoulli probability sequence can be ordered monotonically and is log-concave, so their theorem already covers the MGF corollary in the present binary case. Their inspected information-concentration section derives exponential-moment and tail bounds from uniform varentropy control; it does not state that centered Bernoulli information content is below \(E-1\) in convex order. Their appendix recalls convex-order machinery for auxiliary nonnegative variables used in their majorization argument, but it does not give the centered-information-content comparison proved here.

Targeted searches for Bernoulli surprisal or information content in convex order with a shifted exponential did not locate an equivalent statement.

## Limitations
The full convex-order domination has only been proved here for a one-sample binary empirical distribution. The already-known MGF inequality must not be counted as new. The result does not imply the unresolved centered-gamma conjecture for \(n>1\) or \(k>2\). Because stochastic-order formulations of information content are scattered across information theory and reliability theory, an equivalent binary statement under different terminology remains a residual literature risk.

## References
Bhatt, A. and Pensia, A., *Sharp Concentration Inequalities for the Centered Relative Entropy*, arXiv:2109.09028v1, first public version 2021-09-18.

Melbourne, J. and Palafox-Castillo, G., *A discrete complement of Lyapunov's inequality and its information theoretic consequences*, arXiv:2111.06997v1, first public version 2021-11-13; later *Annals of Applied Probability* 33 (2023), 4322--4340.

Agrawal, R., *Finite-sample concentration of the empirical relative entropy around its mean*, arXiv:2203.00800v1, first public version 2022-03-02.
