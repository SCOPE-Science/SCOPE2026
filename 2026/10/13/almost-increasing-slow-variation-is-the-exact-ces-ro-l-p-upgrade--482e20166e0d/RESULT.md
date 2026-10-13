# Almost-increasing slow variation is the exact Cesàro-\(L^p\) upgrade boundary
## Finding
Fix
\[
1\le p<2.
\]
Let \(L:[0,\infty)\to(0,\infty)\) be measurable and slowly varying at infinity, and assume \(L\) is bounded above and bounded away from zero on each compact interval. Choose any de Bruijn conjugate \(\widetilde L\), and define
\[
b_n=\bigl(n\widetilde L(n)\bigr)^{1/p}.
\]
For a rowwise independent triangular array of integrable random variables
\[
\{X_{n,i}:1\le i\le n,\ n\ge1\},
\]
write
\[
W_{n,i}=|X_{n,i}|^pL(|X_{n,i}|^p),
\qquad
M_n=\max_{1\le j\le n}\left|\sum_{i=1}^j(X_{n,i}-EX_{n,i})\right|.
\]
Suppose the array \(W\) is uniformly integrable in the Cesàro sense:
\[
\mathcal U(A):=
\sup_{n\ge1}\frac1n\sum_{i=1}^n
E\left[W_{n,i}\mathbf1_{\{|X_{n,i}|>A\}}\right]
\xrightarrow[A\to\infty]{}0.
\tag{1}
\]
Then the following are equivalent:

**(a) Eventual almost increase.** There exist \(x_0>0\) and \(K<\infty\) such that
\[
L(u)\le K L(v)
\quad\text{whenever}\quad x_0\le u\le v.
\tag{2}
\]

**(b) Universal maximal mean convergence.** Every such rowwise independent array satisfying (1) obeys
\[
E\left[\left(\frac{M_n}{b_n}\right)^p\right]
\longrightarrow0.
\tag{3}
\]

In fact, if (2) fails, there exists an array of rowwise independent symmetric three-point distributions, identically distributed within each nonzero row and with finite moments of every order for each variable, satisfying (1), for which
\[
M_n/b_n\xrightarrow{\mathbb P}0
\quad\text{but}\quad
\limsup_{n\to\infty}E[(M_n/b_n)^p]=\infty.
\tag{4}
\]

The boundary is nontrivial even among weights bounded below by one. Define
\[
L_{\mathrm{osc}}(x)=
\exp\!\left(\sqrt{\log(e+x)}
\,[1+\sin(\log\log(e+x))]\right).
\tag{5}
\]
This weight is slowly varying, satisfies \(L_{\mathrm{osc}}(x)\ge1\), and violates (2), so (4) holds for it. On the other hand, \(L(x)=2+\sin(\log\log(e^e+x))\) is bounded between one and three, hence satisfies (2), although it is not monotone.

## Assumptions and scope
The independent variables may have different distributions across rows; only independence *within each row* is needed for (3). In the obstruction (4), all entries in a nonzero row are even identically distributed and symmetric. The theorem is universal over the full class of arrays satisfying (1); it does not assert that (2) is necessary for a particular fixed array.

The normalization is associated with the *same* slowly varying function appearing in the moment weight. A de Bruijn conjugate is any slowly varying positive function satisfying
\[
\widetilde L(t)L(t\widetilde L(t))\longrightarrow1.
\tag{6}
\]
Its asymptotic equivalence class is unique, and the limiting property (3) is independent of which representative is used.

The local bounds on \(L\) eliminate irrelevant pathologies on compact intervals. The rate parameter \(p\) may equal one, but the quadratic truncation method requires \(p<2\).

## Proof
Introduce
\[
G(x)=xL(x),\qquad H(x)=x^pL(x^p).
\]
Then \(G\) is regularly varying with index one and \(H\) is regularly varying with index \(p\). From (6),
\[
G(b_n^p)\sim n,
\qquad b_n\to\infty,
\qquad \frac n{b_n^2}\to0.
\tag{7}
\]
The last limit follows because \(b_n\) is regularly varying with index \(1/p>1/2\).

**Sufficiency.** Assume (2). Fix \(\eta\in(0,2-p)\). Potter's comparison for \(H\) gives constants \(A_0,C>0\) such that, whenever \(A_0\le x\le b_n\) and \(n\) is large enough,
\[
\frac{x^2}{b_n^2}
\le C\frac{H(x)}{H(b_n)}.
\tag{8}
\]
Indeed, the lower Potter bound is proportional to \((x/b_n)^{p+\eta}\), and \(p+\eta<2\).

