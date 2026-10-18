# Exact rotational \(2\)-binomial profile diversity at fixed binary composition

## Finding

A binary word is observed through counts of every scattered subsequence of length at most two. The number of different observations obtained by choosing a starting point on a circular word is a natural measure of distinguishability when the starting point is unknown. The following theorem determines its exact mean at every fixed composition, gives a sharp finite-word identifiability criterion, and identifies the leading loss due to repeated observations.

**Theorem.** Fix integers \(n\ge 2\) and \(1\le k<n\). Let \(w\) be uniformly distributed among the \(\binom nk\) labeled binary words of length \(n\) and Hamming weight \(k\). Write \(g=\gcd(n,k)\), \(L=n/g\), \(K=k/g\), and let \(C(w)\) be the number of different \(2\)-binomial equivalence classes among its \(n\) cyclic rotations. For each nonempty set \(T=\{t_1<\cdots<t_r\}\subseteq\{0,1,\ldots,g-1\}\), define its positive cyclic gap sequence
\[
 d_j=t_{j+1}-t_j\quad(1\le j<r),\qquad d_r=g+t_1-t_r,
\]
where for a singleton the sole gap is \(g\). Then the **exact finite formula** is
\[
\boxed{
\mathbb E C(w)=\frac L{\binom{gL}{gK}}
 \sum_{\varnothing\ne T\subseteq\{0,\ldots,g-1\}}
 (-1)^{|T|+1}\prod_{j=1}^{|T|}\binom{d_jL}{d_jK}.
}
\]
For every individual word of the specified composition, \(C(w)\ge L\), with equality **if and only if** \(w\) has period dividing \(L\). In particular, if \(\gcd(n,k)=1\), every rotation has a different observation, so \(C(w)=n\) identically.

For fixed \(g\ge2\), and integers \(L,K\) satisfying \(\gcd(L,K)=1\) and \(\varepsilon\le\alpha=K/L\le1-\varepsilon\) for some fixed \(\varepsilon>0\), the mean has the **uniform asymptotic expansion**
\[
\boxed{
\mathbb E C(w)=gL-
 \frac{g\sqrt g}{2\sqrt{2\pi\alpha(1-\alpha)}}
 \left(\sum_{d=1}^{g-1}\frac1{\sqrt{d(g-d)}}\right)\sqrt L
 +O_{g,\varepsilon}(1).
}
\]
The second term is strictly negative: repeated observations cause a square-root, rather than an order-\(L\), loss when the greatest common divisor stays fixed.

When \(g=2\), writing \(p=\binom LK^2/\binom{2L}{2K}\) gives exactly \(\mathbb EC=2L-Lp\). When \(g=3\), writing
\[
p=\frac{\binom LK\binom{2L}{2K}}{\binom{3L}{3K}},\qquad
q=\frac{\binom LK^3}{\binom{3L}{3K}},
\]
gives exactly \(\mathbb EC=3L-3Lp+Lq\). In this latter case, the expected counts of distinct rotational observations attained exactly once, twice and three times are respectively \(3L(1-2p+q)\), \(3L(p-q)\), and \(Lq\).

## Assumptions and scope

An occurrence of a scattered subword is an increasing selection of indices, not necessarily adjacent. Two finite binary words are \(2\)-binomially equivalent when the counts of each of the two one-letter and four two-letter scattered subwords are identical. Every rotation is considered as a linear word with a specified start; identical outputs are counted once, even if rotations originate from different starting points. All randomness is uniform over **labeled** fixed-weight words, not over necklaces. The theorem applies for all stated integers without assumptions of aperiodicity, balance, or large length. The asymptotic assumes \(g\) fixed and density bounded away from zero and one.

## Proof

