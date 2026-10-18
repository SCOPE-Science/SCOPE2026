# Exact cyclic-shift sign census in dimension \(35\) for odd-degree real fiducials

## Finding

Let \(K\subset\mathbb R\) be a number field with odd \([K:\mathbb Q]\). If a normalized real Weyl–Heisenberg fiducial \(v=(v_j)_{j\in\mathbb Z/35\mathbb Z}\in K^{35}\) exists, its \(17\) independent cyclic-shift signs must be one of exactly \(19\) configurations, split into three unit-multiplier orbits of sizes \(12\), \(3\), and \(4\). Every such fiducial necessarily satisfies \(\sum_jv_j=0\).

For a sign vector, put \(P=\{a\in\{1,\ldots,17\}:\sigma_a=+1\}\). Orbit representatives are

\[
\begin{aligned}
P_1&=\{1,3,4,7,10,11,14\} &&(12\text{ profiles}),\\
P_2&=\{1,5,6,7,8,13,14\} &&(3\text{ profiles}),\\
P_3&=\{1,5,10,11,14,15,16\} &&(4\text{ profiles}).
\end{aligned}
\]

The orbits use the action of \((\mathbb Z/35\mathbb Z)^\times\) on distances \(a\sim-a\pmod{35}\). All \(19\) profiles are **exactly** the ones passing the cyclic-shift positive-semidefiniteness test under the odd-degree sum restriction. Conversely, without requiring a number-field degree or any modulated overlap conditions, every surviving profile is the cyclic autocorrelation sign profile of at least one real unit vector. This is a classification of the **shift-only** subsystem, not a classification of full fiducials.

## Assumptions and scope

Here \(X\) denotes cyclic coordinate translation, \((Xv)_j=v_{j-1}\), with subscripts in \(\mathbb Z/35\mathbb Z\). A real Weyl–Heisenberg fiducial is a unit vector satisfying \(|\langle v,X^a Z^b v\rangle|^2=1/36\) whenever \((a,b)\ne(0,0)\). Its unmodulated shift correlations are real and obey

\[
\langle v,X^av\rangle=\sigma_a/6,\quad \sigma_a\in\{-1,1\},\quad \sigma_a=\sigma_{35-a},\quad 1\le a\le34.
\]

This result only imposes those correlations and the necessary positivity of their circulant Gram matrix, together with the field-degree restriction on \(\sum_jv_j\). It does **not** impose the remaining nonzero-modulation constraints. In particular, a compatible sign profile does not imply an odd-degree fiducial exists.

## Proof

Set \(S=\sum_{a=1}^{17}\sigma_a\) and \(T=\sum_{j=0}^{34}v_j\in K\). The shift correlations and unit normalization give

\[
T^2=\sum_{a=0}^{34}\langle v,X^av\rangle
=1+\frac{S}{3}=\frac{S+3}{3}.
\]

Since \(T^2\in\mathbb Q\) and \([K:\mathbb Q]\) is odd, \(T\in\mathbb Q\): otherwise \(\mathbb Q(T)\) would be a quadratic subfield of \(K\). A rational number whose square has denominator dividing \(3\) must be an integer here: write \(T=r/s\) in lowest terms; the displayed equality implies \(s^2\mid3\), hence \(s=1\). Thus \(S=3(T^2-1)\). There are \(17\) signs, so \(S\) is odd and \(|S|\le17\). The only possibilities are \((T,S)=(0,-3)\) and \((T,S)=(\pm2,9)\). Consequently \(|P|=(17+S)/2\) equals \(7\) or \(13\).

The Gram matrix of the \(35\) shifts of \(v\), indexed by \(j,k\in\mathbb Z/35\mathbb Z\), has entries \(G_{jj}=1\), \(G_{jk}=\sigma_{k-j}/6\) when \(j\ne k\). Fourier diagonalization yields

\[
\lambda_0=1+S/3,\qquad
3\lambda_k=3+\sum_{a=1}^{17}\sigma_a\cos(2\pi ka/35),\quad 1\le k\le17,
\]

