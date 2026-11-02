# The first two integer Fourier levels of the uniform Menger sponge measure

## Finding
Let \(\mu\) be the uniform twenty-map Menger sponge probability measure defined below. Its largest nontrivial integer Fourier coefficient magnitude is
\[
A=\frac15\prod_{j=2}^{\infty}\frac{1+4\cos(2\pi/3^j)}5
\approx 0.158631115297482,
\]
attained exactly at \(n=\pm 3^r e_i\) for \(r\in\mathbb Z_{\ge0}\) and \(i=1,2,3\). The second-largest *distinct* magnitude is
\[
B=\frac15\left|\frac{1+4\cos(8\pi/9)}5\right|
\prod_{j=3}^{\infty}\frac{1+4\cos(8\pi/3^j)}5
\approx0.0715848893600233,
\]
attained exactly at \(n=\pm4\cdot3^r e_i\). Every other nonzero frequency satisfies the strict, explicit separation
\[
|\widehat\mu(n)|<\frac7{100}<B<A.
\]
Consequently, convolution with \(\mu\) on mean-zero \(L^2(\mathbb T^3)\) has exact operator norm \(A\). On the closed invariant Fourier subspace additionally omitting every frequency \(\pm3^r e_i\), its exact norm is \(B\). These statements concern integer Fourier coefficients, not continuous frequencies in \(\mathbb R^3\).

