# Phase-only four-sparse uncertainty over prime cyclic groups
## Finding
Let \(p\ge 5\) be prime and let \(A\subset\mathbb Z_p\) have exactly four elements. For \(f:\mathbb Z_p\to\mathbb C\), use the Fourier transform
\[
\widehat f(k)=\sum_{x\in\mathbb Z_p}f(x)e^{-2\pi i kx/p}.
\]
Assume \(\operatorname{supp}f=A\) and all four nonzero values of \(f\) have one common magnitude. Call \(A\) centrally symmetric if there is \(m\in\mathbb Z_p\) with \(A=2m-A\), equivalently if its elements can be labeled \(x_1,x_2,x_3,x_4\) so that
\[
x_1+x_4=x_2+x_3.
\]
Then the attainable numbers of Fourier zeros are exactly
\[
\#\{k:\widehat f(k)=0\}\in
\begin{cases}
\{0,1,2\},&A\text{ centrally symmetric},\\
\{0,1\},&A\text{ not centrally symmetric}.
\end{cases}
\]
In particular, an equal-magnitude four-sparse signal on a prime cyclic group never has three Fourier zeros, although the unrestricted prime-cyclic uncertainty theorem allows a four-sparse signal to have three zeros.

## Assumptions and scope
The modulus is a prime \(p\ge5\). The support \(A\) is fixed and has four distinct elements. Only the four nonzero coefficient magnitudes are constrained to be equal; their phases are arbitrary. Multiplying all coefficients by one nonzero scalar does not affect the Fourier zero set, so the proof normalizes all four coefficient moduli to one.

The statement is specific to prime cyclic groups. For composite moduli, a fixed antipodal pairing can recur at several frequencies because a nonzero support difference need not be invertible, so the prime argument does not extend verbatim.

## Proof
Write \(\rho=e^{-2\pi i/p}\), label the support \(A=\{x_1,x_2,x_3,x_4\}\), and normalize the nonzero coefficients to \(|c_j|=1\). At a Fourier zero \(k\), the four unit complex numbers
\[
z_j=c_j\rho^{kx_j}
\]
satisfy \(z_1+z_2+z_3+z_4=0\).

First use the following elementary rigidity lemma. If four unit complex numbers sum to zero, then they split into two antipodal pairs. Indeed, let
\[
Q(t)=\prod_{j=1}^4(t-z_j)=t^4-e_1t^3+e_2t^2-e_3t+e_4.
\]
Here \(e_1=z_1+z_2+z_3+z_4=0\). Since \(|z_j|=1\),
\[
e_3=(z_1z_2z_3z_4)\,\overline{e_1}=0.
\]
Thus \(Q(t)=t^4+e_2t^2+e_4\) is even, so its roots occur in opposite pairs. Hence every Fourier zero determines at least one perfect matching of the four support indices whose two matched Fourier summands are negatives of one another.

A fixed matching cannot occur at two distinct frequencies. For example, if the pair \(\{i,j\}\) is antipodal at both \(k\) and \(\ell\), then
\[
\rho^{(k-\ell)(x_i-x_j)}=1.
\]
Because \(p\) is prime, \(x_i\ne x_j\), and \(k\ne\ell\), this is impossible. There are only three perfect matchings, so there are at most three Fourier zeros.

Three distinct zeros are impossible. If they existed, their matchings would have to be the three different ones. Relabel so that at frequencies \(k,\ell,m\) the matchings are respectively
\[
(12)(34),\qquad(13)(24),\qquad(14)(23).
\]
From the pairs involving index \(1\),
\[
\frac{c_2}{c_1}=-\rho^{k(x_1-x_2)},\qquad
\frac{c_3}{c_1}=-\rho^{\ell(x_1-x_3)},\qquad
\frac{c_4}{c_1}=-\rho^{m(x_1-x_4)}.
\]
Therefore \(c_3/c_4\) is a \(p\)-th root of unity. But the second pair in the matching \((12)(34)\) also gives
\[
\frac{c_3}{c_4}=-\rho^{k(x_4-x_3)},
\]
which is the negative of a \(p\)-th root of unity. This would make \(-1\) a \(p\)-th root of unity, impossible for odd \(p\). Thus every such signal has at most two Fourier zeros.

