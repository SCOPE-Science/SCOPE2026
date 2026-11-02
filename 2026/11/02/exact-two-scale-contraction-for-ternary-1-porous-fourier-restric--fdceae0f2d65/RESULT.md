# Exact two-scale contraction for ternary \(1\)-porous Fourier restrictions

## Finding
Let \(G_n=\mathbb Z/3^n\mathbb Z\), and let \(\mathcal F_n\) be the unitary discrete Fourier transform with kernel \(3^{-n/2}\exp(-2\pi ixy/3^n)\). Call \(E\subset G_n\) *one-step porous* when, for every \(0\le j<n\), each residue class modulo \(3^j\) has a child residue class modulo \(3^{j+1}\) disjoint from \(E\). Put
\[
R_n=\max_{X,Y\subset G_n\text{ one-step porous}}\|\mathbf1_Y\mathcal F_n\mathbf1_X\|_{\ell^2\to\ell^2}.
\]
Define \(\vartheta=2\cos(2\pi/9)\) and
\[
P(T)=T^4-16T^3+(80-\vartheta)T^2-144T+81.
\]
The polynomial \(P\) has exactly one zero \(T_*\) in \((8,9)\), and
\[
\boxed{R_1=1,\qquad R_2=\sqrt{T_*/9}=0.99241835661824\ldots<1.}
\]
Every maximizing pair whose two sets have maximum permissible cardinality four is equivalent under Fourier-preserving affine symmetries to \(X=Y=\{0,1,3,4\}\); exactly \(243\) ordered pairs of cardinality-four supports attain \(R_2\).

By the submultiplicativity theorem for arbitrary porous Fourier restrictions from Badalucco--Franchi, all \(n\ge1\) satisfy
\[
R_n\le R_2^{\lfloor n/2\rfloor}\le R_2^{-1/2}\,3^{-\beta n},\qquad
\beta=-\frac{\log R_2}{2\log3}=0.00346370153380\ldots.
\]
In particular the *first* strictly contracting block has length two. The rate above is an explicit admissible rate, **not** asserted to be the optimal asymptotic exponent.

## Assumptions and scope
The theorem concerns every pair of one-step porous supports in the cyclic groups \(\mathbb Z/3^n\mathbb Z\), not merely self-similar ternary digit sets. It uses the unitary Fourier normalization stated above. The maximizing-pair count concerns pairs with both supports of cardinality four; no complete classification of maximizers with smaller supports is asserted. The final all-scale bound invokes Lemma 3.1 of Badalucco--Franchi (arXiv:2607.11534), while the exact two-scale computation and orbit classification are proved here.

## Proof
**1. Porosity and maximal completion.** In \(G_2\), the root has three residue classes modulo three. At most two may be occupied; each occupied class contains at most two of its three points. Hence every one-step porous set has size at most four, and every such set extends to a size-four porous set. Such maximal sets are specified by one omitted residue modulo three and then one omitted point in each of the two surviving classes. There are exactly \(3\cdot3^2=27\) of them. Enlarging either support cannot decrease an operator norm, so maximizing \(R_2\) reduces to these \(27^2\) pairs.

**2. Affine symmetries and three classes.** Let \(X_0=\{0,1,3,4\}\). The affine transformations \(x\mapsto ux+a\), where \(u\in(\mathbb Z/9\mathbb Z)^\times\) and \(a\in G_2\), preserve porosity and preserve the restricted Fourier norm after a compensating multiplication of the frequency support by \(u\). The affine orbit of \(X_0\) contains all \(27\) maximal supports: the group has order \(54\), and the stabilizer is exactly \(\{(1,0),(8,4)\}\). We may therefore hold the spatial support at \(X_0\).

Translating a frequency support multiplies Fourier columns by unit phases and leaves the norm invariant. The \(27\) maximal frequency supports split into exactly three translation orbits, each of size nine (a set of cardinality four has no nonzero translation period modulo nine). Representatives are
\[
Y_1=\{0,1,3,4\},\quad Y_2=\{0,1,3,7\},\quad Y_4=\{0,1,4,6\}.
\]

**3. Exact characteristic polynomials.** Write \(\zeta=\exp(2\pi i/9)\) and let \(A_j=(\zeta^{-xy})_{y\in Y_j,x\in X_0}\), so the restricted unitary Fourier matrix is \(A_j/3\). Set \(B_j=A_j^*A_j\). Direct multiplication in the cyclotomic ring \(\mathbb Z[\zeta]\), using \(\zeta^6+\zeta^3+1=0\), yields for \(j\in\{1,2,4\}\)
\[
\det(TI-B_j)=P_j(T):=T^4-16T^3+
\bigl(80-2\cos(2\pi j/9)\bigr)T^2-144T+81.
\]
This finite identity may be reproduced using the bundled integer-arithmetic program `CHECK.py`: construct the displayed four-by-four matrices, multiply and trace them in the rank-six cyclotomic quotient, and apply Newton's identities. All characteristic coefficients are checked exactly; no floating-point identity is assumed.

