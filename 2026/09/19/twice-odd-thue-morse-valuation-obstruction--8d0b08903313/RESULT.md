# Explicit 2-adic obstructions for all twice-odd powers of the Thue–Morse series

## Result

Let
\[
T(x)=\prod_{j\ge 0}(1-x^{2^j}),\qquad
T(x)^m=\sum_{n\ge0}t_m(n)x^n.
\]

The following boundary congruence holds.

**Theorem.** Let \(A\ge2\), let \(v\) be a positive odd integer, and put
\[
N=2^A,\qquad m=2+Nv,\qquad n=N-1.
\]
Then
\[
\boxed{\;
t_m(N-1)\equiv N(v-1)\pmod{4N}.
\;}
\]
At the same index,
\[
\boxed{\;
\nu_2\binom{n+m-1}{m-1}=A+\nu_2(v+1).
\;}
\]
Consequently the two valuations are always different:
\[
\nu_2(t_m(N-1))\ne
\nu_2\binom{n+m-1}{m-1}.
\]
More explicitly,
\[
v\equiv1\pmod4
\Longrightarrow
\nu_2(t_m(N-1))\ge A+2,\quad
\nu_2\binom{n+m-1}{m-1}=A+1,
\]
whereas
\[
v\equiv3\pmod4
\Longrightarrow
\nu_2(t_m(N-1))=A+1,\quad
\nu_2\binom{n+m-1}{m-1}\ge A+2.
\]

This gives a complete proof of the \(r=1\) slice of Shen's Conjecture 6.2. Indeed, write an even exponent as
\[
m=2u,\qquad u\ \text{odd}.
\]
If \(u=1\), the exact binomial valuation for every \(n\) is the known \(m=2\) case. If \(u>1\), write
\[
a=\nu_2(u-1),\qquad
v=\frac{u-1}{2^a},\qquad
N=2^{a+1}.
\]
Then \(v\) is odd, \(m=2+Nv\), and the theorem supplies the explicit violating index
\[
\boxed{\;n=2^{\nu_2(u-1)+1}-1.\;}
\]
Thus, among exponents with \(\nu_2(m)=1\), the identity
\[
\nu_2(t_m(n))=\nu_2\binom{n+m-1}{m-1}
\quad\text{for every }n\ge0
\]
holds if and only if \(m=2\), exactly as Conjecture 6.2 predicts.

For example,
\[
t_{10}(7)=-1600,\qquad \nu_2(t_{10}(7))=6,
\]
while
\[
\binom{16}{9}=11440,\qquad \nu_2\binom{16}{9}=4.
\]

## Context

Shen [1] studies the coefficients \(t_m(n)\) and proves the exact binomial valuation for \(m=2^r\) and for \(m=3\cdot2^r\) with \(r\ge2\), together with a corrected formula for \(m=6\). Conjecture 6.2 of [1] proposes that for
\[
m=2^r u,\qquad u\text{ odd},
\]
the exact binomial valuation holds at every index if and only if
\[
r\ge 1+\ell\!\left(\frac{u-1}{2}\right),
\]
where \(\ell\) is the longest run of consecutive \(1\)'s in the binary expansion. When \(r=1\), this condition is equivalent to \(u=1\). The theorem above proves precisely this full \(r=1\) layer and gives a closed-form obstruction index for every excluded odd \(u>1\).

The proof uses the known \(m=2^A\) valuation theorem, the functional equation
\[
T(x)=(1-x)T(x^2),
\]
and elementary \(2\)-adic binomial arithmetic.

## Proof

We use two facts from the \(m=2\) case. The functional equation gives
\[
t_2(2h)=t_2(h)+t_2(h-1),\qquad
t_2(2h+1)=-2t_2(h),
\]
and the known exact valuation is
\[
\nu_2(t_2(j))=\nu_2(j+1).
\]
A small refinement will also be needed:
\[
\boxed{\;t_2(2h)\equiv(-1)^h\pmod4.\;}
\tag{1}
\]
This follows by induction from the two recurrences. In the even and odd induction steps, the term \(t_2(a-1)\) or \(t_2(a)\) is odd exactly when the corresponding integer \(a\) has the required parity, by the displayed valuation formula.

### 1. A dyadic coefficient lemma

Put
\[
R(x)=T(x)^{Nv}=\sum_{i\ge0}r_i x^i.
\]
For every \(1\le i<N\),
\[
\boxed{\;\nu_2(r_i)=A-\nu_2(i).\;}
\tag{2}
\]

To see this, write
\[
T(x)^N=1+C(x).
\]
The known power-of-two theorem gives, for \(1\le i<N\),
\[
\nu_2([x^i]C)=A-\nu_2(i).
\]
Since \(v\) is odd,
\[
R=(1+C)^v.
\]
The linear term \(vC\) therefore has exactly the valuation in (2). Every contribution from \(C^s\), \(s\ge2\), has at least one additional factor of \(2\). Indeed, if positive integers \(i_1,\dots,i_s\) sum to \(i<N\), then
\[
\sum_{h=1}^s\bigl(A-\nu_2(i_h)\bigr)
\ge A-\nu_2(i)+s-1.
\tag{3}
\]
For two summands this follows immediately by comparing their \(2\)-adic orders; iteration gives the general case. Hence the higher powers of \(C\) cannot cancel the linear term modulo the next power of \(2\), proving (2).

