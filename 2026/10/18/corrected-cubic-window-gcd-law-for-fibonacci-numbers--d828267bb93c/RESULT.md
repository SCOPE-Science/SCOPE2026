# Corrected cubic-window gcd law for Fibonacci numbers

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). Let \(L_m=F_{m-1}+F_{m+1}\) for \(m\ge1\). For every even integer \(k\ge2\), define
\[
C_3(k)=\gcd_{n\ge0}\left(\sum_{i=1}^{k}F_{n+i}^{3}\right),\qquad
H(k)=\begin{cases}F_{k/2},&4\mid k,\\ L_{k/2},&k\equiv2\pmod4.\end{cases}
\]
Then the **exact** gcd of all cubic windows is
\[
\boxed{C_3(k)=\frac{3^{\mathbf{1}_{8\mid k}}}{2^{\mathbf{1}_{6\mid k}}}\,H(k).}
\]
Equivalently, with \(A(k)=\gcd(F_{k+1}^{3}-1,F_{k+2}^{3}-1)\),
\[
\boxed{A(k)=3^{\mathbf{1}_{8\mid k}}H(k),\qquad
C_3(k)=\begin{cases}A(k)/2,&6\mid k,\\A(k),&6\nmid k.\end{cases}}
\]
The quotients are integers. For example, \(C_3(6)=2\) while \(A(6)=4\); and \(C_3(8)=A(8)=9\). These reverse the two cases in the Fibonacci-cube conjecture printed in Question 6.1 of Mbirika--Spilker (2022). Both the correction and its all-even-length proof are part of the finding.

## Assumptions and scope

Only the classical Fibonacci sequence with the stated normalization is considered. The gcd is the positive gcd of the infinite family of integer sums, with every starting index \(n\ge0\) included. The result holds for **all** even window lengths \(k\ge2\); no assertion is made for odd lengths, Lucas cubic windows, or arbitrary generalized Fibonacci initial data.

## Proof

**1. The first-power period divisor.** Fix \(k=2m\), and put \(u=F_{k+1}\), \(v=F_{k+2}\), and \(h=\gcd(u-1,v-1)\). Let
\[
M=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad w=\binom11.
\]
The vector \(M^kw=(v,u)^T\). Since \(\det M=-1\), multiplying an integer vector by \(M^m\) preserves the gcd of its entries. The classical matrix identities
\[
M^m-M^{-m}=\begin{cases}F_m(M+M^{-1}),&m\text{ even},\\L_m I,&m\text{ odd}\end{cases}
\]
follow from the characteristic roots of \(M\) (or the Fibonacci recurrence). Using \(M^{2m}-I=M^m(M^m-M^{-m})\), \((M+M^{-1})w=(3,1)^T\), and \(\gcd(3,1)=\gcd(1,1)=1\), we get
\[
h=\begin{cases}F_m,&m\text{ even},\\L_m,&m\text{ odd}.\end{cases}=H(k).
\]
Cassini's identity at even \(k\) also gives the norm relation
\[
u^2+uv-v^2=1.\tag{1}
\]

**2. Cubing creates exactly one possible extra factor of three.** Set \(A=\gcd(u^3-1,v^3-1)\), so \(h\mid A\). We show
\[
A=\begin{cases}3h,&8\mid k,\\h,&8\nmid k.\end{cases}\tag{2}
\]
Fix a prime \(\ell\ne3\) and a positive exponent \(e\) such that \(\ell^e\mid A\). Modulo \(\ell\), both \(u\) and \(v\) are cube roots of unity. If \(\ell=2\) or \(\ell\equiv2\pmod3\), each is \(1\). Otherwise the three possible roots are \(1,\omega,\omega^2\), where \(\omega^2+\omega+1=0\). Direct substitution of these nine pairs into (1) shows that, in characteristic other than three, the only pair satisfying (1) is \((1,1)\). Therefore \(u\equiv v\equiv1\pmod\ell\). The factorization \(x^3-1=(x-1)(x^2+x+1)\) gives \(\nu_\ell(x^3-1)=\nu_\ell(x-1)\) for such \(x\) and \(\ell\ne3\). Thus \(A\) and \(h\) have identical \(\ell\)-adic valuations for every \(\ell\ne3\).

Modulo three, \(x^3\equiv x\). The Fibonacci sequence modulo three has period eight; for even \(k\), the pair \((u,v)\) modulo three is \((1,1)\), \((2,0)\), \((2,2)\), or \((1,0)\) according as \(k\equiv0,2,4,6\pmod8\). Therefore \(3\mid A\) precisely when \(8\mid k\). In that case both \(u\) and \(v\) are one modulo three; the factorization above (or the lifting-the-exponent lemma) gives \(\nu_3(x^3-1)=\nu_3(x-1)+1\). This proves (2).

