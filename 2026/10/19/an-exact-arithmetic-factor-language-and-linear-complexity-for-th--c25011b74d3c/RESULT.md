# An exact arithmetic-factor language and linear complexity for the powers-of-two indicator

## Finding
Let \(s:\mathbb N_0\to\{0,1\}\) be the indicator of positive powers of two: \(s(n)=1\) if and only if \(n=2^e\) for some integer \(e\ge0\). For each integer \(k\ge1\), set
\[
L_k=\{(s(n+jd))_{j=0}^{k-1}:n\in\mathbb N_0,\ d\in\mathbb N\},\qquad A(k)=|L_k|.
\]
Write \(\operatorname{odd}(h)=h/2^{\nu_2(h)}\) for positive integers \(h\), and let \(T=\lfloor\log_2 k\rfloor\). Then **the following finite, explicitly specified union is exactly** \(L_k\):

1. the all-zero word;
2. all \(k\) words with exactly one \(1\);
3. all \(k-1\) words with ones exactly at positions \(0,b\) for \(1\le b<k\);
4. for every \(0\le a<b<k\) and integer \(1\le t\le T\), put \(h=b-a\), \(q=2^t-1\), and \(H=\operatorname{odd}(h)\). When \(H\mid q\) and \(aq\le h\), include the word \(v_{a,b,t}\) with
\[
v_{a,b,t}(j)=1\quad\Longleftrightarrow\quad
h+(j-a)q>0\ \text{and}\ \operatorname{odd}(h+(j-a)q)=H,\qquad 0\le j<k.
\]

The union is interpreted as a set, not a sum of multiplicities. It is a finite exact algorithm for every length, requiring no search over unbounded progression starts or differences. Moreover,
\[
\boxed{2k\le A(k)\le30k\quad(k\ge1),\qquad A(k)=\Theta(k).}
\]

## Assumptions and scope
The sampling difference is **strictly positive** and the starting index is **nonnegative**. The initial index \(0\) is not a power of two. One-based positions are not used. A word is a binary vector of length \(k\), and words appearing on multiple progressions are counted once. The odd-part function is applied only to positive integers. For \(k=1\), item 4 is empty and the language is \(\{0,1\}\).

## Proof
**A two-power normalization.** Suppose a progression has powers \(2^u\) and \(2^{u+t}\) at positions \(a<b\), where \(t\ge1\). Write \(h=b-a\) and \(q=2^t-1\). Subtracting the values gives \(hd=2^u q\). Since \(d\) is an integer and \(q\) is odd, necessarily \(H=\operatorname{odd}(h)\mid q\). The nonnegative starting index \(n=2^u-ad\) gives \(aq\le h\). Conversely, whenever these two conditions hold, the explicit integers
\[
n=(h-aq)/H,\qquad d=q/H
\]
are nonnegative and positive respectively. They place powers \(2^{\nu_2(h)}\) and \(2^{\nu_2(h)+t}\) at positions \(a,b\). At arbitrary \(j\), the sampled value is \((h+(j-a)q)/H\), which is a positive power of two precisely when its numerator is positive with odd part \(H\). This proves the exact claimed word \(v_{a,b,t}\).

**The exponent-gap cutoff.** Let \(a<b<c\) be three positions holding powers \(2^u<2^{u+t}<2^{u+t+r}\), with \(t,r\ge1\). From the two positive differences,
\[
(c-b)(2^t-1)=(b-a)2^t(2^r-1).
\]
The odd number \(2^t-1\) is coprime to \(2^t\); therefore \(2^t\mid(c-b)\). If a progression's first two one-positions are \(a<b\), then either \(t\le T\), or \(a=0\) (because \(a(2^t-1)\le b-a<k\)), and no third one-position can follow \(b\) (because \(c-b\ge2^t\ge k\)). There are no ones between \(a,b\) by their choice as the first two. Hence every progression with at least two ones is represented in item 4 or in item 3.

**Existence of every exceptional word.** All-zero windows occur within an arbitrarily long gap between adjacent powers. Every singleton-one word occurs by taking \(d=1\) and centering the desired position at a sufficiently large isolated power. Finally, fix \(1\le b<k\), write \(b=2^eH\) with \(H\) odd, and choose an arbitrarily large \(t\ge1\) such that \(H\mid2^t-1\) (use the multiplicative order of two modulo \(H\), with the modulus-one case immediate). Choose \(2^{t/2}>b\) and \(2^t>k\). Set \(q=2^t-1\), \(n=2^e\) and \(d=q/H\). The positions \(0,b\) hold the powers \(2^e,2^{e+t}\). An additional power at \(0<c<b\), of exponent \(e+s\) with \(0<s<t\), would imply \(q\mid b(2^s-1)\). The standard identity \(\gcd(2^t-1,2^s-1)=2^{\gcd(t,s)}-1\), with \(\gcd(t,s)\le t/2\), would then force \((2^t-1)/(2^{t/2}-1)>b\) to divide \(b\), a contradiction (and this inequality also holds with the integer floor in the denominator). Any power after \(b\) has index difference at least \(2^t>k-1\) by the preceding spacing lemma. Thus the only ones in the window are at \(0,b\). This establishes the reverse inclusion and exact characterization.

