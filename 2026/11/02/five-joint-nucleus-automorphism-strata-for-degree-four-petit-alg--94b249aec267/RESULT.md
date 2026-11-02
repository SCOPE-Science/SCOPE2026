# Five joint nucleus–automorphism strata for degree-four Petit algebras over finite fields

## Finding
Let \(q\) be a prime power satisfying \(q\equiv1\pmod4\). Fix \(K=\mathbb F_{q^4}\), \(F=\mathbb F_q\), and the Frobenius generator \(\sigma(c)=c^q\). For every \(a\in K\setminus F\), define the proper nonassociative cyclic Petit algebra \(A_a\) on \(K\oplus Kt\oplus Kt^2\oplus Kt^3\) by multiplication of skew polynomials modulo the **right** remainder on division by \(t^4-a\). Isomorphisms and automorphisms are \(F\)-algebra maps; \(\operatorname{Nuc}_r\) is the right associative nucleus. Put \(N=(q^4-1)/(q-1)\).

The isomorphism classes of these algebras have **exactly five nonempty joint strata**, indexed by the \(F\)-dimension of their right nucleus and the order of their automorphism group:

| \(\dim_F\operatorname{Nuc}_r(A)\) | \(|\operatorname{Aut}_F(A)|\) | Number of isomorphism classes |
| :--: | :--: | --: |
| \(4\) | \(N\) | \((q-1)(q+1)^2/4\) |
| \(4\) | \(2N\) | \((q-1)/2\) |
| \(4\) | \(4N\) | \(2\) |
| \(8\) | \(2N\) | \((q-1)/2\) |
| \(8\) | \(4N\) | \(1\) |

No other joint pair occurs. The class total is \((q^3+q^2+3q+7)/4\). In particular, both automorphism orders \(2N\) and \(4N\) occur with either possible right-nucleus dimension, so neither of these two invariants determines the other. The last two statements are deductions from the complete five-stratum census, not separately asserted findings.

## Assumptions and scope
The field \(F\) has characteristic different from \(2\), contains a primitive fourth root of unity, and \(K/F\) is its unique cyclic extension of degree \(4\). The twisting automorphism is the specified \(q\)-Frobenius; changing its generator is not part of the equivalence relation. Parameters are nonzero and noncentral (\(a\in K\setminus F\)); reducible defining skew polynomials and hence algebras with zero divisors are **included**. Nothing here claims to classify only division semifields, isotopy classes, or algebras arising from different twisting generators. The explicit individual classifications of isomorphisms, automorphisms, and right nuclei used in the proof are prior results [1–3]; the conclusion here is their simultaneous exact arithmetic distribution in the first composite extension degree.

## Proof
**1. Isomorphism orbits.** The finite-field norm \(N_{K/F}:K^\times\to F^\times\) is surjective. By the degree-four case of the monomial-isomorphism theorem [1, Corollary 3.12 and Theorem 2.8], the full \(F\)-algebra isomorphism relation among proper \(A_a\) is
\[
 A_a\cong_F A_b\ \Longleftrightarrow\ \sigma^j(a)=c b\quad\text{for some }0\le j<4,\ c\in F^\times.
\]
Thus classes are Frobenius orbits in \((K^\times/F^\times)\setminus\{[1]\}\). There is no identification across distinct twisting generators in the statement.

**2. Parameter supports.** Choose \(\zeta\in F^\times\) of order \(4\). Since \(\sigma\) has order four and \(4\) is invertible in \(F\), its \(F\)-linear action on \(K\) has four one-dimensional eigenspaces with eigenvalues \(1,\zeta,\zeta^2,\zeta^3\). Concretely, Kummer theory gives \(\beta\in K\) with \(\sigma(\beta)=\zeta\beta\), such that \(1,\beta,\beta^2,\beta^3\) is an \(F\)-basis. Write \(a=\sum_{i=0}^3 a_i\beta^i\). Its nonempty coefficient support \(I=\{i:a_i\ne0\}\) is preserved by nonzero \(F\)-scaling and by \(\sigma\). Proper nonassociativity excludes precisely the support \(\{0\}\). For each remaining support \(I\), the number of projective parameter points is exactly \((q-1)^{|I|-1}\).

Let \(r(I)\) denote the least positive \(r\mid4\) with \(\sigma^r(a)=a\), and \(e(I)\) the least positive \(e\mid4\) with \(\sigma^e(a)/a\in F^\times\). The eigenbasis makes both constants throughout each support stratum and yields
\[
 r(I)=\frac4{\gcd(4,\{i:i\in I\})},\qquad
 e(I)=\frac4{\gcd(4,\{i-j:i,j\in I\})}.
\]
Here \(\gcd(4,\{0\})=4\), and for a singleton support all differences equal zero. Each projective Frobenius orbit in the support has length \(e(I)\), so it contributes \((q-1)^{|I|-1}/e(I)\) isomorphism classes.

