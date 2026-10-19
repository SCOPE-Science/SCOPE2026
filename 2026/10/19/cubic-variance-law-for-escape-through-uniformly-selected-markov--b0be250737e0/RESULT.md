# Cubic variance law for escape through uniformly selected Markov holes

## Finding

Fix an integer \(b\ge2\). For each integer \(n\ge2\), consider the expanding map \(T_b:[0,1)\to[0,1)\), \(T_b(x)=bx\bmod1\), with Lebesgue initial probability. Select one of its \(b^n\) length-\(n\) symbolic cylinders uniformly, and make this *fixed* cylinder an absorbing hole. Denote its escape rate by \(\Gamma_n\), a random variable over the single initial choice of the hole, and put \(h=b^{-n}\).

Let \(\mu_{\mathrm{arith}}\) be the number-theoretic Möbius function, and define the number of primitive \(b\)-letter words of length \(p\) by
\[
 a_b(p)=\sum_{d\mid p}\mu_{\mathrm{arith}}(d)b^{p/d}.
\]
Then, as \(n\to\infty\) with \(b\) fixed,
\[
 \boxed{\operatorname{Var}(\Gamma_n)=C_bh^3\bigl(1+O_b(n\sqrt h)\bigr),\quad
 C_b=\sum_{p=1}^{\infty}\frac{a_b(p)}{b^{2p}}>0.}
\]
Moreover,
\[
 \mathbb E\left|\frac{\Gamma_n}{h}-1\right|=O_b(nh).
\]
In particular, the fluctuation scale is \(h^{3/2}\), although \(\Gamma_n/h\to1\) in \(L^1\). For the doubling map, \(C_2=0.823295689936509\ldots\); for the tripling map, \(C_3=0.457360440887798\ldots\). The variance is dominated by rare holes containing periodic points of fixed short primitive period, not by typical hole locations.

## Assumptions and scope

The initial measure for each opened system is Lebesgue probability and the escape rate is
\[
 \gamma_{n,w}=-\lim_{k\to\infty}k^{-1}\log\Pr\{X_0,\ldots,X_{k-1}\notin H_w\},
 \qquad X_j=T_b^j(X_0),
\]
where \(H_w\) is the half-open \(b\)-adic cylinder specified by a length-\(n\) word \(w\). The limit equals minus the logarithm of the Perron eigenvalue of the finite forbidden-word transition matrix divided by \(b\). Each hole is selected once and retained at all times; the result is *not* about a newly randomized hole at each iterate.

The asymptotic constants implicit in \(O_b(\cdot)\) can depend on the fixed integer \(b\). Endpoints of cylinders have Lebesgue measure zero. The theorem does not require independence between different holes' escape rates: the variance is defined by uniform sampling of exactly one hole.

## Proof

**1. Exact characteristic equation.** A shift \(p\in\{1,\ldots,n-1\}\) is a period of the finite word \(w=w_1\cdots w_n\) when \(w_i=w_{i+p}\) for all \(1\le i\le n-p\). Set \(\chi_0(w)=1\) and let \(\chi_p(w)\in\{0,1\}\) indicate this property for \(p\ge1\). The word autocorrelation polynomial is
\[
 A_w(z)=\sum_{p=0}^{n-1}\chi_p(w)z^{n-1-p}.
\]
The standard forbidden-word correlation generating function has its dominant pole \(\vartheta_w\) at the largest positive solution of \((z-b)A_w(z)+1=0\). This follows from the single-word Guibas--Odlyzko correlation formula, equivalently from the exact periodic-point formula in Georgiou--Dettmann--Altmann (2012, equations (8)--(12)); it can also be checked using the \(b^{n-1}\)-state de Bruijn transition matrix. The open transfer eigenvalue is \(\lambda_w=\vartheta_w/b\). Writing \(h=b^{-n}\) gives the exact identity
\[
 (1-\lambda_w)\sum_{p=0}^{n-1}\chi_p(w)b^{-p}\lambda_w^{n-p-1}=h. \tag{1}
\]
We use the positive dominant root of the forbidden-word matrix, not an arbitrary algebraic root of (1).