### 2. Comparing \(t_m\) with \(t_2\) below \(N/2\)

Since \(m=2+Nv\),
\[
T(x)^m=T(x)^2R(x).
\]
Define
\[
\delta_k=t_m(k)-t_2(k).
\]
For \(0\le k<N/2-1\), let
\[
s=\nu_2(k+1).
\]
Then
\[
\boxed{\;2^{s+2}\mid\delta_k.\;}
\tag{4}
\]

Indeed,
\[
\delta_k=\sum_{i=1}^k r_i\,t_2(k-i).
\]
For a summand put
\[
a=\nu_2(i),\qquad b=\nu_2(k+1-i).
\]
By (2) and the exact \(m=2\) valuation, its order is
\[
A-a+b.
\]
Because \(k+1<2^{A-1}\), one has \(s\le A-2\). If \(a<s\), then \(b=a\); if \(a>s\), then \(b=s\); and if \(a=s\), then \(b\ge s\). In all three cases
\[
A-a+b\ge s+2,
\]
which proves (4).

At the endpoint
\[
q=\frac N2-1
\]
the same convolution has a sharp parity statement:
\[
\boxed{\;\delta_q\equiv N\pmod{2N}.\;}
\tag{5}
\]
For every \(1\le i\le q\),
\[
\nu_2\!\left(\frac N2-i\right)=\nu_2(i),
\]
so each summand \(r_i t_2(q-i)\) has valuation exactly \(A\). There are
\[
q=\frac N2-1
\]
such summands, an odd number because \(A\ge2\). After division by \(N\), each is odd, hence their sum is odd. This is (5).

### 3. Reduction of the boundary coefficient

The odd-index recurrence from \(T(x)^m=(1-x)^mT(x^2)^m\) is
\[
t_m(2q+1)
=
-\sum_{j=0}^{q}
\binom{m}{2j+1}t_m(q-j).
\tag{6}
\]
For \(j\ge1\),
\[
\boxed{\;
\nu_2\binom{m}{2j+1}=A-\nu_2(j).
\;}
\tag{7}
\]
Indeed,
\[
\nu_2\binom{m}{2j+1}
=
1+\nu_2\binom{1+Nv}{2j},
\]
and the last binomial coefficient has the same valuation as
\(\binom{Nv}{2j}\), namely
\[
A-\nu_2(2j)=A-1-\nu_2(j).
\]

Now put
\[
G=[x^{N-1}](1-x)^mT(x^2)^2.
\]
Replacing \(t_m(q-j)\) by \(t_2(q-j)\) in (6) gives exactly \(G\). Since
\[
\nu_2\!\left(\frac N2-j\right)=\nu_2(j)
\qquad(1\le j<N/2),
\]
(4) and (7) show that every \(j\ge1\) replacement error is divisible by \(4N\). The \(j=0\) term is controlled by (5). Because \(m=2+Nv\) and \(N\ge4\),
\[
-m\delta_q\equiv2N\pmod{4N}.
\]
Therefore
\[
\boxed{\;t_m(N-1)\equiv G+2N\pmod{4N}.\;}
\tag{8}
\]

Using \(T(x)=(1-x)T(x^2)\),
\[
G=[x^{N-1}](1-x)^{Nv}T(x)^2,
\]
hence
\[
G=
\sum_{k=0}^{N-1}
(-1)^k\binom{Nv}{k}t_2(N-1-k).
\tag{9}
\]

### 4. Pairing the terms in \(G\)

For \(1\le k<N\), write
\[
k=2^s q,\qquad q\ \text{odd}.
\]
Then
\[
\nu_2\binom{Nv}{k}=A-s.
\]
More precisely, modulo \(4\),
\[
\frac{\binom{Nv}{k}}{2^{A-s}}
\equiv
(-1)^{k-1}v q^{-1}\varepsilon_k
\pmod4,
\tag{10}
\]
where inverses are taken modulo \(4\), and
\[
\varepsilon_k=
\begin{cases}
1,&k\le N/2,\\
-1,&k>N/2.
\end{cases}
\]
To prove (10), use
\[
\binom{Nv}{k}
=
\frac{Nv}{k}(-1)^{k-1}
\prod_{j=1}^{k-1}\left(1-\frac{Nv}{j}\right).
\]
All factors in the product are \(1\bmod4\), except that when \(k>N/2\) the unique term \(j=N/2\) contributes
\[
1-2v\equiv-1\pmod4.
\]

