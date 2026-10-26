# Congruence normal forms and finite-quotient growth of arithmetic overflow semirings

## Finding

Fix an integer \(k\ge 1\), and let \(L_k=\{\omega_1<\cdots<\omega_k\}\) be a chain of \(k\) formal overflow levels. Let \(S_k=\mathbb N_0\uplus_{\mathrm{ord}}L_k\) be the commutative overflow semiring with ordinary addition and multiplication on \(\mathbb N_0\), and with
\[
\omega_i+\omega_j=\omega_i\omega_j=\omega_{\max(i,j)},\qquad
n+\omega_i=\omega_i\ (n\in\mathbb N_0),\qquad
n\omega_i=\begin{cases}0&n=0,\\\omega_i&n>0.\end{cases}
\]
A congruence is an equivalence relation compatible with both semiring operations.

**Classification.** Every congruence on \(S_k\) belongs to exactly one of the following three disjoint types.

1. **Universal:** all elements are equivalent.
2. **Separated:** no natural number is equivalent to an overflow level. The restriction to the natural numbers is either equality or one of the eventual-period congruences \(\theta_{t,p}\), with arbitrary integers \(t,p\ge1\), where all numbers below \(t\) are singleton classes and the numbers at least \(t\) are equivalent exactly when they differ by a multiple of \(p\). The overflow restriction is an arbitrary partition of \(L_k\) into consecutive intervals. The two choices are independent.
3. **Absorbed:** choose \(t\ge1\) and a partition of \(L_k\) into consecutive nonempty intervals. Every number below \(t\) is a singleton; all numbers at least \(t\) are equivalent to every overflow level in the *first* interval; the remaining intervals are separate congruence classes.

In particular, there are exactly \(2^{k-1}\) congruences of infinite index, namely the separated congruences with equality on \(\mathbb N_0\). Every other congruence has finite index.

Let \(c_k(h)\) be the number of *distinct congruence kernels* whose quotient semirings have exactly \(h\) elements (not the number of isomorphism classes of quotient semirings). Then \(c_k(1)=1\), and for \(h\ge2\),
\[
c_k(h)=\sum_{b=1}^{\min(k,h-1)}\binom{k-1}{b-1}(h-b).
\]
Consequently the exact finite-quotient-size generating function is
\[
\boxed{\sum_{h\ge1}c_k(h)z^h=z+\frac{z^2(1+z)^{k-1}}{(1-z)^2}.}
\]
For every \(h\ge k+1\), this simplifies to the exact linear law
\[
\boxed{c_k(h)=2^{k-1}\left(h-\frac{k+1}{2}\right).}
\]
All congruences are finitely generated as semiring congruences; in particular \(S_k\) is congruence-Noetherian. The semiring is residually finite.

## Assumptions and scope

Throughout, \(k\) is an arbitrary positive integer. The base \(\mathbb N_0\) consists of ordinary nonnegative integers with their usual arithmetic. The levels \(\omega_i\) are distinct from every integer, and the displayed operations specify the whole semiring; \(0\) is absorbing under multiplication. A *consecutive-interval partition* of \(L_k\) is a partition into blocks of consecutive \(\omega_i\), obtainable by choosing which of the \(k-1\) adjacent gaps to retain. If exactly \(b\) blocks remain, their number is \(\binom{k-1}{b-1}\).

For \(t,p\ge1\), define \(\theta_{t,p}\) on \(\mathbb N_0\) by
\[
a\mathrel{\theta_{t,p}}b\quad\Longleftrightarrow\quad
\bigl(a=b<t\bigr)\ \text{or}\ \bigl(a,b\ge t\text{ and }a\equiv b\pmod p\bigr).
\]
The equality relation is written \(\Delta\). These are restrictions of semiring congruences, not merely equivalence relations. Quotient cardinalities may be infinite.

## Proof