**2. Uniform near-unity root control.** Write
\[
 B_w=\sum_{p=0}^{n-1}\chi_p(w)b^{-p}=1+S_w,
 \qquad S_w=\sum_{p=1}^{n-1}\chi_p(w)b^{-p}.
\]
For \(a=1-\lambda\in[0,2h]\), define
\[
 D_w(a)=\sum_{p=0}^{n-1}\chi_p(w)b^{-p}(1-a)^{n-p-1}.
\]
Since \(1\le B_w\le b/(b-1)\le2\), Bernoulli's inequality gives \(0\le B_w-D_w(a)\le(n-1)aB_w\). For sufficiently large \(n\), the function \(aD_w(a)\) is strictly increasing on \([0,2h]\); it is at most \(h\) at \(a=h/2\) and exceeds \(h\) at \(a=2h\). Thus (1) has exactly one root in that interval. It is the root corresponding to the transfer Perron eigenvalue: its existence makes the spectral radius at least \(1-2h\), and any larger positive eigenvalue would provide another root in the same uniqueness interval. Uniformly over all words,
\[
 1-\lambda_w=\frac{h}{B_w}+O_b(nh^2),
 \qquad \frac{\gamma_{n,w}}h=\frac1{B_w}+O_b(nh). \tag{2}
\]
The logarithm correction uses \(-\log(1-a)=a+O(a^2)\), uniformly for \(a\le2h\).

**3. Exact distribution of short word periods.** Let \(W_n\) be a uniformly random length-\(n\) word. A specified shift \(p\) is a period of \(W_n\) with probability \(b^{-(n-p)}=hb^p\), because its first \(p\) letters determine the whole word. Consequently,
\[
 \mathbb E S_{W_n}=\sum_{p=1}^{n-1}b^{-p}hb^p=(n-1)h. \tag{3}
\]
Let \(q(W_n)\) denote the least positive period, taking \(q=n\) if no proper period exists. For \(q\le\lfloor n/2\rfloor\), exactly \(a_b(q)\) words have least period \(q\): each is a repetition, possibly truncated, of a primitive length-\(q\) word. A shorter period of the full word would, by the Fine--Wilf periodicity theorem applied to periods \(q\) and the shorter period, force a smaller period in the length-\(q\) block. The primitive-word enumeration is the classical Möbius inversion formula stated above.

Fix \(q\). If a word with least period \(q\) has an additional period \(p\) not divisible by \(q\), Fine--Wilf shows \(p>n-q\). All multiples of \(q\) below \(n\) are periods. Therefore, uniformly among such words as \(n\to\infty\),
\[
 B_w=(1-b^{-q})^{-1}+O_b(b^{-(n-q)}),
 \qquad \frac1{B_w}-1=-b^{-q}+O_b(b^{-(n-q)}). \tag{4}
\]
Write \(Z_w=1/B_w-1=-S_w/(1+S_w)\). Whenever \(q(w)=q\),
\[
 |Z_w|\le S_w\le \frac{b^{1-q}}{b-1}. \tag{5}
\]
The contributions of words with least period \(q\le n/2\) to \(h^{-1}\mathbb E Z_{W_n}^2\) thus converge term by term to \(a_b(q)b^{-2q}\). This interchange is valid because the terms are bounded by \((b/(b-1))^2b^{-q}\), a summable majorant.

For the residual words with \(q(W_n)>n/2\), use \(S_w\le\sum_{p>n/2}b^{-p}=O_b(\sqrt h)\), and (3) to obtain
\[
 \mathbb E[Z_{W_n}^2\mathbf1_{\{q(W_n)>n/2\}}]
 \le O_b(\sqrt h)\,\mathbb E S_{W_n}=O_b(nh^{3/2})=o(h). \tag{6}
\]
Combining (4)--(6) proves
\[
 \frac{\mathbb E Z_{W_n}^2}{h}
 =C_b+O_b(n\sqrt h). \tag{7}
\]
For the stated error rate, the short-period estimate (4) makes the total error from \(q\le n/2\) at most \(O_b(\sqrt h)\), since \(a_b(q)\le b^q\); the omitted tail of the convergent series is also \(O_b(\sqrt h)\), and (6) bounds the remaining contribution.

