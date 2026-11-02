# A mod-Poisson root-degree law under maximum-independent-set rigidity in recursive trees

## Finding

Let \(T_n\) be the uniform random recursive tree obtained by attaching label \(j\), for each \(2\le j\le n\), independently to a uniform member of \(\{1,\ldots,j-1\}\). Let \(D_n\) be the number of children of the root (label \(1\)). Let \(A_n\) denote **root rigidity**: the root lies in every maximum independent set of \(T_n\). Write \(L(z)=\log(1/(1-z))\). The following exact joint probability generating function holds for all integers \(n\ge1\) and all complex \(u\):

\[
P_n(u):=\mathbb E\bigl[u^{D_n}\mathbf 1_{A_n}\bigr]
=[z^{n-1}]\exp\left(u\left[L(z)-\log(1+L(z))\right]\right).
\tag{1}
\]

For \(n\ge3\), the event \(A_n\) has positive probability. As \(n\to\infty\), uniformly for \(u\) in a fixed sufficiently small complex neighborhood of \(1\),

\[
\mathbb E[u^{D_n}\mid A_n]
=\frac{\exp((u-1)\lambda_n)}{\Gamma(u)}
\left(1+O\left(\frac1{\log n}\right)\right),
\qquad \lambda_n=\log n-\log\log n.
\tag{2}
\]

Consequently,

\[
\Pr(A_n)=\frac1{\log n}\left(1+O\left(\frac1{\log n}\right)\right),
\tag{3}
\]

\[
\begin{aligned}
\mathbb E[D_n\mid A_n]
&=\lambda_n+\gamma+O((\log n)^{-1}),\\
\operatorname{Var}(D_n\mid A_n)
&=\lambda_n+\gamma-\frac{\pi^2}{6}+O((\log n)^{-1}),
\end{aligned}
\tag{4}
\]

and \((D_n-\lambda_n)/\sqrt{\lambda_n}\Rightarrow N(0,1)\). Since the unconditional degree has \(\mathbb ED_n=H_{n-1}\) and \(\operatorname{Var}D_n=H_{n-1}-H_{n-1}^{(2)}\), conditioning on root rigidity removes \(\log\log n+o(1)\) from **both** the mean and variance. The correction diverges, even though it is smaller than the ordinary \(\sqrt{\log n}\) fluctuation scale.

## Assumptions and scope

Trees are rooted at label \(1\), labels increase strictly along parent-child paths, and the \((n-1)!\) possible parent assignments are equiprobable. A maximum independent set is an independent vertex subset with largest possible cardinality, not merely a maximal set. The empty product convention covers \(n=1\); \(\Pr(A_2)=0\), so conditional probabilities at \(n=2\) are not defined. All asymptotics concern integers \(n\to\infty\), with \(u\) restricted as in (2). The constant \(\gamma\) is Euler's constant; \(H_m^{(2)}=\sum_{j=1}^m j^{-2}\).

## Proof

**Step 1: Root-rigidity recursion.** On a finite rooted tree \(T\), let \(I(T)\) be the independence number, and \(I_0(T)\) the maximum size of an independent set excluding the root. Then \(\iota(T):=I(T)-I_0(T)\in\{0,1\}\). If the root branches are \(T_1,\ldots,T_d\), then \(I_0(T)=\sum_i I(T_i)\), while the best size with the root included is \(1+\sum_i I_0(T_i)\). Therefore the root lies in every maximum independent set precisely when \(\iota(T)=1\), equivalently when \(\iota(T_i)=0\) for **each** root branch. This is the established essential-vertex recursion, applied here to a root-degree mark.

