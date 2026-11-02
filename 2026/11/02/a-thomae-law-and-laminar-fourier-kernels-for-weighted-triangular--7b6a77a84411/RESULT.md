# A Thomae law and laminar Fourier kernels for weighted triangular self-similar measures

## Finding
Fix any odd prime \(p\). For each \(0<t<1/2\), let \(\mu_{p,t}\) be the probability distribution of
\[
X=\sum_{j=1}^{\infty}p^{-j}D_j,\qquad
\mathbb P(D_j=0)=1-2t,\quad
\mathbb P(D_j=e_1)=\mathbb P(D_j=e_2)=t,
\]
with independent identically distributed digits. Write
\(Z_{p,t}=\{(m,n)\in\mathbb Z^2:\widehat\mu_{p,t}(m,n)=0\}\), using the Fourier transform with exponent \(-2\pi i\langle\xi,x\rangle\).

Let \(k\ge1\) and \(a\) be integers satisfying
\[
\gcd(a,p)=1,\qquad p^k/4<a<p^k/2.
\]
Define the exceptional weight and the associated lattice set by
\[
\tau_{p;k,a}=
\frac{1}{2\left(1-\cos(2\pi a/p^k)\right)},
\]
\[
E_{p;k,a}=\bigcup_{v\ge0}
\left\{(m,n)\in\mathbb Z^2:
(m,n)\equiv p^v(a,-a)\ \text{or}\ p^v(-a,a)
\pmod{p^{v+k}}\right\}.
\]
The complete parameter classification is
\[
Z_{p,t}=\begin{cases}
E_{p;k,a},&t=\tau_{p;k,a}\text{ for a pair }(k,a)\text{ above},\\
\varnothing,&\text{otherwise}.
\end{cases}
\]
The parameter pair is unique whenever it exists, and each frequency in its zero set has exactly one vanishing Fourier-product factor. The centered-square natural density exists and is
\[
\delta_p(t)=\begin{cases}
\displaystyle\frac{2}{p^{2(k-1)}(p^2-1)},&t=\tau_{p;k,a},\\
0,&\text{otherwise}.
\end{cases}
\]
For \(L\ge k\), the number of residue classes modulo \(p^L\) whose **first \(L\) Fourier-product factors** include a zero is exactly
\[
2\sum_{j=k}^{L}p^{2(L-j)}
=\frac{2\bigl(p^{2(L-k+1)}-1\bigr)}{p^2-1};
\]
for \(L<k\), the number is zero. These finite-level counts do not assert that the complete infinite Fourier-zero set is periodic modulo \(p^L\).

The exceptional weights form a countable dense subset of \((1/4,1/2)\). The function \(t\mapsto\delta_p(t)\) is continuous at every nonexceptional weight in \((0,1/2)\) and discontinuous at every exceptional weight: a Thomae-type density law.

Furthermore the zero sets are *laminar*: for two distinct exceptional weights with canonical labels \((k,a)\), \((\ell,b)\), if \(k<\ell\) then
\[
E_{p;\ell,b}\subset E_{p;k,a}
\quad\Longleftrightarrow\quad
b\equiv a\text{ or }-a\pmod{p^k},
\]
and otherwise they are disjoint; if \(k=\ell\), their zero sets are disjoint. Thus the kernels of torus convolution by the periodizations of \(\mu_{p,t}\) are either nested or orthogonal in \(L^2(\mathbb T^2)\).

For example, at \(p=5\), the nonuniform choice
\[
\tau_{5;1,2}=\frac{5-\sqrt5}{10}
\]
has zero-frequency density \(1/12\), whereas the equal-weight choice \(t=1/3\) has **no integer Fourier zeros** at base five. The higher-conductor choices \(\tau_{5;2,7}\) and \(\tau_{5;2,8}\) each have density \(1/300\): their zero sets are disjoint and both lie inside the zero set for \(\tau_{5;1,2}\).

