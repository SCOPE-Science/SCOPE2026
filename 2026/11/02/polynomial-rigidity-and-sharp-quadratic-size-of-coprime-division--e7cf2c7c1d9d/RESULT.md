# Polynomial rigidity and sharp quadratic size of coprime division lifts

## Finding
Fix a positive integer \(s\) and a polynomial \(T\in\mathbb Z[X,Y]\) with \(T(a,b)>s\) for every integer \(a\ge2\), \(b\ge1\). Consider the quotient-preserving multiplier template
\[
(a,b)\longmapsto\bigl(aT(a,b),\ bT(a,b)+s\bigr).
\]
The image pair is coprime for **every** such input if and only if \(s=1\) and \(T(X,Y)=XU(X,Y)\) in \(\mathbb Z[X,Y]\). In this case the polynomial divisor \(XT(X,Y)\) has \(X\)-degree at least two, and the lower bound is attained by \(T=X\). This is an optimality statement **within the common-multiplier, fixed-offset polynomial template**, not a claim about arbitrary reductions.

## Assumptions and scope
Coprime means ordinary greatest common divisor equal to one on the standard positive integers. The polynomial coefficients may have either sign, but the specified positivity hypothesis is global on the integer domain. For weak-arithmetic formalization, we additionally restrict to the subfamily \(T\in\mathbb N[X,Y]\), where the polynomial is represented by semiring terms. In a discretely ordered commutative semiring, the paper of Kato defines \(\operatorname{cop}(A,B)\) by nonnegative witnesses \(c,d\) satisfying \(Ad=Bc+1\), and \(\operatorname{euc}(a,b)\) by \(b=aq+r\) with \(r<a\).

## Proof
First suppose \(s>1\). Choose a prime \(p\mid s\) and put \(a=b=p\). Both \(pT(p,p)\) and \(pT(p,p)+s\) are divisible by \(p\). Thus universal coprimality forces \(s=1\).

Now let \(s=1\), and write \(S(Y)=T(0,Y)\). If \(S\ne0\), the integer polynomial \(P(Y)=YS(Y)+1\) has positive degree and unbounded absolute value along positive integers. Choose \(b\ge1\) such that \(|P(b)|>1\), and a prime \(p\mid P(b)\). For \(a=p\), reduction modulo \(p\) gives \(T(p,b)\equiv T(0,b)=S(b)\). Hence \(p\) divides both \(pT(p,b)\) and \(bT(p,b)+1\), contradicting universal coprimality. Therefore \(S=0\), which is equivalent to \(X\mid T\) in \(\mathbb Z[X,Y]\).

Conversely, suppose \(s=1\) and \(T=XU\). Put \(u=U(a,b)\) and \(m=abu\). The positivity hypothesis implies \(u\ge1\). Then \(aT(a,b)=a^2u\), \(bT(a,b)+1=m+1\), and the polynomial identity
\[
(a^2u)(b^2u)=(m+1)(m-1)+1
\]
provides a nonnegative Bézout witness \(d=b^2u\), \(c=m-1\). In particular, the two image coordinates are coprime. Since \(T=XU\ne0\), the \(X\)-degree of \(XT=X^2U\) is at least two, realized by \(T=X\).

For the semiring-term subfamily \(T\in\mathbb N[X,Y]\), divisibility \(X\mid T\) makes \(U\in\mathbb N[X,Y]\), and the positivity of \(u\), \(m\) and the displayed witness follows in \(\mathrm{PA}^{-}\) from \(a>1\) and \(b>0\). Kato's quotient-preserving equivalence \(\operatorname{euc}(a,b)\leftrightarrow\operatorname{euc}(ta,tb+s)\) for \(s<t\), applied to the term \(t=T(a,b)\) and \(s=1\), supplies quotient-preserving division equivalence. This last claim does not assert that a mixed-sign polynomial positive in the standard integers is provably positive in \(\mathrm{PA}^{-}\).

## Verification
A stand-alone Python program `checker.py` evaluates explicit admissible and inadmissible examples, the nonnegative certificate and modulo-prime obstructions. The general theorem is proved algebraically above; these tests are not substitutes for unbounded quantifiers.

## Relationship to prior work
Kato's 2026 theorem proves quotient preservation for every \(0\le s<t\), and uses the specific coprime lift \(T=X\), \(s=1\), solving Visser's question on restricted Euclidean division. The present result does **not** claim discovery of that lift, quotient preservation, or equivalence of the two division principles. Rather, it classifies the globally coprime members of the **whole fixed-offset polynomial multiplier template**, including signed-coefficient polynomials positive on the domain, and proves the exact quadratic lower bound inside this template. Visser's earlier paper posed the logical comparison and discussed coprime division; it does not give the polynomial rigidity criterion in its Section 8.8.

## Limitations
The polynomial template is a restricted class of transformations; no lower bound is established for arbitrary reductions or arbitrary computable multiplier functions. The mixed-sign generality is a standard-integer theorem, not an internal \(\mathrm{PA}^{-}\) formalization. Novelty of this elementary rigidity criterion under older polynomial/Bezout terminology requires independent historical verification; no independent audit has been performed.

## References
Naoya Kato, *Equivalence of Restricted and Full Division*, arXiv:2610.24976v1, first submitted 2026-10-18, especially Theorem 2 and Corollary 3. Albert Visser, *From Numbers to Container Strings*, arXiv:2411.15873v1 (2024-11-24), current open version v4, Section 8.8, Theorems 8.26–8.27 and Question 8.29.
