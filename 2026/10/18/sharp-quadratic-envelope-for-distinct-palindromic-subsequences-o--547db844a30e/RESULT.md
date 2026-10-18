# Sharp quadratic envelope for distinct palindromic subsequences of three-marker binary words

## Finding

For every quadruple of nonnegative integers \(a,b,c,d\), let
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad z=a+b+c+d.
\]
Let \(P(w)\) be the number of **distinct nonempty palindromic scattered subsequences** of \(w\), with each resulting binary word counted once regardless of how many embeddings it has. Put
\[
H=\max\{\min(a,b+c+d),\min(a+b,c+d),\min(a+b+c,d)\}
\]
and define
\[
T=\begin{cases}
(a+1)(b+c+1)+\min(b,d-a)(c+1),&a\le d,\\
(d+1)(b+c+1)+\min(c,a-d)(b+1),&a\ge d.
\end{cases}
\]
The two definitions of \(T\) coincide when \(a=d\). Then the **complete all-gap enumeration** is
\[
\boxed{P(w)=z+H+1+T+(\min(a,d)+1)(\min(b,c)+1).}
\tag{1}
\]
Further, for every integer \(z\ge0\),
\[
\boxed{\max_{a+b+c+d=z}P(0^a1\,0^b1\,0^c1\,0^d)
=\frac{3}{16}z^2+O(z).}
\tag{2}
\]
The implied constant is absolute. In fact every such word satisfies
\[
P(w)\le\frac{3}{16}z^2+3z+3,
\tag{3}
\]
while \(P(0^t1\,0^t1\,0^t1\,0^t)=3t^2+11t+3\) for every \(t\ge0\). **Asymptotic rigidity:** if \((a_z,b_z,c_z,d_z)\) is any maximizing quadruple with sum \(z\), then
\[
\frac{a_z}{z},\frac{b_z}{z},\frac{c_z}{z},\frac{d_z}{z}\longrightarrow\frac14
\quad(z\to\infty).
\tag{4}
\]
Equation (1) also gives an explicit description of the entire palindrome-subsequence spectrum by the number of ones, as detailed in the proof.

## Assumptions and scope

The alphabet is \(\{0,1\}\); the source has **exactly three** occurrences of \(1\); the four zero gaps may vanish. Subsequence means deletion without reordering, rather than a contiguous factor or cyclic factor. The empty word is excluded. Formula (1) holds including \(z=0\), when \(w=111\) and \(P(w)=3\). Equations (2)–(4) concern the maximum over **all labeled linear words** of length \(z+3\) with three ones, not over rotations or dihedral classes.

## Proof

### Classification and exact counting

Every palindromic scattered subsequence contains zero, one, two, or three ones. These four sets are disjoint.

With no ones the possibilities are exactly \(0^j\), \(1\le j\le z\), giving \(z\) words. With one one they have the form \(0^i1 0^i\). If the one is the first, second, or third marked position, the largest feasible \(i\) is, respectively,
\[
\min(a,b+c+d),\quad\min(a+b,c+d),\quad\min(a+b+c,d).
\]
Their union therefore consists of exactly \(H+1\) words.

With two ones each palindrome is uniquely represented as \(0^i1 0^j1 0^i\), where \(i,j\ge0\). Selecting the first and second ones permits
\[
0\le i\le\min(a,c+d),\quad0\le j\le b;
\]
selecting the first and third permits
\[
0\le i\le\min(a,d),\quad0\le j\le b+c;
\]
and selecting the second and third permits
\[
0\le i\le\min(a+b,d),\quad0\le j\le c.
\]
These three rectangles specify the **complete two-one spectrum**. If \(a\le d\), the first \(a+1\) rows \(0\le i\le a\) are supplied fully by the first/third pair, with \(b+c+1\) possible \(j\)'s per row. Beyond \(i=a\), only the second/third pair can contribute. It supplies \(\min(b,d-a)\) further rows, each of width \(c+1\). Their total is precisely the first case of \(T\). If \(a\ge d\), reverse the word, interchanging \((a,b,c,d)\) with \((d,c,b,a)\), to obtain the second case.

With three ones every palindrome has the unique form
\[
0^i1\,0^j1\,0^j1\,0^i
\]
with independent ranges \(0\le i\le\min(a,d)\) and \(0\le j\le\min(b,c)\). This contributes \((\min(a,d)+1)(\min(b,c)+1)\) words. Adding the four disjoint counts proves (1), including every zero-gap boundary.

### Sharp quadratic extremal coefficient

Reversal does not alter \(P\), so assume \(a\le d\) and write \(h=d-a\ge0\), \(p=b+c\), \(m=\min(b,c)\), and \(t=\min(b,h)\). The degree-two part of (1) is
\[
Q=a(b+c+m)+tc,\qquad z=2a+b+c+h.
\tag{5}
\]
We prove the **homogeneous sharp inequality**
\[
Q\le\frac{3}{16}z^2,
\tag{6}
\]
with equality for \(z>0\) only at \(a=b=c=d=z/4\). It is enough to optimize over nonnegative real gap lengths, since the integer domain is contained therein.

