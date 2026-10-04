# Exact additive energy of the finite-field quartic graph
## Finding
Let \(F\) be a finite field of order \(q\) and characteristic different from \(2\) and \(3\). Write \(\chi\) for the quadratic character of \(F\), extended by \(\chi(0)=0\), and set
\[
C_4=\{(t,t^4):t\in F\}\subset F^2.
\]
Then the additive energy
\[
E(C_4)=\#\{(a,b,c,d)\in F^4:(a,a^4)+(b,b^4)=(c,c^4)+(d,d^4)\}
\]
is
\[
E(C_4)=3q^2-q-1-(q-1)(1+\chi(-3))^2.
\]
Since \(\chi(-3)=1\) exactly when \(F\) contains a primitive cube root of unity, this is equivalently
\[
E(C_4)=
\begin{cases}
3q^2-5q+3,&q\equiv1\pmod 3,\
3q^2-q-1,&q\equiv2\pmod 3.
\end{cases}
\]
The number of nontrivial ordered additive collisions, after removing the \(2q^2-q\) permutation collisions, is therefore \((q-1)(q-3)\) when \(q\equiv1\pmod3\) and \(q^2-1\) when \(q\equiv2\pmod3\).

For the finite-field extension normalization
\[
E1(x,y)=\frac1q\sum_{t\in F} e(xt+yt^4),
\]
with counting measure on \(F^2\) and normalized counting measure on \(C_4\), orthogonality gives the exact constant-input fourth moment
\[
\|E1\|_4^4=\frac{E(C_4)}{q^2}.
\]
Thus the constant function exhibits an explicit arithmetic split in its \(L^4\) mass according to \(q\bmod3\).

## Assumptions and scope
The field is arbitrary finite of order \(q\), not necessarily prime. Characteristics \(2\) and \(3\) are excluded because the factorization and the parameter \(-6\) used below degenerate there. No assertion is made here that the constant function is a maximizer of the full \(L^2\)-to-\(L^4\) extension inequality for \(C_4\); the proved invariant is the exact additive energy and, equivalently, the exact fourth moment of the constant input.

## Proof
Fix the common first-coordinate sum
\[
s=a+b=c+d
\]
and put \(u=ab\), \(v=cd\). For any pair with sum \(s\),
\[
a^4+b^4=s^4-4us^2+2u^2.
\]
Hence equality of the quartic coordinates is equivalent to
\[
2(u-v)(u+v-2s^2)=0.
\]
Thus either \(u=v\), which gives the same unordered pair, or \(v=2s^2-u\).

For fixed \(s,u\), the number of ordered pairs \((a,b)\) with sum \(s\) and product \(u\) is
\[
N_s(u)=1+\chi(s^2-4u).
\]
Let \(T_s(u)=2s^2-u\). The energy contribution from a fixed \(s\) is therefore
\[
E_s=\sum_u N_s(u)^2+\sum_uN_s(u)N_s(T_s(u))-N_s(s^2)^2,
\]
where the last term removes the double count at the unique fixed point \(u=s^2\) of \(T_s\).

The first sum is independent of \(s\):
\[
\sum_uN_s(u)^2=2q-1,
\]
because \(u\mapsto s^2-4u\) is a bijection, \(\sum_x\chi(x)=0\), and \(\sum_x\chi(x)^2=q-1\).

When \(s=0\), one has \(T_0(u)=-u\), so
\[
\sum_uN_0(u)N_0(-u)=q+\chi(-1)(q-1),
\]
and \(N_0(0)=1\). Therefore
\[
E_0=3q-2+\chi(-1)(q-1).
\]

Now suppose \(s
e0\). Set \(x=s^2-4u\). The discriminant associated to \(T_s(u)\) is \(-6s^2-x\), so
\[
\sum_uN_s(u)N_s(T_s(u))
=q+\sum_x\chi(x)\chi(-6s^2-x).
\]
For every nonzero \(A\in F\), the quadratic Jacobi sum identity
\[
\sum_x\chi(x)\chi(A-x)=-\chi(-1)
\]
gives
\[
\sum_uN_s(u)N_s(T_s(u))=q-\chi(-1).
\]
At the fixed point \(u=s^2\),
\[
N_s(s^2)=1+\chi(-3).
\]
Consequently every nonzero \(s\) contributes
\[
E_s=3q-1-\chi(-1)-(1+\chi(-3))^2.
\]
Summing one zero-sum contribution and \(q-1\) identical nonzero-sum contributions cancels the \(\chi(-1)\) terms and yields
\[
E(C_4)=3q^2-q-1-(q-1)(1+\chi(-3))^2.
\]
Finally, in characteristic different from \(3\), the polynomial \(X^2+X+1\) has discriminant \(-3\). It splits over \(F\) exactly when \(F^\times\) contains an element of order \(3\), equivalently when \(q\equiv1\pmod3\). This gives the two stated cases.

For the extension identity, expanding \(\|E1\|_4^4\) and summing first over \((x,y)\in F^2\) leaves exactly the additive-collision constraints by character orthogonality, with overall factor \(q^-2\). Hence \(\|E1\|_4^4=E(C_4)/q^2\).

## Verification
The bundled `verify.py` performs exact finite-field collision counts for twenty-four prime fields through \(q=101\), and independently for the quadratic extension fields of orders \(25\), \(49\), and \(121\). It checks the closed formula, the \(q\bmod3\) reformulation, and the polynomial factorization used in the proof. Its successful replay prints `VERIFY_OK prime_fields=24 quadratic_extensions=3 max_prime=101`.

The computation is corroborative only. The proof above establishes the theorem for every finite field in the stated characteristics.

## Relationship to prior work
Mockenhaupt and Tao introduced the finite-field restriction framework, the normalization used here, and the even-exponent representation-count mechanism. Their principal polynomial-curve application is the full moment curve \((t,t^2,\ldots,t^d)\), where enough consecutive power sums determine the underlying multiset. The quartic graph \((t,t^4)\subset F^2\) deliberately omits the intermediate powers, leaving the secondary involution \(u\mapsto2s^2-u\) and the arithmetic \(q\bmod3\) split visible.

Biswas, Carneiro, Flock, Oliveira e Silva, Stovall, and Tautges determine sharp endpoint constants for the finite-field full moment curve in low dimensions and in a large-field regime. Their object remains \((t,t^2,\ldots,t^d)\), so their counting system and sharp maximizer theorem do not specialize to the two-coordinate quartic graph considered here. Biswas and Stovall study sharp restriction for monomial curves in the Euclidean affine-arclength setting, which is a different ambient problem and does not provide this finite-field additive-energy formula.

## Limitations
The result excludes characteristics \(2\) and \(3\). It computes the exact constant-input fourth moment but not the sharp \(L^2\)-to-\(L^4\) operator norm for the quartic graph. Literature searches did not locate the displayed exact energy formula, but obscure or unindexed finite-field additive-combinatorics calculations remain a residual originality risk.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1, 2002; Duke Math. J. 121 (2004), 35--74.
2. C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall, and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1, 2025.
3. C. Biswas and B. Stovall, *Sharp Fourier restriction to monomial curves*, arXiv:2302.05317v1, 2023.