## Assumptions and scope
All primes \(p\) are odd; the weights are strictly positive because \(0<t<1/2\). Frequencies are integer lattice pairs, not arbitrary real frequencies. The digit set is \(\{0,e_1,e_2\}\) with equal weights on the nonzero digits and unrestricted positive remaining weight; arbitrary independent three-weight vectors are not covered. For periodic convolution, reduce the measure modulo \(\mathbb Z^2\) and use the standard Fourier basis of \(L^2(\mathbb T^2)\). The density of a lattice set \(E\) is defined as the limit, when it exists, of
\[
\frac{|E\cap([-R,R]^2\cap\mathbb Z^2)|}{(2R+1)^2},\qquad R\to\infty\text{ through integers}.
\]

## Proof
**1. Factorization and nonvanishing of the remaining product.** Independence gives, for each integer pair \((m,n)\),
\[
\widehat\mu_{p,t}(m,n)=\prod_{j=1}^{\infty}M_t(m/p^j,n/p^j),\qquad
M_t(x,y)=1-2t+t e^{-2\pi i x}+t e^{-2\pi i y}.
\]
For a fixed frequency, \(\sum_j|1-M_t(m/p^j,n/p^j)|<\infty\). Hence the infinite product can vanish **only if** some factor vanishes: once no factor is zero, its tail is a convergent nonzero product. This also proves that cancellation at an individual factor is sufficient.

**2. Rigidity of a weighted three-root cancellation.** Suppose \(M_t(m/p^j,n/p^j)=0\). Put \(u=e^{-2\pi i m/p^j}\), \(v=e^{-2\pi i n/p^j}\), both roots of unity of odd order. Their sum is the strictly negative real number \(-(1-2t)/t\). For two unit complex numbers, a real nonzero sum forces \(v=\overline u\): by the sine addition identity, the alternative is \(v=-u\), which gives sum zero. Consequently \(n\equiv-m\pmod{p^j}\), and
\[
\cos(2\pi m/p^j)=1-\frac{1}{2t}<0.
\]
Odd prime-power roots cannot equal \(-1\), so a solution requires \(1/4<t<1/2\). Let \(p^k\) be the exact order of \(u\). Then there is a unique integer \(a\) with \(p\nmid a\) and \(p^k/4<a<p^k/2\) for which \(u\) has angle congruent to \(\pm2\pi a/p^k\). Thus \(t=\tau_{p;k,a}\). Conversely such a parameter gives zeros for the two residues \((\pm a,\mp a)\) at scale \(p^k\). Equality of two such cosine values forces equality of their reduced rational angles up to sign, proving uniqueness of \((k,a)\).

**3. Exact zero locus and unique level.** A level-\(j\) cancellation with a root of exact order \(p^k\) occurs exactly when \(j\ge k\) and
\[
(m,n)\equiv(\pm a p^{j-k},\mp a p^{j-k})\pmod{p^j}.
\]
Because \(p\nmid a\), both coordinates have \(p\)-adic valuation \(j-k\). Thus different levels cannot cancel for a single frequency. Set \(v=j-k\) to obtain the asserted union \(E_{p;k,a}\), disjoint by \(v\).

**4. Counting and natural density.** At any \(j\ge k\), exactly two residue pairs modulo \(p^j\) satisfy the level-\(j\) condition. Their corresponding cylinder has centered-square natural density \(2p^{-2j}\). Distinct \(j\)'s are disjoint by their coordinate valuations. For a fixed truncation \(L\), their lifts to modulus \(p^L\) have exactly \(2\sum_{j=k}^L p^{2(L-j)}\) elements. The uncounted tail with \(j>L\) has both coordinates divisible by \(p^{L-k+1}\), so its upper centered-square density is at most \(p^{-2(L-k+1)}\). Sending \(L\to\infty\) proves existence of the full density and sums the geometric series:
\[
2\sum_{j=k}^{\infty}p^{-2j}
=\frac{2}{p^{2(k-1)}(p^2-1)}.
\]