**Step 1: zero cannot merge in a proper congruence.** Suppose \(0\sim x\ne0\). If \(x\in\mathbb N_0\) is positive, multiply by \(\omega_1\) to get \(0\sim\omega_1\); if \(x\in L_k\), then also \(0\sim\omega_j\) for some \(j\). From \(0\sim\omega_j\), adding \(1\) gives \(1\sim\omega_j\). Thus \(0\sim1\), and multiplying by any semiring element shows \(0\sim y\) for every \(y\in S_k\). Consequently, in every nonuniversal congruence, \(\{0\}\) is a singleton.

**Step 2: congruences of the positive integers are eventually periodic.** In any nonuniversal congruence, restrict to \((\mathbb N_0,+)\). If the restriction is not equality, choose the least \(t\) which is equivalent to some larger integer, then the least \(p>0\) such that \(t\sim t+p\). Since \(0\) is isolated, \(t\ge1\). Addition gives \(t+r\sim t+p+r\) for every \(r\ge0\). No smaller number can merge with any larger number by minimality of \(t\). If two distinct representatives \(t+i\) and \(t+j\), where \(0\le i<j<p\), were equivalent, adding \(p-i\) and using periodicity would give \(t\sim t+j-i\), contradicting the choice of \(p\). Hence the restriction is exactly \(\theta_{t,p}\). Conversely, every \(\theta_{t,p}\) is a semiring congruence on \(\mathbb N_0\): addition preserves the period and threshold, and multiplication by a positive integer does as well; multiplication by zero is trivial.

**Step 3: overflow blocks are consecutive.** The restriction of a congruence to \(L_k\) respects the maximum operation. If \(\omega_i\sim\omega_j\) with \(i<j\), then for every \(i<r<j\), taking the maximum with \(\omega_r\) yields \(\omega_r\sim\omega_j\), and hence \(\omega_i\sim\omega_r\). Therefore each equivalence class is a consecutive interval. Conversely, a partition into consecutive intervals defines a congruence for maximum.

**Step 4: the separated case.** If no integer is equivalent to an overflow level, Steps 2 and 3 describe the two restrictions. The only remaining mixed-operation tests are automatic: both addition and multiplication of a *positive* integer with any overflow element return that overflow element, while \(0\omega_i=0\). Thus the restrictions can be chosen independently, yielding every separated congruence and no other one.

**Step 5: the absorbed case.** Suppose \(n\sim\omega_j\) for some integer \(n>0\). Adding any nonnegative integer gives \(n+r\sim\omega_j\) for every \(r\ge0\). Multiplying the original equivalence by \(\omega_1\) gives \(\omega_1\sim\omega_j\); hence the class attached to the integer tail is the first interval block of \(L_k\). Let \(t\) be the least integer equivalent to any overflow level. Then every integer at least \(t\) belongs to the first overflow class. No integer smaller than \(t\) is equivalent to one at least \(t\), for that would make it equivalent to an overflow element. Nor can two distinct integers below \(t\) be equivalent: iterating their positive difference by addition would eventually connect the smaller integer to the tail. Thus these integers are singleton classes, giving exactly the absorbed normal form. Conversely, the form is compatible with addition and multiplication: positive natural arithmetic preserves the tail, mixed operations with an overflow level yield that level, and the quotient of the overflow chain respects maximum. No further restrictions occur.

**Step 6: enumeration by quotient size.** If the overflow partition has \(b\) blocks, a separated congruence \(\theta_{t,p}\) has \(t+p+b\) quotient classes, while an absorbed congruence with cutoff \(t\) has \(t+b\). Separated congruences with \(\Delta\) have infinitely many quotient classes, and there are \(2^{k-1}\) of them. For fixed \(b\), the generating function of finite separated quotients is \(z^b(z/(1-z))^2\), whereas that of absorbed quotients is \(z^b z/(1-z)\). Summing over overflow partitions and adding the universal congruence gives
\[
\begin{aligned}
\sum_{h\ge1}c_k(h)z^h
&=z+\sum_{b=1}^{k}\binom{k-1}{b-1}z^b
\left(\frac{z^2}{(1-z)^2}+\frac{z}{1-z}\right)\\
&=z+\frac{z^2(1+z)^{k-1}}{(1-z)^2}.
\end{aligned}
\]
Extracting the coefficient for \(h\ge2\) gives the stated finite sum; once \(h\ge k+1\), all \(b=1,\ldots,k\) appear and the two binomial moments give the linear formula.

