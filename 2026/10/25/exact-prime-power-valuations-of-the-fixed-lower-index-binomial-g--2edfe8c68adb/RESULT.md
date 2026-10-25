# Exact prime-power valuations of the fixed-lower-index binomial gcd

## Finding
For every integer \(k\ge2\), set \(n=k+1\) and
\[
D(k)=\gcd_{2\le q\le n}\binom{qk}{k}.
\]
For each prime \(p\mid n\), write \(p^a\parallel n\), put \(m=n/p^a\), and define \(L_p=\lfloor\log_p m\rfloor\), with \(L_p=0\) for \(m=1\). Then the entire gcd, not merely its prime support, is
\[
\boxed{D(k)=\prod_{p^a\parallel n}p^{\max\{0,a-L_p\}}.}
\]
In particular, \(D(k)\mid k+1\). If \(k+1=p^a\) is a prime power, then \(D(k)=p^a\). The formula refines the published criterion for \(D(k)=1\).

## Assumptions and scope
All variables are ordinary positive integers; \(k\ge2\). The gcd includes exactly the \(k\) values with \(2\le q\le k+1\). A prime-power component \(p^a\parallel n\) means \(p^a\mid n\) and \(p^{a+1}\nmid n\). The floor of \(\log_p m\) is an exact integer (the largest \(L\ge0\) with \(p^L\le m\)), not a numerical logarithm approximation. Two published lemmas from Guo–Qiu–Cao–Feng–Gao [1] are used: their Lemma 4 shows that every prime dividing \(D(k)\) divides \(n\), and their Lemma 9 shows that, for \(p^a\parallel n\), \(p\mid D(k)\) if and only if \(n/p^a\le p^a\). The new assertion here is the *exact exponent* when divisibility occurs.

## Proof
Fix a prime \(p^a\parallel n\), and abbreviate \(P=p^a\), \(m=n/P\), \(L=\lfloor\log_p m\rfloor\). Then \(p\nmid m\). If \(L\ge a\), then \(m\ge P\), and equality \(m=P\) is impossible because \(p\nmid m\). Therefore \(m>P\) and Lemma 9 of [1] gives \(v_p(D(k))=0\), as claimed. Henceforth \(L<a\), so \(m<P\). We prove \(v_p(D(k))=a-L\).

**Uniform lower bound.** Choose any \(q\in\{2,\ldots,n\}\), and put \(u=q-1\) and \(b=v_p(u)\). Kummer's theorem states that the exponent of \(p\) in \(\binom{qk}{k}\) is the number of carries in base \(p\) when adding \(k\) and \(uk\). A carry occurs at level \(j\ge1\) precisely when the least residues satisfy
\[
[qk]_{p^j}<[k]_{p^j}.
\]
For \(1\le j\le a\) with \(j>b\), we have \(k=mP-1\equiv-1\pmod{p^j}\). Hence \([k]_{p^j}=p^j-1\), while \([qk]_{p^j}\neq p^j-1\), because \(p^j\nmid q-1\). These levels contribute at least \(\max\{0,a-b\}\) carries.

Also \(qk=n-q+un\), and \(p^{a+b}\mid un\). For every level with \(a+L<j\le a+b\), we have \(p^j>mP>k\); furthermore \(0\le n-q<k\). Therefore \([qk]_{p^j}=n-q<[k]_{p^j}=k\). These disjoint higher levels contribute \(\max\{0,b-L\}\) further carries. Thus for all permitted \(q\),
\[
 v_p\binom{qk}{k}\ge\max\{0,a-b\}+\max\{0,b-L\}\ge a-L.
\]
In particular \(v_p(D(k))\ge a-L\).

**Matching witness when \(m=1\).** In this case \(k=p^a-1\), and the base-\(p\) expansion of \(k\) consists of \(a\) digits equal to \(p-1\). Adding \(k\) to itself gives exactly \(a\) carries (including the carry out of the top digit), so \(v_p\binom{2k}{k}=a=a-L\).

