# Antisquare-factor spectrum and sharp extremizers for four-run binary words

## Finding

Let \(w=0^a1^b0^c1^d\), where \(a,b,c,d\ge 1\) are integers and \(n=a+b+c+d\). An *antisquare* is a nonempty factor of the form \(u\overline u\), where \(\overline u\) is the binary complement of \(u\). Distinct antisquare strings, not occurrences, are counted. Put \([z]_+=\max\{z,0\}\) and define

\[
\begin{aligned}
R&=\max\{\min(a,b),\min(c,d)\},\\
S&=\min(b,c),\\
U&=[\min(a,b-1)-\max(1,b-c)+1]_+,\\
V&=[\min(b,c-1)-\max(1,c-d)+1]_+.
\end{aligned}
\]

The exact number \(C(w)\) of distinct nonempty antisquare factors is

\[C(w)=R+S+U+V.\]

Every such factor is one of four disjoint types: \(0^t1^t\) with \(1\le t\le R\); \(1^t0^t\) with \(1\le t\le S\); \(0^p1^b0^q\) with \(p,q\ge1\), \(p\le a\), \(q\le c\), and \(p+q=b\); or \(1^p0^c1^q\) with \(p,q\ge1\), \(p\le b\), \(q\le d\), and \(p+q=c\).

For every such word, \(C(w)\le n-1\), and equality holds **exactly** for the union of these two families:

\[
\begin{array}{ll}
\mathrm{I}:& a,c\in\{b-1,b\},\quad 1\le d<c,\\
\mathrm{II}:& b,d\in\{c-1,c\},\quad 1\le a<b.
\end{array}
\]

Consequently the maximum over four-run binary words of length \(n\) is \(n-2\) for \(n=4,5\), and \(n-1\) for every \(n\ge6\). Complementing the starting symbol leaves all counts unchanged.

If a four-run word of length \(n\) is chosen uniformly (equivalently, choose a positive composition of \(n\) into four parts uniformly, and choose either starting symbol), then

