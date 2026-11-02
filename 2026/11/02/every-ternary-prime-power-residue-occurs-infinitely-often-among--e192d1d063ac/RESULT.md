# Every ternary prime-power residue occurs infinitely often among Catalan numbers

## Finding

Let \(C_n=(n+1)^{-1}\binom{2n}{n}\) be the \(n\)-th Catalan number for \(n\ge0\). For every integer \(k\ge1\), **each residue modulo \(3^k\) is attained by infinitely many Catalan numbers**. Equivalently, the set of Catalan numbers is dense in the ring of \(3\)-adic integers.

The result has explicit, uniform witnesses. Put \(L=k+2\) and define the integer units
\[
 c_k\equiv\binom{2\cdot3^L}{3^L}\pmod{3^k},\qquad
 d_k\equiv\frac13\binom{4\cdot3^L}{2\cdot3^L}\pmod{3^k}.
\]
For integers \(v,t\ge0\), set
\[
 n_{k;v,t}=\sum_{i=1}^{v}2\cdot3^{Li}
       +\sum_{i=v+1}^{v+t}3^{Li}.
\]
Then
\[
 \boxed{C_{n_{k;v,t}}\equiv3^v d_k^v c_k^t\pmod{3^k}.}
\]
Moreover, \(c_k\) generates the unit group \((\mathbb Z/3^k\mathbb Z)^\times\), whose order is \(2\cdot3^{k-1}\). Varying \(t\) therefore gives every residue of valuation exactly \(v\) when \(0\le v<k\), and choosing \(v\ge k\) gives zero. Raising \(t\) by multiples of \(2\cdot3^{k-1}\) yields infinitely many distinct witnesses for each residue.

## Assumptions and scope

All valuations \(\nu_3\) are valuations of nonzero integers. For an integer \(N\ge0\), write
\[
 U_k(N)=\frac{N!}{3^{\nu_3(N!)}}\pmod{3^k}.
\]
This is a unit modulo \(3^k\). The theorem concerns all \(n\ge0\), all \(k\ge1\), and all residue classes modulo \(3^k\); it does not assert a positive asymptotic frequency of any fixed residue class. All displayed divisions by \(3\) are exact integer divisions, while inverses in congruences are taken only of units.

## Proof

**1. A factorial-unit formula.** Fix \(k\ge1\), write \(m=3^k\), and, for \(0\le r<m\), put
\[
 A_k(r)=\prod_{\substack{1\le j\le r\\3\nmid j}}j\pmod m,
 \qquad A_k(0)=1.
\]
The product of all units modulo \(m\) is \(-1\), since all units except \(1\) and \(-1\) pair with their distinct inverses. Splitting the integers not divisible by \(3\) into full intervals of length \(m\), and recursively removing factors of \(3\) from \(N!\), gives the finite product
\[
 U_k(N)\equiv
 \prod_{j\ge0}
 (-1)^{\lfloor N/3^{k+j}\rfloor}
 A_k\!\left(\lfloor N/3^j\rfloor\bmod m\right)
 \pmod m.
 \tag{1}
\]
Every factor after \(j>\log_3 N\) is one. This formula follows directly from \(U_k(N)=\prod_{3\nmid s\le N}s\;U_k(\lfloor N/3\rfloor)\).

**2. Isolated-digit factorization.** For \(n\ge0\) write \(B_n=\binom{2n}{n}\) and
\[
 W_k(n)=3^{-\nu_3(B_n)}B_n\pmod m
       \equiv U_k(2n)U_k(n)^{-2}\pmod m.
 \tag{2}
\]
Suppose \(n=\sum_i a_i3^{e_i}\), where each \(a_i\) is \(1\) or \(2\), every \(e_i\ge k+2\), and consecutive occupied positions are separated by at least \(k+2\). Its base-three expansion consists of isolated occupied digits. Doubling a digit \(1\) produces digit \(2\) at the same position, while doubling a digit \(2\) produces digits \(1,1\) at that position and the next; these doubled blocks are disjoint. Thus, for every \(j\), the length-\(k\) base-three windows forming \(\lfloor n/3^j\rfloor\bmod m\) and \(\lfloor2n/3^j\rfloor\bmod m\) meet at most one original occupied block. Their nonzero \(A_k\)-factors in (1) consequently separate by blocks. The sign exponents in (1) separate too, because truncating either digit expansion at any position involves no cross-block carries. Therefore
\[
 W_k(n)\equiv\prod_i W_k(a_i3^{e_i})\pmod m.
 \tag{3}
\]
The same absence of cross-block carries in adding \(n+n\) and Kummer's theorem give
\[
 \nu_3(B_n)=\#\{i:a_i=2\}.
 \tag{4}
\]
For one block, the nontrivial length-\(k\) windows of \(a3^e\) and \(2a3^e\) depend only on the offset of the window from \(e\), not on \(e\) itself, once \(e\ge k+2\). The relative sign exponent in (2) is zero for \(a=1\), and for \(a=2\) consists of the single carry at position \(e+1\). Consequently, \(W_k(a3^e)\) is independent of \(e\ge k+2\). For \(a=1\) it is \(c_k\); for \(a=2\) it is \(d_k\), because (4) gives valuation exactly one in the latter case.

