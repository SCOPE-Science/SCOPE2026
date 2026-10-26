# A three-marker threshold for quadratic Abelian-square sensitivity to one adjacent swap

## Finding

Let \(Q(w)\) count the distinct nonempty Abelian-square contiguous factors of a finite binary word \(w\); an Abelian square has two equally long consecutive halves containing the same number of zeros and ones. For \(k\ge1\), define
\[
 W_k=0^k1\,0^k1\,0^k1\,0^k,\qquad V_k=0^k1\,0^{k+1}1\,0^{k-1}1\,0^k.
\]
These words have length \(4k+3\), contain three ones, and differ by **one adjacent interchange** \(10\mapsto01\). Their exact distinct Abelian-square complexities are
\[
 Q(W_k)=\binom{k+2}{2}-\mathbf1_{k\text{ odd}},\qquad
 Q(V_k)=k(k+2)+\left\lfloor\frac{k+1}{2}\right\rfloor.
\]
Thus \(Q(V_k)-Q(W_k)=k^2/2+O(k)=(4k+3)^2/32+O(k)\), and \(Q(V_k)/Q(W_k)\to2\). Conversely, if two length-\(n\) binary words differ by one adjacent interchange and each has at most two occurrences of its minority symbol, their Abelian-square counts differ by \(O(n)\), with an absolute implied constant. The minimal minority support at which a single adjacent swap can alter \(Q\) by quadratic order is therefore **three**. This is an order-sharp local-sensitivity statement, not a sharp leading constant over all words.

## Assumptions and scope

Only *distinct factor strings*, not occurrence counts, enter \(Q\). Factors are contiguous and nonempty. An adjacent interchange exchanges neighboring unequal symbols and preserves length and composition. For the lower-support assertion, the minority letter means the less frequent of zero and one; exchanging the two letters does not affect \(Q\).

For nonnegative integers \(a,b,c\), set
\[
 K(a,b,c)=\#\{(x,y)\in\mathbb Z^2:0\le x\le a,\;0\le y\le c,\; |x-y|\le b,\;x+y\equiv b\pmod 2\}.
\]
The proof applies also when one or more zero gaps vanish.

## Proof

**1. Two-marker classification.** Consider \(u=0^a1\,0^b1\,0^c\). Every Abelian square has an even number of ones; hence it has either zero or two ones. The distinct all-zero squares are \(0^{2j}\) for \(1\le j\le\lfloor\max(a,b,c)/2\rfloor\). Every factor with two ones has the unique form \(0^x1\,0^b1\,0^y\), with \(0\le x\le a\) and \(0\le y\le c\). Its two halves have one one each precisely when their total length is even, \(x+y\equiv b\pmod2\), and the midpoint lies between the two ones, equivalent to \(|x-y|\le b\). Consequently
\[
 Q(u)=\left\lfloor\frac{\max(a,b,c)}2\right\rfloor+K(a,b,c).
\]
Each parameter pair \((x,y)\) determines a different factor string.

**2. Three-marker classification.** Let \(u=0^a1\,0^b1\,0^c1\,0^d\). A square still contains zero or two ones, never three. Its two ones must be a consecutive pair of the three marked positions. Their factor families are counted by \(K(a,b,c)\) and \(K(b,c,d)\). Two such factor strings can coincide only if their middle zero gaps coincide, \(b=c\), in which case the common strings are exactly those with \(x\le\min(a,b)\) and \(y\le\min(c,d)\). Inclusion–exclusion gives
\[
 Q(u)=\left\lfloor\frac{\max(a,b,c,d)}2\right\rfloor+K(a,b,c)+K(b,c,d)-\mathbf1_{b=c}K(\min(a,b),b,\min(c,d)).\tag{1}
\]

