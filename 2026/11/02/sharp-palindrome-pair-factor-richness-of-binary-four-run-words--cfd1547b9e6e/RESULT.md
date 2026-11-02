# Sharp palindrome-pair factor richness of binary four-run words

## Finding
For every integer \(n\ge 8\), among all binary words of length \(n\) consisting of exactly four maximal constant-letter runs, the largest number \(Q(w)\) of **distinct contiguous factors** that are products of at most two palindromes, **including the empty factor once**, is
\[
\boxed{\max_{\substack{|w|=n\\\operatorname{runs}(w)=4}}Q(w)=\left\lceil\frac{n^2+n+9}{3}\right\rceil.}
\]
This bound is attained for every \(n\ge8\) by explicit words given below. In contrast, a three-run binary word exists at every such length with
\[
Q(w)=\left\lceil\frac{n^2+2n+3}{3}\right\rceil,
\]
so the exact difference between the best three-run construction and the four-run maximum is \(\lceil(n-7)/3\rceil>0\). This does **not** assert that the three-run value is the global maximum among arbitrary binary words.

## Assumptions and scope
A *factor* is a contiguous substring of a finite linear word; factors with the same letters are counted only once. The empty factor \(\varepsilon\) is counted once. A palindrome is a word equal to its reversal, with \(\varepsilon\) allowed. A *palindrome pair* is a concatenation of two palindromes, possibly with an empty part. A *run* is a maximal contiguous block of equal letters. By exchanging the binary letters if necessary, every four-run word has the form
\[
w=0^a1^b0^c1^d,\qquad a,b,c,d\in\mathbb Z_{\ge1},\qquad a+b+c+d=n.
\]
The exponent notation in this display counts repeated literal symbols, not arithmetic powers. The result is for four runs and \(n\ge8\), without circular wrapping or factor multiplicity.

## Proof
**1. Factor classification.** Every factor with at most three runs is a palindrome pair: for a three-run factor \(0^x1^y0^z\), take a palindromic block encompassing the full middle run and matching \(\min(x,z)\) symbols on each side, and leave the unmatched end symbols as a constant palindrome. The two-run and one-run cases are immediate.

For four runs, a factor necessarily has the form \(0^x1^b0^c1^y\), with \(1\le x\le a\) and \(1\le y\le d\). Such a factor is a palindrome pair **if and only if** \(x=c\) or \(y=b\). Indeed, splitting after the first run makes the suffix \(1^b0^c1^y\) palindromic exactly when \(y=b\); splitting after the third run makes the prefix \(0^x1^b0^c\) palindromic exactly when \(x=c\). Any other split leaves a nonempty piece whose first and last symbols disagree. Thus the number of four-run factors that are palindrome pairs equals
\[
d\mathbf1_{c\le a}+a\mathbf1_{b\le d}-\mathbf1_{c\le a}\mathbf1_{b\le d}.
\]

The distinct one-run factors number \(\max(a,c)+\max(b,d)\). The two-run factors number \(ab+cd-\min(a,c)\min(b,d)+bc\), by counting two types of transitions and removing duplicated factors in the two \(0\)-to-\(1\) boundary rectangles. The three-run factors number \(ac+bd\). Counting \(\varepsilon\) gives the exact identity
\[
\begin{aligned}
Q(0^a1^b0^c1^d)={}&1+\max(a,c)+\max(b,d)\\
&+ab+cd-\min(a,c)\min(b,d)+bc+ac+bd\\
&+d\mathbf1_{c\le a}+a\mathbf1_{b\le d}-\mathbf1_{c\le a}\mathbf1_{b\le d}.
\end{aligned}
\tag{1}
\]
All counted categories are disjoint by their number and orientation of runs.

**2. Uniform upper bound.** Write \(G(n)=\lceil(n^2+n+9)/3\rceil\). We distinguish three exhaustive cases, using reversal followed by bit complementation (which preserves \(Q\)) to handle the mirrored case.

If \(a\ge c\) and \(b\le d\), (1) reduces to
\[
Q=(a+d)(b+c+2)\le\frac{(n+2)^2}{4}<\frac{n^2+n+9}{3}\le G(n).
\]
The strict inequality follows from \(n^2-8n+24=(n-4)^2+8>0\).

If \(a\ge c\) and \(b>d\), (1) reduces to
\[
Q=1+n+b(n-b)+c(a-1).
\]
Since \(a+c=n-b-d\le n-b-1\), and \(c(a-1)\le(a+c-1)^2/4\), setting \(u=n-b\) yields
\[
Q\le n+2+(n-1)u-\frac{3u^2}{4}
\le\frac{n^2+n+7}{3}<\frac{n^2+n+9}{3}\le G(n).
\]
The case \(a<c\) and \(b\le d\) is the image of this case under the symmetry \((a,b,c,d)\mapsto(d,c,b,a)\).

