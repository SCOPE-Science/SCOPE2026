# A sharp one-sided pair-cover bound for Johnson walks

## Finding

Fix an integer \(r\ge3\). Let \(H_1,H_2,\ldots\) be the Markov chain on the \(r\)-subsets of \([n]\) obtained by deleting one uniformly chosen present element and adding one uniformly chosen absent element at each transition; take \(H_1\) uniform. For \(n\ge r+2\), let \(T_{n,r}\) be the first index by which every unordered pair of \([n]\) has appeared in some \(H_t\). Put \(m=\binom n2\), \(a=2/(n-r)\), and
\[
\delta_{n,r}=\frac{4(r-1)}{(n-r)\left(n+2r-2+\sqrt{(n+2r-2)^2-8r(r-1)}\right)},\quad \lambda_{n,r}=1-\delta_{n,r},\quad h_{n,r}=1-\frac{\delta_{n,r}(n-r)}2.
\]
Then \(0<h_{n,r}<1\), and, for every integer \(t\ge1\), the number \(U_t\) of unordered pairs never observed in \(H_1,\ldots,H_t\) satisfies the finite bounds
\[
 m\left(1-\frac{r(r-1)}{n(n-1)}\right)h_{n,r}\lambda_{n,r}^{t-1}\le\mathbb E U_t\le\frac{m}{h_{n,r}}\lambda_{n,r}^{t-1}.
\]
In particular, with \(K=1+\lceil\log(m/h_{n,r})/[-\log\lambda_{n,r}]\rceil\),
\[
\mathbb E T_{n,r}\le K+\delta_{n,r}^{-1},\qquad
\limsup_{n\to\infty}\frac{\mathbb E T_{n,r}}{\frac{m}{r-1}\log m}\le1.
\]
For fixed \(r\), every real \(x\), and \(t_n=\lceil(\log m+x)/\delta_{n,r}\rceil\),
\[
\mathbb E U_{t_n}\longrightarrow e^{-x},\qquad
\limsup_{n\to\infty}\Pr(T_{n,r}>t_n)\le e^{-x}.
\]
The limsup is the conjectured *upper* constant for pair super-coupon collection under Johnson-walk dependence; it is **not** a matching lower bound or a limiting law for the cover time.

## Assumptions and scope

Throughout, \(r\ge3\) is an arbitrary fixed integer and \(n\ge r+2\). There is one Markov step between consecutive rounds; the first round is numbered one. The chain starts at stationarity (uniform among \(r\)-subsets), although the upper probability bound also holds from any starting state. Each pair counts as observed on the first round whose \(r\)-subset contains it. The asymptotic statements take \(n\to\infty\) with \(r\) held fixed; no uniform-in-\(r\) claim is made.

## Proof

Fix \(S=\{u,v\}\). Before its first observation, the intersection \(J_t=|H_t\cap S|\) is in \(\{0,1\}\). Its killed transition matrix, with rows and columns indexed by \(0,1\), is
\[
Q=\begin{pmatrix}1-a&a\\ b&1-b-c\end{pmatrix},\quad
 a=\frac2{n-r},\quad b=\frac{n-r-1}{r(n-r)},\quad c=\frac{r-1}{r(n-r)}.
\]
Indeed, from intersection zero the inserted coupon is one of the two marked elements with probability \(a\). From intersection one, deleting the sole marked element and inserting an unmarked element has probability \(b\), whereas deleting an unmarked element and inserting the other marked element (which observes the pair) has probability \(c\). The remaining probability stays at intersection one. Since \(a,b,c>0\), \(Q\) is irreducible and strictly substochastic; its Perron eigenvalue \(\lambda\) lies in \((0,1)\). Writing \(\lambda=1-\delta\), the characteristic equation gives
\[
\delta^2-(a+b+c)\delta+ac=0.
\]
Its smaller positive root is the displayed \(\delta_{n,r}\), after rationalization. Perron--Frobenius and the first row give the positive right eigenvector \(v=(1,h)^\top\) with \(h=1-\delta/a\); positivity implies \(0<h<1\). Since \(v\le\mathbf1\le v/h\) componentwise, multiplying by \(Q^{t-1}\), which has nonnegative entries, yields
\[
(\pi v)\lambda^{t-1}\le\pi Q^{t-1}\mathbf1\le(\pi v/h)\lambda^{t-1}
\]
for every nonnegative initial row distribution \(\pi\) supported on the unobserved states. For a uniform initial \(H_1\),
\[
\pi_0=\frac{(n-r)(n-r-1)}{n(n-1)},\qquad
\pi_1=\frac{2r(n-r)}{n(n-1)},\qquad
\pi_2=\frac{r(r-1)}{n(n-1)}.
\]
Thus \(\pi v\ge(1-\pi_2)h\) and \(\pi v/h\le 1/h\). By symmetry, every pair has this survival probability. Linearity of expectation yields both bounds on \(\mathbb E U_t\), without any assumption of independence among distinct pairs.

