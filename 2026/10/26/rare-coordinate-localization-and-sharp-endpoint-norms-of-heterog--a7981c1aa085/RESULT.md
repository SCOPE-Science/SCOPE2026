# Rare-coordinate localization and sharp endpoint norms of heterogeneous Bernoulli affine projections

## Finding
Let \(n\ge2\), let \(0<p_i<1\) for \(1\le i\le n\), and let \(\mu=\bigotimes_{i=1}^n\mathrm{Bernoulli}(p_i)\) on \(\{0,1\}^n\). Write \(P\) for the \(L^2(\mu)\)-orthogonal projection onto the \((n+1)\)-dimensional space spanned by the constant function and the coordinate functions. Define \(r_i=\min\{p_i,1-p_i\}\), and let \(B_i\) be independent Bernoulli random variables with success probabilities \(r_i\).

The two sharp endpoint norms have the **exact formula**
\[
\boxed{\|P\|_{L^1(\mu)\to L^1(\mu)}=\|P\|_{L^\infty(\mu)\to L^\infty(\mu)}=\mathbb E\left|\sum_{i=1}^n\frac{B_i}{r_i}-(n-1)\right|.}
\]
An evaluation vertex attaining the maximum is any vertex whose coordinate is the less probable value in each coordinate. A sign-valued input attains the sharp maximum-norm amplification. The displayed norm is nonincreasing in **each** \(r_i\) while the other \(r_j\)'s are held fixed. In particular, its unique global minimum over all positive parameter vectors is at \(p_1=\cdots=p_n=1/2\), whereas
\[
\sup_{0<p_1,\ldots,p_n<1}\|P\|=2n-1,
\]
with the supremum unattained.

For four coordinates a further exact formula displays genuine heterogeneity effects. With \(r_i\le1/2\), put \(R=\prod_i(1-r_i)\). Then
\[
\|P\|=1+6R+2\sum_{i=1}^4(3r_i-1)_+\prod_{j\ne i}(1-r_j).
\]
Three bias vectors with **identical average bias** \(1/4\) exhibit both directions of change under a mean-preserving spread:
\[
\begin{aligned}
 (p_1,p_2,p_3,p_4)=(1/6,1/6,1/3,1/3) &: \quad \|P\|=77/27,\\
 (p_1,p_2,p_3,p_4)=(1/4,1/4,1/4,1/4) &: \quad \|P\|=371/128,\\
 (p_1,p_2,p_3,p_4)=(1/8,1/8,3/8,3/8) &: \quad \|P\|=6213/2048.
\end{aligned}
\]
The homogeneous norm exceeds the first value by \(161/3456\), while the last exceeds the homogeneous value by \(277/2048\). Both unequal vectors majorize the constant bias vector but move the norm in opposite directions: this norm is **neither Schur-convex nor Schur-concave** in the bias vector on the fixed-mean slice. Hence neither homogeneous averaging nor a universal majorization heuristic controls the exact endpoint sensitivity.

## Assumptions and scope
All claims concern **real** functions on the finite probability space \(\{0,1\}^n\) with the strictly positive product measure \(\mu\). The coordinatewise probabilities are arbitrary and need not coincide. Operator norms use the same probability measure in both domain and range. The affine space consists of functions of the form \(x\mapsto a_0+\sum_i a_ix_i\), with no cross terms. The positive-part notation means \(t_+=\max\{t,0\}\). No claims are made about higher Walsh chaos, nonproduct laws, or optimality among projections other than this canonical orthogonal projector.

## Proof
**Reproducing kernel.** Since independent coordinates have zero covariance, the functions
\[
1,\qquad \phi_i(x)=\frac{x_i-p_i}{\sqrt{p_i(1-p_i)}}\quad(1\le i\le n)
\]
form an orthonormal basis of the affine subspace in \(L^2(\mu)\). Therefore
\[
(Pf)(x)=\sum_{y\in\{0,1\}^n}K(x,y)f(y)\mu(y),\qquad
K(x,y)=1+\sum_i\frac{(x_i-p_i)(y_i-p_i)}{p_i(1-p_i)}.
\]
In particular, \(K(x,y)=K(y,x)\) and \(\sum_yK(x,y)\mu(y)=1\).

**Kernel rows and localization.** Fix an evaluation vertex \(x\), and put \(s_i=p_i\) when \(x_i=1\), otherwise \(s_i=1-p_i\). For independent \(Y\sim\mu\), the random variable
\[
\frac{(x_i-p_i)(Y_i-p_i)}{p_i(1-p_i)}
\]
changes independently across \(i\), taking value \(1/s_i-1\) with probability \(s_i\) and value \(-1\) with probability \(1-s_i\). If \(C_i\sim\mathrm{Bernoulli}(s_i)\) independently, the absolute kernel row sum is exactly
\[
L(s_1,\ldots,s_n)=\mathbb E\left|\sum_i\frac{C_i}{s_i}-(n-1)\right|.
\]
For any real \(a\), define \(h_a(s)=(1-s)|a|+s|a+1/s|\). If \(a\ge0\), this equals \(a+1\), independently of \(s\). If \(a<0\), then
\[
h_a(s)=\begin{cases}1-a+2as,&0<s<-1/a,\\-a-1,&-1/a\le s\le1,\end{cases}
\]
where empty branches are ignored. Thus \(h_a\) is nonincreasing on \((0,1]\). Condition on all the other independent coordinates: the row expectation \(L\) is nonincreasing in each \(s_i\). For each input-coordinate bias \(p_i\), the smaller of its two possible \(s_i\) values is \(r_i\). Choosing the rare evaluation vertex gives the exact global row maximum \(L(r_1,\ldots,r_n)\), proving the boxed formula for the \(L^\infty\) norm. Choosing the sign of \(K(x,\cdot)\) at such a vertex achieves that norm. Symmetry of \(K\) makes its absolute row sums equal to the weighted absolute column sums that determine the \(L^1(\mu)\) operator norm; hence the endpoint constants coincide.