**4. From autocorrelations to the variance.** Let \(\Delta_n=\Gamma_n/h-1\). By (2), \(\Delta_n=Z_{W_n}+O_b(nh)\) uniformly. Equations (3) and (5) imply \(\mathbb E|Z_{W_n}|\le(n-1)h\), hence
\[
 \mathbb E|\Delta_n|=O_b(nh),\qquad
 \frac{\mathbb E\Delta_n^2}{h}=C_b+O_b(n\sqrt h),
 \qquad \frac{(\mathbb E\Delta_n)^2}{h}=O_b(n^2h).
\]
For fixed \(b\), \(n^2h=O_b(n\sqrt h)\) for all sufficiently large \(n\). Since \(\operatorname{Var}(\Gamma_n)=h^2\operatorname{Var}(\Delta_n)\), (7) yields the claimed cubic-variance law. Positivity follows from \(a_b(1)=b\). The constant series converges absolutely as \(a_b(p)\le b^p\).

## Verification

The standalone `verify.py` constructs, independently, finite de Bruijn forbidden-word matrices and compares their Perron eigenvalues against the roots of (1) for every word at \((b,n)=(2,5),(2,6),(3,4)\). It checks the primitive-word Möbius formula by exhaustive enumeration and computes all \(b^n\) escape rates for several moderate values of \(n\). It reports `VERIFY_OK` when all tests pass. For example, its standardized variances are \(0.819618025621\) at \((b,n)=(2,14)\), and \(0.453430256543\) at \((b,n)=(3,8)\), compared with the respective limiting constants above. These finite computations corroborate, but do not establish, the infinite-\(n\) theorem, for which the preceding proof supplies the necessary uniform estimates and summability argument.

## Relationship to prior work

Georgiou, Dettmann and Altmann (2012) derived the exact periodic-orbit characteristic equation, distinguished short-period and long-period holes, and studied the mean escape rate as the hole varies. All of these are prior results; particularly, the autocorrelation equation and primitive-word counts used here are *not* claimed as new. Attarchi and Bunimovich (2020) explained inequalities involving average escape rates by convexity. Cheriyath and Agarwal (2019/2022) developed correlation-polynomial comparisons and escape rates for unions of cylinders in subshifts of finite type. Their stated results do not compute the variance across the full population of equal-size holes.

The claim here is the *second-moment law* and its nonzero explicit primitive-orbit constant, including the uniform control proving that atypical short-period holes determine an \(h^3\) rather than an \(h^4\) variance scale. The earlier mean formulas and pointwise periodic-orbit asymptotics suggest the mechanism but do not, by themselves, validate the passage from individual-hole asymptotics to an average of squared deviations: the long-period population and uniform remainder must be controlled. Published or unindexed equivalent derivations cannot be ruled out absolutely.

## Limitations

The result is for fixed integer \(b\ge2\), a single uniformly chosen length-\(n\) Markov cylinder, and the Lebesgue-preserving full-branch map. It does not cover non-Markov holes, biased choice of hole, random holes resampled over time, or a simultaneous limit in \(b\) and \(n\). It describes ensemble variance, not temporal variance along one survivor orbit. The numerical verifier does not certify historical originality or replace the infinite proof. The open question of whether a broader general random-hole theorem subsumes this specific constant remains a residual literature-priority risk.

## References

1. O. Georgiou, C. P. Dettmann and E. G. Altmann, *Faster than expected escape for a class of fully chaotic maps*, first public preprint July 30, 2012, arXiv:1207.7000v1; HTML text of v2: https://arxiv.org/html/1207.7000v2. See especially Sections III.1--III.3 and IV.1.
2. H. Attarchi and L. A. Bunimovich, *Why Escape Is Faster Than Expected*, first public preprint August 12, 2020, arXiv:2008.05405, https://arxiv.org/abs/2008.05405. See Sections 2--3.
3. H. Cheriyath and N. Agarwal, *Subshifts of Finite Type with a Hole*, first public preprint May 28, 2019, arXiv:1905.11767, https://arxiv.org/html/1905.11767v5. See Sections 2--3 and 6--7.
4. N. J. Fine and H. S. Wilf, *Uniqueness theorems for periodic functions*, Proceedings of the American Mathematical Society 16 (1965), 109--114; the classical Fine--Wilf periodicity theorem.