with \(\lambda_{35-k}=\lambda_k\). Positivity of a real Gram matrix forces all these eigenvalues to be nonnegative. The complete exhaustive certificate in `verification/spectral_census.py` checks all \(\binom{17}{7}=19{,}448\) choices with \(S=-3\) and all \(\binom{17}{13}=2{,}380\) with \(S=9\), using rational arithmetic only for certified enclosures of every sampled cosine. It produces exactly \(19\) positive-semidefinite profiles in the first family and none in the second. For every survivor \(\lambda_0=0\), while every other eigenvalue is strictly positive (the certificate gives a common positive rational lower bound). Therefore the only possible value of \(T\) is \(0\). The same certificate verifies that the \(19\) surviving sets form exactly the three stated disjoint multiplier orbits.

For the converse concerning **only** the cyclic-shift subsystem, let \(G\) be the positive-semidefinite circulant matrix of any surviving profile. Write its Fourier eigenvalues as \(\lambda_k\ge0\), with \(\lambda_k=\lambda_{35-k}\). Choose Fourier coefficients \(\widehat v_k=\sqrt{\lambda_k}\), using the nonnegative square root. Fourier inversion produces a real vector \(v\), because its Fourier coefficients are real and reversal-symmetric. Its cyclic autocorrelation has Fourier coefficients \(|\widehat v_k|^2=\lambda_k\), so equals the first row of \(G\); in particular \(\|v\|_2=1\). This proves shift-only realizability and makes no claim about the coefficient field or modulated fiducial identities.

## Verification

From the package root, run `python3 verification/spectral_census.py` using Python 3's standard library. The program constructs a rational enclosure of \(\pi\) from Machin's arctangent identity, then rational interval bounds for \(\cos(2\pi t/35)\) for \(0\le t\le17\) by Taylor's theorem. It scales intervals by \(10^{15}\) and uses integer lower/upper bounds for the \(17\) nontrivial Fourier eigenvalues. A sign vector is rejected only when a certified eigenvalue upper bound is negative. Every surviving eigenvalue has a certified positive lower bound; ambiguity triggers an exception rather than a favorable classification. The computation also independently enumerates the unit-multiplier orbits. Its expected counts are \(19{,}448\to19\), \(2{,}380\to0\), and orbit sizes \(12,3,4\). The exact certified common lower bound on the nonzero eigenvalues of all survivors is \(135849403747801/3000000000000000>0\).

## Relationship to prior work

Van Loo and Oggier (arXiv:2610.13168v1, 2026) derive the fundamental shift-sign identity, establish odd-degree field restrictions, and rule out the special all-positive-overlap case. Their work supplies the structural setup and does not report the dimension-\(35\) complete positive-semidefinite sign census or its three orbits. Khatirinejad (2008) supplies general rational equations and specific real fiducial constructions in dimensions \(7\) and \(19\), rather than this composite-dimension sign census. Appleby and collaborators (2022) study Stark-unit constructions in dimensions of the form \(n^2+3\), especially prime dimensions, and do not classify the current finite sign system. General circulant spectral methods, including those considered by Song and Tranel (2022), underlie the Fourier diagonalization, but their specified design/concurrence classifications are different. The present result is not inferred from those papers merely by changing their parameters; it requires a complete certified enumeration of the new natural finite system.

## Limitations

This result does not establish existence or nonexistence of real Weyl–Heisenberg fiducials in dimension \(35\) over any number field. The \(19\) positive-semidefinite profiles may all fail the modulated overlap equations or the odd-degree coefficient-field condition. The converse produces real vectors only for the shift equations; it makes no assertion about the degree of their coordinate fields. The exact census is specialized to dimension \(35\), not an asymptotic theorem. Independent evaluation of the scientific claim has not been performed.

## References

1. I. Van Loo and F. Oggier, *Real Fiducial Vectors Only Exist in Dimensions \(d\equiv3\pmod4\)*, arXiv:2610.13168v1 (first posted 2026-10-09), https://arxiv.org/html/2610.13168v1.
2. M. Khatirinejad, *On Weyl-Heisenberg orbits of equiangular lines*, J. Algebraic Combin. 28 (2008), 333–349, doi:10.1007/s10801-007-0104-1.
3. M. Appleby et al., *SIC-POVMs from Stark units: Prime dimensions \(n^2+3\)*, J. Math. Phys. 63 (2022), 112205, doi:10.1063/5.0083520.
4. S.-Y. Song and T. Tranel, *Partial geometric designs having circulant concurrence matrices*, J. Combin. Des. 30 (2022), 420–460, doi:10.1002/jcd.21834.
