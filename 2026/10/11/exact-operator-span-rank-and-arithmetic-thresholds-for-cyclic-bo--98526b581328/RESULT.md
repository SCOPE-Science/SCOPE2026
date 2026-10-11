# Exact operator-span rank and arithmetic thresholds for cyclic boxcar Gabor measurements

## Finding
Fix an integer \(N\geq3\), a window length \(1\leq k<N\), and the unit vector
\[
 g_{N,k}(x)=k^{-1/2}\mathbf1_{\{0,1,\ldots,k-1\}}(x),\qquad x\in\mathbb Z_N.
\]
Let \(P_{u,v}\) range over the \(N^2\) rank-one projectors onto the full cyclic time-frequency orbit of \(g_{N,k}\), and define
\[
 R_N(k)=\dim_{\mathbb C}\operatorname{span}\{P_{u,v}:u,v\in\mathbb Z_N\}.
\]
The following rules determine \(R_N(k)\) exactly for *every* admissible \(N,k\). Put
\[
 d=\gcd(N,k),\qquad
 \beta_m(a)=\begin{cases}\gcd(m,a),&m/\gcd(m,a)\text{ is even},\\0,&\text{otherwise},\end{cases}
\]
for positive integers \(m\). For \(a=0,1,\ldots,N-1\), put
\[
 r_a=\max\{k-a,0\},\qquad s_a=\max\{k+a-N,0\},
\]
and let
\[
 c_a=\begin{cases}
 0,&r_a+s_a=0,\\
 N-\gcd(N,r_a+s_a)+1,&r_as_a=0\text{ and }r_a+s_a>0,\\
 N-d+1-\beta_N(a)+\beta_d(a),&r_as_a>0.
\end{cases}
\]
**Exact classification:** \(\boxed{R_N(k)=\sum_{a=0}^{N-1}c_a}\).

In particular, if \(p\) is the least prime divisor of odd \(N\), the projectors are informationally complete *if and only if*
\[
 \boxed{k\ge N-\frac{p-1}{2}}.
\]
For even \(N\), no constant rectangular window of length strictly between \(0\) and \(N\) yields informational completeness.

The power-of-two case has an additional **sharp capacity law**. For \(N=2^q\), \(q\ge2\), the exact maximum over all rectangular lengths is
\[
 \boxed{\max_{1\le k<N}R_N(k)=N^2-\frac{qN}{2}},
\]
and its optimizers are *exactly* the odd lengths \(N/2<k<N\). More precisely, for \(N/2<k<N\), setting \(d=\gcd(N,k)=2^h\) gives
\[
 \boxed{N^2-R_N(k)=\frac{qN}{2}+\frac{2k-N}{2}(2d-2-h)}.
\]

## Assumptions and scope
Use the standard character \(\omega=e^{2\pi i/N}\) and unitary shifts
\(T_ag(x)=g(x-a)\), \(M_bg(x)=\omega^{bx}g(x)\). Each projector is
\(P_{a,b}=|M_bT_ag\rangle\langle M_bT_ag|\) on \(\mathbb C^N\). The rank is the complex-linear span dimension in \(M_N(\mathbb C)\); equivalently it counts identifiable independent Hermitian observables in the real-linear span. It is **not** the rank of the ordinary Gabor vector frame, which spans \(\mathbb C^N\) for every nonzero window, nor a claim that failure of informational completeness necessarily causes failure of nonlinear phase retrieval on pure states.

The formulas use only integer arithmetic and apply to all composite as well as prime dimensions. Length \(k=N\) is excluded from the optimization; the constant full-support window has rank \(N\) and is not informationally complete for \(N>1\).

## Proof
**1. Projector rank equals ambiguity support.** Put
\[
 A(a,b)=\langle g,M_bT_ag\rangle
 =\frac1k\sum_{x\in I\cap(I+a)}\omega^{bx},\qquad I=\{0,\ldots,k-1\}.
\]
The \(N^2\) Weyl matrices \(M_bT_a\) form a Hilbert--Schmidt orthogonal basis for \(M_N(\mathbb C)\). Conjugation by \(M_vT_u\) multiplies each Weyl coefficient by a character of \(\mathbb Z_N^2\). The \(N^2\)-point Fourier matrix on that group therefore diagonalizes the analysis map of the projector orbit. Its singular support is exactly the set of \((a,b)\) with \(A(a,b)\ne0\). Consequently
\[
 R_N(k)=\#\{(a,b)\in\mathbb Z_N^2:A(a,b)\ne0\}.
\]
This rank/ambiguity relation is also Theorem 1 of Goldberger--Kang--Okoudjou [1], and here the remaining work is to evaluate *every* ambiguity zero for this concrete rectangular family.

