# Arithmetic resonances and geometric multiplicity laws for Bernoulli Fourier zeros

## Finding

For \(0<\lambda<1\), let \(\mu_\lambda\) be the law of the random series \(\sum_{j=0}^{\infty}\varepsilon_j\lambda^j\), where the signs are independent and equally likely to be \(+1\) or \(-1\). Adopt the Fourier–Stieltjes convention
\[
F_\lambda(t)=\int_{\mathbb R}e^{itx}\,d\mu_\lambda(x)
=\prod_{j=0}^{\infty}\cos(\lambda^jt).
\]
For \(t>0\) with \(F_\lambda(t)=0\), denote the order of this *entire-function* zero by \(m_\lambda(t)\). Let \(N_{\lambda,m}(R)\) count distinct such \(t\in(0,R]\) with order exactly \(m\), and let \(N_{\lambda,\mathrm{all}}(R)\) count zeros with their orders.

Put
\[
\mathcal Q_{\mathrm{odd}}=\{a/b:a,b\text{ positive odd integers}\},\qquad
\mathcal E=\{\lambda\in(0,1):\lambda^k\in\mathcal Q_{\mathrm{odd}}\text{ for some }k\ge1\}.
\]

**Theorem (complete real-zero multiplicity census).** The following conclusions hold.

1. If \(\lambda\notin\mathcal E\), every real zero is simple and
\[
N_{\lambda,1}(R)=\frac{R}{\pi(1-\lambda)}+O_\lambda(\log(2+R)),
\qquad N_{\lambda,m}(R)=0\quad(m\ge2).
\]

2. If \(\lambda\in\mathcal E\), let \(k\ge1\) be the **least** integer for which \(\lambda^k=a/b\) in lowest terms with \(a,b\) positive odd integers. Necessarily \(1\le a<b\). Every order \(m\ge1\) occurs, and for each *fixed* \(m\),
\[
\boxed{\displaystyle
N_{\lambda,m}(R)=
\frac{(b-1)^2}{\pi b^{m+1}(1-\lambda)}R
+O_{\lambda,m}(\log(2+R)).}
\]
The number of distinct positive zeros satisfies
\[
\boxed{\displaystyle
N_{\lambda,\mathrm{distinct}}(R)=
\frac{b-1}{\pi b(1-\lambda)}R+O_\lambda(\log(2+R)).}
\]
The smallest positive frequency at which the order is *at least* \(m\) is exactly
\[
\boxed{\displaystyle
\min\{t>0:m_\lambda(t)\ge m\}=\frac\pi2 b^{m-1},
\qquad m_\lambda\!\left(\frac\pi2b^{m-1}\right)=m.}
\]

3. In either case, with multiplicities included,
\[
\boxed{\displaystyle
N_{\lambda,\mathrm{all}}(R)=\frac{R}{\pi(1-\lambda)}+O_\lambda(\log(2+R)).}
\]
The exceptional set \(\mathcal E\) is countable, dense in \((0,1)\), and has Lebesgue measure zero. Thus a generic parameter has only simple zeros, whereas **every exceptional parameter has zeros of unbounded order**.

For a reduced rational parameter \(\lambda=p/q\), the exceptional case is exactly when \(p,q\) are both odd; then \(k=1,a=p,b=q\). For example, the multiplicity density at order \(m\) for \(\lambda=3/5\) equals \(\frac{8}{\pi5^m}\). At the irrational algebraic parameter \(\lambda=1/\sqrt3\), one has \(k=2,a=1,b=3\), so the same geometric multiplicity distribution holds with the different total density prescribed above.

## Assumptions and scope

The result concerns the *ordinary positive real zeros* of the entire function \(F_\lambda\), not all complex zeros and not zeros of a finite truncation. The normalization starts at index \(j=0\) with the symmetric two-point law \(\{\pm1\}\); changing the spatial Fourier convention rescales every zero location and density. The asymptotics fix \(\lambda\); the estimate for exact order \(m\) also fixes \(m\). The integer \(b\) is the denominator of the first odd-over-odd rational **power**, not necessarily the denominator of \(\lambda\).

