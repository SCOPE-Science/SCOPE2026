# A sharp composition threshold for two adjacent binary motif counts

## Finding
Fix integers \(a\ge1\) and \(b\ge2\), with \(n=a+b\ge6\). Uniformly sample a binary word with exactly \(a\) ones and \(b\) zeros. Let \(U\) and \(V\) count (possibly overlapping) **consecutive** occurrences of the length-three words \(001\) and \(010\), respectively. They have identical means,
\[
\mathbb E U=\mathbb E V=\frac{ab(b-1)}{n(n-1)},
\]
but their covariance has the following **strict, exhaustive sign classification**:
\[
\operatorname{Cov}(U,V)
\begin{cases}
>0,& b\ge a+2,\\
<0,& b\le a+1.
\end{cases}
\]
In particular, no admissible composition produces zero covariance. For example, at \((a,b)=(2,4)\) it is \(2/75\), while at \((a,b)=(3,3)\) it is \(-11/100\). These are finite-population covariances under exact global symbol counts, not independent Bernoulli-word covariances.

## Assumptions and scope
A binary word means a sequence \(w=(w_1,\dots,w_n)\in\{0,1\}^n\). The law gives equal mass \(1/\binom{n}{a}\) to each word with \(a\) ones. For every starting position \(1\le i\le n-2\), define \(I_i=\mathbf1\{(w_i,w_{i+1},w_{i+2})=(0,0,1)\}\) and \(J_i=\mathbf1\{(w_i,w_{i+1},w_{i+2})=(0,1,0)\}\), and put \(U=\sum_i I_i\), \(V=\sum_i J_i\). Occurrences may overlap; neither statistic is a disjoint-pattern count. The restriction \(n\ge6\) ensures disjoint pairs of length-three windows exist. All statements quantify over every admissible integer pair \((a,b)\), with no limiting regime.

## Proof
Write \((x)_k=x(x-1)\cdots(x-k+1)\) and \((x)_0=1\), so that for any fixed ordered configuration of \(r\) ones and \(s\) zeros at distinct positions, its probability is \((a)_r(b)_s/(n)_{r+s}\). In particular, both patterns use one one and two zeros, whence
\[
E:=\mathbb E U=\mathbb E V=(n-2)\frac{a(b)_2}{(n)_3}=\frac{ab(b-1)}{n(n-1)}.
\]
For the mixed second moment, enumerate **ordered** pairs of starts: the \((n-4)(n-5)\) disjoint pairs require two ones and four zeros; among the five possible overlapping displacements, only those in which the \(010\) start is two places before the \(001\) start, or one place after it, are compatible. The first produces the length-five word \(01001\), using two ones and three zeros, and occurs at \(n-4\) paired starts. The second produces the length-four word \(0010\), using one one and three zeros, and occurs at \(n-3\) paired starts. All three remaining overlaps are inconsistent. Hence
\[
\mathbb E(UV)=
(n-4)(n-5)\frac{(a)_2(b)_4}{(n)_6}
+(n-4)\frac{(a)_2(b)_3}{(n)_5}
+(n-3)\frac{a(b)_3}{(n)_4}.
\]
Subtracting \(E^2\) and reducing to a common denominator yields the exact rational identity
\[
\operatorname{Cov}(U,V)=
-\frac{ab(b-1)\,P(a,b)}{n^2(n-3)(n-2)(n-1)^2},
\]
where
\[
\begin{aligned}
P(a,b)={}&2a^3b-2a^3-a^2b-2ab^3+8ab^2-9ab+2a\\
&+b^3-3b^2+2b.
\end{aligned}
\]
The prefactor of \(-P\) is strictly positive throughout the stated domain. To determine its sign without asymptotics, first assume \(b\le a+1\) and set \(v=a-b+1\ge0\). Then exact expansion gives
\[
\begin{aligned}
P(a,b)={}&2b(b-1)(b-2)
+(4b^3-12b^2+11b-4)v\\
&+(6b^2-13b+6)v^2+(2b-2)v^3.
\end{aligned}
\]
For every integer \(b\ge2\), the three coefficients of positive powers of \(v\) are strictly positive, and the constant term is nonnegative. If \(b\ge3\) the constant term is strictly positive; if \(b=2\), then \(n\ge6\) forces \(a\ge4\), hence \(v>0\). Thus \(P(a,b)>0\) in this case.

