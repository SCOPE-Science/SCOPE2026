# Exact minimal-state enumeration for all translated Rudin–Shapiro sequences

## Finding

Let \(R(n)\in\{0,1\}\) be the parity of the number of adjacent `11` pairs in the binary representation of a nonnegative integer \(n\), with \(R(0)=0\). For every integer \(c\ge0\), let \(N(c)\) be the number of states of a *minimal, complete, binary-output DFAO* producing \(R(n+c)\) from **least-significant-digit-first** binary input for \(n\), including the empty input and arbitrary terminal zeros.

There is an exact finite formula for \(N(c)\) requiring only \(O(1+\log_2(c+1))\) short interval tests, **without constructing or minimizing any automaton**. Put \(B=\operatorname{bitlength}(c)\), taking \(B=0\) when \(c=0\), and \(E=B+3\). Define
\[
\mathcal S_0(c)=\{(c,0,0)\}.
\]
For each integer \(1\le e\le E\), put \(h=2^{e-1}\) and let \(\mathcal S_e(c)\) contain precisely the triples
\[
\left(q,s,R(b)\mathbin{\oplus}s(q\bmod2)\right),\quad
\begin{cases}
 c\le a<c+2^e,\\
 q=\lfloor a/2^e\rfloor,\\
 b=a-q2^e,\\
 s=\lfloor b/h\rfloor\in\{0,1\},
\end{cases}
\]
where \(\oplus\) is addition modulo two. Then
\[
\boxed{\displaystyle N(c)=\left|\bigcup_{e=0}^{B+3}\mathcal S_e(c)\right|.}
\]
Although the displayed definition uses all \(a\) in a long interval, it is evaluated by **at most four interval intersections per level**: the only possible \(q\)'s are \(\lfloor c/2^e\rfloor\) and its successor; for each \((q,s)\), the admissible \(b\)'s form one interval. If that interval contains at least five integers, both possible parities \(R(b)\) occur. Otherwise its at most four elements suffice. Thus the exact count requires only \(O(B+1)\) small tests and set insertions, with \(O((B+1)^2)\) elementary bit operations in a straightforward implementation.

In particular, the exact dyadic-shift counts are
\[
\boxed{N(2^m)=4m+2\qquad(m\ge3).}
\]
The initial values are \(N(0)=4\), \(N(1)=5\), \(N(2)=7\), and \(N(4)=11\). This exact count is also the cardinality of a concrete minimal DFAO with explicit arithmetic transition and output functions given below.

## Assumptions and scope

Input strings are finite words \(w=b_0b_1\cdots b_{e-1}\), read from the least significant end and representing \([w]=\sum_{i=0}^{e-1}b_i2^i\). The empty word represents zero. Terminal zeroes do not change the integer represented, and the DFAO must give the correct result on *all* such words, not just canonical representations. A state's residual is its output on every possible continuation. No statement about most-significant-digit-first automata is made.

For a triple \((q,s,t)\in\mathbb N_0\times\{0,1\}^2\), define the binary-valued residual function
\[
F_{q,s,t}(n)=R(n+q)\oplus s(n\bmod2)\oplus t\quad(n\ge0).
\]
In particular, the initial residual is \(F_{c,0,0}\). The underlying function \(R\) obeys
\[
R(2n)=R(n),\qquad R(2n+1)=R(n)\oplus(n\bmod2).
\]
All quantifiers in the theorem range over nonnegative integers unless otherwise specified.

## Proof

**1. Every residual has the stated form.** For integers \(e\ge1\), \(0\le b<2^e\) and \(n\ge0\), concatenation of binary digits gives the exact identity
\[
R(2^e n+b)=R(n)\oplus R(b)\oplus
\left((n\bmod2)\left\lfloor\frac b{2^{e-1}}\right\rfloor\right).
\]
Only the pair crossing the boundary between the two blocks is not accounted for by \(R(n)\oplus R(b)\). After reading a prefix of length \(e\) representing \(j\in[0,2^e)\), any continuation representing \(n\) produces \(R(2^e n+j+c)\). Divide \(j+c=q2^e+b\) with \(0\le b<2^e\) and set \(s=\lfloor b/2^{e-1}\rfloor\). The preceding identity becomes
\[
R(2^e n+j+c)
=R(n+q)\oplus s(n\bmod2)\oplus
\big(R(b)\oplus s(q\bmod2)\big).
\]
Thus the reachable residuals after exactly \(e\) digits are precisely \(\{F_{q,s,t}:(q,s,t)\in\mathcal S_e(c)\}\). The empty prefix gives \(\mathcal S_0(c)\).

