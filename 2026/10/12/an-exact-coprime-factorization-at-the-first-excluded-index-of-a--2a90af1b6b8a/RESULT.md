# An exact coprime factorization at the first excluded index of a Jacobsthal Lucas quotient

## Finding

Let the Jacobsthal sequence be defined by \(J_0=0\), \(J_1=1\) and \(J_{r+2}=J_{r+1}+2J_r\). For a positive integer \(r\), consider the rational Lucas quotient
\[
T_r=\frac{J_{9r}}{J_9J_r},\qquad J_9=171.
\]
For every integer \(n\ge1\) with \(3\nmid n\), both \(T_n\) and \(T_{3n}\) are positive integers and
\[
\boxed{\gcd(T_n,T_{3n})=\frac{J_{9n}}{57J_{3n}}.}
\]
More precisely, with \(\epsilon=(-1)^n\) and \(z=2^n\), define
\[
U_n=\frac{z^2+\epsilon z+1}{3},\qquad
V_n=\frac{z^{18}+\epsilon z^9+1}{3},\qquad
H_n=\frac{z^6+\epsilon z^3+1}{57}.
\]
All three are positive integers, \(\gcd(U_n,V_n)=1\), and
\[
\boxed{T_n=H_nU_n,\qquad T_{3n}=H_nV_n.}
\]
Consequently,
\[
\frac{T_n}{\gcd(T_n,T_{3n})}
=\frac{J_{3n}}{3J_n}
=U_n.
\]
This factor equals \(1\) only at \(n=1\). Thus for every \(n\ge2\) with \(3\nmid n\), the divisibility \(T_n\mid T_{3n}\) fails, and its exact missing factor is \(U_n\).

## Assumptions and scope

The quantifier covers every positive integer \(n\) not divisible by \(3\), without a size cutoff. The sequence \(J_r\) has the closed form \(J_r=(2^r-(-1)^r)/3\). The rational quotient \(T_r\) is defined for all positive \(r\), but this result asserts integrality and the gcd formula only for the indicated pair of indices \(r=n\) and \(r=3n\). The gcd is the positive integer gcd, not a polynomial gcd.

## Proof

**Step 1 (three exact factors).** Set \(z=2^n\) and \(\epsilon=(-1)^n\). Repeated difference-of-cubes factorizations give
\[
\frac{J_{3n}}{J_n}=C=z^2+\epsilon z+1,
\quad \frac{J_{9n}}{J_{3n}}=E=z^6+\epsilon z^3+1,
\quad \frac{J_{27n}}{J_{9n}}=F=z^{18}+\epsilon z^9+1.
\]
These are identities of positive integers for every \(n\ge1\). Therefore
\[
T_n=\frac{CE}{171},\qquad T_{3n}=\frac{EF}{171}.
\]

**Step 2 (normalizing integer factors).** Since \(2^n\equiv(-1)^n\pmod3\), the three integers \(C,E,F\) are divisible by \(3\). We also show that \(19\mid E\) when \(3\nmid n\). Modulo \(19\), the residue \(-8\equiv11\) has exact multiplicative order \(3\), because \(11^3\equiv1\) and \(11\not\equiv1\). Write \(w=(-8)^n\). When \(3\nmid n\), the residue \(w\) is a nontrivial cube root of unity modulo \(19\), so \(w^2+w+1\equiv0\pmod{19}\). But
\[
E=(\epsilon z^3)^2+\epsilon z^3+1=w^2+w+1.
\]
Consequently \(57=3\cdot19\mid E\). Thus \(C/3\), \(F/3\) and \(E/57\) are integers; moreover, since \(171=3\cdot57\), the identities in Step 1 become
\[
T_n=\frac C3\frac E{57}=U_nH_n,
\qquad T_{3n}=\frac F3\frac E{57}=V_nH_n.
\]
This also independently establishes the asserted integrality of the two quotients.

