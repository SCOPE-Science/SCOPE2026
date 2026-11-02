# Sharp three-channel finite Gabor conditioning for a two-tap window

## Finding

Let \(N\ge4\) be an integer, let \(s\in\mathbb Z_N\) satisfy \(\gcd(s,N)=1\), and set
\[
g=\frac{\delta_0+\delta_s}{\sqrt2}\in\mathbb C^N.
\]
For every three-element set \(L\subset\mathbb Z_N\), consider the \(3N\) unit-vector Gabor system
\[
\mathcal G(L)=\{M_\ell T_k g:k\in\mathbb Z_N,\ \ell\in L\},
\quad (T_kg)[j]=g[j-k],\quad (M_\ell g)[j]=e^{2\pi i\ell j/N}g[j].
\]
Write \(S_L\) for its positive frame operator and \(\kappa(L)=\lambda_{\max}(S_L)/\lambda_{\min}(S_L)\) for its squared spectral condition number. All such systems are frames. The **globally smallest** \(\kappa(L)\), over every set of exactly three distinct modulation frequencies, and **all** minimizers have the following form.

Put \(q=\lfloor N/3\rfloor\), \(\delta=\pi/N\), and
\[
\rho_N=\begin{cases}
0,&N\equiv0\pmod3,\\
1+2\cos(2\pi q/N),&N\equiv1\pmod3,\\
-1-2\cos(2\pi(q+1)/N),&N\equiv2\pmod3.
\end{cases}
\]
For \(N\not\equiv0\pmod3\), this number is strictly positive. The sharp condition number is
\[
\boxed{\kappa_N^{\rm opt}=\begin{cases}
1,&3\mid N,\\
(3+\rho_N)/(3-\rho_N),&3\nmid N,\ 2\mid N,\\
(3+\rho_N)/(3-\rho_N\cos\delta),&N\equiv1\pmod3,\ 2\nmid N,\\
(3+\rho_N\cos\delta)/(3-\rho_N),&N\equiv2\pmod3,\ 2\nmid N.
\end{cases}}
\]
The minimizing sets are precisely the inverse images under multiplication by \(s\) of the translates of
\[
\begin{cases}
\{0,q,2q\},&N\equiv0,1\pmod3,\\
\{0,q+1,2(q+1)\},&N\equiv2\pmod3.
\end{cases}
\]
There are exactly \(N/3\) minimizing unordered sets when \(3\mid N\), and exactly \(N\) otherwise. The same sets uniquely minimize the frame-potential defect
\[
\operatorname{tr}(S_L^2)-9N,
\]
whose exact sharp value is \(N\rho_N^2/2\). In particular, perfect tightness with only three modulation channels occurs **if and only if** \(3\mid N\). Along either nonzero residue class modulo three,
\[
\lim_{\substack{N\to\infty\\3\nmid N}}N(\kappa_N^{\rm opt}-1)
=\frac{4\pi}{3\sqrt3},\qquad
\lim_{\substack{N\to\infty\\3\nmid N}}N\min_{|L|=3}\big(\operatorname{tr}(S_L^2)-9N\big)
=\frac{2\pi^2}{3}.
\]

## Assumptions and scope

The ambient space is \(\mathbb C^N\) with counting-measure Euclidean norm. The window has exactly two equally weighted nonzero coordinates at a generating displacement \(s\); all \(N\) translations and exactly three **distinct**, equally weighted frequency modulations are used. The eigenvalue ratio is for the frame operator, not for the synthesis matrix itself. Frequencies are genuine subsets, not multisets or weighted quadrature rules. Only the finite cyclic group, not an arbitrary finite abelian group, is asserted.

## Proof

**1. The complete spectral reduction.** Let \(\zeta=e^{2\pi i/N}\) and use the unitary discrete Fourier transform. The Fourier-domain frame operator is diagonal because the translations range over \(\mathbb Z_N\). As
\[
N|\widehat g(j)|^2=1+\cos(2\pi sj/N),
\]
its exact eigenvalues are
\[
\lambda_j=3+\operatorname{Re}\big(\zeta^{sj}Z_L\big),
\qquad Z_L=\sum_{\ell\in L}\zeta^{-s\ell},\qquad 0\le j<N.
\tag{1}
\]
Since the three roots in \(Z_L\) are distinct, \(|Z_L|<3\) and every eigenvalue is positive. Orthogonality of first and second nontrivial characters gives
\[
\operatorname{tr}(S_L)=3N,\qquad
\operatorname{tr}(S_L^2)-9N=\frac N2|Z_L|^2.
\tag{2}
\]
Multiplication by \(s\) permutes the group, so it suffices to optimize over arbitrary three distinct \(N\)-th roots of unity.

