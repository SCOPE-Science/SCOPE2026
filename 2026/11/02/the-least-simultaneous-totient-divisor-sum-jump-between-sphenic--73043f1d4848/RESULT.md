# The least simultaneous totient–divisor-sum jump between sphenic integers is 320

## Finding

Call a positive integer *sphenic* if it is a product of three **distinct** primes. Let \(\varphi\) denote Euler's totient and \(\sigma\) the sum of positive divisors. For a positive integer \(h\), consider two sphenic integers \(n\) and \(n+h\) obeying both equal-increment identities
\[
\varphi(n+h)-\varphi(n)=h,\qquad
\sigma(n+h)-\sigma(n)=h.
\]
**The least possible positive increment is exactly \(320\).** The threshold is attained by
\[
 n=11\cdot23\cdot29=7337,\qquad
 n+320=13\cdot19\cdot31=7657.
\]
In particular, the complete strict subthreshold consists of **no admissible prime-triple pairs**, without any bound on either integer.

## Assumptions and scope

The two arguments are arbitrary positive products of exactly three different primes. A factor may be repeated between the two arguments *a priori*; that possibility is excluded within the proof. No primality restriction is imposed on the shift \(h\), which is a positive integer to be minimized. The result neither covers nonsquarefree integers nor claims all solutions for a given shift.

## Proof

**1. Equal increments force equal two symmetric sums.** Write
\(n=p_1p_2p_3\), \(n+h=q_1q_2q_3\), with all primes distinct within each triple. Let \(S_p=\sum p_i\), \(T_p=\sum_{i<j}p_ip_j\), and define \(S_q,T_q\) analogously. Expanding multiplicative formulas,
\[
\varphi(n)=n-T_p+S_p-1,\quad\sigma(n)=n+T_p+S_p+1.
\]
The two asserted differences equal \(h\) if and only if
\[
S_p=S_q,\qquad T_p=T_q.
\]
For \(P(X)=\prod_i(X-p_i)\) and \(Q(X)=\prod_i(X-q_i)\), therefore,
\[
P(X)-Q(X)=\prod_iq_i-\prod_ip_i=h
\]
identically. Since \(h>0\), no prime belongs to both triples; a common root would make \(h=0\).

**2. Only odd prime factors occur, and normalize the smallest.** Since \(\varphi(m)\) is even for every \(m>2\), the shift \(h\) is even. Thus \(n\) and \(n+h\) have the same parity. If they were even, both prime triples would contain \(2\), contradicting the absence of common roots. All six primes are odd.

Let \(t\) be the least of the six primes. It belongs to the \(p\)-triple: if it belonged to the \(q\)-triple, \(P(t)\) would be a product of three negative factors, hence negative, contradicting \(P(t)-Q(t)=h>0\). Rename the triples in ascending order as
\[
(p_1,p_2,p_3)=(t,t+u,t+v),\qquad
(q_1,q_2,q_3)=(t+a,t+b,t+c),
\]
where \(0<u<v\), \(0<a<b<c\), and the five offsets \(u,v,a,b,c\) are positive **even** integers. From the symmetric-sum equalities,
\[
u+v=a+b+c=:S,\qquad uv=ab+ac+bc=:T.
\]
Evaluating \(P(t)-Q(t)\) gives \(h=abc\). Thus \(u,v\) are the distinct positive even roots of \(X^2-SX+T\); in particular
\[
\Delta=S^2-4T=(v-u)^2>0
\]
must be a positive square. These constraints are necessary for every candidate, independent of the magnitude of \(t\).

**3. A complete, short bound-free candidate census for \(h<320\).** Because \(a,b,c\) are strictly increasing even integers with \(abc<320\), we have \(a(a+2)(a+4)<320\), hence \(a\in\{2,4\}\). The inequality \(ab(b+2)<320\) leaves only five possibilities for \((a,b)\), with every admissible even \(c\) given in the following table:

| \((a,b)\) | Full possible range of \(c\) | \(\Delta\) a nonnegative square only when |
|---|---|---|
| \((2,4)\) | \(6,8,\ldots,38\) | \(c=12\), \(\Delta=4\), \((u,v)=(8,10)\) |
| \((2,6)\) | \(8,10,\ldots,26\) | \(c=16\), \(\Delta=16\), \((u,v)=(10,14)\) |
| \((2,8)\) | \(10,12,\ldots,18\) | \(c=18\), \(\Delta=0\), \((u,v)=(14,14)\) |
| \((2,10)\) | \(12,14\) | none |
| \((4,6)\) | \(8,10,12\) | none |

The table comprises \(17+10+5+2+3=37\) checked triples, with integer arithmetic using the displayed formula for \(\Delta\). The zero-discriminant case repeats an element and cannot represent three distinct primes. Consequently the only valid normalized pair shapes below \(320\) are
\[
\begin{aligned}
 h=96:&\quad (0,8,10)\text{ versus }(2,4,12),\\
 h=192:&\quad (0,10,14)\text{ versus }(2,6,16).
\end{aligned}
\]
For each of the two rows, the six offsets represent every residue class modulo \(3\). If \(t>3\), one of the six numbers is divisible by \(3\) and strictly exceeds \(3\), hence cannot be prime. If \(t=3\), the first row contains \(t+12=15\) and the second contains \(t+6=9\); again a number is composite. Since \(t\) is an odd prime, these are all cases. Thus no such pair exists for \(0<h<320\).

**4. Attainment.** The six numbers \(11,23,29,13,19,31\) are distinct primes. Both triples have sum \(63\) and second elementary symmetric sum \(1239\), while their products differ by \(320\). Directly,
\[
\begin{array}{c|cc}
 &7337&7657\\\hline
\varphi&6160&6480\\
\sigma&8640&8960
\end{array}
\]
proving both equal-increment identities for \(h=320\). Combining the strict lower bound and attainment proves the theorem.

## Verification

The accompanying standard-library program `verify.py` implements the complete \(37\)-triple discriminant enumeration with exact integer square roots, checks the two modular obstructions, primality of the six witness factors, both symmetric sums and the actual \(\varphi\)- and \(\sigma\)-values. Run `python3 verify.py`. Its expected output includes `tested_normalized_even_offset_triples=37` and `jump=320`. The finite check is exhaustive **only after** the algebraic reduction in Steps 1–2; the universal assertion is supplied by those steps and the finite proof in Step 3.

## Relationship to prior work

Choudhury and Wei, *Prime Quadruplets and Jump Conditions on Arithmetic Functions* (arXiv:2606.10331v1; first public version 2026-06-09), investigate the fixed shift \(12\), give its complete squarefree-semiprime case, and study prime-power obstructions. The present result instead varies the positive shift and isolates its *first possible value* when **both arguments have three distinct prime factors**. It neither claims a new fixed-\(12\) solution nor extends the conjecture to all integers.

The common-sum/common-pair-sum reduction is an ideal degree-two Prouhet–Tarry–Escott equality. Such equal-power-sum identities are classical; no novelty is claimed for the general construction. The new arithmetic point is a sharp **prime-realizable** shift threshold with a no-unbounded-search proof. OEIS A056777 tabulates the different, fixed-\(12\) condition; it is not a general-variable-shift table.

## Limitations

The theorem is restricted to squarefree integers with exactly three prime factors on **both** sides, and to simultaneous increments equal to the argument difference. It does not determine the first shift if other factorization types are permitted, nor all pairs at shift \(320\), nor infinite families. Priority searches cannot exclude unindexed treatments of the corresponding prime-restricted Prouhet problem. The computation independently tests the \(37\) finite candidates but does not replace the derivation proving that the list is exhaustive.

## References

1. H. Roy Choudhury and S. Wei, *Prime Quadruplets and Jump Conditions on Arithmetic Functions*, arXiv:2606.10331v1 (2026-06-09). https://arxiv.org/abs/2606.10331
2. E. W. Weisstein, *Prouhet–Tarry–Escott Problem*, MathWorld. https://mathworld.wolfram.com/Prouhet-Tarry-EscottProblem.html
3. OEIS A056777, *Composite numbers k such that both phi(k+12)=phi(k)+12 and sigma(k+12)=sigma(k)+12*. https://oeis.org/A056777
