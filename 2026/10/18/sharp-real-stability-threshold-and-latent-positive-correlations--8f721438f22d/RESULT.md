# Sharp real-stability threshold and latent positive correlations in a batch-coalescing lattice

## Finding
For the stationary homogeneous asymmetric simple inclusion process (ASIP) with Poisson input rate \(\lambda>0\), independent gate-opening rate \(\mu>0\), and \(r=\lambda/\mu\), let \(B_j\) indicate that site \(j\) is nonempty. The joint three-site law \((B_1,B_2,B_3)\) is **strongly Rayleigh if and only if**
\[
0<r\le r_*=8+4\sqrt5.
\]
For \(r>r_*\), all three ordinary stationary pairwise covariances remain strictly negative, but multiplying the probability of each configuration by \(t^{B_2}\), then renormalizing, makes \(B_1\) and \(B_3\) positively correlated for precisely
\[
\frac{1-\sqrt{1-16(r+1)/r^2}}2<t<\frac{1+\sqrt{1-16(r+1)/r^2}}2.
\]
In particular, \(t=1/2\) detects this sharp transition. Because the first three sites are autonomous, every finite ASIP of length at least three also fails the strongly Rayleigh property above the same threshold. No all-length stability statement is asserted below the threshold.

## Assumptions and scope
At independent Poisson times of rate \(\lambda\), a particle arrives at site 1. Each site has its own independent exponential gate of rate \(\mu\); opening a gate transfers the entire population to the next site (coalescing with its population), or out of the system at the final gate. All sites have unbounded nonnegative integer occupation numbers. The Boolean indicators \(B_j=\mathbf 1\{X_j>0\}\) form a finite-state Markov factor on any initial segment. For the first three sites, a birth sets \(B_1=1\); gate \(j\), when occupied, empties \(j\) and occupies \(j+1\), except gate 3 which empties site 3. Set \(\mu=1\) by time rescaling.

For a distribution \(p\) on three Boolean variables, its multiaffine generating polynomial is \(F(z_1,z_2,z_3)=\sum_{b\in\{0,1\}^3}p(b)\prod_{j=1}^3z_j^{b_j}\). The law is *strongly Rayleigh* when \(F\) is real stable, meaning \(F\ne0\) whenever all three variables are in the open upper half-plane. A positive external field on the middle site with weight \(t>0\) means \(p_t(b)=t^{b_2}p(b)/F(1,t,1)\); it is a statistical reweighting, not a modified hopping process.

The exact stationary probabilities are, with the bit tuple always in physical order \((B_1,B_2,B_3)\):

| \((B_1,B_2,B_3)\) | Probability multiplied by \(8(1+r)^3\) |
| --- | --- |
| \((0,0,0)\) | \(8\) |
| \((1,0,0)\) | \(2r^3+6r^2+8r\) |
| \((0,1,0)\) | \(5r^2+8r\) |
| \((1,1,0)\) | \(3r^3+4r^2\) |
| \((0,0,1)\) | \(8r\) |
| \((1,0,1)\) | \(2r^3+6r^2\) |
| \((0,1,1)\) | \(3r^2\) |
| \((1,1,1)\) | \(r^3\) |

## Proof
**Stationarity and uniqueness.** Number Boolean states by \(b=B_1+2B_2+4B_3\) from 0 to 7. In the continuous-time generator \(Q\), add rate \(r\) from \(b\) to \(b\mathbin{|}1\) when these states differ. For each occupied bit \(j=0,1\), add rate 1 from \(b\) to \((b\mathbin{\&}\neg2^j)\mathbin{|}2^{j+1}\); for bit \(j=2\), clear that bit at rate 1. Each diagonal entry is minus its row's off-diagonal sum. These finite transitions follow from the underlying batch process, including when arrivals or gate openings leave the Boolean state unchanged. Direct multiplication gives \(Q^{\mathsf T}p=0\) for the eight probabilities displayed above; their sum is one and every entry is positive. The chain is irreducible: one can clear all sites by successive gate openings with no intervening arrivals, and can construct any selected occupied sites from empty by delivering a fresh batch first to the rightmost target, then successively to targets farther left. Hence \(p\) is the unique stationary law.

