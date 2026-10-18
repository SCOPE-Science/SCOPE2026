# Sharp fixed-length Zumkeller-sum thresholds

## Finding
A positive integer is **Zumkeller** if its set of positive divisors can be divided into two disjoint sets whose sums coincide. Let \(Z\) be the set of all such integers. For \(k\ge3\), write
\[
G_k=\max\{N\in\mathbb Z_{\ge0}:N\ne z_1+\cdots+z_k\text{ for every }z_1,\ldots,z_k\in Z\}.
\]
The maximum exists, and the exact answer is
\[
\boxed{G_3=983,\qquad G_k=6k+955\quad (k\ge4).}
\]
The representations use **exactly** \(k\) positive summands; repeated summands are permitted. Each endpoint is genuinely excluded, and every greater integer has a representation.

## Assumptions and scope
The assertion applies to all integers \(k\ge3\), with no computational upper bound. We use the published theorem of Somu, Kukla and Tran [1, Proposition 4.6(a)] that every even integer at least \(40\) is a sum of two Zumkeller numbers, whereas \(38\) is not. No assertion about the greatest nonrepresentable integer for \(k=1\) or \(k=2\) is made. The study concerns additive sums of Zumkeller integers, not partitions of the divisors of one integer into several equal-sum parts (the separate notion of a layered integer).

## Proof
**1. Necessary size and small divisors.** If \(n\) is Zumkeller, its divisor sum \(\sigma(n)\) satisfies \(\sigma(n)\ge2n\): one of the two equal-sum parts contains \(n\) and has sum \(\sigma(n)/2\). Direct divisor checks give that the Zumkeller integers below \(24\) are exactly \(6,12,20\). In particular, the even Zumkeller integers no larger than \(22\) are \(6,12,20\). The numbers \(6,12,20,24,28,30,945\) are all Zumkeller, witnessed respectively by half-sum subsets \(\{6\}\), \(\{12,2\}\), \(\{20,1\}\), \(\{24,6\}\), \(\{28\}\), \(\{30,6\}\), \(\{945,15\}\). Their divisor sums are, respectively, \(12,28,42,60,56,72,1920\).

**2. Small odd Zumkeller integers.** We show that \(945\) is the only odd Zumkeller integer not exceeding \(971\). Let \(n\) be odd, \(1\le n\le971\), with \(\sigma(n)\ge2n\). For each prime power \(p^e\parallel n\),
\[
\frac{\sigma(p^e)}{p^e}=1+p^{-1}+\cdots+p^{-e}<\frac{p}{p-1}.
\]
If \(3\nmid n\), there can be at most three distinct prime factors, since \(5\cdot7\cdot11\cdot13>971\), whence \(\sigma(n)/n<(5/4)(7/6)(11/10)<2\). If \(3\mid n\) and there are at most two distinct primes, the ratio is below \((3/2)(5/4)<2\). At least four distinct primes would imply \(n\ge3\cdot5\cdot7\cdot11>971\). Thus \(n=3^a p^b q^c\), with \(5\le p<q\) odd primes and positive exponents. When \(a=1\), the ratio is less than \((4/3)(5/4)(7/6)<2\). When \(a=2\), the size bound forces \(b=c=1\), so the ratio is at most \((13/9)(6/5)(8/7)<2\). When \(a\ge4\), \(n\ge3^4\cdot5\cdot7>971\). Finally, when \(a=3\), the size bound forces \(p=5,q=7,b=c=1\), giving exactly \(n=945\). The half-sum subset \(\{945,15\}\) shows that this integer really is Zumkeller. Therefore
\[
Z\cap(2\mathbb Z+1)\cap[1,971]=\{945\}.
\]

**3. The three-summand threshold.** If \(N\ge984\) is even, then \(N=6+(N-6)\) and the even remainder is at least \(978\), hence is a sum of two Zumkeller numbers by [1]. If \(N\ge985\) is odd, then \(N=945+(N-945)\) and its even remainder is at least \(40\), again covered by [1]. Hence all \(N\ge984\) have three summands. But \(983\) does not: an odd representation with three summands has at least one odd summand, and three odd summands alone total at least \(3\cdot945>983\). With exactly one odd summand, the other two are at least \(6\) each, so that odd term is no greater than \(971\) and is therefore \(945\). The remaining \(38\) is not a sum of two Zumkeller numbers [1]. Thus \(G_3=983\).