**Step 2: Exact marked enumeration.** The exponential generating function of all recursive trees is \(T(z)=\sum_{n\ge1}(n-1)!z^n/n!=L(z)\), and it satisfies \(T'(z)=e^{T(z)}\). Let \(E(z)\) be the exponential generating function of root-rigid recursive trees and \(N(z)=T(z)-E(z)\) that of root-nonrigid trees. The root is rigid exactly when all its root branches are nonrigid, hence \(E'(z)=e^{N(z)}=e^{T(z)-E(z)}\). As \(E(0)=0\), differentiation gives \((e^{E(z)})'=e^{T(z)}=(1-z)^{-1}\), and integration gives

\[
e^{E(z)}=1+L(z),\qquad N(z)=L(z)-\log(1+L(z)).\tag{5}
\]

Mark every direct child of the root by \(u\) and no other edge. The exponential set of nonrigid branches yields the marked derivative \(E_u'(z)=e^{uN(z)}\). A recursive tree of order \(n\) has probability \(1/(n-1)!\), so multiplying \([z^n]E_u(z)\) by \(n!/(n-1)!=n\) proves equation (1), including its normalization.

**Step 3: Complex-uniform coefficient transfer.** From (1) and (5),

\[
P_n(u)=[z^{n-1}](1-z)^{-u}(1+L(z))^{-u}.
\tag{6}
\]

Choose the principal branches near the origin and continue into a slit \(\Delta\)-domain at \(z=1\). There are no other singularities of modulus at most one: for \(|z|<1\), \(\operatorname{Re}(1+L(z))>1-\log2>0\). For \(u\) in a fixed small complex disk around \(1\), the standard logarithmic singularity-transfer argument is uniform: in the Hankel scaling \(z=1-w/n\), \(L(z)=\log n-\log w\), and the leading inverse-gamma contour integral is \((2\pi i)^{-1}\int_{\mathcal H}e^w w^{-u}\,dw=1/\Gamma(u)\). Expanding \((1+\log n-\log w)^{-u}\) uniformly on the truncated contour and controlling its tails by the logarithmic transfer bounds gives

\[
P_n(u)=\frac{n^{u-1}}{\Gamma(u)(\log n)^u}
\left(1+O\left(\frac1{\log n}\right)\right),
\tag{7}
\]

uniformly in that disk. This is the standard Flajolet–Odlyzko transfer for algebraic-logarithmic singularities; the bounded parameter disk also permits differentiation of the remainder by Cauchy's integral formula. At \(u=1\), (7) gives (3). Dividing (7) by its value at \(u=1\) yields (2).

**Step 4: Moments and Gaussian fluctuations.** With \(u=e^t\), the conditional logarithmic moment generating function is, uniformly for small complex \(t\),

\[
\log\mathbb E[e^{tD_n}\mid A_n]
=\lambda_n(e^t-1)-\log\Gamma(e^t)+O((\log n)^{-1}).
\tag{8}
\]

Differentiating at zero, using \(\psi(1)=-\gamma\) and \(\psi'(1)=\pi^2/6\), gives (4). Replacing \(t\) by \(t/\sqrt{\lambda_n}\) in (8) and subtracting \(t\sqrt{\lambda_n}\) proves the normal limit by the moment generating function theorem. The unconditional root degree is \(\sum_{j=2}^n\mathbf1_{\{j\text{ attaches to root}\}}\), an independent sum with success probabilities \(1/(j-1)\), establishing the stated unconditioned moments and the \(\log\log n\) deficits.

## Verification

The supplied standalone file `CHECK.py` independently enumerates all \((n-1)!\) parent assignments for \(1\le n\le8\), tests root rigidity by globally enumerating maximum independent sets (not only by the subtree recursion), and compares every exact root-degree coefficient to (1). It also checks the previously established unmarked recurrence and factorial moments with exact rational arithmetic. The replay passes 11,887 exact assertions. A separate numerical recurrence at \(n=1000\) gives conditional mean approximately \(5.5322979\) versus the leading prediction \(5.5523262\), and variance \(4.0185097\) versus the leading prediction \(3.9073921\). These are finite diagnostics, not a substitute for Step 3.

Run with a standard Python 3 interpreter: `python CHECK.py`. No network or external Python packages are needed.

## Relationship to prior work

Fuchs, Holmgren, Mitsche and Neininger (first public version 2019) gave the *unmarked* root-selection recurrence and its generating function, as well as a central limit theorem for the **total** independence number. Janson (2020) proved the general root-essential recursion and a law of large numbers for the **total** independence number; in Yule time he computed the root-essential probability at a fixed time. Dadedzi and Wagner (2022) studied eigenvalue multiplicities and the associated *total* independence-number fluctuations by generating functions. The present claim is neither the known scalar rigidity probability nor another total-size fluctuation theorem: it is the exact root-degree/root-rigidity **joint** law and a complex-uniform conditional mod-Poisson asymptotic, producing a diverging second-order degree deficit. General singularity transfer is a proof tool, not a claim of novelty.

## Limitations

The proof addresses uniform recursive trees, a fixed oldest root and the event of membership in every maximum independent set. It does not classify degrees of other labels, simultaneous essentiality of multiple vertices, or alternative attachment rules. The numerical test is finite. The transfer formula is local in \(u\), and does not assert local large deviations for arbitrary root-degree scales. Historical priority is based on specified accessible sources and is not independently certified.

## References

- M. Fuchs, C. Holmgren, D. Mitsche and R. Neininger, *A note on the independence number, domination number and related parameters of random binary search trees and random recursive trees*, arXiv:1909.12767, first posted 27 September 2019, https://arxiv.org/html/1909.12767v2 .
- S. Janson, *On the independence number of some random trees*, arXiv:2003.08712, first posted 19 March 2020, https://arxiv.org/html/2003.08712v2 .
- K. Dadedzi and S. Wagner, *On the distribution of eigenvalues of increasing trees*, arXiv:2208.05575, first posted 10 August 2022, https://arxiv.org/abs/2208.05575 .
- P. Flajolet and A. Odlyzko, *Singularity analysis of generating functions*, SIAM J. Discrete Math. 3 (1990), 216–240, https://doi.org/10.1137/0403019 .
