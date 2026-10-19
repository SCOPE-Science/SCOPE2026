# Pairwise-independent cat-map observations with exact Chebyshev prediction and cubic fluctuations

## Finding
Let \(A\in SL(2,\mathbb Z)\) have integer trace \(t\geq3\), let \(k\in\mathbb Z^2\setminus\{0\}\), and let \(X\) be Haar-uniform on \(\mathbb T^2\). Define, for every integer \(n\geq0\),
\[
Y_n=\cos(2\pi\langle k,A^nX\rangle),\qquad
Z_n(c)=Y_n+cP_t(Y_n),\qquad
S_N(c)=\sum_{n=0}^{N-1}Z_n(c),
\]
where \(c\in\mathbb R\) and \(P_t(\cos u)=\cos(tu)\) is the Chebyshev polynomial of degree \(t\).

The random variables \(Y_n\) (and likewise \(Z_n(c)\) for fixed \(c\)) are identically distributed and **pairwise independent**. Nonetheless, for almost all \((x,y)\in(-1,1)^2\), the conditional distribution of \(Y_{n+2}\) given \((Y_n,Y_{n+1})=(x,y)\) is the equal-weight two-point law
\[
\frac12\delta_{xP_t(y)+\sqrt{(1-x^2)(1-P_t(y)^2)}}+
\frac12\delta_{xP_t(y)-\sqrt{(1-x^2)(1-P_t(y)^2)}}.
\]
Consequently
\[
\mathbb E[Y_{n+2}\mid Y_n,Y_{n+1}]=Y_nP_t(Y_{n+1}),\qquad
\mathbb E[Y_nY_{n+2}P_t(Y_{n+1})]=\frac14.
\]
Thus the observations are not jointly independent in triples. For every \(N\geq1\) and \(c\in\mathbb R\), the centered sum has the **exact**, not merely asymptotic, moments
\[
\operatorname{Var}(S_N(c))=\frac{N(1+c^2)}2,\qquad
\kappa_3(S_N(c))=\mathbb E[S_N(c)^3]=\frac{3c}{2}\max\{N-2,0\}.
\]
For fixed \(c\ne0\), its standardized third moment is asymptotic to
\[
\frac{3\sqrt2\,c}{(1+c^2)^{3/2}\sqrt N}.
\]
The trace harmonic \(P_t\) is singled out by the minimal three-time recurrence; the result is uniform in the chosen nonzero integer sensor \(k\) and hyperbolic automorphism \(A\) with the same trace.

## Assumptions and scope
The measure is normalized Haar area on \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\), **not** counting measure on a finite rational grid. The matrix determinant is \(1\), its trace satisfies \(t\ge3\), and observations are at nonnegative integer times. These assumptions imply two distinct positive real eigenvalues \(\lambda>1\) and \(\lambda^{-1}<1\), with \(\lambda+\lambda^{-1}=t\). No primitivity condition is imposed on \(k\); the dependence on \(c\) is exact for all real coefficients. Conditional laws are assertions for Haar-almost-every observed pair, as usual for regular conditional distributions. The third cumulant refers to the unnormalized \(S_N(c)\).

## Proof
**(1) Two-time independent angles.** Write \(B=A^{\mathsf T}\), \(v_n=B^nk\), and \(U_n=\langle v_n,X\rangle\pmod1\). Every nonzero rational vector has nonzero components in both real eigendirections of \(B\): each eigendirection has irrational slope because the characteristic polynomial \(z^2-tz+1\) is irreducible over \(\mathbb Q\) for integer \(t\ge3\) (an integer square strictly between \((t-1)^2\) and \(t^2\) cannot equal \(t^2-4\)). If \(v_i,v_j\) were proportional for \(i<j\), the vector \(v_i\) would be an eigenvector of \(B^{j-i}\), contradicting its two nonzero eigencoordinates. The integer homomorphism \(X\mapsto(U_i,U_j)\) therefore has full rank. Its image is all of \(\mathbb T^2\), and its pushforward of Haar measure is product Haar measure. Hence every two distinct phases \(U_i,U_j\) are independent uniform variables, and so are any measurable functions \(Y_i,Y_j\) or \(Z_i(c),Z_j(c)\) of the respective phases.

