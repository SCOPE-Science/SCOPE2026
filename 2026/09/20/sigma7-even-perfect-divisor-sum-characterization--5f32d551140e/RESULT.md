# The k=7 case of Chu's divisor-sum conjecture for even perfect numbers

## Statement

For a positive integer \(m\), write
\[
\sigma_7(m)=\sum_{d\mid m} d^7.
\]

### Theorem

Let
\[
n=2^{\alpha-1}p^{\beta-1}, \qquad \alpha,\beta>1,
\]
where \(p\) is an odd prime satisfying
\[
p<3\cdot 2^{\alpha-1}-1.
\]
Then
\[
n\mid \sigma_7(n)
\]
if and only if \(n\) is an even perfect number different from
\[
2^6(2^7-1)=8128.
\]

Equivalently, this proves the \(k=7\) case of Conjecture 5 in H. V. Chu,
*Divisibility of Divisor Functions of Even Perfect Numbers*, Journal of Integer
Sequences 24 (2021), Article 21.3.4. Chu proved the full statement for \(k=5\)
and conjectured the analogous result for every prime \(k>2\) for which
\(2^k-1\) is a Mersenne prime.

The backward implication is Chu's Theorem 3. The content below is the forward
implication for \(k=7\).

## Proof

Put
\[
S_\alpha=\sigma_7(2^{\alpha-1})
=\frac{2^{7\alpha}-1}{127}.
\]
If \(n\mid \sigma_7(n)\), Chu's preliminary argument gives
\[
p^{\beta-1}\mid S_\alpha,
\tag{1}
\]
\[
2^\alpha\mid p^{7\beta}-1,
\tag{2}
\]
and \(\beta\) is even. Write
\[
\beta=2^v b,\qquad b\ \text{odd},\quad v\ge1.
\]

We use Chu's Lemmas 8--10, which are stated for arbitrary prime \(k>2\)
with \(2^k-1\) prime, specialized here to \(k=7\).

### 1. The case \(p\equiv1\pmod4\)

Chu's Lemma 8 gives
\[
\alpha\le v+1,\qquad
p^{2^v-1}
\le
\frac{2^{7(v+1)}-1}{127}.
\tag{3}
\]
Since \(p\ge5\), (3) fails for \(v=4\):
\[
5^{15}> \frac{2^{35}-1}{127}.
\]
It then fails for every larger \(v\): on increasing \(v\) by one, the
left-hand lower bound is multiplied by \(5^{2^v}\), whereas the
right-hand side is multiplied by less than \(129\). Hence \(v\le3\).

If \(v=1\), then \(\alpha\le2\), so the hypothesis
\(p<3\cdot2^{\alpha-1}-1\) leaves no prime \(p\equiv1\pmod4\).

If \(v=2\), then \(\alpha\le3\), and the only possible prime is \(p=5\),
with \(\alpha=3\). But
\[
S_3=16513\not\equiv0\pmod5,
\]
contradicting (1), since \(\beta\ge4\).

If \(v=3\), (3) forces \(p=5\). Equation (1) would require
\(5^7\mid S_\alpha\) for \(2\le\alpha\le4\), whereas
\[
S_2=129,\qquad S_3=16513,\qquad
S_4=2113665,
\]
and \(\nu_5(S_2),\nu_5(S_3),\nu_5(S_4)=0,0,1\).
Thus this case is impossible.

### 2. The exceptional prime \(p=7\)

Suppose \(p=7\). Chu's Lemma 9 gives
\[
\alpha\le v+3,
\tag{4}
\]
because \(\nu_2(7^2-1)=4\).

The order of \(2\) modulo \(7\) is \(3\). Hence \(7\mid S_\alpha\) only
if \(3\mid\alpha\). In that case LTE gives
\[
\nu_7(S_\alpha)
=\nu_7(2^{7\alpha}-1)
=2+\nu_7(\alpha).
\tag{5}
\]
If \(v\ge2\), then \(\beta-1\ge2^v-1\), while (4)--(5) give
\[
\nu_7(S_\alpha)\le 2+\nu_7(\alpha)<2^v-1;
\]
for \(v=2\), \(\alpha\le5\) makes the inequality immediate, and for
\(v\ge3\), use \(\nu_7(\alpha)\le\log_7(v+3)\) and
\(2^v-1>v+2\). This contradicts (1).

If \(v=1\), then \(\alpha\le4\). Divisibility by \(7\) forces
\(\alpha=3\), and (5) gives \(\nu_7(S_3)=2\). Thus
\(\beta-1\le2\); since \(\beta\) is even with \(\nu_2(\beta)=1\),
we get \(\beta=2\). This gives \(n=28\), an even perfect number.

Henceforth assume
\[
p\equiv3\pmod4,\qquad p\ne7.
\]

### 3. Bounds for \(p\equiv3\pmod4\), \(p\ne7\)

