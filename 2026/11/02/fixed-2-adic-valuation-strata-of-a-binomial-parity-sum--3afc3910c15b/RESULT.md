# Fixed 2-adic valuation strata of a binomial-parity sum

## Finding

For every integer \(n\ge0\), define the positive integer
\[
T(n)=\sum_{k=0}^{n}\left[\binom{n+5k}{2n+2k}\binom nk\pmod 2\right],
\]
where the square brackets are the ordinary residue in \(\{0,1\}\). Write \(\nu_2\) for the exponent of \(2\) dividing a positive integer. For integers \(r,v\ge0\), put
\[
a_r(v)=\#\{0\le n<2^r:\nu_2(T(n))=v\}.
\]
Set \(Q(t)=1-t-t^2-t^3-t^4-t^5\). Then the complete exact zero- and one-valuation dyadic enumerators are
\[
\boxed{\sum_{r\ge0}a_r(0)t^r=\frac{1+t+t^2+t^3}{Q(t)},\qquad
\sum_{r\ge0}a_r(1)t^r=\frac{t^4(1-t^5)}{(1+t^5)Q(t)^2}.}
\]
More generally, **for every fixed integer \(v\ge0\)**, \(\sum_{r\ge0}a_r(v)t^r\) is a computable rational function, and its coefficients satisfy the exact first-order asymptotic law
\[
\boxed{a_r(v)\sim c_v r^v\lambda^r\qquad(r\to\infty),}
\]
with explicitly positive constants described below. Here \(\lambda=1/\rho\approx1.9659482366454852\), and \(\rho\) is the unique positive root of \(Q\). In particular, every fixed valuation has natural density zero, but for every fixed \(v\) its counting function obeys
\[
\#\{0\le n<N:\nu_2(T(n))=v\}
=\Theta_v\bigl(N^{\log_2\lambda}(\log N)^v\bigr)
\qquad(N\to\infty).
\]
The zero-valuation binary-word count is separately known from OEIS A124312; the exact one-valuation enumerator and the uniform fixed-valuation asymptotic hierarchy are the additional claims examined here.

## Assumptions and scope

Only nonnegative integer indices \(n,r,v\) are considered. At \(n=0\), the sum contains the single term \(1\), hence \(T(0)=1\). An empty product of binary run weights is \(1\). The asymptotic statement fixes \(v\) before taking \(r\to\infty\); it does not claim uniformity when \(v\) grows with \(r\). The valuation \(\nu_2\) is applied only to positive integers, and positivity of \(T(n)\) follows from the recurrence and transform below.

Define \(S(0)=S(1)=S(2)=S(3)=1\) and
\[
S(\ell)=S(\ell-1)+S(\ell-2)-S(\ell-3)+S(\ell-4)
\quad(\ell\ge4).
\]
Theorem 13 of Rampersad and Wiebe (2023) states that \(T(n)\) equals the product of \(S(\ell)\) over the lengths \(\ell\) of all maximal runs of ones in the binary expansion of \(n\). This existing theorem is an explicitly cited premise, not a new result. The recurrence makes \(S\) positive: since its first four terms are nondecreasing and positive, the identity
\[
S(\ell)-S(\ell-1)
=S(\ell-2)-S(\ell-3)+S(\ell-4)>0
\quad(\ell\ge4)
\]
propagates nondecreasing positivity by induction.

## Proof