**Step 7: finite generation and residual finiteness.** A separated periodic congruence is generated by the pair \((t,t+p)\) and finitely many pairs joining endpoints of overflow blocks; for a separated equality congruence only the block pairs are needed. An absorbed congruence is generated by \((t,\omega_1)\) and the overflow block pairs. The universal congruence is generated by \((0,1)\). Thus every congruence is finitely generated. To separate any distinct pair of elements, choose a separated \(\theta_{t,1}\) with \(t\) larger than both integers appearing in the pair, and take the discrete partition of the overflow chain. This gives a finite quotient distinguishing the pair; hence \(S_k\) is residually finite.

## Verification

The standalone `verify.py` constructs finite quotients of \(S_k\), enumerates **every set partition** of each finite carrier, and independently checks the two semiring operations for congruence compatibility. It compares the resulting sets against the normal forms, including both threshold-absorbed quotients and periodic separated quotients.

The successful run returned `VERIFY_OK` for twelve absorbed quotients, and `QUOTIENT_VERIFY_OK` for nine periodic quotients, with explicit counts. The largest tested carrier had seven elements. These finite exhaustive calculations check boundary cases and cross-operation compatibility, but do not replace Steps 1–7 for the infinite family. The formula for quotient-index counts also follows algebraically from the normal forms and does not depend on observed initial terms.

The verifier uses only Python's standard library and can be run with `python3 verify.py`.

## Relationship to prior work

Nasehpour (2026) introduces the overflow semiring \(A\uplus_{\mathrm{ord}}L\), defines its operations, and classifies its ideals, primes, and chain conditions. The present result specializes to \(A=\mathbb N_0\) but studies a different invariant: **all semiring congruences and the exact number of their finite quotient kernels at each index**. Neither the ideal description nor the Krull-dimension formula is a congruence classification.

Sen (2025), Example 3.1, explicitly recalls the classical description of monogenic additive congruences \(t\sim t+p\) and the congruence-Noetherian notion. That fact is used and reproved above; it is not claimed as new. The additional issue is compatibility with multiple absorbing overflow levels, including the forced attachment of any integer tail to the least overflow block, followed by the all-index quotient census.

The one-level case \(k=1\) recovers the classical semiring of extended natural numbers \(\mathbb N_0\cup\{\infty\}\). Priority for individual one-level consequences is not asserted. The exact multilevel classification and its uniform index generating function were not located in the inspected sources.

## Limitations

The claim concerns finite totally ordered overflow components and the natural-number base. It does not classify congruences for general positive information algebras, incomparable overflow levels, or infinite chains, and it counts congruence kernels rather than isomorphism types of quotient semirings. The originality comparison is bounded by accessible indexed literature; unindexed or older semiring-congruence calculations may overlap.

## References

1. Peyman Nasehpour, *Algebraic properties of overflow semirings*, arXiv:2606.00916 (first posted 2026-05-30), https://arxiv.org/abs/2606.00916; especially Definition 1.1, Section 3 and Corollary 3.19.
2. Snehinh Sen, *Finitely Generated Congruences in Semirings and Canonical Positive Models*, arXiv:2511.12815 (first posted 2025-11-16), https://arxiv.org/abs/2511.12815; Section 3, Example 3.1.
3. *Extended natural numbers*, https://en.wikipedia.org/wiki/Extended_natural_numbers, consulted for the standard one-level terminology, not for the multilevel classification.