Split each variable at \(b_n\):
\[
Y_{n,i}=X_{n,i}\mathbf1_{\{|X_{n,i}|\le b_n\}},
\qquad
R_{n,i}=X_{n,i}-Y_{n,i}.
\]
For any fixed \(A\ge A_0\), (8) and (1) imply
\[
\frac1{b_n^2}\sum_{i=1}^n E[Y_{n,i}^2]
\le\frac{nA^2}{b_n^2}
+C\frac{n}{H(b_n)}\mathcal U(A).
\tag{9}
\]
By (7), first let \(n\to\infty\), then \(A\to\infty\), to conclude
\[
\frac1{b_n^2}\sum_{i=1}^n E[Y_{n,i}^2]\longrightarrow0.
\tag{10}
\]
The centered \(Y_{n,i}\)'s are independent. Doob's maximal \(L^2\) inequality, followed by Jensen's inequality, yields
\[
E\left[\left(
\frac1{b_n}\max_{j\le n}
\left|\sum_{i=1}^j(Y_{n,i}-EY_{n,i})\right|
\right)^p\right]
\le\left(\frac4{b_n^2}\sum_{i=1}^n E[Y_{n,i}^2]\right)^{p/2}
\longrightarrow0.
\tag{11}
\]

By (2), for large \(n\) and \(|X_{n,i}|>b_n\),
\[
L(b_n^p)\le K L(|X_{n,i}|^p).
\]
Consequently
\[
\frac1{b_n^p}\sum_{i=1}^nE|R_{n,i}|^p
\le K\frac{n}{H(b_n)}\mathcal U(b_n)
\longrightarrow0.
\tag{12}
\]
For \(1<p<2\), the von Bahr--Esseen inequality and Doob's maximal \(L^p\) inequality bound the maximal \(p\)-moment of the centered independent \(R_{n,i}\)'s by a constant depending only on \(p\) times \(\sum_iE|R_{n,i}|^p\). For \(p=1\), the triangle inequality gives the same bound with constant two. Equation (12), together with (11), proves (3).

**Necessity.** Suppose (2) fails. For each \(m\ge2\), select real numbers
\[
u_m<v_m,\qquad u_m\to\infty,
\qquad \frac{L(u_m)}{L(v_m)}\ge m^3.
\tag{13}
\]
The choices can be made with \(u_m\) and the indices below strictly increasing. Put
\[
n_m=\lfloor G(u_m)\rfloor,
\qquad q_m=\frac1{mG(v_m)}.
\tag{14}
\]
Since \(G\) is regularly varying with index one, \(G(u_m)\to\infty\) and the asymptotic inverse relation in (7) gives
\[
\frac{b_{n_m}^p}{u_m}\longrightarrow1.
\tag{15}
\]
Potter's bound with index smaller than one shows that
\[
\frac{G(u_m)}{G(v_m)}\le C
\quad\text{for }u_m\le v_m\text{ large},
\]
so
\[
n_mq_m\le C/m\longrightarrow0.
\tag{16}
\]
On each special row \(n=n_m\), take \(n_m\) independent identically distributed variables with law
\[
P(X_{n_m,i}=0)=1-q_m,
\quad
P(X_{n_m,i}=v_m^{1/p})
=P(X_{n_m,i}=-v_m^{1/p})=q_m/2.
\tag{17}
\]
On every other row, take zero variables. Each variable in (17) has mean zero and moments of every finite order. On a special row, the Cesàro mean of \(W\) equals
\[
\frac1{n_m}\sum_{i=1}^{n_m}EW_{n_m,i}
=q_mG(v_m)=\frac1m.
\]
Thus for every fixed \(A\),
\[
\mathcal U(A)=
\sup_{m\ge2}\frac1m\mathbf1_{\{v_m^{1/p}>A\}}
\longrightarrow0
\quad(A\to\infty),
\tag{18}
\]
because finitely many early rows eventually disappear from the supremum and all later rows contribute at most \(1/m\).

The probability that any variable on row \(n_m\) is nonzero is at most \(n_mq_m\to0\), proving the probability convergence in (4). On the event that exactly one variable on the row is nonzero, its maximal centered partial sum equals \(v_m^{1/p}\). Therefore
\[
E\left[\left(\frac{M_{n_m}}{b_{n_m}}\right)^p\right]
\ge
n_mq_m(1-q_m)^{n_m-1}\frac{v_m}{b_{n_m}^p}.
\tag{19}
\]
By (14)--(16), the right side is
\[
(1+o(1))\frac{L(u_m)}{mL(v_m)}
\ge (1+o(1))m^2\longrightarrow\infty.
\tag{20}
\]
This disproves universal mean convergence whenever (2) fails and completes the equivalence.

