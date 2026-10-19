# Complete two-step transvection conjugacy-class distribution over finite fields

## Finding
Let \(q\) be any prime power and \(n\ge2\). Write \(G=\mathrm{GL}_n(\mathbb F_q)\), and let \(\mathcal T\) be its conjugacy class of nonidentity transvections: matrices \(I+ab^{\mathsf T}\) where \(a,b\ne0\) and \(b^{\mathsf T}a=0\). Set
\[
H=|\mathcal T|=\frac{(q^n-1)(q^{n-1}-1)}{q-1},\qquad L=\frac{q^{n-1}-1}{q-1}.
\]
The following table is the **complete distribution of conjugacy classes of ordered products** \(T_1T_2\) with \((T_1,T_2)\in\mathcal T^2\). The middle column counts possible second factors for any fixed first factor. Multiply that column by \(H\) to get the number of ordered pairs in the stated conjugacy class.

| Product similarity type | Number of second factors for a fixed first factor |
| --- | ---: |
| \(I_n\) | \(1\) |
| \(J_2(1)\oplus I_{n-2}\) | \(2q^{n-1}-q-2\) |
| \(J_3(1)\oplus I_{n-3}\) | \(2(q^{2n-3}-q^{n-1})\) |
| \(J_2(1)\oplus J_2(1)\oplus I_{n-4}\) | \((L-1)(q^{n-2}-q)\) |
| \(C_c\oplus I_{n-2}\), one class for each \(c\in\mathbb F_q^\times\) | \(q^{2n-3}\) for each \(c\) |

Here \(J_k(1)\) is a unipotent Jordan block of length \(k\); rows demanding negative identity-block dimension are omitted (their displayed counts are zero). The \(2\)-by-\(2\) matrix \(C_c=\begin{pmatrix}0&-1\\1&2+c\end{pmatrix}\) has polynomial \(X^2-(2+c)X+1\) and no eigenvalue \(1\). These \(q-1\) classes are pairwise distinct and distinct from the unipotent classes, including in characteristic two. All unspecified conjugacy classes have count zero. Thus the entire two-step random walk on \(G\), started at identity and driven by uniformly sampled transvections, has class masses given by the middle column divided by \(H\). Within each class, the walk is uniform by conjugation invariance.

## Assumptions and scope
The field is the full finite field \(\mathbb F_q\), of arbitrary prime characteristic; both factors are **nonidentity** transvections, sampled independently if probabilities are used. Products are ordered and taken in the natural defining \(n\)-dimensional representation. All displayed counts are integers; no assumption of diagonalizability, distinct eigenvalues or odd characteristic is required.

## Proof
Every transvection \(I+a\alpha\), with \(\alpha(a)=0\), is conjugate to \(I+e_1e_2^{\mathsf T}\). Fix this first factor. A second transvection has the unique presentation \(I+b\beta\) once the nonzero vector \(b\) is chosen as a representative of its projective image line; \(\beta(b)=0\) and \(\beta\ne0\). Let \(s=\alpha(b)\), \(t=\beta(a)\), and \(c=st\). Then
\[
M=(I+a\alpha)(I+b\beta)=I+a\alpha+b\beta+s a\beta.
\]
Its fixed subspace contains \(\ker\alpha\cap\ker\beta\), so at most two nontrivial characteristic roots occur. On \(\operatorname{span}(a,b)\), when \(c\ne0\), the matrix of \(M-I\) in the basis \((a,b)\) is \(\begin{pmatrix}c&s\\t&0\end{pmatrix}\). It is invertible. Therefore \(M\) is similar to \(C_c\oplus I_{n-2}\), with the asserted polynomial; for \(c\ne0\) no unipotent specialization can arise. There are exactly \(q^{n-1}\) image lines \([b]\) outside \(\ker\alpha\); for each and each prescribed nonzero \(c\), the independent conditions \(\beta(b)=0\) and \(\beta(a)=c/s\) leave \(q^{n-2}\) choices. This proves the \(q^{2n-3}\) count for each nonzero \(c\).

