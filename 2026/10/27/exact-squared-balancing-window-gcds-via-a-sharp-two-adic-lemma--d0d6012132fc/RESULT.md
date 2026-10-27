# Exact squared balancing-window GCDs via a sharp two-adic lemma

## Finding

Let \(P_0=0\), \(P_1=1\), and \(P_{n+2}=2P_{n+1}+P_n\) be the Pell numbers. Let the balancing and Lucas-balancing sequences be defined by
\[
B_0=0,\quad B_1=1,\qquad C_0=1,\quad C_1=3,\qquad X_{n+2}=6X_{n+1}-X_n\quad(X=B,C).
\]
For every integer \(k\ge1\), define the positive GCD of all shifted squared balancing sums by
\[
G_B(k)=\gcd_{n\ge0}\left(\sum_{i=1}^k B_{n+i}^{2}\right).
\]
**Theorem.** Every positive integer \(k\) satisfies
\[
\boxed{G_B(k)=\frac{\gcd(k,P_{2k})}{\gcd(k,2)}.}
\]
The critical sharp valuation, also proved here for every \(k\ge1\), is
\[
\boxed{\nu_2\!\left(\sum_{i=1}^k B_i^2\right)=\nu_2(k(k+1))-1.}
\]
The theorem solves the squared balancing-sequence portion of Question 30 of Mbirika–Schrader–Spilker (2023), where the relation to the Lucas-balancing companion GCD was reported as a numerical observation.

## Assumptions and scope

All indices are integers; \(n\ge0\) and \(k\ge1\). The sequences are normalized as above. No bound on the window length or shift is imposed. The theorem concerns the squared balancing sequence only; the Lucas-balancing sequence is an auxiliary identity, not an independently claimed new GCD classification. The remaining cobalancing families are outside the scope. The gcd of an infinite family of positive integers means the positive generator of its integer ideal. The valuation \(\nu_p(m)\) is used only for nonzero integers \(m\).

## Proof

**1. Two telescoping identities.** Set \(Q_0=Q_1=1\), \(Q_{n+2}=2Q_{n+1}+Q_n\). Standard addition identities from the Pell recurrence give \(B_j=P_{2j}/2\), \(C_j=Q_{2j}\),
\[
C_j^2=8B_j^2+1=\frac{C_{2j}+1}{2},\qquad
B_{j+1}-B_{j-1}=2C_j\quad(j\ge1).
\]
Therefore
\[
\sum_{i=1}^k C_{2i}=\frac{B_{2k+1}-1}{2}.
\]
The Pell addition/difference formula with an index shift divisible by four yields
\[
B_{2k+1}-1=P_{2k}C_{k+1}.
\]
Thus, with \(T_B(k)=\sum_{i=1}^k B_i^2\) and \(T_C(k)=\sum_{i=1}^k C_i^2\),
\[
T_B(k)=\frac{B_{2k+1}-(2k+1)}{32}
=\frac{P_{2k}C_{k+1}-2k}{32},\qquad
T_C(k)=8T_B(k)+k=\frac{P_{2k}C_{k+1}+2k}{4}.\tag{1}
\]
All quotients in (1) are integers, as they equal the displayed sums.

**2. An exact two-adic lemma.** For every odd integer \(t\ge3\),
\[
\nu_2(B_t-t)=\nu_2(t^2-1)+2.\tag{2}
\]
To prove it, expand the generating function \(\sum_{t\ge1}B_tz^{t-1}=1/(1-6z+z^2)\) geometrically as
\[
\frac{1}{(1-z)^2-4z}
=\sum_{j\ge0}\frac{4^jz^j}{(1-z)^{2j+2}},
\quad\text{hence}\quad
B_t=\sum_{j=0}^{t-1}4^j\binom{t+j}{2j+1}.
\]
For \(j\ge1\), the binomial coefficient factors as
\[
\binom{t+j}{2j+1}=\frac{t\prod_{h=1}^{j}(t^2-h^2)}{(2j+1)!}.
\]
The terms \(j=1,2\) sum to
\[
\frac{2t(t^2-1)(t^2+1)}{15},
\]
which has valuation exactly \(\nu_2(t^2-1)+2\), because \(t\) is odd and \(\nu_2(t^2+1)=1\). Each term with \(j\ge3\) includes the factor \(t^2-9\), divisible by eight for odd \(t\), while \(\nu_2((2j+1)!)\le2j\). Hence every such term has valuation at least \(\nu_2(t^2-1)+3\). It cannot cancel the lower-valuation sum. Equation (2) follows. Taking \(t=2k+1\) in (1) gives
\[
\nu_2(T_B(k))=\nu_2(k(k+1))-1.\tag{3}
\]


**3. Exact GCDs of consecutive window differences.** For each \(n\ge1\), standard Pell identities give
\[
Q_{4(n+k)}-Q_{4n}=4P_{2k}P_{4n+2k}.
\]
Consequently,
\[
B_{n+k}^2-B_n^2=\frac{P_{2k}P_{4n+2k}}4.\tag{4}
\]
The Pell sequence is strongly divisible: \(\gcd(P_u,P_v)=P_{\gcd(u,v)}\) for positive \(u,v\). This follows from the addition formula \(P_{u+v}=P_uP_{v+1}+P_{u-1}P_v\), the consecutive-term coprimality \(\gcd(P_v,P_{v+1})=1\), and Euclidean induction. Therefore
\[
\gcd_{n\ge1}P_{4n+2k}=
\begin{cases}P_2=2,&k\text{ odd},\\P_4=12,&k\text{ even}.
\end{cases}
\]
For a fixed \(k\), adjacent window sums differ by (4). Hence the full infinite-window GCD equals the gcd of its first window \(T_X(k)\) and the gcd of these differences. Write the latter gcd as \(D_B(k)\). We obtain
\[
D_B(k)=\begin{cases}P_{2k}/2,&k\text{ odd},\\3P_{2k},&k\text{ even}.\end{cases}\tag{5}
\]
Thus \(G_B(k)=\gcd(T_B(k),D_B(k))\).

