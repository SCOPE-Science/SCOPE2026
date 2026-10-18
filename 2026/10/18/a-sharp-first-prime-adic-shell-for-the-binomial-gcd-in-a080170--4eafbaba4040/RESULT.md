# A sharp first prime-adic shell for the binomial gcd in A080170

## Finding
For every integer \(k\ge 2\), define the binomial greatest common divisor
\[
D(k)=\gcd_{2\le q\le k+1}\binom{qk}{k}.
\]
**Theorem.** Let \(p\) be any prime, let \(a\ge2\), and take an integer \(m\) satisfying \(p^{a-1}<m<p^a\) and \(p\nmid m\). With \(n=p^a m\) and \(k=n-1\), one has the **exact integer equality**
\[
\boxed{D(p^a m-1)=p.}
\]
An explicit member of the defining binomial family attains the exact valuation \(1\): setting \(s=p^{a-1}-1\) and \(q_*=1+p^a s\),
\[
\boxed{\nu_p\!\left(\binom{q_*k}{k}\right)=1.}
\]
In particular, the nontrivial greatest common divisor on this entire first prime-adic shell is never divisible by \(p^2\), even when \(p^a\mid k+1\).

## Assumptions and scope
All integers and inequalities are literal; \(\nu_p\) is the valuation of a nonzero integer at prime \(p\). No conjectural implication or computation is assumed. The archival motivating object is OEIS A080170 (dated January 31, 2003); the published prime-divisor criterion used below is Lemma 9 of Guo–Qiu–Cao–Feng–Gao (2026). The latter paper settles whether \(D(k)=1\), not the exact valuation asserted here. A proof of the finite-difference prime-support fact is included to limit dependence on published results.

## Proof
Write \(A=p^a\), \(n=Am\), \(k=Am-1=A(m-1)+(A-1)\). The assumptions give \(p\nmid m\) and \(A/p<m<A\).

**Step 1: every binomial is divisible by \(p\).** Suppose \(p\nmid\binom{qk}{k}\) for some \(2\le q\le n\). By Lucas's theorem, the low \(a\) digits of \(qk\) must be \(p-1\), because those of \(k\) all equal \(p-1\). Therefore \(qk\equiv-1\pmod A\), hence \(q\equiv1\pmod A\) since \(k\equiv-1\pmod A\). Write \(q=1+At\), where \(1\le t\le m-1\). In the addition \(k+(q-1)k=qk\), the second summand is \(At k\). Below digit \(a\) it is zero. Above digit \(a\), the two summands begin as \(m-1\) and \(tk\). Their residues modulo \(A\) are \(m-1\) and \(A-t\), respectively, since \(tk\equiv-t\pmod A\). Because \(m-1\ge t\), their sum is at least \(A\), producing a carry. Kummer's theorem now contradicts nondivisibility. Thus \(p\mid D(k)\).

**Step 2: an explicit single-carry witness.** Put \(s=A/p-1\) and \(q_*=1+As\). As \(m>A/p\), one has \(s\le m-1\), so \(2\le q_*\le n\). We compute carries in
\[
k+As\,k=q_*k.
\]
The lowest \(a\) digits of the second addend are zero, so they produce no carries. Dividing at that digit boundary, the addition becomes \((m-1)+(sk)\). The exact identity
\[
sk=A(sm-1)+(A-s),\qquad A-s=(p-1)p^{a-1}+1
\]
shows that the lower \(a\) digits of \(sk\) are a \(1\) in position \(0\), zeros in positions \(1,\ldots,a-2\), and a \(p-1\) in position \(a-1\). The units digit of \(m-1\) is at most \(p-2\) (since \(p\nmid m\)), so the initial \(1\) causes no carry. The intervening zeros do not cause carries. Since \(m>A/p\), the digit of \(m-1\) in position \(a-1\) is at least \(1\); consequently there is precisely one carry from this position. At the next position the remaining upper addend is \(sm-1\); its units digit is at most \(p-2\), because \(sm\not\equiv0\pmod p\). Thus the propagated carry terminates immediately. No additional high digits of \(m-1\) remain, and exactly one carry has occurred. Kummer's theorem yields \(\nu_p\binom{q_*k}{k}=1\). Coupled with Step 1, this gives \(\nu_p(D(k))=1\).

**Step 3: exclusion of other prime divisors.** The elementary prime-support lemma \(r\mid D(k)\Rightarrow r\mid n\) follows from the polynomial \(F(x)=\binom{kx}{k}\) of degree \(k\): since \(F(0)=0\), \(F(1)=1\), and \(F(2),\ldots,F(k+1)\equiv0\pmod r\) if \(r\mid D(k)\), the order-\(k\) Newton forward-difference interpolation at \(x=0\) gives \(0\equiv k+1\pmod r\). (For complete details see Lemma 4 of the cited paper.) Now take a prime \(r\ne p\) dividing \(n\), and write \(r^e\Vert n\). Since \(r^e\mid m\), \(r^e\le m<A\), whereas \(n/r^e=Am/r^e\ge A>r^e\). The independently published local criterion (Guo et al., Lemma 9) states
\[
r\mid D(n-1)\quad\Longleftrightarrow\quad n/r^e\le r^e\qquad(r^e\Vert n).
\]
Its necessary condition therefore fails for every \(r\ne p\). Hence \(D(k)\) has no prime factor besides \(p\). Its \(p\)-valuation is exactly \(1\), proving \(D(k)=p\). \(\square\)

## Verification
The accompanying standard-library Python program `verify.py` checks the specified Kummer witness via independent factorial valuations; computes the gcd valuations by scanning the entire admissible binomial family for all moderate candidate indices; and checks several boundary cases. Execute `python verify.py` in the same directory. An exhaustive finite computation is evidence only for tested indices, not the proof of the infinite theorem.

## Relationship to prior work
OEIS A080170 asks for the indices \(k\) with \(D(k)=1\). Guo, Qiu, Cao, Feng and Gao proved a qualitative threshold in 2026 and, more precisely, the local **prime-support** criterion stated in Step 3. On the present shell their results imply \(p\mid D(k)\) and exclude primes other than \(p\), but do not bound its positive \(p\)-adic exponent by one. Step 2 supplies a new explicit witness with exactly one carry; this is the additional quantitative content. No general valuation formula for other shells is claimed. The ordinary row-binomial gcd theorem of Ram and the binomial-index families studied by Joris–Oestreicher–Steinig and McTague do not select the same fixed lower argument and moving upper arguments.

## Limitations
The result is restricted to \(a\ge2\) and the natural first shell \(A/p<m<A\) with \(p\nmid m\). It does not classify \(D(k)\) outside this shell, and it uses the published (nontrivial) local prime-divisor criterion in Step 3. A stronger general identity hidden in prior literature could imply the shell formula. The independent mathematical audit of this proof and the literature priority check are outstanding.

## References
1. OEIS Foundation, **A080170**, original entry by Benoit Cloitre dated 2003-01-31, https://oeis.org/A080170.
2. Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng and Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1 (2026), especially Lemmas 4 and 9 and Theorem 1, https://arxiv.org/html/2606.22997v1.
3. Édouard Lucas, Lucas's congruence theorem (1878); Ernst Kummer, theorem identifying binomial valuations with carrying in base \(p\) (1852).