Now suppose two distinct zeros occur. Their matchings are distinct, so relabel them as \((12)(34)\) at \(k\) and \((13)(24)\) at \(\ell\). The four antipodal relations give two expressions for \(c_4/c_1\):
\[
\frac{c_4}{c_1}=\rho^{k(x_1-x_2)+\ell(x_2-x_4)}
=\rho^{\ell(x_1-x_3)+k(x_3-x_4)}.
\]
Hence
\[
(k-\ell)(x_1+x_4-x_2-x_3)=0\pmod p.
\]
Since \(k\ne\ell\), the support must satisfy \(x_1+x_4=x_2+x_3\), which is exactly central symmetry.

Conversely, suppose \(x_1+x_4=x_2+x_3\). Set
\[
c_1=1,\qquad c_2=-1,\qquad c_3=-\rho^{x_1-x_3},\qquad c_4=\rho^{x_1-x_3}.
\]
Then \(\widehat f(0)=0\) by the matching \((12)(34)\), while \(\widehat f(1)=0\) by the matching \((13)(24)\). The already proved upper bound shows that this signal has exactly two Fourier zeros.

It remains to realize zero and one zero for every support. Taking all four coefficients equal to \(1\) gives no Fourier zero: a zero at a nonzero frequency would be a vanishing sum of four \(p\)-th roots of unity, and the antipodal-pair lemma would force \(-1\) to be a \(p\)-th root of unity; at frequency \(0\) the sum is \(4\). For exactly one zero, choose
\[
(c_1,c_2,c_3,c_4)=(1,-1,u,-u),\qquad |u|=1.
\]
Then \(\widehat f(0)=0\). For each fixed nonzero \(k\), the equation \(\widehat f(k)=0\) determines at most one value of \(u\), because both differences \(\rho^{kx_1}-\rho^{kx_2}\) and \(\rho^{kx_3}-\rho^{kx_4}\) are nonzero. Avoiding the finitely many forbidden phases leaves a unimodular \(u\) for which \(0\) is the unique Fourier zero. This proves the complete classification.

## Verification
The proof is analytic and covers every prime \(p\ge5\). The standalone script `artifacts/verify.py` is only a finite corroboration. For every prime \(5\le p\le31\) and every four-element support, it checks that the indicator has no Fourier zeros and that the deterministic one-zero test phase used by the script has exactly one zero. For every centrally symmetric support in that range, it constructs the explicit two-zero coefficients from the proof and checks that exactly two Fourier samples vanish.

The verifier does not establish the infinite theorem and is not used to infer any statement for primes beyond its finite range.

## Relationship to prior work
Tao's prime-cyclic uncertainty theorem states that every nonzero \(f:\mathbb Z_p\to\mathbb C\) satisfies
\[
|\operatorname{supp}f|+|\operatorname{supp}\widehat f|\ge p+1,
\]
and conversely every support pair satisfying the cardinality condition occurs. In particular, unrestricted four-sparse signals can attain three Fourier zeros. The present result imposes the natural phase-only constraint of equal coefficient magnitudes and shows that the three-zero extremal disappears completely; moreover, two zeros survive exactly on centrally symmetric four-point supports.

Krahmer, Pfander, and Rashkov survey and extend finite-Abelian support uncertainty to time-frequency representations. Their finite-Fourier discussion works with arbitrary coefficient vectors and does not impose equal coefficient magnitudes or classify the zero counts of one fixed four-point support.

Targeted searches also considered constant-modulus, phase-only, unimodular-null-vector, four-sparse, roots-of-unity, and additive-parallelogram formulations. No inspected source supplied this fixed-support phase-only classification.

## Limitations
No assertion is made for composite cyclic groups, supports of cardinality other than four, unequal coefficient magnitudes, or short-time Fourier transforms. The originality comparison is strongest against the inspected prime-cyclic uncertainty literature; there remains a residual risk that an equivalent elementary special case appears in older sequence-design or phase-code literature under different terminology.

## References
1. Terence Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286v1, first public 2003-08-29; 1991 MSC 42A99.
2. Felix Krahmer, Goetz E. Pfander, and Peter Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, first public 2006-11-16.
