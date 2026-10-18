# Exact arithmetic-progression census in odd-binomial Pascal rows

## Finding

For every integer \(n\ge1\), define the set of indices of odd coefficients in Pascal row \(n\):
\[
E_n=\left\{j\in\{0,\ldots,n\}:\binom{n}{j}\equiv1\pmod2\right\}.
\]
Write the binary expansion of \(n\) as maximal runs of consecutive ones, of lengths \(t_1,\ldots,t_r\), separated by one or more zeros. For \(k\ge2\), let \(P_k(n)\) be the number of pairs \((a,d)\) of integers with \(d>0\) such that
\(a,a+d,\ldots,a+(k-1)d\) are all in \(E_n\). Set
\[
L_i=2^{t_i},\qquad h_i=\left\lfloor\frac{L_i-1}{k-1}\right\rfloor,\qquad
B_i=L_i(2h_i+1)-(k-1)h_i(h_i+1).
\]
Then the exact census, for every \(n\ge1\) and \(k\ge2\), is
\[
\boxed{P_k(n)=\frac12\left(\prod_{i=1}^r B_i-\prod_{i=1}^r L_i\right).}
\]
In particular, the longest possible progression has exactly \(2^{\max_i t_i}\) terms. Thus the set of odd coefficients in a row is free of nonconstant three-term progressions if and only if the binary expansion of the row index has no adjacent ones. The number of indices \(0\le n<2^m\) whose odd-coefficient support is three-term-progression-free equals \(F_{m+2}\), where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\).

There is also an exact extremal count. If \(t=\max_i t_i\), \(c=|\{i:t_i=t\}|\), and \(w=\sum_i t_i\), then
\[
\boxed{P_{2^t}(n)=2^{w-ct}\,\frac{(2^t+2)^c-(2^t)^c}{2}.}
\]

## Assumptions and scope

The row index \(n\) is any positive integer, the progression length \(k\) is any integer at least two, and progressions have **positive** common difference. Each pair \((a,d)\) is counted once; a progression need not consist of consecutive elements of \(E_n\). A singleton row \(n=0\) has no nonconstant progression and satisfies \(P_k(0)=0\); its maximum progression length is left undefined. Powers and congruences here are statements over ordinary integers, not modular progressions.

## Proof

**Lucas support decomposition.** Lucas' congruence for the prime \(2\) says that \(\binom{n}{j}\) is odd exactly when every one-bit of \(j\) occupies a position carrying a one-bit of \(n\). Let the successive one-runs begin at binary positions \(a_1<\cdots<a_r\), counting from zero. Distinct runs obey \(a_{i+1}\ge a_i+t_i+1\). Consequently
\[
E_n=\left\{\sum_{i=1}^r2^{a_i}u_i:0\le u_i<L_i\right\},\qquad L_i=2^{t_i}.
\]
The representation is unique because the binary positions of the blocks do not overlap.

**Additive rigidity across separated blocks.** Let four members \(x,y,z,w\) of \(E_n\) have block coordinates \(u_i(x),u_i(y),u_i(z),u_i(w)\). We claim
\[
x+y=z+w\quad\Longleftrightarrow\quad
u_i(x)+u_i(y)=u_i(z)+u_i(w)\quad\text{for all }i,\]
where \(u_i(\cdot)\) denotes its \(i\)-th block coordinate. The reverse implication follows by summing with powers of two. For the forward direction, the coordinate difference
\[
\delta_i=u_i(x)+u_i(y)-u_i(z)-u_i(w)
\]
has absolute value at most \(2(L_i-1)\). If \(r\ge2\), the equation at the lowest run implies \(2^{a_1}\delta_1\) is divisible by \(2^{a_2}\). But
\(2^{a_2-a_1}\ge2^{t_1+1}=2L_1>2(L_1-1)\), hence \(\delta_1=0\). Removing the first run and repeating inductively proves all \(\delta_i=0\). The one-run case is immediate. In particular, a triple of members of \(E_n\) is a three-term arithmetic progression if and only if its block coordinates are three-term progressions in every block.

