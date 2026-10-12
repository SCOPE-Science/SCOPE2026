# The odd-window square-sum gcd of cobalancing numbers

## Finding

Let \(b_0=b_1=0\) and \(b_{n+2}=6b_{n+1}-b_n+2\) for \(n\ge0\). These are cobalancing numbers (the first terms are \(0,0,2,14,84,492,\ldots\)). Let \(Q_0=Q_1=1\), \(Q_{n+2}=2Q_{n+1}+Q_n\), the associated Pell sequence. For **every positive odd integer** \(k\),
\[
\boxed{\gcd_{n\ge0}\left(\sum_{i=1}^k b_{n+i}^2\right)=4\gcd(k,Q_k).}
\]
The gcd is positive and taken over all nonnegative window starts. For example the values at \(k=1,3,5,21,63\) are \(4,4,4,28,28\). This result addresses the entire odd-index portion of the cobalancing-square case of Question 30 in [1].

## Assumptions and scope

All sequences and gcds are over integers. Set \(a_n=b_n/2\), so \(a_0=a_1=0\) and \(a_{n+2}=6a_{n+1}-a_n+1\); integrality follows from the recurrence. Define the balancing numbers \(B_0=0\), \(B_1=1\), \(B_{n+2}=6B_{n+1}-B_n\). Throughout, \(k\ge1\) is odd, \(h=(k-1)/2\), and \(E=Q_k\). We use \(F_n=\sum_{i=1}^k a_{n+i}^2\). No assertion is made about the analogous even-window gcd.

## Proof

**1. Shift factorization.** The cobalancing identities in [1, Definition 6 and Section 3] give, for odd \(k\),
\[
b_k=P_{k-1}Q_k,\qquad b_{k+1}=P_{k+1}Q_k,\qquad B_j=P_{2j}/2,
\]
where \(P_0=0\), \(P_1=1\), \(P_{n+2}=2P_{n+1}+P_n\). Hence \(a_k=E B_h\) and \(a_{k+1}=E B_{h+1}\). Both sequences \(a_{n+k}-a_n\) and \(B_{n+h}\) obey the same homogeneous recurrence of characteristic polynomial \(z^2-6z+1\), and the first two values agree. Thus for every \(n\ge0\),
\[
a_{n+k}-a_n=E B_{n+h}.\tag{1}
\]
Since \(\gcd(B_j,B_{j+1})=1\) and \(B_j\) has parity \(j\bmod2\), the shifted sequence \(u_n=B_{n+h}\) has coprime consecutive terms and assumes odd values infinitely often.

**2. The square-period obstruction is at most seven.** Put \(v_n=a_{n+k}+a_n\) and \(H=\gcd_{n\ge1}u_nv_n\). Since \(E=Q_k\) is odd and (1) gives \(v_n\equiv u_n\pmod2\), some \(u_nv_n\) is odd; hence \(H\) is odd. The recurrences are
\[
u_{n+2}=6u_{n+1}-u_n,\qquad v_{n+2}=6v_{n+1}-v_n+2.\tag{2}
\]
Suppose an odd prime \(p\) divides every \(u_nv_n\). There must be an index \(n\ge1\) with \(u_n\equiv0\pmod p\), since otherwise all \(v_n\) vanish modulo \(p\), contradicting the nonzero forcing term \(2\) in (2). Set \(u_j=u_{n+j}\), \(v_j=v_{n+j}\) temporarily. Then \(u_1\) is a unit modulo \(p\) and \(v_1\equiv0\pmod p\). The recurrence gives
\[
u_2\equiv6u_1,\quad u_3\equiv35u_1,\quad u_4\equiv204u_1\pmod p.\tag{3}
\]
If \(p\ge11\), \(u_2,u_3\) are units, so \(v_2=v_3=0\pmod p\), but (2) forces \(v_3=2\pmod p\), contradiction. For \(p=3\), \(u_3\) is a unit while \(v_3\equiv2\pmod3\), contradiction. For \(p=5\), \(u_2,u_4\) are units, forcing \(v_2=v_4=0\pmod5\), whereas (2) gives \(v_3=2\), \(v_4=14\pmod5\), contradiction. Therefore only \(p=7\) may divide \(H\).

Even \(49\) cannot divide \(H\). If it did, choose \(n\) with \(7\mid u_n\) as above. Both \(u_1,u_2\) are units modulo \(7\); consequently \(v_1=v_2=0\pmod{49}\). Thus \(v_3=2\) and \(v_4=14\pmod{49}\), while \(u_4\equiv204u_1\equiv u_1\not\equiv0\pmod7\). Therefore \(u_4v_4\) has exact \(7\)-adic valuation one, a contradiction. We have proved \(H\mid7\).

If \(7\mid H\), then (1) implies \(a_{n+k}^2\equiv a_n^2\pmod7\) for all \(n\ge1\). But the recurrence for \(a_n\) gives the exact periodic sequence \(a_n\bmod7=0,0,1,0,0,1,\ldots\), whose squared sequence has minimal period three. Consequently \(3\mid k\). This is the only condition on a potential factor \(7\) needed below.

