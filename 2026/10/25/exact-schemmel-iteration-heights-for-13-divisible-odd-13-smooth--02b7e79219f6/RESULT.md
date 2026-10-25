# Exact Schemmel iteration heights for 13-divisible odd 13-smooth integers

## Finding

Let \(L_2\) be the second Schemmel totient function. For an odd positive integer \(n>1\), let \(R_2(n)\) be the number of its iterates under \(L_2\) required to reach \(1\). For every \(a,b,c,d\in\mathbb Z_{\ge0}\) and \(e\in\mathbb Z_{\ge1}\), set
\[
n=3^a5^b7^c11^d13^e,\qquad W=a+b+c+2d+2e.
\]
Then the **exact** iteration height is
\[
R_2(n)=\begin{cases}
W+\mathbf 1_{a=0},&d\ge1,\\
W+\mathbf 1_{a=0}+\mathbf 1_{\{a\le1,\ b=0\}},&d=0.
\end{cases}
\]
Thus the total delay beyond a linear prime-exponent weight is at most two steps, completely determined by the displayed initial occupancy conditions. In particular,
\[
49n<15\cdot 7^{R_2(n)}.
\]
This proves the *strict* case of Defant's 2015 Conjecture 20 throughout the specified infinite family; it does not establish the conjecture for arbitrary odd integers.

## Assumptions and scope

For \(n=1\), set \(L_2(1)=1\). For each odd prime power \(p^u\) with \(u\ge1\), the definition is \(L_2(p^u)=p^{u-1}(p-2)\), extended multiplicatively to odd positive integers. All five allowed primes are greater than \(2\), so every iterate of a number in the asserted family is positive and remains supported on \(\{3,5,7,11,13\}\): explicitly, \(3-2=1\), \(5-2=3\), \(7-2=5\), \(11-2=3^2\), and \(13-2=11\). The exponents \(a,b,c,d\) may vanish but \(e\) must be positive. The theorem concerns first hitting \(1\), with no intermediate \(0\).

## Proof

**Exponent dynamics.** Write a current iterate as \(3^a5^b7^c11^d13^e\). In one application of \(L_2\), with \([P]\) denoting \(1\) if \(P\) holds and \(0\) otherwise, its exponent vector becomes
\[
\begin{aligned}
a'&=a-[a>0]+[b>0]+2[d>0],\\
b'&=b-[b>0]+[c>0],\\
c'&=c-[c>0],\\
d'&=d-[d>0]+[e>0],\\
e'&=e-[e>0].
\end{aligned}
\]
For \(W=a+b+c+2d+2e\), substitution and cancellation give the exact one-step identity
\[
W-W'=[a>0].
\]
This is a nonnegative integer potential, zero exactly at the terminal state. Consequently, \(R_2(n)\) equals its starting value \(W\) **plus the number of nonterminal steps made with \(a=0\)**.

