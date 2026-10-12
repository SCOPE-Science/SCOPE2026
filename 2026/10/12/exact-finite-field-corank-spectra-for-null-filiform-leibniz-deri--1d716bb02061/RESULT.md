# Exact finite-field corank spectra for null-filiform Leibniz derivations

## Finding
Let \(q=p^e\) be any prime power and \(n\ge2\). Every derivation of the null-filiform right Leibniz algebra defined below belongs to an explicitly counted nullity stratum. Write \(N_{n,q}(v)\) for the number of derivations whose kernel dimension is \(v\), and set \(z=\lfloor n/p\rfloor\). The exact answer is \(N_{n,q}(v)=B(v)+C(v)\), with
\[
B(v)=\begin{cases}(q-1)q^{n-v-1},&1\le v<n,\\1,&v=n,\\0,&\text{otherwise},\end{cases}
\]
and
\[
C(v)=\begin{cases}(q-1)q^{n-1},&z=0,\ v=0,\\
(q-1)^2q^{n-v-1},&z\ge1,\ 1\le v<z,\\
(q-1)q^{n-z},&z\ge1,\ v=z,\\
0,&\text{otherwise}.\end{cases}
\]
The two summands count derivations whose generating-vector coefficient \(a_1\) is respectively zero and nonzero. Both formulas are valid when \(q\) is a nonprime finite field. In particular, the full distribution has total mass \(q^n\), and invertible derivations exist if and only if \(n<p\).

There is also an individual test when \(a_1\ne0\). For \(1\le h<n\), put \(f_h=a_{h+1}/a_1\). If \(z=0\), the derivation is invertible. Otherwise its nullity is
\[
\min\left(\{h\in\{1,\ldots,z-1\}:f_h^p\ne f_{ph}\}\cup\{z\}\right).
\]
Thus modular Frobenius-resonance equations determine the entire positive-leading-coefficient distribution.

## Assumptions and scope
The algebra \(L_n(q)\) is an \(n\)-dimensional vector space over \(\mathbb F_q\) with basis \(e_1,\ldots,e_n\). Its only nonzero products of basis elements are
\[
[e_j,e_1]=e_{j+1}\qquad (1\le j<n).
\]
The convention is *right* Leibniz: \([x,[y,z]]=[[x,y],z]-[[x,z],y]\). A derivation is an \(\mathbb F_q\)-linear map \(D\) satisfying \(D([x,y])=[D(x),y]+[x,D(y)]\). The results count maps, not conjugacy classes, and specify kernel dimensions on the whole underlying \(n\)-space. They assert nothing about other Leibniz multiplication tables or infinite fields.

## Proof
**Derivation normal form.** Write \(D(e_1)=\sum_{r=1}^{n}a_r e_r\). Set \(S(e_j)=e_{j+1}\) for \(j<n\), and \(S(e_n)=0\). Every product is \([x,y]=y_1S(x)\), where \(y_1\) is the coefficient of \(e_1\). The derivation rule applied to \(e_{j+1}=[e_j,e_1]\) gives \(D(e_{j+1})=S D(e_j)+a_1 e_{j+1}\). Induction gives, with the integer \(j\) interpreted in \(\mathbb F_q\),
\[
D_{\mathbf a}(e_j)=j a_1e_j+\sum_{r=2}^{n-j+1}a_r e_{j+r-1}.
\]
Conversely, these formulas satisfy the derivation rule on every pair: when the right argument is \(e_j\) with \(j\ge2\), its image has zero \(e_1\)-coefficient, so both sides vanish; when it is \(e_1\), the displayed recursion applies, including at the terminal basis vector. Thus \(\mathbf a\mapsto D_{\mathbf a}\) is a bijection \(\mathbb F_q^n\to\operatorname{Der}(L_n(q))\).

**Zero leading coefficient.** Suppose \(a_1=0\) and the first nonzero coefficient is \(a_r\), for \(2\le r\le n\). The images of \(e_1,\ldots,e_{n-r+1}\) have distinct leading basis positions \(e_r,\ldots,e_n\), while all remaining images vanish. Therefore \(\operatorname{rank}D=n-r+1\) and \(\dim\ker D=r-1\). There are \((q-1)q^{n-r}\) such choices. The all-zero parameter vector contributes the unique nullity-\(n\) map. This gives \(B(v)\).

