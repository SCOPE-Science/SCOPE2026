# Alternating covariance of cycle classes in uniform derangements

## Finding

Let \(\pi\) be uniform among permutations of \(\{1,\ldots,n\}\) with no fixed points, and let \(C_j\) be its number of cycles of length \(j\). For any **distinct** integers \(r,s\ge2\) and any integer \(n\ge r+s\), put \(m=n-r-s\). Then

\[
\operatorname{sgn}\operatorname{Cov}(C_r,C_s)=(-1)^m,
\]

where the sign on the right is \(+1\) or \(-1\): **the covariance never vanishes**. More precisely, with

\[
a_k=\sum_{j=0}^{k}\frac{(-1)^j}{j!},\qquad k\ge0,
\]

we have

\[
\operatorname{Cov}(C_r,C_s)=
\frac{a_m a_n-a_{m+r}a_{m+s}}{rs\,a_n^2}.
\]

For fixed distinct \(r,s\ge2\) and \(m\to\infty\), with \(n=m+r+s\),

\[
\lim_{m\to\infty}(-1)^m rs(m+1)!\operatorname{Cov}(C_r,C_s)=e.
\]

If \(r+s>n\), the covariance is strictly negative whenever both cycle classes can occur individually (equivalently, neither length equals \(n-1\), given \(2\le r,s\le n\)); otherwise it is zero because one class is impossible. Examples: \(\operatorname{Cov}(C_2,C_3)=30/121\) at \(n=5\), but \(-432/2809\) at \(n=6\). Thus forbidding fixed points creates an exact parity-alternating dependence between two cycle-size counts, even though the corresponding counts in unrestricted uniform permutations are uncorrelated whenever \(r+s\le n\).

## Assumptions and scope

All probabilities are uniform on the finite set of fixed-point-free permutations. The theorem concerns distinct cycle lengths \(r,s\ge2\), integer \(n\ge\max(r,s)\), and ordinary covariance of their numerical counts. The scaling limit fixes the two lengths while adding more labels. The analytic determinant lemma used below holds more generally for all positive integer shifts.

## Proof

**1. Exact factorial moments.** A derangement on \(n\ge2\) labels has \(D_n=n!a_n\) possible realizations; \(a_n>0\). To mark one \(r\)-cycle, choose its labels, cyclically arrange them, and derange the remaining labels. Consequently

\[
\mathbb EC_r=\frac{a_{n-r}}{r a_n}.
\]

For distinct \(r,s\) with \(r+s\le n\), mark an \(r\)-cycle and an \(s\)-cycle disjointly; this gives

\[
\mathbb E(C_rC_s)=\frac{a_{n-r-s}}{rs a_n}.
\]

Subtracting the product of means establishes the displayed covariance formula. If \(r+s>n\), the joint product is identically zero. Every length \(2\le j\le n-2\) has positive mean (complete an \(j\)-cycle by a derangement on the remaining \(n-j\ge2\) labels); the length \(n\) also has positive mean, whereas the length \(n-1\) has zero mean.

**2. A strict alternating-determinant lemma.** For any integers \(m\ge0\) and \(r,s\ge1\), we prove

\[
(-1)^m\bigl(a_m a_{m+r+s}-a_{m+r}a_{m+s}\bigr)>0.
\]

Write

\[
B_{t,h}=\sum_{j=1}^{h}\frac{(-1)^{j+1}}{(t+j)!},\qquad t\ge0,\quad h\ge1.
\]

Alternating-series bounds give, uniformly for all such \(t,h\),

\[
0<\frac{t+1}{(t+2)!}\le B_{t,h}\le\frac1{(t+1)!}.
\]

Because \(a_{t+h}-a_t=(-1)^{t+1}B_{t,h}\), direct subtraction yields

\[
(-1)^m\bigl(a_m a_{m+r+s}-a_{m+r}a_{m+s}\bigr)
=a_{m+r}B_{m,s}-(-1)^r a_mB_{m+r,s}.
\]