**(2) Complete conditional law.** Cayley–Hamilton gives \(B^{n+2}=tB^{n+1}-B^n\), and therefore \(U_{n+2}=tU_{n+1}-U_n\pmod1\). Put \(\alpha=2\pi U_n\) and \(\beta=2\pi U_{n+1}\). By step (1), the angles are independent uniform modulo \(2\pi\). Conditional on their cosines \((\cos\alpha,\cos\beta)=(x,y)\), each angle has two equiprobable choices of sine sign, independently. Since
\[
\cos(t\beta-\alpha)=xP_t(y)+\sin(t\beta)\sin\alpha,
\]
and \(\lvert\sin(t\beta)\sin\alpha\rvert=\sqrt{(1-x^2)(1-P_t(y)^2)}\), the asserted two-point conditional law follows, including coincident-atom cases as a twofold mass at one value. Averaging the signs proves the predictor. Furthermore, the independent marginal arcsine laws give \(\mathbb E[Y_n^2]=\mathbb E[P_t(Y_{n+1})^2]=1/2\). The predictor then implies the mixed moment \(1/4\), whereas three independent centered variables would give zero.

**(3) Exhaustive cubic resonance lemma.** For three (possibly repeated) indices and multipliers \(m_j\in\{1,t\}\), consider an exact integer Fourier resonance
\[
\epsilon_1m_1B^{n_1}k+\epsilon_2m_2B^{n_2}k+\epsilon_3m_3B^{n_3}k=0,
\qquad\epsilon_j\in\{-1,1\}.
\]
We claim that the only solutions have three *distinct consecutive* indices \(r,r+1,r+2\), with multiplier \(t\) at \(r+1\), unit multipliers at the endpoints, and signs satisfying the Cayley–Hamilton relation (or its negative).

First, if all three multipliers are identical, cancel their common factor. Projecting the vector equation onto the expanding and contracting real eigenvectors yields simultaneously \(\sum_j\epsilon_j\lambda^{n_j}=0\) and \(\sum_j\epsilon_j\lambda^{-n_j}=0\). Because all powers are positive, this would require one power to equal the sum of the other two in *both* eigendirections. Their product gives \(1=2+\lambda^d+\lambda^{-d}\), where \(d\) is the difference between the two summed exponents; impossible. The argument allows repeated exponents.

Second, if exactly two multipliers are \(t\), divide the original relation by the content \(g=\gcd(k_1,k_2)\), making the integer vector \(k/g\) primitive. Reducing modulo \(t\), the remaining unit term forces \(B^n(k/g)\equiv0\pmod t\), impossible because \(B\) is invertible modulo \(t\) and a primitive vector cannot have both components divisible by \(t\).

Finally, suppose exactly one multiplier is \(t\), at index \(j\), with the unit multipliers at \(p,q\). Positivity of both eigenvalue powers rules out the opposite signs on the two unit terms: if they differ, their expanding and contracting differences have opposite signs, so they cannot both match one fixed signed \(t\)-term. Up to global sign, the relation is consequently \(B^pk+B^qk=tB^jk\). Taking expanding and contracting components gives
\[
\lambda^p+\lambda^q=t\lambda^j,\qquad
\lambda^{-p}+\lambda^{-q}=t\lambda^{-j}.
\]
Multiplication yields \(2+\lambda^{|p-q|}+\lambda^{-|p-q|}=t^2=2+\lambda^2+\lambda^{-2}\). Strict monotonicity of \(d\mapsto\lambda^d+\lambda^{-d}\) on nonnegative integers gives \(|p-q|=2\). Thus \(j\) is their midpoint, because \(\lambda^r+\lambda^{r+2}=t\lambda^{r+1}\). This proves the claimed exhaustive lemma, including exclusion of all coincident-time cubic resonances.