\[\mathbb E[C(w)]=\frac{7n}{16}+O(1)\qquad(n\to\infty).\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Factors are contiguous; the two halves of an antisquare are complementary coordinatewise and have equal positive length. The four maximal constant runs are nonempty, and no wraparound factors are considered. Counts identify equal factor strings occurring at different locations. The expectation is over all words with precisely four maximal constant runs of the prescribed total length, not over all binary words.

## Proof

**1. Exhaustive types.** A prior run-parity observation for antisquares (Baranwal et al., Lemma 14) says that an antisquare has a number of constant runs congruent to \(2\) or \(3\) modulo \(4\). Thus a factor of a four-run word that is an antisquare has exactly two or three runs. Directly splitting its halves shows that the two-run possibilities are \(0^t1^t\) and \(1^t0^t\), while the three-run possibilities are \(0^p1^{p+q}0^q\) and \(1^p0^{p+q}1^q\), where \(p,q\ge1\). This is exhaustive: a half with one run produces two runs, a half with two produces three, and a half with at least three produces at least six.

**2. Exact factor enumeration.** The \(0^t1^t\) factors can cross the first or third run boundary, and exist for precisely \(1\le t\le\max\{\min(a,b),\min(c,d)\}=R\). The \(1^t0^t\) factors can cross only the second boundary, and exist for precisely \(1\le t\le\min(b,c)=S\). A three-run factor \(0^p1^{p+q}0^q\) necessarily uses the whole second run, so \(p+q=b\), \(1\le p\le a\), \(1\le q\le c\); its distinct possibilities are indexed by integers

\[\max\{1,b-c\}\le p\le\min\{a,b-1\},\]

whose number is \(U\). The other three-run orientation must use the whole third run and is counted by \(V\). These four types cannot duplicate one another, proving the exact formula.

**3. The sharp bound and all equality cases.** Set \(r=\min(a,b)\) and \(s=\min(c,d)\). If \(R=r\ge s\), then

\[r+U\le a+b-1,\qquad S\le c,\qquad V\le d.\]

The first inequality follows from \(U\le\min(a,b-1)\): for \(a<b\) use \(r=a\), and for \(a\ge b\) use \(r=b\). Equality in it holds exactly when \(a\in\{b-1,b\}\) and \(c\ge b-1\). Equality in \(S\le c\) means \(c\le b\). Equality in \(V\le d\) means that every \(q\in\{1,\ldots,d\}\) gives a permitted \(p=c-q\), or equivalently \(d<c\) and \(c-1\le b\). Together these conditions yield Family I; conversely Family I implies \(r\ge s\) and all three equalities.

If \(R=s\ge r\), the reversed charge gives

\[s+V\le c+d-1,\qquad S\le b,\qquad U\le a.\]

Equality in the first inequality means \(d\in\{c-1,c\}\) and \(b\ge c-1\); equality in \(S\le b\) means \(b\le c\); equality in \(U\le a\) means \(a<b\) and \(b-1\le c\). These conditions give precisely Family II and conversely imply \(s\ge r\). Even in a tie \(r=s\), either charge is valid. Therefore the two families are necessary and sufficient for \(C(w)=n-1\).

For \(n=4,5\), direct substitution over the positive compositions gives the maximum \(n-2\). For \(n=6\), \((a,b,c,d)=(1,2,2,1)\) attains \(n-1\). For all \(n\ge7\), write \(n=3k+1,3k+2\), or \(3k+3\), with \(k\ge2\); respectively use

\[(1,k,k,k),\qquad(1,k,k+1,k),\qquad(1,k,k+1,k+1).\]

Each belongs to Family II and attains \(n-1\).

**4. Mean density.** Let \((X_1,X_2,X_3,X_4)\) be uniformly distributed on the simplex of nonnegative coordinates summing to \(1\). Dividing the formula by \(n\), the discrete terms converge uniformly up to error \(O(1/n)\) to the continuous, piecewise-linear homogeneous function

\[
\begin{aligned}
F(x_1,x_2,x_3,x_4)
={}&\max\{\min(x_1,x_2),\min(x_3,x_4)\}+\min(x_2,x_3)\\
&+\big[\min(x_1,x_2)-\max(0,x_2-x_3)\big]_+\\
&+\big[\min(x_2,x_3)-\max(0,x_3-x_4)\big]_+.
\end{aligned}
\]

Uniform positive compositions are a regular three-dimensional simplex lattice. For a Lipschitz function, their normalized grid average differs from the uniform simplex integral by \(O(1/n)\) (partition into grid cells, with a boundary layer of relative size \(O(1/n)\)). Hence \(\mathbb E[C(w)]=n\mathbb E[F(X)]+O(1)\).

For an exact evaluation, let \(A,B,C,D\) be independent rate-one exponential variables, put \(T=A+B+C+D\), and note that \((A,B,C,D)/T\) is uniform on that simplex and independent of \(T\), with \(\mathbb ET=4\). By homogeneity, \(\mathbb EF(X)=\mathbb EF(A,B,C,D)/4\). The two disjoint pair-minima \(\min(A,B)\) and \(\min(C,D)\) are independent rate-two exponentials; their maximum has mean \(3/4\). The cross-minimum \(\min(B,C)\) has mean \(1/2\). The first positive-part term is the length of the overlap of the intervals \([0,A]\) and \([B-C,B]\), and so has mean

\[
\int_0^\infty e^{-b}\int_0^b e^{-t}e^{-(b-t)}\,dt\,db
=\int_0^\infty b e^{-2b}\,db=\frac14.
\]

The second positive-part term has the same mean \(1/4\) by symmetry. It follows that

\[\mathbb EF(X)=\frac14\left(\frac34+\frac12+\frac14+\frac14\right)=\frac7{16},\]

proving the mean asymptotic.

## Verification

The standalone file `verify.py` independently enumerates distinct antisquare factor strings by positions and half-lengths, and compares against the four-term formula for all \(8^4=4096\) positive parameter quadruples with coordinates at most \(8\). It also checks the sharp bound, equality families, and fixed-length maxima for every \(4\le n\le80\). Run with `python3 verify.py` from a directory containing the script. Output includes `VERIFY_OK`; only the analytic proof applies to all parameters and the asymptotic expectation.

## Relationship to prior work

The run-count obstruction and the classification of two- and three-run *shapes* of antisquares are already explicit in Baranwal et al. (2022), particularly Lemma 14 and the proof of Theorem 11; they are not claimed here as new. That work addresses avoidance, critical exponents, and minimal antisquares rather than the number of all distinct antisquare factors of an arbitrary four-run host word, its maximizers, or a distributional mean. Ng et al. (2019) concerns extremal simultaneous avoidance and bounded numbers of squares and antisquares, without deriving this unrestricted four-run count. The new content is the complete host-dependent formula, the sharp fixed-length equality classification, and the linear-density expectation.

## Limitations

No bound is asserted for binary words with more than four runs. No convergence in probability or full limiting distribution is asserted; the expectation result has an \(O(1)\) additive remainder without an exact finite-length mean formula. Publication novelty has been assessed against the cited primary material and relevant database searches but cannot be guaranteed against all unindexed literature. Finite enumeration is a consistency check, not an infinite proof.

## References

1. A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223 (first public version September 19, 2022), particularly Section 6, Lemma 14 and Theorem 11. https://arxiv.org/abs/2209.09223
2. T. Ng, P. Ochem, N. Rampersad, J. Shallit, *New Results on Pseudosquare Avoidance*, arXiv:1904.09157 (first public version April 19, 2019), particularly Sections 1–2. https://arxiv.org/abs/1904.09157