## Proof

**Step 1: product zeros and the resonance subgroup.** The random series converges absolutely and is uniformly bounded by \((1-\lambda)^{-1}\), so its Fourier–Stieltjes transform extends to an entire function. Independence gives the displayed product, uniformly on compact subsets of the complex plane. At any fixed \(t\), the tail has no zeros and has a nonzero limit because \(\sum_j |1-\cos(\lambda^jt)|<\infty\) for all sufficiently large \(j\). Thus the zeros on the real line are exactly
\[
t=\frac\pi2\lambda^{-j}u,\qquad j\in\mathbb Z_{\ge0},\quad u\in2\mathbb Z+1,
\]
and their analytic orders equal the *number of vanishing cosine factors*: each factor has a simple zero, and only finitely many vanish at any fixed \(t\).

Two levels with indices \(j<\ell\) can share a real zero only if \(\lambda^{\ell-j}=v/u\) for odd nonzero integers \(u,v\). Conversely, every relation \(\lambda^h=a/b\) with positive odd \(a,b\) produces arbitrarily many coincidences (e.g. at \(t=\pi b^r/2\), the factor indices \(0,h,\dots,rh\) vanish). The set of integer exponents \(h\) with \(\lambda^h\in\mathcal Q_{\mathrm{odd}}\) is a subgroup of \(\mathbb Z\). If nontrivial, its positive generator is the stated \(k\). Hence coincidence can occur only between levels congruent modulo \(k\). In the absence of such an exponent, all zeros are simple.

**Step 2: unique primitive indexing in the resonant case.** Fix a residue \(r\in\{0,\dots,k-1\}\). Its level indices are \(r+kj\), \(j\ge0\), and its candidates are
\[
t_{r,j,u}=\frac\pi2\lambda^{-r}\left(\frac ba\right)^j u,
\qquad u\text{ positive odd},\quad j\ge0.
\]
If \(j\ge1\), the candidate appears at an earlier level in this same residue class precisely when \(a\mid u\): indeed an earlier level at distance \(d\) requires \(a^d\mid u\). Thus each positive zero is indexed **uniquely** by a primitive candidate with either \(j=0\), or \(j\ge1\) and \(a\nmid u\). Distinct residue classes cannot intersect by the minimality of \(k\).

For a primitive candidate, a later level at distance \(d\ge1\) contains the same frequency exactly when \(b^d\mid u\), since \((a/b)^du\) must be an odd integer and \(\gcd(a,b)=1\). Define \(v_b(u)=\max\{d\ge0:b^d\mid u\}\), meaningful also for composite \(b\). The complete multiplicity identity is
\[
\boxed{m_\lambda(t_{r,j,u})=1+v_b(u)\quad\text{for primitive }(r,j,u).}
\]
In particular, an order-\(m\) zero forces \(u\ge b^{m-1}\). Since \(\lambda^{-r}(b/a)^j\ge1\), the frequency is at least \(\pi b^{m-1}/2\). Equality is attained at \(r=j=0,u=b^{m-1}\), where the order is exactly \(m\).

**Step 3: exact leading densities.** For any fixed odd \(a,b\) with \(\gcd(a,b)=1\), the proportion among positive odd integers \(u\) having \(v_b(u)=m-1\) is
\[
\alpha_m=(1-b^{-1})b^{-(m-1)}.
\]
For the primitive levels \(j\ge1\), the additional condition \(a\nmid u\) changes that proportion to \((1-a^{-1})\alpha_m\), by inclusion–exclusion and coprimality. Counting a fixed arithmetic collection of odd integers up to \(X\) yields \(\text{proportion}\cdot X/2+O_{a,b,m}(1)\).

