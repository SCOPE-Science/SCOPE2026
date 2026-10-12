# Characteristic-two Rota–Baxter resonance on square-zero local algebras

## Finding
Let \(K\) be any field and let \(A=K\oplus V\) be the unital algebra with \(V^2=0\) and \(1\le n=\dim_K V<\infty\). A \(K\)-linear operator \(P:A\to A\) is a weight-zero Rota–Baxter operator precisely when there are uniquely determined \(u\in V\) and \(L\in\operatorname{End}_K(V)\) such that
\[
P(a+v)=au+L(v),\qquad L^2=0,\qquad 2L(u)=0.
\]
Consequently, in characteristic two the condition on \(u\) disappears, every such operator satisfies \(P^3=0\), and \(P^2\ne0\) occurs if and only if \(L(u)\ne0\). Such an operator exists for every \(n\ge2\), whereas over fields of characteristic different from two every weight-zero Rota–Baxter operator on \(A\) satisfies \(P^2=0\).

The classification also gives exact finite-field rank and nilpotency-index strata. For \(K=\mathbb F_q\), \(0\le r\le\lfloor n/2\rfloor\), put
\[
M_q(n,r)=\binom nr_q\binom{n-r}r_q\prod_{i=0}^{r-1}(q^r-q^i),
\]
where \(\binom ab_q\) denotes the Gaussian binomial coefficient and an empty product is one. Exactly \(M_q(n,r)\) endomorphisms \(L\) have \(L^2=0\) and \(\operatorname{rank}L=r\). For each such \(L\), the possible vectors \(u\), grouped by \((\operatorname{rank}P,\text{nilpotency index})\), are:

| Type of \(u\) | Number when \(q\) is odd | Number when \(q\) is even | \(\operatorname{rank}P\) | Nilpotency index |
| --- | ---: | ---: | ---: | --- |
| \(u\in\operatorname{im}L\) | \(q^r\) | \(q^r\) | \(r\) | At most \(2\) |
| \(u\in\ker L\setminus\operatorname{im}L\) | \(q^{n-r}-q^r\) | \(q^{n-r}-q^r\) | \(r+1\) | \(2\) |
| \(u\notin\ker L\) | \(0\) | \(q^n-q^{n-r}\) | \(r+1\) | \(3\) |

The sole index-one operator is \(P=0\). Thus the total number of weight-zero Rota–Baxter operators equals
\[
\begin{cases}
\sum_{r=0}^{\lfloor n/2\rfloor}M_q(n,r)q^{n-r},&q\text{ odd},\\
q^n\sum_{r=0}^{\lfloor n/2\rfloor}M_q(n,r),&q\text{ even}.
\end{cases}
\]
For even \(q\), the exact number of nilpotency-index-three operators is
\[
\sum_{r=1}^{\lfloor n/2\rfloor}M_q(n,r)\bigl(q^n-q^{n-r}\bigr).
\]
In particular, when \(n=2\) and \(q\) is even, there are exactly \(q^4\) weight-zero operators, of which \((q^2-1)(q^2-q)\) have nilpotency index three; for odd \(q\), the total is \(q^3+q^2-q\), all of nilpotency index at most two.

## Assumptions and scope
Here multiplication is \((a+v)(b+w)=ab+aw+bv\) for scalars \(a,b\in K\) and vectors \(v,w\in V\). The weight-zero Rota–Baxter identity is
\[
P(x)P(y)=P\bigl(xP(y)+P(x)y\bigr)\qquad(x,y\in A).
\]
All classifications are for \(K\)-linear maps, all fields \(K\), and finite radical dimension \(n\ge1\). The counting and rank formulas additionally assume \(K=\mathbb F_q\) for a prime power \(q\). Nilpotency index means the least positive \(j\) with \(P^j=0\); it equals one only for the zero operator. These claims concern weight zero, not arbitrary nonzero weights or nonsplit local algebras.

## Proof
**1. Forced image in the square-zero radical.** Write \(P(1)=a+u\) with \(a\in K\), \(u\in V\). For \(v\in V\), uniquely write \(P(v)=f(v)+L(v)\), where \(f:V\to K\) and \(L:V\to V\) are linear. Apply the Rota–Baxter identity to \((v,v)\): the scalar coefficient of the left side is \(f(v)^2\), while the scalar coefficient of the right side is \(2f(v)^2\). Thus \(f(v)^2=0\) in the field \(K\), so \(f(v)=0\) for all \(v\in V\). Now the scalar coefficients at \((1,1)\) are \(a^2\) and \(2a^2\), respectively; hence \(a=0\). Therefore \(P(A)\subseteq V\), \(P(1)=u\), and \(P|_V=L\).

