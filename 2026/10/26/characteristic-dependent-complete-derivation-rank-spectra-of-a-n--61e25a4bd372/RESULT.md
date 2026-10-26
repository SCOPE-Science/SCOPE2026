# Characteristic-dependent complete derivation-rank spectra of a nilpotent evolution-algebra family

## Finding

For every field \(k\), integer \(m\ge2\), and commutative, associative evolution algebra \(E_m(k)\) with basis \(e_1,\ldots,e_m,z\) and multiplication \(e_i^2=z\), \(e_i e_j=0\) for distinct \(i,j\), and \(zE_m=0\), its ordinary derivations have the exact normal form
\[
D=\begin{pmatrix}A&0\\ \ell&c\end{pmatrix},\qquad A^T+A=cI_m,\quad \ell\in k^{1\times m}.
\]
Consequently, in odd characteristic the derivation space has dimension \(1+m(m+1)/2\) and includes invertible derivations, while in characteristic two it has dimension \(m(m+3)/2\) and every derivation is singular. This is a jump of \(m-1\) dimensions together with the disappearance of the full-rank stratum.

For every finite field \(\mathbb F_q\) of **even** order, the number \(C_j(m,q)\) of derivations of rank exactly \(j\), for \(0\le j\le m\), is
\[
C_j(m,q)=N_j(m,q)q^j+\mathbf 1_{j\ge1}N_{j-1}(m,q)\bigl(q^m-q^{j-1}\bigr),
\quad N_r(m,q)={m\brack r}_q\,\beta_r(q),
\]
with \(C_{m+1}(m,q)=0\), Gaussian binomial \({m\brack r}_q=\prod_{i=0}^{r-1}(q^{m-i}-1)/(q^{r-i}-1)\), and
\[
\beta_0=1,\quad \beta_1=q-1,\quad
\beta_r=(q-1)q^{r-1}\beta_{r-1}+(q^{r-1}-1)q^{r-1}\beta_{r-2}\quad(r\ge2).
\]
Equivalently, \(\beta_{2s}=q^{s(s+1)}\prod_{i=1}^{s}(q^{2i-1}-1)\) and \(\beta_{2s+1}=q^{s(s+1)}\prod_{i=1}^{s+1}(q^{2i-1}-1)\). These counts sum to \(q^{m(m+3)/2}\).

For \(m=3\) and every **odd** prime power \(q\), the complete rank vector \((C_0,C_1,C_2,C_3,C_4)\) is
\[
\left(1,\ q^3-1,\ q^2(q^3-1),\ (q^3-1)(q^3-q^2)+(q-1)q^3(q^2+q),\ (q-1)q^3(q^3-q^2-q)\right).
\]
For \(m=3\) and even \(q\), it specializes to
\[
\left(1,\ (q+1)(q^3-1),\ (q^3-1)(q^4+q^3-q),\ q^4(q^2-1)(q^3-1),\ 0\right).
\]

## Assumptions and scope

A derivation is a \(k\)-linear endomorphism satisfying \(D(xy)=D(x)y+xD(y)\) for all \(x,y\). Rank always means rank as a \(k\)-linear map on the entire \((m+1)\)-dimensional algebra; individual operators are counted, not equivalence classes. \(E_m^2=kz\) and \(\operatorname{Ann}(E_m)=kz\). The family has nilpotency index three because \(E_m^2=kz\ne0\) and \(E_m^3=E_m^2E_m=0\). It is **commutative and associative**, since every product lies in the annihilator \(kz\); it is simultaneously an evolution algebra. It is defined in every characteristic. Formulae stated for odd \(q\) require \(q\) a prime power, not just a prime.

## Proof

