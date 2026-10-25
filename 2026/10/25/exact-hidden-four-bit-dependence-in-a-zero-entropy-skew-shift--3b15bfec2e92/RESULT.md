# Exact hidden four-bit dependence in a zero-entropy skew shift

## Finding
Let \(\alpha\in\mathbb R\setminus\mathbb Q\), let \(S_\alpha(x,y)=(x+\alpha,y+x)\pmod 1\) act on the Haar two-torus, and put \(s(t)=1\) when \(\{t\}\in[0,1/2)\) and \(s(t)=-1\) otherwise. For a Haar-distributed initial point define the stationary signs \(Z_j=s(\pi_y S_\alpha^j(x,y))\), \(j\in\mathbb Z\). Then:

1. Every collection of at most **three distinct-time observations** consists of independent fair signs. The process has **zero entropy rate**, while its underlying torus transformation is uniquely ergodic.
2. For every \(h\in\mathbb Z_{\ge1}\), the four-point moment at times \(0,h,2h,3h\) equals \(\mathbb E[Z_0Z_hZ_{2h}Z_{3h}]=\Theta(h^2\alpha)\). The continuous, even, half-periodic function \(\Theta\) is specified on \(t=\alpha\bmod(1/2)\in[0,1/2)\) by

\[
\Theta(t)=\begin{cases}
\frac13-16t^2,&0\le t\le\frac16,\\[2pt]
-\frac13+32(t-\frac14)^2,&\frac16\le t\le\frac13,\\[2pt]
\frac13-16(t-\frac12)^2,&\frac13\le t\le\frac12.
\end{cases}
\]

3. The **complete length-four consecutive word law** is, for any signs \(\epsilon_j\in\{-1,1\}\),
\[
\Pr(Z_0=\epsilon_0,\ldots,Z_3=\epsilon_3)
=\frac{1+\Theta(\alpha)\epsilon_0\epsilon_1\epsilon_2\epsilon_3}{16}.
\]
In particular every such word has positive probability, and \(\lvert\Theta(\alpha)\rvert\le1/3\). Although \(\Theta(\alpha)=0\) at exceptional irrational parameters, \(\Theta(\alpha)\) and \(\Theta(4\alpha)\) **never vanish simultaneously**. Therefore the maximal degree of distinct-time independence is **exactly three for every irrational** \(\alpha\).

The exact four-word Shannon entropy (natural logarithms) is \(4\log2-\frac12[(1+\Theta)\log(1+\Theta)+(1-\Theta)\log(1-\Theta)]\), with \(\Theta=\Theta(\alpha)\). This is a finite-block entropy, not an entropy rate.

## Assumptions and scope
All probabilities and expectations use normalized Haar measure on \(\mathbb T^2\); they are not assertions about independent random initial points at each time. The sign partition assigns its measure-zero boundary to the positive half-circle. The map is an invertible affine torus homeomorphism. The formulas for marginal independence and the four-point moments actually hold for arbitrary real \(\alpha\); irrationality is invoked to place them in a uniquely ergodic example. Distinct-time independence is meant jointly at any three different integer indices, not only consecutive ones. Entropy rate is Kolmogorov--Sinai entropy of the stationary binary factor.

## Proof
**Orbit coordinates, invariance and entropy.** The exact iterates, valid for all integer \(j\), are
\[
\pi_x S_\alpha^j(x,y)=x+j\alpha,\qquad
\pi_y S_\alpha^j(x,y)=y+jx+\binom j2\alpha\pmod1.
\]
The linear part has determinant one, hence Haar measure is invariant. For irrational \(\alpha\), the polynomial Weyl criterion makes each orbit uniformly distributed: for the torus character with indices \((r,s)\ne(0,0)\), its orbit phase is a polynomial whose nonconstant coefficient is irrational (linear if \(s=0\), quadratic if \(s\ne0\)). Thus Haar is uniquely invariant. A grid with widths \(O(\varepsilon/n)\) in \(x\) and \(O(\varepsilon)\) in \(y\) controls every first-\(n\) orbit distance by \(O(\varepsilon)\), since \(\Delta y_j=\Delta y+j\Delta x\). Consequently spanning numbers grow at most linearly with \(n\) for fixed \(\varepsilon\), so topological entropy and its measurable factor entropy are zero.

**Three-wise independence.** For distinct integers \(i,j\), the affine Haar map \((x,y)\mapsto(y+ix+\binom i2\alpha,\ y+jx+\binom j2\alpha)\) has integer linear determinant \(i-j\ne0\), hence maps Haar onto Haar on \(\mathbb T^2\). Therefore \(Z_i,Z_j\) are independent fair signs. Translating the initial \(y\) by \(1/2\) flips *every* sign, and preserves Haar. Thus the expectation of any product of an odd number of distinct signs, including any triple, is zero. For symmetric \(\pm1\) variables, the Walsh expansion of each three-sign law has only marginal, pair, and triple moments; all nonconstant moments vanish, so it is the uniform law on \(\{-1,1\}^3\).

