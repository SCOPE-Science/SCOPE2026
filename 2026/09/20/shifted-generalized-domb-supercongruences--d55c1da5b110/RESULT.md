# Sharp p-adic hierarchy for shifted generalized Domb sums

## Statement

For integers \(A\ge 0\), \(B,C\ge 1\), define for \(n\ge 1\)
\[
T_{A,B,C}(n)=
\sum_{k=0}^{n}
\binom{n+k-1}{k}^{A}
\binom{2k}{k}^{B}
\binom{2(n-k)}{n-k}^{C},
\]
and put \(T_{A,B,C}(0)=1\).

### Theorem

Let \(p\ge 5\) be prime and let \(m,r\ge 1\). Then
\[
T_{A,B,C}(mp^r)\equiv T_{A,B,C}(mp^{r-1})
\pmod{p^{e r}},
\qquad
e=\min(A+1,3).
\]

Thus the uniform exponent is \(r\) for \(A=0\), \(2r\) for \(A=1\), and
\(3r\) for every \(A\ge 2\).

In particular, for \(A\ge2\) this proves the generalized supercongruence
conjectured on OEIS A364111. The case \((A,B,C)=(2,1,1)\) is the sequence
A364111 itself:
\[
1,4,76,2560,106060,4864504,\ldots .
\]

The three exponents in the theorem are sharp as uniform statements over this
family already for \(p=5\) and \(r=1\):
\[
\begin{aligned}
\nu_5\!\left(T_{0,1,1}(5)-T_{0,1,1}(1)\right)&=1,\\
\nu_5\!\left(T_{1,2,1}(5)-T_{1,2,1}(1)\right)&=2,\\
\nu_5\!\left(T_{2,1,1}(5)-T_{2,1,1}(1)\right)&=3.
\end{aligned}
\]

## Proof

Write
\[
R_N(k)=\binom{N+k-1}{k},\qquad
C(k)=\binom{2k}{k},
\]
and
\[
F_N(k)=R_N(k)^A C(k)^B C(N-k)^C.
\]

It is enough first to treat \(N=mp^r\) with \(p\nmid m\).

### 1. Two valuation bounds

Let \(0<k<N\), put \(s=\nu_p(k)\), and write \(x_+=\max(x,0)\).

First,
\[
\nu_p R_N(k)\ge (r-s)_+.
\]
Indeed, when \(s\le r\),
\[
R_N(k)=\frac{N}{k}\binom{N+k-1}{k-1},
\]
and the second factor is an integer. When \(s>r\), the asserted lower
bound is just integrality.

Second,
\[
\nu_p C(k)+\nu_p C(N-k)\ge (r-s)_+.
\tag{1}
\]
Only \(s<r\) needs proof. Set
\[
x=\frac{k}{p^s},\qquad y=\frac{N-k}{p^s},\qquad d=r-s.
\]
Then \(p\nmid xy\) and \(x+y\equiv0\pmod{p^d}\). For every \(j\le d\),
the nonzero residues of \(x\) and \(y\) modulo \(p^j\) add to \(p^j\).
Since \(p^j\) is odd, exactly one of these two residues is greater than
\(p^j/2\).

Legendre's formula gives
\[
\nu_p C(z)
=
\sum_{j\ge1}
\left(
\left\lfloor\frac{2z}{p^j}\right\rfloor
-2\left\lfloor\frac{z}{p^j}\right\rfloor
\right),
\]
and the \(j\)-th summand is \(1\) exactly when the residue of \(z\)
modulo \(p^j\) is greater than \(p^j/2\). Hence, for each
\(j=1,\ldots,d\), the two central binomial coefficients in (1)
contribute at least one factor of \(p\) between them. This proves (1).

Because \(B,C\ge1\), the two bounds imply
\[
\nu_p F_N(k)\ge (A+1)(r-s)_+.
\tag{2}
\]

### 2. Scaling a \(p\)-divisible summand

We use Jacobsthal's binomial congruence in the form
\[
\frac{\binom{p^u a}{p^v b}}
     {\binom{p^{u-1}a}{p^{v-1}b}}
\equiv1\pmod{p^{u+v+\min(u,v)}}
\qquad (p\ge5,\ u,v\ge1),
\tag{3}
\]
as recalled, for example, in Lemma 2.1 of Osburn--Sahu--Straub.

Suppose \(p\mid k\), \(k>0\), and put
\[
s=\nu_p(k),\qquad q=\min(r,s).
\]
For the shifted factor,
\[
R_N(k)=\frac{N}{N+k}\binom{N+k}{N},
\]
and the rational prefactor is unchanged after simultaneously replacing
\((N,k)\) by \((N/p,k/p)\). Since \(p^q\mid N+k\) and \(p^r\mid N\),
(3) yields
\[
\frac{R_N(k)}{R_{N/p}(k/p)}
\equiv1\pmod{p^{r+2q}}
\equiv1\pmod{p^{3q}}.
\tag{4}
\]
Similarly,
\[
\frac{C(k)}{C(k/p)}\equiv1\pmod{p^{3q}},
\tag{5}
\]
and, if \(N-k>0\),
\[
\frac{C(N-k)}{C((N-k)/p)}
\equiv1\pmod{p^{3q}}.
\tag{6}
\]
When \(k=N\), the last ratio is exactly \(1\). Raising (4)--(6) to
fixed nonnegative powers and multiplying gives a \(p\)-adic unit
\(\lambda\) such that
\[
F_N(k)=\lambda F_{N/p}(k/p),
\qquad
\lambda\equiv1\pmod{p^{3q}}.
\tag{7}
\]