**Reduction when \(a_1\ne0\).** Scale the linear map by \(a_1^{-1}\), which preserves kernel dimension. Relative to the invariant subspace \(W=\operatorname{span}(e_2,\ldots,e_n)\), the quotient map on \(L_n(q)/W\) is multiplication by the nonzero scalar \(a_1\); hence the whole kernel dimension equals that of the restriction to \(W\). Identify \(e_j\leftrightarrow t^j\) on \(W=t^2\mathbb F_q[t]/(t^{n+1})\). The normalized restriction is
\[
T=E+M_f,\qquad E=t\frac{d}{dt},\qquad f=\sum_{h=1}^{n-1}f_h t^h,\quad f_h=a_{h+1}/a_1,
\]
where \(M_f\) denotes multiplication by \(f\). All operators descend to the truncated algebra.

**Gauge reduction.** In \(R=\mathbb F_q[t]/(t^{n+1})\), seek a unit \(h\in1+tR\) and a series \(g\in t^p\mathbb F_q[t^p]\) satisfying \(E(h)+fh=hg\). Comparing coefficients degree by degree: if \(p\nmid k\), set \(g_k=0\) and solve uniquely for \(h_k\), since \(k\) is invertible; if \(p\mid k\), choose \(h_k=0\) and solve uniquely for \(g_k\). This determines both series and yields the similarity
\[
M_h^{-1}TM_h=E+M_g\quad\text{on }W.
\]
Group monomials in \(W\) by their exponent modulo \(p\). On the nonzero residue classes, \(E+M_g\) equals a nonzero scalar operator plus a nilpotent multiplication, and is therefore invertible. The zero-residue class has basis \(t^p,t^{2p},\ldots,t^{zp}\) and \(E=0\); multiplication by \(g(t^p)\) on this class has kernel dimension equal to its first nonzero \(t^p\)-degree, capped by \(z\), or \(z\) if it is identically zero there. Thus \(z=0\) gives nullity zero, and otherwise all nullity comes from this explicit truncated multiplication operator.

**The characteristic-\(p\) resonance test.** On the commutative truncated polynomial algebra, for any derivation \(\delta\) and multiplication operator \(M_f\), the identity
\[
(\delta+M_f)^p=\delta^p+M_{\delta^{p-1}(f)+f^p}
\]
holds. For completeness, \([\delta+M_f,M_b]=M_{\delta(b)}\) for every \(b\); taking the \(p\)th adjoint power shows the difference of the two sides commutes with every multiplication operator, hence is itself multiplication. Evaluation on \(1\) gives the claimed multiplier: the expansion \((\delta+M_f)^p(1)\) is the sum over set partitions of \(p\) labelled positions of the products of \(\delta^{|B|-1}(f)\) over blocks \(B\). Rotation of these labels has orbits of size \(p\), except the all-singletons and one-block partitions. In characteristic \(p\) only those two terms survive, yielding \(f^p+\delta^{p-1}(f)\). Here \(E^p=E\) on monomials and \(E^{p-1}(f)=\sum_{p\nmid h}f_h t^h\). Consequently
\[
T^p-T=M_{c},\qquad c(t)=f(t)^p-\sum_{p\mid h}f_h t^h
=\sum_{h\ge1}(f_h^p-f_{ph})t^{ph},
\]
where coefficients outside the truncation are omitted and absent coefficients are interpreted as zero. The same operator after the gauge similarity is multiplication by \(g^p-g\); multiplication operators commute with the conjugating \(M_h\). If \(g\) first has a nonzero term at \(t^{pr}\), then \(g^p-g\) first has a nonzero term at the same degree, with coefficient the negative of that of \(g\). Therefore the first nonzero \(f_h^p-f_{ph}\) with \(1\le h<z\) is exactly the kernel dimension; when all these coefficients vanish the kernel dimension is \(z\). This proves the individual formula.

