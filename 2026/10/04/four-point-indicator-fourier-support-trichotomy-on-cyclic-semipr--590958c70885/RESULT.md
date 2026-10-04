# Four-point indicator Fourier-support trichotomy on cyclic semiprime groups
## Finding
Let \(p\) be an odd prime and \(N=2p\). For a four-element set \(A\subset\mathbb Z_N\), write \(1_A\) for its indicator and use the unnormalized Fourier transform
\[
\widehat{1_A}(k)=\sum_{a\in A}\exp(-2\pi i ka/N),\qquad k\in\mathbb Z_N.
\]
Then only three Fourier-support cardinalities occur:
\[
|\operatorname{supp}\widehat{1_A}|\in\{p,2p-1,2p\}.
\]
More precisely:

1. \(|\operatorname{supp}\widehat{1_A}|=p\) exactly when \(A\) is the union of two distinct antipodal pairs \(\{x,x+p\}\). There are \(\binom p2\) such sets, and their Fourier zero set is the set of all odd frequencies.
2. \(|\operatorname{supp}\widehat{1_A}|=2p-1\) exactly when \(A\) contains two even and two odd residues but is not a union of two antipodal pairs. There are \(\binom p2^2-\binom p2\) such sets, and their only Fourier zero is \(k=p\).
3. Every other four-element set has full Fourier support \(2p\). There are \(\binom{2p}4-\binom p2^2\) such sets.

Thus the complete indicator-restricted support distribution at time-support size four is explicit for every cyclic group of order twice an odd prime.
## Assumptions and scope
The prime \(p\) is odd. The set \(A\) has four distinct elements in \(\mathbb Z_{2p}\). Coefficients are fixed to be the indicator coefficients \(1\); the result does not classify arbitrary complex-valued functions supported on four points. The Fourier transform is unnormalized, although support cardinalities are normalization-independent.
## Proof
We first use an elementary unit-circle lemma. If four complex numbers of modulus one sum to zero, then they split into two antipodal pairs. Indeed, for roots \(z_1,z_2,z_3,z_4\) with \(z_1+z_2+z_3+z_4=0\), the monic polynomial having these roots has first elementary symmetric coefficient zero. Since \(|z_j|=1\), its third elementary symmetric coefficient is the product \(z_1z_2z_3z_4\) times the complex conjugate of the first, and is therefore also zero. The polynomial is even, so its roots occur in pairs \(z,-z\).

Fix a frequency \(k\). If \(k\) is even and nonzero, then \(e^{-2\pi i k/N}\) has odd order dividing \(p\). A vanishing sum of four of its powers would, by the lemma, contain an antipodal pair; this is impossible because \(-1\) is not a root of unity of odd order. Hence no nonzero even frequency is a zero.

At \(k=p\),
\[
\widehat{1_A}(p)=\sum_{a\in A}(-1)^a,
\]
so it vanishes exactly when \(A\) has two even and two odd elements.

Now let \(k\) be odd with \(k\ne p\). Since \(p\) is prime, \(\gcd(k,2p)=1\). If \(\widehat{1_A}(k)=0\), the unit-circle lemma pairs the four values into antipodal pairs. Thus paired exponents \(a,b\) obey
\[
k(b-a)\equiv p\pmod{2p}.
\]
The inverse of the odd unit \(k\) is odd, hence multiplying by it leaves \(p\) fixed modulo \(2p\). Therefore \(b-a\equiv p\pmod{2p}\). So \(A\) is the union of two antipodal pairs. Conversely, if \(A\) is such a union, each pair cancels at every odd frequency, so every odd \(k\) is a zero.

We have therefore proved the exact zero-set trichotomy: an antipodal-pair union has all \(p\) odd frequencies as zeros; a non-antipodal set with two even and two odd elements has only \(p\) as a zero; and every other set has no zeros.

For the counts, the \(p\) antipodal pairs partition \(\mathbb Z_{2p}\), so choosing two gives \(\binom p2\) sets of the first type. There are \(p\) even and \(p\) odd residues, hence \(\binom p2^2\) sets with two of each parity. Removing the antipodal-pair unions gives \(\binom p2^2-\binom p2\) sets of the second type. Subtracting all two-even/two-odd sets from the total \(\binom{2p}4\) gives the third count.
## Verification
The accompanying script `verify_z2p_four_indicator.py` independently evaluates Fourier zeros by exact integer arithmetic in cyclotomic quotient rings, rather than by floating-point trigonometry. It exhaustively checks every four-subset for \(p\in\{3,5,7,11,13\}\), totaling 23,491 subsets and 565,834 exact frequency tests. For each subset it compares the direct cyclotomic zero set with the theorem's structural prediction and checks all three counting formulas. The replay ends with `VERIFY_OK`.

The finite computation corroborates the theorem; the proof above is the argument for all odd primes.
## Relationship to prior work
Meshulam's finite-abelian uncertainty inequality gives general lower bounds on Fourier support as a function of time support, but it concerns arbitrary complex coefficients and does not give this indicator-restricted distribution.

Bonami and Ghobber classify equality cases for uncertainty minima in several finite abelian families, including \(\mathbb Z_q\times\mathbb Z_p\) for distinct primes. Their results likewise concern arbitrary complex-valued functions and extremal support pairs, not the full distribution of Fourier-support sizes of four-point indicators.

Mercer's length-four Newman-polynomial analysis supplies a closely related local fact: a four-term \(0,1\) polynomial with a unimodular zero has a highly constrained cyclotomic structure, and his Lemma 4 gives the four-unit-vector cancellation mechanism used above. The present statement fixes the cyclic modulus \(2p\), determines the complete Fourier zero set of every four-subset, and counts every support stratum. Those fixed-modulus support multiplicities and enumeration are not stated in the inspected source.
## Limitations
The theorem is specific to indicator coefficients and to cyclic order \(2p\) with \(p\) an odd prime. It does not classify four-point indicators for general composite moduli, where nonprimitive odd frequencies can introduce additional zero patterns. The originality comparison cannot exclude an equivalent result hidden under different terminology in older Newman-polynomial or finite Fourier literature; the closest inspected length-four source gives the unit-root existence structure rather than the fixed-modulus support distribution.
## References
1. R. Meshulam, “An uncertainty inequality for finite abelian groups,” arXiv:math/0312407, first posted 2003-12-22; European Journal of Combinatorics 27 (2006), 63–67.
2. A. Bonami and S. Ghobber, “Equality cases for the uncertainty principle in finite Abelian groups,” arXiv:1003.5060, first posted 2010-03-26; Acta Scientiarum Mathematicarum 79 (2013), 507–528.
3. I. Mercer, “Newman Polynomials, Reducibility, and Roots on the Unit Circle,” Integers 12 (2012), 503–519, DOI 10.1515/integers-2011-0120.