**Exact stability criterion.** Write \(\Delta_{ij}=\partial_iF\,\partial_jF-F\partial_{ij}F\). For a multiaffine real polynomial, the Borcea–Brändén–Liggett criterion states that \(F\) is real stable exactly when \(\Delta_{ij}\ge0\) for every real value of its variables and every pair of indices. Since \(\Delta_{ij}\) is independent of \(z_i,z_j\), we obtain three quadratics in the remaining variable \(s\):
\[
\begin{aligned}
\Delta_{12}(s)&=\frac{r^2}{32(1+r)^6}\big[(3r^3+5r^2)s^2+(8r^3+20r^2+16r)s+5r^3+23r^2+32r+16\big],\\
\Delta_{13}(s)&=\frac{r^2}{16(1+r)^5}\big[r^2(s^2-s)+4(r+1)\big],\\
\Delta_{23}(s)&=\frac{r^2}{16(1+r)^5}\big[r^2(r+4)s^2+(r^2+12r)s+10\big].
\end{aligned}
\]
Each quadratic has strictly positive leading coefficient for \(r>0\). All three quadratic discriminants, including the displayed prefactors, are identical:
\[
\operatorname{disc}_s(\Delta_{ij})=\frac{r^6(r^2-16r-16)}{256(1+r)^{10}}.
\]
Consequently all three are everywhere nonnegative precisely when \(r^2-16r-16\le0\), or \(0<r\le8+4\sqrt5\). Equality is included because a quadratic with zero discriminant and positive leading coefficient is nonnegative at its repeated real root.

**Correlation reversal.** For the field-tilted law \(p_t\), direct differentiation of \(F(z_1,t,z_3)/F(1,t,1)\) gives
\[
\operatorname{Cov}_{p_t}(B_1,B_3)=-\frac{\Delta_{13}(t)}{F(1,t,1)^2},\qquad F(1,t,1)=\frac{r^2(t+1)+2r(t+1)+2}{2(1+r)^2}>0.
\]
Thus the covariance is positive precisely when \(r^2(t^2-t)+4(r+1)<0\). This quadratic has positive real roots exactly for \(r>8+4\sqrt5\), and the interval between the roots gives the stated formula. At \(t=1\), \(\Delta_{13}(1)>0\); likewise \(\Delta_{12}(1),\Delta_{23}(1)>0\), which proves all three unweighted pairwise covariances strictly negative for all \(r>0\). The non-stability of every longer stationary chain when \(r>r_*\) follows because its marginal on the first three sites is \(p\), and real stability is preserved by setting extra Boolean polynomial variables to \(1\).

## Verification
Run `python verify.py` (requires SymPy). It independently constructs the eight-state generator, checks exact normalization and stationarity, derives all three Rayleigh-difference discriminants, verifies the field witness at both low and high density, and computes stationary laws on four sites at two rational rates to test the first-three-site projection. All identities hold symbolically in the positive rate ratio; the finite additional projection checks supplement, rather than replace, the proof for arbitrary lengths.

## Relationship to prior work
Reuveni, Eliazar, and Yechiali (2011) introduced ASIP and an iterative steady-state probability-generating-function scheme, including explicit small-chain examples. Reuveni, Hirschberg, Eliazar, and Yechiali (2014) gave exact incremental-load probabilities for consecutive intervals, but did not formulate an external-field stability threshold. Lauber Bonomo and Reuveni (2019) gave stationary covariances of integer particle counts, rather than real stability of the Boolean occupancy polynomial. Borcea, Brändén, and Liggett (2009) established the general equivalence between real stability and the all-real Rayleigh inequalities used in the proof. Those general tools and the underlying stationary model are prior work; the sharp three-site threshold and the associated positive field-tilted correlation are the specific results proved here.

## Limitations
No statement is made that arbitrary chains with four or more sites are strongly Rayleigh at or below \(r_*\), nor that an unweighted Boolean pairwise covariance becomes positive. The external-field ensemble is not claimed to arise from altered gate rates. The earliest verified public date of the underlying ASIP source is 2011-10-03; an undated earlier preprint cannot be assigned a verified date from its filename alone. The original 2011 article's complete text was not accessible for a full section-by-section comparison; available publisher material and later primary articles were compared, and residual bibliographic risk remains. Independent mathematical validation has not been performed.

## References
1. S. Reuveni, I. Eliazar, U. Yechiali, "Asymmetric inclusion process," *Physical Review E* **84** (2011), 041101. DOI: 10.1103/PhysRevE.84.041101.
2. S. Reuveni, O. Hirschberg, I. Eliazar, U. Yechiali, "Occupation probabilities and fluctuations in the asymmetric simple inclusion process," *Physical Review E* **89** (2014), 042109. DOI: 10.1103/PhysRevE.89.042109. Author-hosted PDF: https://www.math.tau.ac.il/~uriy/Papers/OPASIP.pdf.
3. O. Lauber Bonomo, S. Reuveni, "Occupancy correlations in the asymmetric simple inclusion process," *Physical Review E* **100** (2019), 042109. arXiv:1905.02170; DOI: 10.1103/PhysRevE.100.042109.
4. J. Borcea, P. Brändén, T. M. Liggett, "Negative dependence and the geometry of polynomials," *Journal of the American Mathematical Society* **22** (2009), 521–567. arXiv:0707.2340; Theorem 4.1.
