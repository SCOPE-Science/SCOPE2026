# Nilpotency-depth distribution and sharp terminal strata in finite-field Munn algebras

## Finding

Let \(q\) be any prime power and let \(m,n\geq 1\). Give \(M_{m,n}(\mathbb F_q)\) the associative, generally nonunital, Munn product \(X\star Y=XPY\), where \(P\in M_{n,m}(\mathbb F_q)\) has rank \(1\leq r\leq\min(m,n)\). Put \(b=n-r\) and \(c=m-r\). Let \(F_j\) count elements with \(X^{\star j}=0\); the zero element has nilpotency index one.

For a partition \(\lambda\vdash r\), let \(m_s(\lambda)\) be the multiplicity of the part \(s\), let \(\lambda'\) be its conjugate, and define the integer
\[
O_\lambda(q)=\frac{|\mathrm{GL}_r(\mathbb F_q)|}{q^{\sum_i(\lambda'_i)^2}\prod_{s\geq1}\prod_{h=1}^{m_s(\lambda)}(1-q^{-h})}.
\]
This is the size of the ordinary nilpotent similarity class of Jordan type \(\lambda\). For integers \(e,b,t\geq0\), define
\[
R_{e,b,t}(q)={e\brack t}_q\prod_{i=0}^{t-1}(q^b-q^i),
\]
taking empty products to equal one and \({e\brack t}_q=0\) for \(t>e\). It counts the \(e\)-by-\(b\) matrices of rank \(t\). Set \(F_1=1\). For **every** \(2\leq j\leq r+2\), the complete cumulative nilpotency-depth distribution is
\[
\boxed{F_j=q^{bc}\sum_{\substack{\lambda\vdash r\\\lambda_1\leq j}}
 O_\lambda(q)\,q^{(r-a-e)b}
 \sum_{t=0}^{\min(e,b)}R_{e,b,t}(q)q^{c(r-a-t)},\quad
 a=m_j(\lambda),\ e=m_{j-1}(\lambda).}
\]
Thus exactly \(F_j-F_{j-1}\) elements have nilpotency index \(j\), for all possible indices. The entire nilpotent locus has
\[
\boxed{F_{r+2}=q^{mn-r}}.
\]
Its reduced geometric variety is irreducible of dimension \(mn-r\) over an algebraic closure, for every characteristic. When \(r=0\), excluded from the displayed partition formula, the product is identically zero: \(F_1=1\) and \(F_j=q^{mn}\) for \(j\geq2\).

The largest nilpotency index attained is \(r+2\) if \(b,c>0\), \(r+1\) if exactly one of \(b,c\) is positive, and \(r\) if \(b=c=0\). Every index from one through that maximum occurs. Writing \(O_{(r)}(q)=|\mathrm{GL}_r(\mathbb F_q)|/[q^{r-1}(q-1)]\), the number of elements with maximal index is respectively
\[
\boxed{\begin{cases}
O_{(r)}(q)q^{(r-1)(b+c)+bc}(q^b-1)(q^c-1),&b,c>0,\\
O_{(r)}(q)q^{(r-1)b}(q^b-1),&b>0,\ c=0,\\
O_{(r)}(q)q^{(r-1)c}(q^c-1),&b=0,\ c>0,\\
O_{(r)}(q),&b=c=0.
\end{cases}}
\]
These formulas depend only on the three dimensions and the rank of \(P\), not on its other entries. Transposition exchanges \(b\) and \(c\), as the formulas necessarily permit.

## Assumptions and scope

The coefficient field is an arbitrary finite field; no restriction on characteristic or on algebra unitality is made. Sandwich-matrix rank is at least one in the main formula. The algebra dimension is \(mn=(r+c)(r+b)\), and matrix powers are taken with the sandwich multiplication, not ordinary rectangular matrix multiplication. The term "nilpotent locus" refers to the set of nilpotent elements and to its **reduced** algebraic variety; no claim about a nonreduced power-equation scheme is made. The all-zero sandwich matrix is addressed separately.

## Proof

**1. Normal form and exact powers.** Invertible row and column changes on \(P\) induce an algebra isomorphism and reduce it to the matrix with an \(r\)-by-\(r\) identity block and zero elsewhere. Write each element uniquely as
\[
X=\begin{pmatrix}A&B\\ C&D\end{pmatrix},\quad
A\in M_r(k),\ B\in M_{r,b}(k),\ C\in M_{c,r}(k),\ D\in M_{c,b}(k).
\]
An induction from \(X\star Y=XPY\) yields, for each \(j\geq2\),
\[
X^{\star j}=\begin{pmatrix}
A^j&A^{j-1}B\\ CA^{j-1}&CA^{j-2}B
\end{pmatrix}.
\]
Hence \(X\) is nilpotent if and only if \(A\) is an ordinary nilpotent matrix. If \(A^r=0\), then \(X^{\star(r+2)}=0\). The block \(D\) occurs in no power of exponent at least two and is free in every count \(F_j\) with \(j\geq2\).

**2. A fixed Jordan type.** Fix \(j\geq2\), and suppose \(A^j=0\) has Jordan type \(\lambda\) with every part at most \(j\). Put \(a=m_j(\lambda)\) and \(e=m_{j-1}(\lambda)\). The subspace \(H=\operatorname{im}A^{j-1}\) has dimension \(a\), and \(W=\ker A^{j-1}\) has dimension \(r-a\). The conditions \(A^{j-1}B=0\) and \(CA^{j-1}=0\) say that the columns of \(B\) lie in \(W\) and \(C\) annihilates \(H\), respectively. On the quotient by \(H\), the map
\[
T:W\longrightarrow k^r/H,\qquad v\longmapsto A^{j-2}v+H
\]
has rank **exactly** \(e\): on a Jordan block of length \(j-1\) it contributes one rank, on a length-\(j\) block its image belongs to \(H\), and on a shorter block it is zero. Consequently \(T\circ B\) has rank \(t\) for exactly \(q^{(r-a-e)b}R_{e,b,t}(q)\) choices of \(B\), with \(0\leq t\leq\min(e,b)\).

For any such \(B\), the final equation \(CA^{j-2}B=0\), together with \(C(H)=0\), requires \(C\) to annihilate an \((a+t)\)-dimensional subspace. Exactly \(q^{c(r-a-t)}\) matrices \(C\) do so. Independently \(D\) has \(q^{bc}\) choices. Multiplying these factors and summing over \(t\) gives the inner sum in the asserted formula.

**3. Exact similarity-class factor.** The stabilizer of a nilpotent Jordan matrix with partition \(\lambda\) inside \(\mathrm{GL}_r(k)\) is the unit group of its endomorphism algebra as a \(k[t]\)-module. That endomorphism algebra has vector-space dimension \(\sum_i(\lambda'_i)^2\); its semisimple quotient has factors \(M_{m_s(\lambda)}(k)\). The resulting unit count is
\[
q^{\sum_i(\lambda'_i)^2}\prod_{s\geq1}\prod_{h=1}^{m_s(\lambda)}(1-q^{-h}),
\]
so orbit–stabilizer gives \(O_\lambda(q)\). Summing step 2 over every allowed Jordan type proves the cumulative formula. No assumption about the characteristic was used.

**4. Total locus and geometry.** Projection \(X\mapsto A\) identifies the **reduced** nilpotent locus with the ordinary nilpotent cone in \(M_r\), times an affine space of dimension \(rb+rc+bc\). The ordinary nilpotent cone is the closure of the regular nilpotent similarity orbit over an algebraically closed field and has dimension \(r^2-r\); hence the reduced locus is irreducible of dimension \(r^2-r+rb+rc+bc=mn-r\). Over \(\mathbb F_q\), the classical nilpotent-matrix count \(q^{r^2-r}\) yields the exact total \(q^{mn-r}\); it also follows by setting \(j=r+2\) in the partition sum.

**5. Sharp upper index and multiplicity.** If both \(b,c>0\), the only possible nonzero \(X^{\star(r+1)}\) has bottom-right block \(CA^{r-1}B\). This is nonzero only if \(A\) is regular nilpotent (one block of size \(r\)). For such \(A\), write \(A^{r-1}=uv^T\) with \(u,v\ne0\). Then \(CA^{r-1}B=(Cu)(v^TB)\) is nonzero if and only if both vector factors are nonzero. There are \(q^{(r-1)c}(q^c-1)\) choices of \(C\) and \(q^{(r-1)b}(q^b-1)\) choices of \(B\); \(D\) is free. Multiplication by the regular orbit size proves the first terminal formula. If precisely one of \(B,C\) can appear, the same argument tests \(X^{\star r}\) and yields the second and third formulas. With neither present one obtains the ordinary regular-nilpotent matrix count. The displayed multiplicities are positive, so the maximal cutoffs are attained. Every smaller possible index occurs using a Jordan block of the required length in \(A\), or a shorter block with a nonzero terminal \(B\) or \(C\); this includes the \(r=1\) boundaries.

## Verification

The standalone `verify_nilpotency.py` uses literal finite-field matrix coordinates and constructs the sandwich product independently of the partition count. For each tested parameter quadruple it computes powers until vanishing, bins their exact nilpotency indices, evaluates the partition/orbit formula independently, and compares every cumulative count and the claimed maximum-depth multiplicity. The script uses no external Python dependencies, and includes \(\mathbb F_4\) arithmetic, not merely prime fields.

Executed checks covered 18 parameter sets, including \((r,b,c,q)=(2,1,1,2)\) with exact depth counts \((1,43,60,24)\), \((2,1,1,3)\) with \((1,314,1008,864)\), and \((1,1,1,4)\) with \((1,27,36)\). The verification marker was `VERIFY_OK_MUNN_NILPOTENCY_DEPTHS`. Finite verification does not replace the proof for unbounded dimensions and all finite fields.

## Relationship to prior work

Rees matrix semigroups and their semigroup algebras supplied the original sandwich construction. Drozd and Plakosh (2022, §1) identify normal forms for regular Munn algebras and classify representation types, not distributions of nilpotency indices of their individual elements. Yu, Luo and Li (2024, §§1–3, full accessible text) investigate generation by idempotents and commutators and zero-product-determined properties; they do not formulate a nilpotency-depth census. The established Jordan similarity-class formula and classical total count of nilpotent matrices are explicitly used as prior inputs. The result here is the **complete all-parameter finite-field nilpotency-index distribution**, its sharp cutoff strata, and the geometric nilpotent-locus statement. This does not assert novelty for the normal form, orbit enumeration, or ordinary nilpotent-matrix count alone.

## Limitations

The proof assumes the base is a finite field and the sandwich matrix has scalar entries. It does not count nilpotent elements over arbitrary coefficient rings, classify their similarity classes under the unitization, or establish the scheme-theoretic reducedness of the equations \(X^{\star j}=0\). The reduced total nilpotent locus is not the same as the potentially nonreduced zero-power scheme. The published-priority comparison includes fully accessible same-object papers, but older terminology and unavailable print monographs remain a possible source of earlier equivalent enumerations. No independent mathematical validation is claimed.

## References

1. D. Rees, *On semi-groups*, Mathematical Proceedings of the Cambridge Philosophical Society 36 (1940), 387–400, doi:10.1017/S0305004100017436. Historical construction.
2. R. Gray and N. Ruškuc, *Generating Sets of Completely 0-Simple Semigroups*, Communications in Algebra 33 (2005), 4657–4678; publisher online posting verified 1 February 2007, doi:10.1080/00927870500276676. Context for Rees matrices; not a nilpotency census.
3. Yu. A. Drozd and A. I. Plakosh, *Representations of Munn algebras and related semigroups*, arXiv:2202.06103 (first posted 12 February 2022), §§1–3. Full HTML examined for normal-form and representation-type scope.
4. B. Yu, K. Luo and J. Li, *Zero product and zero Jordan product determined Munn algebras*, arXiv:2407.00892 (first posted 1 July 2024), §§1–3. Full HTML examined for same-algebra properties.
5. The classical nilpotent-matrix centralizer and total-count results (Jordan normal form, orbit–stabilizer and the Fine–Herstein count) are invoked as standard prior inputs, not new claims.
