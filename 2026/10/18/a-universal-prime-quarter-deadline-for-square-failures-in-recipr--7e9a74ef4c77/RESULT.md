# A universal prime-quarter deadline for square failures in reciprocal-sum sequences

## Finding

Let \(h\ge1\) and \(x_0\ge1\) be integers. Define positive rational numbers by
\[
 x_{n+1}=\frac{h^2}{x_0+x_1+\cdots+x_n}\qquad(n\ge0),
\]
and write each \(x_n=a_n/b_n\) in lowest positive terms. For \(n\ge2\), put
\[
 Q_n=\frac{2}{h}a_n+b_n.
\]
Define the explicit integer
\[
 B(h)=\max\left(\{1\}\cup\bigl(\{2\}\text{ if }2\mid h\bigr)
 \cup\left\{\frac{p+7}{4}:\ p\mid h,\ p\equiv1\pmod4\right\}\right).
\]
An empty conditional set contributes no entries to the maximum. Then **for every** positive starting integer \(x_0\), **every** term \(Q_n\) with \(n>B(h)\) is the square of an integer. No restriction is imposed on prime exponents in \(h\).

Equality in the stated bound occurs at the smallest relevant odd prime: with \(h=x_0=5\) the term \(Q_3=9/5\) is not an integer square, and \(B(5)=3\). The theorem gives a uniform cutoff across all starting values, not merely a finite number of exceptional indices along each individual trajectory.

## Assumptions and scope

All powers, gcds, and reductions take place in ordinary positive integers. A *perfect square* means the square of a nonnegative integer, not merely the square of a rational number. For \(h=1\) and for \(h\) supported entirely on primes \(3\pmod4\), the maximum above equals \(1\), so every \(Q_n\), \(n\ge2\), is a perfect square. The cutoff is asserted to work for all \(h\) and all initial values; it is **not** asserted to be the optimal cutoff for each separate \(h\).

## Proof

**1. Reduction to first zero-hitting times.** Set \(S_n=x_0+\cdots+x_n\), \(t_n=S_n/h=u_n/v_n\) in lowest positive terms, and initially
\[
 g=\gcd(x_0,h),\qquad u_0=x_0/g,\quad v_0=h/g.
\]
From \(S_{n+1}=S_n+h^2/S_n\) one obtains
\[
 u_{n+1}=u_n^2+v_n^2,\qquad v_{n+1}=u_nv_n.
\]
These are still coprime: if \(\gcd(u,v)=1\), neither a prime of \(u\) nor a prime of \(v\) divides \(u^2+v^2\). Put \(d_n=\gcd(h,u_n)\). Direct reduction of \(x_{n+1}=hv_n/u_n\) gives
\[
 a_{n+1}=hv_n/d_n,\quad b_{n+1}=u_n/d_n,\quad
 Q_{n+1}=\frac{(u_{n-1}+v_{n-1})^2}{d_n}\qquad(n\ge1).
\]
We verify that \(Q_{n+1}\) is an integer square **exactly when** \(d_n=1\). Sufficiency is immediate. If an odd prime \(p\mid d_n\), then \(p\mid u_{n-1}^2+v_{n-1}^2\) and the preceding pair is coprime. Thus \(p\nmid u_{n-1}+v_{n-1}\): otherwise \(p\mid2v_{n-1}^2\), a contradiction. Consequently \(Q_{n+1}\) is not even an integer. If \(2\mid d_n\), the preceding coordinates are both odd, so \(u_n\equiv2\pmod8\), whence \(v_2(d_n)=1\). The \(2\)-adic valuation of \(Q_{n+1}\) is odd; it is not a square. Thus all nonsquare indices correspond exactly to primes dividing \(u_n\), with \(n\ge1\).

**2. Exceptional primes.** If \(p\equiv3\pmod4\), a congruence \(u_n=u_{n-1}^2+v_{n-1}^2\equiv0\pmod p\) contradicts coprimality, so such primes never spoil a term. For \(p=2\), if \(2\mid u_n\) with \(n\ge1\), the previous pair must be odd-odd; the next pair is even-odd and all later pairs odd-even. Thus \(n=1\) and only \(Q_2\) can fail because of \(2\).

For an odd prime \(p\equiv1\pmod4\), if \(p\mid u_0\) or \(p\mid v_0\), the recurrence shows \(p\nmid u_n\) for all \(n\ge1\). Otherwise \(u_0/v_0\) is a nonzero element of \(\mathbb F_p\), and until the first occurrence \(p\mid u_n\) the ratios obey the finite-field map
\[
 T_p(z)=z+z^{-1}\quad(z\in\mathbb F_p^*).
\]
The first \(n\ge1\) with \(p\mid u_n\) is precisely the first time \(T_p^n(u_0/v_0)=0\). After such a hit, the denominator coordinate is \(0\pmod p\) forever, so there is no later hit.