**3. Right nucleus.** Let \(f=t^4-a\) and \(g=\sum_{i=0}^3g_it^i\). The right-nucleus characterization for Petit algebras [3, Theorem 1] is \(g\in\operatorname{Nuc}_r(A_a)\) if and only if \(fg\in K[t;\sigma]f\). Because \(\sigma^4=\mathrm{id}_K\), one has
\[
 fg-gf=\sum_{i=0}^3g_i(\sigma^i(a)-a)t^i.
\]
The quotient in \(fg=hf\) is necessarily \(h=g\), by matching all coefficients of powers at least four; hence \(fg\in K[t;\sigma]f\) precisely when the displayed remainder vanishes. Thus the right nucleus is the \(K\)-span of \(t^i\) with \(r(I)\mid i\), and has \(F\)-dimension \(4(4/r(I))=16/r(I)\). In the noncentral cases \(r(I)\in\{2,4\}\), yielding precisely \(8\) or \(4\).

**4. Automorphisms.** The full automorphism theorem for proper degree-four cyclic Petit algebras [2, Theorem 4 and Corollary 11(i)] says all maps are \(G_{\sigma^j,u}\) with \(\sigma^j(a)=N_{K/F}(u)a\). For each of the \(4/e(I)\) exponents \(j\) stabilizing the projective class \([a]\), the required scalar belongs to \(F^\times\), and norm surjectivity gives exactly \(|\ker N_{K/F}|=N\) lifts \(u\). Therefore \(|\operatorname{Aut}_F(A_a)|=4N/e(I)\).

**5. Exhaustive support partition.** The supports \(I=\{2\}\) and \(I=\{0,2\}\) give respectively \((r,e)=(2,1)\) and \((2,2)\), contributing \(1\) and \((q-1)/2\) classes with right-nucleus dimension \(8\). The supports \(\{1\}\) and \(\{3\}\) give \((r,e)=(4,1)\) and exactly two classes with nucleus dimension \(4\). The support \(\{1,3\}\) gives \((4,2)\) and contributes \((q-1)/2\) classes. Every remaining nonempty support other than \(\{0\}\) necessarily contains indices of different parity, so \((r,e)=(4,4)\). The number of projective parameters in these remaining supports is
\[
 \frac{q^4-1}{q-1}-1-1-(q-1)-2-(q-1)
 =(q-1)(q+1)^2,
\]
where the subtracted terms correspond to \(\{0\}\), \(\{2\}\), \(\{0,2\}\), \(\{1\},\{3\}\), and \(\{1,3\}\). Dividing by orbit length four gives \((q-1)(q+1)^2/4\) classes. Combined with steps 3–4, these are exactly the five asserted rows. Summing their entries yields \((q^3+q^2+3q+7)/4\). \(\square\)

## Verification
The accompanying standalone Python program `verify.py` constructs the five strata by independently enumerating (i) all nonempty Kummer coefficient supports and their projective Frobenius orbit lengths, and (ii) all Frobenius orbits on the cyclic group \(K^\times/F^\times\), using the primitive-exponent test \(q^r a=a\) in the form \((q^r-1)k\equiv0\pmod{q^4-1}\). These independent descriptions agree for \(q=5,9,13,17\) and, as an auxiliary consistency check, for degree six over \(\mathbb F_7\). Both methods reproduce the symbolic five-row formula at each tested field.

For \(q=5\), \(N=156\), and the five multiplicities in the table order are \(36,2,2,2,1\), totaling \(43\) classes. These finite checks do not establish an infinite-field theorem; the proof above does.

## Relationship to prior work
Nevins–Pumplün [1] proves the underlying full isomorphism parametrization and Kummer-support classification; these are **not** new claims. Brown–Pumplün [2] computes automorphisms of Petit algebras, including the full norm conditions used here. Pumplün [3] establishes the right-nucleus subalgebra structure. The known number of unstratified isomorphism classes is not claimed independently new. What is assessed here is the complete **joint frequency table** for two intrinsic algebra invariants throughout the nondivision-inclusive degree-four family. In particular, [1] does not provide this nucleus–automorphism table, [2] does not stratify isomorphism classes by right nucleus, and [3] does not stratify them by automorphism-group size. These are distinct numerical questions; the three prior structural inputs are used explicitly rather than hidden.

## Limitations
The theorem counts \(F\)-isomorphism classes for a **fixed** Frobenius generator, not isomorphisms of multiplicative loops, isotopy classes, only division algebras, or simultaneous twisting-generator changes. It applies only for \(q\equiv1\pmod4\), and does not assert a formula for fields lacking fourth roots of unity, nor determine automorphism-group isomorphism types beyond their orders. The results are obtained by combining established structural theorems and a finite support enumeration; unlocated preexisting joint enumerations could reduce or eliminate historical novelty. No independent validation has been performed.

## References
[1] Monica Nevins and Susanne Pumplün, *A parametrization of nonassociative Petit algebras \(K[t;\sigma]/K[t;\sigma](t^m-a)\) up to equivalence*, arXiv:2610.30921v1, first posted 2026-10-22, especially Theorem 2.8, Theorem 3.11 and Corollary 3.12. https://arxiv.org/html/2610.30921v1

[2] Christian Brown and Susanne Pumplün, *The automorphisms of Petit’s algebras*, arXiv:1703.00718v2 (2017), Theorem 4 and Corollary 11. https://arxiv.org/pdf/1703.00718

[3] Susanne Pumplün, *Nonassociative cyclic algebras and the semiassociative Brauer monoid*, arXiv:2403.03263 / Rendiconti del Circolo Matematico di Palermo, Theorem 1 and skew-polynomial preliminaries. https://link.springer.com/article/10.1007/s12215-024-01105-4