**2. Exact zero count at one lag.** As subsets of \(\{0,\ldots,N-1\}\), the overlap \(I\cap(I+a)\) consists of the two disjoint intervals
\[
 \{a,\ldots,k-1\}\quad(a<k),\qquad
 \{0,\ldots,k+a-N-1\}\quad(a>N-k),
\]
with lengths \(r_a\) and \(s_a\), respectively; an interval with nonpositive length is absent. If both lengths vanish, all modulations vanish. If just one interval of length \(\ell>0\) remains, its nonzero-frequency Fourier transform vanishes precisely when \(\omega^{b\ell}=1\), while the zero-frequency value is \(\ell>0\). Among the \(N\) frequencies there are \(\gcd(N,\ell)-1\) zeros, leaving \(N-\gcd(N,\ell)+1\) nonzero coefficients.

If both intervals are present, then for \(z=\omega^b\ne1\), geometric summation and \(z^N=1\) give the identity
\[
 kA(a,b)=\frac{z^a-z^k+1-z^{k+a-N}}{1-z}
          =\frac{(1-z^k)(1+z^a)}{1-z}.
\]
At \(b=0\), the sum is \(r_a+s_a=2k-N>0\). For nonzero frequencies, zeros come from \(z^k=1\) (exactly \(d-1\) such frequencies) or \(z^a=-1\) (exactly \(\beta_N(a)\) frequencies). Their intersection has size \(\beta_d(a)\): writing \(b=(N/d)t\) reduces the simultaneous conditions to \(at\equiv d/2\pmod d\). Inclusion--exclusion gives precisely the third case for \(c_a\). Summing over lags proves the exact rank formula.

**3. Sharp informational-completeness threshold.** If \(k\le N/2\), some translated supports are disjoint, so the rank cannot be \(N^2\). Now assume \(k>N/2\). For odd \(N\), both \(\beta_N\) and \(\beta_d\) vanish identically, hence the exact formula is full rank precisely when every integer in
\[
 \{2k-N,2k-N+1,\ldots,k\}
\]
is coprime to \(N\). With \(s=N-k\), this says exactly that every integer in \(\{s,s+1,\ldots,2s\}\) is coprime to \(N\). If \(p\) is the smallest prime factor of \(N\), the condition holds when \(2s<p\). Conversely, if \(2s\ge p\), that interval contains a multiple of \(p\): use \(p\) itself when \(s<p\), or the first multiple of \(p\) at least \(s\) when \(s\ge p\). This proves the stated odd-order threshold. If \(N\) is even and \(k>N/2\), the double-overlap lag \(a=N/2\) and any odd frequency \(b\) satisfy \(\omega^{ab}=-1\), so a Fourier coefficient vanishes. This proves the even-order impossibility.

**4. Exact power-of-two capacity.** Let \(N=2^q\), and fix a nonzero modulation \(b\) whose root \(\omega^b\) has order \(t=2^j\), with \(1\le j\le q\). There are exactly \(\varphi(t)=t/2\) such modulations. Let \(Z_t(k)\) be the number of translation lags at which their ambiguity coefficient vanishes; by the factorization, this number depends on \(b\) only through \(t\).

For \(k\le N/2\), direct single-interval counting yields
\[
 Z_t(k)=N-2k+1+2\left\lfloor\frac{k-1}{t}\right\rfloor
                  +\mathbf1_{t\mid k}\ \ge\frac Nt.
\]
The expression is nonincreasing as \(k\) increases and reaches \(N/t\) at \(k=N/2\). The zero modulation also has at least one vanishing lag, so the total number of ambiguity zeros is strictly larger than
\(\sum_{j=1}^{q}(2^{j-1}N/2^j)=qN/2\).

For \(k>N/2\), put \(s=N-k\). If \(t\nmid k\), the two single-overlap boundary ranges contribute zeros only at lags congruent to \(-s\) and \(s\) modulo \(t\), respectively, while the central double-overlap range contributes zeros only at lags congruent to \(t/2\) modulo \(t\). Writing \(s=ut+v\) with \(0<v<t\), the two boundaries each contain \(u+\mathbf1_{v\ge t/2}\) such lags and the central range contains \(N/t-2u-2\mathbf1_{v\ge t/2}\). Therefore **exactly** \(Z_t(k)=N/t\).