**Exact multiplicities.** For fixed \(a_1\ne0\), the normalized coefficients \(f_1,\ldots,f_{n-1}\) are independent uniform elements of \(\mathbb F_q\). The equation \(f_h^p=f_{ph}\) uniquely fixes the later coefficient \(f_{ph}\); the indices \(ph\) are distinct and exceed \(h\). Therefore the first \(s\) resonance equations have exactly \(q^{-s}\) of all choices, including when one of the earlier \(f_h\) was itself constrained. For \(1\le v<z\), the probability that the first failure is at \(v\) is \(q^{-(v-1)}(1-q^{-1})\); the probability of no failure before \(z\) is \(q^{-(z-1)}\). Multiplying by \((q-1)q^{n-1}\) gives \(C(v)\). Its mass together with \(B(v)\) is exactly \(q^n\). The invertibility criterion follows: \(a_1=0\) is never invertible, while \(a_1\ne0\) gives zero nullity precisely when \(n<p\).

## Verification
A self-contained Python 3 standard-library script, `verify.py`, constructs finite fields of orders \(2,3,4,5,8,9\), exhaustively enumerates all derivations in 29 dimension-field cases, and compares full nullity histograms against the closed formulas. It checks the derivation identity on representative enumerated maps and independently tests the individual Frobenius-resonance criterion on 96,988 nonzero-leading-coefficient parameter vectors. Running `python3 verify.py` from the extracted package prints `FIELD_CASES 6`, `DIMENSION_CASES 29`, `ENUMERATED_DERIVATIONS 25695`, `INDIVIDUAL_RESONANCE_CASES 96988`, and `VERIFY_OK`. The finite checks corroborate; the proof above supplies the general result.

For \(q=2,n=6\), the nullity distribution from \(v=0\) to \(6\) is \((0,32,16,12,2,1,1)\); the coefficients sum to \(64\). The result also exhibits a sharp phase transition in characteristic \(p\): no derivation can be invertible once \(n\ge p\).

## Relationship to prior work
The 2026 paper of Jumayeva O‘g‘iloy Normurodovna gives the complex-field derivation normal form and studies local derivations and automorphisms of null-filiform Leibniz algebras. This is acknowledged as the starting structure, not claimed here as new. The present theorem supplies a different type of information: the characteristic-dependent, entire finite-field rank and nullity distribution and an explicit Frobenius-resonance criterion for each map. The 2021 paper by Kurdachenko, Semko and Yashchuk studies the algebraic structure of derivations of cyclic Leibniz algebras, but its results as inspected do not state these quantitative finite-field strata. An abstract of a 2026 three-dimensional derivation-algebra classification was compared, but its full preprint could not be read. Hence possible equivalent historical formulations are a residual literature risk.

## Limitations
This is a theorem about the specified null-filiform right Leibniz algebras over finite fields, not all nilpotent Leibniz algebras. The individual resonance test assumes \(a_1\ne0\); the separate formula \(B\) handles \(a_1=0\). Counts are by individual derivations, not derivation-conjugacy or isomorphism classes. Exhaustive computations concern small dimensions only and do not imply the universal claim by themselves.

## References
1. Jumayeva O‘g‘iloy Normurodovna, *Derivations, Automorphisms And Local Derivations of Null-Filiform Leibniz Algebras*, European International Journal of Multidisciplinary Research and Management Studies **6** (2026), 94–100, first published 30 June 2026, DOI: 10.55640/eijmrms-06-06-16. Open full text: https://eipublication.com/index.php/eijmrms/article/download/4968/4501/6483.
2. L. A. Kurdachenko, M. M. Semko and V. S. Yashchuk, *On the structure of the algebra of derivations of cyclic Leibniz algebras*, Algebra and Discrete Mathematics **32** (2021), 241–252, DOI: 10.12958/adm1898. Full text: https://admjournal.luguniv.edu.ua/index.php/adm/article/download/1898/pdf.
3. L. A. Kurdachenko, A. A. Pypka and M. M. Semko, *Derivation Algebras of Three-Dimensional Leibniz Algebras: A Complete Description*, arXiv:2609.24323 (2026), abstract consulted; full text not verified.
