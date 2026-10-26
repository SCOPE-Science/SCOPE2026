# Ideal-dimension polynomial of complete-bipartite graphical Lie algebras over finite fields

## Finding
For all integers \(a,b\geq1\) and every prime power \(q\), the dimension enumerator of **all** \(\mathbb F_q\)-linear Lie ideals of the graphical Lie algebra associated with \(K_{a,b}\), with each edge given a distinct central basis vector, is the following explicit finite sum. Put \(M=ab\), \(k(r,s)=rb+as-rs\), \(g_q(h)=|\mathrm{GL}_h(\mathbb F_q)|\), and let \(\genfrac{[}{]}{0pt}{}{n}{j}_q\) be a Gaussian binomial coefficient:

\[
\begin{aligned}
I_{a,b,q}(T)
&=\sum_{J\triangleleft L_{a,b}(\mathbb F_q)}T^{\dim_{\mathbb F_q}J}\\
&=\sum_{r=0}^{a}\sum_{s=0}^{b}\sum_{h=0}^{\min(r,s)}
\genfrac{[}{]}{0pt}{}{a}{r}_q
\genfrac{[}{]}{0pt}{}{b}{s}_q
\genfrac{[}{]}{0pt}{}{r}{h}_q
\genfrac{[}{]}{0pt}{}{s}{h}_q g_q(h)
\sum_{d=k(r,s)}^{M}
\genfrac{[}{]}{0pt}{}{M-k(r,s)}{d-k(r,s)}_q
q^{(r+s-h)(M-d)}T^{r+s-h+d}.
\end{aligned}
\]

In particular, the formula records the entire dimension distribution, not only the total ideal count; it includes nongraded ideals and works in characteristic two. A geometric classification of the summands is part of the proof.