**Matching witness when \(2\le m<P\).** Let \(1\le t\le m-1\) and choose \(q=1+tP\). This lies in the required range \(2\le q\le mP=n\). Writing \(s_p(z)\) for the sum of base-\(p\) digits of a nonnegative integer \(z\), the identities
\[
\begin{aligned}
k&=(m-1)P+(P-1),\\
tPk&=(tm-1)P^2+(P-t)P,\\
qk&=tmP^2+(m-1-t)P+(P-1)
\end{aligned}
\]
are genuine nonoverlapping base-\(p\) digit-block decompositions since \(1\le t\le m-1<P\). Legendre's digit-sum formula, combined with \(p\nmid m\), now yields
\[
\boxed{v_p\binom{(1+tP)(mP-1)}{mP-1}=a-v_p\binom{m-1}{t}.}\tag{1}
\]
For completeness, substituting the blocks into \(v_p\binom{U+V}{U}=(s_p(U)+s_p(V)-s_p(U+V))/(p-1)\), and using \(s_p(z-1)=s_p(z)-1+(p-1)v_p(z)\) for \(z\ge1\) together with \(s_p(P-t)=a(p-1)-s_p(t-1)\), gives (1).

If \(L=0\), then \(m<p\), and \(t=1\) gives \(v_p\binom{m-1}{1}=v_p(m-1)=0\). Thus (1) equals \(a\). If \(L\ge1\), write \(m=p^L+s\) with \(1\le s<(p-1)p^L\). Because \(p\nmid m\), also \(p\nmid s\). Choose \(t=p^L-1\), for which \(1\le t\le m-1\). Adding \(t\) to \(s=m-1-t\) in base \(p\) produces exactly \(L\) carries: its lowest \(L\) digits equal \(p-1\), the nonzero units digit of \(s\) starts the carry chain, and the sum \(m-1<p^{L+1}\) produces no further carry. Hence Kummer's theorem gives \(v_p\binom{m-1}{t}=L\). The chosen \(q=1+tP\) therefore achieves \(a-L\) in (1), proving \(v_p(D(k))=a-L\).

Finally, Lemma 4 of [1] rules out all primes \(p\nmid n\) as factors of \(D(k)\). Multiplying these exact prime valuations proves the formula. \(\square\)

## Verification
The accompanying standard-library program `check.py` independently computes the claimed valuation at every prime dividing \(n\) for every \(3\le n\le1200\) (1,198 cases), directly forms large-integer gcds of the defining binomial coefficients for \(3\le n\le80\) (78 cases), and verifies identity (1) in 1,295 eligible small-parameter choices. Run `python3 check.py` to reproduce `CERTIFICATE_OK n_formulas= 1198 direct_gcd_cases= 78 witness_identity_cases= 1295`. These checks are finite tests, not a substitute for the proof for every \(k\).

## Relationship to prior work
Guo, Qiu, Cao, Feng and Gao [1], arXiv:2606.22997v1 (first publicly available June 22, 2026), establish the gcd-one criterion, exclusion of prime factors not dividing \(k+1\) (Lemma 4), and their prime-support criterion (Lemma 9). The present result retains those published facts as cited inputs and supplies an explicit valuation for *every* prime factor. In particular, the Boolean condition \(D(k)=1\) does not imply the exact positive exponents. Classical row-gcd theorems and selected fixed-upper-index binomial gcds cited in [1] concern different coefficient families. Related results on other constrained binomial gcds do not by themselves yield equation (1) and this valuation formula.

## Limitations
The result concerns the fixed lower index and the exact finite upper-multiplier interval stated here, not arbitrary multiplier sets or a general theorem on all binomial gcds. Earlier implicit statements of this exponent formula could exist in classical or incompletely indexed literature. The classification uses two published support lemmas; it is not a new independent proof of their conclusions. The computations corroborate, but do not prove, the infinite statement. Independent mathematical audit has not been performed.

## References
[1] Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng, Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1, first submitted 2026-06-22, https://arxiv.org/html/2606.22997v1 . Relevant: Theorem 1, Lemmas 4 and 9.

[2] E. E. Kummer, classical carry characterization of prime valuations of binomial coefficients; and A. M. Legendre, factorial valuation/digit-sum formula.

[3] OEIS A080170, the original gcd-one sequence and problem motivating [1], https://oeis.org/A080170 .
