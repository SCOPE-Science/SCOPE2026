# Square-zero elements of prime dihedral quandle algebras: a Frobenius-cycle census

## Finding

For an odd prime \(p\) and a prime power \(q\) with \(p\nmid q\), let \(A_{p,q}=\mathbb F_q[R_p]\) be the nonassociative dihedral quandle algebra, defined on its basis \(e_i\), \(i\in\mathbb Z/p\mathbb Z\), by \(e_i e_j=e_{2j-i}\). The exact number of elements whose (unambiguously defined) square vanishes is determined by elementary multiplicative orders modulo \(p\).

Set \(d=\operatorname{ord}_p(q)\), \(H=\langle q\bmod p\rangle\le(\mathbb Z/p\mathbb Z)^\times\), and let \(\ell\) be the order of the coset \(-2H\) in the cyclic quotient \((\mathbb Z/p\mathbb Z)^\times/H\). Put \(r=(p-1)/(d\ell)\) and \(w=q^d-1\). For each positive integer \(\ell\) define
\[
P_\ell(w)=\sum_{j=0}^{\lfloor\ell/2\rfloor}\frac{\ell}{\ell-j}\binom{\ell-j}{j}w^j.
\]
The fractions in this display are nonnegative integers; in particular \(P_1(w)=1\) and \(P_2(w)=1+2w\). The complete square-zero census is
\[
\boxed{\#\{u\in A_{p,q}:u^2=0\}=P_\ell(q^d-1)^r.}
\]
There is a nonzero square-zero element **if and only if** \(-2\notin H\). In particular, over \(\mathbb F_2\), writing \(d=\operatorname{ord}_p(2)\), the number equals \(1\) if \(d\) is even and equals \((2^{d+1}-1)^{(p-1)/(2d)}\) if \(d\) is odd.

The count is of **elements**, not isomorphism classes, and counts zero. No claim is made about nilpotency under alternative parenthesizations of products of three or more elements.

## Assumptions and scope

The prime \(p\) is odd and \(q\) is a prime power coprime to \(p\). The algebra is precisely the \(p\)-dimensional, possibly nonassociative, \(\mathbb F_q\)-algebra with the stated multiplication table. For \(u=\sum_{i\bmod p}a_i e_i\), the expression \(u^2\) means the single bilinear product \(u\cdot u\). The standard Fourier-transform normalization below is unscaled in the forward direction and has scalar \(p^{-1}\) in its inverse; this inverse exists because \(p\nmid q\).

The group \(H\) has exactly \(d\) elements, and \(\ell\) divides \((p-1)/d\), making \(r\) a positive integer. The formula includes characteristic two, where the square map need not behave as it does in associative algebras.

## Proof

**1. Fourier product.** Let \(K=\mathbb F_{q^d}\). Since \(p\mid(q^d-1)\), this field contains a primitive \(p\)-th root of unity \(\zeta\). For \(u=\sum_i a_i e_i\), define its unscaled Fourier coordinates \(X_t=\sum_i a_i\zeta^{ti}\) for \(t\in\mathbb Z/p\mathbb Z\). The Fourier transform is bijective \(K^p\to K^p\), with inverse \(a_i=p^{-1}\sum_t X_t\zeta^{-ti}\).

If \(u^2=\sum_k b_k e_k\), then for each \(t\)
\[
\sum_k b_k\zeta^{tk}
=\sum_{i,j}a_i a_j\zeta^{t(2j-i)}
=\left(\sum_i a_i\zeta^{-ti}\right)
 \left(\sum_j a_j\zeta^{2tj}\right)
=X_{-t}X_{2t}.
\]
Thus \(u^2=0\) holds exactly when \(X_sX_{-2s}=0\) for **every** \(s\bmod p\). The equation with \(s=0\) is \(X_0^2=0\), hence \(X_0=0\).

**2. Frobenius descent.** The Fourier coordinates correspond to \(a_i\in\mathbb F_q\) exactly when \(X_{qt}=X_t^q\) for all \(t\). Necessity follows by raising \(X_t\) to its \(q\)-th power. For sufficiency, substitute the relation into the inverse transform: \(a_i^q=p^{-1}\sum_t X_t^q\zeta^{-qti}=p^{-1}\sum_t X_{qt}\zeta^{-qti}=a_i\), where \(p^{-1}\) lies in the prime field. Therefore each \(a_i\) is fixed by Frobenius.

Every nonzero index lies in a \(q\)-cyclotomic orbit of size \(d\); the \((p-1)/d\) orbits are indexed by cosets of \(H\) in \((\mathbb Z/p\mathbb Z)^\times\). On any such orbit its Fourier coordinates are determined by a single freely chosen value of \(K\). Precisely \(w=q^d-1\) choices make the entire orbit nonzero; one choice makes it identically zero.

**3. Support compatibility and cycles.** The condition \(X_sX_{-2s}=0\) is unchanged along a Frobenius orbit because both factors are raised to the same \(q\)-power on replacing \(s\) by \(qs\). On the quotient of indices by \(H\), it therefore forbids a nonzero choice at a coset and a nonzero choice at its image under multiplication by \(-2\). The map is translation by the class \(-2H\) in a cyclic group. It decomposes into exactly \(r=(p-1)/(d\ell)\) disjoint directed cycles of length \(\ell\).

An allowable support is thus an independent set of the undirected cycle associated with each orbit; when \(\ell=1\) the loop forces the sole orbit to vanish, and when \(\ell=2\) the two vertices cannot both be occupied. Every occupied vertex carries \(w\) choices and every unoccupied one carries one choice. Choosing exactly \(j\) nonadjacent vertices on a cycle of length \(\ell\) gives \(\ell/(\ell-j)\binom{\ell-j}{j}\) possibilities (also valid with the preceding length-one/two interpretations). Multiplying weights and then multiplying over the \(r\) independent cycles proves the boxed formula. There are no unstated compatibility conditions because distinct Frobenius orbits have independent Fourier values.

**4. Existence criterion and binary specialization.** Since \(w\ge1\), a nonempty allowable support exists if and only if \(\ell>1\); this is exactly \(-2H\ne H\). For \(q=2\) the element \(-2H\) equals \(-H\). If \(d\) is even, the unique order-two element \(-1\) of the cyclic group \(\mathbb F_p^\times\) lies in \(H\), so \(\ell=1\). If \(d\) is odd, \(-1\notin H\), so \(\ell=2\), \(P_2(w)=1+2w=2^{d+1}-1\), and \(r=(p-1)/(2d)\). This proves the stated binary formula.

## Verification

The supplied standalone `check_square_zero.py` independently builds finite fields by polynomial-coordinate arithmetic, directly multiplies each coefficient vector in the quandle basis, and counts the solutions of \(u^2=0\). It separately calculates the proposed count from modular orders and the cycle polynomial; agreement is not forced by use of the Fourier transform in the checker.

Exhaustive configurations are \((p,q)=(3,2),(3,4),(3,5),(5,2),(5,3),(5,4),(5,7),(5,8),(5,11),(7,2),(7,3),(7,4),(11,2),(13,2)\). The matching counts in that order are \(1,1,1,1,1,31,1,1,241,15,1,127,1,1\). The checker reports `ALL_DIHEDRAL_SQUARE_ZERO_TESTS_PASSED 14`. All computations are finite tests; the preceding proof, not extrapolation from these checks, establishes the general formula.

## Relationship to prior work

Bardakov–Passi–Singh, *Zero-divisors and idempotents in quandle rings*, established the motivating quandle-ring questions, including zero divisors and small idempotent classifications. Their general square-zero example uses a nontrivial trivial subquandle; it does not give the exact prime-dihedral finite-field census here.

Elhamdadi–Ta–Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, Theorem 3.2, proves a general Fourier product identity over complex Alexander quandle algebras. The Fourier factorization in step 1 is an elementary finite-field instance of that known structural principle and is **not claimed as a new identity**. Their stated results concern complex/integral idempotents; the present statement counts every absolute square-zero element over each finite field by Frobenius descent and a weighted cycle polynomial.

Zhang, *Group-ring methods for Alexander quandle rings*, develops related coefficient-ring and Fourier structural methods, with results on augmentation ideals and integral idempotents, not this numeric square-zero distribution. Churchill and collaborators investigate nilpotence in certain other quandle rings and core-quandle idempotents. A separate finite-field census of **idempotents** in dihedral quandle algebras is logically different: the equation \(u^2=u\) imposes nonzero values on the Fourier support, whereas \(u^2=0\) imposes a support-exclusion condition. That idempotent count does not imply the square-zero multiplicities here merely by replacing a parameter.

## Limitations

The theorem excludes fields whose characteristic equals \(p\), when the Fourier transform over the \(p\)-th roots is not invertible. It treats odd **prime** dihedral-quandle order, not arbitrary composite order, and distinguishes square-zero from general nonassociative nilpotency conventions. No statement about uniqueness in all prior literature or independent validation is made. The precise originality risk is that a published or unpublished Fourier-support formulation may make the cyclic independent-set count an unstated corollary; examined sources contain its building blocks but not an equivalent explicit finite-field arithmetic census.

## References

1. V. G. Bardakov, I. B. S. Passi and M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843, first public version 2020-01-19. Primary MSC 17D99. https://arxiv.org/abs/2001.06843
2. M. Elhamdadi, L. Ta and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (2026-09-03), especially Theorem 3.2 and Section 3.2. https://arxiv.org/html/2609.03799v1
3. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (2026-10-06). https://arxiv.org/abs/2610.08204
4. *A Further Study of Quandles and Quandle Rings*, arXiv:2608.09149v1 (2026-08-10). https://arxiv.org/html/2608.09149v1