**1. Complete normal form.** Because the square ideal is characteristic under derivations, \(D(z)=cz\). Write \(D(v)=Av+\ell(v)z\) for \(v\in V=k^m\). Products satisfy \(vw=(v^Tw)z\); the Leibniz identity becomes \(c(v^Tw)=v^T(A^T+A)w\) for all \(v,w\in V\). Therefore \(A^T+A=cI_m\), and conversely every such triple \((A,\ell,c)\) satisfies all products, establishing completeness. In odd characteristic, \(A=(c/2)I_m+S\) with \(S^T=-S\), giving \(1+\binom m2+m=1+m(m+1)/2\) parameters. For \(c=2\) and \(A=I_m\), \(\ell=0\), the derivation is invertible. In characteristic two, the diagonal of \(A^T+A\) vanishes, whence \(c=0\), and \(A\) is arbitrary symmetric; this gives \(\binom{m+1}{2}+m=m(m+3)/2\) parameters. Since \(D(z)=0\), no such derivation is invertible.

**2. Symmetric-matrix ranks in characteristic two.** Set \(\beta_r(q)\) to be the number of nonsingular symmetric \(r\times r\) matrices. For \(r\ge2\), split by the first diagonal entry \(a\). If \(a\ne0\), the Schur complement on the remaining \(r-1\) coordinates is arbitrary nonsingular, and the other first-row entries are free; this gives \((q-1)q^{r-1}\beta_{r-1}\). If \(a=0\), nonsingularity requires the remaining first row \(v\ne0\). After a change of basis of the remaining coordinates moving \(v\) to a coordinate functional, expanding on the hyperbolic two-space shows that a complementary \((r-2)\)-block must be nonsingular, whereas \(r-1\) coefficients are free. This yields \((q^{r-1}-1)q^{r-1}\beta_{r-2}\). Thus the stated recurrence holds, and its products follow by induction. The radical of any symmetric matrix \(A\) of rank \(r\) is a unique \((m-r)\)-subspace. Conversely choosing a radical and a nonsingular symmetric form on its quotient gives a unique form of rank \(r\); hence \(N_r={m\brack r}_q\beta_r\). (The argument counts symmetric bilinear forms, including nonalternating forms; it does not silently replace them by quadratic forms.)

**3. Appending the central row.** For \(c=0\), \(D\) has block rows \((A,0)\), \((\ell,0)\). If \(A\) has rank \(r\), precisely \(q^r\) of the \(q^m\) choices of \(\ell\) lie in the row span of \(A\), so they preserve the rank; all others increase it by one. Summing over symmetric \(A\) proves \(C_j\). The total counts all \(q^{m(m+3)/2}\) symmetric matrices and appended rows.

**4. The first odd-characteristic rank spectrum.** For \(m=3\), put \(A=tI_3+S\) with
\[
S=\begin{pmatrix}0&a&b\\-a&0&c\\-b&-c&0\end{pmatrix},
\quad D(z)=2tz,\quad\det(A)=t(t^2+a^2+b^2+c^2).
\]
For \(t=0\), the zero \(S\) contributes one rank-zero operator and \(q^3-1\) rank-one operators as \(\ell\) varies. Every nonzero \(S\) is rank two (a skew \(3\times3\) matrix in odd characteristic); among its \(q^3\) appended rows, \(q^2\) yield rank two and \(q^3-q^2\) yield rank three. For \(t\ne0\), the determinant vanishes precisely at the \(q^2+q\) triples satisfying \(a^2+b^2+c^2=-t^2\). Indeed, writing \(\chi\) for the quadratic character with \(\chi(0)=0\), the count of \(c\) for fixed \(a,b\) is \(1+\chi(s-a^2-b^2)\). For any \(u\ne0\), \(\sum_b\chi(u-b^2)=-\chi(-1)\), while for \(u=0\) the sum is \((q-1)\chi(-1)\); these identities follow by counting the solutions of \(v^2+b^2=u\) after a quadratic twist, or by the factorization \((v-b)(v+b)=u\). Thus for \(s\ne0\) the double sum equals \(q\chi(-s)\), whence \(\#\{(a,b,c):a^2+b^2+c^2=s\}=q^2+q\chi(-s)\). For \(s=-t^2\), this gives \(q^2+q\). In this determinant-zero case, \(A\) has rank exactly two, since \(A+A^T=2tI_3\) has rank three, forcing \(\operatorname{rank}A\ge2\). Thus \(D\) has rank three, as its center column is \(2tz\ne0\). Otherwise \(A\) and \(D\) are invertible, independently of \(\ell\). Counting the \(q-1\) choices of \(t\) and all \(q^3\) choices of \(\ell\) gives the odd-characteristic vector. Substitution of the symmetric-matrix formula in the even case gives the second vector.

## Verification

The standalone script `verify.py` enumerates all \(512\), \(2187\), and \(78125\) operators in the asserted normal form over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), checks every Leibniz relation independently, and compares complete rank histograms with the above expressions. Separately, it computes the unrestricted derivation-equation linear-system dimensions, yielding \(9\), \(7\), \(7\), respectively. It also exhaustively enumerates every symmetric \(3\times3\) matrix over \(\mathbb F_4\) and every symmetric \(4\times4\) matrix over \(\mathbb F_2\), computing matrix ranks with explicit extension-field arithmetic or binary elimination and comparing \(N_r\) and derived \(C_j\) with the general formula. Its required final line is `EVOLUTION_DERIVATION_RANKS_OK`; the final two additional checks print `PASS` independently. These finite tests corroborate but are not substitutes for the proofs for arbitrary fields and dimensions.

