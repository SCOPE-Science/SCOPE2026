# Independent mathematical audit

## correctness

PASS

For an n-term rational-coefficient exponential sum, strengthen Schulz Lemma 3.2 induction from zero density to O((1+log H)^n) distinct integer values in [-H,H]. Subspace theorem partitions solutions into finitely many degenerate proper-subspace S1 and nondegenerate S2. On S1, eliminate one exponent term to get at most n-1-term sums, invoking the quantitative induction. On S2 Schulz already proves (bh)^(4n^2)>max a_i^e_i, hence at most (5n^2 log_2(bH))^n exponent tuples plus finite bounded exceptions. Finite Presburger affine pieces and finitely many choices of powers bases preserve exponent <=M. For sharpness, B>M avoids carrying, so unordered multisets of M exponents <=L inject into M-power sums <=M B^L; count exactly binomial(L+M,M)=Theta((log H)^M). Independent exact enumeration verified 42 (M,L) carry-free cases. The source subspace theorem is used as a cited lemma, not re-proved.

## originality

PASS

Best-of-knowledge quantitative enhancement of Schulz’s qualitative Theorem B: the source explicitly proves zero natural density, not the uniform O((log H)^M) bound with optimal exponent. Although S2 logarithmic counting is printed in Lemma 3.2 and the S1 elimination is already in its proof, quantitative induction over degenerate subspaces must be strengthened for the full claim, then sharpness is separately established by a carry-free B>M lower family. A narrowly close implication risk remains, but the sharp all-dimension counting theorem and matching construction were not stated in inspected primary literature.

## value

PASS

The sharp growth exponent M for all Presburger images of finite unions of exponential powers is a natural quantitative sparseness invariant; it refines mere density zero by orders of magnitude and cannot be lowered uniformly, as the distinct-multiset construction shows. The exact exponent can be independently useful in quantitative model-theoretic and exponential-sum arguments even if the stronger induction is close to earlier proof machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