**1. A sufficient scalar for the observation.** Index a binary word by \(0,1,\ldots,n-1\) and let \(S(w)=\sum_{j=0}^{n-1}j w_j\). With \(k\) ones, the count of scattered \(01\) equals
\[
\binom w{01}=S(w)-\binom k2.
\]
Indeed the one in position \(j\) has \(j\) earlier positions, of which as many as its rank among the ones minus one are ones. In addition, the counts of \(00\) and \(11\) are \(\binom{n-k}{2}\) and \(\binom{k}{2}\), and the \(10\) count is \(k(n-k)-\binom w{01}\). The one-letter counts are fixed. Thus, **within a fixed weight class, two words have the same full \(2\)-binomial signature exactly when their \(S\)-values agree.**

**2. Cyclic moment increment and its arithmetic obstruction.** Let \(R_iw=w_iw_{i+1}\cdots w_{n-1}w_0\cdots w_{i-1}\) and \(S_i=S(R_iw)\), with indices understood modulo \(n\). Moving the first bit to the end decreases the positions of all remaining ones by one and increases the moved one's position by \(n-1\). Hence
\[
S_{i+1}-S_i=n w_i-k,
\qquad
S_{i+d}-S_i=n\sum_{j=0}^{d-1}w_{i+j}-dk.
\]
In particular \(S_i\equiv S_0-ik\pmod n\). Since the additive order of \(k\pmod n\) is \(L=n/g\), a collision requires the two starting indices to be congruent modulo \(L\). Consequently the \(n\) starting points separate into \(L\) groups of \(g\) points each, and no observation is shared between different groups. This already proves \(C(w)\ge L\) and proves \(C(w)=n\) for \(g=1\).

**3. Probability of complete collision in a chosen subset.** Fix one residue-class group with starting points \(i+tL\) for \(t=0,\ldots,g-1\). For the nonempty subset \(T\) of group indices specified in the theorem, all \(S_{i+tL}\) at \(t\in T\) are equal exactly when every arc between consecutive selected starting points contains the number of ones dictated by its length: the arc of length \(d_jL\) must contain \(d_jK\) ones. This uses the telescoping increment formula, including the wrap-around arc since \(S_{i+n}=S_i\) identically. The arcs partition the \(n\) labeled positions. Their allowed fillings can be chosen independently subject only to the displayed counts. Since the total weight is \(gK\), the probability of this event is exactly
\[
\frac{\prod_{j=1}^r\binom{d_jL}{d_jK}}{\binom{gL}{gK}}.
\]
This argument also applies to \(r=1\), when the event is certain.

**4. Exact expectation by partition inclusion-exclusion.** For any finite indexed family of values \(v_0,\ldots,v_{g-1}\), let \(A_T\) be the event that all entries indexed by nonempty \(T\) are equal. The identity
\[
\#\{v_0,\ldots,v_{g-1}\}=
\sum_{\varnothing\ne T\subseteq\{0,\ldots,g-1\}}(-1)^{|T|+1}{\bf1}_{A_T}
\]
follows by considering one equality cluster at a time: a cluster of size \(m\) contributes \(\sum_{r=1}^m(-1)^{r+1}\binom mr=1\). Applying this identity within each of the \(L\) residue-class groups, taking expectations, and using their identical distribution under uniform fixed-weight sampling proves the finite formula. The \(g=2\) and \(g=3\) displays and the three multiplicity expectations follow by considering events that two or all three members in a group agree.

**5. Exactly when the lower bound is attained.** If \(C(w)=L\), each of the \(L\) residue groups must contribute exactly one observation. Thus \(S_i=S_{i+L}\) for every \(i\), so every cyclic window of length \(L\) contains exactly \(K\) ones by Step 2. Taking the difference of this window count at starting indices \(i+1\) and \(i\) shows \(w_{i+L}=w_i\) for every \(i\). Conversely, if \(w_{i+L}=w_i\) for all \(i\), every length-\(L\) window has \(K\) ones and so \(S_i=S_{i+L}\). Then each group contributes one observation and \(C(w)=L\). This also covers all periodic words with shorter periods dividing \(L\).

