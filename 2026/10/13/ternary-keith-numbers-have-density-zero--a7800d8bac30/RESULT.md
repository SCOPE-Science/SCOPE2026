# Ternary Keith numbers have density zero
## Finding
Let \(\mathcal K_3(x)\) denote the number of base-\(3\) Keith numbers at most \(x\). Then
\[
\mathcal K_3(x)\ll \frac{x}{\sqrt{\log x}}.
\]
Consequently ternary Keith numbers have asymptotic density zero.

The estimate has the same order as the Klazar--Luca bound for ordinary decimal Keith numbers. Their published argument extends directly to bases at least \(4\), but they explicitly isolate base \(3\) as the unresolved case of that method. The obstruction is removed by counting zero-rich ternary strings with a sharp binomial large-deviation estimate instead of the crude bound used there.

## Assumptions and scope
Write an \(n\)-digit base-\(3\) integer as
\[
N=(a_1a_2\cdots a_n)_3,
\qquad a_1\in\{1,2\},\quad a_i\in\{0,1,2\}.
\]
Its Keith sequence is initialized by
\[
K^N_1=a_1,\ldots,K^N_n=a_n
\]
and thereafter satisfies
\[
K^N_m=K^N_{m-1}+\cdots+K^N_{m-n}
\qquad(m>n).
\]
The integer \(N\) is a ternary Keith number if \(K^N_m=N\) for some \(m\).

Let \(L^{(r)}\) be the order-\(r\) recurrence initialized by \(r\) ones. The recurrence estimates used below are the same ones proved by Klazar and Luca: for indices linear in \(r\),
\[
L^{(r)}_j=(r-1)2^{j-r-1}\left(1+O\!\left(\frac{j}{2^r}\right)\right)+1.
\]
Their comparison lemmas depend only on positivity and linearity of the recurrence. In base \(3\), the upper digit bound changes from \(9\) to \(2\).

Fix
\[
\alpha=\frac7{20}.
\]
Two strict inequalities drive the proof:
\[
\frac13<\alpha
\qquad\text{and}\qquad
3^\alpha<\frac32.
\]
The second is exact, since it is equivalent after raising to the twentieth power to
\[
2^{20}<3^{13},
\]
namely \(1048576<1594323\).

## Proof
Consider ternary Keith numbers with exactly \(n\) digits. We separate the digit strings according to their number of zero digits.

First consider strings having at least \(\alpha n\) zeros. Under the uniform measure on all ternary strings, the number of zeros has the binomial distribution \(\operatorname{Bin}(n,1/3)\). Since \(\alpha>1/3\), the standard binomial large-deviation bound gives a constant \(c>0\) such that
\[
\sum_{j\ge \alpha n}\binom nj2^{n-j}
\le 3^n e^{-cn}.
\]
Restricting the leading digit to be nonzero can only decrease this count. Thus the zero-rich strings are exponentially negligible, in particular
\[
O\!\left(\frac{3^n}{\sqrt n}\right).
\]
For completeness, no probability theorem is essential here: the exponent
\[
H(t)+(1-t)\log 2,
\qquad
H(t)=-t\log t-(1-t)\log(1-t),
\]
has its unique maximum on \([0,1]\) at \(t=1/3\), so its maximum on \([\alpha,1]\) is strictly smaller than \(\log3\).

Now take a ternary Keith number \(N\) with fewer than \(\alpha n\) zeros. It has at least
\[
r=\lfloor(1-\alpha)n\rfloor
\]
nonzero digits. Suppose
\[
N=K^N_m.
\]
The elementary recurrence comparisons from the Klazar--Luca argument give, for all sufficiently large \(n\),
\[
K^N_m\ge L^{(r)}_{r+m-n}
\]
and
\[
K^N_m\le2L^{(n)}_m.
\]
The same comparisons also imply \(m=O(n)\): for large \(n\), one has \(m>2n\), because
\[
K^N_{2n}\le2L^{(n)}_{2n}=O(n2^n)<3^{n-1}\le N,
\]
while the Fibonacci lower bound for \(L^{(n)}\) gives an upper bound linear in \(n\).

We may therefore use the displayed asymptotic for \(L^{(r)}\) and \(L^{(n)}\). Since \(r\asymp n\), it yields constants \(c_1,c_2>0\) such that
\[
c_1 n2^{m-n}<N<c_2 n2^{m-n}
\]
for all sufficiently large \(n\). Together with
\[
3^{n-1}\le N<3^n,
\]
this gives
\[
2^{m-n}n\asymp3^n,
\]
and hence
\[
m=(1+\log_2 3)n-\log_2 n+O(1).
\]
In particular, for each sufficiently large \(n\), only \(O(1)\) values of \(m\) can occur.