**4. The four-summand threshold.** Every even \(N\ge980\) equals \(6+6+(N-12)\), with the even remainder \(N-12\ge968\) a sum of two Zumkeller numbers by [1]. Every odd \(N\ge991\) equals \(6+(N-6)\), where \(N-6\ge985\) is a sum of three by step 3. The five omitted odd values have the following four-summand representations:
\[
\begin{aligned}
981&=945+6+6+24,\\
983&=945+6+12+20,\\
985&=945+6+6+28,\\
987&=945+6+6+30,\\
989&=945+12+12+20.
\end{aligned}
\]
Consequently all \(N\ge980\) admit exactly four summands.

**5. One uniform sharp obstruction.** For any integer \(k\ge4\), put \(T_k=6k+955\). Suppose \(T_k\) were a sum of \(k\) positive Zumkeller integers. As \(T_k\) is odd, at least one summand is odd. Since all others are at least \(6\), an odd summand is at most \(T_k-6(k-1)=961\), and by step 2 it must equal \(945\). There cannot be three or more odd summands, since they contribute at least \(3\cdot945+6(k-3)=6k+2817>T_k\). Thus precisely one summand equals \(945\), and the other \(k-1\) summands \(y_1,\ldots,y_{k-1}\) are even and satisfy
\[
\sum_{j=1}^{k-1}(y_j-6)=T_k-945-6(k-1)=16.
\]
Every summand here has \(0\le y_j-6\le16\), so step 1 forces \(y_j-6\in\{0,6,14\}\). No nonnegative combination of \(6\) and \(14\) is \(16\), a contradiction. Hence \(T_k\) is not representable for every \(k\ge4\); in particular \(979=T_4\) is not a four-term sum.

**6. Induction for all lengths.** Step 4 proves every integer greater than \(T_4=979\) has four summands. If every \(N>T_k\) has \(k\) summands, any integer \(M>T_{k+1}=T_k+6\) satisfies \(M=6+(M-6)\), with \(M-6>T_k\), and therefore has \(k+1\) summands. This induction, combined with step 5, proves \(G_k=T_k\) for every \(k\ge4\). \(\square\)

## Verification
Run the standalone standard-library script `python3 verify.py`, supplied with this finding. It constructs every Zumkeller number through \(4000\) from exact proper-divisor subset sums, checks the even two-sum premise on the finite interval \(40\) through \(4000\), tests fixed-length representation thresholds for \(3\le k\le30\), confirms all five four-summand witnesses, and verifies the odd necessary abundance bound through \(971\). The recorded output is in `verification_output.txt`. The proof, not the finite experiment, establishes the claims for all integers in the stated ranges.

## Relationship to prior work
Somu, Kukla and Tran [1, Proposition 4.6(a)] prove the complete **two-summand** classification for even targets, which is explicitly used as a premise here. Their Section 5 proposes study of sums of three or four Zumkeller numbers. Their results supply convenient upper bounds but not the sharp three- and four-term thresholds, the odd obstruction \(983\), or the all-length affine formula proved here. Bhaskara Rao and Peng [2] establish structural properties of the underlying Zumkeller set. The OEIS [3,4,5] records members of the set, odd abundant numbers, and two-sum exceptions, rather than this exact fixed-length threshold law. The divisor-partition notion of \(k\)-layered numbers is a different object, not a formula for sums of \(k\) Zumkeller integers.

## Limitations
This argument uses an established published two-summand theorem [1], not an independently reconstructed proof of that theorem. It proves existence and sharp largest gaps, not the number of fixed-length representations or a classification of all smaller gaps. The computation only tests finitely many cases. There may be equivalent results in literature not discovered by targeted searches; originality is assessed relative to the identified works and tables, not certified independently.

## References
[1] S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149, v1 first public 22 October 2023; Proposition 4.6 and Section 5; https://arxiv.org/pdf/2310.14149.

[2] K. P. S. Bhaskara Rao and Y. Peng, *On Zumkeller Numbers*, arXiv:0912.0052; https://arxiv.org/pdf/0912.0052.

[3] OEIS A083207, Zumkeller numbers; https://oeis.org/A083207.

[4] OEIS A005231, odd abundant numbers; https://oeis.org/A005231.

[5] OEIS A368007, integers not expressible as sums of two Zumkeller numbers; https://oeis.org/A368007.