**3. All cubic window differences have gcd \(A\).** Write
\[
S_n=\sum_{i=1}^{k}F_{n+i}^3,\qquad
S_{n+1}-S_n=F_{n+k+1}^3-F_{n+1}^3.
\]
Because \(h\mid u-1,v-1\), the Fibonacci recurrence gives \(h\mid(F_{n+k}-F_n)\) for every \(n\ge1\). Therefore \(h\) divides every cubic difference. If \(8\mid k\), then \(3\mid h\), so writing \(F_{n+k}-F_n=ht\) shows
\[
F_{n+k}^3-F_n^3=ht\bigl(3F_n^2+3F_nht+h^2t^2\bigr)
\]
is divisible by \(3h\). In all cases (2) implies \(A\) divides every cubic difference. Conversely, the differences at indices one and two are \(u^3-1\) and \(v^3-1\), whose gcd is exactly \(A\). Hence
\[
\gcd_{n\ge0}(S_{n+1}-S_n)=A,
\qquad C_3(k)=\gcd(A,S_0).\tag{3}
\]

**4. The initial window contributes precisely the two-adic correction.** A polynomial telescoping identity valid for every Fibonacci pair \((x,y)=(F_j,F_{j+1})\) is
\[
\big[-3y^3+3y(x+y)^2-(x+y)^3\big]
-\big[-3x^3+3xy^2-y^3\big]=2x^3.
\]
Summing gives
\[
2S_0=-3u^3+3uv^2-v^3+1.\tag{4}
\]
As \(u^3\equiv v^3\equiv1\pmod A\), equation (4) yields \(2S_0\equiv3(uv^2-1)\pmod A\). But \(h\mid u-1,v-1\), so \(h\mid uv^2-1\). Since \(A\mid3h\) by (2), this proves \(A\mid2S_0\).

If \(6\nmid k\), the Fibonacci parity pattern shows that \(u,v\) are not both odd, so \(h\), and therefore \(A\), are odd. Then \(A\mid S_0\), and (3) gives \(C_3(k)=A\).

If \(6\mid k\), the matrix congruence \(M^6\equiv I\pmod4\) gives \(u\equiv v\equiv1\pmod4\). Set \(e=\nu_2(A)=\nu_2(h)\ge2\), \(a=u-1\), and \(b=v-1\). From (1), \((u-1)(u+1)=v(v-u)\). As \(v\) is odd, \(2^{e+1}\mid(v-u)\). Both \(a\) and \(b\) are divisible by \(2^e\); by the definition of \(e\), at least one has valuation exactly \(e\). Their difference is divisible by \(2^{e+1}\), so **both** have valuation exactly \(e\). Expanding (4),
\[
2S_0=-6a+3b-9a^2+6ab+3ab^2-3a^3-b^3
\equiv3b\pmod{2^{e+1}},
\]
since \(e\ge2\). Hence \(\nu_2(2S_0)=e\) and \(\nu_2(S_0)=e-1\). Combined with \(A\mid2S_0\), all odd prime-power factors of \(A\) divide \(S_0\), but its full two-part does not. Thus (3) gives \(C_3(k)=A/2\). Equations (2)--(3) complete the theorem.

## Verification

The standalone Python 3 checker `verify.py` uses integer arithmetic only. Run `python3 verify.py` after extracting the embedded files. It compares the formula to direct gcds of 31 consecutive cubic windows for all 200 even lengths from 2 through 400, checks 6,200 cubic differences modulo the predicted gcd, and checks the cubing, norm, and telescoping identities in each case. It also confirms the concrete contradictory cases \(k=6\) and \(k=8\). These tests are finite consistency checks; the four-part proof establishes the unbounded result.

## Relationship to prior work

Guyer and Mbirika (2021), Theorem 15 and Table 1, proved the first-power gcd and its Fibonacci/Lucas closed forms; these give the factor \(H(k)\), not the cubic gcd. Mbirika and Spilker (2022), Question 6.1, proposed an even-length Fibonacci-cube formula with the factor of one half on the **opposite** residue class. At \(k=8\) their stated expression would be \(9/2\), whereas the actual gcd is \(9\); at \(k=6\) their expression is \(4\), whereas the actual gcd is \(2\). The theorem corrects the entire cubic case, incorporating both a three-adic exceptional factor and the correct two-adic distinction. OEIS A210209 tabulates the **first-power** window gcd and does not itself supply the cubic result. These statements do not claim anything about whether the printed conjecture might be a typographical inversion; the mathematical content is the proved formula.

## Limitations

The result is restricted to classical Fibonacci cubes and even \(k\). The original question also raises Lucas cubes, generalized initial conditions, and higher powers; none is settled here. Independent scrutiny of this new proof has not been carried out. No claim of literature-wide uniqueness is made beyond the specifically inspected references and indexed searches.

## References

1. D. Guyer and aBa Mbirika, *GCD of sums of k consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, J. Integer Sequences 24 (2021), Article 21.9.8; arXiv:2104.12262, especially Theorem 15 and Table 1. https://arxiv.org/abs/2104.12262
2. aBa Mbirika and J. Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269; arXiv:2204.12626, especially Section 6, Question 6.1. First posted 2022-04-26. https://arxiv.org/abs/2204.12626
3. OEIS A210209, *GCD of all sums of n consecutive Fibonacci numbers*. https://oeis.org/A210209