Fix one such \(m\), and also fix the first \(r\) ternary digits of \(N\). Put
\[
s=n-r.
\]
Then
\[
s\le \alpha n+1.
\]
We claim that the possible suffixes form an antichain in the product poset \(\{0,1,2\}^s\).

Indeed, suppose two distinct suffixes in one block were coordinatewise comparable, with corresponding Keith numbers \(N_1<N_2\). Because their prefixes agree, the difference
\[
M=N_2-N_1
\]
has at most \(s\) ternary digits and is obtained by digitwise subtraction without borrowing, so
\[
0<M<3^s.
\]
Let \(M^*\) be the length-\(n\) ternary digit string consisting of \(r\) leading zeros followed by that suffix difference. By linearity of the recurrence,
\[
M=K^{M^*}_m.
\]
Since \(M^*\) is nonzero, the recurrence comparison gives
\[
K^{M^*}_m\ge L^{(n)}_{m-n}.
\]
Using the recurrence asymptotic and \(2^{m-n}n\asymp3^n\), we obtain
\[
M\gg n2^{m-2n}\asymp\left(\frac32\right)^n.
\]
On the other hand,
\[
M<3^s\le3^{\alpha n+1}.
\]
Because \(3^\alpha<3/2\), these inequalities are incompatible for all sufficiently large \(n\). This proves the antichain claim.

Klazar and Luca's product-poset lemma bounds an antichain in \(\{0,1,2\}^s\) by
\[
O\!\left(\frac{3^s}{\sqrt s}\right).
\]
There are \(3^r\) possible fixed prefixes and only \(O(1)\) possible recurrence indices \(m\). Hence the zero-poor ternary Keith numbers with \(n\) digits number
\[
O\!\left(3^r\frac{3^s}{\sqrt s}\right)
=O\!\left(\frac{3^n}{\sqrt n}\right).
\]
Adding the exponentially small zero-rich class proves the same bound for all \(n\)-digit ternary Keith numbers.

Finally, if \(3^{n-1}\le x<3^n\), summing the digit-block bounds and using \(3^n\le3x\) gives
\[
\mathcal K_3(x)\ll\frac{x}{\sqrt n}
\asymp
\frac{x}{\sqrt{\log x}}.
\]

## Verification
The proof is analytic and infinite. The accompanying checker verifies the exact admissible window for \(\alpha=7/20\), evaluates the zero-rich binomial proportion for growing \(n\), and exhaustively enumerates ternary Keith numbers through ten ternary digits. These computations are sanity checks only.

The critical logical points are independent of enumeration: the zero-rich class is exponentially sparse because \(7/20>1/3\); the antichain contradiction works because \(3^{7/20}<3/2\); and the recurrence estimates force only boundedly many possible recurrence indices for each digit length.

## Relationship to prior work
Klazar and Luca proved
\[
\#\mathcal K(x)\ll \frac{x}{\sqrt{\log x}}
\]
for ordinary decimal Keith numbers. Their proof also treats every fixed base \(b\ge4\). They then state explicitly that their two parameter inequalities cannot be met for \(b=3\), so the ternary case “seems to require more substantial changes.” The present argument supplies that missing change: the crude estimate for strings with many zeros is replaced by the exact binomial large-deviation threshold at zero density \(1/3\).

The same source proves the antichain lemma and recurrence estimates used here; those components already work in base \(3\). The only new ingredient needed to close the base is the sharper zero-digit counting step and the observation that the interval
\[
\left(\frac13,1-\log_3 2\right)
\]
is nonempty.

OEIS A007629 records ordinary decimal Keith numbers and cites Klazar--Luca. OEIS A320122 concerns integers that fail to be Keith numbers in every base. Neither inspected entry states a ternary density theorem.

## Limitations
The theorem gives an upper bound and density zero; it does not establish whether infinitely many ternary Keith numbers exist, nor a lower-order asymptotic.

The proof deliberately reuses the published recurrence and antichain lemmas and changes only the step that blocks base \(3\). The literature search found no later paper stating this ternary extension, but an unindexed note could exist; this is the main originality risk.

Base \(2\) is qualitatively different: powers of \(2\) already give infinitely many binary Keith numbers, so this density argument is not being asserted there.

## References
1. M. Klazar and F. Luca, “Counting Keith Numbers”, arXiv:math/0608419v1, submitted 16 August 2006; *Journal of Integer Sequences* 10 (2007), Article 07.2.2. Primary MSC 11B39; secondary 11A63.
2. OEIS Foundation, A007629, “Keith numbers, or Repfigit numbers”.
3. OEIS Foundation, A320122, “Numbers that are not Keith numbers in any base”.