If \(h\ge b\), the expression in (5) is independent of \(h\), except through \(a\) under fixed \(z,b,c\). Decreasing \(h\) to \(b\) and increasing \(a\) by \((h-b)/2\) cannot decrease \(Q\). It thus suffices to examine \(h=b\). If \(b\le c\), then \(z=2a+2b+c\) and
\[
Q=2ab+(a+b)c\le\frac12(a+b)^2+(a+b)c
\le\frac16 z^2.
\]
The last inequality follows by setting \(u=a+b\), \(c=z-2u\) and maximizing \(zu-3u^2/2\).

If instead \(h=b\ge c\), set \(e=b-c\ge0\). Here \(Q=a(b+2c)+bc\) and direct expansion gives the nonnegative certificate
\[
3z^2-16Q
=12(a-c/2)^2+8c^2+8ae+20ce+12e^2.
\tag{7}
\]
This is strictly positive whenever \(z>0\), so the case \(h\ge b\) does not attain the upper bound.

Now assume \(0\le h\le b\). Fix \(z,b,c\) and substitute \(a=(z-b-c-h)/2\) into (5). If \(b\ge c\), then
\[
Q=a(b+2c)+hc
\]
is nonincreasing in \(h\), with slope \(-b/2\). Its maximum occurs at \(h=0\); writing \(a'=(z-b-c)/2\), the inequalities \(b+2c\le3(b+c)/2\) and \(2a'+b+c=z\) yield
\[
Q\le\frac32a'(b+c)\le\frac3{16}z^2.
\]
If \(b\le c\), then \(Q=a(2b+c)+hc\) is affine in \(h\), with slope \(c/2-b\). For a nonpositive slope its maximum is again at \(h=0\) and follows from \(2b+c\le3(b+c)/2\). For positive slope, the maximum occurs at the opposite endpoint of \(0\le h\le\min\{b,z-b-c\}\). Either \(h=b\), already bounded above by \(z^2/6\), or \(a=0\). In the latter case \(Q=hc\) and \(h\le b\) implies \(c\le z-2h\); hence
\[
Q\le h(z-2h)\le z^2/8.
\]
All cases prove (6). Equality in the only potentially sharp case requires \(h=0\), \(b=c\), and \(2a=b+c=z/2\), giving \(a=b=c=d=z/4\).

The exact formula yields
\[
P=Q+z+H+2a+p+m+t+3.
\]
Since \(H\le z/2\), \(m\le z/2\), and \(2a+p+t\le z\), we obtain (3). At \(a=b=c=d=t\), direct substitution into (1) gives \(3t^2+11t+3\). For arbitrary \(z\), take \(t=\lfloor z/4\rfloor\) and append the remaining zero symbols to this balanced word. Appending symbols never removes a scattered subsequence, so this supplies the lower bound \(3z^2/16-O(z)\). Equation (2) follows.

Finally, normalized quadruples belong to the compact simplex of nonnegative reals with sum one. The bound \(0\le P-Q\le3z+3\) is uniform. A maximizing quadruple must therefore satisfy \(Q/z^2\to3/16\). Every convergent subsequence of normalized maximizing quadruples attains equality in (6), whose only maximizer is the all-quarter point. This proves (4).

## Verification

The companion `verify.py` reconstructs every word with \(0\le z\le17\) and exactly three ones, compares (1) to an independent interval dynamic program for **distinct palindromic subsequences**, and additionally forms literal subsequence sets for \(0\le z\le8\). It also checks 300 randomly chosen larger gap quadruples and enumerates the finite extremal counts for \(0\le z<75\). The reported result is `VERIFY_OK exhaustive_gap_tuples=5985 raw_subsequence_cases=495 random_cases=300 envelope_scans=75`. These finite computations corroborate (1); the infinite statements (1)–(4) are justified by the preceding proof, not by extrapolation.

To reproduce: run `python verify.py` using a standard Python 3 interpreter; no nonstandard packages or external datasets are required.

## Relationship to prior work

Chowdhury, Hasan, Iqbal, and Rahman (2011) introduced algorithms for *longest common palindromic subsequences* of two strings. General dynamic programming also permits counting all distinct palindromic subsequences of an arbitrary fixed word. Neither fact gives, by itself, the uniform all-gap classification (1), the sharp sparse-class extremal coefficient (2), or the rigidity law (4). General palindromic-*factor* complexity counts contiguous substrings, a different invariant from the scattered subsequences counted here.

The structural contribution is the exact union-of-three-rectangles representation for the two-one layer and the sharp four-gap continuous extremal inequality (6). Broad algorithmic computability, the ordinary palindrome definition, and any existing general dynamic-programming recurrences are not claimed as new.

## Limitations

No exact finite-length formula for the global maximum or complete finite-length extremizer list is claimed. The error term in (2) is not optimized, and (4) does not provide a finite-length stability constant. Higher fixed numbers of ones, arbitrary alphabets, palindromic *factors*, and cyclic sources are not classified. Exhaustive finite checks cannot certify the absence of an equivalent theorem in unindexed literature; independent validation has not been performed.

## References

1. S. R. Chowdhury, M. M. Hasan, S. Iqbal, and M. S. Rahman, *Computing a Longest Common Palindromic Subsequence*, arXiv:1110.5296v1, first posted 2011-10-24; full text at https://arxiv.org/html/1110.5296v1 .
2. *Count Different Palindromic Subsequences*, general dynamic-programming problem and solution, https://leetcode.doocs.org/en/lc/730/ ; consulted as algorithmic background, not as a dated research priority claim.
