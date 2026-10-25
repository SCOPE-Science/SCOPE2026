# Complete dyadic cycle census for the Pell companion recurrence

## Finding

For each integer \(k\ge1\), let \(R_k=(\mathbb Z/2^k\mathbb Z)^2\), and act on it by the Pell companion permutation
\[
T_k(a,b)=(b,a+2b)\pmod{2^k}.
\]
The exact numbers of cycles of each *least* period are as follows:

| Least period | Number of cycles |
| --- | --- |
| \(1\) | \(2\), for all \(k\ge1\) |
| \(2\) | \(1\), for all \(k\ge1\) |
| \(4\) | \(0\) if \(k=1\), \(3\) if \(k=2\), \(7\) if \(k\ge3\) |
| \(2^t\), \(3\le t\le k\) | \(2^{t-1}\) when \(t=k\); \(3\cdot2^{t-1}\) when \(t<k\) |
| Other periods | \(0\) |

Thus the total number of cycles is \(3\) for \(k=1\) and exactly \(2^{k+1}-2\) for \(k\ge2\). For each fixed \(t\ge3\), the number of cycles of length \(2^t\) stabilizes at \(3\cdot2^{t-1}\) as soon as \(k\ge t+1\). In contrast, at its first appearance \(k=t\), that period has \(2^{t-1}\) cycles.

An individual-state classification accompanies the census. For any representatives \(a,b\in\mathbb Z\), put
\[
\Delta(a,b)=(a+b)^2-2b^2,
\qquad h_k(a,b)=2k-\min\{2k,\nu_2(\Delta(a,b))\},
\]
where \(\nu_2(0)=+\infty\). The least period is
\[
\pi_k(a,b)=
\begin{cases}
1,&h_k\le1,\\
2,&h_k=2,\\
4,&3\le h_k\le5,\\
2^{\lfloor h_k/2\rfloor},&6\le h_k\le2k.
\end{cases}
\]
The value of the truncated valuation, and hence the period, is independent of the chosen representatives.

## Assumptions and scope

The modulus is precisely a positive power of two; both state coordinates are arbitrary residues, not necessarily relatively prime to the modulus. Every state is periodic because the companion matrix has determinant \(-1\), a unit modulo \(2^k\). Least period always means the least positive return time of the ordered pair, not just of one scalar coordinate. The number of cycles counts orbits under the permutation, not states.

## Proof

**Step 1: ramified quadratic encoding.** Work in \(\mathcal O=\mathbb Z_2[\varpi]\), where \(\varpi^2=2\), with the normalized discrete valuation \(v(\varpi)=1\). For \(c,d\in\mathbb Z_2\), the two terms \(c^2\) and \(2d^2\) in the norm \(c^2-2d^2\) have valuations of opposite parity. Therefore they cannot cancel at their leading valuation, and
\[
v(c+d\varpi)=\nu_2(c^2-2d^2)
=\min\{2\nu_2(c),1+2\nu_2(d)\}.
\]
This also follows directly from the \(\varpi\)-adic expansion and shows that \(\mathcal O/(2^k)=\mathcal O/(\varpi^{2k})\) has \(2^{2k}\) elements and one residue class modulo \(\varpi\) of size two. Every truncated valuation shell is well defined in this quotient.

Set \(\lambda=1+\varpi\). Identify \((a,b)\) with
\[
\alpha=a+b\lambda=(a+b)+b\varpi\pmod{\varpi^{2k}}.
\]
Since \(\lambda^2=1+2\lambda\), multiplication by \(\lambda\) sends \(\alpha\) to \(b+(a+2b)\lambda\), exactly the state update. Multiplication by \(\lambda\) is invertible since its norm equals \(-1\).

**Step 2: powers of the unit.** Directly,
\[
v(\lambda-1)=1,\qquad
v(\lambda^2-1)=2,\qquad
v(\lambda^4-1)=5.
\]
Indeed, \(\lambda^2-1=2\lambda\) and \(\lambda^4-1=2\lambda\,2(\lambda+1)\); the factor \(\lambda+1=2+\varpi=\varpi(1+\varpi)\) has valuation one. For every \(s\ge2\), the element \(\lambda^{2^s}\) is congruent to one modulo \(\varpi^5\), so \(v(\lambda^{2^s}+1)=v(2)=2\). Induction via the difference-of-squares identity yields
\[
v(\lambda^{2^s}-1)=
\begin{cases}
1,&s=0,\\
2,&s=1,\\
2s+1,&s\ge2.
\end{cases}
\]
For every odd positive integer \(u\), the factor \(1+\lambda^{2^s}+\cdots+\lambda^{(u-1)2^s}\) is a unit modulo \(\varpi\), since its residue is \(u\equiv1\pmod2\). Hence \(v(\lambda^{u2^s}-1)=v(\lambda^{2^s}-1)\). There are therefore no non-power-of-two least periods.

