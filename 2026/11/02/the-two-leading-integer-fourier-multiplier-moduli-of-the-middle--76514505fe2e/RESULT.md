# The two leading integer Fourier multiplier moduli of the middle-thirds Cantor measure

## Finding
Let \(\mu\) be the probability law on \([0,1]\) of \(X=\sum_{j=1}^{\infty}2B_j3^{-j}\), where the \(B_j\) are independent fair Bernoulli variables. Define the Fourier–Stieltjes coefficients
\[
\widehat\mu(n)=\int_{[0,1]}e^{-2\pi i n x}\,d\mu(x),\qquad n\in\mathbb Z.
\]
Set
\[
A=\prod_{j=1}^{\infty}\left|\cos\frac{2\pi}{3^j}\right|,
\qquad B=\prod_{j=1}^{\infty}\left|\cos\frac{8\pi}{3^j}\right|,
\qquad C=\frac9{32}\cos\frac{\pi}{9}.
\]
Then \(A>B>C>1/4\). For nonzero integer frequencies the exact first and second largest absolute Fourier–Stieltjes coefficient values are \(A\) and \(B\), with all equality cases:
\[
|\widehat\mu(n)|=A\iff n=\pm3^a\ (a\in\mathbb Z_{\ge0}),
\qquad
|\widehat\mu(n)|=B\iff n=\pm4\cdot3^a\ (a\in\mathbb Z_{\ge0}).
\]
Every remaining nonzero integer frequency obeys the explicit strict gap bound
\[
|\widehat\mu(n)|\le C<B.
\]
Numerically, \(A\approx0.3714373567087654\), \(B\approx0.2655694472818223\), and \(C\approx0.2642885495960368\). The exact values are the displayed convergent products.

Equivalently, convolution by \(\mu\) on the circle has \(L^2\) norm \(A\) on the zero-mean subspace, and norm \(B\) after the Fourier modes \(n=\pm3^a\) are removed. After also removing \(n=\pm4\cdot3^a\), its norm is at most \(C<B\). The constants \(A\) and \(B\) are attained (at infinitely many modes).

## Assumptions and scope
The Fourier transform uses \(e^{-2\pi i n x}\), not a \(2\pi\)-free frequency convention. All statements concern integer \(n\), the symmetric absolute values of the coefficients, and the standard equal-weight middle-third Cantor measure. The frequency \(n=0\) has coefficient \(1\) and is excluded from the ranking. The subspace norm statements concern the closures of the spans of the designated Fourier characters in \(L^2(\mathbb R/\mathbb Z)\). No assertion about noninteger frequencies or arbitrary Bernoulli convolutions is made.

## Proof
**Product and scale invariance.** Independence yields
\[
\widehat\mu(n)=(-1)^n\prod_{j=1}^{\infty}\cos\frac{2\pi n}{3^j},
\quad F(n):=|\widehat\mu(n)|=\prod_{j=1}^{\infty}\left|\cos\frac{2\pi n}{3^j}\right|.
\]
Absolute convergence of the product tail follows from \(1-\cos x\le x^2/2\) for small \(x\). Since the first factor at frequency \(3m\) has modulus \(1\), shifting the other indices gives \(F(3m)=F(m)\). Hence it suffices to compare positive integers \(n\) not divisible by \(3\).

**Universal paired-factor inequality.** For every \(u\in[1/3,1)\), let \(c=\cos(2\pi u/3)\). The angle lies in \([2\pi/9,2\pi/3)\), so \(c^2\le3/4\). By the triple-angle identity,
\[
\left|\cos(2\pi u)\cos(2\pi u/3)\right|
=|4c^4-3c^2|\le\frac9{16},
\]
because the quadratic \(4v^2-3v\) ranges over \([-9/16,0]\) for \(0\le v\le3/4\).

**All sufficiently large reduced frequencies.** If \(n\ge9\) and \(3\nmid n\), let \(L\ge3\) satisfy \(3^{L-1}\le n<3^L\). Apply the paired-factor inequality to factors \(j=L,L+1\) with \(u=n/3^L\). Factor \(j=1\) has modulus \(1/2\). Independently, factor \(j=2\) is at most \(\cos(\pi/9)\), by considering the six nonzero residue classes modulo \(9\). These four factors have distinct indices; every other factor is at most \(1\). Therefore
\[
F(n)\le\frac12\cos\frac\pi9\cdot\frac9{16}=C.
\]