**Step 3 (the exact gcd).** The factorization \(z^3-\epsilon=(z-\epsilon)C\) implies \(z^3\equiv\epsilon\pmod C\). Because \(\epsilon^2=1\), it follows that \(z^9\equiv\epsilon\pmod C\) and \(z^{18}\equiv1\pmod C\). Hence
\[
F=z^{18}+\epsilon z^9+1\equiv3\pmod C.
\]
It follows that \(\gcd(C,F)=\gcd(C,3)=3\), where the last equality uses \(3\mid C\). Dividing both entries by \(3\) gives \(\gcd(U_n,V_n)=1\). Therefore \(\gcd(T_n,T_{3n})=H_n\), which is \(J_{9n}/(57J_{3n})\) by Step 1.

**Step 4 (sharpness of the boundary).** When \(n=1\), \(C=2^2-2+1=3\), so \(U_1=1\). If \(n\ge2\), then \(z=2^n\ge4\), and \(C\ge z^2-z+1>3\). Thus \(U_n>1\). Since \(T_n=H_nU_n\) and \(T_{3n}=H_nV_n\) with coprime \(U_n,V_n\), one has \(T_n\mid T_{3n}\) exactly in the single case \(n=1\), completing the proof.

## Verification

The standalone `verify.py` uses only Python's standard library. From independently evaluated Jacobsthal terms, it checks the three difference-of-cubes identities for \(1\le n\le500\) and checks the original quotients, their exact gcd, the coprime factorization and the sharp divisibility boundary for all \(1\le n\le400\) not divisible by \(3\) (267 indices). It also checks the required order-three congruence modulo \(19\). Its captured output is `verify_output.txt`. These finite arithmetic checks are not used to infer the theorem for infinitely many indices; Steps 1–4 supply that proof. For example, at \(n=2\), \(T_2=511=7\cdot73\) and \(\gcd(T_2,T_6)=73\).

## Relationship to prior work

Panraksa and Tangboonduangjit (2022) define normalized Lucas quotients \(T_r=U_{r\Delta}/(U_rU_\Delta)\) and establish a \(\Delta\)-almost strong divisibility property when the relevant indices avoid \(\Delta\) (their Theorem 7). For the Jacobsthal Lucas sequence \(U_r=J_r\), the discriminant has absolute value \(\Delta=9\). The index pair \((n,3n)\) falls outside the theorem's coprimality hypothesis, even though both quotients are integral when \(3\nmid n\). The exact factorization above describes this first excluded local stratum, determines the gcd there, and establishes an infinite, quantified obstruction to simply extending the strong-divisibility conclusion.

Sanna (2016) gives general prime-adic valuations for Lucas sequences, and Yildiz (2022) investigates Jacobsthal divisibility. Their pointwise valuation/divisibility statements are compatible with the present calculation; neither inspected work states this two-quotient coprime factorization or its exact lost factor. The valuation results could provide an alternative derivation, which remains relevant to the assessment of originality.

## Limitations

No classification is claimed for arbitrary pairs \((m,n)\), for \(3\mid n\), or for general Lucas-sequence parameters. The proof uses the specific Jacobsthal closed form and the prime \(19\) dividing \(J_9\). This is a self-contained mathematical argument with self-review only; no independent audit or external validation has been performed.

## References

1. C. Panraksa and A. Tangboonduangjit, *Some Divisibility Properties Concerning Lucas and Elliptic Divisibility Sequences*, Journal of Integer Sequences **25** (2022), Article 22.9.2, published October 28, 2022. https://cs.uwaterloo.ca/journals/JIS/VOL25/Tangboonduangjit/tang17.pdf
2. C. Sanna, *The p-Adic Valuation of Lucas Sequences*, Fibonacci Quarterly **54** (2016), 118–124. https://doi.org/10.1080/00150517.2016.12427821
3. V. Yildiz, *Some divisibility properties of Jacobsthal numbers*, arXiv:2212.08814v1 (2022). https://arxiv.org/abs/2212.08814
4. Christian Ballot, *Lucasnomial Fuss-Catalan Numbers and Related Divisibility Questions*, Journal of Integer Sequences **21** (2018). https://cs.uwaterloo.ca/journals/JIS/VOL21/Ballot/ballot30.pdf
