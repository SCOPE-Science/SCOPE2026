# Exact four-term residue densities and support counts for the Stern sequence

## Finding
Let \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\). For any integer \(m\ge2\) and residues \(a,b,c,d\pmod m\), the natural density
\[
\mu_m(a,b,c,d)=\lim_{N\to\infty}\frac1N\#\{0\le n<N:(s(n),s(n+1),s(n+2),s(n+3))\equiv(a,b,c,d)\pmod m\}
\]
exists and is the following exact rational number. Write \(J_2(m)=m^2\prod_{p\mid m}(1-p^{-2})\). Define \(K_m(w,z)\) by setting \(g=\gcd(w,m)\) and \(q=m/g\). If \(g\nmid z\), then \(K_m(w,z)=0\); otherwise let \(r\) be the unique residue in \(\{0,\ldots,q-1\}\) with \((w/g)r\equiv z/g\pmod q\), taking \(r=0\) for \(q=1\). Set
\[
K_m(w,z)=\frac{2^{q-r-1}}{2^q-1}.
\]
Then
\[
\boxed{\mu_m(a,b,c,d)=\frac{\mathbf1_{\gcd(a,b,m)=1}}{2J_2(m)}\left[\mathbf1_{c\equiv b-a\pmod m}K_m(2(b-a),d+a-2(b-a))+\mathbf1_{d\equiv c-b\pmod m}K_m(2b,c+a-3b)\right].}
\]
The exact number of quadruples having positive density is
\[
\boxed{S(m)=2A(m)-J_2(m),}
\]
where \(A\) is multiplicative with the following prime-power values:
\[
A(p^k)=(p-1)p^{3k-1}+(p-1)^2\sum_{t=1}^{k-1}p^{3k-2t-2}+(p-1)p^{k-1}\quad(p\text{ odd}),
\]
\[
A(2)=3,\qquad A(2^k)=2^{3k-2}+\sum_{t=1}^{k-2}2^{3k-2t-3}+2^k\quad(k\ge2).
\]
Empty sums equal zero. Thus \(S(2)=3\), \(S(3)=32\), \(S(4)=28\), \(S(5)=184\), \(S(6)=96\), and \(S(8)=256\).

## Assumptions and scope
Every modulus \(m\ge2\) is allowed, including composite moduli and prime powers; each coordinate denotes an arbitrary integer residue modulo \(m\). Natural density means a limit through all integers \(N\to\infty\), not merely dyadic subsequences. There are no exclusions for zero coordinates. The function \(K_m\) is the distribution of a geometric random variable reduced modulo a linear congruence; in the case \(q=1\), the same formula gives one.

## Proof
**1. Pair distribution and binary suffixes.** Reznick's Theorem 4.7 [1] (also Deshouillers–Schinzel Theorem 1.1 [2]) states that for every \(m\ge2\), the pair \((s(j),s(j+1))\pmod m\) is uniformly distributed over the \(J_2(m)\) primitive pairs, those satisfying \(\gcd(s(j),s(j+1),m)=1\). For \(h=\nu_2(t+1)\), write \(t=2^{h+1}j+2^h-1\). Its binary suffix consists of a zero followed by \(h\) ones. The pair map under a binary zero is \((u,v)\mapsto(u,u+v)\), while under a one it is \((u,v)\mapsto(u+v,v)\). Consequently, conditioning on \(h\), the pair \((s(t),s(t+1))\) is obtained from \((s(j),s(j+1))\) by the determinant-one matrix \(\bigl(\begin{smallmatrix}h+1&h\\1&1\end{smallmatrix}\bigr)\). It remains uniform over primitive pairs. The natural frequency of any fixed \(h\) is \(2^{-(h+1)}\). The tail \(h\ge H\) has upper natural density at most \(2^{-H}\). Thus the conditional probability series may be summed with no exchange-of-limits gap.