**2. Root-triangle minimization and the second-best separation.** Write the three successive positive cyclic gaps as integers \(a,b,c\), so \(a+b+c=N\). An elementary cosine identity yields
\[
\left|1+\zeta^a+\zeta^{a+b}\right|^2
=1-8\cos(\pi a/N)\cos(\pi b/N)\cos(\pi c/N).
\tag{3}
\]
If some gap is at least \(N/2\), the right side is at least one. Otherwise each factor is positive and \(h(t)=\log\cos(\pi t/N)\) is strictly concave for \(0<t<N/2\). Replacing two positive integer gaps that differ by at least two with their nearer pair strictly increases the cosine product. Repeating this *smoothing* proves the unique optimal unordered gap multiset: \((q,q,q)\), \((q,q,q+1)\), or \((q,q+1,q+1)\), according to \(N\bmod3\). Their root-sum moduli are precisely \(\rho_N\). The exceptional small order \(N=4\) has only balanced triples, and direct inspection gives \(\rho_4=1\); \(N=5\) has the two gap types \((1,2,2)\) and \((1,1,3)\), with moduli \((\sqrt5-1)/2\) and \((\sqrt5+1)/2\). For \(N=8\), the best nonbalanced gap type is \((2,2,4)\), whose modulus is one.

For quantitative strictness, when \(3\nmid N\), denote by \(\rho_N^{(2)}\) the smallest modulus from an **unbalanced** gap triple. For \(N\ge7\) other than \(N=8\), a second smoothing argument makes the runner-up explicit. Sort the three gaps increasingly. Among sorted integer triples distinct from the balanced pattern, the unique triple majorized by every other unbalanced triple is \((q-1,q+1,q+1)\) if \(N=3q+1\), or \((q,q,q+2)\) if \(N=3q+2\): in the first case any unbalanced triple must have minimum at most \(q-1\) and maximum at least \(q+1\), and in the second it must have maximum at least \(q+2\) or minimum at most \(q-1\). Strict concavity of \(h\) therefore makes that runner-up the strict largest cosine product among unbalanced triples with all gaps below \(N/2\). Any gap at least \(N/2\) instead has modulus at least one. The displayed runner-up moduli are at most one: in the first residue class the angle \(2\pi(q+1)/N\) lies in \([2\pi/3,\pi]\); in the second, for \(N\ge11\), the angle \(2\pi q/N\) lies in \([\pi/2,2\pi/3)\). The identity (3) therefore proves
\[
\rho_N^{(2)}=
\begin{cases}
\left|1+2\cos(2\pi(q+1)/N)\right|,&N\equiv1\pmod3,\\
\left|1+2\cos(2\pi q/N)\right|,&N\equiv2\pmod3.
\end{cases}
\tag{4}
\]
This is also directly valid for \(N=5,8\) by the inspection above.

We need the uniform separation
\[
\rho_N^{(2)}>\frac43\rho_N\qquad (N\ge5,\ 3\nmid N).
\tag{5}
\]
For \(N=5,8\), the directly evaluated values establish (5). Otherwise write \(d=\pi/N\). Half-angle identities reduce the ratio in (5) to
\[
\frac{\rho_N^{(2)}}{\rho_N}
=\begin{cases}
\displaystyle\frac{2\cos(d/3)\cos(\pi/6+2d/3)}{\cos(\pi/6-d/3)},&N\equiv1\pmod3,\\[2mm]
\displaystyle\frac{2\cos(d/3)\cos(\pi/6-2d/3)}{\cos(\pi/6+d/3)},&N\equiv2\pmod3.
\end{cases}
\tag{6}
\]
In the first case \(N\ge7\), so \(d\le\pi/7\), and the elementary bounds
\[
\cos(\pi/21)>39/40,\quad
\cos(11\pi/42)>2/3,\quad
\cos(5\pi/42)<15/16
\]
give a ratio greater than \(2(39/40)(2/3)/(15/16)>4/3\). These three inequalities follow from alternating Taylor bounds for \(\cos\) and \(3<\pi<22/7\). In the second case, the ratio is at least \(2\cos(d/3)\), which exceeds \(4/3\) since \(d\le\pi/5\). This establishes (5).