The remaining case is \(a<c\) and \(b>d\). With \(x=b+c\) and \(t=a+d=n-x\), (1) becomes
\[
Q=1+x(t+1)+bc-ad.
\]
Because \(bc\le x^2/4\) and \(ad\ge t-1\) for positive integers \(a,d\),
\[
Q\le 2-n+(n+2)x-\frac{3x^2}{4}
\le\frac{n^2+n+10}{3}.
\]
As \(Q\) is an integer and \(n^2+n\equiv 0,2\pmod3\), this last inequality gives
\[
Q\le\left\lfloor\frac{n^2+n+10}{3}\right\rfloor=G(n).
\]
This completes the all-length upper bound.

**3. Sharpness.** The following positive quadruples \((a,b,c,d)\) all have sum \(n\), satisfy \(a<c\) and \(b>d\), and attain \(Q=G(n)\) by (1):
\[
\begin{array}{c|c|c}
 n & (a,b,c,d)&\text{range}\\ \hline
3m&(1,m,m+1,m-2)&m\ge3\\
3m+1&(1,m+1,m+1,m-2)&m\ge3\\
3m+2&(1,m+1,m+1,m-1)&m\ge2
\end{array}
\]
They cover every \(n\ge8\).

**4. Three-run benchmark and strict gap.** Every factor of \(0^a1^b0^c\) has at most three runs and hence is a palindrome pair. Its distinct-factor count, including \(\varepsilon\), is exactly
\[
1+\max(a,c)+b+ab+bc+ac.
\]
Choosing \((a,b,c)=(m,m,m)\) at \(n=3m\), \((m,m,m+1)\) at \(n=3m+1\), and \((m,m+1,m+1)\) at \(n=3m+2\) gives \(H(n)=\lceil(n^2+2n+3)/3\rceil\). Direct residue-class subtraction yields \(H(n)-G(n)=\lceil(n-7)/3\rceil\) for every \(n\ge8\). This establishes the claimed strict separation without presuming an unrestricted global optimum.

## Verification
The standalone `verify.py` implements (1) and independently enumerates distinct factors and tests all palindrome splits, rather than using the run-classification formula. It checks every four-run composition at lengths \(4\) through \(16\), every three-run composition at lengths \(3\) through \(17\), every four-run maximum at lengths \(8\) through \(75\), and explicit witnesses and benchmark gaps through length \(299\). A complete replay returned `VERIFY_OK`, including 2,500 definition-level comparisons and 1,215,415 parameter-level comparisons. These computations check finite instances; the proof above establishes the unbounded claim.

## Relationship to prior work
Borchert and Rampersad (2015), Section 4, conjectured the unrestricted binary length-\(n\) maximum \(H(n)\) and described three-run candidate maximizers, while explicitly leaving the global extremal problem unsolved. Their Lemma 13 establishes that words with at most three blocks are palindrome pairs. The present result is **not** a proof of that global conjecture: it solves the complete four-run competitor class and quantifies a growing separation from the three-run benchmark.

Guo, Shallit and Shur (2015), Section 3, characterize individual palindrome pairs by conjugacy with reversal and enumerate classes of palindrome pairs of a given length. This includes a general individual-word membership criterion, but neither that census nor their rich-word bounds state an extremum for distinct palindrome-pair *factors within one four-run word*. Formula (1) explicitly counts distinct factors and is optimized here over all positive run parameters.

## Limitations
The four-run extremum holds for \(n\ge8\) only. It does not classify all maximizing four-run parameter quadruples, nor establish the extremum among words having five or more runs. The cited global maximum is a conjectural benchmark, not used as a theorem. The originality comparison is based on inspected relevant primary sources and database searches; overlooked literature remains possible. No independent audit or certification is claimed.

## References
1. A. Borchert and N. Rampersad, *Words with many palindrome pair factors*, arXiv:1509.05396v1 (first public posting September 17, 2015), Section 4 and Lemma 13. https://arxiv.org/abs/1509.05396
2. C. Guo, J. Shallit and A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112v1 (March 31, 2015), Section 3, especially Proposition 5. https://arxiv.org/abs/1503.09112
3. A. E. Frid, S. Puzynina and L. Q. Zamboni, *On minimal factorizations of words as products of palindromes*, arXiv:1210.6179 (October 23, 2012), background on palindromic length. https://arxiv.org/abs/1210.6179