If \(1\le s<r\), applying (2) at the lower level
\((N/p,k/p)\) gives
\[
\nu_p F_{N/p}(k/p)\ge (A+1)(r-s).
\]
Let \(e=\min(A+1,3)\). From (7),
\[
\begin{aligned}
\nu_p\!\left(F_N(k)-F_{N/p}(k/p)\right)
&\ge e(r-s)+3s\\
&=er+(3-e)s\\
&\ge er.
\end{aligned}
\tag{8}
\]
If \(s\ge r\), then \(q=r\), so (7) itself gives (8) because
\(3r\ge er\).

The endpoint \(k=0\) is even simpler:
\[
F_N(0)=C(N)^C,
\]
and (3) gives
\[
F_N(0)\equiv F_{N/p}(0)\pmod{p^{3r}},
\]
which is stronger than required.

### 3. Comparing the sums

If \(p\nmid k\), then \(s=0\), and (2) gives
\[
\nu_p F_N(k)\ge (A+1)r\ge er.
\]
Therefore all terms with \(p\nmid k\) vanish modulo \(p^{er}\).

For terms with \(p\mid k\), equation (8), including the endpoints, gives
\[
F_N(k)\equiv F_{N/p}(k/p)\pmod{p^{er}}.
\]
Reindexing \(k=pj\) now yields
\[
T_{A,B,C}(N)
\equiv
\sum_{j=0}^{N/p}F_{N/p}(j)
=
T_{A,B,C}(N/p)
\pmod{p^{er}}.
\]

Finally, if \(p\mid m\), write \(m=p^t m_0\) with \(p\nmid m_0\).
Applying the already proved case to exponent \(r+t\) gives the stronger
congruence modulo \(p^{e(r+t)}\), and hence the claimed modulus
\(p^{er}\).

This proves the theorem.

## Sharpness examples

The exact differences at \(p=5\), \(m=r=1\) are
\[
\begin{aligned}
T_{0,1,1}(5)-T_{0,1,1}(1)&=1020,\\
T_{1,2,1}(5)-T_{1,2,1}(1)&=8\,783\,950,\\
T_{2,1,1}(5)-T_{2,1,1}(1)&=4\,864\,500.
\end{aligned}
\]
Their \(5\)-adic valuations are respectively \(1,2,3\).

## Context and originality

Osburn and Sahu proved the cubic two-term supercongruence for generalized
Domb sums
\[
\sum_k
\binom{n}{k}^{A}
\binom{2k}{k}^{B}
\binom{2(n-k)}{n-k}^{C}
\]
when \(A\ge2\). Later work of Osburn, Sahu and Straub developed
Jacobsthal-based termwise scaling for several related Apéry-like and
central-binomial families.

OEIS A364111 replaces \(\binom{n}{k}^{A}\) by
\(\binom{n+k-1}{k}^{A}\) and explicitly states the cubic congruence for
all \(A\ge2\), \(B,C>0\) as a conjecture. The A364111 page was last
modified on 5 September 2026 and still labels both the specific
\((2,1,1)\) case and this full generalization as conjectural.

Searches for A364111, the exact shifted-binomial summand, negative-upper-
index formulations, shifted/generalized Domb terminology, and stronger
covering theorems did not locate a prior proof of this family. The
argument above is not a formal consequence of the generalized Domb
theorem: its extra ingredient is the complementary carry bound (1),
which supplies the missing valuation from the two central binomial
factors.

To the best of our knowledge, the theorem therefore resolves the
generalized A364111 conjecture and additionally gives the sharp uniform
\(p^r,p^{2r},p^{3r}\) hierarchy for \(A=0,1,\ge2\).

## Verification

`artifacts/verify.py` uses exact Python integers only. It checks the
published A364111 prefix, 96 instances of the theorem for
\(p\in\{5,7\}\), \(m\in\{1,2\}\), \(r\in\{1,2\}\),
\(A\in\{0,1,2,3\}\), and three choices of \((B,C)\), and verifies the
three sharpness valuations above. The deterministic output is stored in
`artifacts/verification.txt`.

These computations are corroborative; the proof is the argument above.

## Limitations

- The theorem is stated only for primes \(p\ge5\). Small primes can have
  weaker Jacobsthal moduli and are not covered here.
- The assumption \(B,C\ge1\) is essential to this proof because the
  complementary carry bound uses both central-binomial factors.
- For the special \(A=1,B=C=1\) sequence OEIS A362676, numerical evidence
  and OEIS conjecture a stronger cubic modulus \(p^{3r}\). The present
  theorem proves only the uniform quadratic modulus \(p^{2r}\) in the
  \(A=1\) layer and does not settle that stronger special case.
- Coster's 1988 thesis *Supercongruences*, a foundational source for this
  method family, was not inspected in full. Related accessible sources
  and later papers were inspected, but the thesis leaves a residual
  priority risk.
- No independent audit or formal proof-assistant verification is asserted.

## References

1. OEIS A364111, https://oeis.org/A364111
2. Robert Osburn and Brundaban Sahu, *A supercongruence for generalized
   Domb numbers*, arXiv:1201.6195, https://arxiv.org/abs/1201.6195
3. Robert Osburn, Brundaban Sahu and Armin Straub, *Supercongruences for
   sporadic sequences*, arXiv:1312.2195,
   https://arxiv.org/abs/1312.2195
4. OEIS A362676, https://oeis.org/A362676
5. Matthijs Coster, *Supercongruences*, Ph.D. thesis, University of
   Leiden, 1988; bibliographic/full-text link indexed at
   https://core.ac.uk/download/pdf/301642554.pdf