**Product enumeration.** Fix \(k\ge2\). A sequence of \(k\) elements of \(E_n\) is an arithmetic progression if and only if each coordinate sequence is an arithmetic progression: apply additive rigidity to every consecutive three terms; for \(k=2\), any two terms are a progression. In the interval of integers \(\{0,\ldots,L_i-1\}\), the number of \(k\)-term progressions **with an oriented common difference** (possibly zero or negative) is
\[
\begin{aligned}
B_i&=L_i+2\sum_{d=1}^{h_i}\bigl(L_i-(k-1)d\bigr)\\
&=L_i(2h_i+1)-(k-1)h_i(h_i+1),
\end{aligned}
\]
since \(h_i=\lfloor(L_i-1)/(k-1)\rfloor\). The separated-block bijection transports the Cartesian product of these progressions to every oriented progression in \(E_n\), producing \(\prod_i B_i\) such sequences. Exactly \(\prod_iL_i=|E_n|\) are constant. Reversal pairs every nonconstant sequence with one of opposite sign of common difference, because two distinct coordinate tuples map to distinct integers. Dividing the nonconstant total by two gives the claimed formula.

**Maximum length and exact count.** A nonconstant progression requires at least one coordinate to have nonzero common difference, which is possible in block \(i\) precisely when \(k\le L_i\). Thus \(k_{\max}=\max_iL_i=2^{\max_i t_i}\). At \(k=2^t\), every maximal block has \(h_i=1\) and \(B_i=L_i+2\), while every shorter block has \(h_i=0\) and \(B_i=L_i\). Substitution yields the displayed extremal count. A nonconstant three-term progression exists if and only if \(\max_iL_i\ge3\), equivalently \(t\ge2\); these are precisely the indices whose binary expansion contains adjacent ones. Among binary strings of length \(m\), including leading zeros, strings avoiding consecutive ones satisfy the Fibonacci recurrence, giving \(F_{m+2}\). This also includes the zero index for this last counting statement.

## Verification

The standalone pure-Python script `CHECK.py` implements the product formula and independently enumerates actual eligible indices using the bitwise criterion \((j\mathbin{\&}n)=j\). It compares exact progression counts for every \(1\le n\le1024\) and \(2\le k\le9\), giving \(8192\) direct comparisons. It also checks the maximum-length formula and the three-term criterion for every index in that range, and tests the Fibonacci census on binary strings of lengths zero through twelve. Execute with `python3 CHECK.py`. For example, for \(n=27\), the counts for \(k=2,3,4\) are \(120,24,10\). These are finite corroborations; the preceding proof, not the tests, establishes the result for all integers.

## Relationship to prior work

The classical Lucas theorem yields the precise binary-digit support of odd binomial coefficients. Meštrović's 2014 survey, section 6.1, recounts the classical Glaisher/Fine count of odd coefficients in each row, \(|E_n|=2^{\operatorname{popcount}(n)}\). The present result instead counts **every length of arithmetic progression of odd-coefficient positions** and identifies a block-coordinate additive rigidity which permits its factorization.

Rolnick's 2014 paper analyzes three-term-progression-free **ternary-digit Stanley sequences**, a different object: its construction does not count progressions in fixed rows of Pascal's triangle. Kuca's 2018 paper uses the Sierpinski triangle in additive-sequence questions and Freiman homomorphisms for Ulam-type sequences, but its theorems concern those additive sequences, not the exact binary-binomial row census. The overlap distinction is at the level of mathematical statements, not merely terminology.

## Limitations

This concerns parity modulo \(2\), not arbitrary primes or prime-power divisibility. It counts unweighted increasing arithmetic progressions by their length, not their common-difference distribution. Source searching cannot rule out every equivalent statement in the literature; the novelty assessment is best-knowledge and subject to independent checking.

## References

1. Romeo Meštrović, *Lucas' theorem: its generalizations, extensions and applications (1878--2014)*, arXiv:1409.3820v1 (2014), especially section 6.1. https://arxiv.org/html/1409.3820v1
2. David Rolnick, *On the classification of Stanley sequences*, arXiv:1408.1940v1 (2014), section 3. https://arxiv.org/html/1408.1940v1
3. Borys Kuca, *Structures in Additive Sequences*, arXiv:1804.09594v1 (2018), sections 3--5. https://arxiv.org/html/1804.09594v1