**2. Four consecutive terms.** With \(u=s(t)\) and \(v=s(t+1)\), the recurrence implies
\[
s(t+2)=(2h+1)v-u\qquad(h=\nu_2(t+1)).
\]
Indeed, iterating the odd transition on the suffix of \(t\) gives this identity, including \(t=0\). Thus the four terms at even and odd starting indices are, respectively,
\[
(s(2t),s(2t+1),s(2t+2),s(2t+3))=(u,u+v,v,(2h+2)v-u),
\]
\[
(s(2t+1),s(2t+2),s(2t+3),s(2t+4))=(u+v,v,(2h+2)v-u,(2h+1)v-u).
\]
The first branch forces \(c=b-a\) and \(2h(b-a)\equiv d+a-2(b-a)\pmod m\); the second forces \(d=c-b\) and \(2hb\equiv c+a-3b\pmod m\). Each primitive starting pair has mass \(1/J_2(m)\), and the two parities have equal density. The geometric sum over all solutions to \(wh\equiv z\pmod m\) is precisely \(K_m(w,z)\), proving the formula.

**3. Support and local arithmetic.** Fix a primitive \((a,b)\). In the even branch \(c=b-a\) is fixed and there are exactly \(m/\gcd(2(b-a),m)\) possible \(d\); in the odd branch \(d=c-b\) is fixed and there are exactly \(m/\gcd(2b,m)\) possible \(c\). The branches intersect at precisely \((a,b,b-a,-a)\), which is attained since the relevant linear congruences admit \(h\ge0\). Translation \((a,b)\mapsto(a,b-a)\) is a bijection on primitive pairs. Therefore
\[
S(m)=2\sum_{\gcd(a,b,m)=1}\frac m{\gcd(2b,m)}-J_2(m)=2A(m)-J_2(m).
\]
The Chinese remainder theorem makes \(A\) multiplicative. At an odd prime power \(p^k\), split according to \(t=\nu_p(b)\): when \(t=0\), there are \((p-1)p^{k-1}\) choices of \(b\), \(p^k\) choices of \(a\), and weight \(p^k\); when \(1\le t<k\), there are \((p-1)p^{k-t-1}\) choices of \(b\), \((p-1)p^{k-1}\) of \(a\), and weight \(p^{k-t}\); when \(b=0\), there are \((p-1)p^{k-1}\) choices of \(a\) and weight one. This is the displayed odd-prime expression. At \(2^k\), the weight for an odd \(b\) is \(2^{k-1}\); for \(1\le t\le k-2\) it is \(2^{k-t-1}\); for \(b=0\) or \(\nu_2(b)=k-1\) it is one. Counting these cases gives the displayed \(2\)-power expression. The formula at \(2\) follows by direct two-coordinate counting. Every listed residue quadruple with nonzero mass occurs with positive density, completing the classification.

## Verification
The accompanying standard-library `verify.py` computes the exact mass of all quadruples modulo every integer from \(2\) to \(12\), checks total mass one, counts the support, and compares the closed formulas against direct finite arithmetic. It checks \(4096\) identities on actual consecutive Stern terms and compares a sample modulo \(7\) against the limiting distribution. Running `python3 verify.py` returns `VERIFY_OK`. The proof above, not finite computation, establishes the result for arbitrarily large moduli and indices.

## Relationship to prior work
Reznick [1, Theorem 4.7] proves uniformity of the *pair* state. Deshouillers and Schinzel [2, Theorem 1.1] establish the same pair density using automata. Their theorems are essential inputs but do not state the four-term geometric joint law or the multiplicative arithmetic formula for the number of attainable four-term residue blocks. Reznick's Corollary 2.4 gives a general dyadic identity, which is compatible with the derivation but does not itself enumerate four-block support. Exact three-term densities, where just one extra residue is recorded, do not determine the joint law of both extra residues; the two-branch intersection and local support census are additional features of length four.

## Limitations
This result is for exactly four consecutive terms at a fixed modulus and does not assert independence of overlapping blocks or a limit as the modulus varies. Pair equidistribution is taken from published theorems, not reproved here. The method may extend to longer blocks but no such extension is claimed. Earlier equivalent formulas in unindexed literature are a residual originality risk. Finite checks cannot prove the infinite statement.

## References
[1] B. Reznick, *Regularity Properties of the Stern Enumeration of the Rationals*, arXiv:math/0610601v1, first publicly posted 19 October 2006, Sections 2 and 4. https://arxiv.org/abs/math/0610601

[2] J.-M. Deshouillers and A. Schinzel, *The modular distribution of Stern's sequence*, Banach Center Publications **118** (2019), 37–44, Theorem 1.1. https://doi.org/10.4064/bc118-3