When \(r\) is odd, the expression is strictly positive: \(a_k\ge0\) for \(k\ge0\), and the two factors cannot both be zero because \(a_k=0\) only for \(k=1\). When \(r\) is even (so \(r\ge2\)), it suffices to show \(a_{m+r}/a_m>B_{m+r,s}/B_{m,s}\) if \(a_m>0\). The alternating bounds imply

\[
\frac{B_{m+r,s}}{B_{m,s}}
\le\frac{(m+2)!}{(m+1)(m+r+1)!}
\le\frac1{(m+1)(m+3)}.
\]

For \(m=0\), \(a_m=1\) and \(a_r>1/3\), while the last bound is at most \(1/3\). For \(m\ge2\), \(1/3\le a_k\le1/2\) for every \(k\ge2\); hence \(a_{m+r}/a_m\ge2/3\), whereas the last bound is at most \(1/15\). For \(m=1\), \(a_m=0\) and the expression equals \(a_{m+r}B_{m,s}>0\). This completes the lemma. Substituting \(m=n-r-s\) gives the strict parity sign of the covariance.

**3. Sharp factorial decay.** For fixed \(r,s\ge2\), as \(m\to\infty\), the alternating Taylor series gives

\[
B_{m,s}\sim\frac1{(m+1)!},\qquad
B_{m+r,s}=O\left(\frac1{(m+r+1)!}\right),\qquad
a_{m+r},a_{m+r+s}\longrightarrow e^{-1}.
\]

The exact determinant identity from Step 2 therefore yields

\[
(-1)^m\bigl(a_m a_{m+r+s}-a_{m+r}a_{m+s}\bigr)
\sim\frac{e^{-1}}{(m+1)!}.
\]

Dividing by \(rs\,a_{m+r+s}^2\) proves the limit \(e\) asserted above.

## Verification

A standalone Python 3 verifier, `verify.py`, uses exact rational arithmetic for the moment formulas, the determinant reduction, the alternating sign, and the alternating-series bounds across thousands of parameter tuples. It independently enumerates all derangements for \(3\le n\le8\) and directly recomputes every relevant cycle-size pair moment, then checks the first two explicit covariance values. Finite computations corroborate the algebra but are not used to infer the universal inequality or limit.

## Relationship to prior work

The conditioned Ewens cycle-count factorial moments are established in Poly H. da Silva, Arash Jamshidpey and Simon Tavaré, *Random derangements and the Ewens Sampling Formula* (arXiv:2006.04840, 8 June 2020), particularly their equation (6) with \(\theta=1\). Thus the **moment formula itself is prior work**, not a novelty claim. Their paper gives an explicit joint factorial-moment expression and asymptotic independent-Poisson convergence; the present statement isolates and proves the strict parity sign for all finite sizes and the leading factorial coefficient via an independent alternating-determinant inequality. Tavaré's *The magical Ewens sampling formula* (2021) provides broader background on Ewens sampling and the conditioning relation. Published general formulas determine the moments algebraically, so the priority distinction lies in the nontrivial sign-and-rate analysis, not enumeration.

## Limitations

The result is restricted to the **uniform** derangement law, rather than arbitrary Ewens parameter, and to two distinct cycle lengths. Pairwise covariance does not characterize full dependence or any monotone stochastic ordering. The asymptotic constant holds for fixed lengths, not lengths growing with \(n\). Historical originality is assessed only against inspected accessible sources and searches; an older observation of the sign theorem remains possible, especially as the underlying factorial moments are classical. No independent audit or external certification is asserted.

## References

1. P. H. da Silva, A. Jamshidpey, and S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840v1 (8 June 2020), especially Section 2, equation (6). https://arxiv.org/abs/2006.04840
2. S. Tavaré, *The magical Ewens sampling formula*, Bulletin of the London Mathematical Society (2021), DOI:10.1112/blms.12537. https://doi.org/10.1112/blms.12537
