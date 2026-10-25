# Complete triple-intersection spectrum of binary exact-two substitution spheres

## Finding
For each integer \(n\ge 3\), let \(\Sigma_n=\{0,1\}^n\). Write
\[
S_2(x)=\{y\in\Sigma_n:d_H(x,y)=2\},\qquad
J(x_1,x_2,x_3)=\bigl|S_2(x_1)\cap S_2(x_2)\cap S_2(x_3)\bigr|,
\]
where the three centers are pairwise distinct. Define the complete intersection-population polynomial by summing over **unordered** three-element subsets of centers:
\[
P_n(z)=\sum_{\{x_1,x_2,x_3\}\in\binom{\Sigma_n}{3}}z^{J(x_1,x_2,x_3)}.
\]
Then, with \(\binom nk=0\) whenever \(k>n\),
\[
\boxed{\begin{aligned}
P_n(z)={}&\binom{2^n}{3}\\
&+2^n\left[\binom n3(z^{n-2}-1)
+3\binom n4(z^4-1)
+10\binom n5(z^3-1)
+15\binom n6(z-1)\right].
\end{aligned}}
\]
The terms at coincident exponents must be combined: for example, the \(\binom n3\) term and the \(\binom n4\) term both contribute at exponent four when \(n=6\). In particular,
\[
\boxed{\max_{\{x_1,x_2,x_3\}}J(x_1,x_2,x_3)
=\begin{cases}1,&n=3,\\\max\{4,n-2\},&n\ge4.\end{cases}}
\]
The numbers of unordered triples attaining the maximum, successively for \(n=3\), \(n=4,5\), \(n=6\), and \(n\ge7\), are
\[
2^n\binom n3,\qquad3\cdot2^n\binom n4,\qquad
2^n\left[\binom n3+3\binom n4\right],\qquad
2^n\binom n3.
\]
Consequently, for uncoded binary length-\(n\) transmissions with **exactly two** substitutions in each read, \(1+\max J\) distinct reads are necessary and sufficient in the worst case to limit the candidate-message list to at most two. This threshold is sharp without any minimum-distance hypothesis on the message space.

As a further population consequence, the probability that three distinct centers selected uniformly without replacement have a common radius-two output is
\[
\frac{2^n\left[\binom n3+3\binom n4+10\binom n5+15\binom n6\right]}
{\binom{2^n}{3}}
=\frac{n^6}{8\,4^n}\bigl(1+O(n^{-1})\bigr)
\quad(n\to\infty).
\]

## Assumptions and scope
The alphabet is binary; Hamming distance counts differing coordinates. An exact-two substitution sphere requires **exactly** two changed bits, not zero, one, or at most two changes. All center triples are unordered and consist of distinct length-\(n\) strings. The statements hold for every integer \(n\ge3\), including small dimensions, and use the convention that out-of-range binomial coefficients vanish. When applying the two-list threshold, observed outputs are distinct words; no probability distribution, codebook restrictions, or channel independence assumption is required.

## Proof
**1. Normalize the three centers and derive feasibility.** Translating all strings by the bitwise XOR of the first center preserves Hamming distance. Therefore take \(x_1=0^n\), and partition the coordinates into four classes according to the ordered bit pair \((x_{2,i},x_{3,i})\): sizes \(A,a,b,c\) for patterns \((0,0),(1,0),(0,1),(1,1)\), respectively, with \(A=n-a-b-c\). The three pairwise center distances are
\[
d_H(x_1,x_2)=a+c,\qquad d_H(x_1,x_3)=b+c,\qquad d_H(x_2,x_3)=a+b.
\]
If a word lies in all three exact-two spheres, the triangle inequality bounds each of these positive distances by four. Parity makes each distance even: every center is at even distance from the common output, so two centers have even mutual distance. Thus each pair distance belongs to \(\{2,4\}\).

**2. Classify all possible center types.** Since the three pair distances completely determine \(a,b,c\), the eight choices of distances from \(\{2,4\}^3\) give exactly the following eight permitted profiles:
\[
(a,b,c)\in\{(1,1,1),(0,2,2),(2,0,2),(2,2,0),
(1,1,3),(1,3,1),(3,1,1),(2,2,2)\}.
\]
There cannot be a positive intersection for any other triple of distinct centers. A profile occurs only if \(a+b+c\le n\).

**3. Compute every positive intersection.** Let \(i,j,\ell,r\) denote the numbers of ones of a possible output in the respective coordinate classes of sizes \(A,a,b,c\). Requiring distance two from each center is equivalent to
\[
i+j+\ell+r=2,\qquad j+r=(a+c)/2,\qquad
\ell+r=(b+c)/2.
\]
The number of choices for a feasible quadruple is
\[
\binom Ai\binom aj\binom b\ell\binom cr.
\]
In the \((1,1,1)\) profile, the two candidate allocations contribute \(1\) and \(A\) (the latter vanishes when \(A=0\)), hence \(J=A+1=n-2\). For each permutation of \((0,2,2)\), the unique feasible allocation has four realizations, so \(J=4\). For each permutation of \((1,1,3)\), it has three realizations, so \(J=3\). For \((2,2,2)\), it has one realization, so \(J=1\). These counts, including the boundary cases with \(A=0\), exhaust all positive intersections.

