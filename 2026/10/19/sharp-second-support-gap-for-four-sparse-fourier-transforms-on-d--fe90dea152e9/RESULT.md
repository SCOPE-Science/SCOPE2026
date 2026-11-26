# Sharp second-support gap for four-sparse Fourier transforms on dyadic cycles

## Finding

For every integer \(m\ge3\), let \(N=2^m\) and let \(f:\mathbb Z/N\mathbb Z\to\mathbb C\) have exactly four nonzero values. For the unnormalized Fourier transform
\[
\widehat f(k)=\sum_{x\in\mathbb Z/N\mathbb Z} f(x)e^{-2\pi ikx/N},
\]
either \(|\operatorname{supp}\widehat f|=N/4\) or \(|\operatorname{supp}\widehat f|\ge 3N/8\). Equality at \(N/4\) holds precisely for a nonzero scalar multiple of a character restricted to a coset of \(H=\{0,N/4,N/2,3N/4\}\). Both endpoints are attained for every \(m\ge3\).

## Assumptions and scope

The group is cyclic of two-power order and the four spatial coefficients are arbitrary nonzero complex numbers. Support counts exact nonzero entries. There is no numerical threshold or small-noise assumption.

## Proof

**Two and three spatial atoms.** On a cyclic group of order \(T=2^h\), a two-term Fourier polynomial, after removal of a monomial, has form \(u+vz^d\) with \(u,v\ne0\) and \(d\not\equiv0\pmod T\). Its zero count on the \(T\)-th roots is either zero or \(\gcd(d,T)\), by the cyclic-group power map. In particular its transform support has at least \(T/2\) elements. For three terms, remove a common monomial and divide the exponent differences by their largest common power of two. This means replacing the polynomial by one evaluated at \(z^{2^j}\) for some \(j\ge0\); the smaller root group is sampled with constant multiplicity \(2^j\). In the smaller group the exponents include both parities. If the polynomial vanished at both \(z\) and \(-z\), its even and odd parts would each vanish at \(z\), impossible because one part is a single nonzero monomial. Thus at least half of the original Fourier entries are nonzero. A one-atom function has no Fourier zeros.

**Four-atom minimum and equality.** Write \(A=\operatorname{supp} f\), \(B=\operatorname{supp}\widehat f\). Parseval, the triangle inequality and Cauchy–Schwarz give
\[
N\|f\|_2^2\le |B|\Big(\sum_{x\in A}|f(x)|\Big)^2\le 4|B|\|f\|_2^2.
\]
At equality the four coefficients have common magnitude; for each \(k\in B\), the four contributions to \(\widehat f(k)\) have common argument. Comparing two frequencies in \(B\) gives \(B-B\subseteq\langle A-A\rangle^\perp\). Since \(|B|=N/4\), translating \(B\) by one of its elements shows that the annihilator has at least \(N/4\) elements. The subgroup \(\langle A-A\rangle\) thus has at most four elements; its coset containing \(A\) shows it has exactly four. The alignment at a single \(k\in B\) gives the scalar restricted character. Conversely, the transform of such a function is supported on a coset of the annihilator and has exactly \(N/4\) nonzero entries.

**Induction for the gap.** At \(N=4\) the whole group is the only four-point support, and the minimum bound and equality characterization just proved apply. In the step \(N\ge8\), put \(M=N/2\), and use representatives \(0\le r<M\) to define
\[
F_0(r)=f(r)+f(r+M),\qquad
F_1(r)=e^{-2\pi ir/N}(f(r)-f(r+M)).
\]
Since \(e^{-2\pi i kM/N}=(-1)^k\), one has \(\widehat f(2j)=\widehat F_0(j)\) and \(\widehat f(2j+1)=\widehat F_1(j)\) for \(j\) modulo \(M\), using the same transform convention in the quotient. Thus the two quotient support counts add.

If there is exactly one occupied pair \(\{r,r+M\}\), each \(F_j\) has the two unpaired atoms and at most one other, so its transform has support at least \(M/2\). If there are two occupied pairs and both folded functions are nonzero, each has at most two atoms, giving the same bounds. In both situations the total is at least \(M\).

If there are two occupied pairs and one folded function vanishes identically, the other has two nonzero entries. Let \(d\not\equiv0\pmod M\) be their separation. If \(d\not\equiv M/2\), its zero count is at most \(\gcd(d,M)\le M/4\), giving at least \(3M/4=3N/8\) nonzero entries. If \(d\equiv M/2\), its transform, up to a nonzero character factor, is \(u+v(-1)^j\) with \(u,v\ne0\). The only way it vanishes at a frequency is \(u=v\) or \(u=-v\); equality of magnitudes alone is not enough. In those cases exactly one parity vanishes and the count is \(M/2=N/4\); otherwise it is \(M\). The minimum-equality analysis identifies the character cases at \(N/4\).