## Assumptions and scope
Let \(A\cong\mathbb F_q^a\), \(B\cong\mathbb F_q^b\), \(Z=A\otimes_{\mathbb F_q}B\), and define \(L=L_{a,b}(\mathbb F_q)=A\oplus B\oplus Z\) with
\[
[(u,v,z),(u',v',z')]=u\otimes v'-u'\otimes v.
\]
All brackets involving \(Z\) are zero. This is an alternating bracket, including in characteristic two, and the Jacobi identity holds because every bracket is central. The dimension is \(a+b+ab\). Each of the \(ab\) edges of \(K_{a,b}\) labels its own generator of \(Z\). We count arbitrary linear subspaces \(J\subseteq L\) closed under bracketing with all of \(L\). We use \(g_q(0)=1\), and \(\genfrac{[}{]}{0pt}{}{n}{j}_q=0\) when \(j\notin[0,n]\).

## Proof
**1. Ideals over a projection pair.** Write \(V=A\oplus B\) and let \(\pi:L\to V\) be the canonical projection. For any ideal \(J\), define \(W=\pi(J)\leq V\), \(D=J\cap Z\leq Z\). Because \(Z\) is central, the ideal condition is exactly
\[
[W,V]\subseteq D.
\]
Conversely, given subspaces \(W\leq V\) and \(D\leq Z\) satisfying this inclusion, ideals with these data are in bijection with linear maps \(f:W\to Z/D\): their images under \(L\to L/D\cong V\oplus (Z/D)\) are the graphs of \(f\). There are precisely \(q^{(\dim W)(M-\dim D)}\) such ideals. Their dimensions are \(\dim W+\dim D\). No assumption of gradedness or of split ideals is imposed.

**2. Commutator space from projected ranks.** Set \(A'=\pi_A(W)\), \(B'=\pi_B(W)\), with dimensions \(r\) and \(s\). Bracketing elements of \(W\) with elements of \(0\oplus B\) gives \(A'\otimes B\), and with \(A\oplus0\) gives \(A\otimes B'\). Therefore
\[
[W,V]=A'\otimes B+A\otimes B'.
\]
Choosing complements to \(A'\leq A\) and \(B'\leq B\) proves that the intersection of these two tensor subspaces is exactly \(A'\otimes B'\). Hence
\[
\dim[W,V]=rb+as-rs=k(r,s).
\]
There are \(\genfrac{[}{]}{0pt}{}{M-k(r,s)}{d-k(r,s)}_q\) choices of a \(d\)-dimensional subspace \(D\) containing this fixed commutator space.

**3. Counting projections by the vector-space Goursat argument.** There are \(\genfrac{[}{]}{0pt}{}{a}{r}_q\) choices of \(A'\) and \(\genfrac{[}{]}{0pt}{}{b}{s}_q\) choices of \(B'\). A subspace \(W\leq A'\oplus B'\) that projects surjectively to both factors has kernels \(A_0=\{u\in A':(u,0)\in W\}\) and \(B_0=\{v\in B':(0,v)\in W\}\). The quotient projections identify \(A'/A_0\cong B'/B_0\). Write their common dimension as \(h\). Then \(0\leq h\leq\min(r,s)\), the two kernels have codimensions \(h\), and \(\dim W=r+s-h\). Conversely, the kernels and an isomorphism between the two \(h\)-dimensional quotients uniquely construct \(W\). Consequently the number of \(W\) with fixed \(A',B',h\) is
\[
\genfrac{[}{]}{0pt}{}{r}{h}_q
\genfrac{[}{]}{0pt}{}{s}{h}_q
\lvert\mathrm{GL}_h(\mathbb F_q)\rvert.
\]
Here \(\lvert\mathrm{GL}_h(\mathbb F_q)\rvert=\prod_{j=0}^{h-1}(q^h-q^j)\), with the empty product equal to one. No cases are omitted, including zero projections and \(h=0\).

**4. Assemble without overcounting.** Each ideal has unique \((W,D,f)\), unique projected subspaces \((A',B')\), and a unique quotient dimension \(h\). Multiply the independent numbers of choices from Steps 1–3 and sum over \(r,s,h,d\). Since \(\dim J=r+s-h+d\), placing \(T^{r+s-h+d}\) gives the displayed identity. The proof is valid over every finite field and needs no characteristic restriction.

## Verification
The accompanying standalone Python 3 script `verify.py` computes the displayed formula by Gaussian-binomial arithmetic and **independently** enumerates all reduced-row-echelon-form subspaces of the ambient Lie algebra, checking the ideal property on all basis brackets. All six tested cases agree: \((a,b,q)=(1,1,2),(1,1,3),(1,2,2),(1,2,3),(1,3,2),(2,2,2)\). The last case has dimension distribution
\[
(1,15,35,39,55,51,35,15,1).
\]
The checks range from \(16\) to \(417199\) examined ambient subspaces; they are finite tests, **not** proof of the universal result. The proof above supplies the all-parameter argument. Additional immediate checks are \(I_{a,b,q}(0)=1\), the leading coefficient is one, the coefficient of \(T\) is \(\genfrac{[}{]}{0pt}{}{ab}{1}_q\), and that of \(T^{a+b+ab-1}\) is \(\genfrac{[}{]}{0pt}{}{a+b}{1}_q\), since proper maximal ideals are hyperplanes containing the derived algebra.

## Relationship to prior work
Carnevale–Schein–Voll (2019), Section 5.3, explicitly study the **same abstract family** as the free class-two product \(\mathfrak g_{a,b}\) of two abelian Lie rings. Their principal result is the local ideal-zeta function, aggregating all finite-index ideals over compact discrete valuation rings by index; Section 4 develops finer lattice-projection methods. That is strong and directly relevant prior structural coverage. The present statement isolates the distinct, rank-refined enumeration of **ideals in the reduction over \(\mathbb F_q\)**, including each elementary-quotient dimension. A univariate local index zeta function does not itself distinguish elementary-quotient ideals from other index-equal lattices. Their projection machinery is nevertheless closely related, and the possibility that its specialized identities recover this displayed formula is a specific priority risk rather than a claimed independence result.

Godoy Molina–Lagos (2023), Sections 2, 3 and 5.2, study labeled-graph Lie algebras, certain graph-induced ideals, and graded derivations for the all-distinct-label complete-bipartite case. The dimension distribution of **all** field-linear ideals is not stated in those inspected sections. Bauer–Schein (2022) study ideal zeta functions of amalgamated class-two objects over discrete valuation rings; this differs from a direct dimension enumerator over a finite field. Carnevale–Schein–Voll also cite earlier work of Paajanen giving the local ideal zeta of the rank-two-by-rank-two case; its Theorem 11.1 and accompanying example were inspected and concern a local p-adic normal-subgroup zeta function, not the displayed finite-field rank polynomial. The universal finite-field proof here uses the central-extension graph parametrization together with the Goursat count.

## Limitations
This formula covers the specified complete-bipartite, all-distinct-edge-label class-two family only; it does not classify ideals for arbitrary graphs, repeated edge labels, integral lattices, or local ideal-zeta functions. Published p-adic ideal-zeta and lattice-projection results on the identical Lie-ring family, including the Paajanen rank-two-by-rank-two precedent, create a substantive overlap risk: the finite-field rank refinement may be derivable from that more general apparatus even though it is not its stated rank-count theorem. Exhaustive checks cover only the parameter cases listed above. No external proof certification is claimed.

## References
1. A. Carnevale, M. M. Schein and C. Voll, *Generalized Igusa functions and ideal growth in nilpotent Lie rings*, arXiv:1903.03090 (first posted 2019-03-07), especially Sections 4 and 5.3. https://arxiv.org/abs/1903.03090
2. M. Godoy Molina and D. Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272 (first posted 2023-08-01), especially Sections 2, 3 and 5.2. https://arxiv.org/abs/2308.00272
3. P. Paajanen, *Geometric structure of class two nilpotent groups and subgroup growth*, arXiv:0802.1796 (first posted 2008-02-13), cited for the rank-two-by-rank-two local ideal-zeta case in Reference 1; the abstract and Section 11, Theorem 11.1, were inspected; the remainder was not read. https://arxiv.org/abs/0802.1796
4. T. Bauer and M. M. Schein, *Ideal growth in amalgamated powers of nilpotent rings of class two and zeta functions of quiver representations*, arXiv:2202.10865 (first posted 2022-02-22), Sections 1.1–1.2. https://arxiv.org/abs/2202.10865