**4. Count center triples in every class.** For a fixed first center, the number of ordered choices for the other two centers of a profile \((a,b,c)\) is the multinomial coefficient
\[
\frac{n!}{A!\,a!\,b!\,c!}.
\]
There are \(2^n\) choices for the first center, and each unordered triple of distinct centers has exactly six orderings. Summing over the one, three, three, and one profiles in the four classes, respectively, gives their unordered populations:
\[
\begin{array}{c|c|c}
\text{profile class}&J&\text{number of unordered triples}\\ \hline
(1,1,1)&n-2&2^n\binom n3\\
\text{permutations of }(0,2,2)&4&3\cdot2^n\binom n4\\
\text{permutations of }(1,1,3)&3&10\cdot2^n\binom n5\\
(2,2,2)&1&15\cdot2^n\binom n6
\end{array}
\]
All remaining triples have empty intersection, and there are \(\binom{2^n}{3}\) unordered triples in total. Subtracting the positive populations from the total gives the constant coefficient and therefore the claimed polynomial.

**5. Sharpness and population consequences.** Each displayed class is realized whenever its support size does not exceed \(n\). Comparing the four positive sizes, with absent classes removed at small \(n\), gives the maximum and the exact maximizing populations. Let \(Y\) be a set of distinct observed words. It admits at least three possible centers exactly when \(Y\) is contained in the common exact-two sphere of three distinct centers. Therefore more than \(\max J\) reads exclude three candidates, whereas \(\max J\) distinct outputs can be selected from the intersection of an extremal triple. This proves both directions of the two-list threshold. The positive-triple count is the sum of the four displayed populations. Its leading term is \(15\cdot2^n\binom n6\), and division by \(\binom{2^n}{3}\) yields the stated asymptotic probability.

## Verification
The included standard-library-only program at `verification/verify_triple_spheres.py` independently constructs the exact-two spheres as bit masks and enumerates **every unordered center triple** for dimensions \(n=3,4,5,6,7,8\). It compares their complete computed histograms with the closed polynomial, checks each sharp maximum, and independently enumerates the eight admissible coordinate profiles. Execute with `python3 verification/verify_triple_spheres.py`; the expected terminal marker is `VERIFY_OK`. The output of a successful complete run is embedded at `verification/verify_output.txt`.

An additional symbolic consistency check follows by double counting pairs consisting of an output and a center triple all at Hamming distance two from it:
\[
\sum_{\{x_1,x_2,x_3\}}J(x_1,x_2,x_3)
=2^n\binom{\binom n2}{3}
=2^n\left[(n-2)\binom n3+12\binom n4+30\binom n5+15\binom n6\right].
\]
The finite experiments confirm the formulas in the tested dimensions; the proof above, not the finite enumeration, establishes their validity for all \(n\ge3\).

## Relationship to prior work
Vu, Wang, and Vu (2026) study the maximum three-**ball** intersection in a regime where error radius and center separation grow linearly with word length. Their exact sphere counting formula is developed for a canonical equidistant center configuration; they do not enumerate the intersection populations across all distinct center triples at fixed exact-two radius.

Junnila, Laihonen, Lehtilä, and Devaraj (2026) derive general exact formulas for intersections of Hamming **balls** (possibly with unequal radii) and analyze extremal triples. Their general formula can recover the size for a prescribed triple of exact spheres by taking differences of radii, but this is not a formula for the number of center triples of each possible intersection size. The present finding counts that entire population, identifies every maximizing type, and determines the resulting sharp exact-two two-list threshold; it does not claim that per-center intersection formulas are new.

Older intersections-of-spheres literature includes Honkala's 1987 contribution. The complete text could not be inspected from the available source, so possible older equivalent classifications are an originality limitation.

## Limitations
This is a mathematical classification for the binary alphabet and the exact-two substitution model only; it is not a bound for at-most-two substitutions, unequal exact radii, or nonbinary alphabets. The two-list consequence concerns **uncoded**, unrestricted centers and distinct reads. It neither constructs an error-correcting code nor improves coding rate. Although the closest accessible papers do not state the global population law, earlier unindexed treatments, including inaccessible older sphere literature, could contain an equivalent enumeration. No independent external validation is asserted.

## References
1. Binh Vu, Shuche Wang, and Van Khu Vu, *List Reconstruction Problem with List Size Two*, arXiv:2605.23638v1, publicly available 2026-05-22. https://arxiv.org/html/2605.23638v1
2. Ville Junnila, Tero Laihonen, Tuomo Lehtilä, and Pavan Padavu Devaraj, *The Size of the Intersection of q-ary Hamming Balls*, arXiv:2606.09158v1, publicly available 2026-06-08. https://arxiv.org/abs/2606.09158
3. I. Honkala, *On the intersections and unions of Hamming spheres*, in *The Very Knowledge of Coding*, pp. 70–81, 1987. Bibliographic reference only; full text not inspected.
