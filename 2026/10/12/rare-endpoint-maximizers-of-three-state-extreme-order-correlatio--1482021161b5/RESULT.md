# Rare-endpoint maximizers of three-state extreme-order correlation
## Finding
For each integer \(n\ge2\), consider independent and identically distributed observations \(X_1,\ldots,X_n\) with
\[
\Pr(X_i=-1)=\Pr(X_i=1)=t,
\qquad
\Pr(X_i=0)=1-2t,
\qquad 0<t\le\tfrac12.
\]
Let \(L_n=\min_iX_i\), \(U_n=\max_iX_i\), and let
\[
\rho_n(t)=\operatorname{Corr}(L_n,U_n),
\qquad
R_n=\max_{0<t\le1/2}\rho_n(t).
\]
The finite-sample maximum exists and is positive. For
\[
\ell=(1-t)^n,\qquad e=t^n,\qquad b=(1-2t)^n,
\]
the correlation is exactly
\[
\boxed{\rho_n(t)=\frac{(\ell+e)^2-b}{\ell+3e-(\ell+e)^2}.}
\tag{1}
\]
Define \(c_*\) as the unique solution in \((1,2)\) of
\[
(2-c_*)e^{c_*}=2.
\]
Then
\[
\boxed{\lim_{n\to\infty}nR_n
=\max_{c>0}\frac{c^2}{e^c-1}
=c_*(2-c_*)\simeq0.647610237891915.}
\tag{2}
\]
Furthermore, **every** selection of optimizing probabilities \(t_n\) satisfies
\[
\boxed{nt_n\longrightarrow c_*\simeq1.5936242600400266.}
\tag{3}
\]
Thus the endpoint masses that maximize the correlation become rare, of order \(1/n\), in the large-sample regime. In contrast, at equal three-point probabilities \(t=1/3\), the correlation decays exponentially in \(n\).

## Assumptions and scope
The observations are independent and identically distributed. The support is fixed to the equally spaced set \(\{-1,0,1\}\) and the endpoint masses are constrained to be equal; the middle mass may vanish at \(t=1/2\). Both extreme order statistics have positive finite variance for each allowed \(t\), so Pearson correlation is well defined.

The optimization is only over this symmetric one-parameter family. It is not the optimization over arbitrary three-point probability vectors, arbitrary support positions, or nonlinear functions of the extrema (maximal correlation).

## Proof
**Exact moments.** An affine translation of all observations does not change their extreme-order correlation, so temporarily replace the states \(\{-1,0,1\}\) by \(\{0,1,2\}\). Let \(M_n\) and \(V_n\) denote the translated minimum and maximum. Write
\[
I=\mathbf 1\{M_n\ge1\},\qquad J=\mathbf 1\{M_n=2\}.
\]
Then \(M_n=I+J\), and the two events are nested. Their probabilities are
\[
\mathbb EI=\ell,\qquad \mathbb EJ=e.
\]
Therefore
\[
\mathbb E M_n=\ell+e,
\qquad
\mathbb EM_n^2=\ell+3e,
\qquad
\operatorname{Var}(M_n)=\ell+3e-(\ell+e)^2.
\tag{4}
\]
The law is symmetric about the middle state, so \(V_n\) has the same variance. By expressing \(V_n\) through the complementary occupancy indicators, one finds
\[
\mathbb E(M_nV_n)=2\ell-b+2e.
\]
Because \(\mathbb EV_n=2-(\ell+e)\),
\[
\operatorname{Cov}(M_n,V_n)
=2\ell-b+2e-(\ell+e)[2-(\ell+e)]
=(\ell+e)^2-b.
\tag{5}
\]
Dividing (5) by (4) proves (1). Positivity follows from
\[
\ell^2\ge b,
\]
which is strict for \(t>0\), since \((1-t)^2>1-2t\).