## Assumptions and scope
Put \(\mathcal D=\{d\in\{0,1,2\}^3:\#\{i:d_i=1\}\le1\}\), which has exactly twenty members. Let \((D_j)_{j\ge1}\) be independent uniform \(\mathcal D\)-valued random variables, and let \(\mu\) be the distribution of \(X=\sum_{j\ge1}3^{-j}D_j\). This specifies the probability measure, including its uniform weights and ternary scaling, without presuming product structure. Define \(\widehat\mu(n)=\mathbb E\,e^{-2\pi i n\cdot X}\) for every \(n\in\mathbb Z^3\). The vectors \(e_i\) are the three standard coordinate vectors. Frequencies with a factor of three are compared after deleting all such common factors. No assertion is made for arbitrary weights or noninteger frequencies.

## Proof
**1. Exact digit mask and product.** Write \(c_i=\cos\theta_i\) and center the digit alphabet by subtracting \((1,1,1)\). The eight centered digits with no zero coordinate contribute \(8c_1c_2c_3\) to the characteristic sum; the twelve with exactly one zero contribute \(4(c_1c_2+c_1c_3+c_2c_3)\). The centered normalized mask is therefore
\[
m(\theta)=\frac{2c_1c_2c_3+c_1c_2+c_1c_3+c_2c_3}{5}.
\]
The uncentered mask differs by a unit-modulus phase. Independence and convergence of the infinite sum give
\[
|\widehat\mu(n)|=\prod_{j=1}^{\infty}\left|m(2\pi n/3^j)\right|,
\qquad |m(\theta)|\le1.
\]
If \(3\mid n_i\) for each coordinate, then \(\widehat\mu(3n)=\widehat\mu(n)\) in modulus; in fact the coefficient itself obeys this equality, since the first uncentered digit mask at integral angles is one. It suffices to consider primitive vectors with at least one coordinate nonzero modulo three.

**2. The first scale.** At \(j=1\), every cosine is \(1\) or \(-1/2\). Substituting into the preceding mask shows that the absolute mask values for exactly one, two, or three nonzero coordinates modulo three are respectively \(1/5\), \(1/20\), and \(1/10\). Two nonzero coordinates thus give a full Fourier magnitude at most \(1/20<7/100\). With all three coordinates nonzero, at \(j=2\) each cosine belongs to \([-1,4/5]\). The numerator is affine separately in each cosine, so its greatest absolute value on the cube occurs at a corner. Directly checking its eight corners gives \(|m|<3/5\), hence the product through depth two is strictly below \(3/50<7/100\).

**3. Reduction to axial residues at depth two.** Suppose exactly one coordinate is nonzero modulo three. If either of the other two is nonzero modulo nine, at least one transverse cosine at \(j=2\) equals \(-1/2\). The other transverse cosine is \(1\) or \(-1/2\), and for the active cosine \(x\in[-1,1]\),
\[
m(x,-1/2,1)=-(1+x)/10,\qquad
m(x,-1/2,-1/2)=(1-2x)/20.
\]
Thus the second mask magnitude is at most \(1/5\) and the product through this scale at most \(1/25<7/100\). The only possible survivors are axial modulo nine. Their active residues are \(\pm1\), \(\pm2\), or \(\pm4\); for such axial vectors the second mask equals \((1+4\cos(2\pi r/9))/5\). The elementary certified bounds
\[
\begin{gathered}
3/4<\cos(2\pi/9)<4/5,\\
0<\cos(4\pi/9)<3/16,\\
-19/20<\cos(8\pi/9)<-15/16
\end{gathered}
\]
show that the residue \(\pm2\) gives a prefix strictly below \((1/5)(7/20)=7/100\). Only axial \(\pm1\) and \(\pm4\) modulo nine survive, with depth-two prefixes bounded above by \((1/5)(21/25)\) and \((1/5)(14/25)\), respectively.

**4. Depth-three exhaustion.** If a transverse coordinate becomes nonzero at depth three, the mixed-mask identities above bound the third factor by \(1/5\), so its prefix is below \(1/25\). The axial centered residues modulo \(27\) extending the previous four residues are, up to sign, \(1,4,5,8,10,13\). The new residues \(5,8,10,13\) have their third cosine and mask bounded as follows:
\[
\begin{array}{c|c|c|c}
|r|&\text{bound on }\cos(2\pi r/27)&\text{bound on }|m_3|&\text{bound on depth-three prefix}\\\hline
5&0<\cos(10\pi/27)<2/5&13/25&(1/5)(14/25)(13/25)\\
8&-1/2<\cos(16\pi/27)<0&1/5&(1/5)(21/25)(1/5)\\
10&-3/4<\cos(20\pi/27)<-1/2&2/5&(1/5)(21/25)(2/5)\\
13&-1<\cos(26\pi/27)<0&3/5&(1/5)(14/25)(3/5)
\end{array}
\]
Each displayed final bound is strictly below \(7/100\). Therefore any Fourier magnitude at least \(7/100\) must have residue modulo \(27\) equal to one of \(\pm e_i\) or \(\pm4e_i\).

**5. No later branching.** For \(j\ge3\), suppose a primitive frequency has survived along an axial residue \(\pm a e_i\pmod{3^j}\), for one fixed sign and \(a\in\{1,4\}\). If a transverse coordinate first becomes nonzero modulo \(3^{j+1}\), the next mask is at most \(1/5\), making the total prefix at most \(1/25\). If all transverse coordinates stay zero but the active residue changes by a nonzero multiple of \(3^j\), the next active angle is within \(2\pi a/3^{j+1}\) of \(\pm2\pi/3\) modulo \(2\pi\). The cosine Lipschitz estimate implies
\[
|m_{j+1}|\le\frac{1+8\pi a/3^{j+1}}5.
\]
Because all earlier factors are at most one, the product through depth \(j\) is bounded by the appropriate depth-two upper bound. For every \(j\ge3\), using \(\pi<22/7\),
\[
\frac15\frac{21}{25}\frac{1+8(22/7)/81}5<\frac7{100},
\qquad
\frac15\frac{14}{25}\frac{1+32(22/7)/81}5<\frac7{100}.
\]
So no new branch can retain magnitude at least \(7/100\). A fixed integer frequency congruent to exactly one of these six axial residues at every depth must equal that vector. Restoring the deleted common power of three, every frequency of magnitude at least \(7/100\) belongs to one of the claimed two families.

**6. Both families exceed the cutoff, and are ordered.** For \(\pm e_i\) the first factor equals \(1/5\) and every later factor is positive, producing \(A\). For \(\pm4e_i\) the second factor is negative and all factors at depth three and higher are positive, giving \(B\). The certified inequalities \(\cos(8\pi/9)<-15/16\) and \(\cos(8\pi/27)>19/32\) imply that the magnitude of the second factor in \(B\) exceeds \(11/20\), and the third factor exceeds \(27/40\). At every later depth \(j\ge4\), the factor is positive and
\[
1-\frac{1+4\cos(8\pi/3^j)}5
=\frac45\bigl(1-\cos(8\pi/3^j)\bigr)
\le\frac25(8\pi/3^j)^2.
\]
The inequality \(\prod(1-u_j)\ge1-\sum u_j\) for \(0\le u_j\le1\), together with \(\pi^2<10\), gives the strict lower bound
\[
B>\frac15\frac{11}{20}\frac{27}{40}
\left(1-\frac{160}{3645}\right)
=\frac{7667}{108000}>\frac7{100}.
\]
Finally, the second factor for \(e_i\) exceeds \(4/5\), while the absolute second factor for \(4e_i\) is below \(14/25\). At every depth \(j\ge3\), the cosine at \(2\pi/3^j\) strictly exceeds that at \(8\pi/3^j\); both factors are positive. Thus \(A>B\). The first and second levels and all equality cases follow.

**7. Torus operator consequence.** Convolution by the periodic pushforward of \(\mu\) is the Fourier multiplier \(f\mapsto\widehat\mu(n)\widehat f(n)\). Plancherel yields norm equal to the supremum of the multiplier magnitudes over each indicated closed Fourier-invariant subspace, and the two extremizing families attain those suprema.

## Verification
The standalone `check_menger.py` reproduces the exact 20-digit mask, first-scale residue cases, eight-vertex multiaffine inequality, nine certified rational cosine enclosures, positive tail and lift inequalities. It uses rational arithmetic, alternating-arctangent enclosures of \(\pi\), and Taylor remainder estimates, and also tests 15,624 nonzero frequencies in the box of radius twelve. Running `python3 check_menger.py` reports `MENGER_SPECTRAL_TWO_LEVEL_CERTIFICATE_OK 9 rational cosine enclosures, 15624 finite tests`. The proof's all-depth branch argument is the infinite certificate; numerical enumeration is only supplementary.

## Relationship to prior work
Jorgensen and Pedersen (2006) develop Fourier analysis of affine self-similar measures and the associated orthogonal-harmonic framework. Berner, Herr, Jorgensen, and Weber (2024), Example 3.14, specify exactly the uniform twenty-map Menger sponge measure and establish its slice-singularity as an example in their theory of nonorthogonal \(L^2(\mu)\) Fourier expansions. Their expansion/frame theorem and slice-singularity result concern different invariants from the two pointwise integer Fourier magnitude extrema and their complete extremizer sets here. Previous work on other self-similar digit sets does not imply these mask-specific three-dimensional inequalities.

## Limitations
The scope is the standard uniform twenty-digit construction and the integer lattice. This does not give the third largest coefficient magnitude, claims for weighted sponges, Fourier decay away from integer frequencies, or uniqueness in the entire literature. The literature comparison is bounded and independent mathematical review has not been performed. The comparison to the high-relevance 2024 source is based on its accessible full preprint, including the main theorem and the entire Menger sponge example.

## References
- P. E. T. Jorgensen and S. Pedersen, *Harmonic Analysis of Fractal Measures*, arXiv:math/0604087, first public 2006-04-04, https://arxiv.org/pdf/math/0604087.
- C. Berner, J. E. Herr, P. E. T. Jorgensen and E. S. Weber, *Fourier series for singular measures in higher dimensions*, arXiv:2402.15950, first public 2024-02-25, especially Theorem A, Section 3.4 and Example 3.14, https://arxiv.org/pdf/2402.15950.
