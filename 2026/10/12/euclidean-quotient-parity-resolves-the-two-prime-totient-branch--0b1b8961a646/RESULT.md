# Euclidean quotient parity resolves the two-prime totient branch
## Finding
Let \(1<p<q\) be coprime odd integers. Run the ordinary Euclidean algorithm
\[
r_{-1}=q,\qquad r_0=p,\qquad r_{i-1}=c_i r_i+r_{i+1},
\]
with positive quotients \(c_0,\ldots,c_m\), terminal values \(r_m=1\) and \(r_{m+1}=0\), and the canonical final quotient \(c_m\ge2\). Let \(a,b\) be the unique least positive integers satisfying
\[
ap-bq=1,\qquad 0<a<q,\qquad 0<b<p.
\]
Then
\[
a\equiv c_0+\cdots+c_m\pmod 2.
\]
Because \(p\) and \(q\) are odd, \(a\) and \(b\) have opposite parity. Thus the parity of the total Euclidean quotient sum predicts exactly which least positive Bézout coefficient is even.

For distinct odd primes \(p<q\), integers \(e,f\ge1\), and \(n=p^e q^f\), let
\[
T(n)=\left|\left\{1\le m\le n:m\text{ odd},\ \gcd(m,n)=\gcd((m-1)/2,n)=1\right\}\right|
\]
and let
\[
S(n)=n\prod_{\ell\mid n}\left(1-\frac{2}{\ell}\right).
\]
Then the two possibilities in Renshaw's Corollary 6 are selected explicitly by
\[
T(n)=
\begin{cases}
\dfrac{S(n)+1}{2},&c_0+\cdots+c_m\text{ is odd},\\[4pt]
\dfrac{S(n)-3}{2},&c_0+\cdots+c_m\text{ is even}.
\end{cases}
\]
In particular, the branch is independent of the exponents \(e\) and \(f\).

## Assumptions and scope
The Euclidean quotients are those of the standard division algorithm for the ordered pair \(q>p>1\); equivalently \(q/p=[c_0;\ldots,c_m]\) with the canonical last partial quotient at least \(2\). The parity theorem holds for all coprime odd integers \(p,q\), not only primes. The totient corollary is stated for distinct odd primes because that is the two-prime-power case of the source's Corollary 6. No claim is made here for integers with three or more distinct odd prime divisors.

## Proof
For an integer \(c\ge1\), set
\[
M(c)=\begin{pmatrix}c&1\\1&0\end{pmatrix}.
\]
The continued-fraction matrix identity gives
\[
P=M(c_0)\cdots M(c_m)=\begin{pmatrix}q&u\\p&v\end{pmatrix}
\]
for integers \(u,v\) with
\[
pu-qv=(-1)^m.
\]
If \(m\) is even then the least positive solution of \(ap-bq=1\) is \((a,b)=(u,v)\). If \(m\) is odd then it is \((a,b)=(q-u,p-v)\). Since \(q\) is odd,
\[
a\equiv u+m\pmod2. \tag{1}
\]

Reduce the matrix product modulo \(2\). An even quotient contributes
\[
E=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
which acts as a transposition on the three nonzero vectors of \(\mathbb F_2^2\), whereas an odd quotient contributes
\[
O=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\]
which acts as a three-cycle. Because \(p\) and \(q\) are odd, the first column of \(P\) modulo \(2\) is \((1,1)^T\). There are only two matrices in \(\mathrm{GL}_2(\mathbb F_2)\) with that first column: the one with upper-right entry \(0\) is a transposition, and the one with upper-right entry \(1\) is a three-cycle. If \(e_0\) denotes the number of even quotients, the permutation sign of the product is \((-1)^{e_0}\). Hence
\[
u\equiv1+e_0\pmod2.
\]
If \(o_0\) is the number of odd quotients, then \(e_0+o_0=m+1\), so
\[
u\equiv m+o_0\pmod2.
\]
Combining this with (1) yields
\[
a\equiv o_0\equiv c_0+\cdots+c_m\pmod2,
\]
which proves the parity theorem.

Now let \(n=p^e q^f\), put \(h=n/(pq)\), and use the source's sets \(B_p,C_p\) of odd residues divisible respectively by \(p\) and congruent to \(1\) modulo \(p\). The two cross-intersections are governed by the least positive solution \(ap-bq=1\). Writing \(b=(ap-1)/q\), one has \(b\) even exactly when \(a\) is odd. In that case each cross-intersection has cardinality \((h+1)/2\); otherwise each has cardinality \((h-1)/2\). Since
\[
|B_{pq}|=|C_{pq}|=\frac{h+1}{2},
\]
inclusion-exclusion gives
\[
T(n)=\frac{S(n)-1+2\delta}{2},
\]
where \(\delta=1\) when \(a\) is odd and \(\delta=-1\) when \(a\) is even. Substituting the proved quotient-sum parity gives exactly the displayed two-branch formula.

## Verification
The proof is symbolic and covers the full stated infinite domain. The accompanying `verify.py` is corroborative: it checks the Bézout parity identity for every coprime odd pair \(1<p<q\) with \(p\le301\) and \(q\le401\), and checks the two-prime-power formula by direct enumeration for all generated cases with \(n\le30000\). Replaying the packaged checker gives `VERIFY_OK bezout_parity_pairs=15169 two_prime_power_cases=304` followed by sample values.

## Relationship to prior work
Renshaw introduces \(T(n)\), proves that for \(n=p^e q^f\) it is either \((S(n)-3)/2\) or \((S(n)+1)/2\), and explicitly states that it is not obvious how to predict which value occurs. The same paper ends by asking, for coprime odd \(p,q\), which of the least positive coefficients in \(ap-bq=1\) is even. The theorem above answers that stated parity problem and simultaneously resolves the branch ambiguity in Corollary 6.

Classical continued-fraction theory supplies the matrix identity used in the proof. Wu and Xu discuss modular inverses, Euclidean state matrices, and continued fractions in a broader algorithmic setting, but the inspected material does not state the quotient-sum parity law or its consequence for Renshaw's totient. Targeted searches for equivalent modular-inverse parity criteria and for the exact two-prime branch did not locate a covering statement. This is evidence against overlap, not a proof of worldwide novelty.

## Limitations
The result is an elementary parity classification; it does not give a closed formula for \(T(n)\) when three or more distinct odd primes divide \(n\), nor does it address the even-argument cases of the source beyond what is already known there. The computational replay is finite and is not used as proof of the universal statements. A residual originality risk is that the continued-fraction parity identity may exist as unindexed folklore under different terminology.

## References
1. James Renshaw, *A Totient Function Associated with Variants of Groups*, arXiv:2603.13939v1, 14 March 2026; especially Lemma 4, Corollary 6, and the final problem.
2. Han Wu and Guangwu Xu, *Qin's Algorithm, Continued Fractions and 2-dimensional Lattices*, arXiv:2310.09103v2.