**The minimum is uniquely fair.** Coordinatewise nonincrease proves \(L(r_1,\ldots,r_n)\ge L(1/2,\ldots,1/2)\). To prove strictness whenever some \(r_i<1/2\), first set all other coordinates to \(1/2\). Their random contribution, after removing the chosen Bernoulli coordinate from the sum, has the form \(a=-(n-1)+2J\) with \(J\sim\mathrm{Bin}(n-1,1/2)\). If \(n=2m\), the event \(J=m-1\) has positive probability and gives \(a=-1\); on this event \(h_{-1}(s)=2-2s\) for \(s\le1/2\), strictly larger for \(s<1/2\) than at \(s=1/2\). If \(n=2m+1\), the event \(J=m-1\) gives \(a=-2\), for which \(h_{-2}(s)=3-4s\) on \(s<1/2\), strictly larger than \(h_{-2}(1/2)=1\). All other conditional contributions are nonincreasing, so the one-coordinate inequality is strict. Reducing the other \(r_j\)'s from \(1/2\) cannot reduce the norm. Thus any nonfair parameter vector has norm strictly greater than the fair value.

**Upper envelope and approach.** Write \(Z=\sum_i B_i/r_i-(n-1)\), so \(\mathbb EZ=1\) and \(Z\ge-(n-1)\). Consequently \(\mathbb E|Z|=1+2\mathbb E(-Z)_+\le2n-1\). For each strictly positive parameter vector the inequality is strict, since events with at least one \(B_i=1\) have positive probability and satisfy \((-Z)_+<n-1\). If all \(r_i\downarrow0\), the event of no successes has probability tending to one and on it \((-Z)_+=n-1\); bounded convergence of these negative parts proves \(\mathbb E|Z|\to2n-1\).

**Four-coordinate computation.** For \(n=4\), every success adds at least two to \(Z=-3+\sum_i B_i/r_i\). Hence a negative value is possible only when there are zero successes, contributing \(3\prod_i(1-r_i)\), or exactly one success at coordinate \(i\), contributing \((3r_i-1)_+\prod_{j\ne i}(1-r_j)\) to \(\mathbb E(-Z)_+\). The preceding identity \(\mathbb E|Z|=1+2\mathbb E(-Z)_+\) gives the displayed closed formula. Exact substitution gives all three rational values and the two signed gaps. Every displayed bias vector has arithmetic mean \(1/4\). The two nonconstant vectors are permutations of two repeated entries and each majorizes the constant vector; the opposite strict inequalities disprove both Schur-convexity and Schur-concavity on the fixed-sum feasible region.

## Verification
The standalone file `check.py` reconstructs the projector through an independently inverted \((n+1)\)-dimensional rational Gram matrix and computes complete kernel rows, rather than using the probabilistic formula to build the projector. It checks row/column endpoint duality, kernel idempotence in tested smaller dimensions, the stated rare-vertex optimizer, sign-valued extremizers, the three exact rational witnesses, and sampled coordinatewise monotonicity using rational arithmetic. Run `python check.py` in the directory containing this document and that file. Successful local execution produced `PASS {'assertions': 4863, 'matrix_instances': 38, 'bias_comparisons': 500}`. This finite verification is supplementary; the preceding arguments prove the claims for all positive biases and dimensions.

## Relationship to prior work
The standard orthogonal product Fourier basis and biased Boolean analysis are developed in O'Donnell's *Analysis of Boolean Functions* (first edition 2014), notably Sections 8.1 and 8.4. Section 10.4 establishes a bounded-norm statement for low-degree projections at fixed finite \(L^q\) exponents \(1<q<\infty\), but not the exact strong endpoint constant sought here. De Wolf's exposition treats Fourier expansions on the uniform cube, again not the heterogeneous endpoint norm. A previous homogeneous-Bernoulli sharp endpoint formula gives the special case \(p_1=\cdots=p_n\) (up to coordinate flips); no novelty is claimed for that special case. The present theorem concerns arbitrary unequal parameters, the rare-coordinate localization principle, componentwise bias-ordering, strict global minimization, and the two-sided fixed-mean heterogeneity/majorization obstruction.

## Limitations
The formula is a finite \(2^n\)-term expectation and is not claimed to admit a closed elementary expression in arbitrary dimension. Uniqueness is proved for the **minimizing bias vector**, not for all maximizing evaluation vertices. No finite-dimensional maximizing bias vector exists for the upper envelope. The originality assessment is conditional on inspected material and available earlier research records; an equivalent heterogeneous endpoint formula under alternative terminology may remain unlocated. No independent validation has been performed.

## References
1. Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), §§8.1, 8.4, 10.4, Exercise 8.24; publisher record `https://doi.org/10.1017/CBO9781139814782`; publicly accessible revised text `https://arxiv.org/pdf/2105.10386` (2021 revision of 2014 first edition).
2. Ronald de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube* (pre-2016 exposition), accessible primary PDF `https://homepages.cwi.nl/~rdewolf/publ/other/fourier.pdf`.
3. Prior mathematical record on homogeneous Bernoulli affine projections, opaque identifier `71f416ba-0fcb-4e2b-8a00-076074e837ee` (special case acknowledged, not a dependency of the proof).