As \(\{T_{n,r}>t\}=\{U_t>0\}\), Markov's inequality gives \(\Pr(T_{n,r}>t)\le\min\{1,mh^{-1}\lambda^{t-1}\}\) for every \(t\ge1\). By the definition of \(K\), the geometric tail starting at \(t=K\) sums to at most \(1/(1-\lambda)=1/\delta\); the first \(K\) terms sum to at most \(K\). This proves the finite expectation inequality.

Finally, at fixed \(r\), rationalizing the root shows
\[
\delta_{n,r}=\frac{2(r-1)}{n^2}\bigl(1+O_r(n^{-1})\bigr),\quad h_{n,r}=1+O_r(n^{-1}).
\]
Hence \([-\log\lambda]/\delta\to1\), \(\delta\log m\to0\), and \(\delta^{-1}\sim m/(r-1)\). Dividing the finite expectation bound by \(\delta^{-1}\log m\) yields the limsup. At \(t_n\), \(m\lambda^{t_n-1}\to e^{-x}\); the two uniform-in-time bounds squeeze \(\mathbb E U_{t_n}\) to the claimed value. The tail bound follows again by Markov's inequality. \(\square\)

## Verification

The accompanying `verify.py` uses exact rational arithmetic to enumerate all Johnson-walk transitions on \(r\)-subsets of \([n]\) for \(5\le n\le10\), \(3\le r\le n-2\), and the first seven observation rounds. It confirms the two-state killed recurrence and the stationary hypergeometric starting distribution. It also checks the Perron eigenvector and asymptotic rate numerically. These finite checks corroborate, but do not replace, the algebraic proof for unbounded \(n\).

## Relationship to prior work

Athreya, S. Mukherjee and S. S. Mukherjee formulated the Markovian super-coupon cover-time conjecture for general \(r\ge s\), and proved its \(r=s\) case. The conjectured expected cover time is \(\frac rs\binom rs^{-1}\binom ns\log\binom ns\,(1+o(1))\). At \(s=2\), this scale equals \(\frac{\binom n2}{r-1}\log\binom n2\). Their independent-round super-coupon theorem does not apply to the Markovian walk, and their Johnson-graph cover theorem addresses \(r=s\), not \(r>2=s\). The present killed-pair calculation gives the sharp conjectured leading *upper bound* in this unresolved dependent case. A sharper lower bound would require controlling simultaneous survivals of different pairs.

## Limitations

Only the upper constant for the expected pair-cover time is proved; the matching lower asymptotic and an extreme-value limit remain unproved. The exact Perron root concerns avoidance of a **fixed pair**, not a joint survival probability for many pairs. The asymptotic proof fixes \(r\) as \(n\to\infty\); the finite inequalities apply to all integers \(n\ge r+2\). An equivalent earlier consequence of a general hitting-set theorem remains a residual priority possibility.

## References

1. S. Athreya, S. Mukherjee and S. S. Mukherjee, *On a Generalisation of the Coupon Collector Problem*, arXiv:2304.01145, first public version 2023-04-03, Conjecture 2.4 and Theorem 2.5. https://arxiv.org/abs/2304.01145
2. N. Rivera, T. Sauerwald and J. Sylvester, *Multiple random walks on graphs: mixing few to cover many*, Combinatorics, Probability and Computing 32 (2023), 594–637. https://doi.org/10.1017/S0963548322000372
