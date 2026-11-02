# Exact iterated tortoise complexity of periodic Christoffel words

## Finding

Fix coprime integers \(1\le p<q\). Let \(\mathbf c_{p,q}\) be the infinite binary periodic mechanical word
\[
c_i=\left\lfloor\frac{(i+1)p}{q}\right\rfloor-\left\lfloor\frac{ip}{q}\right\rfloor\quad(i\ge0).
\]
For a finite binary word, \(T\) deletes its first \(1\) and appends that \(1\), fixing an all-zero word. Let \(\rho^{(k)}_{p,q}(n)\) count the distinct images \(T^k(w)\) of its distinct length-\(n\) factors, where \(k,n\ge1\). Define the integer parameters
\[
H=\left\lfloor\frac{kq-1}{p}\right\rfloor,\qquad
L=\max\{1,n-q+1\},\qquad U=\min\{n-1,H\},
\]
and let
\[
B=\begin{cases}
0,&U<L,\\
U-L+1-\left\lfloor\frac Uq\right\rfloor+\left\lfloor\frac{L-1}{q}\right\rfloor,&U\ge L.
\end{cases}
\]
**The exact all-iterate image-complexity formula** is
\[
\boxed{\rho^{(k)}_{p,q}(n)=\min\{q,n+1\}-B.}
\tag{1}
\]
Equivalently, \(B\) is the number of positive integers \(j\) satisfying
\[
\max\{1,n-q+1\}\le j\le\min\{n-1,H\},\qquad q\nmid j.
\tag{2}
\]
For every \(k\ge1\), the **sharp eventual injectivity threshold** on the distinct factors is
\[
\boxed{N_{p,q}(k)=q+\left\lfloor\frac{kq-1}{p}\right\rfloor.}
\tag{3}
\]
The map \(T^k\) is injective for every length \(n\ge N_{p,q}(k)\), but not for \(n=N_{p,q}(k)-1\). It need not be noninjective at *every* smaller length. In particular, for \(1\le n<q\), formula (1) reduces to \(\max\{2,n+1-H\}\); at and beyond \(q\), the modular exclusion in (2) produces the new rational-periodic oscillation. The specialization \(k=1\) is previously known and is included for uniformity; the contribution is the all-iteration law, especially \(k\ge2\).

## Assumptions and scope

The alphabet is ordered \(0<1\); \(\gcd(p,q)=1\) makes the period primitive. Factors are contiguous, with repeated starting positions collapsed when they yield the same letters. The period is repeated indefinitely. Phase cuts are evaluated with the right-continuous floor convention. The iteration \(T^k\) moves the first \(\min\{k,|w|_1\}\) ones of a length-\(n\) word to its end in their original order and otherwise preserves the order of zeros and other ones. Its action preserves the number of ones. There is no assumption that \(k\) is smaller than the number of ones.

## Proof