Finally, set \(t=\log(e+x)\) and \(f(t)=\sqrt t\,[1+\sin(\log t)]\). Then
\[
f'(t)=\frac{1+\sin(\log t)}{2\sqrt t}
+\frac{\cos(\log t)}{\sqrt t}\longrightarrow0.
\]
Thus \(L_{\mathrm{osc}}(cx)/L_{\mathrm{osc}}(x)\to1\) for every fixed \(c>0\). At the increasing pairs
\[
u_m=\exp(\exp(\pi/2+2\pi m))-e,
\quad
v_m=\exp(\exp(3\pi/2+2\pi m))-e,
\]
one has
\[
L_{\mathrm{osc}}(u_m)
=\exp\!\left(2\sqrt{\exp(\pi/2+2\pi m)}\right),
\qquad
L_{\mathrm{osc}}(v_m)=1.
\]
This proves the claimed explicit \(L\ge1\) boundary example.

## Verification
The standalone standard-library script `verify.py` replays a constructive decreasing-weight example by solving \(x/\log(e+x)=n\) through deterministic bisection. It uses the asymptotically equivalent inverse normalization rather than any particular choice of de Bruijn conjugate and checks that the single-spike lower bound grows on the predicted scale.

The script also checks the exact peak/trough formulas for (5), an example of a bounded nonmonotone but almost-increasing slowly varying weight, and the probability bound in (16) in logarithmic coordinates.

A successful run ends with `VERIFY_OK ratios=4.000,9.000,16.000,25.000 oscillation=unbounded`.

These finite computations are only checks. The universal equivalence and all infinite limits are proved analytically above.

## Relationship to prior work
Thành's 2022 preprint establishes a weak law for normalized maximal partial sums under Cesàro uniform integrability of the regularly varying moment weight, and explicitly asks whether convergence in \(L^p\) follows even for independent variables.

The same author's later paper gives an affirmative answer when \(L\) is increasing and \(L\ge1\) (Theorem 4.1, in the larger dependent-row class satisfying a maximal second-moment inequality), and develops general sufficient and necessary tail conditions (Theorem 3.1). Its Example 4.2 demonstrates failure for a decreasing weight tending to zero, using a common distribution with infinite ordinary \(p\)-moment.

The present theorem does not reassert that already settled open question. Instead it classifies the slowly varying weights for which *every* independent-row array enjoys the upgrade. Eventual almost increase is exactly necessary and sufficient. The positive half permits nonmonotone weights, and the negative half applies to every weight outside this class, even when the weight remains at least one and every individual random variable has finite moments of all orders. The existing sufficient theorem does not state this universal function-class boundary, and its one counterexample does not imply the necessity for all non-almost-increasing weights.

Earlier weighted-integrability and mean-convergence work treats different array conditions or gives sufficient criteria without the sharp function-level equivalence above. Targeted literature searches for the equivalent quasi-increasing, monotone-envelope, uniform-Cesàro, and regularly varying tail formulations did not locate the all-weight characterization.

## Limitations
The theorem is universal over rowwise independent arrays, not over arbitrary dependent arrays, and it does not classify a single given array's convergence. The necessity witnesses may vary their distribution with the row; they are not required to be a single identically distributed sequence across rows.

A known general tail-condition theorem for maximal mean convergence already provides broad sufficient criteria, so part of the positive argument can also be obtained by checking those hypotheses. The separate contribution here is the exact universal necessary-and-sufficient boundary in the class of slowly varying moment weights.

Unindexed older work might contain an equivalent functional criterion under monotone-envelope or Orlicz-weight language; this remains the main bibliographic risk.

## References
1. Lê Vǎn Thành, “On a new concept of stochastic domination and the laws of large numbers,” arXiv:2207.06715v1, first publicly posted 14 July 2022; *TEST* 32 (2023), 74–106.
2. Lê Vǎn Thành, “Sharp sufficient conditions for mean convergence of the maximal partial sums of dependent random variables with general norming sequences,” *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 118 (2024), article 40; first published online 22 December 2023, DOI: 10.1007/s13398-023-01540-5.
3. L. Cao, “Mean convergence theorems for weighted sums of random variables under a condition of weighted integrability,” *Journal of Inequalities and Applications* 2013 (2013), article 558, DOI: 10.1186/1029-242X-2013-558.
4. N. H. Bingham, C. M. Goldie, and J. L. Teugels, *Regular Variation*, Cambridge University Press, 1989 (regular-variation inversion and Potter bounds).