**3. The endpoint congruence.** The homogeneous sequence \(t_n=4a_n+1\) satisfies \(t_0=t_1=1\) and \(t_{n+2}=6t_{n+1}-t_n\), so its invariant is
\[
t_n^2+t_{n+1}^2-6t_nt_{n+1}=-4.\tag{4}
\]
For \(G(x,y)=4y^2-12xy+5x-9y\), substitution of \(a_{n+2}=6a_{n+1}-a_n+1\) and (4) gives the exact telescoping identity
\[
64a_{n+1}^2=G(a_{n+1},a_{n+2})-G(a_n,a_{n+1})+5.\tag{5}
\]
Sum (5) from \(n=0\) through \(k-1\); since \(a_0=a_1=0\),
\[
64F_0=5k+G(a_k,a_{k+1}).\tag{6}
\]
Equation (1) implies \(E\mid a_k\) and \(E\mid a_{k+1}\), hence \(64F_0\equiv5k\pmod E\). Every \(Q_j\) is odd. Moreover \(5\nmid Q_k\) for odd \(k\): the Pell identity \(Q_k^2-2P_k^2=-1\) would otherwise require a square congruent to \(3\pmod5\). We conclude
\[
\gcd(F_0,E)=\gcd(k,E).\tag{7}
\]

**4. Removal of the possible factor seven.** For each \(n\ge0\),
\[
F_{n+1}-F_n=a_{n+k+1}^2-a_{n+1}^2=E u_{n+1}v_{n+1}.
\]
Therefore \(\gcd_{n\ge0}F_n=\gcd(F_0,EH)\). By Step 2, \(H\) is \(1\) or \(7\). In the latter case \(3\mid k\). Write \(k=3m\), necessarily with odd \(m\). The associated Pell identity \(2Q_{3m}=(\alpha^3)^m+(\beta^3)^m\), where \(\alpha=1+\sqrt2\), \(\beta=1-\sqrt2\), gives by the odd-power binomial lifting lemma at \(7\), using \(\alpha^3+\beta^3=14\) and \(\alpha^3\beta^3=-1\),
\[
\nu_7(Q_k)=1+\nu_7(m)=1+\nu_7(k).\tag{8}
\]
For clarity, the lifting lemma here is the elementary statement \(\nu_7(x^m+y^m)=\nu_7(x+y)+\nu_7(m)\) for odd \(m\) and \(7\)-adic units \(x,y\) with \(7\mid x+y\); it follows by binomial expansion for \(m\) prime to \(7\) and successive seventh powers. It applies in the unramified ring \(\mathbb Z_7[\sqrt2]\), where the integer \(7\)-valuation is preserved.
By (6), (8), and the fact that \(64\) and \(5\) are \(7\)-adic units, \(\nu_7(F_0)=\nu_7(k)\). Thus adjoining the one possible extra factor \(7\) to \(E\) cannot change \(\gcd(F_0,E)\). Combining with (7),
\[
\gcd_{n\ge0}F_n=\gcd(F_0,EH)=\gcd(k,Q_k).
\]
Finally \(b_n=2a_n\), so each original square-window sum is \(4F_n\), proving the boxed formula.

## Verification

A standalone Python 3 standard-library verifier, `verify.py`, builds the integer recurrences and checks the shift identity, telescoping identity, and claimed gcd against independently accumulated window sums for every odd \(k\le501\). It also verifies the modular-\(7\) pattern. The verification output is in `verification_output.txt`. These finite checks test normalization and algebra; the proof in the preceding section is unrestricted in \(k\) and \(n\).

## Relationship to prior work

Mbirika, Schrader and Spilker [1, Section 6.1, Question 30] explicitly ask for closed forms for the gcds of consecutive squared balancing, Lucas-balancing, cobalancing, and Lucas-cobalancing terms, and record only partial numerical observations. The formula here is for *all odd lengths* of the original cobalancing-square problem, and is not supplied by their unsquared braid identities. The generalized Fibonacci square-window result [2] concerns a different (homogeneous Fibonacci) recurrence; its statement does not imply this cobalancing identity. Searches for the explicit odd-window formula, aliases, Pell companion forms and recurrence reductions found no stronger equivalent published formula in the inspected sources.

## Limitations

The theorem does not evaluate even-window cobalancing square gcds, nor the square-window gcds for the other named sequences. No general claim of unpublished uniqueness is made: sources that are unindexed or not fully searchable may contain an equivalent result. The attached verifier is finite evidence only, not a replacement for the proof. No independent review has been performed.

## References

1. aBa Mbirika, Janee Schrader and Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of k consecutive Pell, balancing, and related numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4; arXiv:2301.05758, version 3, Section 6.1, Question 30. https://arxiv.org/abs/2301.05758 ; https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf
2. aBa Mbirika and Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269; arXiv:2204.12626. https://arxiv.org/abs/2204.12626