**Lemma 1 (prefix dominance is preserved).** For equal-length binary words \(u,v\), write \(u\preccurlyeq v\) if every prefix of \(u\) contains at most as many ones as the corresponding prefix of \(v\). Then
\[
u\preccurlyeq v\ \Longrightarrow\ T^k(u)\preccurlyeq T^k(v)
\quad\text{for all }k\ge0.
\]
To prove this, let the one positions of \(u\) be \(a_1<\cdots<a_m\) and those of \(v\) be \(b_1<\cdots<b_{m'}\), numbered from one. Prefix dominance means \(m\le m'\) and \(a_i\ge b_i\) for all \(i\le m\). The positions of the ones in \(T^k(u)\), in increasing rank \(i=1,\ldots,m\), are
\[
A_i=\begin{cases}a_{i+k}-k,&i\le m-k,\\n-m+i,&i>m-k,\end{cases}
\]
where the first branch is absent if \(k\ge m\). The analogous formula holds for \(v\). At each rank \(i\le m\), three cases are possible: both one positions are from surviving unshifted suffixes, in which case \(A_i\ge B_i\) follows from \(a_{i+k}\ge b_{i+k}\); the position in \(u\) is in its appended tail but the position in \(v\) is not, in which case \(A_i\ge n-k+1>B_i\); or both positions are appended, in which case \(A_i=n-m+i\ge n-m'+i=B_i\). The impossible reverse mixed case is excluded by \(m\le m'\). Hence the transformed one-position vectors remain coordinatewise ordered, which is equivalent to prefix dominance. \(\square\)

**Lemma 2 (ordered rational phase factors).** For \(x\in[0,1)\) define
\[
P_j(x)=\left\lfloor x+\frac{jp}{q}\right\rfloor,
\qquad w_n(x)_i=P_{i+1}(x)-P_i(x)\quad(0\le i<n).
\]
The phases \(x=\{sp/q\}\), \(0\le s<q\), produce exactly all length-\(n\) factors of \(\mathbf c_{p,q}\), since coprimality makes them all \(q\) rational grid points. The vector \((P_1(x),\ldots,P_n(x))\) is coordinatewise nondecreasing in \(x\). Its distinct internal cuts occur at
\[
d_r=1-\left\{\frac{rp}{q}\right\},
\quad1\le r\le\min(n,q-1).
\]
At the cut \(d_r\), exactly the prefix sums \(P_j\) for \(1\le j\le n\) and \(j\equiv r\pmod q\) increase by one. All cuts are grid points. Thus each half-open phase cell contains at least one attained phase, and distinct cells give distinct words. The number of cells is \(F(n)=\min(n+1,q)\). Their words form a totally ordered chain under \(\preccurlyeq\), so, by Lemma 1, their \(T^k\) images are also a weakly ordered chain. In particular, **every image fiber is an interval of consecutive phase cells**, and the image count equals \(F(n)\) minus the number of adjacent cell pairs having equal images. \(\square\)

**Lemma 3 (exact adjacent-edge test).** Fix an internal cut \(d_r\). If \(n\equiv r\pmod q\), the cut changes \(P_n\) and thus the total number of ones; the adjacent words cannot have equal \(T^k\) images. Otherwise, at each index \(j\) with \(1\le j<n\), \(j\equiv r\pmod q\), crossing the cut changes the adjacent letters at zero-based positions \(j-1,j\) from \(01\) to \(10\). These swaps occupy disjoint position pairs, since consecutive affected indices differ by \(q\ge2\). No other letter changes. Therefore the two words' ordered lists of one positions differ by shifting one position to the left for precisely the ones involved in these swaps, while all other one positions coincide.

The transformed images are equal if and only if all the moved ones are among the first \(k\) ones: those are precisely the ones erased from their original locations by \(T^k\), whereas any altered one of rank greater than \(k\) survives at different positions after the common number of deletions. The affected one associated to index \(j\) has rank
\[
1+P_{j-1}(d_r)=1+\left\lfloor\frac{jp}{q}\right\rfloor.
\]
Indeed, writing \(j=r+tq\) and using \(d_r=1-\{rp/q\}\) gives \(P_{j-1}(d_r)=tp+\lfloor rp/q\rfloor\). Hence if \(j_*\) is the largest affected index strictly below \(n\), the adjacent pair has equal images if and only if
\[
\left\lfloor\frac{j_*p}{q}\right\rfloor<k
\iff j_*\le H=\left\lfloor\frac{kq-1}{p}\right\rfloor.
\]
This is a necessary-and-sufficient test, including cases where \(k\) exceeds the number of ones. \(\square\)

**The count.** For each internal cut \(d_r\) not changing the total ones, the largest affected index \(j_*<n\) is the unique representative of the nonzero residue \(r\pmod q\) lying in
\[
\max\{1,n-q+1\}\le j_*\le n-1.
\]
Conversely, each integer in this interval not divisible by \(q\) corresponds to exactly one such cut. The right endpoint \(n-q\) is excluded because, when its residue is nonzero, the same cut also affects \(P_n\), so total weight changes; if it is zero it is not an internal cut. Lemma 3 thus identifies equal adjacent edges bijectively with the integers in (2). Counting these integers by subtracting multiples of \(q\) from the interval \([L,U]\) gives \(B\) in (1). By Lemma 2, contracting exactly these adjacent edges gives (1).

Finally \(H\) is never divisible by \(q\). To see this, write \(k=ap+r\), \(0\le r<p\). If \(r=0\), then \(H=aq-1\); otherwise \(H=aq+\lfloor(rq-1)/p\rfloor\), where \(1\le\lfloor(rq-1)/p\rfloor\le q-1\). For \(n\ge q+H\), the interval (2) is empty because \(L>H\), proving injectivity. At \(n=q+H-1\), the admissible integer \(j=H\) lies in (2) and is not divisible by \(q\), so a collision remains. This proves (3). \(\square\)

## Verification

Run `python3 verify.py` with Python 3's standard library. The checker directly generates all cyclic factors from the integer mechanical period and computes each iterated tortoise image from its ordered one positions. Independently, it reconstructs factors by sorted rational phases, checks contiguity of every image fiber, evaluates the modular interval count, and tests the sharp final collision and all later injectivity claims. The included `VERIFY_OUTPUT.txt` reports `VERIFY_OK` for all coprime \(1\le p<q\le28\), iteration counts \(1\le k\le6\), and all \(1\le n\le q+H+2\): 49,750 parameter-iteration-length cases, 769,053 individual phase-factor checks, and 23,908 post-period injectivity tests, and 93,235 independent direct operator replays. These finite checks corroborate, but do not replace, the unbounded proof.

## Relationship to prior work

Campbell and Rampersad (2026, first public April 28) define the tortoise-complexity function and establish results for the paperfolding and Thue–Morse words, while explicitly calling for Sturmian variants. Carey and Clampitt (2018) analyze lexicographically adjacent conjugates of Christoffel periods and their height-profile varieties, but not tortoise-image complexity. An earlier result determines the **one-iterate** rational Christoffel image complexity and its eventual-injectivity threshold; the present statement specializes to that result when \(k=1\), without claiming this specialization as new. Likewise, existing irrational Sturmian formulas for arbitrary \(k\) concern languages with \(n+1\) distinct factors at every length; those do not imply the modular oscillations or eventual-injectivity law of rational periods. The present theorem establishes the complete all-iteration transition, including the new prefix-dominance preservation lemma and the exact count of surviving residue-class collisions.

## Limitations

This is a theorem for primitive rational mechanical binary periods, not arbitrary binary periods, higher alphabets or other stack-sorting operators. It counts image classes for all iteration counts but does not classify the internal membership of each fiber for all \(k\). The standalone finite enumeration is not an independent mathematical audit; earlier unindexed equivalent work could affect priority.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v2 (first publicly posted 2026-04-28), https://arxiv.org/html/2604.25811v2.
2. N. Carey and D. Clampitt, *Partitioned Factors in Christoffel and Sturmian Words*, arXiv:1804.08724 (2018), https://arxiv.org/abs/1804.08724.
3. C. Defant and N. Kravitz, *Stack-sorting for words*, arXiv:1809.09158 (2018), https://arxiv.org/abs/1809.09158.