**4. Prime-by-prime evaluation.** Every \(Q_m\) is odd. Since \(P_{2m}=2P_mQ_m\) and \(P_m\) is odd for odd \(m\), induction gives
\[
\nu_2(P_m)=\nu_2(m)\qquad(m\ge1).\tag{6}
\]
Equations (3), (5), and (6) show that the two-adic valuation of \(G_B(k)\) is exactly \(\max\{\nu_2(k)-1,0\}\).

For any odd prime \(p\ne3\), (1) and (5) imply
\[
\nu_p(G_B(k))=\min\{\nu_p(k),\nu_p(P_{2k})\}.\tag{7}
\]
Indeed, modulo the highest power of \(p\) dividing \(P_{2k}\), the expression for \(T_B(k)\) reduces to a nonzero odd-prime-unit multiple of \(k\). The factors in (5) add no odd prime other than a possible extra factor \(3\).

It remains to control \(p=3\) when \(k\) is even. For every \(m\ge1\),
\[
\nu_3(P_{4m})=1+\nu_3(m).\tag{8}
\]
Here is an elementary proof. Put \(A=17+12\sqrt2\), \(A'=17-12\sqrt2\), so \(AA'=1\), \(P_{4m}=(A^m-A'^m)/(2\sqrt2)\). The quotient \(P_{4m}/12\) obeys \(U_0=0,U_1=1,U_{m+2}=34U_{m+1}-U_m\), whence modulo three \(U_m\equiv(-1)^{m-1}m\pmod3\). Thus \(3\mid U_m\) exactly when \(3\mid m\). Furthermore,
\[
U_{3m}=U_m\big((A^m+A'^m)^2-1\big).
\]
Since \(A\equiv-1+3\sqrt2\pmod9\) and \(A'\equiv-1-3\sqrt2\pmod9\), the binomial theorem gives \(A^m+A'^m\equiv2(-1)^m\pmod9\), so the parenthesized factor is congruent to \(3\pmod9\). Dividing \(m\) repeatedly by three proves (8).

For even \(k\), equation (8) gives \(\nu_3(P_{2k})=1+\nu_3(k)\). Thus the term involving \(P_{2k}\) in the numerator defining \(T_B(k)\) in (1) is divisible by one greater power of three than \(2k\). Consequently \(\nu_3(T_B(k))=\nu_3(k)\), and (5) shows that the extra factor three in \(D_B\) cannot alter (7). For odd \(k\), there is no extra factor three, so (7) holds automatically. Combining all prime valuations proves the asserted balancing GCD formula. \(\square\)

## Verification

Run `python3 verify.py` with Python 3; it requires only the standard library. It independently computes the original sequences by integer recurrence and checks the claimed balancing GCD against the first three window sums for every \(1\le k\le180\). Three windows suffice for this test because any squared second-order trace sequence satisfies the order-three recurrence with characteristic polynomial \((z-1)(z^2-34z+1)\), whose constant coefficient is a unit. The checker also compares the difference GCD in (5), the prefix-sum identities, and the odd-index valuation lemma through index \(361\).

The executable checks are finite corroboration; the proof above covers all \(k\ge1\) and all shifts \(n\ge0\) without relying on extrapolation.

## Relationship to prior work

Mbirika, Schrader, and Spilker (2023), Question 30, explicitly asks for closed forms for the square-window GCDs of balancing and Lucas-balancing sequences and reports the even/odd ratio between them as computational evidence. The present theorem supplies a proof for the **balancing** square-GCD and its sharp two-adic prefix valuation. A Lucas-balancing counterpart giving \(G_C(k)=\gcd(k,B_k)\) is already known; the present theorem is not claiming that counterpart as new. The identity \(\gcd(k,B_k)=\gcd(k,P_{2k})\) follows because \(B_k=P_{2k}/2\) and \(\nu_2(B_k)=\nu_2(k)\). Together the companion formula and the new balancing theorem rigorously yield the even/odd ratio which the 2023 authors reported only as an observation. Their paper solves **first-power** GCD problems and offers squared-window observations but does not prove this balancing-square formula. Mbirika and Spilker (2022) treat squares of sequences with Fibonacci coefficient one rather than the present coefficient-six recurrence.

## Limitations

The result does not evaluate \(\gcd(k,P_{2k})\) into prime factors without computing that Pell term; its value is an exact, uniform reduction from infinitely many sums to a single finite arithmetic GCD. It does not newly classify the Lucas-balancing GCD or determine the square-window GCDs for the cobalancing and Lucas-cobalancing sequences or settle the paper's Question 31. Publication priority is subject to a more exhaustive literature examination; in particular, an unindexed general theorem for squared Lucas sequences might imply this case.

## References

1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of k consecutive Pell, balancing, and related numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4, especially definitions, Lemmas 11–13, and §6.1, Question 30. arXiv:2301.05758 (first posted 2023-01-13). https://arxiv.org/abs/2301.05758 .
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269, arXiv:2204.12626 (first posted 2022-04-26). https://arxiv.org/abs/2204.12626 .
3. C. Sanna, *The p-adic valuation of Lucas sequences*, Fibonacci Quarterly 54 (2016), 118–124. The relevant two-adic Pell valuation is also proved directly above.