Also, with
\[
q'=2^{A-s}-q,
\]
the \(m=2\) recurrence gives
\[
\frac{t_2(N-1-k)}{2^s}
=
(-1)^s t_2(q'-1).
\tag{11}
\]
The normalized \(k\)-th term of (9) is therefore odd.

Pair the terms indexed by \(k\) and \(N-k\) for \(k<N/2\). They have the same \(s\), while their odd parts \(q,q'\) satisfy
\[
q+q'=2^{A-s},\qquad A-s\ge2.
\]
Thus
\[
q'\equiv-q\pmod4.
\]
Moreover, by (1),
\[
t_2(q-1)\equiv(-1)^{(q-1)/2}\pmod4,
\]
and
\[
t_2(q'-1)\equiv-\,t_2(q-1)\pmod4,
\]
because \((q-1)/2\) and \((q'-1)/2\) have opposite parity. Substituting (10) and (11), each pair contributes \(0\bmod4\) after division by \(N\).

Only \(k=0\) and \(k=N/2\) remain. The first contributes
\[
\frac{t_2(N-1)}N=(-1)^A,
\]
while the middle term contributes
\[
v(-1)^A.
\]
Hence
\[
\frac GN\equiv(-1)^A(1+v)\equiv1+v\pmod4,
\tag{12}
\]
because \(1+v\) is even. Combining (8) and (12),
\[
\frac{t_m(N-1)}N
\equiv v+3
\equiv v-1
\pmod4,
\]
which proves the main congruence.

### 5. The binomial comparator

At \(n=N-1\),
\[
\binom{n+m-1}{m-1}
=
\binom{N(v+1)}{N-1}.
\]
Using the binary digit-sum formula for \(\nu_2\binom ab\),
\[
\begin{aligned}
\nu_2\binom{N(v+1)}{N-1}
&=s_2(N-1)+s_2(Nv+1)-s_2(N(v+1))\\
&=A+1+s_2(v)-s_2(v+1)\\
&=A+\nu_2(v+1),
\end{aligned}
\]
since \(v\) is odd. The two residue classes of \(v\bmod4\) now give the opposite valuation inequalities stated in the theorem, so equality is impossible.

This completes the proof.

## Verification

A standalone exact-integer script in `artifacts/verify.py` independently evaluates coefficients from
\[
T(x)^m=(1-x)^mT(x^2)^m
\]
and checks the congruence, the binomial valuation formula, and the resulting mismatch. The supplied verification checks 112 \((A,v)\) pairs with
\[
2\le A\le8,\qquad 1\le v\le31,\quad v\ \text{odd},
\]
and all 127 odd integers \(3\le u\le255\). All checks passed. The computation is auxiliary; the theorem is proved above.

## Originality and scope

To the best of our knowledge, this explicit boundary congruence and the resulting complete \(r=1\) case of Conjecture 6.2 are not in the prior literature.

Shen [1] states Conjecture 6.2 as open after proving the power-of-two family, the family \(3\cdot2^r\) for \(r\ge2\), and the exceptional formula for \(m=6\). The case \(m=6\) is the first member \(u=3\) of the obstruction proved here, but [1] does not extend that obstruction to arbitrary odd \(u>1\). The earlier paper of Gawron--Miska--Ulas [2] proves the exact valuation for power-of-two exponents and studies several other arithmetic properties, but does not give the all-\(2u\) obstruction above. Ulas [3] develops general methods for \(2\)-adic valuations of powers of integer-coefficient series; its available description does not state this Thue--Morse boundary congruence or the \(r=1\) classification.

Searches also used synonymous formulations involving twice-odd exponents, \(m=2u\), exact binomial valuations, boundary coefficients \(2^A-1\), and \(2\)-adic valuations of powers of the Thue--Morse generating function. No stronger theorem implying the result was located.

The main residual originality risk is contemporaneous or not-yet-indexed work: [1] is a very recent preprint. No inaccessible source was identified whose title or available metadata specifically suggests the same \(r=1\) classification.

The result does **not** prove either direction of Conjecture 6.2 for general \(r\ge2\), and it does not address the separate automatic-odd-parts Conjecture 6.1.

## References

1. Zhao Shen, *Powers of the Thue--Morse Series: 2-Adic Valuations and Automatic Odd Parts*, arXiv:2609.16966v1 (2026), especially Theorems 1.1, 1.4 and Conjecture 6.2. https://arxiv.org/abs/2609.16966
2. Maciej Gawron, Piotr Miska, and Maciej Ulas, *Arithmetic properties of coefficients of power series expansion of \(\prod_{n=0}^{\infty}(1-x^{2^n})^t\) (with an appendix by Andrzej Schinzel)*, Monatsh. Math. 185 (2018), 307--360. https://doi.org/10.1007/s00605-017-1041-2
3. Maciej Ulas, *2-Adic valuations of coefficients of certain integer powers of formal power series*, Int. J. Number Theory 15 (2019), 723--762. https://doi.org/10.1142/S1793042119500386