**Local rare-endpoint limit.** Fix \(c>0\) and set \(t=c/n\) (for sufficiently large \(n\)). The standard uniform-on-compact exponential expansions give
\[
(1-c/n)^{2n}
=e^{-2c}\left(1-\frac{c^2}{n}+O(n^{-2})\right),
\]
\[
(1-2c/n)^n
=e^{-2c}\left(1-\frac{2c^2}{n}+O(n^{-2})\right),
\]
while \((c/n)^n\) is negligible to every fixed inverse power of \(n\). Thus, uniformly for \(c\) in each compact subinterval of \((0,\infty)\),
\[
(\ell+e)^2-b
=\frac{c^2e^{-2c}}n+O(n^{-2}),
\qquad
\ell+3e-(\ell+e)^2\longrightarrow e^{-c}(1-e^{-c}).
\]
Consequently
\[
\boxed{n\rho_n(c/n)\longrightarrow H(c):=\frac{c^2}{e^c-1}}
\tag{6}
\]
locally uniformly for positive \(c\).

**Uniform exclusion of escaping endpoints.** The nested events defining \(I\) and \(J\) imply
\[
\operatorname{Cov}(I,J)=e(1-\ell)\ge0,
\]
so (4) yields the important lower bound
\[
\operatorname{Var}(M_n)\ge \ell(1-\ell).
\tag{7}
\]
Also, for \(0<t\le1/2\),
\[
\frac{b}{\ell^2}
=\left(1-\frac{t^2}{(1-t)^2}\right)^n,
\]
and Bernoulli's inequality gives
\[
0\le\ell^2-b
\le n\left(\frac{t}{1-t}\right)^2\ell^2.
\]
Since \(e\le\ell\),
\[
0\le (\ell+e)^2-b
\le n\left(\frac{t}{1-t}\right)^2\ell^2+3\ell e.
\]
Set \(u=nt\). As \((1-t)^{-2}\le4\), \(\ell\le e^{-u}\), and \(e=t^n\), equations (1) and (7) yield the **global finite-sample estimate**
\[
0<n\rho_n(t)
\le\frac{4u^2}{e^u-1}
+\frac{3nt^n}{1-e^{-u}}.
\tag{8}
\]
This bound is uniform over \(n\ge2\) and \(0<t\le1/2\). If a sequence of such parameters has \(u=nt\to0\), then \(t^n\le t^2\) and both terms on the right of (8) tend to zero, because
\[
\frac{nt^2}{1-e^{-u}}
=\frac{u^2}{n(1-e^{-u})}\longrightarrow0.
\]
If instead \(u=nt\to\infty\), then the first term tends to zero and the second is at most
\[
\frac{3n2^{-n}}{1-e^{-u}}\longrightarrow0.
\]
Therefore
\[
nt\to0\ \text{or}\ nt\to\infty
\quad\Longrightarrow\quad n\rho_n(t)\to0.
\tag{9}
\]
For each fixed \(n\), (8) also shows \(\rho_n(t)\to0\) as \(t\downarrow0\); because the correlation is positive at every allowed \(t\), a maximizer exists in \((0,1/2]\).

**Sharp optimization and localization.** Differentiate the nonnegative function \(H\) in (6):
\[
H'(c)=\frac{c[(2-c)e^c-2]}{(e^c-1)^2}.
\]
The bracket has derivative \((1-c)e^c\), increases from zero on \((0,1)\), and strictly decreases after \(c=1\). It is positive at \(c=1\) and negative at \(c=2\), hence has exactly one zero \(c_*\in(1,2)\). Since \(H(c)\to0\) at both ends of \((0,\infty)\), it attains its unique positive global maximum at \(c_*\). Rearranging \((2-c_*)e^{c_*}=2\) yields
\[
H(c_*)=c_*(2-c_*).
\]