**1. Exact small 2-adic weights.** The recurrence's coefficient of \(S(\ell-4)\) is \(+1\). Thus its four-coordinate companion shift is invertible over \(\mathbb Z/2^h\mathbb Z\) for every positive integer \(h\), and every modular orbit is purely periodic, rather than merely eventually periodic. Direct substitution in the recurrence shows that the initial four-coordinate state repeats after five steps modulo \(2\), and after ten steps modulo \(4\). The corresponding residue blocks are, respectively,
\[
(S(0),\ldots,S(4))\bmod2=(1,1,1,1,0)
\]
and
\[
(S(0),\ldots,S(9))\bmod4=(1,1,1,1,2,3,1,3,3,0).
\]
Consequently, for every \(\ell\ge1\),
\[
\nu_2(S(\ell))=0\iff \ell\not\equiv4\pmod5,
\qquad
\nu_2(S(\ell))=1\iff \ell\equiv4\pmod{10}.
\]
Lengths congruent to \(9\) modulo \(10\) have valuation at least two. More generally, for fixed \(v\), the exact classes of lengths with valuation \(j\le v\) are determined by \(S(\ell)\bmod 2^{v+1}\); their indicator functions are periodic.

**2. Binary-run renewal identity.** For nonnegative \(j\), let
\[
R_j(t)=\sum_{\substack{\ell\ge1\\\nu_2(S(\ell))=j}}t^\ell,
\qquad R(t,z)=\sum_{j\ge0}R_j(t)z^j.
\]
Unique factorization of a finite binary word into maximal one-runs separated by nonempty zero-runs, with arbitrary initial and terminal zeros, yields the formal generating function
\[
A(t,z)=\sum_{r\ge0}\sum_{v\ge0}a_r(v)t^r z^v
=\frac{1+R(t,z)}{1-t(1+R(t,z))}.
\]
This can also be checked by summing the contribution \(t^{k-1}R(t,z)^k/(1-t)^{k+1}\) from words having exactly \(k\ge1\) one-runs, together with the all-zero words \(1/(1-t)\). The identity is valid as a formal power series because each coefficient contains finitely many binary words.

By step 1,
\[
R_0(t)=\frac{t+t^2+t^3+t^5}{1-t^5},\qquad
R_1(t)=\frac{t^4}{1-t^{10}}.
\]
Write
\[
B(t)=1+R_0(t)=\frac{1+t+t^2+t^3}{1-t^5},\qquad
D(t)=1-tB(t)=\frac{Q(t)}{1-t^5}
\]
and \(E(t,z)=\sum_{j\ge1}R_j(t)z^j\). Algebraic expansion of the renewal identity gives
\[
A(t,z)=\frac{B(t)}{D(t)}+
\sum_{k\ge1}\frac{t^{k-1}E(t,z)^k}{D(t)^{k+1}}.
\]
Taking its constant and linear coefficients in \(z\) gives \(G_0=B/D\) and \(G_1=R_1/D^2\), which simplify to the two displayed rational functions. For any fixed \(v\ge1\), the exact formula is
\[
G_v(t)=\sum_{k=1}^{v}\frac{t^{k-1}}{D(t)^{k+1}}
\sum_{\substack{j_1,\ldots,j_k\ge1\\j_1+\cdots+j_k=v}}
\prod_{i=1}^{k}R_{j_i}(t).
\]
Each \(R_j\) appearing here is rational because its coefficients are purely periodic modulo a fixed power of two. This proves rationality and furnishes a finite algorithm for every fixed valuation.