If there is no occupied pair, both folded functions have the same four-point support \(A'\) on \(\mathbb Z/M\mathbb Z\). When \(A'\) is not a coset of the order-four subgroup, the minimum-equality characterization and the inductive gap give at least \(3M/8\) Fourier entries in each. This subcase does not occur for \(M=4\).

When \(A'\) is an order-four coset, nonvanishing for each folded transform is periodic modulo four, since (after removing the factor from the coset representative) it is the Fourier sum of four positions spaced by \(M/4\). The two counts are positive multiples of \(M/4\), so if their sum is less than \(3M/4\), both must be \(M/4\). Then both folded functions are scalar characters on the same coset. Let \(r_0\) be the least representative of that coset and let \(r_1=r_0+M/4\). Denote their occupied lifts by \(x_0,x_1\). At either residue, \(F_1(r_i)/F_0(r_i)=e^{-2\pi ix_i/N}\). The ratio of two scalar characters on this coset, evaluated at \(r_1\) relative to \(r_0\), has fourth power \(1\). But the fourth power calculated from the lifts is \(e^{-2\pi i4(x_1-x_0)/N}=-1\), since \(x_1-x_0\equiv M/4\pmod M\). This contradiction completes the induction.

**Sharpness.** The character on \(H\) with constant value one attains \(N/4\). The four distinct terms of \(P(z)=(1+z^{N/2})(1+z^{N/8})\) give an indicator attaining \(3N/8\): on \(z=e^{-2\pi ik/N}\) the first factor vanishes at odd \(k\), and the second at \(k\equiv4\pmod8\). The disjoint zero sets leave exactly \(3N/8\) nonzeros.

## Verification

The proof above uses only exact identities. The original package's `verify.py` remains a bounded consistency check, not a proof over complex coefficients. As reported in `VERIFICATION.md`, it tests the four phases \(1,-1,i,-i\) exhaustively on order eight, uses finite samples at higher orders, and checks the endpoint witnesses through order 256. Its Fourier-support counts use a numerical threshold. The two-atom branch in the proof can be checked exactly with \(N=8\) and \(f(0)=f(4)=1,\ f(2)=f(6)=i\), all other values zero: \(F_1=0\), and \(\widehat F_0(j)=2+2i(-1)^j\) is nonzero for every \(j\), although the two folded coefficients have the same magnitude.

## Relationship to prior work and limitations

The classical product uncertainty principle gives \(N/4\), including the subgroup-coset equality case; Meshulam's divisor-interpolation bound also gives \(N/4\) at spatial support size four. Neither separates the next support from the minimum. Exact rank methods for support pairs and the order-eight uncertainty diagram address finite sizes or provide general criteria rather than the all-orders gap stated here. The published dyadic shell classification for four-point indicators [1] already gives both numerical endpoints for coefficient-one signals in all orders, and the order-eight support-pattern incidence table [2] covers arbitrary complex signals at \(N=8\). The distinct claim here is exclusion of the intervening supports for **arbitrary nonzero complex coefficients uniformly over all dyadic orders**. The exact three-point bound in [3] covers the three-atom auxiliary bound. The abstract of Delvaux and Van Barel [8] is relevant to alternative rank formulations; the full text was not inspected, so historical priority against a finer implication of their rank results is not established.

This result neither classifies all signals attaining \(3N/8\) nor gives a robust near-zero estimate or an extension to other prime powers.

## References

1. *Dyadic shell classification of Fourier zeros for four-point indicators*, Resultary record `68cf8ce2dd05`.
2. *Support-pattern incidence refinement of the order-eight Fourier uncertainty diagram*, Resultary record `78caf4d7929b`.
3. *Exact three-point Fourier uncertainty on every cyclic group*, Resultary record `cf7d7124f263`.
4. R. Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407.
5. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060, Acta Sci. Math. 79 (2013), 507–528.
6. F. Krahmer, G. Pfander, and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, Applied and Computational Harmonic Analysis 25 (2008), 209–225.
7. Yang et al., *Characterizing Kirkwood-Dirac nonclassicality and uncertainty diagram based on discrete Fourier transform*, arXiv:2303.17203.
8. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, DOI:10.1016/j.laa.2008.04.043.
