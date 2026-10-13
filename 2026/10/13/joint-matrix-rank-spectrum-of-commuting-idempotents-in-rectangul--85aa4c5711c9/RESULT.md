# Joint matrix-rank spectrum of commuting idempotents in rectangular sandwich semigroups

## Finding

Let \(K=\mathbb F_q\), with \(q\) any prime power. Let \(m,n\ge1\), and let \(S\in M_{n\times m}(K)\) have rank \(0\le r\le\min(m,n)\). Give \(M_{m\times n}(K)\) the associative sandwich product \(X\star Y=XSY\). Put \(\tau=m+n-2r\), and \(G_j(q)=|\operatorname{GL}_j(\mathbb F_q)|=\prod_{i=0}^{j-1}(q^j-q^i)\), including \(G_0(q)=1\). For ordered pairs of sandwich-idempotents that commute under the sandwich product, define

\[
C_{m,n,r,q}(U,V)=\sum_{\substack{X\star X=X,\;Y\star Y=Y\\X\star Y=Y\star X}}U^{\operatorname{rank}X}V^{\operatorname{rank}Y}.
\]

**Theorem (complete joint ordinary-rank enumerator).** In every characteristic and for all parameters as above,

\[
\boxed{C_{m,n,r,q}(U,V)=\sum_{\substack{a,b,c,d\ge0\\a+b+c+d=r}}\frac{G_r(q)}{G_a(q)G_b(q)G_c(q)G_d(q)}\;q^{\tau(b+c+d)}U^{b+d}V^{c+d}.}
\]

The coefficient ratio is an integer: it counts ordered four-term direct-sum decompositions of an \(r\)-space with the prescribed component dimensions. The univariate enumerator of all sandwich-idempotents by ordinary matrix rank is

\[
E_{m,n,r,q}(T)=\sum_{t=0}^{r}{r\brack t}_q q^{t(r-t)+\tau t}T^t.
\]

In particular, \(C_{m,n,r,q}(0,V)=E_{m,n,r,q}(V)\). For \((m,n,r,q)=(3,3,2,2)\), there are exactly \(41\) idempotents and \(409\) commuting ordered idempotent pairs. For \((m,n,r,q)=(3,3,3,2)\), these numbers are \(58\) and \(1012\).

For fixed \(q\) and \(r\ge1\), as \(\tau=m+n-2r\to\infty\), the probability that two independently uniformly sampled sandwich-idempotents commute is asymptotic to \(K_r(q)q^{-\tau r}\), where

\[
K_r(q)=\sum_{b+c+d=r}\frac{G_r(q)}{G_b(q)G_c(q)G_d(q)}.
\]

## Assumptions and scope

All matrix ranks refer to **ordinary linear-map rank**, not semigroup generating rank or sandwich-product rank. The sandwich matrix may be rectangular and singular. The result counts labeled ordered pairs, including \((X,X)\), without dividing by automorphisms or exchanging the pair. The formula also handles \(r=0\): only the zero matrix is an idempotent, and the bivariate polynomial equals \(1\). The simultaneous decomposition underlying the proof works over any field, but numerical counting assumes a finite field. Distinct rank-\(r\) sandwich matrices give isomorphic sandwich semigroups by invertible changes of coordinates.

## Proof

**Step 1: normal form and all idempotents.** If the sandwich matrix has rank \(r\), choose invertible changes of row and column basis that take it to

\[
S=\begin{pmatrix}I_r&0\\0&0\end{pmatrix}\in M_{n\times m}(K).
\]

The induced invertible linear change on \(M_{m\times n}(K)\) preserves the sandwich product and ordinary matrix rank. Write a typical matrix as

\[
X=\begin{pmatrix}P&B\\C&D\end{pmatrix},
\quad P\in M_r(K),\;B\in M_{r\times(n-r)}(K),\;C\in M_{(m-r)\times r}(K).
\]

The equation \(XSX=X\) is *equivalent* to the four equations

\[
P^2=P,\qquad PB=B,\qquad CP=C,\qquad D=CB.
\]

For these data,

\[
X=\begin{pmatrix}I_r\\C\end{pmatrix}P\begin{pmatrix}I_r&B\end{pmatrix},
\]

and its upper-left block is \(P\), so \(\operatorname{rank}X=\operatorname{rank}P\). For a rank-\(t\) projection \(P\), its image and kernel form an ordered complementary decomposition, giving exactly \({r\brack t}_q q^{t(r-t)}\) possibilities. The restrictions \(PB=B\), \(CP=C\) leave \(t(n-r)+t(m-r)=\tau t\) free field entries. This proves the univariate identity and the rank bound \(\operatorname{rank}X\le r\).

**Step 2: commute condition.** Write an independently chosen idempotent as

\[
Y=\begin{pmatrix}Q&E\\F&FE\end{pmatrix},\quad Q^2=Q,\ QE=E,\ FQ=F.
\]

Direct multiplication yields

\[
XSY=\begin{pmatrix}PQ&PE\\CQ&CE\end{pmatrix},\qquad
YSX=\begin{pmatrix}QP&QB\\FP&FB\end{pmatrix}.
\]

Hence commutation is equivalent to

\[
PQ=QP,\qquad PE=QB,\qquad CQ=FP.
\]

Indeed, these equations also force \(CE=FB\), since with \(H=PE=QB\), one has \(CE=CH=CQH=FPH=FH=FB\), using \(CP=C\), \(FQ=F\), and the fact that \(H\) is in both projection images.

