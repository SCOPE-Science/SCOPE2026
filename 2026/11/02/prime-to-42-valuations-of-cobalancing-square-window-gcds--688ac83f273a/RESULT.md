# Prime-to-42 valuations of cobalancing square-window GCDs

## Finding
For \(k\ge1\), define the infinite window GCD
\[
D_b(k)=\gcd_{n\ge0}\left(\sum_{i=1}^{k}b_{n+i}^{2}\right).
\]
Let \(\nu_p\) denote the valuation at a rational prime \(p\). For **every** positive integer \(k\) and every prime \(p\ge5\), \(p\ne7\),
\[
\boxed{\nu_p(D_b(k))=\min\{\nu_p(5k),\nu_p(B_k),\nu_p(C_k-1)\}.}
\]
Consequently, removing all factors of \(2\), \(3\), and \(7\) from an integer (denote the operation by \(\operatorname{co}_{42}\)) gives the exact identity
\[
\operatorname{co}_{42}(D_b(k))=
\operatorname{co}_{42}\bigl(\gcd(5k,B_k,C_k-1)\bigr).
\]
A distinctive explicit prime-five consequence, holding for all \(k\ge1\), is
\[
\boxed{\nu_5(D_b(k))=\begin{cases}0,&6\nmid k,\\1+\nu_5(k),&6\mid k.\end{cases}}
\]
For instance, \(D_b(6)=20\), \(D_b(30)=100\), and \(D_b(150)=500\).

## Assumptions and scope
The cobalancing sequence is \(b_0=b_1=0\) and \(b_{n+2}=6b_{n+1}-b_n+2\) for all \(n\ge0\). The balancing and Lucas-balancing sequences are \(B_0=0,B_1=1\), \(C_0=1,C_1=3\), and \(X_{n+2}=6X_{n+1}-X_n\). All window lengths \(k\) are positive integers. The GCD is the positive GCD of all indicated integer sums. The theorem concerns exactly the prime factors other than \(2,3,7\): these three exceptional primes are explicitly excluded, not assumed absent.

## Proof
Set \(y_n=b_n/2\); the recurrence and initial values show \(y_n\in\mathbb Z\). Put \(u=\sqrt2\), \(\gamma=1+u\), and \(\lambda=3+2u=\gamma^2\). The standard Pell closed form, or direct verification against the defining recurrence and initial values, gives
\[
y_n=a\lambda^n+b\lambda^{-n}-\tfrac14,\qquad a=\frac{\gamma^{-1}}{8u},\quad b=\frac{\gamma}{8u}.
\]
(The letter \(b\) without an index is the displayed coefficient, not a cobalancing number.) As \(ab=1/128\), squaring gives the exact identity
\[
y_n^2=\frac5{64}+a^2\lambda^{2n}+b^2\lambda^{-2n}
-\frac a2\lambda^n-\frac b2\lambda^{-n}.
\tag{1}
\]
Fix any prime \(p\ge5\) with \(p\ne7\), and work in the rank-two finite free algebra \(R=\mathbb Z_p[u]/(u^2-2)\). Its canonical basis is \(1,u\). Both \(u\) and \(\lambda\) are units in \(R\), and the four nonconstant coefficients of (1) are units in \(R\). Denote the largest integer \(e\ge0\) for which an element lies in \(p^eR\) by \(v_R\).

For \(j=1,2,3,4\), the quadratic norm of \(\lambda^j-1\) equals \(2-(\lambda^j+\lambda^{-j})\). Since \(\lambda^j+\lambda^{-j}=2C_j\), its four values are precisely
\[
-4,\quad -32,\quad -196,\quad -1152.
\tag{2}
\]
None of these integers is divisible by \(p\). Hence every difference between two distinct members of the five bases \(1,\lambda,\lambda^{-1},\lambda^2,\lambda^{-2}\) is a unit in \(R\), as is every denominator \(\lambda^j-1\) for \(j=\pm1,\pm2\).