**2. Different triples are genuinely inequivalent.** First, \(R\) is not ultimately periodic. If it had any eventual period \(p>0\), the relation \(R(2n)=R(n)\) would allow division of each factor of two in \(p\), giving an *odd* eventual period \(p\). But for odd \(p\), and sufficiently large \(n\),
\[
R(2n+2p+1)=R(n+p)\oplus((n+p)\bmod2)
=R(2n+1)\oplus1,
\]
contradicting eventual periodicity with period \(p\) (hence also \(2p\)).

If \(q\ne q'\) and \(F_{q,s,t}=F_{q',s',t'}\), shifting the argument if necessary implies
\[
R(n+p)\oplus R(n)=\alpha(n\bmod2)\oplus\beta
\]
for some \(p>0\) and bits \(\alpha,\beta\), for all sufficiently large \(n\). If \(p\) is even, applying this identity twice gives \(R(n+2p)=R(n)\) eventually. If \(p\) is odd, applying it twice gives \(R(n+2p)=R(n)\oplus\alpha\), hence applying twice more gives the eventual period \(4p\). Either contradicts nonperiodicity. For fixed \(q\), differing \((s,t)\) give distinct functions immediately by evaluating both parities of \(n\). Thus *no two different triples can be merged*. By the residual/Myhill–Nerode characterization of minimal DFAOs, counting reachable triples gives exactly the minimal state count.

The corresponding direct transition on input bit \(x\in\{0,1\}\) is
\[
\delta((q,s,t),x)=
\left(q',d,t\oplus sx\oplus d(q'\bmod2)\right),\quad
q'=\left\lfloor\frac{q+x}{2}\right\rfloor,\quad d=(q+x)\bmod2,
\]
with output \(\tau(q,s,t)=R(q)\oplus t\). The recurrence for \(R\) proves that this transition correctly computes the next residual. Restricting it to the reachable triples yields the explicitly minimal complete machine.

**3. The truncation at \(E=B+3\) is exact.** For \(c=0\), the four triples with \(q=0\) all appear by \(e=3\), and no other \(q\) can occur. Suppose \(c\ge1\). For every \(e\ge B+3\), the interval \([c,c+2^e-1]\) produces only \(q=0\) or \(q=1\). In its \(q=1\) portion, the remainder \(b\) ranges over \([0,c-1]\), and \(b<2^{e-1}\); hence only \(s=0\) occurs and the possible \(t\)'s are the fixed parities \(R(b)\) with \(0\le b<c\). These are already realized at \(e=B+3\).

For \(q=0\), the lower-half remainder interval starts at \(c\) and ends at \(2^{e-1}-1\), while the entire upper half is also present. At \(e=B+3\), each interval has at least five elements. To see that both values of \(R\) occur in every interval of at least five successive nonnegative integers, observe that
\[
R(4j+2)\oplus R(4j+3)=1\quad(j\ge0),
\]
and every five consecutive integers contain such a pair. Thus all four triples \((0,s,t)\) already occur at level \(B+3\), and no larger \(e\) contributes any additional state. This proves the finite formula without extrapolating from a finite search.

**4. Evaluation requires only short intervals.** At a fixed \(e\), intersect \([c,c+2^e-1]\) with the four possible blocks
\[
[q2^e+s2^{e-1},\ q2^e+(s+1)2^{e-1}-1],
\quad q\in\{\lfloor c/2^e\rfloor,\lfloor c/2^e\rfloor+1\},\quad s\in\{0,1\}.
\]
Each nonempty intersection fixes \(q,s\); it contributes either one or both \(t\)-values according to \(R\) on a contiguous remainder interval. The five-consecutive-integers property handles every interval of length at least five, while at most four explicit evaluations handle each shorter interval. There are \(B+3\) levels and no dependence on the magnitudes of their \(2^e\) ranges. This proves the stated complexity bound.