**Step 3: simultaneous eigenspaces and exact fibers.** Commuting idempotents \(P,Q\) split the \(r\)-space into four canonical joint eigenspaces

\[
K^r=W_{00}\oplus W_{10}\oplus W_{01}\oplus W_{11},
\]

of dimensions \(a,b,c,d\), because the four operators \((I-P)(I-Q),P(I-Q),(I-P)Q,PQ\) are pairwise orthogonal idempotents summing to \(I\). This holds even in characteristic \(2\). Each ordered direct-sum decomposition of dimensions \((a,b,c,d)\) determines a unique commuting pair \((P,Q)\). The transitive \(\operatorname{GL}_r(K)\)-action has stabilizer \(\operatorname{GL}_a(K)\times\operatorname{GL}_b(K)\times\operatorname{GL}_c(K)\times\operatorname{GL}_d(K)\); therefore there are \(G_r/(G_aG_bG_cG_d)\) such pairs.

For each column of \((B,E)\), the idempotence and commutation equations allow no choice on \(W_{00}\), one arbitrary field value on each of \(W_{10}\) and \(W_{01}\), and one *shared* arbitrary value on \(W_{11}\). Thus there are \(q^{b+c+d}\) possibilities per column and \(q^{(n-r)(b+c+d)}\) for all columns. The same independent row computation for \((C,F)\) yields \(q^{(m-r)(b+c+d)}\) possibilities. The lower-right blocks are already fixed, and Step 2 gives no extra constraint. Multiplication of these independent factors yields \(q^{\tau(b+c+d)}\). Finally \(\operatorname{rank}X=b+d\) and \(\operatorname{rank}Y=c+d\), giving the claimed polynomial.

**Step 4: asymptotic.** The univariate formula is a polynomial in \(q^\tau\) of degree \(r\), with leading coefficient \(1\). The bivariate formula evaluated at \((1,1)\) is also a polynomial in \(q^\tau\) of degree \(r\), whose leading coefficient is exactly \(K_r(q)\) (the terms \(a=0\)). Dividing commuting-pair count by the square of the number of idempotents proves the asserted asymptotic for fixed \(q,r\) and \(\tau\to\infty\).

## Verification

The standalone `checker.py` independently enumerates all \(m\times n\) matrices for ten small cases over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); the \(\mathbb F_4\) multiplication uses a polynomial-basis implementation. It tests \(XSX=X\), \(YSY=Y\), and \(XSY=YSX\) using actual matrices, computes ordinary ranks by field Gaussian elimination, and compares **every joint-rank coefficient** with the closed formula. Its final output is `VERIFY_OK`. For example, it finds \(409\) commuting ordered pairs for \((m,n,r,q)=(3,3,2,2)\) and \(1012\) for \((3,3,3,2)\). These finite checks are tests, not substitutes for the proof for all fields and dimensions.

## Relationship to prior work

Dolinka and East, *Semigroups of rectangular matrices under a sandwich operation* (arXiv:1503.03139, first public March 11, 2015), established the sandwich-semigroup setting and Proposition 7.2's **univariate count of idempotents by ordinary rank**. Their formula agrees with \(E_{m,n,r,q}(T)\) above and is **not** claimed as new. The additional result here classifies **commuting ordered pairs** and their coupled ranks; a one-element idempotent census does not determine this two-element commutation distribution. Their Lemma 6.9 and Sections 6–7 were inspected for comparison.

Dolinka and collaborators' *Sandwich semigroups in locally small categories I: Foundations* (arXiv:1710.01890, first public October 5, 2017) develops the broader categorical context, in particular regularity, Green relations, and generation of idempotent-generated subsemigroups. Its available abstract does not state a joint rank enumerator. The complete text of this particular source was not materially inspected, so an additional implication from its abstract alone cannot be excluded.

Zhdanovskiy's *Homotopes of finite-dimensional algebras* (arXiv:2005.00309, first public May 1, 2020) treats related associative sandwich-multiplication constructions and categorical properties. Its inspected Section 3 concerns homotopes and representations, not the enumerative joint-idempotent question. The comparison rests on the **mathematical statements** and not merely paper titles. Published-result semantic searches for commuting idempotents, simultaneous projection decompositions, Munn rings, and matrix variants revealed no source explicitly containing the stated joint formula. An undiscovered equivalent result remains possible.

## Limitations

The result concerns commuting **pairs of idempotents** under a fixed sandwich product, not arbitrary commuting matrices, joint similarity-conjugacy classification, triples of commuting idempotents, or the full structure of the commuting graph beyond its rank-pair counts. It does not establish priority or independent verification, and a possible older equivalent formulation under variant-semigroup or Munn-ring terminology remains a bibliographic risk. For infinite fields the structural classification persists but the finite-field count is not asserted as a cardinal enumeration.

## References

- I. Dolinka and J. East, *Semigroups of rectangular matrices under a sandwich operation*, arXiv:1503.03139 (v1, 2015-03-11), especially Lemma 6.9 and Proposition 7.2. https://arxiv.org/abs/1503.03139
- I. Dolinka, I. Đurđev, J. East, P. Honyam, K. Sangkhanan, J. Sanwong, and W. Sommanee, *Sandwich semigroups in locally small categories I: Foundations*, arXiv:1710.01890 (v1, 2017-10-05). https://arxiv.org/abs/1710.01890
- I. Zhdanovskiy, *Homotopes of finite-dimensional algebras*, arXiv:2005.00309 (v1, 2020-05-01). https://arxiv.org/abs/2005.00309