**2. Exact operator conditions.** At \((1,v)\), the left side is \(uL(v)=0\) and the right side is \(P(L(v))=L^2(v)\). Hence \(L^2=0\). At \((1,1)\), the left side is \(u^2=0\) and the right side is \(P(2u)=2L(u)\), so \(2L(u)=0\). Conversely, if these two conditions hold and \(P(a+v)=au+L(v)\), then \(P(A)\subseteq V\) gives \(P(x)P(y)=0\) for every \(x=a+v,y=b+w\), while
\[
P\bigl(xP(y)+P(x)y\bigr)=aP^2(y)+bP^2(x)=2abL(u)=0.
\]
This proves necessity and sufficiency in every characteristic. It also gives \(P^2(a+v)=aL(u)\) and \(P^3=0\); the latter is sharp precisely in characteristic two for \(n\ge2\). For example, take independent \(e_1,e_2\in V\), set \(L(e_2)=e_1\), \(L(e_1)=0\), and let \(u=e_2\), with \(L\) zero on any remaining basis vectors. Then \(L^2=0\) but \(P^2(1)=e_1\ne0\).

**3. Count the square-zero endomorphisms.** Fix \(r=\operatorname{rank}L\). From \(L^2=0\) follows \(U=\operatorname{im}L\subseteq W=\ker L\), so \(r\le n-r\). Choose an \(r\)-dimensional image \(U\) in \(\binom nr_q\) ways, an \((n-r)\)-dimensional kernel \(W\supseteq U\) in \(\binom{n-r}r_q\) ways, and an isomorphism \(V/W\overset\sim\longrightarrow U\) in \(\prod_{i=0}^{r-1}(q^r-q^i)\) ways. The resulting map is unique for these data; this proves the displayed \(M_q(n,r)\).

**4. Rank/index strata.** For a fixed \(L\), \(\operatorname{im}P=\operatorname{im}L+Ku\). Thus \(\operatorname{rank}P=r\) if \(u\in\operatorname{im}L\) and \(r+1\) otherwise. Since \(\operatorname{im}L\subseteq\ker L\), the three disjoint vector sets \(\operatorname{im}L\), \(\ker L\setminus\operatorname{im}L\), and \(V\setminus\ker L\) have cardinalities \(q^r\), \(q^{n-r}-q^r\), and \(q^n-q^{n-r}\). In odd characteristic, the identity \(2L(u)=0\) excludes the last set; in characteristic two it excludes none. Finally \(P^2(1)=L(u)\) and \(P^2(V)=0\). The displayed strata and totals follow by multiplication with \(M_q(n,r)\) and summation.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 and no external packages. The program checks the defining Rota–Baxter identity directly on every ordered pair of algebra basis elements for **every** linear operator in the following finite cases: radical dimension \(1\) over \(\mathbb F_2,\mathbb F_3\); dimension \(2\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\); and dimension \(3\) over \(\mathbb F_2\). It independently tests the structural classification and compares the observed operator-index distributions with the formulas. The outputs are, respectively: \((2;1,1,0)\), \((3;1,2,0)\), \((16;1,9,6)\), \((33;1,32,0)\), \((256;1,75,180)\), and \((176;1,91,84)\), where each tuple is total count followed by index-one, index-two and index-three counts. The program finishes with \(\texttt{VERIFY_OK}\). Its exhaustive checks are finite evidence only; the proof above handles all field sizes and dimensions.

## Relationship to prior work
Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras* (arXiv:2605.15670v1, publicly available May 15, 2026), classifies the same square-zero local algebra in **characteristic zero**; Theorem 3.4 requires \(P^2=0\), or equivalently \(L(u)=0\). The present result recovers that classification for characteristic different from two but identifies a genuinely different, larger characteristic-two family, determines its sharp nilpotency index, and counts every finite-field rank/index stratum. Gubarev's *Rota–Baxter Operators on Unital Algebras* establishes general nilpotency results under the characteristic-zero hypothesis, not the characteristic-two classification. Existing small-algebra classifications, including the four-dimensional exterior algebra over \(\mathbb F_2\), concern different multiplications; an exterior radical has nonzero square and does not automatically imply the present formulas. No claim of universal priority or independent validation is made.

## Limitations
This treats split radical-square-zero unital algebras and weight-zero \(K\)-linear Rota–Baxter operators only. The finite-field enumerations are exact because of the proof, not because large cases were exhaustively tested. Results for general local algebras with nonzero radical square, arbitrary nonzero weight, or nonassociative structures are not asserted. A logically equivalent treatment under other terminology in earlier literature remains a possible originality risk.

## References
1. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (May 15, 2026), especially Theorem 3.4 and its hypotheses. https://arxiv.org/abs/2605.15670 . Accessible public full-text transcription: https://www.researchgate.net/publication/404963487_Rota_Baxter_Operators_on_Truncated_Polynomial_Algebras .
2. V. Gubarev, *Rota–Baxter Operators on Unital Algebras*, Moscow Mathematical Journal 21 (2021), 325–364. https://www.mathjournals.org/mmj/2021-021-002/2021-021-002-004.html .
3. S. Zheng, L. Guo and M. Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, Communications in Algebra 47 (2019), 3094–3116. https://doi.org/10.1080/00927872.2018.1552278 .