**Step 3: exact least period of an individual state.** If \(\alpha\) has truncated valuation \(r=\min\{2k,v(\alpha)\}\), the return congruence \(\lambda^n\alpha\equiv\alpha\pmod{\varpi^{2k}}\) is equivalent to
\[
v(\lambda^n-1)\ge2k-r=h_k(a,b).
\]
Step 2 now gives the displayed formula for \(\pi_k(a,b)\), including the zero state and all boundary values. The norm expression for \(r\) is exactly \(\nu_2((a+b)^2-2b^2)\) truncated at \(2k\) by Step 1.

**Step 4: shell census and cycle division.** For each integer \(h\) satisfying \(1\le h\le2k\), there are exactly \(2^{h-1}\) states of truncated valuation \(2k-h\): there are \(2^h\) elements in the ideal quotient of valuation at least \(2k-h\), of which half have strictly larger valuation. The zero state supplies the unique element with \(h=0\). Hence \(h=0,1\) give \(1+1=2\) fixed states, and \(h=2\) gives two states of least period two, constituting one two-cycle. The \(h=3,4,5\) shells have respectively \(4,8,16\) states of least period four. Only \(h=3,4\) exist when \(k=2\), giving \((4+8)/4=3\) four-cycles, while all three exist when \(k\ge3\), giving seven; none exists when \(k=1\).

For \(t\ge3\), the period \(2^t\) arises from the shells \(h=2t\) and \(h=2t+1\). If \(k=t\), only \(h=2t\) occurs, yielding \(2^{2t-1}/2^t=2^{t-1}\) cycles. If \(k\ge t+1\), both occur, yielding \((2^{2t-1}+2^{2t})/2^t=3\cdot2^{t-1}\) cycles. Summing the displayed counts gives precisely \(3\) at \(k=1\) and \(2^{k+1}-2\) for \(k\ge2\). This proves the classification. \(\square\)

## Verification

The attached standalone file `verify.py` enumerates every state, follows its actual orbit using integer modular arithmetic, and independently checks its least period against the closed norm-valuation formula. It also compares the full cycle spectrum against the symbolic census. Executing `python3 verify.py` checks all \(87{,}380\) states for \(1\le k\le8\), without using the quadratic-ring proof in the orbit tracer. The symbolic valuation argument, rather than the finite replay, proves the theorem for arbitrary \(k\).

## Relationship to prior work

Pell matrix periodicity and generalized Pell recurrences have an established literature. In particular, Deveci and Karaduman (2015), Theorems 2.2 and 2.4–2.6, determine the period of the standard Pell sequence modulo prime powers and the order of its companion matrix. Their results cover the maximum period, but do not give the individual periods of *all* seed pairs, the exact numbers of cycles of each least period, or the complete total-cycle formula above. Deveci, Akdeniz, and Karaduman (2015) study generalized Pell sequences in finite groups under a different group-generating-seed setup. Deveci (2011) and Aydin–Dikici (1998) provide earlier general finite-group recurrence context, not this particular dyadic census. The ramified quadratic norm and complete shell enumeration supply the extra information. No claim is made to have discovered Pell periodicity or the companion-matrix method.

## Limitations

The exact formulas are proved only for the coefficient-two Pell recurrence and moduli \(2^k\), not arbitrary companion matrices, arbitrary prime powers, or moduli with odd factors. The formulas count ordered-pair orbits; individual scalar-coordinate periods may require separate analysis. Existing general results on finite modules or ramified quadratic unit actions might subsume portions of this specialized census despite the absence of explicit coverage in the inspected literature; a separate independent mathematical audit has not been performed.

## References

1. Ö. Deveci, E. Karaduman, *The Pell Sequences in Finite Groups*, Utilitas Mathematica **96** (2015), 263–276. Public full text: https://www.researchgate.net/publication/295591003_The_Pell_Sequences_in_Finite_Groups
2. Ö. Deveci, M. Akdeniz, E. Karaduman, *The Generalized Pell p-Sequences in Groups*, Ars Combinatoria **120** (2015), 383–401. Open article: https://combinatorialpress.com/ars-articles/volume-120-ars-articles/the-generalized-pell-sequences-in-groups/
3. Ö. Deveci, *The Polytopic-k-Step Fibonacci Sequences in Finite Groups*, Discrete Dynamics in Nature and Society (2011), article 431840, first published 10 October 2011, https://doi.org/10.1155/2011/431840
4. H. Aydin, R. Dikici, *General Fibonacci Sequences in Finite Groups*, Fibonacci Quarterly **36** (1998), 216–221, https://www.fq.math.ca/Scanned/36-3/aydin.pdf
