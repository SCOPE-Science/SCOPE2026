# An exact periodic sieve for two Fibonacci-offset families of Zeckendorf–Niven runs

## Finding

Let \(F_0=0,F_1=1\), and index the canonical Zeckendorf expansion using \(F_j\) with \(j\ge2\). Write \(s_Z(n)\) for its number of terms. An integer \(n>0\) is Zeckendorf–Niven if \(s_Z(n)\mid n\).

Consider a six-term progression with step two beginning at \(n=F_G-a\), where \(G\ge9\) and \(a\in\{3,5\}\). If all six terms are Zeckendorf–Niven, then \(G\) is odd. More precisely, the prime-\(3\) screen described below allows only \(G\equiv5,11\pmod{24}\) for \(a=3\), and only \(G\equiv1,5,7,11\pmod{24}\) for \(a=5\).

Adding primes \(5\) and \(7\) gives exact periodic necessary-condition sets. An explicit predicate for them is given below. Counted modulo \(1680\), they have the following sizes:

| Prime cutoff | \(a=3\) | \(a=5\) | Intersection | Union |
|---|---:|---:|---:|---:|
| 3 | 140 | 280 | 140 | 280 |
| 5 | 112 | 224 | 112 | 224 |
| 7 | 80 | 144 | 72 | 152 |

Thus the exact fractions of index classes passing this screen for at least one of the two offsets are \(1/6\), \(2/15\), and \(19/210\), respectively. These counts are for the screen, not for actual progressions.

## Scope

The two offsets are candidate families, not asserted here to exhaust all six-term runs. The result is unconditional for progressions in either family but does not assert that any index passing the screen yields a run. The index bound \(G\ge9\) covers all progressions in these families with \(n\ge21\).

## Proof

Write \(V=F_G\) and \(r=\lfloor(G-3)/2\rfloor\). The six weights, in progression order, are
\[
\begin{array}{c|c|c}
 a & G\text{ parity} & (s_Z(V-a+2j))_{j=0}^{5}\\ \hline
 3 & \text{either} & (r,r+1,2,2,2,3)\\
 5 & \text{odd} & (r-1,r,r+1,2,2,2)\\
 5 & \text{even} & (r,r,r+1,2,2,2).
\end{array}
\]
For the negative offsets \(w=5,3,1\), the base cases at \(G=8\) are \(F_7+F_4\), \(F_7+F_5\), and \(F_7+F_5+F_3\), respectively. At \(G=9\) they are \(F_8+F_6\), \(F_8+F_6+F_3\), and \(F_8+F_6+F_4+F_2\). The identity \(F_{G+2}-w=F_{G+1}+(F_G-w)\) transports these weights to each larger index of the same parity, adding one term each time: the largest index in \(F_G-w\) is at most \(G-1\), so the expansion after adjoining \(F_{G+1}\) is canonical. For the positive offsets, \(1,3,5,7\) have weights \(1,1,1,2\) and highest index at most \(5\). Their expansions concatenate canonically with \(F_G\).

For \(a=5\) and even \(G\ge10\), the first two weights equal \(r\ge3\); their divisibility conditions would force \(r\mid2\). Discard these even indices before sieving. For the remaining shapes, the conditions from the weight-two terms both reduce to \(V\) odd, in turn equivalent to \(3\nmid G\). For \(a=3\), the last term also requires \(V\equiv2\pmod3\). The other tests are
\[
 r\mid V-3,\qquad r+1\mid V-1,
 \qquad \text{and for }a=5\text{ also }r-1\mid V-5.
\]
Define the cutoff-\(B\) screen, for \(B=3,5,7\), by keeping the shape restrictions just given and replacing each of these last variable-divisor tests \(d\mid V-c\) by the implications
\[
 \ell\mid d\ \Longrightarrow\ V\equiv c\pmod\ell \qquad(\ell\in\{2,3,5,7\},\ \ell\le B).
\]
Only prime-divisor consequences are imposed, not prime powers or full divisibility.

The tests for \(\ell=2\) follow from \(V\) odd. In shape \(a=3\), if \(G\) is even, then \(G=2r+4\). The case \(r\equiv1\pmod3\) contradicts \(3\nmid G\); the cases \(r\equiv0,2\pmod3\) require \(V\equiv0,1\pmod3\), respectively, contrary to \(V\equiv2\pmod3\). For odd \(G=2r+3\), the only possibilities for shape \(a=3\) are \(r\equiv1\pmod3\) and \(V\equiv2\pmod3\). Shape \(a=5\) adds the case \(r\equiv2\pmod3\), \(V\equiv1\pmod3\), from the test on \(r+1\); when \(r\equiv1\pmod3\) the test on \(r-1\) gives \(V\equiv5\equiv2\pmod3\). Fibonacci residues at odd indices are \(1,2,2,1\pmod3\) at residues \(1,3,5,7\pmod8\), respectively. Combining with \(G=2r+3\) yields the claimed classes modulo \(24\).

The Fibonacci residue pairs return to \((0,1)\) after \(3,8,20,16\) steps modulo \(2,3,5,7\), respectively (iterate \((u,v)\mapsto(v,u+v)\)). The parity restriction on \(G\) and the test \(\ell\mid d\) are both determined by \(G\bmod 2\ell\). Thus the predicates are periodic in \(G\) with common period
\[
 \operatorname{lcm}(3,8,20,16,4,6,10,14)=1680.
\]
The accompanying `verify.py` constructs the Fibonacci residue arrays by iterating the pair recurrence to its first return. It evaluates the displayed predicate at every index from \(9\) through \(1688\), representing each class once, and counts the two sets, their intersection and their union. This finite enumeration proves the claimed counts for the periodic predicates, not for full Zeckendorf–Niven divisibility.

## Relationship to prior work and limitations

Lao, Miller, Rosa, Shiliaev, Tresch, Wong and Zhang, *On Zeckendorf-Niven numbers and arithmetic progressions*, [arXiv:2606.24006](https://arxiv.org/abs/2606.24006), study consecutive Zeckendorf–Niven terms in progressions of common difference two, including constructions and bounds on run lengths. The screen here quantifies a separate obstruction for two fixed Fibonacci offsets, at arbitrarily large indices. It neither extends finite exclusions to all indices nor rules out any candidate beyond what the stated divisibility tests imply. Primes beyond seven and prime powers can exclude further classes.