Let \(T_n(k)=\sum_{i=1}^k y_{n+i}^2\). Summing (1) as geometric series yields a five-exponential expression in \(n\) whose constant coefficient is \(5k/64\) and whose four other coefficients are, for \(j\in\{-2,-1,1,2\}\), nonzero \(p\)-adic units multiplied by \((\lambda^{jk}-1)/(\lambda^{j}-1)\). The Vandermonde matrix of the five bases is invertible over \(R\) by (2). Therefore, for each integer \(e\ge0\), all the first five values \(T_0(k),\ldots,T_4(k)\) lie in \(p^eR\) **if and only if** all five exponential coefficients lie in \(p^eR\). The same implication from coefficients to all \(T_n(k)\) holds for every \(n\ge0\). Because \(T_n(k)\) are rational integers, this proves
\[
\nu_p(D_b(k))=\min\{\nu_p(5k),v_R(\lambda^k-1),v_R(\lambda^{2k}-1)\}.
\]
Here the factor \(4\) between the squared \(b\)-sum and the squared \(y\)-sum is a unit at \(p\). Since \(\lambda^{2k}-1=(\lambda^k-1)(\lambda^k+1)\), its valuation cannot be smaller than that of \(\lambda^k-1\), so the last minimum simplifies. Finally,
\[
\lambda^k=C_k+2uB_k
\]
is the standard balancing-number identity, directly checked by recurrence. Relative to the free basis \(1,u\), with \(2\) a \(p\)-adic unit,
\[
v_R(\lambda^k-1)=\min\{\nu_p(C_k-1),\nu_p(B_k)\}.
\]
Combining proves the prime-to-42 valuation identity for every positive \(k\).

For the special prime \(p=5\), one has \(\lambda^3=C_3+2uB_3=99+70u\equiv-1\pmod{5R}\), but \(\lambda\not\equiv-1\pmod{5R}\). Thus the exact order of \(\lambda\) modulo \(5R\) is \(6\). Also \(B_6=6930\) has \(\nu_5(B_6)=1\), while \(C_6-1=19600\) has \(\nu_5(C_6-1)=2\), whence \(v_R(\lambda^6-1)=1\). The binomial expansion of \((1+5w)^5-1\), followed by iteration, shows for every \(h\ge1\) that
\[
v_R(\lambda^{6h}-1)=1+\nu_5(h),
\]
where the initial \(w\) is a unit modulo \(5R\). If \(6\nmid k\), then \(v_R(\lambda^k-1)=0\). Substituting in the first formula, and using \(\nu_5(5k)=1+\nu_5(k)\), gives the asserted exact dichotomy. \(\square\)

## Verification
The squares \(y_n^2\) are a linear combination of exponentials with bases \(1,\lambda^{\pm1},\lambda^{\pm2}\); consequently their window sums satisfy the monic integer recurrence with characteristic polynomial
\[
(X-1)(X^2-6X+1)(X^2-34X+1).
\]
This shows that the GCD across **all** windows for a fixed \(k\) equals the GCD of the first five window sums, with no extrapolation. A standalone integer-only verifier (`verify.py`) computes this five-window GCD and independently checks the prime-to-42 identity and the prime-five valuation law for every \(1\le k\le500\). It additionally checks the recurrence and several exact sample values. These finite computations corroborate but do not replace the all-\(k\) proof above.

## Relationship to prior work
Mbirika, Schrader and Spilker (2023), Question 30, expressly seek closed forms for the GCDs of consecutive cobalancing squares and record only the observed divisibility by \(4\). Their full article supplies the recurrence definitions but not the stated prime-to-42 classification or the prime-five formula. Mbirika and Spilker (2022) establish square-window GCDs for generalized Fibonacci sequences satisfying \(G_{n+2}=G_{n+1}+G_n\), whose recurrence and hypotheses differ substantially from the affine cobalancing recurrence. The present result isolates the nonexceptional prime components using a quadratic Vandermonde argument and exposes prime \(5\) as a genuine contributor. It is partial progress on the 2023 question, not a claimed complete solution.

## Limitations
The theorem does **not** determine \(\nu_2(D_b(k))\), \(\nu_3(D_b(k))\), or \(\nu_7(D_b(k))\), and it does not assert a closed form for the entire integer \(D_b(k)\). Equation (2) explains why the Vandermonde proof does not directly cover those three primes. Literature checking cannot exclude undiscovered equivalent results or private/unindexed manuscripts. No independent mathematical audit has been performed.

## References
1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, arXiv:2301.05758 (first posted 2023-01-13), §§2 and 6, particularly Question 30. https://arxiv.org/abs/2301.05758
2. aBa Mbirika and Jürgen Spilker, *GCD of Sums of k Consecutive Squares of Generalized Fibonacci Numbers*, arXiv:2204.12626 (first posted 2022-04-26), §§1–3. https://arxiv.org/abs/2204.12626