**3. Exact asymptotic order and constants.** Let \(\rho\in(0,1)\) solve \(Q(\rho)=0\), and define
\[
d=-\rho D'(\rho)>0.
\]
Since \(\rho+\rho^2+\cdots+\rho^5=1\), the triangle inequality implies that \(Q\) has no other root of modulus at most \(\rho\): equality on that circle would force the first and second powers of the root to have the same positive argument. The root is simple because \(Q'(\rho)<0\). Periodic series \(R_j\) have poles only at roots of unity, all outside the circle of radius \(\rho\). Thus \(D(t)=d(1-t/\rho)+O((1-t/\rho)^2)\) at the unique dominant pole.

For \(v=0\), the simple pole of \(B/D\), with \(B(\rho)=1/\rho\), gives
\[
c_0=\frac{1}{\rho d}.
\]
For fixed \(v\ge1\), the term \(k=v\) in the exact sum for \(G_v\) has pole order \(v+1\); its numerator is \(t^{v-1}R_1(t)^v\). Every term with \(k<v\) has pole order at most \(v\), because the periodic \(R_j\) are regular at \(\rho\). Consequently the coefficient of \(t^r\) is asymptotic to \(c_v r^v\rho^{-r}\), where
\[
\boxed{c_v=\frac{\rho^{v-1}R_1(\rho)^v}{v!d^{v+1}}>0\qquad(v\ge1).}
\]
The standard identity \([t^r](1-t/\rho)^{-v-1}=\binom{r+v}{v}\rho^{-r}\) gives the constant without any probabilistic limit assumption. With \(\lambda=\rho^{-1}<2\), these estimates imply vanishing natural density at every fixed valuation. For \(2^r\le N<2^{r+1}\), monotonicity of the counting function sandwiches it between \(a_r(v)\) and \(a_{r+1}(v)\); substituting the just-proved asymptotic gives the asserted \(\Theta_v\) estimate for arbitrary \(N\).

## Verification

The included standalone script `verify.py` uses only the Python standard library. It verifies the modular companion-state returns modulo \(2\) and \(4\), directly evaluates the original binomial-parity sum through \(n=1999\) using Lucas parity, independently computes the published run-length product for those indices, and exhaustively checks both rational-function coefficient formulas against all binary words through \(r=17\) inclusive (262,143 total dyadic word checks across levels). It also verifies that the level counts partition all \(2^r\) words. The executable returns `VERIFY_OK` on success. Finite checks are corroboration; the proof above supplies the unrestricted assertions.

For orientation, the exact sequences \(a_r(0)\), beginning at \(r=0\), are \(1,2,4,8,15,30,59,116,228,448,881,1732,\ldots\), and \(a_r(1)\) begins \(0,0,0,0,1,2,5,12,28,62,138,302,\ldots\). Both are independently reconstructible from the displayed rational generating functions.

## Relationship to prior work

Rampersad and Wiebe (2023), Theorem 13, already identify the binomial parity sum with this specific fourth-order run-length transform. Their result is used explicitly; no new run-length identity is claimed. Chai Wah Wu (2022) develops the earlier binomial-sum/run-transform framework, focused on other underlying sequences. The known zero-valuation word count coincides (by exchanging zero and one digits) with the sequence described in OEIS A124312; the pentanacci denominator and that baseline count are therefore **not claimed as discoveries**. The nearby OEIS A118898 counts words with one occurrence of `0000`, and its coefficient at binary length ten is \(136\), rather than the present exact one-valuation count \(138\); those problems differ beyond their initial agreement. Neither sequence entry supplies the one-valuation rational function or the fixed-valuation asymptotic hierarchy for this binomial sum. The exact additional results concern valuation one and all fixed higher strata, including their pole orders and positive leading constants.

## Limitations

This result does not give a uniform asymptotic when the valuation grows with \(r\), a central-limit theorem for a typical valuation, or information about odd-prime valuations. The fixed-valuation rational functions can become computationally large because their residue periods modulo increasing powers of two may grow. The claim of originality is limited to the inspected literature and mathematical-record evidence; an unlocated stronger or equivalent enumeration may exist.

## References

1. N. Rampersad and M. Wiebe, *Sums of products of binomial coefficients mod 2 and 2-regular sequences*, arXiv:2309.04012v1, first public 7 September 2023, Theorem 13; https://arxiv.org/abs/2309.04012 .
2. C. W. Wu, *Sums of products of binomial coefficients mod 2 and run length transforms of sequences*, INTEGERS **22** (2022), #A81; https://math.colgate.edu/~integers/w81/w81.pdf .
3. OEIS A124312, pentanacci sequence with an explicit binary-word interpretation avoiding zero-runs of lengths congruent to four modulo five; https://oeis.org/A124312 .
4. OEIS A118898, binary words with exactly one occurrence of a four-zero subsequence, a related but distinct enumeration; https://oeis.org/A118898 .