**4. Strict comparison of the spectral maxima.** Write \(\vartheta_j=2\cos(2\pi j/9)\), \(c_j=80-\vartheta_j\). Since \(|\vartheta_j|<2\), for every \(T\ge8\)
\[
P_j''(T)=12T(T-8)+2c_j>0,\qquad
P_j'(8)=112-16\vartheta_j>80.
\]
Thus each \(P_j\) is strictly increasing on \([8,\infty)\). Moreover
\[
P_j(8)=-47-64\vartheta_j,\qquad P_j(9)=81(2-\vartheta_j)>0.
\]
The first two angles \(2\pi/9\) and \(4\pi/9\) have positive cosine, so \(P_1(8),P_2(8)<0\); whereas \(\vartheta_4<-1\) gives \(P_4(8)>0\). Each \(B_j\) is positive semidefinite, and the unitary Fourier normalization forces all eigenvalues of \(B_j\) into \([0,9]\). Therefore \(B_1,B_2\) each have precisely one eigenvalue in \((8,9)\), namely their largest, and \(B_4\) has no eigenvalue in that interval. Finally \(\vartheta_1>\vartheta_2\), so \(P_1(T)<P_2(T)\) for \(T>0\). Evaluating at the unique root of \(P_2\) in \((8,9)\), strict monotonicity forces the root of \(P_1\) to be strictly larger. Hence the unique best frequency translation orbit is the one represented by \(Y_1=X_0\), proving the exact value \(R_2=\sqrt{T_*/9}\).

For each of the \(27\) maximal spatial sets exactly the corresponding nine-element orbit of maximal frequency sets attains this value, giving \(27\cdot9=243\) ordered cardinality-four optimizers.

**5. Minimal scale and all-scale consequence.** Every one-step porous support in \(G_1\cong\mathbb Z/3\mathbb Z\) has size at most two. Taking any two-element spatial and frequency supports, the corresponding two-dimensional subspaces of \(\mathbb C^3\) intersect nontrivially after Fourier transformation, by the dimension inequality \(2+2>3\). Hence \(R_1=1\). Lemma 3.1 of Badalucco--Franchi proves \(R_{m+k}\le R_mR_k\) for these (indeed all \(L\)-porous) sets. Applying it to \(\lfloor n/2\rfloor\) blocks of length two and possibly one terminal block gives \(R_n\le R_2^{\lfloor n/2\rfloor}\), and elementary rearrangement gives the stated explicit exponent and constant.

## Verification
Run `python CHECK.py` from a directory containing only the extracted program (Python standard library suffices). It checks the three four-by-four characteristic-polynomial identities over the integer cyclotomic quotient, the list of all \(27\) maximal supports, affine transitivity, the three translation orbits and their cardinalities. These are exact computations, not floating-point regressions. The proof separately establishes real-root location and ordering for all three spectral classes and uses the published submultiplicativity lemma for the infinite collection of scales. The decimal estimates are informational only.

## Relationship to prior work
Badalucco and Franchi, *Fractal uncertainty principle over \(\mathbb Q_p\)* (arXiv:2607.11534, first posted 2026-07-13), prove a general qualitative positive-exponent result for arbitrary porous sets and their Lemma 3.1 supplies the submultiplicativity used here. Their strict-contraction proof selects a block satisfying \((3-1)^q<3^{q-1}\), yielding block length four in the \(p=3,L=1\) case, and it gives no exact two-scale restricted norm. The present theorem replaces that step with the sharp first contracting scale and exact contraction factor, without changing their general theorem. Dyatlov and Jin (arXiv:1608.02238) study self-similar Cantor alphabets and do not cover all varying one-step porous subsets of \(\mathbb Z/9\mathbb Z\). Osgood, Siripuram and Wu (arXiv:1204.0992) establish universal-sampling invertibility, not the sharp singular-value optimization performed here. None of the inspected results implies the displayed cyclotomic quartic optimization.

## Limitations
Only the exact \(p=3,L=1,n=2\) block optimum and its submultiplicative consequence are settled. The displayed all-scale decay exponent is an effective admissible exponent, not proved sharp. No classification of all optimizers with smaller cardinality is claimed, nor any corresponding sharp computation for other primes or porosity lengths. Full historical coverage cannot be guaranteed from accessible material; independent mathematical audit has not been performed.

## References
1. V. Badalucco and L. Franchi, *Fractal uncertainty principle over \(\mathbb Q_p\)*, arXiv:2607.11534, first public 2026-07-13. https://arxiv.org/abs/2607.11534 .
2. S. Dyatlov and L. Jin, *Resonances for open quantum maps and a fractal uncertainty principle*, arXiv:1608.02238 (2016). https://arxiv.org/abs/1608.02238 .
3. B. Osgood, A. Siripuram and W. Wu, *Discrete sampling and interpolation: universal sampling sets for discrete bandlimited spaces*, arXiv:1204.0992 (2012). https://arxiv.org/abs/1204.0992 .