**3. The condition-number minimax.** For an arbitrary triple let \(R=|Z_L|\) and \(c_N=\cos(\pi/N)>3/4\). Sampling the cosine at all \(N\)-th roots guarantees that at least one eigenvalue in (1) is at least \(3+Rc_N\) and another is at most \(3-Rc_N\). Consequently
\[
\kappa(L)\ge\frac{3+Rc_N}{3-Rc_N}.
\tag{7}
\]
Every balanced triple has \(R=\rho_N\), so its condition number is at most \((3+\rho_N)/(3-\rho_N)\). For any unbalanced triple, (5) gives \(Rc_N>\rho_N\), and (7) makes its condition number **strictly larger** than this upper bound for balanced triples. This proves uniqueness of the minimizing geometry for \(3\nmid N\) with \(N\ge5\). For \(3\mid N\), the balanced sets have \(Z_L=0\) and hence \(\kappa=1\), while no other triple has zero root sum. At \(N=4\), every triple is balanced. Thus all orders are covered.

**4. Exact minimizing eigenvalue extremes.** For the balanced frequency sets, after permuting indices and removing a common phase, (1) becomes
\[
\lambda_j=\begin{cases}
3,&3\mid N,\\
3+\rho_N\cos(2\pi j/N),&N\equiv1\pmod3,\\
3-\rho_N\cos(2\pi j/N),&N\equiv2\pmod3.
\end{cases}
\]
When \(N\) is even, both \(1\) and \(-1\) occur among the sampled cosine values. When \(N\) is odd, the minimum cosine is \(-\cos(\pi/N)\). Reading off the extremes proves all displayed optimal ratios. Cyclic translation generates exactly \(N\) distinct balanced triples when \(3\nmid N\), since the exceptional long or short gap is uniquely positioned; when \(3\mid N\) the optimum is a coset of the order-three subgroup, producing \(N/3\) distinct sets. Formula (2) gives the exact potential defect and its equality cases. Finally, (6) and the half-angle formulas imply \(N\rho_N\to2\pi/\sqrt3\) along nonzero residue classes; expansion of the exact ratios and (2) gives both stated limits.

## Verification

Run `python3 CHECK.py` with Python 3 and NumPy. The executable enumerates every three-element frequency set for each \(4\le N\le40\), tests the independent discrete spectral formula, checks both global optimizer sets and both sharp values, and directly constructs Gabor frame matrices for all \(4\le N\le11\) with all coprime two-tap spacings. It returned `CHECK_OK 102701 N=4..40 exhaustive optimizers; direct spectral checks N=4..11`. These finite tests do not prove the universal quantifier; the root-triangle and separation arguments above do. No external numerical constants or external files are needed beyond NumPy.

## Relationship to prior work

Asipchuk, De Carli, and Rodriguez give general block-equivalence and a Fourier-diagonalization criterion for finite Gabor systems, including full translation sets [1]. That structural reduction is used here and is **not** claimed as new. Their results do not select the best set of three distinct modulation channels, calculate its sharp spectral ratio, or classify these minimizers. Classical finite Gabor-frame theory also supplies the frame-operator viewpoint [2].

The nearby published finding *Sharp Riesz conditioning for consecutive triples on finite cycles* [3] obtains the same balanced frequency geometry for a different \(3\times3\) exponential Vandermonde Gram matrix on three **spatial** sample sites. Its eigenvalues and optimand differ from the present \(N\times N\) full-translation two-tap Gabor operator, and its sharp Riesz ratio does not imply (7) or the present parity-dependent optimum. The elementary three-root minimization itself belongs to classical small-sum-of-roots theory [4]; novelty is claimed only for the complete optimal **Gabor conditioning** and its interaction with discrete cosine extrema, not for the balanced-triangle fact in isolation. An earlier unindexed equivalent finite-Gabor design formula is a residual originality risk.

## Limitations

The optimization holds only for two equally weighted taps with coprime spacing, all translations, and exactly three distinct equally weighted modulation frequencies. No claim is made for arbitrary tap amplitudes, noncoprime spacings, partial translations, noisy reconstruction, or more than three channels. The self-review does not constitute an independent audit.

## References

1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, first publicly submitted 2026-05-15, revised 2026-10-24, Theorem 1.1, Corollary 1.2, Lemma 3.1.
2. H. Bölcskei and A. J. E. M. Janssen, *Gabor frames, unimodularity, and window decay*, Journal of Fourier Analysis and Applications 6 (2000), 255–276, DOI 10.1007/BF02511155.
3. *Sharp Riesz conditioning for consecutive triples on finite cycles*, published-finding corpus published finding, 2026-10-11, identifier `1200745c9cae`, `https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-riesz-conditioning-for-consecutive-triples-on-finite-cycle--1200745c9cae`.
4. G. Myerson, *How Small Can a Sum of Roots of Unity Be?*, American Mathematical Monthly 93 (1986), 457–459; see also D. Stack Exchange question *Minimising a sum of roots of unity* (2014), linking the three-root case to classical literature.