**5. Laminar kernels.** For two exceptional parameters of conductors \(k\le\ell\), a frequency belonging to both must have the same common \(p\)-adic valuation \(v\). Reducing the two unit-residue conditions modulo \(p^k\) shows that overlap is possible precisely when \(b\equiv\pm a\pmod{p^k}\). If \(k<\ell\) and this holds, every deeper cylinder lies inside the corresponding shallower cylinder, giving containment. Otherwise the cylinders are disjoint. The case \(k=\ell\) is disjoint for distinct canonical labels. Fourier diagonalization of convolution proves the identical alternative for the corresponding closed operator kernels.

**6. Dense discontinuities.** Primitive fractions with denominators \(p^k\) are dense in \((1/4,1/2)\); the continuous strictly monotone map \(x\mapsto[2(1-\cos2\pi x)]^{-1}\) carries them onto a countable dense set of exceptional weights. Every exceptional weight has positive density but is approached by nonexceptional weights with density zero. At a nonexceptional weight, any convergent sequence of exceptional weights must have conductors tending to infinity (only finitely many labels exist below a given conductor); the density values then tend to zero. This proves exactly the claimed continuity set.

## Verification
The companion script `weighted_triangular_checker.py` checks the mask-zero congruence against numerical complex-mask evaluations for \((p,k,a)=(3,1,1),(5,1,2),(5,2,7),(5,2,8),(7,1,2)\) at finite resolution; it also checks modular first-hit counts and the nested/disjoint examples. The golden-ratio cancellation is separately checked in exact symbolic arithmetic using \(\cos(4\pi/5)=-(1+\sqrt5)/4\). These tests corroborate finite instances only. The infinite assertions and exact density rely on the six analytic proof steps above, not the script.

## Relationship to prior work
Lam–Leung's work concerns sums of roots of unity with **unit integral coefficients** and does not determine which continuous nonuniform probability weights force cancellations. Dutkay–Jorgensen develop Fourier analysis and infinite-product methods for affine IFS measures, focusing on equal-weight spectral constructions; those general tools do not state the parameter-dependent integer-zero density or the laminar family proved here. Published investigations of the spectrality of planar Sierpiński-type measures use equal digit weights, and results about weighted Fourier frames use weights on exponential frame elements, not the unequal IFS probabilities here. The previously established equal-weight ternary triangular law is recovered at \(p=3,t=1/3\), and is not claimed as new.

## Limitations
The classification is confined to odd-prime integer scaling, the indicated symmetric one-parameter positive weights, and integer frequencies. It does not establish spectral bases, Fourier decay, exact real-frequency zero loci, or a general result for all positive three-component weight vectors. An equivalent earlier result in broader work on self-similar distributions or cyclotomic mask zeros has not been conclusively ruled out; no independent audit has been performed.

## References
1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209, first public version 1995-11-13; *Journal of Algebra* 224 (2000), 91–109. https://arxiv.org/abs/math/9511209
2. D. E. Dutkay and P. E. T. Jorgensen, *Fourier frequencies in affine iterated function systems*, arXiv:math/0604547, first public version 2006-04-25; *Journal of Functional Analysis* 247 (2007), 110–137. https://arxiv.org/abs/math/0604547
3. R. S. Strichartz, *Self-similar measures and their Fourier transforms. II*, *Transactions of the American Mathematical Society* 336 (1993), 335–361. DOI: 10.1090/S0002-9947-1993-1081941-2 (full text not inspected).
4. D. E. Dutkay and R. Ranasinghe, *Weighted Fourier frames on self-affine measures*, *Journal of Mathematical Analysis and Applications* 462 (2018), 1032–1047. DOI: 10.1016/j.jmaa.2017.12.055.
5. Q. Li and M.-M. Zhang, *Spectrality of planar Moran–Sierpiński-type measures*, *Revista de la Unión Matemática Argentina* (2024). DOI: 10.33044/revuma.2932 (abstract inspected).