**No further idle steps after a two-token buffer.** We prove the following invariant. If a state has \(a\ge2\), every later nonterminal state has \(a>0\). Indeed, consider the persistent class of states satisfying either \(a\ge2\), or \(a=1\) and at least one of \(b>0\), \(d>0\), or \(b=c=d=e=0\). Every state in this class has \(a>0\), unless its next state is the terminal zero vector. If \(a\ge2\), then \(a'\ge1\). In the only case where \(a'=1\), we have \(a=2\), \(b=d=0\); any positive \(c\) makes \(b'>0\), any positive \(e\) makes \(d'>0\), and otherwise there is no upstream work. If \(a=1,b>0\), then \(a'\ge1\); whenever \(a'=1\), positive remaining \(b,c,e\) make either \(b'>0\) or \(d'>0\), while if none remain, the single \(3\)-factor is the entire state. If \(a=1,d>0\), then \(a'\ge2\). Finally, the state \((1,0,0,0,0)\) terminates in one step. Thus this class is invariant up to termination and includes all states with \(a\ge2\).

**Start-up analysis.** We now use \(e\ge1\).

If \(d\ge1\) initially, the first step produces \(a'=a-[a>0]+[b>0]+2\ge2\). By the invariant there are no later idle steps. The initial step is idle precisely when \(a=0\). Hence the total delay is \([a=0]\).

If \(d=0\) initially, the first step produces \(d'=1\), and \(a'=a-[a>0]+[b>0]\). On the second step the positive \(d'\) contributes two factors of \(3\), so \(a''\ge2\); by the invariant, no later step is idle. The first step is idle exactly for \(a=0\). The second is idle precisely when \(a'=0\), equivalent to \(a\le1\) and \(b=0\). Adding these at most two delays to \(W\) proves the stated two formulas. Both steps exist because \(e>0\): at the start \(W\ge2\), and after the first step the \(11\)-exponent is positive.

**Strict bound.** Since \(R_2(n)\ge W\), and \(7>3,5\) and \(49>11,13\),
\[
\frac{7^{R_2(n)}}n
\ge\left(\frac73\right)^a\left(\frac75\right)^b
\left(\frac{49}{11}\right)^d\left(\frac{49}{13}\right)^e
\ge\frac{49}{13}>\frac{49}{15}.
\]
Rearrangement gives \(49n<15\cdot7^{R_2(n)}\). The inequality is strict even for the smallest \(13\)-factor; no statement about other integers is implied.

## Verification

The companion `verify.py` computes the literal multiplicative Schemmel function on integers, independently iterates exponent vectors, and checks the theorem over 6480 complete initial exponent tuples and 52,488 further tuples respectively. Nine additional cases exercise exponents as large as \(100\). All tests agree. These finite checks are corroboration; the proof above supplies the universal argument.

## Relationship to prior work

Colin Defant introduced the counting functions \(R_m\) for iterated Schemmel totients and posed the global lower-bound question as Conjecture 20 (*Journal of Integer Sequences* 18 (2015), Article 15.2.1, published January 13, 2015). His paper does not derive the two-case exact formula above. Harrington and Jones (2010) studied the equivalent indexing convention \(C_2=R_2-1\) on a restricted domain excluding any initial prime factor congruent to \(1\) modulo \(3\); every integer covered here contains \(13\), so lies outside that domain. White (1962) provides a general theory for other multiplicative iteration functions satisfying distinct hypotheses, not this formula.

Earlier calculations determine \(R_2\) for odd \(7\)-smooth integers supported on \(\{3,5,7\}\). The present theorem has disjoint domain because it requires a factor \(13\). Here the transition \(13\to11\to3^2\) introduces delayed, double-sized input, and the key new feature is the exact one- or two-step start-up correction in that branching chain. The corollary does not claim the global conjecture is solved.

## Limitations

The exact statement requires a positive exponent of \(13\) and no prime factors larger than \(13\); it does not classify trajectories outside this invariant support. Its novelty is subject to the possibility of an equivalent unindexed specialization in the iteration literature. Full text of Harrington and Jones (2010) could not be obtained in this examination; the domain exclusion is supported by Defant's explicit discussion. The general literature search cannot establish exhaustive uniqueness. Independent mathematical validation has not been performed.

## References

1. Colin Defant, "On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions", *Journal of Integer Sequences* 18 (2015), Article 15.2.1. Published January 13, 2015. https://www.maths.tcd.ie/EMIS/journals/JIS/VOL18/Defant/defant5.pdf
2. J. Harrington and L. Jones, "On the Iteration of a Function Related to Euler's \(\phi\)-Function", *Integers* 10 (2010), 497–515. DOI: 10.1515/integ.2010.042.
3. G. K. White, "Iterations of Generalized Euler Functions", *Pacific Journal of Mathematics* 12 (1962), 777–783. https://msp.org/pjm/1962/12-2/pjm-v12-n2-p32-s.pdf