**3. Evaluate the neighboring words.** Substituting \((a,b,c,d)=(k,k,k,k)\) into (1) cancels one pair family. All pairs in \([0,k]^2\) meet the band inequality, so direct parity counting yields
\[
 K(k,k,k)=\begin{cases}(k^2+2k+2)/2&k\text{ even},\\(k+1)^2/2&k\text{ odd}.\end{cases}
\]
Adding \(\lfloor k/2\rfloor\) proves the formula for \(Q(W_k)\). For \(V_k\), the two internal gaps \(k+1\) and \(k-1\) are unequal, so the factor families have no intersection. Their counts are
\[
 K(k,k+1,k-1)=\frac{k(k+1)}2,\qquad K(k+1,k-1,k)=\frac{k(k+3)}2.
\]
The first identity follows because the distance bound is automatic and the rectangle has equally many points of each parity. For the second, group pairs by \(e=x-y\), whose allowed values satisfy \(|e|\le k-1\) and \(e\equiv k-1\pmod2\); counting each diagonal and summing the resulting arithmetic progression gives \(k(k+3)/2\) for either parity of \(k\). Adding the \(\lfloor(k+1)/2\rfloor\) all-zero squares proves the asserted \(Q(V_k)\). Their unique displaced one moves from the second marked position one step right, so the words differ by one adjacent swap. Their exact formulas yield the stated asymptotics.

**4. Why two minority symbols cannot have quadratic one-swap sensitivity.** Up to exchanging the binary letters, a word with two minority symbols has the form considered in Step 1. An adjacent interchange moves one marked symbol one position, so changes two of the three zero gaps by at most one. Altering the outer gap bound \(a\) or \(c\) by one changes \(K\) by at most the number of points in a single new row or column, at most \(n\). Altering \(b\) by one changes the permitted diagonal strip by at most two points per row; it also flips the parity requirement. For each fixed \(x\), the permitted \(y\)-values form one interval of integers, and its two parity counts differ by at most one. Consequently the full parity-flip discrepancy is at most \(n\), plus at most \(2n\) from the changing strip boundary. Hence the total change in \(K\) under one gap modification is bounded by a universal multiple of \(n\); the all-zero-square contribution varies by at most one. Words with one or zero minority symbols are even simpler: their Abelian squares are solely the all-majority even powers, whose count changes by at most one under the swap. Thus the one-swap sensitivity with minority support at most two is \(O(n)\).

Every length-\(n\) word has at most \(n(n+1)/2\) distinct factors, so the trivial universal sensitivity bound is \(O(n^2)\). Step 3 attains that order with exactly three minority-symbol occurrences, while Step 4 rules it out with fewer. \(\square\)

## Verification

Execute `python3 verify_swap.py` with Python 3. The independent checker directly enumerates all contiguous factors to test Abelian-square membership. It checks equation (1) for all nonnegative four-gap tuples with total zero-gap length at most ten; independently compares the two exact families for \(1\le k\le14\), tests their formulas through \(k=34\), verifies the two-marker formula over all triples with up to thirteen zeros, and examines every adjacent swap with minority support at most two through length eleven. Finite checks supplement rather than replace the infinite proof above.

## Relationship to prior work

Fici and Mignosi, *Words with the Maximum Number of Abelian Squares* (2015, arXiv:1506.03562), Proposition 1, use the symmetric two-marker word \(0^k1\,0^k1\,0^k\) to obtain quadratic Abelian-square complexity. Kociumaka and collaborators developed general quadratic lower bounds for distinct Abelian squares in earlier work. The present finding concerns a different invariant—**the change in distinct-factor complexity caused by a single adjacent swap**—and establishes the sharp threshold in minority-symbol support. The symmetric two-marker result is used as background, not reclaimed. The existing exact two-marker gap formula does not imply quadratic sensitivity at three markers because distinct two-marker factor families can overlap or separate under a swap; equation (1) resolves that obstruction.

## Limitations

The theorem does not optimize the sensitivity constant among all words of given length, characterize every maximizing pair, or extend the support threshold to other repetition notions. Earlier equivalent results under another name for local edits remain a priority risk. The review is self-review only; independent mathematical audit has not been performed.

## References

1. G. Fici and F. Mignosi, *Words with the Maximum Number of Abelian Squares*, WORDS 2015, arXiv:1506.03562, first made public 2015-06-11, https://arxiv.org/html/1506.03562v1 .
2. T. Kociumaka et al., *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, arXiv:1604.02238, https://arxiv.org/abs/1604.02238 .
3. G. Fici, F. Mignosi and J. Shallit, *Abelian-square-rich words*, Theoretical Computer Science 684 (2017), 29–42, doi:10.1016/j.tcs.2017.02.012 (later supporting literature, not the date anchor).