**3. The explicit Catalan congruence.** The index \(n_{k;v,t}\) has \(v\) isolated digits \(2\) followed by \(t\) isolated digits \(1\). Equations (3) and (4) give
\[
 \nu_3(B_{n_{k;v,t}})=v,
 \qquad W_k(n_{k;v,t})\equiv d_k^v c_k^t\pmod m.
\]
All occupied positions exceed \(k\), so \(n_{k;v,t}\equiv0\pmod m\). Thus its denominator \(n_{k;v,t}+1\) is a unit congruent to \(1\pmod m\), and the Catalan formula gives
\[
 C_{n_{k;v,t}}\equiv3^v d_k^v c_k^t\pmod m.
 \tag{5}
\]

**4. A primitive unit.** For every integer \(e\ge1\), the identity
\[
 \binom{2\cdot3^e}{3^e}
   =2\prod_{j=1}^{3^e-1}\left(1+\frac{3^e}{j}\right)
\]
holds in the \(3\)-adic integers. Terms with \(\nu_3(j)\le e-2\) are \(1\pmod9\); the two remaining factors, at \(j=3^{e-1}\) and \(j=2\cdot3^{e-1}\), multiply to
\[
 (1+3)(1+3/2)\equiv4\cdot7\equiv1\pmod9.
\]
Hence \(\binom{2\cdot3^e}{3^e}\equiv2\pmod9\). In particular, \(c_k\equiv2\pmod9\) whenever \(k\ge2\), and \(c_1\equiv2\pmod3\). For \(k\ge2\), \(c_k\) is odd modulo \(3\) and \(\nu_3(c_k^2-1)=1\). The lifting-the-exponent identity gives
\[
 \nu_3\!\left(c_k^{2\cdot3^h}-1\right)=h+1
 \qquad(h\ge0),
\]
for any integer representative satisfying \(c_k\equiv2\pmod9\). Thus the order of \(c_k\) modulo \(3^k\) is exactly \(2\cdot3^{k-1}\), also for \(k=1\).

**5. All residue classes, infinitely often.** Fix \(a\pmod m\). If \(a=0\), equation (5) with \(v=k\) and arbitrary \(t\) supplies infinitely many distinct indices. Otherwise let \(0\le v<k\) be its exact truncated \(3\)-adic valuation. Since \(d_k\) is a unit and \(c_k\) generates all units modulo \(m\), there exists \(t\ge0\) with
\[
 d_k^v c_k^t\equiv a/3^v\pmod{3^{k-v}}.
\]
Equation (5) gives \(C_{n_{k;v,t}}\equiv a\pmod m\). The same congruence holds upon replacing \(t\) by \(t+j(2\cdot3^{k-1})\) for every \(j\ge0\), producing strictly increasing indices. This proves both claims.

## Verification

The standalone, standard-library script `verify.py` computes factorial units modulo \(3^k\) exactly, without constructing the enormous factorials. Run `python3 verify.py`. It cross-checks the oracle against exact integer Catalan numbers for \(0\le n<400\), checks the isolated-block congruence for \(1\le k\le7\) with two block separations and multiple valuations, tests primitive-root orders, and exhaustively realizes all residues modulo \(3^k\) for \(1\le k\le5\). Its expected terminal line begins `VERIFY_OK`. The unrestricted theorem is proved above; finite testing is corroboration only.

## Relationship to prior work

Rowland and Yassawi explicitly asked in Open question 3.6 of their 2013 preprint whether any residue modulo some power of three is forbidden for the Catalan sequence. Their finite-automaton methods establish congruence decision procedures for fixed powers, not this uniform negative answer. Krattenthaler and Müller (2013, Section 12) derive generating-function congruences modulo powers of three, including explicit formulas modulo \(9\) and \(27\); their inspected Section 12 does not establish the all-exponent surjectivity theorem. Chen and Jiang (2013, Theorem 1) establish eventual constancy and pairwise distinctions only for the thin subsequences \(C_{p^j-a}\) modulo \(p^k\), not surjectivity of the full Catalan sequence. Deutsch and Sagan (2006) give a characterization modulo \(3\). Burns (2017) establishes full residue coverage modulo primes \(p\ge5\) and comments on differences for prime powers, without the all-power-of-three statement. The present proof uses sparse ternary digits, unit factorial blocks, and a primitive generator to give explicit witnesses for all \(3^k\) at once.

## Limitations

The result does not concern powers of other primes. It does not give a useful small upper bound on the first index attaining a prescribed residue: explicit witnesses can be enormous. Infinite occurrence is not positive natural density. Priority beyond the cited and inspected accessible literature has not been independently certified.

## References

1. Eric Rowland and Reem Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635, first public 2013-10-31, Open question 3.6 and Section 3.1. https://arxiv.org/abs/1310.8635
2. Christian Krattenthaler and Thomas W. Müller, *A method for determining the mod-\(3^k\) behaviour of recursive sequences*, arXiv:1308.2856, 2013-08-13, Section 12. https://arxiv.org/abs/1308.2856
3. Eric Deutsch and Bruce E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, Journal of Number Theory 117 (2006), Theorem 5.2. https://users.math.msu.edu/users/bsagan/Papers/Old/ccm.pdf
4. Rob Burns, *The Catalan numbers have no forbidden residue modulo primes*, arXiv:1703.02705, 2017-03-08. https://arxiv.org/abs/1703.02705
5. Yong-Gao Chen and Wen Jiang, *Catalan numbers modulo a prime power*, Integers 13 (2013), #A36, first published 2013-06-14, Theorem 1. https://math.colgate.edu/~integers/n36/n36.pdf