If \(t\mid k\), then \(t\mid s\); the double-overlap coefficient vanishes at *every* central lag, and direct counting gives
\[
 Z_t(k)=N-2s+\frac{2s}{t}
          =\frac Nt+\frac{t-1}{t}(2k-N)>\frac Nt.
\]
The zero modulation has no vanishing lag in this regime. Summing \(Z_t(k)\) with multiplicity \(\varphi(t)=t/2\) shows that the deficiency is at least \(qN/2\), with equality exactly when no \(t=2^j>1\) divides \(k\), i.e. exactly when \(k\) is odd. For general \(k>N/2\), the excess is
\[
 \frac{2k-N}{2}\sum_{j=1}^{h}(2^j-1)
 =\frac{2k-N}{2}(2d-2-h),
\]
which proves the precise formula and optimality, including uniqueness of the optimal *lengths*.

## Verification
A standalone, standard-library Python checker is supplied as `verify_boxcar.py`. Run `python3 verify_boxcar.py`. It computes the Fourier zero test independently of the gcd formulas: every overlap polynomial is reduced by exact integer division modulo the cyclotomic polynomial associated with each character, without floating-point tolerances. It verified every lag, frequency and length for each \(3\le N\le24\), including both rank boundaries and the power-of-two optimizers. These finite checks are supporting evidence; the all-dimensional proof above is independent of enumeration.

For example, the rank profiles for lengths \(1\le k<N\) are \((8,23,38,51,52,50,52)\) at \(N=8\) and \((9,27,43,59,77,71,77,81)\) at \(N=9\). Longer rectangular windows can *lose* linearly identifiable operator directions. The odd-composite dimension \(N=25\) first attains rank \(625\) at length \(23\), while at \(N=16\) the maximum is \(224\), attained exactly at lengths \(9,11,13,15\).

## Relationship to prior work
Goldberger--Kang--Okoudjou [1] provide the general Gram-rank/ambiguity equivalence and classify other special families; this result applies that equivalence to every cyclic boxcar length and evaluates the complete rank deficiency, not merely whether some coefficient vanishes. Bendory--Eldar [2, Corollary 3.2] already give a sufficient coprimality hypothesis for stable rectangular-window STFT recovery. In the odd case, that sufficient condition covers every successful length identified by our theorem; **those sufficient recoverability claims are not asserted as new**. The new content here is the exact rank at every unsuccessful length, the converse arithmetic classification of linear completeness, and the sharp power-of-two maximal rank with all optimal lengths. Bendory--Eldar--Boumal [3, Lemma 5] study admissible short windows and nonlinear phase-recovery methods, not the complete rank profile of the lifted boxcar measurement family. Published work on sparse multiwindow Gabor systems concerns a different window class and a multiwindow rather than single-window capacity; it is not used to infer the present rank formula.

## Limitations
Informational completeness means injectivity on *all Hermitian matrices* of the lifted measurement map; nonlinear pure-state phase retrieval is weaker and can sometimes succeed with a deficient operator span. This finding does not establish noise conditioning or a recovery algorithm, and it does not classify nonrectangular or multiwindow probes. The rank formula includes previously understood endpoint special cases; its claim of originality concerns the complete boxcar family and its sharp arithmetic consequences. Unindexed earlier rank censuses remain a literature risk. All statements use unit time and frequency shifts on the full cyclic phase space, not subsampling.

## References
[1] A. Goldberger, S. Kang and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1 (first public 2021-06-02), https://arxiv.org/html/2106.01509v1 .

[2] T. Bendory and Y. C. Eldar, *A Least Squares Approach for Stable Phase Retrieval from Short-Time Fourier Transform Magnitude*, arXiv:1510.00920v1 (first public 2015-10-04), https://arxiv.org/html/1510.00920v1 .

[3] T. Bendory, Y. C. Eldar and N. Boumal, *Non-Convex Phase Retrieval From STFT Measurements*, IEEE Transactions on Information Theory **64** (2018), 467--484; lawful full text https://www.weizmann.ac.il/math/yonina/sites/math.yonina/files/uploads/publications/Non-Convex%20Phase%20Retrieval%20From_0.pdf ; first arXiv preprint 2016-07-27 (arXiv:1607.08218).