Chu's Lemma 9 gives
\[
p^{2^v-15}
<
\frac{2^{7(v-1)}}{127}.
\tag{6}
\]
Since \(p\ge3\), (6) fails at \(v=5\), and then for every larger
\(v\): the left lower bound gains a factor \(3^{2^v}\), while the
right side gains only a factor \(128\). Thus
\[
1\le v\le4.
\tag{7}
\]

Write
\[
p+1=2^\lambda q,\qquad \lambda\ge2,\quad q\ \text{odd}.
\]
The proof of Chu's Lemma 10 gives
\[
\alpha\le\lambda+v.
\tag{8}
\]
Because \(p\ne7=k\), its scenario (a) is absent. Scenarios (b) and (c)
both imply
\[
(2^\lambda-1)^{\beta-1}
\le
\sum_{i=0}^6 2^{i(\lambda+v)}.
\tag{9}
\]
Moreover, the size hypothesis and (8) imply
\[
2^\lambda q=p+1
<3\cdot2^{\alpha-1}
\le3\cdot2^{\lambda+v-1},
\]
so
\[
q<3\cdot2^{v-1}.
\tag{10}
\]

A useful consequence of (9) is
\[
(\lambda-1)(\beta-1)<6(\lambda+v)+1,
\tag{11}
\]
because \(2^\lambda-1\ge2^{\lambda-1}\) and the geometric sum in (9)
is less than twice its largest term.

For fixed \(v,\beta\) with \(\beta-1>6\), the ratio of the right-hand
side of (9) to its left-hand side is strictly decreasing as
\(x=2^\lambda\) increases: each term
\[
\frac{2^{iv}x^i}{(x-1)^{\beta-1}},\qquad 0\le i\le6,
\]
is strictly decreasing.

### 4. The subcase \(v=1\)

From (10), \(q=1\), so
\[
p=2^\lambda-1.
\]
Combining the original size condition with (8) shows
\[
\alpha\in\{\lambda,\lambda+1\}.
\]

If \(\beta=2\), Chu's Theorem 3 gives exactly the allowed even perfect
numbers, excluding \(8128\).

If \(\beta>2\), then \(\beta\ge6\). For \(\alpha=\lambda\), LTE gives
\[
\nu_p(S_\alpha)\le1
\]
for \(p\ne7\); when \(p=127\), the denominator \(127\) removes that one
factor. For \(\alpha=\lambda+1\), reducing \((2^\alpha)^7-1\) modulo
\(p\) gives \(127\), so \(p\nmid S_\alpha\) unless \(p=127\); for
\(p=127\), LTE again gives \(\nu_{127}(S_\alpha)=0\) after division by
\(127\). Thus (1) cannot hold when \(\beta\ge6\).

### 5. A \(k=7\) replacement for Chu's \(\beta=4\) lemma

Assume \(v=2\) and \(\beta=4\). Then
\[
\sigma_7(p^3)
=(p^{14}+1)(p^7+1).
\]
For odd \(p\equiv3\pmod4\), \(p^{14}+1\) has exactly one factor of
\(2\), and
\[
\frac{p^7+1}{p+1}
=p^6-p^5+p^4-p^3+p^2-p+1
\]
is odd. Since \(2^{\alpha-1}\mid\sigma_7(p^3)\),
\[
2^{\alpha-2}\mid p+1.
\]
Therefore
\[
p=t\,2^{\alpha-2}-1,\qquad 1\le t\le5.
\tag{12}
\]

Set \(x=2^\alpha\) and
\[
F(x)=x^6+x^5+\cdots+x+1.
\]
Equation (1) says \(p^3\mid(x^7-1)/127\).

If \(p=127\), (12) forces \(\alpha\in\{7,8,9\}\); LTE gives
\(\nu_{127}(S_\alpha)=\nu_{127}(\alpha)=0\), impossible.
Thus \(p\ne127\). Since \(p\ne7\),
\[
\gcd(x-1,F(x))
\]
is not divisible by \(p\), so \(p^3\) must divide one of \(x-1\) or
\(F(x)\).

From (12),
\[
t x\equiv4\pmod p.
\]
If \(p\mid x-1\), then \(p\mid4-t\). The only nontrivial possibilities
are \(t=1,p=3,\alpha=4\), where \(\nu_3(x-1)=1\), or \(t=4\), where
\(x-1=p\); neither allows \(p^3\mid x-1\).

If \(p\mid F(x)\), then
\[
p\mid C_t:=\sum_{i=0}^6 4^i t^{6-i}.
\]
The five constants are
\[
\begin{array}{c|c}
t&C_t\\ \hline
1&5461=43\cdot127\\
2&8128=2^6\cdot127\\
3&14197\\
4&28672=2^{12}\cdot7\\
5&61741=29\cdot2129.
\end{array}
\]
Combining these prime factors with (12) leaves only \(p=7\) or
\(p=127\), already excluded, or values for which \((p+1)/t\) is not
a power of two. Hence \(\beta=4\) is impossible.

