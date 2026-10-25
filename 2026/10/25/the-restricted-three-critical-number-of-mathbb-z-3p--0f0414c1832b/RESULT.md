# The restricted three-critical number of \(\mathbb Z_{3p}\)

## Finding

For every prime \(p\ge 7\) with \(p\equiv1\pmod3\),
\[
\widehat{\chi}(\mathbb Z_{3p},3)=p+3.
\]
Here \(\widehat{\chi}(G,3)\) is the least integer \(m\) such that every \(m\)-element subset of \(G\) has every element of \(G\) as a sum of three pairwise distinct elements.

## Assumptions and scope

Let \(p\) be prime, \(p\ge7\), and \(p\equiv1\pmod3\). The Chinese remainder theorem identifies \(\mathbb Z_{3p}\) with \(\mathbb Z_3\times\mathbb F_p\). For \(B\subseteq\mathbb F_p\), write
\[
h^{\wedge}B=\{b_1+\cdots+b_h:b_1,\ldots,b_h\in B\text{ pairwise distinct}\}.
\]
The proof uses the Cauchy–Davenport theorem and the Dias da Silva–Hamidoune bound
\[
|h^{\wedge}B|\ge\min\{p,h|B|-h^2+1\}.
\]
No conclusion is asserted for other group orders or for primes outside the stated congruence class.

## Proof

**Lower bound.** Put \(a=(p+2)/3\), an integer because \(p\equiv1\pmod3\), and let \(I=\{0,1,\ldots,a-1\}\subseteq\mathbb F_p\). In \(\mathbb Z_3\times\mathbb F_p\), define
\[
A=\bigcup_{r\in\mathbb Z_3}(\{r\}\times I).
\]
Then \(|A|=3a=p+2\). A sum of three elements of \(A\) whose first coordinate is \(1\) must use two elements from some class \(r\) and one from class \(r+1\). The two second coordinates from class \(r\) are distinct, so the second coordinate of the sum is an integer between
\[
0+1+0=1\quad\text{and}\quad(a-2)+(a-1)+(a-1)=3a-4=p-2.
\]
There is no wraparound modulo \(p\) in this interval. Thus neither \((1,0)\) nor \((1,p-1)\) belongs to the restricted triple sumset of \(A\), so \(A\) does not cover the group. Consequently \(\widehat{\chi}(\mathbb Z_{3p},3)\ge p+3\).

**Upper bound.** Let \(A\subseteq\mathbb Z_3\times\mathbb F_p\) have size \(p+3\). For \(i\in\mathbb Z_3\), write
\[
B_i=\{x\in\mathbb F_p:(i,x)\in A\},\qquad a_i=|B_i|.
\]
Then \(0\le a_i\le p\) and \(a_0+a_1+a_2=p+3\). At most one \(B_i\) is empty.

First suppose all three are nonempty. Cauchy–Davenport gives
\[
|B_0+B_1+B_2|\ge\min\{p,a_0+a_1+a_2-2\}=p,
\]
so every second coordinate occurs in first-coordinate class \(0\), using one element from each class of \(A\). Fix \(t\in\{1,2\}\). There is an index \(i\) with \(a_i>a_{i+2}\) if \(t=1\), and an index \(i\) with \(a_i>a_{i+1}\) if \(t=2\), with indices taken modulo \(3\). Otherwise the corresponding cyclic chain of inequalities would force \(a_0=a_1=a_2\), impossible because their sum \(p+3\) is not divisible by \(3\). Set \(j=i+t\pmod3\), and let \(k\) be the remaining index. Then \(a_i>a_k\), hence
\[
2a_i+a_j-4=(a_i+a_j+a_k)+(a_i-a_k)-4\ge p.
\]
The Dias da Silva–Hamidoune bound gives \(|2^{\wedge}B_i|\ge\min\{p,2a_i-3\}\). If this size is already \(p\), adding \(B_j\) preserves full coverage. Otherwise Cauchy–Davenport yields
\[
|2^{\wedge}B_i+B_j|\ge\min\{p,|2^{\wedge}B_i|+a_j-1\}
\ge\min\{p,2a_i+a_j-4\}=p.
\]
These sums use two distinct elements from class \(i\) and one from class \(j\), so they cover every second coordinate in first-coordinate class \(t\). This proves coverage of all three classes when all \(B_i\) are nonempty.

