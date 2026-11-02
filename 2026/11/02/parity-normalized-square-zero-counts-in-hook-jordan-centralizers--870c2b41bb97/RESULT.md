# Parity-normalized square-zero counts in hook Jordan centralizers over finite fields

## Finding
Let \(q\) be any prime power, \(n\ge2\), \(r\ge0\), and \(B=J_n(0)\oplus 0_r\) on \(\mathbb F_q^{n+r}\). Write
\[
N_{n,r}(q)=\#\{X\in M_{n+r}(\mathbb F_q):XB=BX,\ X^2=0\}.
\]
For integers \(0\le k\le\lfloor r/2\rfloor\), put
\[
G_{r,k}(q)={r\brack k}_q{r-k\brack k}_q\prod_{i=0}^{k-1}(q^k-q^i),\qquad s=r-2k,
\]
where Gaussian binomial coefficients have their usual subspace-counting meaning and the empty product is \(1\). Define
\[
H_{\mathrm{ev}}(s,q)=\begin{cases}1&s=0,\\q^{2s-1}+(q-1)q^{s-1}&s\ge1,\end{cases}
\quad H_{\mathrm{odd}}(s,q)=q^{2s}\ (s\ge0).
\]
Then the **complete count** is
\[
\boxed{N_{n,r}(q)=q^{\lfloor n/2\rfloor}\sum_{k=0}^{\lfloor r/2\rfloor}G_{r,k}(q)q^{2k}H_{\mathrm{parity}(n)}(r-2k,q).}
\]
In particular the normalized count \(q^{-\lfloor n/2\rfloor}N_{n,r}(q)\) is independent of the size \(n\) within each parity class. For every \(r\ge1\), the odd-parity normalized count is strictly greater than the even-parity normalized count. Their difference is exactly
\[
\sum_{k=0}^{\lfloor (r-1)/2\rfloor}G_{r,k}(q)q^{2k}(q-1)q^{r-2k-1}(q^{r-2k}-1)>0.
\]
For the smallest nontrivial hook tail \(r=1\), this specializes to
\[
N_{2h,1}(q)=q^h(2q-1),\quad N_{2h+1,1}(q)=q^{h+2}\qquad(h\ge1).
\]
The full commuting centralizer contains \(q^{n+2r+r^2}\) matrices, so the formula also gives the exact probability that a uniformly selected matrix commuting with \(B\) is square-zero.

## Assumptions and scope
The field \(\mathbb F_q\) is arbitrary, including characteristic two; \(J_n(0)\) is one nilpotent Jordan block, while \(0_r\) denotes \(r\) singleton nilpotent blocks. For \(r=0\), the formula reduces to \(N_{n,0}(q)=q^{\lfloor n/2\rfloor}\). The restriction \(n\ge2\) is essential for the displayed block-square identity: for \(n=1\), the two summands are identical trivial modules and a different count applies. The result concerns labelled matrices in the full linear centralizer, not similarity classes or conjugacy orbits of the square-zero locus.

## Proof
Set \(R=\mathbb F_q[t]/(t^n)\) and \(W=\mathbb F_q^r\) with \(tW=0\). Identify the Jordan module with \(R\oplus W\), with \(B\) acting as multiplication by \(t\) on \(R\) and zero on \(W\). Its commuting endomorphisms have uniquely specified block data
\[
X=\begin{pmatrix}f(t)&t^{n-1}b\\c&D\end{pmatrix},
\]
where \(f\in R\), \(b\in W^*\), \(c\in W\), \(D\in\operatorname{End}_{\mathbb F_q}(W)\). Here the lower-left map \(R\to W\) sends \(g(t)\) to \(g(0)c\), and \(t^{n-1}b\) maps \(w\) to \(t^{n-1}b(w)\). This proves the centralizer dimension \(n+2r+r^2\).

Write \(a=f(0)\). Multiplication in this block presentation, using \(n\ge2\), gives the **equivalent** equations
\[
f(t)^2+(bc)t^{n-1}=0,\qquad ab+bD=0,\qquad ac+Dc=0,\qquad D^2=0.
\]
The constant term of the first equation gives \(a^2=0\), hence \(a=0\) in every field. The remaining cross conditions are \(bD=0\), \(Dc=0\).

Fix a square-zero \(D\) of rank \(k\), and put \(U=\operatorname{im}D\) and \(K=\ker D\). We have \(U\subset K\), \(\dim U=k\), \(\dim K=r-k\), and \(\dim(K/U)=s=r-2k\). Conditions \(bD=0\), \(Dc=0\) say exactly \(b\in U^\perp\) and \(c\in K\). Their scalar pairing \(bc=b(c)\) factors through the perfect pairing of \((K/U)^*\) and \(K/U\), with \(q^{2k}\) choices of lifts for each pair. The number of rank-\(k\) square-zero matrices \(D\) is \(G_{r,k}(q)\): choose the image \(U\), choose the kernel \(K\supseteq U\), then choose an isomorphism \(W/K\to U\).