The positive indices \(u\) at level \((r,j)\) satisfy \(u\le 2R\lambda^r(a/b)^j/\pi\), so the leading count for order \(m\) is
\[
\frac R\pi\left(\sum_{r=0}^{k-1}\lambda^r\right)
\alpha_m\left(1+(1-a^{-1})\sum_{j=1}^{\infty}(a/b)^j\right).
\]
Use
\[
\sum_{r=0}^{k-1}\lambda^r=\frac{1-a/b}{1-\lambda},\qquad
1+(1-a^{-1})\frac{a}{b-a}=\frac{b-1}{b-a},
\]
to obtain the asserted density \((b-1)^2/[\pi b^{m+1}(1-\lambda)]\). At most \(O_\lambda(\log(2+R))\) levels can have any positive frequencies up to \(R\); each contributes only an \(O(1)\) lattice-count error, while the unused geometric tails contribute \(O(1)\). The same argument without fixing \(m\) counts all primitive indices and gives the stated distinct-zero density.

**Step 4: multiplicity-weighted census for all parameters.** Regardless of collisions, level \(j\) supplies \(R\lambda^j/\pi+O(1)\) positive vanishing factors through \(R\). There are \(O_\lambda(\log(2+R))\) active levels, and the unobserved geometric tail contributes \(O(1)\) to the formal leading sum. Therefore the total zero count with multiplicity is \(R/[\pi(1-\lambda)]+O_\lambda(\log(2+R))\), including when there are no resonances.

Finally, \(\mathcal E\) is a countable union of sets of roots of positive odd rational numbers. It is dense because the positive odd rational numbers themselves are dense in \((0,1)\); hence it is also Lebesgue-null.

## Verification

The standalone Python checker `check_zero_census.py` enumerates positive zero factors using exact rational arithmetic for the rational contractions \(1/3,3/5,3/7,2/5,3/8,1/4\). It compares the observed exact multiplicity histograms with the proven asymptotic densities, checks every displayed first high-multiplicity threshold through order five, and independently checks the two algebraic scaling chains for \(\lambda=1/\sqrt3\) using integer arithmetic. Run `python3 check_zero_census.py` with Python 3.10 or newer. Expected output is in `checker_output.txt`. These are **finite sanity checks**; the proof above, not the enumeration, establishes the results for all frequencies and parameters.

## Relationship to prior work

The infinite cosine product and the union-of-factor-zero formula are classical, and are expressly established in Jorgensen–Kornelson–Shuman's papers on orthogonal exponentials and Bernoulli convolution spectra. Their analysis also distinguishes rational contraction parities for the **existence of infinite orthogonal exponential families**. Those facts are prerequisites, not claimed as new here. The additional object classified here is the analytic zero **order**, the first location of each order, and the precise density of each multiplicity class for *all* odd-rational-power parameters, including irrational algebraic parameters. Orthogonality sets depend only on the zero **locations**, whereas the new census detects collisions and quantifies their scale. The source results give a route to these calculations but do not state this multiplicity-density and first-occurrence classification.

## Limitations

No claim is made about the complex zero distribution, optimizing constants in the logarithmic error term, uniform asymptotics as \(\lambda\) varies, or stability of inverse Fourier transforms. The exact product-zero union is prior mathematics. The analysis relies essentially on equal Bernoulli weights and the one-ratio self-similarity. An equivalent older arithmetic analysis of the product's zero orders would supersede the novelty claim; the available historical search cannot rule out all such sources.

## References

1. P. E. T. Jorgensen, K. Kornelson, and K. Shuman, *Orthogonal Exponentials for Bernoulli Iterated Function Systems*, arXiv:math/0703385 (public preprint posted 2007-03-13), especially Lemmas 2.1–2.2 and Section 4. https://arxiv.org/abs/math/0703385
2. P. E. T. Jorgensen, K. A. Kornelson, and K. L. Shuman, *Families of Spectral Sets for Bernoulli Convolutions*, arXiv:0911.2435 (public preprint posted 2009-11-12), especially equations (6)–(8) and Section 4. https://arxiv.org/abs/0911.2435
3. B. Solomyak, *Notes on Bernoulli convolutions*, expository treatment of the classical cosine-product identity. https://u.math.biu.ac.il/~solomyb/RESEARCH/Bernotes.pdf