Now suppose exactly one class, say \(B_k\), is empty. Let \(i,j\) be the other two indices. Then \(a_i+a_j=p+3\), so both \(a_i,a_j\ge3\). The two nonzero first-coordinate classes are filled by \(2^{\wedge}B_i+B_j\) and \(B_i+2^{\wedge}B_j\), respectively: for example,
\[
2a_i+a_j-4=(a_i+a_j)+a_i-4=p+a_i-1\ge p,
\]
and the same bound holds with \(i,j\) reversed. Applying the same restricted-pair bound and Cauchy–Davenport therefore gives all \(p\) second coordinates in each of those classes.

For first-coordinate class \(0\), put \(M=\max(a_i,a_j)\). Since \(a_i+a_j=p+3\), we have \(M\ge(p+3)/2\), and hence
\[
3M-8\ge\frac{3p-7}{2}\ge p
\]
for \(p\ge7\). The Dias da Silva–Hamidoune bound with \(h=3\) now gives \(|3^{\wedge}B_{\ell}|=p\) for a class \(\ell\) of size \(M\). Its three-term sums have first coordinate \(0\) and cover that entire class. Two empty classes are impossible because \(|A|=p+3>p\). Thus every \((p+3)\)-element subset has full restricted triple sumset, proving \(\widehat{\chi}(\mathbb Z_{3p},3)\le p+3\).

Combining the two bounds proves the claim.

## Verification

The proof separates all possible fiber-size patterns: three nonempty fibers or exactly one empty fiber. The only analytic inputs are Cauchy–Davenport and the Dias da Silva–Hamidoune inequality with \(h=2,3\); the numerical thresholds used above are \(2a_i+a_j-4\ge p\) and \(3M-8\ge p\). A finite sanity check verified the explicit obstruction for \(p=7,13,19,31\) and sampled 300 subsets of size \(p+3\) for each of those primes; these experiments are not used as proof of the infinite statement.

## Relationship to prior work

Bajnok’s 2014 preprint formulates a conjectured exact value for the restricted three-critical number of \(\mathbb Z_n\), and identifies the lower-bound regime relevant here: \(n\) has no prime divisor congruent to \(2\pmod3\) and \(9\nmid n\). For \(n=3p\) with \(p\equiv1\pmod3\), that prediction is \(p+3\). The preprint records prime and even orders as known cases and reports finite verification only through \(n\le50\); it does not give this infinite odd-composite family. The lower-bound construction above is explicit, and the upper bound is supplied here by a three-fiber argument using the prime-field restricted-sumset theorem.

The 2026 preprint by Chen and Huang gives broader density bounds for odd-order groups, rather than an exact formula for this family; its general bound is weaker than \(p+3\) for \(p\ge13\). A 2023 Kneser-type theorem concerns lower bounds for restricted two-set sums under general restrictions, not an explicit three-critical-number formula. The latter paper’s full text was not accessible, so that comparison remains a residual literature risk.

## Limitations

The theorem applies only to cyclic groups of order \(3p\) with prime \(p\equiv1\pmod3\), \(p\ge7\). It does not settle Bajnok’s conjecture for arbitrary odd composite orders. The literature search was not exhaustive; an unindexed result specifically covering this family could exist. No independent audit has been performed.

## References

1. B. Bajnok, “The \(h\)-critical number of finite abelian groups,” arXiv:1412.4058v1, submitted 2014-12-12, Section 7.
2. B. Bajnok, “On the minimum size of restricted sumsets in cyclic groups,” arXiv:1305.2141v2; *Acta Mathematica Academiae Scientiarum Hungaricae* 148 (2016), 228–256, DOI 10.1007/s10474-015-0546-1.
3. J. A. Dias da Silva and Y. O. Hamidoune, “Cyclic spaces for Grassmann derivatives and additive theory,” *Bulletin of the London Mathematical Society* 26 (1994), 140–146, DOI 10.1112/blms/26.2.140.
4. B. Chen and J. Huang, “Critical Numbers for Restricted Sumsets: Rigidity and Collapse in Finite Abelian Groups,” arXiv:2602.10402v1, 2026-02-11.
5. M. Huicochea, “A Kneser-Type Theorem for Restricted Sumsets,” *SIAM Journal on Discrete Mathematics* 37 (2023), 83–93, DOI 10.1137/22M1476150.
6. B. Bajnok, “Corrigendum to the h-Critical Number of Finite Abelian Groups,” DOI 10.1515/udt-2017-0018 (2017).
