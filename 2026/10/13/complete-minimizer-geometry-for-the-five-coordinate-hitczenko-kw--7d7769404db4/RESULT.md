# Complete minimizer geometry for the five-coordinate Hitczenko–Kwapień constant
## Finding
Let \(\varepsilon_1,\ldots,\varepsilon_m\) be independent Rademacher signs, let \(1\le m\le5\), and let \(a\in\mathbb R^m\setminus\{0\}\). Pad the normalized absolute coefficients \((|a_i|/\|a\|_2)\) with zeros to five entries and sort them as
\[
0\le b_1\le b_2\le b_3\le b_4\le b_5.
\]
Set
\[
\tau=\frac{b_1+b_2+b_3+b_4+b_5-1}{2},
\]
and let \(u\le v\le w\) be the increasing rearrangement, with multiplicity, of the three numbers
\[
b_3,\qquad b_4,\qquad b_1+b_2.
\]
Then
\[
\Pr\!\left\{\left|\sum_{i=1}^m a_i\varepsilon_i\right|\ge\|a\|_2}\right\}\ge\frac14.
\]
Moreover, equality holds exactly when
\[
u\le\tau<v.
\]
If this condition fails, then
\[
\Pr\!\left\{\left|\sum_{i=1}^m a_i\varepsilon_i\right|\ge\|a\|_2}\right\}\ge\frac5{16}.
\]
Thus the complete minimizer set for the known low-dimensional value \(G_3=G_4=G_5=1/4\) is described by one exact gap between the fourth and fifth relevant subset sums.

## Assumptions and scope
The coefficients are real and not all zero. Signs are independent and symmetric. Multiplying all coefficients by a common nonzero scalar, changing individual coefficient signs, permuting coordinates, or adjoining zero coefficients does not change the normalized tail probability, so the five-entry ordered normalization above loses no generality. The statement is restricted to at most five nonzero coefficients and does not classify global minimizers over arbitrary dimension.

## Proof
Normalize \(\|a\|_2=1\), absorb coefficient signs into the Rademacher variables, pad by zero coefficients, and write
\[
s=b_1+b_2+b_3+b_4+b_5,
\qquad
\tau=\frac{s-1}{2}.
\]
For a subset \(J\subseteq\{1,\ldots,5\}\), start from the all-positive sign vector and flip exactly the coordinates in \(J\). If \(w(J)=\sum_{j\in J}b_j\), the resulting signed sum is \(s-2w(J)\). Hence
\[
s-2w(J)\ge1
\quad\Longleftrightarrow\quad
w(J)\le\tau.
\]
Let \(N\) be the number of subsets satisfying this inequality. Symmetry gives
\[
\Pr\!\left\{\left|\sum_{i=1}^5 b_i\varepsilon_i\right|\ge1}\right\}
=\frac{N}{16}.
\]
It remains to identify the minimum possible \(N\) and its equality cases.

We first prove
\[
\tau\ge\min\{b_3,b_1+b_2\}.
\]
Write \(x=b_1\), \(y=b_2\), \(z=b_3\), \(p=b_4\), and \(q=b_5\), so
\[
x^2+y^2+z^2+p^2+q^2=1
\]
and \(p,q\ge z\).

Suppose first that \(z\le x+y\). Put \(r=x+y-z\ge0\). Then
\[
s-2z=r+p+q.
\]
A direct expansion gives
\[
\frac{(s-2z)^2-1}{2}
=pq+r(p+q-z)+xy-z^2.
\]
Since \(pq\ge z^2\), every term on the right after replacing \(pq\) by \(z^2\) is nonnegative. Therefore \(s-2z\ge1\), so \(\tau\ge z\).