**6. Sharp asymptotics.** Keep \(g\ge2\) fixed and suppose \(\alpha=K/L\in[\varepsilon,1-\varepsilon]\). Uniform Stirling approximation of the binomial coefficients gives, for a subset \(T\) of size \(r\) with cyclic gaps \(d_1,\ldots,d_r\),
\[
\Pr(A_T)=
\frac{\sqrt g}{(2\pi\alpha(1-\alpha)L)^{(r-1)/2}\sqrt{d_1\cdots d_r}}
\bigl(1+O_{g,\varepsilon}(L^{-1})\bigr).
\]
The \(g\) singleton subsets yield \(gL\). The terms with \(r\ge3\) each have probability \(O_{g,\varepsilon}(L^{-1})\), thus their entire contribution to the expectation is \(O_{g,\varepsilon}(1)\). For any pair of selected indices at cyclic separation \(d\), the two gaps are \(d\) and \(g-d\). Summing over unordered pairs amounts to taking \(g/2\) times the sum over all \(d=1,\ldots,g-1\). Multiplying the resulting pair probabilities by \(-L\) gives the asserted square-root coefficient; their aggregate Stirling error is \(O_{g,\varepsilon}(L^{-1/2})\), subsumed by the remainder. This completes the proof.

## Verification

The standalone standard-library script `rotation_checker.py` directly enumerates every labeled nonconstant binary word of every length \(2\le n\le12\), computes all six scattered-subword counts for every rotation, and compares the number of signature classes with both the direct moment criterion and the exact rational expectation. It additionally checks \(C(w)\ge L\), the if-and-only-if period criterion, the coprime case, and the exact two- and three-group formulae (including their multiplicity expectations). In total this checks \(66\) parameter pairs and \(8{,}166\) words. Invocation: `python3 rotation_checker.py`. These finite tests are independent evidence only; the unrestricted proof is the six-step argument above.

## Relationship to prior work

Lejeune, Rigo, and Rosenfeld develop finite-word binomial-equivalence classes and a generation algorithm for \(2\)-binomial equivalence; Rigo, Stipulanti, and Whiteland investigate factor-wise binomial complexity of morphic infinite words. The present observable uses the same established equivalence relation, but restricts to **the cyclic rotation orbit of one binary fixed-content word** and averages the number of classes over that composition, obtaining a gcd-dependent closed formula and a square-root correction. The general size of a binomial-equivalence class does not determine its intersection with a given cyclic orbit: individual rotation comparisons and their joint fixed-content probabilities are needed. The general monoid-conjugacy questions in Whiteland's study concern \(xz\sim_2 zy\) with an auxiliary word \(z\), rather than equality among the concrete rotations of one fixed-length word. The exact distribution of all classes and factor complexity results do not imply the orbital expectation established here. No equivalence to an inspected earlier theorem was found, but an unindexed equivalent formulation remains a risk.

## Limitations

The probability model samples labeled words of one prescribed binary composition; it does **not** sample distinct necklaces uniformly. The exact formula may have exponential complexity in \(g\), and this result does not provide a corresponding closed distribution for every \(g\), extend directly to alphabets with three or more symbols, or give error-correcting reconstruction. The asymptotic is uniform only for fixed \(g\) and densities bounded away from both endpoints; it does not claim uniformity when \(g\) grows with \(n\). An independent mathematical audit has not been performed.

## References

- M. Lejeune, M. Rigo, M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732v1, submitted 2020-01-31. https://arxiv.org/abs/2001.11732
- M. Rigo, M. Stipulanti, M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, arXiv:2201.04603v1, submitted 2022-01-12. https://arxiv.org/abs/2201.04603
- M. Rigo, P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, Theoretical Computer Science 601 (2015), 47–57. https://orbi.uliege.be/handle/2268/178703
- M. A. Whiteland, *Equations over the \(k\)-binomial monoids*, WORDS 2021; related dissertation sections on binomial conjugacy. https://www.utupub.fi/server/api/core/bitstreams/b3b51aff-6c73-43aa-854c-ca2a6e5ba99a/content