If \(b\ge a+2\), instead set \(v=b-a-2\ge0\); then
\[
\begin{aligned}
P(a,b)={}&-2a^3+2a
+(-4a^3-6a^2+5a+2)v\\
&+(-6a^2-a+3)v^2+(1-2a)v^3.
\end{aligned}
\]
For every integer \(a\ge1\), all three nonconstant coefficients are strictly negative and the constant term is nonpositive, strictly negative for \(a\ge2\). If \(a=1\), the condition \(n\ge6\) forces \(b\ge5\) and therefore \(v\ge2\). Consequently \(P(a,b)<0\) throughout this case. Combining the two inequalities with the covariance identity proves both strict signs and the absence of equality cases. \(\square\)

## Verification
The standalone standard-library program `verify.py` independently enumerates all fixed-composition words with \(6\le n\le13\) and compares exact rational means, mixed moments, covariance and signs to the formulas. It additionally checks the rational covariance reduction and both slack-polynomial identities on all admissible integer pairs with \(1\le a\le80\), \(2\le b\le80\). Running `python3 verify.py` produced `PASS exact assertions: 31990`. Those are finite consistency checks; the unrestricted theorem is established by the event-overlap enumeration and polynomial sign proof above.

## Relationship to prior work
Joint analysis of patterns in words and of multiset arrangements is an established subject. Even-Zohar, Lakrec and Tessler (arXiv:2012.00742, first posted December 1, 2020) explicitly analyze the same fixed-composition sampling law and covariance geometry of **not-necessarily-consecutive subsequence** counts; their variables count all subsequences of a prescribed length, not consecutive windows. Their primary MSC is 60C05. Mansour, Rastegar and Roitershtein (2019, arXiv:1905.05646) analyze occurrences of **one order-isomorphic subsequence pattern** in uniformly sampled alphabet words, including asymptotic variance. Mansour and Rastegar (2021, arXiv:2102.00443) likewise focus on pattern avoidance and links to permutations. Jelínek, Mansour, Ramírez and Shattuck (2021, arXiv:2111.06185) study **fixed-multiset permutations**, but classify avoidance and Wilf equivalences for **not-necessarily-consecutive subsequence patterns**. None of the theorem statements inspected yields the finite covariance between the two literal adjacent trigrams or its integer-composition sign threshold. Classical overlap and generating-function machinery can compute motif moments in principle, and historical implicit derivation is a genuine unresolved priority risk. The contribution asserted here is the strict phase boundary and exact formula, not a new general method for counting word occurrences.

## Limitations
The law has exactly fixed symbol counts and samples words uniformly; it is neither an iid Bernoulli model nor a Markov model. The result treats one canonical pair of length-three adjacent motifs and does not assert universal negative/positive association, signs for all motifs, conditional independence, limiting normality, or new results on nonconsecutive subsequence patterns. General formal tools for multivariate pattern moments might implicitly subsume the rational covariance identity; their ability to imply the sharp sign boundary without additional argument has not been exhaustively excluded.

## References
- C. Even-Zohar, T. Lakrec and R. J. Tessler, *Spectral Analysis of Word Statistics*, first posted December 1, 2020, arXiv:2012.00742, https://arxiv.org/abs/2012.00742.
- T. Mansour, R. Rastegar and A. Roitershtein, *Finite automata, probabilistic method, and occurrence enumeration of a pattern in words and permutations*, publicly posted May 14, 2019, arXiv:1905.05646, https://arxiv.org/abs/1905.05646.
- T. Mansour and R. Rastegar, *Pattern occurrences in k-ary words revisited: a few new and old observations*, publicly posted January 31, 2021, arXiv:2102.00443, https://arxiv.org/abs/2102.00443.
- V. Jelínek, T. Mansour, J. L. Ramírez and M. Shattuck, *Avoiding a pair of patterns in multisets and compositions*, publicly posted November 11, 2021, arXiv:2111.06185, https://arxiv.org/abs/2111.06185.
- A. L. Rukhin, *Joint Distribution of Pattern Frequencies and Multivariate Polya-Aeppli Law*, published January 14, 2010, https://www.nist.gov/publications/joint-distribution-pattern-frequencies-and-multivariate-polya-aeppli-law.