**Linear upper bound.** Put \(\tau(q)\) for the number of positive divisors of \(q\), and use \(\tau(q)\le2\sqrt q\). The first three families contain \(2k\) distinct words. At \(a=0\), for each exponent gap \(t\le T\), admissible separations \(h=b\) have form \(h=2^e\delta\) with \(\delta\mid q=2^t-1\). There are at most \((1+\log_2 k)\tau(q)\) such pairs. Therefore their total count is at most
\[
2(1+\log_2 k)\sum_{t=1}^T2^{t/2}
\le \frac{2\sqrt2}{\sqrt2-1}(1+\log_2 k)\sqrt k
\le\frac{4}{1-1/\sqrt2}\,k.
\]
Here the last inequality uses \(1+\log_2 k\le2\sqrt k\) for \(k\ge1\).

For \(a\ge1\), fix \(t\), put \(q=2^t-1\) and let \(h=2^e\delta<k\) where \(\delta\mid q\). The number of admissible positions \(a\) is at most \(h/q\), because \(aq\le h\). Summing over allowed \(e\) gives at most \(2k/q\) for each \(\delta\), and thus at most \(2k\tau(q)/q\) for that \(t\). Summing over all \(t\ge1\), using \(2^t-1\ge2^{t-1}\), yields
\[
2k\sum_{t\ge1}\frac{\tau(2^t-1)}{2^t-1}
\le4k\sum_{t\ge1}2^{-(t-1)/2}
=\frac{4}{1-1/\sqrt2}\,k.
\]
Hence
\[
A(k)\le \left(2+\frac{8}{1-1/\sqrt2}\right)k<30k.
\]
The first three families are mutually disjoint, giving \(A(k)\ge2k\) and completing the proof. The elementary inequality \(1+\log_2 k\le2\sqrt{k}\) follows by differentiating \(2\sqrt x-1-\log_2x\) on \(x\ge1\).

## Verification
Run `python3 verify.py` (Python standard library only). The program implements the finite language independently of any bounded search over progression starts. It checks explicit actual-progression witnesses for **every generated candidate** through length \(40\), independently enumerates many small progressions through length \(17\), and checks thousands of additional large progressions at selected larger lengths. The reported first values of \(A(k)\) for \(k=1,2,3,4,5,8,16,24,32,40\) are \(2,4,7,10,12,21,43,69,88,114\). Finite computations do not prove the theorem for arbitrary \(k\); the argument above supplies the infinite proof.

## Relationship to prior work
Konieczny and Müllner (2023, arXiv:2309.03180) study arithmetical subword complexity of general automatic sequences and prove a general \(r^k\exp(o(k))\) growth bound in terms of effective alphabet size. The indicator considered here has effective alphabet size one, but that general bound does not imply linear complexity or the exact language generator. Avgustinovich, Cassaigne, and Frid (2006) classify certain uniformly recurrent low-complexity words; this sparse indicator is not uniformly recurrent, so their structural classification does not subsume the result. Frid (2006) also studies possible arithmetical-complexity growth rates via Toeplitz constructions, without an equivalent formula for this indicator in the inspected material. The novelty claim is limited to this exact language description and resulting linear bound.

## Limitations
The constants \(2\) and \(30\) are not claimed optimal; the result does not determine \(\lim_{k\to\infty}A(k)/k\) or a closed numerical formula free from finite duplicate elimination. Other power bases and arithmetic patterns with negative starts are not covered. The literature comparison cannot exclude an unindexed equivalent result.

## References
- J. Konieczny and C. Müllner, *Arithmetical subword complexity of automatic sequences*, arXiv:2309.03180, initially posted 2023-09-06; https://arxiv.org/abs/2309.03180.
- S. V. Avgustinovich, J. Cassaigne and A. E. Frid, *Sequences of low arithmetical complexity*, RAIRO Theoretical Informatics and Applications 40 (2006), 569–582; https://doi.org/10.1051/ita:2006041.
- A. E. Frid, *On possible growths of arithmetical complexity*, RAIRO Theoretical Informatics and Applications 40 (2006), 443–458; https://doi.org/10.1051/ita:2006021.