**(4) Exact moments.** Fourier orthogonality on \(\mathbb T^2\) says that the integral of a product of cosine characters vanishes unless its signed frequency sum is zero. Since \(t\ge3\), the single-time modes \(\cos(2\pi U_n)\) and \(\cos(2\pi tU_n)\) have zero means and are mutually orthogonal, with individual squared means \(1/2\). Pairwise independence gives \(\operatorname{Var}S_N=N(1+c^2)/2\). The resonance lemma rules out nonzero third moments at one time and at repeated or nonconsecutive times. For each triple \((r,r+1,r+2)\), only the two unit end harmonics and the middle trace harmonic resonate, giving
\[
\mathbb E[Z_r(c)Z_{r+1}(c)Z_{r+2}(c)]
=c\mathbb E[Y_rP_t(Y_{r+1})Y_{r+2}]=c/4.
\]
There are \(\max\{N-2,0\}\) consecutive unordered triples and six orderings in the cubic expansion. This yields exactly \(\mathbb E[S_N^3]=6(c/4)\max\{N-2,0\}\), as claimed. Dividing by the exact variance to the power \(3/2\) gives the standardized asymptotic.

## Verification
The accompanying standalone `verify.py` uses exact integer-frequency Fourier arithmetic and rational coefficients. For traces \(3,4,5,7\), sensors \((1,0),(1,1),(2,3)\), coefficients \(c\in\{-2,-1,0,1,2\}\), and lengths \(1\le N\le6\), it checks the exact mean, variance, third moment, and a three-time harmonic identity. Its output is `VERIFY_OK`. The unrestricted result rests on the eigenprojection and modular arguments in the proof; finite checks alone establish nothing beyond their sampled parameters. A second, independent manual derivation of the conditional law uses two independent uniform angles and four sign choices, not numerical integration.

## Relationship to prior work
Barash and Shchur, first publicly posted in 2004, develop cat-map recurrence and higher-order dependence for finite-lattice pseudorandom generators. Their explicit higher-block correlations anticipate the phenomenon that low-order decorrelation does not imply independence. However, their binary-partition results do not give the present Haar-arc-sine Chebyshev conditional distribution, an exhaustive three-frequency resonance classification, or the exact polynomial-observable cubic sum law. Ayyer–Liverani–Stenlund (2007) and Conze–Le Borgne–Roger (2010) develop central-limit and Fourier-decorrelation frameworks for toral automorphisms and their products. Such second-order or asymptotic statements do not specify the finite-time third cumulant or the exact conditional predictor above. Statement-level searches also compared public research records on toral three-delay reconstruction and cat-driven periodic resonances; those are topological/spectral questions on different systems or observables, not covering this theorem.

## Limitations
This does **not** claim that pairwise independence, the Cayley–Hamilton recurrence, or the general fact of cat-map higher-order dependence is new. It provides no fourth- or higher-cumulant classification, no Edgeworth expansion, and no assertion that nonconsecutive three-time observations are jointly independent. The exact two-atom predictor relies on a single cosine sensor and Haar sampling, while the cubic formula relies on its specially motivated trace harmonic. Earlier results expressed as high-order frequency-resonance identities might contain an equivalent specialization; independent scholarly validation has not been performed.

## References
1. L. Barash and L. N. Shchur, *Periodic orbits of the ensemble of Sinai-Arnold cat maps and pseudorandom number generation*, first posted 2004-09-14, arXiv:physics/0409069, https://arxiv.org/abs/physics/0409069 ; full text https://arxiv.org/html/physics/0409069v3 .
2. A. Ayyer, C. Liverani, and M. Stenlund, *Quenched CLT for random toral automorphism*, first posted 2007-11-24, arXiv:0711.3818, https://arxiv.org/html/0711.3818v1 .
3. J.-P. Conze, S. Le Borgne, and M. Roger, *Central limit theorem for products of toral automorphisms*, first posted 2010-06-21, arXiv:1006.4051, https://arxiv.org/html/1006.4051v1 .