For all large \(n\), the admissible competitor \(t=c_*/n\) shows from (6) that
\[
\liminf_{n\to\infty}nR_n\ge H(c_*)>0.
\]
Let \(t_n\) attain \(R_n\), and put \(u_n=nt_n\). By (9), no subsequence of \(u_n\) can tend to zero or infinity. Hence every subsequence of \(u_n\) has a further subsequence tending to a positive finite \(c\); by locally uniform convergence (6), the corresponding values \(nR_n\) tend to \(H(c)\le H(c_*)\). The lower bound forces equality, and the uniqueness of \(c_*\) forces \(c=c_*\). Thus \(u_n\to c_*\) and \(nR_n\to H(c_*)\), proving (2)–(3).

Finally, for fixed \(t=1/3\), one has \(\ell=(2/3)^n\), \(e=b=(1/3)^n\). Formula (1) shows
\[
\rho_n(1/3)\sim (2/3)^n,
\]
which is exponentially smaller than the asymptotically optimal \(1/n\) correlation.

## Verification
The companion standalone script `verify.py` uses exact fractions to enumerate all length-\(n\) outcome vectors for selected \(n\le6\) and probabilities \(t\), checking the joint-moment formula (1) against the combinatorial definition, including the endpoint \(t=1/2\).

It checks two convenient exact values:
\[
\rho_2(1/3)=\frac8{19},\qquad
\rho_3(3/10)=\frac{81}{319}.
\]
It then computes the unique root \(c_*\) by deterministic bisection and checks numerical approach of \(nR_n\) to \(H(c_*)\) using finite grid searches. Those finite checks are reproducibility aids, not a proof of the asymptotic statement, which follows from (6)–(9) for every sequence of maximizing parameters.

## Relationship to prior work
Papadatos' 2022 preprint studies Pearson correlations of order statistics from discrete populations, gives the sharp two-draw discrete-uniform characterization, quotes the general Székely–Móri inequality
\[
\operatorname{Corr}(X_{1:n},X_{n:n})\le\frac1n,
\]
and explicitly raises optimization over nonuniform probability vectors. That universal upper bound does not determine the sharper constant within the symmetric three-atom family or identify how the optimal masses depend on sample size.

López-Blázquez and Salamanca-Miño (2021) study maximal correlations of pairs of order statistics from discrete parents by an automatic-differentiation approach. Their stated functional-maximal-correlation problem differs from optimizing **ordinary Pearson correlation** over symmetric parent masses. Full-text comparison of their article was not completed; this remains a bibliographic limitation rather than a claim that all possible equivalences are excluded.

The new result supplies the exact three-state ordinary-correlation formula, the asymptotically optimal rate \(c_*/n\) of rare endpoint masses, the sharp coefficient \(c_*(2-c_*)\), and the localization of **all** maximizing sequences. It makes no claim about unrestricted nonsymmetric probability vectors.

## Limitations
This theorem applies only to symmetric probabilities on a fixed equally spaced three-point support and to the extreme pair of an iid sample. It does not determine the finite-\(n\) maximizing parameter in closed form, nor does it optimize arbitrary nonsymmetric three-point laws or nonlinear transformations of the extremes. A general optimization theorem under older dependence or rare-event terminology may provide implicit coverage of the sharp asymptotics.

## References
1. N. Papadatos, “A discrete analogue of Terrell's characterization of rectangular distributions,” arXiv:2205.14360v1, 28 May 2022; *Mathematical Methods of Statistics* 32 (2023), 122–132. DOI: 10.3103/S1066530723020035.
2. G. J. Székely and T. F. Móri, “An extremal property of rectangular distributions,” *Statistics & Probability Letters* 3 (1985), 107–109. DOI: 10.1016/0167-7152(85)90035-5.
3. F. López-Blázquez and B. Salamanca-Miño, “Automatic differentiation and maximal correlation of order statistics from discrete parents,” *Computational Statistics* 36 (2021), 2889–2915. DOI: 10.1007/s00180-021-01103-5.