## Relationship to prior work

Hegazi and Abdelwahab [1] classify low-dimensional nilpotent evolution algebras, including the four-dimensional example with precisely these products at \(m=3\). Elduque and Labra [2] explain the bilinear-form construction for nilpotent evolution algebras. Camacho et al. [3] derive general equations for derivations of certain evolution-algebra families, with different structure-matrix hypotheses. The broader derivation classification of Cabrera et al. [4] provides closely related structural context; full text could not be verified here, so an indirect implication for these exact rank distributions remains a publication-priority risk. None of the inspected full texts [1]–[3] states the complete characteristic-two finite-field rank spectrum for all \(m\) nor the odd-characteristic \(m=3\) rank vector. The rank distributions here are derived anew, not inferred solely from uninspected summaries. Martín Barquero, Martín González, and Sánchez-Ortega [5] classify commutative one-dimensional-square algebras, explicitly including the associative nilpotent class containing this family, but the inspected full text does not give derivation-rank multiplicities. Standard finite-field bilinear-form counts are used transparently in the proof and do not by themselves identify the derivations of this algebra.

## Limitations

The result describes this explicitly defined nondegenerate one-dimensional-square family, not all nilpotent evolution algebras or arbitrary bilinear forms. In odd characteristic a closed full-rank distribution is supplied only when \(m=3\); an arbitrary-dimension odd-characteristic rank distribution is not asserted. The proof does not classify derivations up to conjugacy or assert that the counting formula was previously unknown in every publication. A relevant general derivation-classification article [4] was not inspected in full; independent validation and exhaustive publication-priority certification have not been performed.

## References

[1] A. S. Hegazi and H. Abdelwahab, *Nilpotent evolution algebras over arbitrary fields*, arXiv:1508.06860v1, posted 2015-08-27, especially the displayed four-dimensional algebra with three squares equal to the final basis vector. https://arxiv.org/abs/1508.06860

[2] A. Elduque and A. Labra, *On nilpotent evolution algebras*, arXiv:1602.01590v1, posted 2016-02-04. https://arxiv.org/abs/1602.01590

[3] L. M. Camacho et al., *The derivations of some evolution algebras*, arXiv:1004.1936, 2010. https://arxiv.org/abs/1004.1936

[4] Y. Cabrera et al., *On the characterization of the space of derivations in evolution algebras*, arXiv:1912.06925, 2019 (full text not inspected here). https://arxiv.org/abs/1912.06925

[5] D. Martín Barquero, C. Martín González, and J. Sánchez-Ortega, *Commutative Algebras with One-Dimensional Square*, Mediterranean J. Math. 22, 48 (2025), open access. https://doi.org/10.1007/s00009-025-02812-7