**5. Dyadic-shift specialization.** Let \(c=2^m\), \(m\ge3\). At levels \(1\le e\le m\) no quotient transition occurs: the only quotient is \(q=2^{m-e}\), and the remainders traverse the entire interval \([0,2^e)\). At \(e=1\) the quotient contributes two triples; at \(e=2\), three triples; and at each \(3\le e\le m\), exactly four, since \(R\) takes both values in each binary half-block. The distinct positive quotients never overlap. For \(e>m\), the only new quotient is \(q=0\), which contributes four triples in total; quotient \(q=1\) already had four at \(e=m\). With the initial state this gives
\[
N(2^m)=1+2+3+4(m-2)+4=4m+2.
\]
The exceptional small counts follow directly from the same finite formula.

## Verification

The companion Python program `checker.py` provides three independently organized checks. For each of 2,048 offsets \(0\le c<2048\), it compares the sets of arithmetic residual triples obtained by direct breadth-first transition closure against those obtained from the short-interval formula. Separately, it constructs an addition-with-carry automaton that tracks the parity of adjacent output bits and minimizes that automaton by partition refinement. All 2,048 minimal-state counts agree with the symbolic theorem. Further output checks cover 15,000 offset/input pairs, and the dyadic identity is checked at the 17 values \(3\le m\le19\).

Run `python3 checker.py` with a standard Python 3 interpreter. No third-party dependencies are required. The corresponding actual recorded output is in `checker_output.txt`. These finite tests corroborate the symbolic argument; they are not a substitute for the infinite distinguishability or truncation proofs.

## Relationship to prior work

Moradi, Rampersad, and Shallit [1] study state complexity of shifted automatic sequences, including explicit work on the Thue–Morse sequence and most-significant-digit-first shifts, and distinguish the two orientations of input. Their analysis does not provide a formula for the least-significant-digit-first shifts of the Rudin–Shapiro sequence. Rampersad and Shallit [2] study Rudin–Shapiro summatory functions through automata and give its fundamental recurrences; they do not enumerate minimal automata for every translated coefficient sequence. Rowland and Yassawi [3] exhibit the classical four-element binary kernel of the unshifted Rudin–Shapiro sequence, corresponding to \(N(0)=4\), but not arbitrary translations.

The contribution here is the exact residual classification and bounded interval formula **for every offset**, along with the nontrivial dyadic exact count; no general claim of priority beyond the examined literature is made.

## Limitations

The result is for one-sided coefficient sequences \(R(n+c)\), fixed nonnegative shifts, two-symbol output, and LSD-first input with trailing zeros allowed. It says nothing about MSD-first minimal-state complexity, arbitrary affine subsequences \(R(an+b)\), or the number of states after changing the output encoding. Exact finite formulas are not polynomial formulas in \(c\); the count depends on the binary pattern of the shift. Equivalent treatments in material not indexed or inspected remain possible. Independent mathematical audit has not been performed.

## References

[1] D. Moradi, N. Rampersad, J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017, first publicly submitted 2025-12-10; examined HTML v5, especially Sections 3, 4.2, and 4.3. https://arxiv.org/html/2512.10017v5

[2] N. Rampersad, J. Shallit, *Rudin-Shapiro Sums Via Automata Theory and Logic*, arXiv:2302.00405, 2023, HTML v3 examined, especially Sections 1, 3, and 9. https://arxiv.org/html/2302.00405v3

[3] E. Rowland, R. Yassawi, *A characterization of \(p\)-automatic sequences as columns of linear cellular automata*, *Advances in Applied Mathematics* 63 (2015), 68–89, especially Example 4.2 (unshifted four-element kernel). https://doi.org/10.1016/j.aam.2014.10.002
