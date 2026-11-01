# Exact first-band Fourier sampling spectra on surjective words

## Finding
For integers \(q\ge2\) and \(n\ge q\), let \(\Omega_{n,q}\) be the set of onto words of length \(n\) over the additive cyclic alphabet \(\mathbb Z/q\mathbb Z\). Equip this nonempty finite set with uniform probability. The restrictions of the constant character and all \(n(q-1)\) nonconstant one-coordinate characters have a completely explicit probability-normalized Gram spectrum. Define \(S(n,q)\) as a Stirling number of the second kind and
\[
\theta_{n,q}=\frac{S(n-1,q-1)}{(q-1)S(n,q)}.
\]
The spectrum, listing multiplicities, is \(1\) (once), \(1+\theta_{n,q}\) (\((n-1)(q-1)\) times), and \(1-(n-1)\theta_{n,q}\) (\(q-1\) times). Hence the first Fourier band is linearly independent on onto words if and only if \(n>q\). At \(n=q\), precisely \(q-1\) independent dependencies remain. For \(n>q\), the exact squared condition number is
\[
\kappa_{n,q}^{2}=\frac{1+\theta_{n,q}}{1-(n-1)\theta_{n,q}}.
\]
At the minimal injective word length \(n=q+1\), this becomes exactly \(q+2\). For each fixed \(q\), as \(n\to\infty\),
\[
\theta_{n,q}\sim \frac{q}{(q-1)^2}\left(\frac{q-1}{q}\right)^n,\qquad
\kappa_{n,q}^2=1+\frac{nq}{(q-1)^2}\left(\frac{q-1}{q}\right)^n(1+o(1)).
\]

## Assumptions and scope
Here \(q\) is any integer at least two, not necessarily a prime power; characters are those of the cyclic alphabet. A word is onto when each of the \(q\) symbols occurs at least once. The cardinality is \(q!S(n,q)\). Put \(\zeta=\exp(2\pi i/q)\); the sampled functions are \(1\) and \(f_{i,k}(x)=\zeta^{kx_i}\) for \(1\le i\le n\) and \(1\le k\le q-1\). Inner products average \(f\overline g\) over \(\Omega_{n,q}\). All eigenvalues are those of this actual Gram matrix, not of a rescaled covariance matrix. Singular-value condition number means the ratio of the largest to smallest singular values of the restriction map with uniform sampling measure.

## Proof
Permuting the colors and positions preserves the onto-word law. In particular, each coordinate is uniform on the \(q\) colors; therefore the constant character is orthogonal to all \(f_{i,k}\) and different nonzero frequencies in the same coordinate are orthogonal. For \(i\ne j\), the probability that positions \(i,j\) have the same color equals \(S(n-1,q)/S(n,q)\): identify the two positions to get an onto word of length \(n-1\). Conditional on equality or inequality, color exchangeability gives the respective uniform distributions on equal and unequal ordered color pairs. The sum of a nontrivial character over all ordered unequal color pairs is \(-q\) for equal frequency indices and zero for unequal indices. Thus
\[
\mathbb E[f_{i,k}\overline{f_{j,\ell}}]=
\begin{cases}
1,&i=j,\ k=\ell,\\
-\theta_{n,q},&i\ne j,\ k=\ell,\\
0,&k\ne\ell.
\end{cases}
\]
The Stirling recurrence \(S(n,q)=qS(n-1,q)+S(n-1,q-1)\) yields the displayed coefficient \(\theta_{n,q}\). Consequently, for each \(k\) the \(n\)-by-\(n\) Gram block is \((1+\theta_{n,q})I_n-\theta_{n,q}J_n\). Its eigenvalues are \(1+\theta_{n,q}\) on the zero-sum coordinate subspace and \(1-(n-1)\theta_{n,q}\) on the constant-coordinate vector, with dimensions \(n-1\) and one. This proves the entire spectrum.

If \(n=q\), each color is used once, so the sum of every nontrivial color character over coordinates is zero, giving \(q-1\) independent kernel vectors and the formula has \(\theta_{q,q}=1/(q-1)\). If \(n>q\), compare two onto words formed by using one occurrence of every color and putting all remaining \(n-q\) occurrences into color zero or into color one: for any \(1\le k<q\), the sums of the \(k\)-th color character differ by \((n-q)(1-\zeta^k)\ne0\). Hence each constant-coordinate block has strictly positive variance, establishing positive definiteness of the Gram matrix. The largest and smallest eigenvalues are then \(1+\theta_{n,q}\) and \(1-(n-1)\theta_{n,q}\).

For \(n=q+1\), the Stirling identities \(S(q,q)=1\) and \(S(q+1,q)=\binom{q+1}{2}\) give \(\theta_{q+1,q}=1/(q+1)\), hence \(\kappa_{q+1,q}^{2}=q+2\). At fixed \(q\), inclusion-exclusion gives \(S(n,q)=q^n/q!(1+O_q(((q-1)/q)^n))\) and the corresponding \((q-1)\)-color estimate. Substitution gives the displayed \(\theta\)-asymptotic and condition-number asymptotic.

## Verification
The accompanying standard-library Python file `surjection_checker.py` enumerates all onto words for \(2\le q\le4\) and \(q\le n\le q+3\), compares exact character correlations via rational equal/different-color probabilities, and checks each predicted eigenvalue. It reported 3006 exact moment comparisons passed. These finite computations are tests of the infinite-parameter algebraic proof, not substitutes for it.

## Relationship to prior work
Stirling-number partition enumeration is classical. Bóna and Mező (arXiv:0705.2734, dated 2007-05-18) study partition restrictions and associated Stirling enumerations, but not the present character sampling spectra. Kuperberg, Lovett and Peled (arXiv:1302.4295) study regular combinatorial structures and orthogonality phenomena, without establishing this all-surjective-word first-band Gram law. Carayol and Rotondo (arXiv:2605.24068) study sampling uniformly from onto functions; that subsequent paper supplies context on naturalness of the sampling domain but does not directly state these Fourier Gram eigenvalues. The exact probability-normalized spectral statement, linear independence boundary, and sharp condition number are the claim here, not the Stirling recurrence itself.

## Limitations
This is a degree-one statement only; higher-degree character families are not analyzed. No universal monotonicity in \(n\) or \(q\), beyond formulas displayed, is claimed. The novelty comparison is bounded, and an older equivalent result in exchangeable occupancy or categorical covariance literature is possible; this research does not establish historical uniqueness. There has been no independent mathematical validation.

## References
- M. Bóna and I. Mező, *Real Zeros and Partitions without singleton blocks*, arXiv:0705.2734, first public version 2007-05-18, https://arxiv.org/abs/0705.2734 .
- G. Kuperberg, S. Lovett, R. Peled, *Probabilistic existence of regular combinatorial structures*, arXiv:1302.4295, https://arxiv.org/abs/1302.4295 .
- A. Carayol and P. Rotondo, *Efficient Uniform Sampling of Surjections via their Profiles*, arXiv:2605.24068, https://arxiv.org/abs/2605.24068 (later supporting background, not used for archive-date assignment).