### 6. The remaining finite cases

For \(v=2\), admissible values of \(\beta\) are \(4,12,20,\ldots\).
The case \(\beta=4\) was just excluded. For \(\beta=12\), (11) gives
\(\lambda\le4\). At \(\beta=20,\lambda=2\), (9) already fails:
\[
3^{19}> \sum_{i=0}^6 2^{4i},
\]
and monotonicity eliminates every larger \(\beta\). Thus only
\[
(v,\beta,\lambda)=(2,12,\lambda),\qquad2\le\lambda\le4
\]
remains.

For \(v=3\), admissible values are \(8,24,\ldots\). For \(\beta=8\),
(11) gives \(\lambda\le25\). At \(\beta=24,\lambda=2\), (9) fails:
\[
3^{23}> \sum_{i=0}^6 2^{5i},
\]
so only
\[
(v,\beta,\lambda)=(3,8,\lambda),\qquad2\le\lambda\le25
\]
remains.

For \(v=4\), admissible values are \(16,48,\ldots\). Equation (11)
gives \(\lambda\le4\) for \(\beta=16\), while it contradicts
\(\lambda\ge2\) for \(\beta\ge48\). Thus only
\[
(v,\beta,\lambda)=(4,16,\lambda),\qquad2\le\lambda\le4
\]
remains.

These ranges are finite because (10) bounds \(q\), and (8) bounds
\(\alpha\). The standalone exact-integer verifier `artifacts/verify.py`
enumerates precisely the remaining possibilities, retaining only prime
\[
p=q2^\lambda-1
\]
that satisfy the original size hypothesis. It finds:
\[
\begin{array}{c|c|c|c}
(v,\beta)&\text{admissible tuples}&
\max \nu_p(S_\alpha)&\beta-1\\ \hline
(2,12)&8&1&11\\
(3,8)&62&1&7\\
(4,16)&33&2&15.
\end{array}
\]
Thus (1) fails in every remaining case.

We have shown that the forward implication can occur only when
\(\beta=2\); Chu's Theorem 3 then gives precisely the even perfect
numbers other than \(8128\). This proves the theorem.

## Verification

`artifacts/verify.py` uses only exact Python integer arithmetic. It checks the
finite ranges above, the constants in the \(\beta=4\) lemma, and a direct sanity
scan of the original divisibility for \(2\le\alpha\le14\),
\(2\le\beta\le20\). The deterministic output is recorded in
`artifacts/verification.txt`.

The finite enumeration is part of the proof only after the analytic reductions
to bounded \((v,\beta,\lambda,q,\alpha)\). The small-box scan is corroborative
only.

## Context and originality

Chu's 2021 paper proves the corresponding full theorem for \(k=5\), proves the
\(\beta=2\) case for all relevant \(k\), and explicitly states the general
\(\beta>1\) assertion as Conjecture 5, noting that the method used for \(k=5\)
does not apply directly to other \(k\). Since \(2^7-1=127\) is prime, the theorem
above supplies the next Mersenne-exponent case.

Searches through 20 September 2026 using the exact conjecture, the title and
author of Chu's paper, `sigma_7`, "seventh powers of divisors", the form
\(2^{\alpha-1}p^{\beta-1}\), and stronger divisor-sum characterizations did not
locate a later proof of the \(k=7\) case. This originality claim is therefore
to the best of our knowledge, not exhaustive.

The full text of X.-W. Jiang's 2018 paper *On even perfect numbers* was not
inspected. Its accessible abstract states the \(k=3\) theorem, and Chu's paper
describes it as the \(k=3\) predecessor; it does not provide evidence of
\(k=7\) coverage. No inaccessible source with title or abstract suggesting a
proof of the \(k=7\) case was identified.

## Limitations

The theorem is only the \(k=7\) instance of Chu's broader Conjecture 5; it does
not settle \(k=13,17,19,\ldots\). The finite step is computer-assisted, though
it uses exact arithmetic over explicitly bounded ranges and is independently
reproducible from the included script. No formal proof-assistant verification
or independent audit is asserted.

## References

1. H. V. Chu, *Divisibility of Divisor Functions of Even Perfect Numbers*,
   Journal of Integer Sequences 24 (2021), Article 21.3.4.
   https://cs.uwaterloo.ca/journals/JIS/VOL24/Chu/chu26.html
2. X.-W. Jiang, *On even perfect numbers*, Colloquium Mathematicum 154 (2018),
   131--135. DOI: 10.4064/cm7374-11-2017.
3. T. Cai, D. Chen, and Y. Zhang, *Perfect numbers and Fibonacci primes (I)*,
   International Journal of Number Theory 11 (2015), 159--169.
   DOI: 10.1142/S1793042115500098.