**Small reduced frequencies.** The only positive reduced integers less than \(9\) are \(1,2,4,5,7,8\). For \(n=2,7\), the second factor has modulus \(\cos(4\pi/9)<1/2\). For \(n=5\), the third factor is \(\cos(10\pi/27)<1/2\); for \(n=8\) it has modulus \(|\cos(16\pi/27)|<1/2\). As each of these four frequencies also has first factor \(1/2\), they satisfy \(F(n)\le1/4<C\). Thus only \(n=1,4\) can exceed \(C\).

**Strict separation with a rational certificate.** For \(n=4\), the first factor is \(1/2\), the second is \(\cos(\pi/9)\), and the third is \(\cos(8\pi/27)>0\). The tail satisfies
\[
\prod_{j=4}^{\infty}\cos\frac{8\pi}{3^j}
\ge1-\frac12\sum_{j=4}^{\infty}\left(\frac{8\pi}{3^j}\right)^2
=1-\frac{4\pi^2}{729}.
\]
This follows by \(\cos t\ge1-t^2/2\) and \(\prod(1-a_j)\ge1-\sum a_j\) for \(a_j\in[0,1]\). The elementary bound \(\pi<22/7\), with \(x=176/189<1\), and the alternating Taylor lower bound for cosine give
\[
\cos\frac{8\pi}{27}\prod_{j=4}^{\infty}\cos\frac{8\pi}{3^j}
>
\left(1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}\right)
\left(1-\frac4{729}\left(\frac{22}7\right)^2\right)
>\frac9{16}.
\]
The final strict inequality is between explicit rational numbers; `check_cantor.py` verifies it with exact fractions. Multiplying by \(\tfrac12\cos(\pi/9)\) gives \(B>C\). Also \(C>1/4\) follows from \(\cos(\pi/9)>1-(22/63)^2/2>8/9\).

To compare the top level, the same tail argument gives
\[
A\ge\frac12\cos\frac{2\pi}{9}\left(1-\frac{\pi^2}{324}\right)
>\frac12\left(1-\frac12\left(\frac{44}{63}\right)^2\right)
\left(1-\frac1{324}\left(\frac{22}7\right)^2\right)>\frac9{32}.
\]
For \(n=4\), apply the paired-factor inequality at \(j=2,3\) and the first factor \(1/2\) to get \(B\le9/32\). Hence \(A>B\). Scaling invariance and reflection symmetry now identify *all* equality cases. The circle convolution claims follow by diagonalization on Fourier characters and Plancherel's theorem.

## Verification
Run `python check_cantor.py` with Python 3 and no third-party dependencies. The program verifies exactly, using rational fractions, the strict polynomial certificates \(B>C\), \(A>9/32\), and \(C>1/4\). It separately compares truncated products at 20,000 integers as a non-probative consistency probe. The infinite-frequency theorem and uniqueness assertions follow from the analytic inequalities above, not from the finite probe or floating-point arithmetic.

## Relationship to prior work
The classical Bernoulli convolution product and the fact that integer Fourier coefficients persist under triadic dilation are background. Sidorov and Solomyak (2002 preprint, 2003 journal) prove countability and derived-set statements for the Fourier multiplier spectrum of Bernoulli convolutions, including the normalized Cantor measure, but their inspected main statements do not specify its two largest nontrivial coefficient moduli or their exact extremizing frequencies. Sarnak (1980) addresses the full convolution spectrum without an identified comparable two-tier classification in accessible metadata; its full text was not available for definitive comparison. Huang (2016 preprint) treats measure rigidity for multiplication-invariant measures, with different conclusions. The assessed contribution is the exact two-tier order and a uniform explicit separation from every other Fourier mode.

## Limitations
The theorem does not characterize the third-largest value, the full coefficient spectrum, or the ordering of all remaining modes; \(C\) is a certified upper bound, not asserted sharp. The originality comparison is bounded by accessible primary text and database results; unavailable older spectrum literature remains a residual risk. The accompanying checker is not an independent mathematical audit.

## References
1. N. Sidorov and B. Solomyak, *Spectra of Bernoulli convolutions as multipliers in \(L^p\) on the circle*, arXiv:math/0210053, first public version 2002-10-03; Duke Math. J. 120 (2003), 353–370. https://arxiv.org/abs/math/0210053
2. P. Sarnak, *Spectra of singular measures as multipliers on \(L^p\)*, J. Functional Analysis 37 (1980), 302–317. https://doi.org/10.1016/0022-1236(80)90046-4
3. H. Huang, *Fourier coefficients of multiplication-invariant measures*, arXiv:1606.06078, first public version 2016-06-20. https://arxiv.org/abs/1606.06078