Suppose \(c=0\), and put \(X=a\alpha\), \(Y=b\beta\), \(N=M-I=X+Y+XY\). The relations \(X^2=Y^2=0\) and \(XYX=cX=YXY= cY=0\) give \(N^2=XY+YX\) and \(N^3=0\). If exactly one of \(s,t\) is nonzero, then \(\operatorname{rank}N^2=1\), and since \(\operatorname{rank}N\le2\), the Jordan type is precisely one length-three block. The number of choices with \(s=0,t\ne0\) is
\[
(L-1)(q-1)q^{n-2}=q^{2n-3}-q^{n-1}.
\]
Indeed, the image line \([b]\) lies in \(\ker\alpha\) but is not \([a]\); after choosing it, \(\beta(b)=0\) and \(\beta(a)\ne0\) give \((q-1)q^{n-2}\) choices. Symmetrically, \(t=0,s\ne0\) has \(q^{n-1}(q^{n-2}-1)=q^{2n-3}-q^{n-1}\) choices: the line \([b]\) lies outside \(\ker\alpha\), while \(\beta\ne0\) annihilates both independent vectors \(a,b\). Summing gives the third table row.

Finally, when \(s=t=0\), we have \(XY=YX=0\) and \(N=X+Y\) is square-zero. If \([b]=[a]\), there are \(q^{n-1}-1\) nonzero forms \(\beta\) annihilating \(a\); exactly one yields \(Y=-X\), so \(M=I\), and the other \(q^{n-1}-2\) yield a rank-one square-zero \(N\). For each of the \(L-1\) lines \([b]\ne[a]\) contained in \(\ker\alpha\), the nonzero forms annihilating both \(a\) and \(b\) number \(q^{n-2}-1\). Exactly \(q-1\) of these are nonzero multiples of \(\alpha\), yielding \(\operatorname{rank}N=1\); the other \(q^{n-2}-q\) are independent of \(\alpha\), yielding \(\operatorname{rank}N=2\). The two remaining table rows follow. Every second transvection belongs to exactly one of the counted cases. Since all first factors are conjugate, multiply by \(H\) to count ordered pairs, and divide by \(H\) to obtain two-step class probabilities.

## Verification
A standalone pure-Python program `transvection_checker.py` enumerates actual nonzero rank-one square-zero matrices and their products for nine prime-field dimension combinations. For \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\), it enumerates **every ordered pair** and checks the table by similarity invariants; for \((3,5),(4,3),(5,2)\), it exhausts every second factor against a fixed first factor. Every case passed. For \(n=4,q=2\), \(H=105\) and the fixed-first-factor counts are \(1,12,48,12,32\) for identity, a length-two block, a length-three block, two length-two blocks, and the unique nonzero \(c\), respectively. All integers sum to \(105\). The checker independently computes matrix products and ranks of \(M-I\) and its square; finite tests corroborate but do not replace the proof for all \(n,q\).

## Relationship to prior work
Diaconis, Ram and Simper establish the conjugacy-invariant random-transvection walk on finite general linear groups, its total transvection count and its Borel-double-coset projection (2022 preprint; 2023 journal). Their examined transvection sections and Hecke formulas concern projected walks, not the explicit two-step **full conjugacy-class** law above. Phadke (1974) studies minimal-length transvection factorizations; the accessible abstract does not resolve these finite-field class multiplicities. Classical finite-group character convolution gives general implicit formulas for conjugacy-class products, whereas this statement is a direct closed-form class law resolving the small-rank unipotent and nonunipotent strata uniformly.

## Limitations
The result concerns exactly two factors. It does not give arbitrary-length class convolution, mixing times, or independent verification of mathematical priority. No claim is made that the general transvection-walk or factorization framework is new. Some earlier finite-group class-algebra formula or inaccessible older product-of-transvections paper may imply equivalent coefficients; this remains a priority risk.

## References
1. P. Diaconis, A. Ram, M. Simper, *Double Coset Markov Chains*, arXiv:2208.10699v1, first publicly posted 2022-08-23; *Forum of Mathematics, Sigma* **11** (2023), e2, DOI: 10.1017/fms.2022.106, Sections 1, 2.4, 3, 5.3.
2. B. B. Phadke, *Products of Transvections*, *Canadian Journal of Mathematics* **26** (1974), 1412–1417, DOI: 10.4153/CJM-1974-135-0 (abstract and bibliographic material consulted; full article not assessed).