Suppose instead that \(x+y\le z\), and put \(r=z-x-y\ge0\). Then
\[
s-2(x+y)=r+p+q
\]
and
\[
\frac{(s-2(x+y))^2-1}{2}
=pq+r(p+q)+xy-z(x+y).
\]
Using \(pq\ge z^2\), \(p+q\ge2z\), and \(x+y=z-r\), the right-hand side is at least
\[
z^2+2zr+xy-z(z-r)=3zr+xy\ge0.
\]
Thus \(s-2(x+y)\ge1\), so \(\tau\ge x+y\). This proves the claimed lower bound.

Now consider the five particular subsets
\[
\varnothing,\qquad \{1\},\qquad \{2\},\qquad \{3\},\qquad \{1,2\}.
\]
The preceding inequality guarantees at least four admissible subsets, and therefore \(N\ge4\), proving the probability bound \(1/4\).

For equality, note that the two possible additional boundary weights after \(0,b_1,b_2\) are controlled by the three numbers \(b_3\), \(b_4\), and \(b_1+b_2\). Let \(u\le v\le w\) be their increasing rearrangement. We already proved \(\tau\ge u\).

If \(u=b_1+b_2<v\) and \(\tau<v\), every subset containing an index at least \(3\) has weight at least \(b_3\ge v>\tau\). Exactly the four subsets of \(\{1,2\}\) are admissible. If instead \(u=b_3<v\) and \(\tau<v\), then \(b_3<b_4\) and \(b_3<b_1+b_2\); exactly \(\varnothing,\{1\},\{2\},\{3\}\) are admissible. Hence \(u\le\tau<v\) implies \(N=4\).

Conversely, if \(\tau\ge v\), then \(\varnothing\), \(\{1\}\), \(\{2\}\), and the two subsets corresponding to the two smallest members of the multiset \(\{b_3,b_4,b_1+b_2\}\) are all admissible. These are five distinct subsets, so \(N\ge5\). Therefore \(N=4\) if and only if \(u\le\tau<v\); outside that region the probability is at least \(5/16\).

## Verification
The proof above is exact and establishes the statement for every real coefficient vector with at most five nonzero entries. The companion script `verify.py` is only a regression check. It exhaustively enumerates every nondecreasing integer five-tuple with entries from \(0\) through \(8\), checks all \(32\) sign patterns using integer arithmetic, and compares the exact tail count with the stated \([u,v)\) criterion. Its successful output is recorded in `VERIFICATION.md`.

## Relationship to prior work
Hu, Lan, and Sun define the finite-dimensional Hitczenko–Kwapień constants and explicitly record \(G_3=G_4=G_5=1/4\), while their main theorem proves the conjectured \(7/32\) lower bound through dimension seven. Their public full text does not give the minimizer geometry for \(G_3,G_4,G_5\). The present result keeps the known value \(1/4\) but classifies every coefficient vector attaining it and gives the discrete gap \(5/16\) for every nonattaining vector with at most five nonzero coefficients.

Hollom later proved the global sharp bound \(7/32\) and the complete threshold profile over all normalized Rademacher sums. That global theorem is stronger as a dimension-free lower bound at threshold one, but it does not imply which vectors are exactly extremal inside the restricted class of at most five nonzero coefficients; its full public text does not state the \([u,v)\) classification above.

## Limitations
The theorem classifies only the exact one-standard-deviation tail threshold for support size at most five. It does not classify minimizers for six or more nonzero coefficients, nor does it address strict-tail probabilities. The originality check cannot exclude an unindexed elementary observation formulated purely as a Boolean subset-sum lemma.

## References
1. Z.-C. Hu, G.-L. Lan, and W. Sun, “Some explorations on two conjectures about Rademacher sequences,” arXiv:1910.11312, first public version 2019-10-24; Acta Mathematicae Applicatae Sinica, English Series 37 (2021), 1–16, doi:10.1007/s10255-021-0993-0.
2. L. Hollom, “Tight Anti-Concentration of Rademacher Sums,” Random Structures & Algorithms (2025), doi:10.1002/rsa.70024.