**3. A fourfold-orbit depth bound.** Suppose a nonzero \(z\in\mathbb F_p\) first reaches \(0\) after \(k\ge1\) iterations of \(T_p\). For \(1\le j\le k\), let \(D_j\) be the set of starting nonzero field elements whose first hitting time is \(j\). Each \(D_j\) is nonempty, and the sets are disjoint. The identities
\[
 T_p(-z)=-T_p(z),\qquad T_p(z^{-1})=T_p(z)
\]
show that \(D_j\) is stable under both \(z\mapsto-z\) and \(z\mapsto z^{-1}\). Their joint orbits have four elements, except for \(z^2=1\) or \(z^2=-1\), where there are two. The elements satisfying \(z^2=-1\) hit \(0\) after exactly one step; the elements satisfying \(z^2=1\) (namely \(\pm1\)) can belong to at most one level. Therefore among the \(k\) nonempty levels, at least \(k-2\) each contribute at least four field elements, and the other two contribute at least two each. This gives
\[
 p-1\ \ge\ \sum_{j=1}^k|D_j|\ \ge\ 4k-4,
 \qquad k\le\frac{p+3}{4}.
\]
The same inequality remains true when \(k=1\), since then \(|D_1|=2\) and the lower bound is vacuous. Thus a prime \(p\equiv1\pmod4\) can spoil only a term \(Q_{k+1}\) with
\[
 k+1\le\frac{p+7}{4}.
\]
Combining all prime divisors of \(h\) proves the asserted uniform bound \(B(h)\).

**4. Sharpness.** When \(h=x_0=5\), direct recurrence yields \(x_1=5\), \(x_2=5/2\), \(x_3=2\), so \(Q_3=(2/5)\cdot2+1=9/5\). Here the finite-field orbit \(1\mapsto2\mapsto0\) modulo \(5\) attains hitting depth \(2=(5+3)/4\), and \(B(5)=3\).

## Verification

The accompanying standalone script `verify_boundary.py` uses exact integer arithmetic. It enumerates \(135621\) nonzero starting states over all relevant prime fields through \(2000\), confirms the fourfold-orbit bound at every zero-hitting state, and checks the prime-\(5\) and prime-\(13\) hitting-level counts. Separately, it compares direct rational recurrences with independently computed modular predictions for \(4240\) positive starting values across \(1\le h\le40\), including all nonsquare indices and the predicted cutoff. The script confirms \(Q_3=9/5\) indirectly by an exact nonsquare test at \(h=x_0=5\). These are finite checks only; the proof above establishes the infinite claim.

To reproduce from this directory, run `python3 verify_boundary.py` using the Python standard library.

## Relationship to prior work

Matijasevick, Rodríguez, and Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields* (arXiv:2610.00765v1, first publicly submitted 2026-09-30) derive the reduced recurrence, establish the prime-wise square obstruction, and prove that each prime dividing \(h\) spoils at most one term. The present theorem instead supplies an explicit **starting-value-independent index deadline** with a prime-quarter coefficient and an attained example. An earlier exact starting-value law describes exception positions by finite-field first-hit data; that description alone does not supply the universal quantitative bound on first-hit depth proved here.

The finite-field map \(z\mapsto z+z^{-1}\), its functional graphs, and the associated polynomial transforms were studied in *On the iterations of certain maps over finite fields of odd characteristic*, *Journal of Number Theory* **142** (2014), 274–297, DOI:10.1016/j.jnt.2014.02.024. The fourfold sign-and-inversion orbit-count argument is applied here to a uniform arithmetic deadline. Prior analyses of specialized finite-field functional graphs are not represented as a general classification of all prime fields.

## Limitations

The displayed deadline need not be optimal for a fixed \(h\) or prime \(p\); equality is exhibited at \(p=5\), but no asymptotic sharpness of the coefficient \(1/4\) is asserted. The theorem concerns the square case \(k=h^2\) and says nothing about all-square properties for nonsquare \(k\), nor about density of starting values, which is a separate subject. The relevant 2014 functional-graph article and later portions of the 2026 preprint were not fully accessible during this comparison; implicit or earlier equivalent bounds remain a literature-overlap risk.

## References

1. M. Matijasevick, S. Rodríguez, and G. Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1 (2026-09-30), https://arxiv.org/abs/2610.00765.
2. *On the iterations of certain maps over finite fields of odd characteristic*, *Journal of Number Theory* **142** (2014), 274–297, DOI:10.1016/j.jnt.2014.02.024.