If \(n=2h\), any solution \(f\) must have valuation at least \(h\); otherwise its first nonzero squared coefficient has degree below \(n-1\) and cannot cancel the term involving \(bc\). Every such \(f\) satisfies \(f^2=0\), so \(bc=0\), with exactly \(q^h\) choices of \(f\). For \(s\ge1\), the number of pairs \((u,v)\in(\mathbb F_q^s)^*\times\mathbb F_q^s\) with \(u(v)=0\) is
\[
q^s+(q^s-1)q^{s-1}=q^{2s-1}+(q-1)q^{s-1};
\]
for \(s=0\) there is one pair. This gives \(H_{\mathrm{ev}}\).

If \(n=2h+1\), the same lowest-term argument forces \(f=t^h(a_h+a_{h+1}t+\cdots+a_{2h}t^h)\). Its only possibly nonzero square coefficient is \(a_h^2t^{2h}\); the other \(h\) coefficients are arbitrary, contributing \(q^h\). The condition becomes \(a_h^2+bc=0\). For \(s\ge1\), there are \(q^s\) solutions with \(u=0\) (then \(a_h=0\) and \(v\) arbitrary), and \((q^s-1)q^s\) solutions with \(u\ne0\) (choose \(a_h\) arbitrarily and solve one independent linear equation for \(v\)). Thus exactly \(q^{2s}\) triples occur. When \(s=0\), necessarily \(a_h=0\), again yielding one triple. This gives \(H_{\mathrm{odd}}\).

Multiplying by \(G_{r,k}(q)q^{2k}q^h\) and summing over admissible ranks establishes the formula. For positive \(s\), the difference of the two local factors is
\[
q^{2s}-\bigl(q^{2s-1}+(q-1)q^{s-1}\bigr)=(q-1)q^{s-1}(q^s-1)>0.
\]
For \(r\ge1\), the summand \(k=0\) has \(s=r>0\), proving strict parity separation. All steps use finite-field linear algebra and are valid in every characteristic.

## Verification
The companion `verify.py` constructs the centralizing endomorphism matrices directly, multiplies them over each specified finite field (including a genuine four-element extension field), and tests \(X^2=0\) without using the block-square coefficient equations in the theorem. It exhaustively compares the direct counts with the formula for the thirteen triples
\[
(n,r,q)\in\{(2,0,2),(3,0,3),(2,1,2),(3,1,2),(4,1,3),(2,2,2),(3,2,2),(2,2,3),(5,2,2),(3,3,2),(2,1,4),(3,1,4),(2,1,5)\}.
\]
Separately it exhaustively tests the rank-wise square-zero counts \(G_{r,k}(q)\) for \(0\le r\le4\) over \(\mathbb F_2\) and \(0\le r\le3\) over \(\mathbb F_3\), and checks normalization and parity for five field orders. Run with `python verify.py`. The observed output is recorded in `VERIFICATION.md`. Finite tests corroborate but are not an infinite proof; the proof is the algebraic argument above.

## Relationship to prior work
The general theory of centralizers and nilpotent commuting varieties long predates this calculation. Britnell and Wildon [1] examine possible commuting types over finite fields, including hook cases, rather than counting the entire square-zero fiber of a fixed hook centralizer. Ngo, Levy, and Šivic [2] study geometric dimensions and structures of nilpotent commuting varieties; they do not give these finite-field cardinalities. Bogdanić and collaborators [3] classify Jordan types occurring in centralizers with two equal Jordan blocks; this is a different base partition and an existence question. Boij, Iarrobino, and Khatami [4] study geometric stratifications, not the stated finite-field counts. Khatami and Košir [5], closest in the *hook* parameter, classify possible Jordan types for commuting nilpotent matrices in characteristic zero, but do not enumerate labelled square-zero elements over finite fields. These works are credited as structural background; the proposed new claim is the explicit count and strict parity normalization, not the parametrization of all centralizing matrices.

## Limitations
The formula only treats hooks with exactly one block of length at least two. It does not enumerate conjugacy orbits within the square-zero locus, does not cover arbitrary nilpotent partitions, and makes no assertion about joint limits when both the field order and partition change. The date of the motivating source is the first public preprint date of [2], not a publication or revision date. An undiscovered Hall-polynomial or representation-theoretic generalization may imply the formula; novelty is a best-knowledge comparison, not a priority certificate. No independent mathematical audit has been performed.

## References
[1] J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, 2010, https://arxiv.org/abs/1001.0811.

[2] H. Ngo, P. Levy, and K. Šivic, *Commuting Varieties and Cohomological Complexity*, arXiv:2105.07918, first submitted 2021-05-17, https://arxiv.org/abs/2105.07918.

[3] G. Bogdanić, A. Đurić, P. Koljančić, K. Oblak, and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425, https://arxiv.org/abs/2212.08425.

[4] M. Boij, A. Iarrobino, and L. Khatami, *Jordan Type stratification of spaces of commuting nilpotent matrices*, arXiv:2409.13553, https://arxiv.org/abs/2409.13553.

[5] L. Khatami and T. Košir, *Jordan types commuting with a hook partition*, arXiv:2605.27692, https://arxiv.org/abs/2605.27692. This later paper is a comparison, not the motivating 2021 source.