**Fourier computation of the four-point moment.** Write \(c_k=\int_0^1s(t)e^{-2\pi i kt}\,dt\). Then \(c_k=0\) for even \(k\), including zero, and \(c_k=2/(\pi i k)\) for odd \(k\). For consecutive times, the Haar integral is
\[
\Theta(\alpha)=\iint s(y)s(y+x)s(y+2x+\alpha)s(y+3x+3\alpha)\,dx\,dy.
\]
It is even and \(1/2\)-periodic in \(\alpha\), as is also clear from the Fourier constraints below. For \(r\in\mathbb Z\), its Fourier coefficient at frequency \(2r\) in \(\alpha\) arises from odd integers \((k_0,k_1,k_2,k_3)\) satisfying
\[
\sum_{j=0}^3k_j=0,\qquad \sum_{j=0}^3jk_j=0,\qquad k_2+3k_3=2r.
\]
Writing \(v=k_3\) gives \((k_0,k_1,k_2,k_3)=(2r-v,3v-4r,2r-3v,v)\). Fejér regularization of \(s\) justifies the Fourier multiplication and passage to the limit; at each fixed \(r\) the resulting sum is absolutely convergent. Its value is
\[
\widehat\Theta(r)=\frac{16}{\pi^4}\sum_{v\in2\mathbb Z+1}
\frac1{(2r-v)(3v-4r)(2r-3v)v}.
\]
For \(r=0\) this is \(16/(9\pi^4)\sum_{v\,\mathrm{odd}}v^{-4}=1/27\). For \(r\ne0\), partial fractions in \(v\) give the residues \(-1,1,-3,3\), divided by \(16r^3\), at poles \(0,2r,4r/3,2r/3\), respectively. Using the symmetrically interpreted sum \(\sum_{v\,\mathrm{odd}}(v-a)^{-1}=(\pi/2)\tan(\pi a/2)\) at these non-odd poles, one obtains
\[
\widehat\Theta(r)=\frac{3}{\pi^3r^3}\tan\left(\frac{\pi r}{3}\right)
=\frac{6}{\pi^3r^3}\sin\left(\frac{2\pi r}{3}\right).
\]
The claimed three-piece quadratic has mean \(1/27\), is continuously differentiable and has second derivative \(-32\) on the two outer intervals and \(64\) on the middle interval. Integration by parts yields exactly the same Fourier coefficients, and uniqueness of Fourier series of continuous periodic functions proves the displayed formula for \(\Theta\). (At junctions take either adjacent piece.)

**Arbitrary arithmetic spacing and a universal fourth-order witness.** For \(h\ge1\), set \(x'=hx+\binom h2\alpha\). Since multiplication by integer \(h\) sends Haar to Haar, \(x'\) is uniform independently of \(y\), and
\[
\pi_yS_\alpha^{kh}(x,y)=y+kx'+\binom k2h^2\alpha\pmod1.
\]
The four-point moment is therefore \(\Theta(h^2\alpha)\). On the half-period \([0,1/2)\), the only zeros are \(t=1/(4\sqrt3)\) and \(t=1/2-1/(4\sqrt3)\). At either zero the reduced argument of \(4\alpha\) is \(1/\sqrt3-1/2\), or its reflection, so
\[
\Theta(4\alpha)=-9+\frac{16}{\sqrt3}>0.
\]
Thus either \(h=1\) or \(h=2\) witnesses failure of four-wise independence, for every \(\alpha\). Finally the Walsh inversion formula for four fair signs with vanishing one-, two- and three-point moments gives the complete four-word law and entropy formula.

## Verification
Run `python3 verify.py` from this directory. The standalone checker exactly integrates the sign products by rational-polygon clipping for nine rational parameters and spacings one, two and three (27 comparisons); independently verifies all sixteen four-word probabilities for five rational parameters; checks the parity relations for 364 time triples; tests ten nonzero Fourier coefficients against rapidly convergent symmetric sums; and checks the exceptional-parameter two-step witness. It uses only the Python standard library. The exact rational computations check finite examples, while the unbounded claims follow from the analytical Fourier and Haar arguments above.

## Relationship to prior work
The classical irrational skew shift and its unique ergodicity are treated explicitly in Tao's 4 February 2008 lecture (proofs of ergodicity and unique ergodicity). Frantzikinakis' 2014 preprint, *Multiple correlation sequences and nilsequences*, gives general structural decomposition results for multiple-correlation sequences, but its theorems do not give the particular half-circle sign process's exact 16-word law, the three-piece quadratic fourth moment, or the lag-one/lag-two nonvanishing alternative. The distinction is between a general framework and these explicit finite-time formulas. The present claim is not an assertion that skew shifts, nilsequence structure, Walsh moment inversion, or Fourier methods are newly discovered.

## Limitations
This is a precise theorem about one prescribed half-circle observable and the Haar-distributed phase, not a claim about all observables, every four-time pattern, positive entropy, mixing, or independent full trajectories. The explicit fourth-moment formula covers four-term arithmetic progressions of times, not arbitrary ordered quadruples. The binary process may have additional longer-range dependencies beyond those quantified here. Earlier implicit equivalent computations in specialized literature cannot be categorically ruled out without independent historical scrutiny. No independent scientific audit has been performed.

## References
- Terence Tao, *254A, Lecture 9: Ergodicity*, 4 February 2008, especially Propositions 1 and 3 on the irrational skew shift. https://terrytao.wordpress.com/2008/02/04/254a-lecture-9-ergodicity/
- Nikos Frantzikinakis, *Multiple correlation sequences and nilsequences*, arXiv:1407.0631, first posted 2 July 2014, revised 21 March 2015. https://arxiv.org/abs/1407.0631
- H. Furstenberg, *Strict ergodicity and transformation of the torus*, American Journal of Mathematics 83 (1961), 573–601, classical background on the transformation and strict ergodicity. https://doi.org/10.2307/2372899
